from astarteplatform.msghub import astarte_message_pb2 as _astarte_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Node(_message.Message):
    __slots__ = ["uuid", "interface_jsons"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_JSONS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    interface_jsons: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, uuid: _Optional[str] = ..., interface_jsons: _Optional[_Iterable[bytes]] = ...) -> None: ...

class NodeMessage(_message.Message):
    __slots__ = ["uuid", "astarte_message"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    astarte_message: _astarte_message_pb2.AstarteMessage
    def __init__(self, uuid: _Optional[str] = ..., astarte_message: _Optional[_Union[_astarte_message_pb2.AstarteMessage, _Mapping]] = ...) -> None: ...
