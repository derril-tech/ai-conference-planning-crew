from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Venue(Base):
    __tablename__ = "venues"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    capacity = Column(Integer, nullable=True)
    price_per_day = Column(Float, nullable=True)
    contact_person = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)
    amenities = Column(JSON, nullable=True)  # List of available amenities
    status = Column(String, default="proposed")  # proposed, selected, rejected, booked
    notes = Column(Text, nullable=True)
    metadata = Column(JSON, nullable=True)  # Additional venue data
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    event = relationship("Event", back_populates="venues")

    def __repr__(self):
        return f"<Venue(id={self.id}, name={self.name}, status={self.status})>"
