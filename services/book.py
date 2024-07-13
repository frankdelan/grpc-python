from google.protobuf.json_format import MessageToDict

from db.repositories.book import BookRepository
from protos import book_pb2_grpc, book_pb2


class BookService(book_pb2_grpc.BookServiceServicer):
    def __init__(self):
        self.repository = BookRepository()

    async def CreateBook(self, request, context):
        book = await self.repository.create(MessageToDict(request, preserving_proto_field_name=True))
        if book:
            return book_pb2.SingleBookResponse(book=book.to_dict())
        return book_pb2.SingleBookResponse()

    async def RetrieveBook(self, request, context):
        book = await self.repository.retrieve(request.id)
        if book:
            return book_pb2.SingleBookResponse(book=book.to_dict())
        return book_pb2.SingleBookResponse()

    async def UpdateBook(self, request, context):
        book = await self.repository.update(MessageToDict(request, preserving_proto_field_name=True))
        if book:
            return book_pb2.SingleBookResponse(book=book.to_dict())
        return book_pb2.SingleBookResponse()

    async def DeleteBook(self, request, context):
        book = await self.repository.delete(request.id)
        if book:
            return book_pb2.SingleBookResponse(book=book.to_dict())
        return book_pb2.SingleBookResponse()
