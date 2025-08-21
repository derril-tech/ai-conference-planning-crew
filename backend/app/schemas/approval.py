from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class ApprovalBase(BaseModel):
    event_id: str
    agent_id: str
    type: str = Field(..., pattern="^(venue_selection|speaker_confirmation|budget_approval|sponsorship_approval|marketing_approval|logistics_approval|risk_approval)$")
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    priority: str = Field(default="normal", pattern="^(low|normal|high|urgent)$")
    expires_at: Optional[datetime] = None

class ApprovalCreate(ApprovalBase):
    pass

class ApprovalUpdate(BaseModel):
    status: Optional[str] = Field(None, pattern="^(pending|approved|rejected)$")
    comments: Optional[str] = None
    approved_at: Optional[datetime] = None

class ApprovalInDB(ApprovalBase):
    id: str
    status: str
    approver_id: Optional[str] = None
    comments: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    approved_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Approval(ApprovalBase):
    id: str
    status: str
    approver_id: Optional[str] = None
    comments: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    approved_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ApprovalList(BaseModel):
    approvals: list[Approval]
    total: int
    page: int
    page_size: int
