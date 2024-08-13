from typing import (
    Type,
    Any
)

from sqlalchemy import (
    Row,
    RowMapping,
    select,
)
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import NotFoundError
from src.repositories.base_repository import BaseRepository
from src.models.tasks import Tasks


class TasksRepository(BaseRepository):
    def __init__(self, session_factory: Type[AsyncSession]):
        super().__init__(session_factory, Tasks)

    async def get_by_id(self, obj_id: int) -> Row[Any] | RowMapping:
        async with self._session_factory() as session:
            obj = (await session.execute(
                select(self._model).\
                    filter_by(id=obj_id).\
                    options(joinedload(Tasks.project))
            )).scalars().first()
            if obj is None:
                raise NotFoundError(detail=f"Not found task with id: {obj_id}")
            return obj
