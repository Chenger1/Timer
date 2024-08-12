from typing import (
    Iterable,
    Optional
)

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

    @classmethod
    def convert_model_to_schema(cls, model: Tasks) -> TaskResponse:
        return TaskResponse(
            title=model.title,
            start_date=model.start_date,
            end_date=model.end_date,
            user_id=model.user_id,
            task_id=model.id
        )

    async def create_task(self, task_info: CreateTask) -> TaskResponse:
        task = Tasks(**task_info.dict(exclude_none=True))
        task = await self._repository.create(task)
        return self.convert_model_to_schema(task)

    async def edit_task(self, task_id: int, task_info: CreateTask) -> TaskResponse:
        task = await self._repository.get_by_id(task_id)
        apply_pydantic_fields_to_model(task, task_info)
        task = await self._repository.update(task)
        return self.convert_model_to_schema(task)

    async def delete_task(self, task_id: int) -> TaskResponse:
        task = await self._repository.delete_by_id(task_id)
        return self.convert_model_to_schema(task)

    async def get_tasks_list(self, user_id: int, project_id: Optional[int] = None) -> Iterable[TaskResponse]:
        return await self._repository.get_many_with_filters(filters={"user_id": user_id, "project_id": project_id},
                                                            paginate_query=True)
