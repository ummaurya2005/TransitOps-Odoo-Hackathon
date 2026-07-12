from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.models.vehicle import Vehicle
from app.models.driver import Driver
from app.schemas.trip import TripCreate, TripUpdate


class TripService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Trip).all()

    @staticmethod
    def get_by_id(trip_id: int, db: Session):
        return db.query(Trip).filter(
            Trip.id == trip_id
        ).first()

    @staticmethod
    def create(trip: TripCreate, db: Session):

        vehicle = db.query(Vehicle).filter(
            Vehicle.id == trip.vehicle_id
        ).first()

        if not vehicle:
            raise ValueError("Vehicle not found.")

        driver = db.query(Driver).filter(
            Driver.id == trip.driver_id
        ).first()

        if not driver:
            raise ValueError("Driver not found.")

        if vehicle.status != "Available":
            raise ValueError("Vehicle is not available.")

        if driver.status != "Available":
            raise ValueError("Driver is not available.")

        if trip.cargo_weight > vehicle.max_load_capacity:
            raise ValueError(
                "Cargo exceeds vehicle capacity."
            )

        db_trip = Trip(**trip.model_dump())

        db.add(db_trip)
        db.commit()
        db.refresh(db_trip)

        return db_trip

    @staticmethod
    def update(
        trip_id: int,
        trip: TripUpdate,
        db: Session
    ):

        db_trip = TripService.get_by_id(
            trip_id,
            db
        )

        if not db_trip:
            return None

        update_data = trip.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_trip, key, value)

        db.commit()
        db.refresh(db_trip)

        return db_trip

    @staticmethod
    def delete(
        trip_id: int,
        db: Session
    ):

        db_trip = TripService.get_by_id(
            trip_id,
            db
        )

        if not db_trip:
            return None

        db.delete(db_trip)
        db.commit()

        return {
            "message": "Trip deleted successfully."
        }

    @staticmethod
    def dispatch(
        trip_id: int,
        db: Session
    ):

        trip = TripService.get_by_id(
            trip_id,
            db
        )

        if not trip:
            return None

        trip.dispatch()

        db.commit()
        db.refresh(trip)

        return trip

    @staticmethod
    def complete(
        trip_id: int,
        db: Session
    ):

        trip = TripService.get_by_id(
            trip_id,
            db
        )

        if not trip:
            return None

        trip.complete()

        db.commit()
        db.refresh(trip)

        return trip

    @staticmethod
    def cancel(
        trip_id: int,
        db: Session
    ):

        trip = TripService.get_by_id(
            trip_id,
            db
        )

        if not trip:
            return None

        trip.cancel()

        db.commit()
        db.refresh(trip)

        return trip