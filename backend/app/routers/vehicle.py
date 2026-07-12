from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.vehicle import (
    VehicleCreate,
    VehicleUpdate,
    VehicleResponse,
)
from app.services.vehicle_service import VehicleService

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)


@router.get("/", response_model=list[VehicleResponse])
def get_all_vehicles(db: Session = Depends(get_db)):
    return VehicleService.get_all(db)


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = VehicleService.get_by_id(vehicle_id, db)

    if not vehicle:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicle


@router.post("/", response_model=VehicleResponse)
def create_vehicle(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db)
):
    return VehicleService.create(vehicle, db)


@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(
    vehicle_id: int,
    vehicle: VehicleUpdate,
    db: Session = Depends(get_db)
):
    updated = VehicleService.update(
        vehicle_id,
        vehicle,
        db
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return updated


@router.delete("/{vehicle_id}")
def delete_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db)
):
    deleted = VehicleService.delete(
        vehicle_id,
        db
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return deleted