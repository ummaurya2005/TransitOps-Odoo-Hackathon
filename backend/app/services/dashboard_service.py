from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.driver import Driver
from app.models.expense import Expense
from app.models.fuel_log import FuelLog
from app.models.maintenance import Maintenance
from app.models.trip import Trip
from app.models.vehicle import Vehicle


class DashboardService:

    @staticmethod
    def get_dashboard(db: Session):

        total_vehicles = db.query(Vehicle).count()

        available_vehicles = db.query(Vehicle).filter(
            Vehicle.status == "Available"
        ).count()

        on_trip = db.query(Vehicle).filter(
            Vehicle.status == "On Trip"
        ).count()

        in_shop = db.query(Vehicle).filter(
            Vehicle.status == "In Shop"
        ).count()

        retired = db.query(Vehicle).filter(
            Vehicle.status == "Retired"
        ).count()

        total_drivers = db.query(Driver).count()

        active_trips = db.query(Trip).filter(
            Trip.status == "Dispatched"
        ).count()

        pending_trips = db.query(Trip).filter(
            Trip.status == "Draft"
        ).count()

        completed_trips = db.query(Trip).filter(
            Trip.status == "Completed"
        ).count()

        maintenance = db.query(Maintenance).filter(
            Maintenance.status == "Open"
        ).count()

        total_fuel = db.query(
            func.sum(FuelLog.cost)
        ).scalar() or 0

        total_expense = db.query(
            func.sum(Expense.amount)
        ).scalar() or 0

        fleet_utilization = 0

        if total_vehicles:
            fleet_utilization = round(
                (on_trip / total_vehicles) * 100,
                2,
            )

        return {

            "total_vehicles": total_vehicles,

            "available_vehicles": available_vehicles,

            "vehicles_on_trip": on_trip,

            "vehicles_in_shop": in_shop,

            "retired_vehicles": retired,

            "total_drivers": total_drivers,

            "active_trips": active_trips,

            "pending_trips": pending_trips,

            "completed_trips": completed_trips,

            "maintenance_records": maintenance,

            "fuel_cost": total_fuel,

            "expense_cost": total_expense,

            "fleet_utilization": fleet_utilization

        }