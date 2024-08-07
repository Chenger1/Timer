import pwdlib

from src.services.base_service import BaseService
from src.schemas.auth import (
    SignUp,
    SignInResponse
)
from src.schemas.users import User as UserSchema
from src.models.user import User
from src.repositories.user_repository import UserRepository


class AuthService(BaseService):
    _password_hash = pwdlib.PasswordHash.recommended()

    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    async def sign_up(self, user_info: SignUp) -> SignInResponse:
        user = User(**user_info.dict(exclude_none=True))
        user.password = self._password_hash.hash(user_info.password)
        user = await self._repository.create(user)
        return SignInResponse(
            access_token="",
            user_info=UserSchema(
                email=user.email,
                name=user.name
            )
        )
