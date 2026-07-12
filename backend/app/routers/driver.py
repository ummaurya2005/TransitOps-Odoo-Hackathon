from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.driver import (
    DriverCreate,
    DriverUpdate,
    DriverResponse,
)
from app.services.driver_service import DriverService

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"]
)


@router.get("/", response_model=list[DriverResponse])
def get_all_drivers(db: Session = Depends(get_db)):
    return DriverService.get_all(db)


@router.get("/{driver_id}", response_model=DriverResponse)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = DriverService.get_by_id(driver_id, db)

    if not driver:
        raise HTTPException(
            status_code=404,
            detail="Driver not found"
        )

    return driver


@router.post("/", response_model=DriverResponse)
def create_driver(
    driver: DriverCreate,
    db: Session = Depends(get_db)
):
    return DriverService.create(driver, db)


@router.put("/{driver_id}", response_model=DriverResponse)
def update_driver(
    driver_id: int,
    driver: DriverUpdate,
    db: Session = Depends(get_db)
):
    updated = DriverService.update(
        driver_id,
        driver,
        db
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Driver not found"
        )

    return updated


@router.delete("/{driver_id}")
def delete_driver(
    driver_id: int,
    db: Session = Depends(get_db)
):
    deleted = DriverService.delete(
        driver_id,
        db
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Driver not found"
        )

    return deleted