from sqlalchemy import select

from src.validators.base_validator import BaseValidator
from src.schemas.auth import SignUp
from src.models.user import User
from src.core.exceptions import ValidationError


class AuthValidator(BaseValidator):
    async def validate(self, schema: SignUp):
        async with self._session_factory() as session:
            result = await session.execute(select(User).where(User.email==schema.email))
            if result.first() is not None:
                raise ValidationError(detail=f"Email: {schema.email} already exists")
            return True
