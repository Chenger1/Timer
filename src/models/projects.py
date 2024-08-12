from decimal import Decimal

from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship
)
from sqlalchemy import (
    String,
    ForeignKey,
    Boolean,
    DECIMAL
)

from src.db.database import Base


class Projects(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    is_public: Mapped[bool] = mapped_column(Boolean, default=False)
    is_billable: Mapped[bool] = mapped_column(Boolean, default=False)
    rate: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=True)

    user_id = mapped_column(ForeignKey("users.id"))
    client_id = mapped_column(ForeignKey("clients.id"), nullable=True)

    user = relationship("User", back_populates="projects")
    client = relationship("Clients", back_populates="projects")
    tasks = relationship("Tasks", back_populates="project")
