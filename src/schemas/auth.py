from datetime import datetime

from pydantic import (
    BaseModel,
    EmailStr
)

from src.schemas.users import User


class SignUp(BaseModel):
    name: str
    email: EmailStr
    password: str


class SignInResponse(BaseModel):
    access_token: str
    expiration_time: datetime
    user_info: User


class JWTPayload(BaseModel):
    id: int
    email: str
    name: str
