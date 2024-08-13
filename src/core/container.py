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
from src.services.clients_service import ClientsService
from src.services.projects_service import ProjectsService
from src.services.tasks_services.tasks_service import TasksService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            # Api modules
            "src.api.v1.endpoints.auth",
            "src.api.v1.endpoints.tasks",
            "src.api.v1.endpoints.clients",
            "src.api.v1.endpoints.projects",
            "src.api.v1.endpoints.reports",

            # Validators
            "src.validators.base_validator",
            
            # dependencies
            "src.dependencies.security",
        ]
    )

    engine = providers.Singleton(
        create_async_engine,
        Config.DATABASE_URI_FORMAT
    )

    async_session = providers.Factory(async_sessionmaker, bind=engine, expire_on_commit=False)

    user_repository = providers.Factory(UserRepository, session_factory=async_session)
    tasks_repository = providers.Factory(TasksRepository, session_factory=async_session)
    clients_repository = providers.Factory(ClientsRepository, session_factory=async_session)
    projects_repository = providers.Factory(ProjectsRepository, session_factory=async_session)

    auth_service = providers.Factory(AuthService, repository=user_repository)
    tasks_service = providers.Factory(TasksService, repository=tasks_repository)
    user_service = providers.Factory(UserService, repository=user_repository)
    clients_service = providers.Factory(ClientsService, repository=clients_repository)
    projects_service = providers.Factory(ProjectsService, repository=projects_repository)
    summary_service = providers.Factory(SummaryService, repository=tasks_repository)
