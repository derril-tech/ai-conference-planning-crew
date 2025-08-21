from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class AgentActivity(Base):
    __tablename__ = "agent_activities"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    agent_id = Column(String, nullable=False, index=True)
    event_id = Column(String, nullable=False, index=True)
    type = Column(String, nullable=False)  # info, success, warning, error
    message = Column(Text, nullable=False)
    data = Column(JSON, nullable=True)  # Additional activity data
    requires_action = Column(Boolean, default=False)
    action_taken = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    agent = relationship("Agent", back_populates="activities")

    def __repr__(self):
        return f"<AgentActivity(id={self.id}, type={self.type}, message={self.message[:50]}...)>"
