from typing import Optional
from decimal import Decimal

from pydantic import BaseModel


class ProjectSchema(BaseModel):
    name: str
    is_public: bool
    user_id: int
    client_id: int
    is_billable: bool
    rate: Optional[Decimal] = None


class ProjectResponse(ProjectSchema):
    id: int
