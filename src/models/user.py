from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import (
    String,
)

from src.db.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    name: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

    tasks = relationship("Tasks", back_populates="user")
