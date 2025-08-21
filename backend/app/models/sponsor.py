from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Sponsor(Base):
    __tablename__ = "sponsors"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False)
    contact_person = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)
    company_website = Column(String, nullable=True)
    sponsorship_level = Column(String, nullable=True)  # platinum, gold, silver, bronze
    amount = Column(Float, nullable=True)
    benefits = Column(JSON, nullable=True)  # List of sponsorship benefits
    status = Column(String, default="contacted")  # contacted, interested, confirmed, declined
    contract_signed = Column(Boolean, default=False)
    payment_received = Column(Boolean, default=False)
    logo_url = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    event = relationship("Event", back_populates="sponsors")

    def __repr__(self):
        return f"<Sponsor(id={self.id}, name={self.name}, status={self.status})>"
