import os

from dotenv import load_dotenv
from pydantic import BaseConfig


load_dotenv()


class Config(BaseConfig):
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")

    DATABASE_URI_FORMAT: str = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
        port=DB_PORT,
    )

    class Config:
        case_sensitive = True


config = Config()
