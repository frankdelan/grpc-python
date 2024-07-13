import asyncio

from grpc import aio
from protos import book_pb2_grpc

from db.entities import Book
from db.config import Settings
from db.settings.db_config import check_table_exists, create_tables
from services.book import BookService


async def start(address: str):
    if await check_table_exists(Book.__tablename__):
        await create_tables()
    server = aio.server()
    book_pb2_grpc.add_BookServiceServicer_to_server(
        BookService(), server
    )
    server.add_insecure_port(address)
    await server.start()
    print(f"BookServer starts on {address}")
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(start(Settings.BOOK_GRPC_SERVER_ADDR))
