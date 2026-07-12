from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FuelLogBase(BaseModel):
    vehicle_id: int
    liters: float
    cost: float
    fuel_date: Optional[date] = None


class FuelLogCreate(FuelLogBase):
    pass


class FuelLogUpdate(BaseModel):
    liters: Optional[float] = None
    cost: Optional[float] = None
    fuel_date: Optional[date] = None


class FuelLogResponse(FuelLogBase):
    id: int

    model_config = ConfigDict(from_attributes=True)