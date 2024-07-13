from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    author_id: int


class CreateUpdateBookSchema(BaseModel):
    title: str
    author_id: int
