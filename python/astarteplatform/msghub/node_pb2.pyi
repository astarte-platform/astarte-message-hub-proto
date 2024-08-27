from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Node(_message.Message):
    __slots__ = ("interfaces_json",)
    INTERFACES_JSON_FIELD_NUMBER: _ClassVar[int]
    interfaces_json: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, interfaces_json: _Optional[_Iterable[str]] = ...) -> None: ...
