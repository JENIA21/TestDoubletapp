from repositories.pet_repository import pet_repository
from src.services.base_service import BaseService


class PetService(BaseService):
    pass


pet_service = PetService(repository=pet_repository)
