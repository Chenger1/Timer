from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import (
    String,
    ForeignKey,
    Text
)

from src.db.database import Base


class Clients(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    address: Mapped[str] = mapped_column(Text(), nullable=True)
    note: Mapped[str] = mapped_column(Text(), nullable=True)

    user_id = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="clients")

    projects = relationship("Projects", back_populates="client")
