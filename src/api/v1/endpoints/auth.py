from typing import Annotated

from dependency_injector.wiring import (
    inject,
    Provide
)
from fastapi import (
    APIRouter,
    Depends
)
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)

from src.core.container import Container
from src.schemas.auth import (
    SignUp,
    SignInResponse
)
from src.services.auth_service import AuthService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/token")
@inject
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                service: AuthService = Depends(Provide[Container.auth_service])):
    return await service.sign_in(form_data)


@router.post('/sign-up', response_model=SignInResponse)
@inject
async def sign_in(user_info: SignUp, service: AuthService = Depends(Provide[Container.auth_service])):
    return await service.sign_up(user_info)
