from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import (
    String,
    DateTime,
    ForeignKey
)

from src.db.database import Base

if TYPE_CHECKING:
    from src.models.user import User


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    start_date: Mapped[datetime] = mapped_column(DateTime())
    end_date: Mapped[datetime] = mapped_column(DateTime())
    user_id = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="tasks")
