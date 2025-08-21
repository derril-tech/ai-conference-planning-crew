from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class AgentBase(BaseModel):
    event_id: str
    type: str = Field(..., pattern="^(venue_scout|speaker_outreach|sponsorship_manager|budget_controller|marketing_ops|attendee_experience|logistics_travel|risk_compliance)$")
    current_task: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class AgentCreate(AgentBase):
    pass

class AgentUpdate(BaseModel):
    status: Optional[str] = Field(None, pattern="^(idle|running|completed|error|waiting_approval)$")
    progress: Optional[int] = Field(None, ge=0, le=100)
    current_task: Optional[str] = None
    decisions: Optional[List[Dict[str, Any]]] = None
    metadata: Optional[Dict[str, Any]] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

class AgentInDB(AgentBase):
    id: str
    status: str
    progress: int
    decisions: List[Dict[str, Any]]
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Agent(AgentBase):
    id: str
    status: str
    progress: int
    decisions: List[Dict[str, Any]]
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class AgentList(BaseModel):
    agents: list[Agent]
    total: int
    page: int
    page_size: int
