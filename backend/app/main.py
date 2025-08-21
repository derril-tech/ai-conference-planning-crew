from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

from app.core.config import settings
from app.core.middleware import setup_middleware
from app.api.v1.api import api_router
from app.core.database import engine
from app.core.redis import redis_client

app = FastAPI(
    title="Conference Planning Crew API",
    description="Multi-agent AI conference planning platform API",
    version="1.0.0",
    docs_url="/docs" if settings.ENVIRONMENT != "production" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT != "production" else None,
)

# Setup security and compliance middleware
setup_middleware(app, redis_client)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Conference Planning Crew API",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "connected" if engine else "disconnected",
        "redis": "connected" if redis_client else "disconnected"
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True if settings.ENVIRONMENT == "development" else False,
    )
