from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from typing import Optional
from app.core.database import get_db
from app.core.auth import get_current_active_user
from app.models.user import User
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate, Event as EventSchema, EventList
import uuid

router = APIRouter()

@router.get("/", response_model=EventList)
async def get_events(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    city_filter: Optional[str] = Query(None, alias="city"),
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Get all events with pagination and filtering."""
    # Build query
    query = select(Event).where(Event.tenant_id == current_user.tenant_id)
    
    # Apply filters
    if status_filter:
        query = query.where(Event.status == status_filter)
    if city_filter:
        query = query.where(Event.city.ilike(f"%{city_filter}%"))
    
    # Get total count
    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar()
    
    # Get paginated results
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    events = result.scalars().all()
    
    return EventList(
        events=events,
        total=total,
        page=skip // limit + 1,
        page_size=limit
    )

@router.post("/", response_model=EventSchema)
async def create_event(
    event: EventCreate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new event."""
    db_event = Event(
        id=str(uuid.uuid4()),
        **event.model_dump(),
        created_by=current_user.id,
        tenant_id=current_user.tenant_id
    )
    
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    
    return db_event

@router.get("/{event_id}", response_model=EventSchema)
async def get_event(
    event_id: str,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Get a specific event."""
    result = await db.execute(
        select(Event).where(
            Event.id == event_id,
            Event.tenant_id == current_user.tenant_id
        )
    )
    event = result.scalar_one_or_none()
    
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    return event

@router.put("/{event_id}", response_model=EventSchema)
async def update_event(
    event_id: str,
    event_update: EventUpdate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Update an event."""
    result = await db.execute(
        select(Event).where(
            Event.id == event_id,
            Event.tenant_id == current_user.tenant_id
        )
    )
    event = result.scalar_one_or_none()
    
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    # Update fields
    update_data = event_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(event, field, value)
    
    await db.commit()
    await db.refresh(event)
    
    return event

@router.delete("/{event_id}")
async def delete_event(
    event_id: str,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete an event."""
    result = await db.execute(
        select(Event).where(
            Event.id == event_id,
            Event.tenant_id == current_user.tenant_id
        )
    )
    event = result.scalar_one_or_none()
    
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    await db.delete(event)
    await db.commit()
    
    return {"message": "Event deleted successfully"}
