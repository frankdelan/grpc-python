from google.protobuf.json_format import MessageToDict, MessageToJson

from db.repositories.book import BookRepository
from protos import book_pb2_grpc, book_pb2
from schemas.book import BookSchema


class BookService(book_pb2_grpc.BookServiceServicer):
    def __init__(self):
        self.repository = BookRepository()

    async def CreateBook(self, request, context):
        book = await self.repository.create(**MessageToDict(request, preserving_proto_field_name=True))
        print("CreateBook from BookService")
        if book:
            return book_pb2.CreateBookResponse(book=book.to_dict())
        return book_pb2.CreateBookResponse()

    async def RetrieveBook(self, request, context):
        book = await self.repository.retrieve(request.id)
        print("RetrieveBook from BookService")
        if book:
            return book_pb2.RetrieveBookResponse(book=book.to_dict())
        return book_pb2.RetrieveBookResponse()

