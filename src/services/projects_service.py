from src.services.base_service import BaseService
from src.repositories.projects_repository import ProjectsRepository
from src.schemas.projects import (
    ProjectSchema,
    ProjectResponse
)
from src.models.projects import Projects


class ProjectsService(BaseService):
    def __init__(self, repository: ProjectsRepository):
        super().__init__(repository)

    @classmethod
    def convert_model_to_schema(cls, model: Projects) -> ProjectResponse:
        return ProjectResponse(
            name=model.name,
            is_public=model.is_public,
            user_id=model.user_id,
            client_id=model.client_id,
            id=model.id
        )

    async def create_repository(self, schema: ProjectSchema) -> ProjectResponse:
        project = Projects(**schema.dict())
        project = await self._repository.create(project)
        return self.convert_model_to_schema(project)
