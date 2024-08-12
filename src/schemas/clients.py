from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr
)


class ClientSchema(BaseModel):
    name: str
    user_id: int
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    note: Optional[str] = None


class ClientResponseSchema(ClientSchema):
    id: int
