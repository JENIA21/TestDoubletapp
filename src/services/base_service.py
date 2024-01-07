from repositories.db_repository import SqlAlchemyRepository, ModelType
from schemas.base_schema import PyModel


class BaseService:

    def __init__(self, repository: SqlAlchemyRepository) -> None:
        self.repository: SqlAlchemyRepository = repository

    async def create(self, model: PyModel) -> ModelType:
        return await self.repository.create(data=model.model_dump())

    async def delete(self, pk: int) -> None:
        await self.repository.delete(id=pk)

    async def get(self, pk: int) -> ModelType:
        return await self.repository.get(id=pk)
