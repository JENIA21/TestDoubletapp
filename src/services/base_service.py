from fastapi import UploadFile

from src.repositories.db_repository import SqlAlchemyRepository, ModelType
from src.schemas.base_schema import PyModel
from src.schemas.pet_schema import PetDelete, PetDeleteResponse, PhotoCreate, Support, PhotoCreateResponse, PetGetResponse


class BaseService:

    def __init__(self, repository: SqlAlchemyRepository) -> None:
        self.repository: SqlAlchemyRepository = repository

    async def create(self, model: PyModel, file: UploadFile) -> ModelType:
        return await self.repository.create(data=model.model_dump(), file=file)

    async def delete(self, ids: PetDelete) -> PetDeleteResponse:
        return await self.repository.delete(ids=ids)

    async def add_photo(self, file: UploadFile, id: Support) -> PhotoCreateResponse:
        return await self.repository.add_photo(id=id, file=file)

    async def get_multi(self,
                        limit: int | None = 20,
                        offset: int | None = 0,
                        has_photo: bool | None = False) -> PetGetResponse:
        return await self.repository.get_multi(limit=limit,
                                               offset=offset,
                                               has_photo=has_photo)
