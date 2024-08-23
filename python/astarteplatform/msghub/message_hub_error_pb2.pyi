from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageHubError(_message.Message):
    __slots__ = ("description", "source")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    description: str
    source: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, description: _Optional[str] = ..., source: _Optional[_Iterable[str]] = ...) -> None: ...
