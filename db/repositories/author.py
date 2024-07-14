from db.entities import Author
from db.repositories.base import DatabaseRepository


class AuthorRepository(DatabaseRepository):
    model = Author
