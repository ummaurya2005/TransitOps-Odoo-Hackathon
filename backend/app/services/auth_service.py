from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, LoginRequest


class AuthService:

    @staticmethod
    def register(user: UserCreate, db: Session):

        existing = db.query(User).filter(
            User.email == user.email
        ).first()

        if existing:
            raise ValueError("Email already exists.")

        db_user = User(**user.model_dump())

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def login(data: LoginRequest, db: Session):

        user = db.query(User).filter(
            User.email == data.email
        ).first()

        if not user:
            return None

        if user.password != data.password:
            return None

        return user