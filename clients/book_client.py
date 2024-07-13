import grpc

from db.config import Settings
from protos import book_pb2_grpc


async def book_grpc_client():
    channel = grpc.aio.insecure_channel(Settings.BOOK_GRPC_SERVER_ADDR)
    client = book_pb2_grpc.BookServiceStub(channel)
    return client
