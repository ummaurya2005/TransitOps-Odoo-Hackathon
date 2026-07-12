from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate


class ExpenseService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Expense).all()

    @staticmethod
    def get_by_id(expense_id: int, db: Session):
        return db.query(Expense).filter(
            Expense.id == expense_id
        ).first()

    @staticmethod
    def create(data: ExpenseCreate, db: Session):

        expense = Expense(**data.model_dump())

        db.add(expense)
        db.commit()
        db.refresh(expense)

        return expense

    @staticmethod
    def update(expense_id: int, data: ExpenseUpdate, db: Session):

        expense = ExpenseService.get_by_id(expense_id, db)

        if not expense:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(expense, key, value)

        db.commit()
        db.refresh(expense)

        return expense

    @staticmethod
    def delete(expense_id: int, db: Session):

        expense = ExpenseService.get_by_id(expense_id, db)

        if not expense:
            return None

        db.delete(expense)
        db.commit()

        return {"message": "Expense deleted successfully."}