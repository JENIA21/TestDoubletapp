from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.models.base_model import Base


class Photo(Base):
    __tablename__ = "photo"

    id_photo: Mapped[str] = mapped_column(String(100))
    pet_id: Mapped[str] = mapped_column(ForeignKey("pet.id"))
