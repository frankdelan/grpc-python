import asyncio

from grpc import aio
from protos import author_pb2_grpc

from db.config import Settings
from db.settings.db_config import create_tables
from services.author import AuthorService


async def start(address: str):
    await create_tables()
    server = aio.server()
    author_pb2_grpc.add_AuthorServiceServicer_to_server(
        AuthorService(), server
    )
    server.add_insecure_port(address)
    await server.start()
    print(f"AuthorServer starts on {address}")
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(start(Settings.AUTHOR_GRPC_SERVER_ADDR))