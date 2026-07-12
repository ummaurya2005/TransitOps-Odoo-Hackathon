from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleUpdate


class VehicleService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Vehicle).all()

    @staticmethod
    def get_by_id(vehicle_id: int, db: Session):
        return db.query(Vehicle).filter(
            Vehicle.id == vehicle_id
        ).first()

    @staticmethod
    def create(vehicle: VehicleCreate, db: Session):

        existing = db.query(Vehicle).filter(
            Vehicle.registration_number == vehicle.registration_number
        ).first()

        if existing:
            raise ValueError(
                "Registration Number already exists."
            )

        db_vehicle = Vehicle(**vehicle.model_dump())

        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)

        return db_vehicle

    @staticmethod
    def update(
        vehicle_id: int,
        vehicle: VehicleUpdate,
        db: Session
    ):

        db_vehicle = VehicleService.get_by_id(vehicle_id, db)

        if not db_vehicle:
            return None

        update_data = vehicle.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_vehicle, key, value)

        db.commit()
        db.refresh(db_vehicle)

        return db_vehicle

    @staticmethod
    def delete(vehicle_id: int, db: Session):

        db_vehicle = VehicleService.get_by_id(vehicle_id, db)

        if not db_vehicle:
            return None

        db.delete(db_vehicle)
        db.commit()

        return {"message": "Vehicle deleted successfully."}