from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, default="user")  # admin, user, manager
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    tenant_id = Column(String, index=True, nullable=True)  # For multi-tenancy
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    events = relationship("Event", back_populates="created_by_user")
    approvals = relationship("Approval", back_populates="approver")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"
