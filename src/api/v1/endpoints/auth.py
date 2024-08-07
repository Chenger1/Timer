from dependency_injector.wiring import (
    inject,
    Provide
)
from fastapi import (
    APIRouter,
    Depends
)

from src.core.container import Container
from src.schemas.auth import (
    SignUp,
    SignInResponse
)
from src.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post('/sign-up', response_model=SignInResponse)
@inject
async def sign_in(user_info: SignUp, service: AuthService = Depends(Provide[Container.auth_service])):
    return await service.sign_up(user_info)
