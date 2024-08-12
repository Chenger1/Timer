from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.base_repository import BaseRepository
from src.models.projects import Projects


class ProjectsRepository(BaseRepository):
    def __init__(self, session_factory: Type[AsyncSession]):
        super().__init__(session_factory, Projects)
