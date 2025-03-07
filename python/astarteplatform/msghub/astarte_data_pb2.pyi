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
    __slots__ = ("astarte_data_double", "astarte_data_integer", "astarte_data_boolean", "astarte_data_long_integer", "astarte_data_string", "astarte_data_binary_blob", "astarte_data_date_time", "astarte_data_double_array", "astarte_data_integer_array", "astarte_data_boolean_array", "astarte_data_long_integer_array", "astarte_data_string_array", "astarte_data_binary_blob_array", "astarte_data_date_time_array")
    ASTARTE_DATA_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_INTEGER_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_LONG_INTEGER_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_STRING_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_BINARY_BLOB_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_DOUBLE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_BOOLEAN_ARRAY_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_LONG_INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_STRING_ARRAY_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_BINARY_BLOB_ARRAY_FIELD_NUMBER: _ClassVar[int]
    ASTARTE_DATA_DATE_TIME_ARRAY_FIELD_NUMBER: _ClassVar[int]
    astarte_data_double: float
    astarte_data_integer: int
    astarte_data_boolean: bool
    astarte_data_long_integer: int
    astarte_data_string: str
    astarte_data_binary_blob: bytes
    astarte_data_date_time: _timestamp_pb2.Timestamp
    astarte_data_double_array: AstarteDoubleArray
    astarte_data_integer_array: AstarteIntegerArray
    astarte_data_boolean_array: AstarteBooleanArray
    astarte_data_long_integer_array: AstarteLongIntegerArray
    astarte_data_string_array: AstarteStringArray
    astarte_data_binary_blob_array: AstarteBinaryBlobArray
    astarte_data_date_time_array: AstarteDateTimeArray
    def __init__(self, astarte_data_double: _Optional[float] = ..., astarte_data_integer: _Optional[int] = ..., astarte_data_boolean: bool = ..., astarte_data_long_integer: _Optional[int] = ..., astarte_data_string: _Optional[str] = ..., astarte_data_binary_blob: _Optional[bytes] = ..., astarte_data_date_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., astarte_data_double_array: _Optional[_Union[AstarteDoubleArray, _Mapping]] = ..., astarte_data_integer_array: _Optional[_Union[AstarteIntegerArray, _Mapping]] = ..., astarte_data_boolean_array: _Optional[_Union[AstarteBooleanArray, _Mapping]] = ..., astarte_data_long_integer_array: _Optional[_Union[AstarteLongIntegerArray, _Mapping]] = ..., astarte_data_string_array: _Optional[_Union[AstarteStringArray, _Mapping]] = ..., astarte_data_binary_blob_array: _Optional[_Union[AstarteBinaryBlobArray, _Mapping]] = ..., astarte_data_date_time_array: _Optional[_Union[AstarteDateTimeArray, _Mapping]] = ...) -> None: ...

class AstarteDatastreamInidividual(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: AstarteData
    def __init__(self, data: _Optional[_Union[AstarteData, _Mapping]] = ...) -> None: ...

class AstarteDatastreamObject(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AstarteData
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AstarteData, _Mapping]] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.MessageMap[str, AstarteData]
    def __init__(self, data: _Optional[_Mapping[str, AstarteData]] = ...) -> None: ...

class AstartePropertyIndividual(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: AstarteData
    def __init__(self, data: _Optional[_Union[AstarteData, _Mapping]] = ...) -> None: ...
