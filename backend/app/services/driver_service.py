from sqlalchemy.orm import Session

from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverUpdate


class DriverService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Driver).all()

    @staticmethod
    def get_by_id(driver_id: int, db: Session):
        return db.query(Driver).filter(
            Driver.id == driver_id
        ).first()

    @staticmethod
    def create(driver: DriverCreate, db: Session):

        existing = db.query(Driver).filter(
            Driver.license_number == driver.license_number
        ).first()

        if existing:
            raise ValueError(
                "License Number already exists."
            )

        db_driver = Driver(**driver.model_dump())

        db.add(db_driver)
        db.commit()
        db.refresh(db_driver)

        return db_driver

    @staticmethod
    def update(
        driver_id: int,
        driver: DriverUpdate,
        db: Session
    ):

        db_driver = DriverService.get_by_id(driver_id, db)

        if not db_driver:
            return None

        update_data = driver.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_driver, key, value)

        db.commit()
        db.refresh(db_driver)

        return db_driver

    @staticmethod
    def delete(driver_id: int, db: Session):

        db_driver = DriverService.get_by_id(driver_id, db)

        if not db_driver:
            return None

        db.delete(db_driver)
        db.commit()

        return {"message": "Driver deleted successfully."}