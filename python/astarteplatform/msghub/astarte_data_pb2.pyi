from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AstarteDoubleArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class AstarteIntegerArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class AstarteBooleanArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, values: _Optional[_Iterable[bool]] = ...) -> None: ...

class AstarteLongIntegerArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class AstarteStringArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class AstarteBinaryBlobArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, values: _Optional[_Iterable[bytes]] = ...) -> None: ...

class AstarteDateTimeArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, values: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class AstarteData(_message.Message):
    __slots__ = ("double", "integer", "boolean", "long_integer", "string", "binary_blob", "date_time", "double_array", "integer_array", "boolean_array", "long_integer_array", "string_array", "binary_blob_array", "date_time_array")
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    LONG_INTEGER_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BINARY_BLOB_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_ARRAY_FIELD_NUMBER: _ClassVar[int]
    LONG_INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
    STRING_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BINARY_BLOB_ARRAY_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_ARRAY_FIELD_NUMBER: _ClassVar[int]
    double: float
    integer: int
    boolean: bool
    long_integer: int
    string: str
    binary_blob: bytes
    date_time: _timestamp_pb2.Timestamp
    double_array: AstarteDoubleArray
    integer_array: AstarteIntegerArray
    boolean_array: AstarteBooleanArray
    long_integer_array: AstarteLongIntegerArray
    string_array: AstarteStringArray
    binary_blob_array: AstarteBinaryBlobArray
    date_time_array: AstarteDateTimeArray
    def __init__(self, double: _Optional[float] = ..., integer: _Optional[int] = ..., boolean: bool = ..., long_integer: _Optional[int] = ..., string: _Optional[str] = ..., binary_blob: _Optional[bytes] = ..., date_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., double_array: _Optional[_Union[AstarteDoubleArray, _Mapping]] = ..., integer_array: _Optional[_Union[AstarteIntegerArray, _Mapping]] = ..., boolean_array: _Optional[_Union[AstarteBooleanArray, _Mapping]] = ..., long_integer_array: _Optional[_Union[AstarteLongIntegerArray, _Mapping]] = ..., string_array: _Optional[_Union[AstarteStringArray, _Mapping]] = ..., binary_blob_array: _Optional[_Union[AstarteBinaryBlobArray, _Mapping]] = ..., date_time_array: _Optional[_Union[AstarteDateTimeArray, _Mapping]] = ...) -> None: ...

class AstarteDatastreamIndividual(_message.Message):
    __slots__ = ("data", "timestamp")
    DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    data: AstarteData
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, data: _Optional[_Union[AstarteData, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AstarteDatastreamObject(_message.Message):
    __slots__ = ("data", "timestamp")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AstarteData
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AstarteData, _Mapping]] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    data: _containers.MessageMap[str, AstarteData]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, data: _Optional[_Mapping[str, AstarteData]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AstartePropertyIndividual(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: AstarteData
    def __init__(self, data: _Optional[_Union[AstarteData, _Mapping]] = ...) -> None: ...
