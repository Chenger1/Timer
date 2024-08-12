from datetime import datetime

from pydantic import (
    BaseModel,
    Field
)


class CreateTask(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    user_id: int
    project_id: int


class TaskResponse(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    user_id: int
    project_id: int
    task_id: int = Field(alias="id")
