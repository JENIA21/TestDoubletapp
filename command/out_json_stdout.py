import asyncio
import sys

from fastapi.encoders import jsonable_encoder

from sqlalchemy import select

from models.pet import Pet
from src.config.database.db_helper import db_helper
from src.schemas.pet_schema import PetGetResponse


async def get_multi(
        limit: int = 100,
        offset: int = 0,

) -> PetGetResponse:
    async with db_helper.get_db_session() as session:
        stmt = select(Pet).order_by("id").limit(limit).offset(offset)
        row = await session.execute(stmt)
    return row.scalars().all()

sys.stdout.write(f"{jsonable_encoder(asyncio.run(get_multi()))}")
