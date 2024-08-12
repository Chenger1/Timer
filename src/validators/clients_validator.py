from sqlalchemy import select

from src.validators.base_validator import BaseValidator
from src.schemas.clients import ClientSchema
from src.models.clients import Clients
from src.core.exceptions import ValidationError


class CreateClientValidator(BaseValidator):
    async def validate(self, schema: ClientSchema):
        async with self._session_factory() as session:
            result = await session.execute(
                select(Clients).where(
                    (Clients.user_id == schema.user_id) &
                    (Clients.name == schema.name)
                )
            )
            if result.first() is not None:
                raise ValidationError(detail="Such client already exists")
            return True
