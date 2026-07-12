from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class VehicleBase(BaseModel):
    registration_number: str
    vehicle_name: str
    vehicle_type: str
    max_load_capacity: float
    odometer: float = 0.0
    acquisition_cost: float
    acquisition_date: Optional[date] = None
    status: str = "Available"
    notes: Optional[str] = None


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(BaseModel):
    registration_number: Optional[str] = None
    vehicle_name: Optional[str] = None
    vehicle_type: Optional[str] = None
    max_load_capacity: Optional[float] = None
    odometer: Optional[float] = None
    acquisition_cost: Optional[float] = None
    acquisition_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class VehicleResponse(VehicleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)