# Pydantic Schemas - TODO

## Overview
This directory contains Pydantic v2 schemas for request/response validation in the Conference Planning Crew API. Schemas ensure data integrity and provide automatic API documentation.

## Schema Categories

### 1. Base Schemas
**Status**: TODO
- `base.py` - Base schema classes
- `common.py` - Common field types and validators
- `pagination.py` - Pagination schemas

### 2. Authentication Schemas
**Status**: TODO
- `auth.py` - Login, register, token schemas
- `user.py` - User profile and management schemas

### 3. Event Schemas
**Status**: TODO
- `event.py` - Event CRUD schemas
- `event_brief.py` - Event brief schemas
- `event_status.py` - Event status and workflow schemas

### 4. Venue Schemas
**Status**: TODO
- `venue.py` - Venue CRUD schemas
- `room.py` - Room and facility schemas
- `cost_card.py` - Pricing and cost schemas

### 5. Speaker Schemas
**Status**: TODO
- `speaker.py` - Speaker CRUD schemas
- `availability.py` - Availability and scheduling schemas
- `contract.py` - Speaker contract schemas

### 6. Sponsor Schemas
**Status**: TODO
- `sponsor.py` - Sponsor CRUD schemas
- `package.py` - Sponsorship package schemas
- `invoice.py` - Invoice and payment schemas

### 7. Agent Schemas
**Status**: TODO
- `agent.py` - Agent status and configuration schemas
- `decision.py` - Agent decision schemas
- `workflow.py` - Workflow state schemas

### 8. Budget Schemas
**Status**: TODO
- `budget.py` - Budget management schemas
- `expense.py` - Expense tracking schemas
- `revenue.py` - Revenue tracking schemas

## Schema Guidelines

### Base Schema Structure
```python
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
import uuid

class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            uuid.UUID: lambda v: str(v)
        }
    )
```

### Request Schemas
```python
class EventCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Event name")
    description: Optional[str] = Field(None, max_length=1000, description="Event description")
    city: str = Field(..., min_length=1, max_length=100, description="Event city")
    start_date: datetime = Field(..., description="Event start date")
    end_date: datetime = Field(..., description="Event end date")
    expected_attendees: int = Field(..., gt=0, le=10000, description="Expected number of attendees")
    budget: float = Field(..., gt=0, description="Event budget in USD")
    
    @field_validator('end_date')
    @classmethod
    def validate_end_date(cls, v, info):
        if 'start_date' in info.data and v <= info.data['start_date']:
            raise ValueError('End date must be after start date')
        return v
```

### Response Schemas
```python
class EventResponse(BaseSchema):
    id: uuid.UUID = Field(..., description="Event ID")
    name: str = Field(..., description="Event name")
    description: Optional[str] = Field(None, description="Event description")
    city: str = Field(..., description="Event city")
    start_date: datetime = Field(..., description="Event start date")
    end_date: datetime = Field(..., description="Event end date")
    status: str = Field(..., description="Event status")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
```

### Update Schemas
```python
class EventUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    city: Optional[str] = Field(None, min_length=1, max_length=100)
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = Field(None, pattern="^(planning|active|completed|cancelled)$")
```

## Validation Rules

### String Fields
- Use `min_length` and `max_length` for string constraints
- Use `pattern` for regex validation
- Use `description` for API documentation

### Numeric Fields
- Use `gt` (greater than) and `lt` (less than) for ranges
- Use `ge` (greater than or equal) and `le` (less than or equal)
- Use `multiple_of` for divisibility constraints

### Date Fields
- Use `datetime` for timestamps
- Use `date` for date-only fields
- Implement custom validators for date logic

### Complex Validation
```python
from pydantic import field_validator, model_validator

class EventBrief(BaseModel):
    target_audience: str = Field(..., min_length=10, max_length=500)
    expected_attendees: int = Field(..., gt=0, le=10000)
    theme: str = Field(..., min_length=5, max_length=200)
    objectives: List[str] = Field(..., min_items=1, max_items=10)
    constraints: List[str] = Field(default_factory=list)
    
    @field_validator('objectives')
    @classmethod
    def validate_objectives(cls, v):
        if len(v) > 10:
            raise ValueError('Maximum 10 objectives allowed')
        return [obj.strip() for obj in v if obj.strip()]
    
    @model_validator(mode='after')
    def validate_brief(self):
        if len(self.objectives) == 0:
            raise ValueError('At least one objective is required')
        return self
```

## Error Handling

### Custom Error Messages
```python
class EventCreate(BaseModel):
    name: str = Field(
        ..., 
        min_length=1, 
        max_length=200,
        description="Event name",
        json_schema_extra={
            "error_messages": {
                "min_length": "Event name cannot be empty",
                "max_length": "Event name cannot exceed 200 characters"
            }
        }
    )
```

### Validation Error Responses
```python
from fastapi import HTTPException
from pydantic import ValidationError

async def create_event(event_data: EventCreate):
    try:
        # Validation happens automatically
        event = EventCreate(**event_data)
        return event
    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Validation error",
                "errors": e.errors()
            }
        )
```

## API Documentation

### Schema Examples
```python
class EventCreate(BaseModel):
    name: str = Field(..., description="Event name")
    description: Optional[str] = Field(None, description="Event description")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Tech Conference 2024",
                "description": "Annual technology conference",
                "city": "San Francisco",
                "start_date": "2024-06-15T09:00:00Z",
                "end_date": "2024-06-17T18:00:00Z",
                "expected_attendees": 500,
                "budget": 75000.0
            }
        }
    )
```

## Implementation Priority

### High Priority (Phase 1)
1. **Base Schemas** - Foundation schemas
2. **Authentication** - User management
3. **Event Schemas** - Core business logic
4. **Common Schemas** - Shared types

### Medium Priority (Phase 2)
1. **Venue Schemas** - Venue management
2. **Speaker Schemas** - Speaker management
3. **Agent Schemas** - AI agent interface
4. **Budget Schemas** - Financial tracking

### Low Priority (Phase 3)
1. **Advanced Validation** - Complex business rules
2. **Nested Schemas** - Complex data structures
3. **Custom Types** - Domain-specific types

## Testing

### Schema Validation Tests
```python
import pytest
from pydantic import ValidationError
from app.schemas.event import EventCreate

def test_valid_event_create():
    data = {
        "name": "Test Event",
        "city": "Test City",
        "start_date": "2024-06-15T09:00:00Z",
        "end_date": "2024-06-17T18:00:00Z",
        "expected_attendees": 100,
        "budget": 10000.0
    }
    event = EventCreate(**data)
    assert event.name == "Test Event"

def test_invalid_event_create():
    with pytest.raises(ValidationError):
        EventCreate(
            name="",  # Invalid: empty name
            city="Test City",
            start_date="2024-06-15T09:00:00Z",
            end_date="2024-06-17T18:00:00Z",
            expected_attendees=100,
            budget=10000.0
        )
```

## TODO Checklist

### Base Schemas
- [ ] Create base schema class
- [ ] Create common field types
- [ ] Create pagination schemas
- [ ] Create error response schemas

### Authentication Schemas
- [ ] Create login request/response schemas
- [ ] Create register request/response schemas
- [ ] Create token schemas
- [ ] Create user profile schemas

### Event Schemas
- [ ] Create event CRUD schemas
- [ ] Create event brief schemas
- [ ] Create event status schemas
- [ ] Create event filter schemas

### Venue Schemas
- [ ] Create venue CRUD schemas
- [ ] Create room schemas
- [ ] Create cost card schemas
- [ ] Create venue search schemas

### Speaker Schemas
- [ ] Create speaker CRUD schemas
- [ ] Create availability schemas
- [ ] Create contract schemas
- [ ] Create speaker search schemas

### Agent Schemas
- [ ] Create agent status schemas
- [ ] Create decision schemas
- [ ] Create workflow schemas
- [ ] Create approval schemas

### Testing
- [ ] Write validation tests for all schemas
- [ ] Test error handling
- [ ] Test API documentation generation
- [ ] Test schema serialization/deserialization
