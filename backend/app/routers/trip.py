from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.trip import (
    TripCreate,
    TripUpdate,
    TripResponse,
)
from app.services.trip_service import TripService

router = APIRouter(
    prefix="/trips",
    tags=["Trips"]
)


@router.get("/", response_model=list[TripResponse])
def get_all_trips(db: Session = Depends(get_db)):
    return TripService.get_all(db)


@router.get("/{trip_id}", response_model=TripResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = TripService.get_by_id(trip_id, db)

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return trip


@router.post("/", response_model=TripResponse)
def create_trip(
    trip: TripCreate,
    db: Session = Depends(get_db)
):
    return TripService.create(trip, db)


@router.put("/{trip_id}", response_model=TripResponse)
def update_trip(
    trip_id: int,
    trip: TripUpdate,
    db: Session = Depends(get_db)
):
    updated = TripService.update(
        trip_id,
        trip,
        db
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return updated


@router.delete("/{trip_id}")
def delete_trip(
    trip_id: int,
    db: Session = Depends(get_db)
):
    deleted = TripService.delete(
        trip_id,
        db
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return deleted


@router.patch("/{trip_id}/dispatch", response_model=TripResponse)
def dispatch_trip(
    trip_id: int,
    db: Session = Depends(get_db)
):
    trip = TripService.dispatch(
        trip_id,
        db
    )

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return trip


@router.patch("/{trip_id}/complete", response_model=TripResponse)
def complete_trip(
    trip_id: int,
    db: Session = Depends(get_db)
):
    trip = TripService.complete(
        trip_id,
        db
    )

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return trip


@router.patch("/{trip_id}/cancel", response_model=TripResponse)
def cancel_trip(
    trip_id: int,
    db: Session = Depends(get_db)
):
    trip = TripService.cancel(
        trip_id,
        db
    )

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return trip