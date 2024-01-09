from typing import Type, TypeVar, Generic, List

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.base_model import Base
from repositories.base_repository import AbstractRepository
from schemas.pet_schema import PetGetResponse, PetDeleteResponse, PetDelete
from utils.response_create_pet_util import create_response_util

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
            return create_response_util(data, instance.id, instance.created_at)

    async def delete(self, ids: PetDelete) -> PetDeleteResponse:
        async with self._session_factory() as session:
            for id in ids.ids:
                await session.execute(delete(self.model).filter_by(id=id))
            await session.commit()
            return ids

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
