from typing import (
    Any,
    Protocol
)


class RepositoryProtocol(Protocol):
    def create(self, inst: Any) -> Any: ...


class BaseService:
    def __init__(self, repository: RepositoryProtocol):
        self._repository = repository

    def add(self, schema: Any) -> Any:
        return self._repository.create(schema)
