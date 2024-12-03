from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Ownership(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE: _ClassVar[Ownership]
    SERVER: _ClassVar[Ownership]
DEVICE: Ownership
SERVER: Ownership

class InterfacesJson(_message.Message):
    __slots__ = ("interfaces_json",)
    INTERFACES_JSON_FIELD_NUMBER: _ClassVar[int]
    interfaces_json: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, interfaces_json: _Optional[_Iterable[str]] = ...) -> None: ...

class InterfacesName(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...
