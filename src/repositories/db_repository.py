from typing import Type, TypeVar, Generic

from fastapi import UploadFile
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.base_model import Base
from src.models.photo_pet import Photo
from src.repositories.base_repository import AbstractRepository
from src.schemas.pet_schema import PetGetResponse, PetDeleteResponse, PetDelete, Support, PhotoCreateResponse

from src.utils.operations_files_minio import creat_files_minio_files, delete_files_minio_files

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Base)


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType, CreateSchemaType]):

    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self._session_factory = db_session
        self.model = model

    async def create(self, data: CreateSchemaType, file: UploadFile) -> ModelType:
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            url = creat_files_minio_files(await file.read(), filename=file.filename)
            instance_photo = Photo(id_photo=file.filename, pet_id=instance.id)
            session.add(instance_photo)
            await session.commit()
            await session.refresh(instance_photo)
            return instance

    async def delete(self, ids: PetDelete) -> PetDeleteResponse:
        async with self._session_factory() as session:
            for id in ids.ids:
                img_name = await session.execute(select(Photo).filter_by(pet_id=id))
                delete_files_minio_files(img_name.scalars().all())
                await session.execute(delete(Photo).filter_by(pet_id=id))
                await session.execute(delete(self.model).filter_by(id=id))

            await session.commit()
            await session.refresh()
            return PetDeleteResponse(deleted=len(ids.ids))

    async def add_photo(self, file: UploadFile, id: Support) -> PhotoCreateResponse:
        async with self._session_factory() as session:
            url = creat_files_minio_files(await file.read(), filename=file.filename)
            instance = self.model(id_photo=file.filename, pet_id=id)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return PhotoCreateResponse(id=instance.id, url=url)

    async def get_multi(
            self,
            limit: int = 10,
            offset: int = 0,
            has_photo: bool = False
    ) -> PetGetResponse:
        async with self._session_factory() as session:
            stmt = select(self.model, Photo).order_by("id").limit(limit).offset(offset).join(Photo, Photo.pet_id==self.model.id)
            row = await session.execute(stmt)
            data = row.scalars().all()
            return PetGetResponse(count=len(data), items=data)
