import asyncio
from grpc import aio

from db.config import settings
from db.settings.db_config import create_tables

from protos import author_pb2_grpc
from services.author import AuthorService


async def start(address: str):
    await create_tables()
    server = aio.server()
    author_pb2_grpc.add_AuthorServiceServicer_to_server(
        AuthorService(), server,
    )
    server.add_insecure_port(address)
    await server.start()
    print(f"BookServer starts on {address}")
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(start(settings.AUTHOR_GRPC_SERVER_ADDR))
