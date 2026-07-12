from sqlalchemy.orm import Session

from app.models.maintenance import Maintenance
from app.models.vehicle import Vehicle
from app.schemas.maintenance import (
    MaintenanceCreate,
    MaintenanceUpdate,
)


class MaintenanceService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Maintenance).all()

    @staticmethod
    def get_by_id(record_id: int, db: Session):
        return db.query(Maintenance).filter(
            Maintenance.id == record_id
        ).first()

    @staticmethod
    def create(data: MaintenanceCreate, db: Session):

        vehicle = db.query(Vehicle).filter(
            Vehicle.id == data.vehicle_id
        ).first()

        if not vehicle:
            raise ValueError("Vehicle not found.")

        vehicle.status = "In Shop"

        record = Maintenance(**data.model_dump())

        db.add(record)
        db.commit()
        db.refresh(record)

        return record

    @staticmethod
    def update(record_id: int, data: MaintenanceUpdate, db: Session):

        record = MaintenanceService.get_by_id(record_id, db)

        if not record:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(record, key, value)

        db.commit()
        db.refresh(record)

        return record

    @staticmethod
    def complete(record_id: int, db: Session):

        record = MaintenanceService.get_by_id(record_id, db)

        if not record:
            return None

        record.complete()

        db.commit()
        db.refresh(record)

        return record

    @staticmethod
    def delete(record_id: int, db: Session):

        record = MaintenanceService.get_by_id(record_id, db)

        if not record:
            return None

        db.delete(record)
        db.commit()

        return {"message": "Maintenance record deleted."}