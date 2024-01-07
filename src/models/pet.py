import enum

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from models.base_model import Base


class TypePet(enum.Enum):
    dog = "dog"
    cat = "cat"


class Pet(Base):
    __tablename__ = "pet"

    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]
    pet_type: Mapped[str] = mapped_column(Enum(TypePet))
