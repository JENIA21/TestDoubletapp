import datetime

from pydantic import BaseModel
from typing import Union

from models.pet import TypePet


class PetSupport(BaseModel):
    id: str


class PetCreate(BaseModel):
    name: str
    year: int
    type: TypePet
    photo: list


class PetCreateResponse(PetCreate, PetSupport):
    created_at: datetime.datetime


class PetGet(BaseModel):
    limit: int | None = 20
    offset: int | None = 0
    has_photo: bool | None = None


class PetGetResponse(BaseModel):
    count: int
    items: list


class PetDelete(BaseModel):
    ids: list


class PetDeleteResponse(PetDelete):
    pass


class PhotoCreate(PetSupport):
    file: bytes


class PhotoCreateResponse(PetSupport):
    url: str
