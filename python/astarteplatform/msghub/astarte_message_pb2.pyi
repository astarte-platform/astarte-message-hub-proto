from astarteplatform.msghub import astarte_data_pb2 as _astarte_data_pb2
from astarteplatform.msghub import message_hub_error_pb2 as _message_hub_error_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_STATE_UNSPECIFIED: _ClassVar[ConnectionState]
    CONNECTION_STATE_IDLE: _ClassVar[ConnectionState]
    CONNECTION_STATE_UNREGISTERED: _ClassVar[ConnectionState]
    CONNECTION_STATE_REGISTERED: _ClassVar[ConnectionState]
    CONNECTION_STATE_CONNECTING: _ClassVar[ConnectionState]
    CONNECTION_STATE_CONNECTED: _ClassVar[ConnectionState]
    CONNECTION_STATE_DISCONNECTED: _ClassVar[ConnectionState]
    CONNECTION_STATE_UNKNOWN: _ClassVar[ConnectionState]
CONNECTION_STATE_UNSPECIFIED: ConnectionState
CONNECTION_STATE_IDLE: ConnectionState
CONNECTION_STATE_UNREGISTERED: ConnectionState
CONNECTION_STATE_REGISTERED: ConnectionState
CONNECTION_STATE_CONNECTING: ConnectionState
CONNECTION_STATE_CONNECTED: ConnectionState
CONNECTION_STATE_DISCONNECTED: ConnectionState
CONNECTION_STATE_UNKNOWN: ConnectionState

class MessageHubEvent(_message.Message):
    __slots__ = ("message", "error", "connection")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    message: AstarteMessage
    error: _message_hub_error_pb2.MessageHubError
    connection: ConnectionEvent
    def __init__(self, message: _Optional[_Union[AstarteMessage, _Mapping]] = ..., error: _Optional[_Union[_message_hub_error_pb2.MessageHubError, _Mapping]] = ..., connection: _Optional[_Union[ConnectionEvent, _Mapping]] = ...) -> None: ...

class AstarteMessage(_message.Message):
    __slots__ = ("interface_name", "path", "datastream_individual", "datastream_object", "property_individual")
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATASTREAM_INDIVIDUAL_FIELD_NUMBER: _ClassVar[int]
    DATASTREAM_OBJECT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_INDIVIDUAL_FIELD_NUMBER: _ClassVar[int]
    interface_name: str
    path: str
    datastream_individual: _astarte_data_pb2.AstarteDatastreamIndividual
    datastream_object: _astarte_data_pb2.AstarteDatastreamObject
    property_individual: _astarte_data_pb2.AstartePropertyIndividual
    def __init__(self, interface_name: _Optional[str] = ..., path: _Optional[str] = ..., datastream_individual: _Optional[_Union[_astarte_data_pb2.AstarteDatastreamIndividual, _Mapping]] = ..., datastream_object: _Optional[_Union[_astarte_data_pb2.AstarteDatastreamObject, _Mapping]] = ..., property_individual: _Optional[_Union[_astarte_data_pb2.AstartePropertyIndividual, _Mapping]] = ...) -> None: ...

class ConnectionEvent(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: ConnectionState
    def __init__(self, state: _Optional[_Union[ConnectionState, str]] = ...) -> None: ...
