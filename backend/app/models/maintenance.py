from datetime import date

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Maintenance(Base):
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )

    maintenance_type = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    cost = Column(
        Float,
        default=0.0
    )

    maintenance_date = Column(
        Date,
        default=date.today
    )

    status = Column(
        String,
        default="Open"
    )

    vehicle = relationship("Vehicle")

    def start(self):
        self.vehicle.status = "In Shop"
        self.status = "Open"

    def complete(self):
        self.status = "Completed"

        if self.vehicle.status != "Retired":
            self.vehicle.status = "Available"
