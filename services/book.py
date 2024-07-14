from google.protobuf.json_format import MessageToDict

from db.repositories.book import BookRepository
from protos import book_pb2_grpc, book_pb2, author_pb2, author_pb2_grpc
from clients.author_client import author_grpc_client


class BookService(book_pb2_grpc.BookServiceServicer):
    def __init__(self, author_stub: author_pb2_grpc.AuthorServiceStub = author_grpc_client()):
        self.repository = BookRepository()
        self.author_stub: author_pb2_grpc.AuthorServiceStub = author_stub

    async def CreateBook(self, request, context):
        book = await self.repository.create(MessageToDict(request, preserving_proto_field_name=True))
        if book:
            author_stub = await author_grpc_client()
            author = await author_stub.RetrieveAuthor(
                author_pb2.RetrieveAuthorRequest(
                    id=book.author_id
                ), timeout=5
            )
            return book_pb2.SingleBookResponse(
                id=book.id,
                title=book.title,
                author=author_pb2.Author(**MessageToDict(author)['author'])
            )
        else:
            return book_pb2.SingleBookResponse()

    async def RetrieveBook(self, request, context):
        book = await self.repository.retrieve(request.id)
        if book:
            author_stub = await author_grpc_client()
            author = await author_stub.RetrieveAuthor(
                author_pb2.RetrieveAuthorRequest(
                    id=book.author_id
                ), timeout=5
            )
            return book_pb2.SingleBookResponse(
                id=book.id,
                title=book.title,
                author=author_pb2.Author(**MessageToDict(author)['author'])
            )
        else:
            return book_pb2.SingleBookResponse()

    async def UpdateBook(self, request, context):
        book = await self.repository.update(MessageToDict(request, preserving_proto_field_name=True))
        if book:
            author_stub = await author_grpc_client()
            author = await author_stub.RetrieveAuthor(
                author_pb2.RetrieveAuthorRequest(
                    id=book.author_id
                ), timeout=5
            )

            return book_pb2.SingleBookResponse(
                id=book.id,
                title=book.title,
                author=author_pb2.Author(**MessageToDict(author)['author'])
            )
        else:
            return book_pb2.SingleBookResponse()

    async def DeleteBook(self, request, context):
        book = await self.repository.delete(request.id)
        if book:
            author_stub = await author_grpc_client()
            author = await author_stub.RetrieveAuthor(
                author_pb2.RetrieveAuthorRequest(
                    id=book.author_id
                ), timeout=5
            )
            return book_pb2.SingleBookResponse(
                id=book.id,
                title=book.title,
                author=author_pb2.Author(**MessageToDict(author)['author'])
            )
        else:
            return book_pb2.SingleBookResponse()
