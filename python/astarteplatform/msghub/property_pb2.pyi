from astarteplatform.msghub import astarte_data_pb2 as _astarte_data_pb2
from astarteplatform.msghub import interface_pb2 as _interface_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Property(_message.Message):
    __slots__ = ("path", "data")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    path: str
    data: _astarte_data_pb2.AstarteData
    def __init__(self, path: _Optional[str] = ..., data: _Optional[_Union[_astarte_data_pb2.AstarteData, _Mapping]] = ...) -> None: ...

class InterfaceProperties(_message.Message):
    __slots__ = ("ownership", "version_major", "properties")
    OWNERSHIP_FIELD_NUMBER: _ClassVar[int]
    VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ownership: _interface_pb2.Ownership
    version_major: int
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    def __init__(self, ownership: _Optional[_Union[_interface_pb2.Ownership, str]] = ..., version_major: _Optional[int] = ..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ...) -> None: ...

class StoredProperties(_message.Message):
    __slots__ = ("interface_properties",)
    class InterfacePropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InterfaceProperties
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InterfaceProperties, _Mapping]] = ...) -> None: ...
    INTERFACE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    interface_properties: _containers.MessageMap[str, InterfaceProperties]
    def __init__(self, interface_properties: _Optional[_Mapping[str, InterfaceProperties]] = ...) -> None: ...

class StoredPropertiesFilter(_message.Message):
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
