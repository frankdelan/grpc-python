from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

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

class Author(_message.Message):
    __slots__ = ("id", "name", "age", "alive")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    age: int
    alive: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., age: _Optional[int] = ..., alive: bool = ...) -> None: ...
