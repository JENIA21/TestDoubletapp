from pydantic import BaseModel
from typing import Union


class PetCreate(BaseModel):
    name: str
    year: int
    type: str
    photo: list


class PetResponse(BaseModel):
    limit: Union[int, None] = 20
    offset: Union[int, None] = 0
    has_photo: Union[bool, None] = None


class PetDelete(BaseModel):
    pass


class PhotoCreate(BaseModel):
    id: int
    file: bytes

