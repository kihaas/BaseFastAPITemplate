from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from .base import Base


class Product(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
