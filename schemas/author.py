from pydantic import BaseModel


class AuthorSchema(BaseModel):
    id: int
    name: str
    age: int
    alive: bool


class CreateUpdateAuthorSchema(BaseModel):
    name: str
    age: int
    alive: bool
