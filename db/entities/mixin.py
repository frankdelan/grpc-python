from sqlalchemy import inspect
from sqlalchemy.orm import Mapped, mapped_column


class BaseMixin:

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    def to_dict(self, ):
        colums_names = inspect(self.__class__).columns.keys()
        return {k: self.__dict__[k] for k in colums_names}
