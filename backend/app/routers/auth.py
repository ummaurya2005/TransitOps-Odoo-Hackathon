from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse,
    LoginRequest,
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return AuthService.register(user, db)


@router.post("/login")
def login(
    user: LoginRequest,
    db: Session = Depends(get_db),
):
    logged = AuthService.login(user, db)

    if not logged:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login Successful",
        "user": logged
    }