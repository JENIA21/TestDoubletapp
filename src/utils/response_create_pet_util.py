from datetime import datetime
from typing import TypeVar

from schemas.base_schema import Base

CreateSchemaType = TypeVar("CreateSchemaType", bound=Base)


def create_response_util(data: CreateSchemaType, id: str, date: datetime) -> CreateSchemaType:
    age = int(datetime.now().year) - int(data["year"])
    data["age"] = age
    data.pop("year")
    data["created_at"] = date
    data["id"] = id
    return data
