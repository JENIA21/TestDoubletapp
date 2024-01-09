from datetime import datetime, date
from typing import List, Any

from pydantic import model_validator

from models.pet import TypePet
from schemas.base_schema import Base


class Support(Base):
    id: str | None = None


class PhotoCreate(Base):
    file: bytes


class PetSupport(Base):
    name: str


class PetCreate(PetSupport):
    year: int
    type: TypePet

    # photo: List[PhotoCreate] | None = None

    @model_validator(mode='after')
    def year(self, data: Any):
        self.type = self.type.value
        return self


class PetCreateResponse(PetSupport, Support):
    age: int
    type: TypePet
    photo: List[PhotoCreate] | None = []
    created_at: datetime | None = None

    @model_validator(mode='before')
    def year(self, data: Any):
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


class PhotoCreateResponse(Support):
    url: str


class PetGetResponse(Base):
    count: int
    items: List[PetCreateResponse]
