from typing import (
    Any,
    Protocol,
)


class RepositoryProtocol(Protocol):
    async def create(self, inst: Any) -> Any: ...
    async def get_one_with_filters(self, filters: Any) -> Any: ...
    async def get_any_with_filters(self, filters: Any) -> Any: ...
    async def get_by_id(self, obj_id: Any) -> Any: ...
    async def update(self, inst: Any) -> Any: ...


class BaseService:
    def __init__(self, repository: RepositoryProtocol):
        self._repository = repository

    def add(self, schema: Any) -> Any:
        return self._repository.create(schema)
