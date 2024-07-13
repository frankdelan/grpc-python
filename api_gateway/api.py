from typing import Union

from fastapi import Depends, HTTPException
from google.protobuf.json_format import MessageToDict, MessageToJson
from grpc.aio import AioRpcError

from api_gateway.config import create_app
from schemas.book import CreateBookSchema, BookSchema
from protos import book_pb2_grpc, book_pb2
from clients import book_client

app = create_app(
    custom_static_url=True
)


@app.get("/")
def greets():
    return {'Hello world!': 123}


@app.post('/books/create')
async def create_book(data: CreateBookSchema,
                      client: book_pb2_grpc.BookServiceStub = Depends(book_client.book_grpc_client)):
    print('Before')
    book = await client.CreateBook(
        book_pb2.CreateBookRequest(
            **data.model_dump()
        ), timeout=5
    )
    print('After')
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
