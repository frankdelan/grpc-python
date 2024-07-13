from fastapi import Depends, HTTPException
from google.protobuf.json_format import MessageToDict
from grpc.aio import AioRpcError

from api_gateway.config import create_app
from schemas.book import CreateUpdateBookSchema, BookSchema
from protos import book_pb2_grpc, book_pb2
from clients import book_client

app = create_app(
    custom_static_url=True
)


@app.post('/books/create')
async def create_book(data: CreateUpdateBookSchema,
                      client: book_pb2_grpc.BookServiceStub = Depends(book_client.book_grpc_client)):
    try:
        book = await client.CreateBook(
            book_pb2.CreateBookRequest(
                **data.model_dump()
            ), timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    return MessageToDict(book)


@app.get('/books/{id}')
async def get_book(id: int,
                   client=Depends(book_client.book_grpc_client)):
    try:
        book = await client.RetrieveBook(
            book_pb2.RetrieveBookRequest(
                id=id,
            ), timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    return MessageToDict(book)


@app.put('/books/{id}')
async def update_book(id: int,
                      data: CreateUpdateBookSchema,
                      client=Depends(book_client.book_grpc_client)):
    try:
        book = await client.UpdateBook(
            book_pb2.UpdateBookRequest(
                id=id,
                **data.model_dump()
            ), timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    return MessageToDict(book)


@app.delete('/books/{id}')
async def delete_book(id: int,
                      client=Depends(book_client.book_grpc_client)):
    try:
        book = await client.DeleteBook(
            book_pb2.DeleteBookRequest(
                id=id,
            ), timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    return MessageToDict(book)
