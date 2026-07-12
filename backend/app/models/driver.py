from datetime import date

from sqlalchemy import Column, Date, Float, Integer, String
from app.db.database import Base


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        nullable=False
    )

    license_number = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    license_category = Column(
        String,
        nullable=False
    )

    license_expiry_date = Column(
        Date,
        nullable=False
    )

    contact_number = Column(
        String,
        nullable=False
    )

    safety_score = Column(
        Float,
        default=100.0
    )

    status = Column(
        String,
        default="Available"
    )

    def is_license_valid(self):
        return self.license_expiry_date >= date.today()

    def assign_trip(self):
        if self.status != "Available":
            raise ValueError("Driver is not available.")

        if not self.is_license_valid():
            raise ValueError("Driver license has expired.")

        self.status = "On Trip"

    def complete_trip(self):
        self.status = "Available"

    def suspend(self):
        self.status = "Suspended"

    def off_duty(self):
        self.status = "Off Duty"

    def available(self):
        self.status = "Available"