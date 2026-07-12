from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.driver import Driver
from app.models.expense import Expense
from app.models.fuel_log import FuelLog
from app.models.trip import Trip
from app.models.vehicle import Vehicle


class ReportService:

    @staticmethod
    def vehicle_report(db: Session):

        return db.query(Vehicle).all()

    @staticmethod
    def driver_report(db: Session):

        return db.query(Driver).all()

    @staticmethod
    def trip_report(db: Session):

        return db.query(Trip).all()

    @staticmethod
    def fuel_report(db: Session):

        return db.query(FuelLog).all()

    @staticmethod
    def expense_report(db: Session):

        return db.query(Expense).all()

    @staticmethod
    def total_operational_cost(db: Session):

        fuel = db.query(func.sum(FuelLog.cost)).scalar() or 0

        expense = db.query(func.sum(Expense.amount)).scalar() or 0

        return {
            "fuel_cost": fuel,
            "expense_cost": expense,
            "total_cost": fuel + expense
        }