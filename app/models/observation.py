import uuid
from uuid import UUID
from sqlmodel import SQLModel, Field
from datetime import date, time, datetime, timezone
from typing import Optional
from sqlalchemy import Column, DateTime
import tzlocal


class Observation(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    date: date
    time: time
    latitude: float
    longitude: float
    severity_level: int = Field(ge=0, le=5)
    temperature: float
    pressure: float
    humidity: float = Field(ge=0, le=100)
    observations: str
    source: str
    user_id: UUID
    registered_at: datetime = Field(
        default_factory=lambda: datetime.now(tzlocal.get_localzone()),
        sa_column=Column(DateTime(timezone=True)),
    )
