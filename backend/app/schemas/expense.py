from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ExpenseBase(BaseModel):
    vehicle_id: int
    expense_type: str
    amount: float
    description: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    expense_type: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseResponse(ExpenseBase):
    id: int

    model_config = ConfigDict(from_attributes=True)