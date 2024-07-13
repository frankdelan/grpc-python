from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from db.config import Settings
from db.entities import Base

DATABASE_URL = (f'postgresql+asyncpg://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_HOST}:'
                f'{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DATABASE}')

async_engine = create_async_engine(DATABASE_URL)

async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)


async def check_table_exists(table_name) -> bool:
    async with async_engine.connect() as conn:
        metadata = Base.metadata
        await conn.run_sync(metadata.reflect)
        table = metadata.tables.get(table_name)
        if table is not None:
            return True
        else:
            return False


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
