import os

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_async_engine(DATABASE_URL)
Session = async_sessionmaker(bind=engine)


class Base(DeclarativeBase): ...
