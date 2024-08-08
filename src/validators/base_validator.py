from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import (
    inject,
    Provide
)
from pydantic import BaseModel


class BaseValidator:
    @inject
    def __init__(self, session_factory: Type[AsyncSession] = Provide["async_session"]):
        self._session_factory = session_factory

    async def validate(self, schema: BaseModel): ...
