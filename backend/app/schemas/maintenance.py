from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MaintenanceBase(BaseModel):
    vehicle_id: int
    maintenance_type: str
    description: Optional[str] = None
    cost: float = 0.0
    maintenance_date: Optional[date] = None
    status: str = "Open"


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceUpdate(BaseModel):
    maintenance_type: Optional[str] = None
    description: Optional[str] = None
    cost: Optional[float] = None
    maintenance_date: Optional[date] = None
    status: Optional[str] = None


class MaintenanceResponse(MaintenanceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)