from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Speaker(Base):
    __tablename__ = "speakers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    company = Column(String, nullable=True)
    title = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    expertise = Column(JSON, nullable=True)  # List of expertise areas
    session_title = Column(String, nullable=True)
    session_description = Column(Text, nullable=True)
    session_duration = Column(Integer, nullable=True)  # in minutes
    fee = Column(Float, nullable=True)
    status = Column(String, default="contacted")  # contacted, confirmed, declined, pending
    travel_requirements = Column(JSON, nullable=True)
    dietary_restrictions = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    event = relationship("Event", back_populates="speakers")

    def __repr__(self):
        return f"<Speaker(id={self.id}, name={self.name}, status={self.status})>"
