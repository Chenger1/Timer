import pwdlib

from fastapi.security import OAuth2PasswordRequestForm

from src.services.base_service import BaseService
from src.schemas.auth import (
    SignUp,
    SignInResponse
)
from src.schemas.users import User as UserSchema
from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.validators.auth_validator import AuthValidator
from src.core.exceptions import AuthError
from src.utils.jwt import create_access_token


class AuthService(BaseService):
    _password_hash = pwdlib.PasswordHash.recommended()

    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    async def sign_in(self, form_data: OAuth2PasswordRequestForm) -> SignInResponse:
        user = await self._repository.get_one_with_filters(filters={"email": form_data.username})
        if user is None:
            raise AuthError(f"Not found user with email: {form_data.username}")
        if self._password_hash.verify(form_data.password, user.password) is False:
            raise AuthError("Wrong password")

        return SignInResponse(
            access_token=create_access_token({"sub": user.email}),
            user_info=UserSchema(
                email=user.email,
                name=user.name
            )
        )

    async def sign_up(self, user_info: SignUp) -> SignInResponse:
        await AuthValidator().validate(user_info)
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
