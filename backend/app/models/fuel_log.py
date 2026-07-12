from datetime import date

from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class FuelLog(Base):
    __tablename__ = "fuel_logs"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )

    liters = Column(
        Float,
        nullable=False
    )

    cost = Column(
        Float,
        nullable=False
    )

    fuel_date = Column(
        Date,
        default=date.today
    )

    vehicle = relationship("Vehicle")