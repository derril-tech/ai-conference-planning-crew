"""
Security Module for OrchestrateX

This module handles authentication, authorization, and security utilities.
"""

import os
import secrets
from datetime import datetime, timedelta
from typing import Optional, Union, Dict, Any
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..core.config import settings
from ..core.database import get_db
from ..models.user import User
from ..models.event import Event

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT token security
security = HTTPBearer()

# Token configuration
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

class SecurityManager:
    """Manages security operations including authentication and authorization."""
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash."""
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        """Generate password hash."""
        return pwd_context.hash(password)
    
    @staticmethod
    def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
        """Create JWT access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def create_refresh_token(data: Dict[str, Any]) -> str:
        """Create JWT refresh token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire, "type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def verify_token(token: str) -> Dict[str, Any]:
        """Verify and decode JWT token."""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    @staticmethod
    def generate_secure_token() -> str:
        """Generate a secure random token."""
        return secrets.token_urlsafe(32)

class RoleBasedAccessControl:
    """Role-based access control system."""
    
    # Role hierarchy (higher roles inherit permissions from lower roles)
    ROLE_HIERARCHY = {
        "super_admin": ["super_admin", "admin", "manager", "user"],
        "admin": ["admin", "manager", "user"],
        "manager": ["manager", "user"],
        "user": ["user"]
    }
    
    # Permission definitions
    PERMISSIONS = {
        "user": [
            "read_own_profile",
            "update_own_profile",
            "read_own_events",
            "create_events",
            "update_own_events",
            "delete_own_events"
        ],
        "manager": [
            "read_team_events",
            "update_team_events",
            "manage_team_users",
            "view_analytics",
            "manage_agents"
        ],
        "admin": [
            "manage_all_events",
            "manage_all_users",
            "manage_tenants",
            "view_system_analytics",
            "manage_system_settings"
        ],
        "super_admin": [
            "manage_system",
            "view_all_data",
            "manage_security_settings"
        ]
    }
    
    @staticmethod
    def has_permission(user_role: str, required_permission: str) -> bool:
        """Check if user has required permission."""
        if user_role not in RoleBasedAccessControl.ROLE_HIERARCHY:
            return False
        
        user_permissions = []
        for role in RoleBasedAccessControl.ROLE_HIERARCHY[user_role]:
            if role in RoleBasedAccessControl.PERMISSIONS:
                user_permissions.extend(RoleBasedAccessControl.PERMISSIONS[role])
        
        return required_permission in user_permissions
    
    @staticmethod
    def get_user_permissions(user_role: str) -> list:
        """Get all permissions for a user role."""
        if user_role not in RoleBasedAccessControl.ROLE_HIERARCHY:
            return []
        
        permissions = []
        for role in RoleBasedAccessControl.ROLE_HIERARCHY[user_role]:
            if role in RoleBasedAccessControl.PERMISSIONS:
                permissions.extend(RoleBasedAccessControl.PERMISSIONS[role])
        
        return list(set(permissions))  # Remove duplicates

class DataProtection:
    """Data protection and privacy utilities."""
    
    @staticmethod
    def mask_sensitive_data(data: str, mask_char: str = "*") -> str:
        """Mask sensitive data like emails and phone numbers."""
        if "@" in data:
            # Mask email
            parts = data.split("@")
            if len(parts) == 2:
                username = parts[0]
                domain = parts[1]
                if len(username) > 2:
                    masked_username = username[:2] + mask_char * (len(username) - 2)
                else:
                    masked_username = mask_char * len(username)
                return f"{masked_username}@{domain}"
        
        # Mask phone numbers
        if len(data) >= 10 and data.replace("+", "").replace("-", "").replace(" ", "").isdigit():
            return data[:3] + mask_char * (len(data) - 6) + data[-3:]
        
        return data
    
    @staticmethod
    def sanitize_input(input_data: str) -> str:
        """Sanitize user input to prevent injection attacks."""
        # Remove potentially dangerous characters
        dangerous_chars = ["<", ">", "'", '"', "&", ";", "|", "`", "$", "(", ")", "{", "}"]
        sanitized = input_data
        for char in dangerous_chars:
            sanitized = sanitized.replace(char, "")
        return sanitized.strip()
    
    @staticmethod
    def validate_password_strength(password: str) -> Dict[str, Any]:
        """Validate password strength."""
        errors = []
        warnings = []
        
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")
        elif len(password) < 12:
            warnings.append("Consider using a longer password (12+ characters)")
        
        if not any(c.isupper() for c in password):
            errors.append("Password must contain at least one uppercase letter")
        
        if not any(c.islower() for c in password):
            errors.append("Password must contain at least one lowercase letter")
        
        if not any(c.isdigit() for c in password):
            errors.append("Password must contain at least one number")
        
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            errors.append("Password must contain at least one special character")
        
        return {
            "is_valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "strength_score": max(0, 10 - len(errors) * 2)
        }

# Dependency functions
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Get current authenticated user."""
    token = credentials.credentials
    payload = SecurityManager.verify_token(token)
    user_id: str = payload.get("sub")
    
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Get user from database
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Get current active user."""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def require_permission(permission: str):
    """Decorator to require specific permission."""
    def permission_checker(current_user: User = Depends(get_current_user)):
        if not RoleBasedAccessControl.has_permission(current_user.role, permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return current_user
    return permission_checker

def require_role(role: str):
    """Decorator to require specific role."""
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != role and not RoleBasedAccessControl.has_permission(current_user.role, f"role_{role}"):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient role privileges"
            )
        return current_user
    return role_checker

async def check_event_access(
    event_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Event:
    """Check if user has access to specific event."""
    # Super admins and admins have access to all events
    if current_user.role in ["super_admin", "admin"]:
        result = await db.execute(select(Event).where(Event.id == event_id))
        event = result.scalar_one_or_none()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event
    
    # Managers can access events in their tenant
    if current_user.role == "manager":
        result = await db.execute(
            select(Event).where(
                Event.id == event_id,
                Event.tenant_id == current_user.tenant_id
            )
        )
        event = result.scalar_one_or_none()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found or access denied")
        return event
    
    # Regular users can only access their own events
    result = await db.execute(
        select(Event).where(
            Event.id == event_id,
            Event.created_by == current_user.id
        )
    )
    event = result.scalar_one_or_none()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found or access denied")
    
    return event
