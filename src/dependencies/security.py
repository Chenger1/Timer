from fastapi import Depends
from dependency_injector.wiring import (
    inject,
    Provide
)
from pydantic import ValidationError

from src.core.security import JWTBearer
from src.core.container import Container
from src.core.exceptions import AuthError
from src.services.user_service import UserService
from src.models.user import User
from src.schemas.auth import JWTPayload


@inject
async def get_current_user(
    jwt_payload: dict = Depends(JWTBearer()),
    service: UserService = Depends(Provide[Container.user_service])
) -> User:
    try:
        token_data = JWTPayload(**jwt_payload)
    except ValidationError:
        raise AuthError("Could not validate credentials")
    current_user: User = await service.get_user_by_id(token_data.id)
    if current_user is None:
        raise AuthError("User not found")
    return current_user
