from datetime import date

from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )

    expense_type = Column(
        String,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    expense_date = Column(
        Date,
        default=date.today
    )

    vehicle = relationship("Vehicle")