from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageHubError(_message.Message):
    __slots__ = ["error_code", "error_description"]
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[MessageHubError.ErrorCode]
        ASTARTE_INVALID_DATA: _ClassVar[MessageHubError.ErrorCode]
        ASTARTE_SDK_ERROR: _ClassVar[MessageHubError.ErrorCode]
        CONVERSION_ERROR: _ClassVar[MessageHubError.ErrorCode]
        ACK_ID_UNKNOWN: _ClassVar[MessageHubError.ErrorCode]
        ACK_ID_NOT_VALID: _ClassVar[MessageHubError.ErrorCode]
    UNKNOWN: MessageHubError.ErrorCode
    ASTARTE_INVALID_DATA: MessageHubError.ErrorCode
    ASTARTE_SDK_ERROR: MessageHubError.ErrorCode
    CONVERSION_ERROR: MessageHubError.ErrorCode
    ACK_ID_UNKNOWN: MessageHubError.ErrorCode
    ACK_ID_NOT_VALID: MessageHubError.ErrorCode
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    error_code: MessageHubError.ErrorCode
    error_description: str
    def __init__(self, error_code: _Optional[_Union[MessageHubError.ErrorCode, str]] = ..., error_description: _Optional[str] = ...) -> None: ...
