from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.maintenance import (
    MaintenanceCreate,
    MaintenanceUpdate,
    MaintenanceResponse,
)
from app.services.maintenance_service import MaintenanceService

router = APIRouter(
    prefix="/maintenance",
    tags=["Maintenance"]
)


@router.get("/", response_model=list[MaintenanceResponse])
def get_all(db: Session = Depends(get_db)):
    return MaintenanceService.get_all(db)


@router.post("/", response_model=MaintenanceResponse)
def create(
    data: MaintenanceCreate,
    db: Session = Depends(get_db),
):
    return MaintenanceService.create(data, db)


@router.put("/{record_id}", response_model=MaintenanceResponse)
def update(
    record_id: int,
    data: MaintenanceUpdate,
    db: Session = Depends(get_db),
):
    record = MaintenanceService.update(record_id, data, db)

    if not record:
        raise HTTPException(404, "Record not found")

    return record


@router.patch("/{record_id}/complete", response_model=MaintenanceResponse)
def complete(
    record_id: int,
    db: Session = Depends(get_db),
):
    record = MaintenanceService.complete(record_id, db)

    if not record:
        raise HTTPException(404, "Record not found")

    return record


@router.delete("/{record_id}")
def delete(
    record_id: int,
    db: Session = Depends(get_db),
):
    record = MaintenanceService.delete(record_id, db)

    if not record:
        raise HTTPException(404, "Record not found")

    return record