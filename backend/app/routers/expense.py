from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpenseResponse,
)
from app.services.expense_service import ExpenseService

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.get("/", response_model=list[ExpenseResponse])
def get_all(db: Session = Depends(get_db)):
    return ExpenseService.get_all(db)


@router.post("/", response_model=ExpenseResponse)
def create(
    data: ExpenseCreate,
    db: Session = Depends(get_db),
):
    return ExpenseService.create(data, db)


@router.put("/{expense_id}", response_model=ExpenseResponse)
def update(
    expense_id: int,
    data: ExpenseUpdate,
    db: Session = Depends(get_db),
):
    expense = ExpenseService.update(expense_id, data, db)

    if not expense:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@router.delete("/{expense_id}")
def delete(
    expense_id: int,
    db: Session = Depends(get_db),
):
    expense = ExpenseService.delete(expense_id, db)

    if not expense:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense