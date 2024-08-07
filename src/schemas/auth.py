from pydantic import BaseModel

from src.schemas.users import User


class SignUp(BaseModel):
    name: str
    email: str
    password: str


class SignIn(BaseModel):
    email: str
    password: str


class SignInResponse(BaseModel):
    access_token: str
    user_info: User
