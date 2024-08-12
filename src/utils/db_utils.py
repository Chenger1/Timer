from typing import TypeVar

from pydantic import BaseModel

from src.db.database import Base


T = TypeVar("T", bound=Base)


def apply_pydantic_fields_to_model(model: T, schema: BaseModel):
    """
    :param model: sqlalchemy model
    :param schema: pydantic schema
    """

    def __apply_dict(data_dict: dict):
        for key, value in data_dict.items():
            if isinstance(value, dict):
                __apply_dict(value)
            else:
                setattr(model, key, value)

    __apply_dict(schema.model_dump())
