import grpc

from db.config import Settings
from protos import author_pb2_grpc


async def author_grpc_client():
    channel = grpc.aio.insecure_channel(Settings.AUTHOR_GRPC_SERVER_ADDR)
    client = author_pb2_grpc.AuthorServiceStub(channel)
    return client
