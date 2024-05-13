from astarteplatform.msghub import interface_pb2 as _interface_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Node(_message.Message):
    __slots__ = ("uuid", "interfaces_json")
    UUID_FIELD_NUMBER: _ClassVar[int]
    INTERFACES_JSON_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    interfaces_json: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[str] = ..., interfaces_json: _Optional[_Iterable[str]] = ...) -> None: ...
