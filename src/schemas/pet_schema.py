import datetime

from pydantic import BaseModel
from typing import Union


class PetSupport(BaseModel):
    id: str


class PetCreate(BaseModel):
    name: str
    year: int
    type: str
    photo: list


class PetCreateResponse(PetCreate, PetSupport):
    created_at: datetime.datetime


class PetGet(BaseModel):
    limit: Union[int, None] = 20
    offset: Union[int, None] = 0
    has_photo: Union[bool, None] = None


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
