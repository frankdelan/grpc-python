from grpc import aio

from db.config import settings
from protos import author_pb2_grpc


async def author_grpc_client():
    channel = aio.insecure_channel(settings.AUTHOR_GRPC_SERVER_ADDR)
    client = author_pb2_grpc.AuthorServiceStub(channel)
    return client
