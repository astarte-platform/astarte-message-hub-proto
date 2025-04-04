from astarteplatform.msghub import astarte_data_pb2 as _astarte_data_pb2
from astarteplatform.msghub import interface_pb2 as _interface_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Property(_message.Message):
    __slots__ = ("interface_name", "path", "version_major", "ownership", "data")
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    interface_name: str
    path: str
    version_major: int
    ownership: _interface_pb2.Ownership
    data: _astarte_data_pb2.AstarteData
    def __init__(self, interface_name: _Optional[str] = ..., path: _Optional[str] = ..., version_major: _Optional[int] = ..., ownership: _Optional[_Union[_interface_pb2.Ownership, str]] = ..., data: _Optional[_Union[_astarte_data_pb2.AstarteData, _Mapping]] = ...) -> None: ...

class StoredProperties(_message.Message):
    __slots__ = ("properties",)
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    def __init__(self, properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ...) -> None: ...

class PropertyFilter(_message.Message):
    __slots__ = ("ownership",)
    OWNERSHIP_FIELD_NUMBER: _ClassVar[int]
    ownership: _interface_pb2.Ownership
    def __init__(self, ownership: _Optional[_Union[_interface_pb2.Ownership, str]] = ...) -> None: ...

class PropertyIdentifier(_message.Message):
    __slots__ = ("interface_name", "path")
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    interface_name: str
    path: str
    def __init__(self, interface_name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...
