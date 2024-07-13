from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ("id", "title", "author_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    author_id: int
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., author_id: _Optional[int] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ("title", "author_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    author_id: int
    def __init__(self, title: _Optional[str] = ..., author_id: _Optional[int] = ...) -> None: ...

class RetrieveBookRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UpdateBookRequest(_message.Message):
    __slots__ = ("id", "title", "author_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    author_id: int
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., author_id: _Optional[int] = ...) -> None: ...

class DeleteBookRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class SingleBookResponse(_message.Message):
    __slots__ = ("book",)
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: Book
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...
