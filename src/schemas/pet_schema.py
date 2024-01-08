from datetime import datetime

from pydantic import BaseModel, validator


from models.pet import TypePet


class Support(BaseModel):
    id: str | None = None


class PhotoCreate(Support):
    file: bytes


class PetSupport(Support):
    name: str
    type: TypePet
    # photo: list[PhotoCreate] | None = None

    @validator('type')
    def validate_id(cls, value):
        value = value.value
        return value


class PetCreate(PetSupport):
    year: int


class PetCreateResponse(PetSupport):
    age: int
    created_at: datetime | None = None


class PetGet(BaseModel):
    limit: int | None = 20
    offset: int | None = 0
    has_photo: bool | None = None


class PetGetResponse(BaseModel):
    count: int
    items: list


class PetDelete(BaseModel):
    ids: list[str]


class PetDeleteResponse(PetDelete):
    pass


class PhotoCreateResponse(Support):
    url: str
