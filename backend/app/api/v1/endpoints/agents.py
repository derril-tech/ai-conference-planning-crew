from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from typing import Optional
from datetime import datetime
from app.core.database import get_db
from app.core.auth import get_current_active_user
from app.models.user import User
from app.models.agent import Agent
from app.models.event import Event
from app.schemas.agent import AgentCreate, AgentUpdate, Agent as AgentSchema, AgentList
import uuid

router = APIRouter()

@router.get("/", response_model=AgentList)
async def get_agents(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    event_id: Optional[str] = Query(None),
    status_filter: Optional[str] = Query(None, alias="status"),
    type_filter: Optional[str] = Query(None, alias="type"),
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Get all agents with pagination and filtering."""
    # Build query
    query = select(Agent).join(Event).where(Event.tenant_id == current_user.tenant_id)
    
    # Apply filters
    if event_id:
        query = query.where(Agent.event_id == event_id)
    if status_filter:
        query = query.where(Agent.status == status_filter)
    if type_filter:
        query = query.where(Agent.type == type_filter)
    
    # Get total count
    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar()
    
    # Get paginated results
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    agents = result.scalars().all()
    
    return AgentList(
        agents=agents,
        total=total,
        page=skip // limit + 1,
        page_size=limit
    )

@router.post("/", response_model=AgentSchema)
async def create_agent(
    agent: AgentCreate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new agent."""
    # Verify event belongs to user's tenant
    result = await db.execute(
        select(Event).where(
            Event.id == agent.event_id,
            Event.tenant_id == current_user.tenant_id
        )
    )
    event = result.scalar_one_or_none()
    
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    db_agent = Agent(
        id=str(uuid.uuid4()),
        **agent.model_dump()
    )
    
    db.add(db_agent)
    await db.commit()
    await db.refresh(db_agent)
    
    return db_agent

@router.get("/{agent_id}", response_model=AgentSchema)
async def get_agent(
    agent_id: str,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Get a specific agent."""
    result = await db.execute(
        select(Agent).join(Event).where(
            Agent.id == agent_id,
            Event.tenant_id == current_user.tenant_id
        )
    )
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    
    return agent

@router.put("/{agent_id}", response_model=AgentSchema)
async def update_agent(
    agent_id: str,
    agent_update: AgentUpdate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Update an agent."""
    result = await db.execute(
        select(Agent).join(Event).where(
            Agent.id == agent_id,
            Event.tenant_id == current_user.tenant_id
        )
    )
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    
    # Update fields
    update_data = agent_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(agent, field, value)
    
    await db.commit()
    await db.refresh(agent)
    
    return agent

@router.post("/{agent_id}/start")
async def start_agent(
    agent_id: str,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Start an agent workflow."""
    result = await db.execute(
        select(Agent).join(Event).where(
            Agent.id == agent_id,
            Event.tenant_id == current_user.tenant_id
        )
    )
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    
    if agent.status == "running":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Agent is already running"
        )
    
    # Update agent status
    agent.status = "running"
    agent.started_at = datetime.utcnow()
    agent.progress = 0
    
    await db.commit()
    await db.refresh(agent)
    
    # TODO: Trigger agent workflow
    # This would integrate with LangGraph and the AI agent system
    
    return {"message": "Agent started successfully", "agent": agent}
