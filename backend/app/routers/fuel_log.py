from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.fuel_log import (
    FuelLogCreate,
    FuelLogUpdate,
    FuelLogResponse,
)
from app.services.fuel_log_service import FuelLogService

router = APIRouter(
    prefix="/fuel-logs",
    tags=["Fuel Logs"]
)


@router.get("/", response_model=list[FuelLogResponse])
def get_all(db: Session = Depends(get_db)):
    return FuelLogService.get_all(db)


@router.post("/", response_model=FuelLogResponse)
def create(
    data: FuelLogCreate,
    db: Session = Depends(get_db),
):
    return FuelLogService.create(data, db)


@router.put("/{log_id}", response_model=FuelLogResponse)
def update(
    log_id: int,
    data: FuelLogUpdate,
    db: Session = Depends(get_db),
):
    fuel = FuelLogService.update(log_id, data, db)

    if not fuel:
        raise HTTPException(404, detail="Fuel log not found")

    return fuel


@router.delete("/{log_id}")
def delete(
    log_id: int,
    db: Session = Depends(get_db),
):
    fuel = FuelLogService.delete(log_id, db)

    if not fuel:
        raise HTTPException(404, detail="Fuel log not found")

    return fuel