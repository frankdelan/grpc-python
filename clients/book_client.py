from grpc import aio

from db.config import settings
from protos import book_pb2_grpc


async def book_grpc_client():
    channel = aio.insecure_channel(settings.BOOK_GRPC_SERVER_ADDR)
    client = book_pb2_grpc.BookServiceStub(channel)
    return client
