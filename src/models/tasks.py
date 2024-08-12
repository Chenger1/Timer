from datetime import datetime

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


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    start_date: Mapped[datetime] = mapped_column(DateTime())
    end_date: Mapped[datetime] = mapped_column(DateTime())

    user_id = mapped_column(ForeignKey("users.id"))
    project_id = mapped_column(ForeignKey("projects.id"))

    user = relationship("User", back_populates="tasks")
    project = relationship("Projects", back_populates="tasks")
