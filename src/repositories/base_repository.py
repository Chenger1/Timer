from typing import (
    TypeVar,
    Type
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.db.database import Base
from src.core.exceptions import DuplicatedError


T = TypeVar("T", bound=Base)


class BaseRepository:
    def __init__(self, session_factory: Type[AsyncSession], model: Type[T]):
        self._session_factory = session_factory
        self._model = model

    async def create(self, inst: T) -> T:
        async with self._session_factory() as session:
            try:
                session.add(instance=inst)
                await session.commit()
                await session.refresh(instance=inst)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig))
            return inst
