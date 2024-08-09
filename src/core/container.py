from dependency_injector import (
    containers,
    providers
)

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

from src.core.config import Config
from src.repositories import *
from src.services import *
from src.services.tasks_service import TasksService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            # Api modules
            "src.api.v1.endpoints.auth",
            "src.api.v1.endpoints.tasks",

            # Validators
            "src.validators.base_validator"
        ]
    )

    engine = providers.Singleton(
        create_async_engine,
        Config.DATABASE_URI_FORMAT
    )

    async_session = providers.Factory(async_sessionmaker, bind=engine, expire_on_commit=False)

    user_repository = providers.Factory(UserRepository, session_factory=async_session)
    tasks_repository = providers.Factory(TasksRepository, session_factory=async_session)

    auth_service = providers.Factory(AuthService, repository=user_repository)
    tasks_service = providers.Factory(TasksService, repository=tasks_repository)
