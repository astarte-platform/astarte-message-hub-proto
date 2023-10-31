from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InterfaceJson(_message.Message):
    __slots__ = ["interface_json"]
    INTERFACE_JSON_FIELD_NUMBER: _ClassVar[int]
    interface_json: bytes
    def __init__(self, interface_json: _Optional[bytes] = ...) -> None: ...
