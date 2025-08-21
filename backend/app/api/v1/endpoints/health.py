from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.redis import get_redis

router = APIRouter()

@router.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "conference-planning-crew-api",
        "version": "1.0.0"
    }

@router.get("/db")
async def database_health(db: AsyncSession = Depends(get_db)):
    """Database health check"""
    try:
        # Simple query to test database connection
        result = await db.execute("SELECT 1")
        await result.fetchone()
        return {"database": "healthy"}
    except Exception as e:
        return {"database": "unhealthy", "error": str(e)}

@router.get("/redis")
async def redis_health(redis = Depends(get_redis)):
    """Redis health check"""
    try:
        await redis.ping()
        return {"redis": "healthy"}
    except Exception as e:
        return {"redis": "unhealthy", "error": str(e)}
