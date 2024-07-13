from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class CreateAuthorRequest(_message.Message):
    __slots__ = ("name", "age", "alive")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    alive: bool
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ..., alive: bool = ...) -> None: ...

class CreateAuthorResponse(_message.Message):
    __slots__ = ("author",)
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    author: Author
    def __init__(self, author: _Optional[_Union[Author, _Mapping]] = ...) -> None: ...

class RetrieveAuthorRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RetrieveAuthorResponse(_message.Message):
    __slots__ = ("author",)
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    author: Author
    def __init__(self, author: _Optional[_Union[Author, _Mapping]] = ...) -> None: ...
