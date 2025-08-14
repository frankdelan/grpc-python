from sqlalchemy import inspect
from sqlalchemy.orm import Mapped, mapped_column, declared_attr


class BaseMixin:

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    def to_dict(self) -> dict:
        # Метод для конвертации модели в словарь
        colums_names = inspect(self.__class__).columns.keys()
        return {k: self.__dict__[k] for k in colums_names}
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
        
