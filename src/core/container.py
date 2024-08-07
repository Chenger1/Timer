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


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.endpoints.auth",
        ]
    )

    engine = providers.Singleton(
        create_async_engine,
        Config.DATABASE_URI_FORMAT
    )

    async_session = providers.Factory(async_sessionmaker, bind=engine, expire_on_commit=False)

    user_repository = providers.Factory(UserRepository, session_factory=async_session)

    auth_service = providers.Factory(AuthService, repository=user_repository)
