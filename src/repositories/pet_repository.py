from src.repositories.db_repository import SqlAlchemyRepository
from src.models.pet import Pet
from src.config.database.db_helper import db_helper

from src.schemas.pet_schema import PetCreate


class PetRepository(SqlAlchemyRepository[Pet, PetCreate]):
    pass


pet_repository = PetRepository(model=Pet, db_session=db_helper.get_db_session)
