from pydantic import (
    BaseModel,
    EmailStr
)

from src.schemas.users import User


class SignUp(BaseModel):
    name: str
    email: EmailStr
    password: str


class SignIn(BaseModel):
    email: EmailStr
    password: str


class SignInResponse(BaseModel):
    access_token: str
    user_info: User
