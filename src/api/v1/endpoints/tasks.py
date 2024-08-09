from dependency_injector.wiring import (
    inject,
    Provide
)

from fastapi import (
    APIRouter,
    Depends
)

from src.schemas.tasks import CreateTask
from src.core.container import Container
from src.dependencies.security import require_permissions
from src.services.tasks_service import TasksService


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post("/create", dependencies=[Depends(require_permissions())])
@inject
async def create_task(task_info: CreateTask, task_service: TasksService = Depends(Provide[Container.tasks_service])):
    return await task_service.create_task(task_info)
