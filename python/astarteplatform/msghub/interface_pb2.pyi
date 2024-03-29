from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InterfaceJson(_message.Message):
    __slots__ = ("interface_json",)
    INTERFACE_JSON_FIELD_NUMBER: _ClassVar[int]
    interface_json: bytes
    def __init__(self, interface_json: _Optional[bytes] = ...) -> None: ...

class InterfacesJson(_message.Message):
    __slots__ = ("interfaces_json",)
    INTERFACES_JSON_FIELD_NUMBER: _ClassVar[int]
    interfaces_json: _containers.RepeatedCompositeFieldContainer[InterfaceJson]
    def __init__(self, interfaces_json: _Optional[_Iterable[_Union[InterfaceJson, _Mapping]]] = ...) -> None: ...

class InterfacesName(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...
