from repositories.file_repository import file_repository
from src.services.base_service import BaseService


class FileService(BaseService):
    pass


file_service = FileService(repository=file_repository)
