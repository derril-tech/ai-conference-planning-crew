from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Approval(Base):
    __tablename__ = "approvals"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String, nullable=False, index=True)
    agent_id = Column(String, nullable=False, index=True)
    approver_id = Column(String, nullable=True, index=True)  # User who approved/rejected
    type = Column(String, nullable=False)  # venue_selection, speaker_confirmation, budget_approval, etc.
    status = Column(String, default="pending")  # pending, approved, rejected
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    data = Column(JSON, nullable=True)  # The data that needs approval
    comments = Column(Text, nullable=True)  # Comments from approver
    priority = Column(String, default="normal")  # low, normal, high, urgent
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    approved_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    event = relationship("Event", back_populates="approvals")
    agent = relationship("Agent")
    approver = relationship("User", back_populates="approvals")

    def __repr__(self):
        return f"<Approval(id={self.id}, type={self.type}, status={self.status})>"
