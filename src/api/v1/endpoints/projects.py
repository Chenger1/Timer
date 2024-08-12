from fastapi import (
    APIRouter,
    Depends
)
from dependency_injector.wiring import (
    inject,
    Provide
)

from src.core.container import Container
from src.services.projects_service import ProjectsService
from src.schemas.projects import (
    ProjectSchema,
    ProjectResponse
)
from src.dependencies.security import require_permissions


router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/create", dependencies=[], response_model=ProjectResponse)
@inject
async def create_project(project: ProjectSchema, service: ProjectsService = Depends(Provide[Container.projects_service])):
    return await service.create_repository(project)
