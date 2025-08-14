from google.protobuf.json_format import MessageToDict
from db.repositories.author import AuthorRepository
from protos import author_pb2
from protos.author_pb2_grpc import AuthorServiceServicer

class AuthorService(AuthorServiceServicer):
    def __init__(self):
        self.repository = AuthorRepository()
        
    async def CreateAuthor(self, request, context) -> author_pb2.SingleAuthorResponse:
        author = await self.repository.create(
            MessageToDict(request, preserving_proto_field_name=True, always_print_fields_with_no_presence=True)
        )
        if author:
            return author_pb2.SingleAuthorResponse(**author.to_dict())
        return author_pb2.SingleAuthorResponse()
    
    async def RetrieveAuthor(self, request, context) -> author_pb2.SingleAuthorResponse:
        author = await self.repository.retrieve(id=request.id)
        if author:
            return author_pb2.AuthorWithBooksResponse(
                **author.to_dict(),
                books=[book.to_dict() for book in author.books],
            )
        return author_pb2.AuthorWithBooksResponse()
