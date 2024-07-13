from db.entities import Book
from db.repositories.base import DatabaseRepository


class BookRepository(DatabaseRepository):
    model = Book
