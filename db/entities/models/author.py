from sqlalchemy.orm import Mapped

from db.entities import Base
from db.entities.mixin import BaseMixin


class Author(BaseMixin, Base):
    __tablename__ = 'author'

    name: Mapped[str]
    age: Mapped[int]
    alive: Mapped[bool]
