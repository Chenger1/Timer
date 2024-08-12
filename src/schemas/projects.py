from pydantic import BaseModel


class ProjectSchema(BaseModel):
    name: str
    is_public: bool
    user_id: int
    client_id: int


class ProjectResponse(ProjectSchema):
    id: int
