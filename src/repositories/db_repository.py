from typing import Type, TypeVar, Generic, List

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.base_model import Base
from models.photo_pet import Photo
from repositories.base_repository import AbstractRepository
from schemas.pet_schema import PetGetResponse, PetDeleteResponse, PetDelete, PhotoCreate, Support, PhotoCreateResponse
from utils.operations_files_minio import creat_files_minio_files, delete_files_minio_files

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Base)


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType, CreateSchemaType]):

    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self._session_factory = db_session
        self.model = model

    async def create(self, data: CreateSchemaType) -> ModelType:
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def delete(self, ids: PetDelete) -> PetDeleteResponse:
        async with self._session_factory() as session:
            for id in ids.ids:
                img_name = await session.execute(select(Photo).filter_by(pet_id=id))
                delete_files_minio_files(img_name.scalars().all())
                await session.execute(delete(Photo).filter_by(pet_id=id))
                await session.execute(delete(self.model).filter_by(id=id))

            await session.commit()
            return PetDeleteResponse(deleted=len(ids.ids))

    async def add_photo(self, file: PhotoCreate, id: Support, filename: str) -> PhotoCreateResponse:
        async with self._session_factory() as session:
            url = creat_files_minio_files(file, filename=filename)
            instance = self.model(id_photo=filename, pet_id=id)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return PhotoCreateResponse(id=instance.id, url=url)

    async def get_multi(
            self,
            limit: int = 100,
            offset: int = 0,
            has_photo: bool = False
    ) -> List[ModelType]:
        async with self._session_factory() as session:
            stmt = select(self.model).order_by("id").limit(limit).offset(offset)
            row = await session.execute(stmt)
            data = row.scalars().all()
            return PetGetResponse(count=len(data), items=data)
