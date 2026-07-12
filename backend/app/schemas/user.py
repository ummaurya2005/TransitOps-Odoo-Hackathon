from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    email: str
    role: str


class UserCreate(UserBase):
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)