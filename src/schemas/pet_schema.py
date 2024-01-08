from datetime import datetime

from pydantic import BaseModel

from models.pet import TypePet
from utils.pet_utils import crate_pet_id


class PetSupport(BaseModel):
    id: str


class PhotoCreate(PetSupport):
    file: bytes


class PetCreate(BaseModel):
    name: str
    year: int
    type: TypePet
    photo: list[PhotoCreate] | None = None
    created_at: datetime | None = datetime.now()
    id: str | None = crate_pet_id()


class PetCreateResponse(PetCreate, PetSupport):
    pass


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
