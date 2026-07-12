from datetime import date

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(
        String,
        nullable=False
    )

    destination = Column(
        String,
        nullable=False
    )

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )

    driver_id = Column(
        Integer,
        ForeignKey("drivers.id"),
        nullable=False
    )

    cargo_weight = Column(
        Float,
        nullable=False
    )

    planned_distance = Column(
        Float,
        nullable=False
    )

    trip_date = Column(
        Date,
        default=date.today
    )

    status = Column(
        String,
        default="Draft"
    )

    # Relationships
    vehicle = relationship(
        "Vehicle",
        backref="trips"
    )

    driver = relationship(
        "Driver",
        backref="trips"
    )

    def dispatch(self):
        if self.vehicle.status != "Available":
            raise ValueError("Vehicle is not available.")

        if self.driver.status != "Available":
            raise ValueError("Driver is not available.")

        if self.cargo_weight > self.vehicle.max_load_capacity:
            raise ValueError(
                "Cargo weight exceeds vehicle capacity."
            )

        self.vehicle.status = "On Trip"
        self.driver.status = "On Trip"
        self.status = "Dispatched"

    def complete(self):
        self.vehicle.status = "Available"
        self.driver.status = "Available"
        self.status = "Completed"

    def cancel(self):
        self.vehicle.status = "Available"
        self.driver.status = "Available"
        self.status = "Cancelled"