from src.repositories.db_repository import SqlAlchemyRepository
from src.models.photo_pet import Photo
from src.config.database.db_helper import db_helper

from src.schemas.pet_schema import PhotoCreate


class FileRepository(SqlAlchemyRepository[Photo, PhotoCreate]):
    pass


file_repository = FileRepository(model=Photo, db_session=db_helper.get_db_session)
