from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    status = Column(String, default="planning")  # planning, active, completed, cancelled
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    venue_name = Column(String, nullable=True)
    venue_address = Column(Text, nullable=True)
    expected_attendees = Column(Integer, default=0)
    max_attendees = Column(Integer, nullable=True)
    budget_total = Column(Float, default=0.0)
    budget_spent = Column(Float, default=0.0)
    brief_json = Column(JSON, nullable=True)  # Store event brief as JSON
    created_by = Column(String, nullable=False, index=True)
    tenant_id = Column(String, index=True, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    created_by_user = relationship("User", back_populates="events")
    venues = relationship("Venue", back_populates="event")
    speakers = relationship("Speaker", back_populates="event")
    sponsors = relationship("Sponsor", back_populates="event")
    agents = relationship("Agent", back_populates="event")
    approvals = relationship("Approval", back_populates="event")

    def __repr__(self):
        return f"<Event(id={self.id}, name={self.name}, status={self.status})>"
