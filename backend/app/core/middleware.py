"""
Middleware Module for OrchestrateX

This module contains middleware for security, logging, rate limiting, and CORS.
"""

import time
import logging
from typing import Callable
from fastapi import Request, Response, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import redis.asyncio as redis
from .config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SecurityMiddleware(BaseHTTPMiddleware):
    """Security middleware for request validation and protection."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Add security headers
        response = await call_next(request)
        
        # Security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"
        
        return response

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate limiting middleware using Redis."""
    
    def __init__(self, app, redis_client: redis.Redis):
        super().__init__(app)
        self.redis = redis_client
        self.rate_limit_requests = 100  # requests per window
        self.rate_limit_window = 60  # seconds
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Get client IP
        client_ip = request.client.host
        
        # Create rate limit key
        rate_limit_key = f"rate_limit:{client_ip}"
        
        try:
            # Check current request count
            current_requests = await self.redis.get(rate_limit_key)
            
            if current_requests is None:
                # First request in window
                await self.redis.setex(rate_limit_key, self.rate_limit_window, 1)
            else:
                current_count = int(current_requests)
                if current_count >= self.rate_limit_requests:
                    raise HTTPException(
                        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                        detail="Rate limit exceeded. Please try again later."
                    )
                
                # Increment request count
                await self.redis.incr(rate_limit_key)
            
            response = await call_next(request)
            
            # Add rate limit headers
            remaining_requests = self.rate_limit_requests - int(await self.redis.get(rate_limit_key) or 0)
            response.headers["X-RateLimit-Limit"] = str(self.rate_limit_requests)
            response.headers["X-RateLimit-Remaining"] = str(max(0, remaining_requests))
            response.headers["X-RateLimit-Reset"] = str(int(time.time()) + self.rate_limit_window)
            
            return response
            
        except redis.RedisError:
            # If Redis is unavailable, continue without rate limiting
            logger.warning("Redis unavailable, skipping rate limiting")
            return await call_next(request)

class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging middleware for request/response tracking."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Log request start
        start_time = time.time()
        
        # Log request details
        logger.info(
            f"Request: {request.method} {request.url.path} "
            f"from {request.client.host} "
            f"User-Agent: {request.headers.get('user-agent', 'Unknown')}"
        )
        
        # Process request
        try:
            response = await call_next(request)
            
            # Calculate processing time
            process_time = time.time() - start_time
            
            # Log response details
            logger.info(
                f"Response: {response.status_code} "
                f"took {process_time:.4f}s "
                f"for {request.method} {request.url.path}"
            )
            
            # Add processing time header
            response.headers["X-Process-Time"] = str(process_time)
            
            return response
            
        except Exception as e:
            # Log errors
            process_time = time.time() - start_time
            logger.error(
                f"Error processing {request.method} {request.url.path}: {str(e)} "
                f"took {process_time:.4f}s"
            )
            raise

class AuditMiddleware(BaseHTTPMiddleware):
    """Audit middleware for tracking sensitive operations."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Track sensitive operations
        sensitive_paths = [
            "/api/v1/auth/login",
            "/api/v1/auth/register",
            "/api/v1/users",
            "/api/v1/events",
            "/api/v1/agents"
        ]
        
        is_sensitive = any(path in request.url.path for path in sensitive_paths)
        
        if is_sensitive:
            logger.info(
                f"AUDIT: {request.method} {request.url.path} "
                f"from {request.client.host} "
                f"at {time.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        
        response = await call_next(request)
        
        # Log sensitive responses
        if is_sensitive and response.status_code in [200, 201, 400, 401, 403]:
            logger.info(
                f"AUDIT: {request.method} {request.url.path} "
                f"returned {response.status_code}"
            )
        
        return response

class DataValidationMiddleware(BaseHTTPMiddleware):
    """Data validation middleware for input sanitization."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Validate content type for POST/PUT requests
        if request.method in ["POST", "PUT", "PATCH"]:
            content_type = request.headers.get("content-type", "")
            
            if not content_type.startswith("application/json"):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Content-Type must be application/json"
                )
        
        # Check for suspicious patterns in request
        user_agent = request.headers.get("user-agent", "").lower()
        suspicious_patterns = [
            "sqlmap", "nikto", "nmap", "w3af", "burp", "zap",
            "sql injection", "xss", "csrf"
        ]
        
        if any(pattern in user_agent for pattern in suspicious_patterns):
            logger.warning(f"Suspicious User-Agent detected: {user_agent}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )
        
        return await call_next(request)

def setup_middleware(app, redis_client: redis.Redis):
    """Setup all middleware for the FastAPI application."""
    
    # Trusted Host middleware
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS
    )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["*"],
    )
    
    # Custom middleware (order matters)
    app.add_middleware(SecurityMiddleware)
    app.add_middleware(DataValidationMiddleware)
    app.add_middleware(RateLimitMiddleware, redis_client=redis_client)
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(AuditMiddleware)
    
    logger.info("Middleware setup completed")

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """Error handling middleware for consistent error responses."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        try:
            return await call_next(request)
        except HTTPException:
            # Re-raise HTTP exceptions as they are already properly formatted
            raise
        except Exception as e:
            # Log unexpected errors
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            
            # Return generic error response
            return Response(
                content='{"detail": "Internal server error"}',
                status_code=500,
                media_type="application/json"
            )
