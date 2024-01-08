import enum

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base_model import Base


class TypePet(enum.Enum):
    dog = "dog"
    cat = "cat"


class Pet(Base):
    __tablename__ = "pet"
    __table_args__ = {'extend_existing': True}

    name: Mapped[str] = mapped_column(String(50))
    year: Mapped[int]
    type: Mapped[str] = mapped_column(Enum(TypePet))
