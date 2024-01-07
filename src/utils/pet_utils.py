import uuid
from datetime import datetime, timezone

from src.schemas.pet_schema import PetCreate
from src.models.pet import Pet
from src.config.database.db_helper import db_helper


async def crate_new_pet(pet: PetCreate):
    id_pet = uuid.uuid4()
    date = datetime.now(timezone.utc)
    query = Pet.insert().values(
        id=id_pet, name=pet.name, age=pet.year, ped_type=pet.type, created_at=date
    )
    create_pet = await db_helper.get_db_session.exucute_query(query)

    return {**pet.dict(), "id": id_pet, "created_at": date}
