import enum

from sqlalchemy import String
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

from  base_model import Base


class TypePet(enum.Enum):
    DOG = "dog"
    CAT = "cat"


class Pet(Base):
    __tablename__ = "pet"

    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]
    is_photo: Mapped[bool]
    pet_type: Mapped[TypePet]
