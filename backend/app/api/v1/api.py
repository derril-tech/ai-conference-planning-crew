from fastapi import APIRouter

from app.api.v1.endpoints import auth, events, venues, speakers, sponsors, agents, health, compliance

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(venues.router, prefix="/venues", tags=["venues"])
api_router.include_router(speakers.router, prefix="/speakers", tags=["speakers"])
api_router.include_router(sponsors.router, prefix="/sponsors", tags=["sponsors"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(compliance.router, prefix="/compliance", tags=["compliance"])
