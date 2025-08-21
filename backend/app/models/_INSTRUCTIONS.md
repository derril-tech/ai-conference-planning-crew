# Database Models - TODO

## Overview
SQLAlchemy 2.0 async models for the Conference Planning Crew database. All models should use async/await patterns and include proper relationships.

## Models to Implement

### 1. Base Models
- `base.py` - Base model with common fields (id, created_at, updated_at)
- `user.py` - User model with authentication fields
- `tenant.py` - Multi-tenancy support

### 2. Event Models
- `event.py` - Main event model
- `venue.py` - Venue and room models
- `track.py` - Conference tracks
- `session.py` - Individual sessions

### 3. People Models
- `speaker.py` - Speaker information
- `attendee.py` - Attendee profiles
- `sponsor.py` - Sponsor information

### 4. Business Models
- `ticket.py` - Ticket types and pricing
- `payment.py` - Payment records
- `budget.py` - Budget tracking
- `contract.py` - Contract management

### 5. AI Agent Models
- `agent.py` - Agent definitions and status
- `run.py` - Agent execution runs
- `approval.py` - Human-in-the-loop approvals
- `task.py` - Task management

### 6. Knowledge Models
- `knowledge_source.py` - Document sources
- `chunk.py` - RAG document chunks
- `audit_log.py` - Audit trail

## Database Schema Requirements
- Use PostgreSQL with pgvector extension
- UUID primary keys
- Proper foreign key relationships
- Indexes for performance
- JSONB fields for flexible data

## Example Model Structure
```python
from sqlalchemy import Column, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid
from datetime import datetime

class Event(Base):
    __tablename__ = "events"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    brief_json = Column(JSON)
    city = Column(String)
    venue_pref = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String, default="planning")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    tenant = relationship("Tenant", back_populates="events")
    venues = relationship("Venue", back_populates="event")
    speakers = relationship("Speaker", back_populates="event")
    sponsors = relationship("Sponsor", back_populates="event")
```

## TODO Checklist
- [ ] Create base model with common fields
- [ ] Implement user and tenant models
- [ ] Create event and venue models
- [ ] Add speaker and sponsor models
- [ ] Implement business models (tickets, payments, budget)
- [ ] Create AI agent models
- [ ] Add knowledge and audit models
- [ ] Set up database migrations with Alembic
- [ ] Add proper indexes and constraints
- [ ] Create seed data for development
