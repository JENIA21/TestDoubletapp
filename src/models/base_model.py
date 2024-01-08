import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstarct__ = True

    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid.uuid4()))
    created_at: Mapped[datetime] = mapped_column(default=func.now())


@declared_attr.directive
def __tablename__(cls) -> str:
    return f"{cls.__name__.lower()}s"
