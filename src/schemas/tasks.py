from datetime import datetime

from pydantic import BaseModel


class CreateTask(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    user_id: int


class TaskResponse(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    user_id: int
    task_id: int
