from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Agent(Base):
    __tablename__ = "agents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String, nullable=False, index=True)
    type = Column(String, nullable=False)  # venue_scout, speaker_outreach, etc.
    status = Column(String, default="idle")  # idle, running, completed, error, waiting_approval
    progress = Column(Integer, default=0)  # 0-100
    current_task = Column(Text, nullable=True)
    decisions = Column(JSON, default=list)  # Store decisions as JSON array
    metadata = Column(JSON, nullable=True)  # Additional agent-specific data
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    event = relationship("Event", back_populates="agents")
    activities = relationship("AgentActivity", back_populates="agent")

    def __repr__(self):
        return f"<Agent(id={self.id}, type={self.type}, status={self.status})>"
