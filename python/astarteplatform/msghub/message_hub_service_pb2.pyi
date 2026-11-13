from astarteplatform.msghub import astarte_data_pb2 as _astarte_data_pb2
from astarteplatform.msghub import astarte_message_pb2 as _astarte_message_pb2
from astarteplatform.msghub import interface_pb2 as _interface_pb2
from astarteplatform.msghub import node_pb2 as _node_pb2
from astarteplatform.msghub import property_pb2 as _property_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IsRegisteredResponse(_message.Message):
    __slots__ = ("registered",)
    REGISTERED_FIELD_NUMBER: _ClassVar[int]
    registered: bool
    def __init__(self, registered: _Optional[bool] = ...) -> None: ...

class IsConnectedResponse(_message.Message):
    __slots__ = ("connected",)
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    connected: bool
    def __init__(self, connected: _Optional[bool] = ...) -> None: ...

class GetConnectionStateResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _astarte_message_pb2.ConnectionState
    def __init__(self, state: _Optional[_Union[_astarte_message_pb2.ConnectionState, str]] = ...) -> None: ...
