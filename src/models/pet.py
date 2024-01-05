import datetime
import enum

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class TypePet(enum.Enum):
    DOG = "dog"
    CAT = "cat"


class Pet(Base):
    __tablename__ = "pet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]
    is_photo: Mapped[bool]
    tupe_pet: Mapped[TypePet]
    created_at: Mapped[datetime.datetime]
