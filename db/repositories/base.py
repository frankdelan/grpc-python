from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete

from db.settings.db_config import async_session_factory


class BaseRepository(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def retrieve(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs):
        raise NotImplementedError


class DatabaseRepository(BaseRepository):
    model = None

    async def create(self, **kwargs):
        async with async_session_factory() as session:
            stmt = insert(self.model).values(**kwargs).returning(self.model)
            obj = await session.execute(stmt)
            await session.commit()
            return obj.scalar_one_or_none()

    async def retrieve(self, id: int):
        async with async_session_factory() as session:
            query = select(self.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def update(self, id: int, **kwargs):
        async with async_session_factory() as session:
            query = update(self.model).filter_by(id=id).values(**kwargs).returning(self.model)
            obj = await session.execute(query)
            await session.commit()
            return obj.scalar_one_or_none()

    async def delete(self, id: int):
        async with async_session_factory() as session:
            query = delete(self.model).filter_by(id=id).returning(self.model)
            obj = await session.execute(query)
            await session.commit()
            return obj.scalar_one_or_none()