from google.protobuf.json_format import MessageToDict

from db.repositories.author import AuthorRepository
from protos import book_pb2_grpc, author_pb2


class AuthorService(book_pb2_grpc.BookServiceServicer):
    def __init__(self):
        self.repository = AuthorRepository()

    async def CreateAuthor(self, request, context):
        author = await self.repository.create(MessageToDict(request, preserving_proto_field_name=True))
        if author:
            return author_pb2.SingleAuthorResponse(author=author.to_dict())
        return author_pb2.SingleAuthorResponse()

    async def RetrieveAuthor(self, request, context):
        author = await self.repository.retrieve(request.id)
        if author:
            return author_pb2.SingleAuthorResponse(author=author.to_dict())
        return author_pb2.SingleAuthorResponse()

    async def UpdateAuthor(self, request, context):
        author = await self.repository.update(MessageToDict(request, preserving_proto_field_name=True))
        if author:
            return author_pb2.SingleAuthorResponse(author=author.to_dict())
        return author_pb2.SingleAuthorResponse()

    async def DeleteAuthor(self, request, context):
        author = await self.repository.delete(request.id)
        if author:
            return author_pb2.SingleAuthorResponse(author=author.to_dict())
        return author_pb2.SingleAuthorResponse()