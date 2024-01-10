import json
from datetime import datetime, date
from typing import List, Any

from pydantic import model_validator

from src.models.pet import TypePet
from src.schemas.base_schema import Base


class Support(Base):
    id: str | None = None

    @model_validator(mode='before')
    def uuid_to_str(self, data: Any):
        self.id = str(self.id)
        return self


class PhotoCreate(Base):
    file: bytes


class PetSupport(Base):
    name: str


class PhotoCreateResponse(Support):
    url: str


class PetCreate(PetSupport):
    year: int
    type: TypePet

    @model_validator(mode='after')
    def get_type(self, data: Any):
        self.type = self.type.value
        return self

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class PetCreateResponse(PetSupport, Support):
    age: int
    type: TypePet
    photo: List[PhotoCreateResponse] | None = []
    created_at: datetime | None = None

    @model_validator(mode='before')
    def age_calculation(self, data: Any):
        self.age = date.today().year - self.year
        self.type = self.type.value
        return self


class PetDeleteErrors(Base):
    id: str | None = None
    error: str | None = None


class PetDelete(Base):
    ids: List[str]


class PetDeleteResponse(Base):
    deleted: int
    errors: List[PetDeleteErrors] | None = []
    pass


class PetGetResponse(Base):
    count: int
    items: List[PetCreateResponse]
