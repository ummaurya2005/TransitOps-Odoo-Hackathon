from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TripBase(BaseModel):
    source: str
    destination: str
    vehicle_id: int
    driver_id: int
    cargo_weight: float
    planned_distance: float
    trip_date: Optional[date] = None
    status: str = "Draft"


class TripCreate(TripBase):
    pass


class TripUpdate(BaseModel):
    source: Optional[str] = None
    destination: Optional[str] = None
    vehicle_id: Optional[int] = None
    driver_id: Optional[int] = None
    cargo_weight: Optional[float] = None
    planned_distance: Optional[float] = None
    trip_date: Optional[date] = None
    status: Optional[str] = None


class TripResponse(TripBase):
    id: int

    model_config = ConfigDict(from_attributes=True)