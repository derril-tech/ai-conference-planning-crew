from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class EventBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    city: str = Field(..., min_length=1, max_length=100)
    country: str = Field(..., min_length=1, max_length=100)
    venue_name: Optional[str] = None
    venue_address: Optional[str] = None
    expected_attendees: int = Field(default=0, ge=0)
    max_attendees: Optional[int] = Field(None, ge=0)
    budget_total: float = Field(default=0.0, ge=0)
    brief_json: Optional[Dict[str, Any]] = None

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    city: Optional[str] = Field(None, min_length=1, max_length=100)
    country: Optional[str] = Field(None, min_length=1, max_length=100)
    venue_name: Optional[str] = None
    venue_address: Optional[str] = None
    expected_attendees: Optional[int] = Field(None, ge=0)
    max_attendees: Optional[int] = Field(None, ge=0)
    budget_total: Optional[float] = Field(None, ge=0)
    budget_spent: Optional[float] = Field(None, ge=0)
    status: Optional[str] = Field(None, pattern="^(planning|active|completed|cancelled)$")
    brief_json: Optional[Dict[str, Any]] = None

class EventInDB(EventBase):
    id: str
    status: str
    budget_spent: float
    created_by: str
    tenant_id: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Event(EventBase):
    id: str
    status: str
    budget_spent: float
    created_by: str
    tenant_id: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class EventList(BaseModel):
    events: list[Event]
    total: int
    page: int
    page_size: int
