from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db.entities import Base
from db.entities.mixin import BaseMixin


class Book(BaseMixin, Base):
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))
    author: Mapped['Author'] = relationship(back_populates='books', lazy='selectin')
