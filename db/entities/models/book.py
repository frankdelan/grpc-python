from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.entities import Base
from db.entities.mixin import BaseMixin


class Book(BaseMixin, Base):
    __tablename__ = 'book'

    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))

