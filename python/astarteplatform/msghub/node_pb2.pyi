from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Node(_message.Message):
    __slots__ = ("interfaces_json", "connection_events")
    INTERFACES_JSON_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    interfaces_json: _containers.RepeatedScalarFieldContainer[str]
    connection_events: bool
    def __init__(self, interfaces_json: _Optional[_Iterable[str]] = ..., connection_events: _Optional[bool] = ...) -> None: ...
