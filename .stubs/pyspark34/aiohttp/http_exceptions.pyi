from .typedefs import _CIMultiDict
from _typeshed import Incomplete

__all__ = ['HttpProcessingError']

class HttpProcessingError(Exception):
    """HTTP error.

    Shortcut for raising HTTP errors with custom code, message and headers.

    code: HTTP Error code.
    message: (optional) Error message.
    headers: (optional) Headers to be sent in response, a list of pairs
    """
    code: int
    message: str
    headers: Incomplete
    def __init__(self, *, code: int | None = None, message: str = '', headers: _CIMultiDict | None = None) -> None: ...

class BadHttpMessage(HttpProcessingError):
    code: int
    message: str
    args: Incomplete
    def __init__(self, message: str, *, headers: _CIMultiDict | None = None) -> None: ...

class HttpBadRequest(BadHttpMessage):
    code: int
    message: str

class PayloadEncodingError(BadHttpMessage):
    """Base class for payload errors"""
class ContentEncodingError(PayloadEncodingError):
    """Content encoding error."""
class TransferEncodingError(PayloadEncodingError):
    """transfer encoding error."""
class ContentLengthError(PayloadEncodingError):
    """Not enough data for satisfy content length header."""

class LineTooLong(BadHttpMessage):
    args: Incomplete
    def __init__(self, line: str, limit: str = 'Unknown', actual_size: str = 'Unknown') -> None: ...

class InvalidHeader(BadHttpMessage):
    hdr: Incomplete
    args: Incomplete
    def __init__(self, hdr: bytes | str) -> None: ...

class BadStatusLine(BadHttpMessage):
    args: Incomplete
    line: Incomplete
    def __init__(self, line: str = '', error: str | None = None) -> None: ...

class InvalidURLError(BadHttpMessage): ...
