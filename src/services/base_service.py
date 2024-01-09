from typing import Any

from models.base_model import Base
from repositories.db_repository import SqlAlchemyRepository, ModelType
from schemas.base_schema import PyModel
from schemas.pet_schema import PetDelete, PetDeleteResponse, PhotoCreate, Support, PhotoCreateResponse


class BaseService:

    def __init__(self, repository: SqlAlchemyRepository) -> None:
        self.repository: SqlAlchemyRepository = repository

    async def create(self, model: PyModel) -> ModelType:
        return await self.repository.create(data=model.model_dump())

    async def delete(self, ids: PetDelete) -> PetDeleteResponse:
        return await self.repository.delete(ids=ids)

    async def add_photo(self, file: PhotoCreate, id: Support, filename: str) -> PhotoCreateResponse:
        return await self.repository.add_photo(id=id, file=file, filename=filename)

    async def get_multi(self,
                        limit: int | None = 20,
                        offset: int | None = 0,
                        has_photo: bool | None = False) -> list[Base | Any]:
        return await self.repository.get_multi(limit=limit,
                                               offset=offset,
                                               has_photo=has_photo)
