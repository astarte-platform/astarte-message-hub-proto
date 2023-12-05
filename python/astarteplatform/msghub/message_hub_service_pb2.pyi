from google.protobuf import empty_pb2 as _empty_pb2
from astarteplatform.msghub import astarte_message_pb2 as _astarte_message_pb2
from astarteplatform.msghub import astarte_type_pb2 as _astarte_type_pb2
from astarteplatform.msghub import message_hub_error_pb2 as _message_hub_error_pb2
from astarteplatform.msghub import node_pb2 as _node_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageHubResult(_message.Message):
    __slots__ = ["empty_message", "hub_error"]
    EMPTY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
    empty_message: _empty_pb2.Empty
    hub_error: _message_hub_error_pb2.MessageHubError
    def __init__(self, empty_message: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., hub_error: _Optional[_Union[_message_hub_error_pb2.MessageHubError, _Mapping]] = ...) -> None: ...
