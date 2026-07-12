from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/vehicles")
def vehicle_report(db: Session = Depends(get_db)):
    return ReportService.vehicle_report(db)


@router.get("/drivers")
def driver_report(db: Session = Depends(get_db)):
    return ReportService.driver_report(db)


@router.get("/trips")
def trip_report(db: Session = Depends(get_db)):
    return ReportService.trip_report(db)


@router.get("/fuel")
def fuel_report(db: Session = Depends(get_db)):
    return ReportService.fuel_report(db)


@router.get("/expenses")
def expense_report(db: Session = Depends(get_db)):
    return ReportService.expense_report(db)


@router.get("/operational-cost")
def operational_cost(db: Session = Depends(get_db)):
    return ReportService.total_operational_cost(db)