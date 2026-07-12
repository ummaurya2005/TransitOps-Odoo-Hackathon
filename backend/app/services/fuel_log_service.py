from sqlalchemy.orm import Session

from app.models.fuel_log import FuelLog
from app.schemas.fuel_log import (
    FuelLogCreate,
    FuelLogUpdate,
)


class FuelLogService:

    @staticmethod
    def get_all(db: Session):
        return db.query(FuelLog).all()

    @staticmethod
    def get_by_id(log_id: int, db: Session):
        return db.query(FuelLog).filter(
            FuelLog.id == log_id
        ).first()

    @staticmethod
    def create(data: FuelLogCreate, db: Session):

        fuel = FuelLog(**data.model_dump())

        db.add(fuel)
        db.commit()
        db.refresh(fuel)

        return fuel

    @staticmethod
    def update(log_id: int, data: FuelLogUpdate, db: Session):

        fuel = FuelLogService.get_by_id(log_id, db)

        if not fuel:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(fuel, key, value)

        db.commit()
        db.refresh(fuel)

        return fuel

    @staticmethod
    def delete(log_id: int, db: Session):

        fuel = FuelLogService.get_by_id(log_id, db)

        if not fuel:
            return None

        db.delete(fuel)
        db.commit()

        return {"message": "Fuel log deleted successfully."}