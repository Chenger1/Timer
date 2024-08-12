from typing import (
    TypeVar,
    Optional,
    Type,
    Any,
    Sequence,
    Union
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, Row, RowMapping
from fastapi_pagination.ext.async_sqlalchemy import paginate

from src.db.database import Base
from src.core.exceptions import (
    DuplicatedError,
    NotFoundError
)
from src.utils.query_builder import convert_dict_to_sqlalchemy_filters


T = TypeVar("T", bound=Base)


class BaseRepository:
    def __init__(self, session_factory: Type[AsyncSession], model: Type[T]):
        self._session_factory = session_factory
        self._model = model

    async def get_by_id(self, obj_id: int) -> Row[Any] | RowMapping:
        async with self._session_factory() as session:
            res = await session.execute(
                select(self._model).filter_by(id=obj_id)
            )
            obj = res.scalars().first()
            if obj is None:
                raise NotFoundError(f"Not found entity with id: {obj_id}")
            return obj

    async def get_many_with_filters(self,
                                    filters: Optional[dict] = None,
                                    paginate_query: bool = False) -> Sequence[Row[tuple[Any]]]:
        async with self._session_factory() as session:
            filter_options = convert_dict_to_sqlalchemy_filters(self._model, filters)
            filtered_query = select(self._model).where(filter_options)
            if paginate_query is True:
                return await paginate(session, filtered_query)
            return (await session.execute(filtered_query)).fetchall()

    async def get_one_with_filters(self, filters: Optional[dict] = None) -> Union[T, None]:
        async with self._session_factory() as session:
            filter_options = convert_dict_to_sqlalchemy_filters(self._model, filters)
            filtered_query = select(self._model).where(filter_options)
            return (await session.execute(filtered_query)).first()[0]

    async def create(self, inst: T) -> T:
        async with self._session_factory() as session:
            try:
                session.add(instance=inst)
                await session.commit()
                await session.refresh(instance=inst)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig))
            return inst

    async def update(self, inst: T) -> T:
        return await self.create(inst)

    async def delete_by_id(self, obj_id: int) -> T:
        async with self._session_factory() as session:
            obj = (await session.execute(
                select(self._model).filter_by(id=obj_id)
            )).scalars().first()
            if obj is None:
                raise NotFoundError(f"Not found entity with id: {obj_id}")
            await session.delete(obj)
            await session.commit()
            return obj
