from sqlalchemy.orm import Mapped, relationship

from db.entities import Base
from db.entities.mixin import BaseMixin


class Author(BaseMixin, Base):
    name: Mapped[str]
    age: Mapped[int]
    alive: Mapped[bool]
    books: Mapped[list['Book']] = relationship(back_populates='author', lazy='selectin')
