from datetime import datetime
from typing import List

from pydantic import validator


from models.pet import TypePet
from schemas.base_schema import Base


class Support(Base):
    id: str | None = None


class PhotoCreate(Support):
    file: bytes


class PetSupport(Base):
    name: str


class PetCreate(PetSupport):
    year: int
    type: TypePet
    # photo: List[PhotoCreate] | None = None

    @validator('type')
    def validate_type_create(cls, value):
        if type(value) is not str:
            value = value.value
        return value


class PetCreateResponse(PetSupport, Support):
    age: int | None = None
    type: TypePet
    photo: List[PhotoCreate] | None = []
    created_at: datetime | None = None

    @validator('type', pre=True)
    def validate_type(cls, value):
        if type(value) is not str:
            value = value.value
        return value


class PetGet(Base):
    limit: int | None = 20
    offset: int | None = 0
    has_photo: bool | None = None


class PetDelete(Base):
    ids: List[str]


class PetDeleteResponse(PetDelete):
    pass


class PhotoCreateResponse(Support):
    url: str


class PetGetResponse(Base):
    count: int
    items: List[PetCreateResponse]
