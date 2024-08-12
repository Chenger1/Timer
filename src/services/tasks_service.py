from src.services.base_service import BaseService
from src.repositories.tasks_repository import TasksRepository
from src.schemas.tasks import (
    CreateTask,
    TaskResponse,
)
from src.models.tasks import Tasks
from src.utils.db_utils import apply_pydantic_fields_to_model


class TasksService(BaseService):
    def __init__(self, repository: TasksRepository):
        super().__init__(repository)

    async def create_task(self, task_info: CreateTask) -> TaskResponse:
        task = Tasks(**task_info.dict(exclude_none=True))
        task = await self._repository.create(task)
        return TaskResponse(
            title=task.title,
            start_date=task.start_date,
            end_date=task.end_date,
            user_id=task.user_id,
            task_id=task.id
        )

    async def edit_task(self, task_id: int, task_info: CreateTask) -> TaskResponse:
        task = await self._repository.get_by_id(task_id)
        apply_pydantic_fields_to_model(task, task_info)
        task = await self._repository.update(task)
        return TaskResponse(
            title=task.title,
            start_date=task.start_date,
            end_date=task.end_date,
            user_id=task.user_id,
            task_id=task.id
        )

    async def delete_task(self, task_id: int) -> TaskResponse:
        task = await self._repository.delete_by_id(task_id)
        return TaskResponse(
            title=task.title,
            start_date=task.start_date,
            end_date=task.end_date,
            user_id=task.user_id,
            task_id=task.id
        )
