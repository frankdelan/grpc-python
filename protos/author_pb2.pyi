from protos import entities_pb2 as _entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetrieveAuthorRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CreateAuthorRequest(_message.Message):
    __slots__ = ("name", "age", "alive")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    alive: bool
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ..., alive: bool = ...) -> None: ...

class SingleAuthorResponse(_message.Message):
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

class AuthorWithBooksResponse(_message.Message):
    __slots__ = ("id", "name", "age", "alive", "books")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    age: int
    alive: bool
    books: _containers.RepeatedCompositeFieldContainer[_entities_pb2.Book]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., age: _Optional[int] = ..., alive: bool = ..., books: _Optional[_Iterable[_Union[_entities_pb2.Book, _Mapping]]] = ...) -> None: ...
