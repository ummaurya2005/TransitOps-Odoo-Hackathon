from sqlalchemy import Column, Integer, String, Float, Date
from app.db.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)

    registration_number = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    vehicle_name = Column(
        String,
        nullable=False
    )

    vehicle_type = Column(
        String,
        nullable=False
    )

    max_load_capacity = Column(
        Float,
        nullable=False
    )

    odometer = Column(
        Float,
        default=0.0
    )

    acquisition_cost = Column(
        Float,
        nullable=False
    )

    acquisition_date = Column(
        Date
    )

    status = Column(
        String,
        default="Available"
    )

    notes = Column(
        String,
        nullable=True
    )