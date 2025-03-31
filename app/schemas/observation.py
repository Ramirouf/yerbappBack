from datetime import date, time, datetime
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID


class ObservationBase(BaseModel):
    date: date
    time: time
    latitude: float
    longitude: float
    severity_level: int = Field(..., ge=0, le=5)
    temperature: float
    pressure: float
    humidity: float = Field(..., ge=0, le=100)
    observations: str
    source: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "date": "2023-03-15",
                    "time": "14:30:00",
                    "latitude": -31.4201,
                    "longitude": -64.1888,
                    "severity_level": 3,
                    "temperature": 25.4,
                    "pressure": 1013,
                    "humidity": 75,
                    "observations": "Mild discoloration on leaves.",
                    "source": "Field Survey",
                }
            ]
        }
    }


class ObservationCreate(ObservationBase):
    user_id: UUID

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "date": "2023-03-15",
                    "time": "14:30:00",
                    "latitude": -31.4201,
                    "longitude": -64.1888,
                    "severity_level": 3,
                    "temperature": 25.4,
                    "pressure": 1013,
                    "humidity": 75,
                    "observations": "Mild discoloration on leaves.",
                    "source": "Field Survey",
                    "user_id": "123e4567-e89b-12d3-a456-426614174000",
                }
            ]
        }
    }


class ObservationRead(ObservationBase):
    id: UUID
    user_id: UUID
    registered_at: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "987e6543-e21b-12d3-a456-426614174111",
                    "date": "2023-03-15",
                    "time": "14:30:00",
                    "latitude": -31.4201,
                    "longitude": -64.1888,
                    "severity_level": 3,
                    "temperature": 25.4,
                    "pressure": 1013,
                    "humidity": 75,
                    "observations": "Mild discoloration on leaves.",
                    "source": "Field Survey",
                    "user_id": "123e4567-e89b-12d3-a456-426614174000",
                }
            ]
        }
    }


class ObservationUpdate(BaseModel):
    date: Optional[date] = None
    time: Optional[time] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    severity_level: Optional[int] = Field(None, ge=0, le=5)
    temperature: Optional[float] = None
    pressure: Optional[float] = None
    humidity: Optional[float] = Field(None, ge=0, le=100)
    observations: Optional[str] = None
    source: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "date": "2023-03-16",
                    "time": "15:00:00",
                    "latitude": -31.4201,
                    "longitude": -64.1888,
                    "severity_level": 4,
                    "temperature": 26.0,
                    "pressure": 1012,
                    "humidity": 80,
                    "observations": "Increased severity noted.",
                    "source": "Follow-up Survey",
                }
            ]
        }
    }


class ObservationDelete(BaseModel):
    detail: str

    class Config:
        schema_extra = {"example": {"detail": "Observation deleted successfully."}}
