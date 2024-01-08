from typing import Type, TypeVar, Generic

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.base_model import Base
from repositories.base_repository import AbstractRepository
from utils.response_create_pet_util import create_response_util

ModelType = TypeVar("ModelType")
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

    async def delete(self, **filters) -> None:
        async with self._session_factory() as session:
            await session.execute(delete(self.model).filter_by(**filters))
            await session.commit()

    async def get_multi(
            self,
            order: str = "id",
            limit: int = 100,
            offset: int = 0
    ) -> list[ModelType]:
        async with self._session_factory() as session:
            stmt = select(self.model).order_by(*order).limit(limit).offset(offset)
            row = await session.execute(stmt)
            return row.scalars().all()
