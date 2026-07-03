from _typeshed import Incomplete
from datetime import datetime

class BadData(Exception):
    """Raised if bad data of any sort was encountered. This is the base
    for all exceptions that ItsDangerous defines.

    .. versionadded:: 0.15
    """
    message: Incomplete
    def __init__(self, message: str) -> None: ...

class BadSignature(BadData):
    """Raised if a signature does not match."""
    payload: Incomplete
    def __init__(self, message: str, payload: _t_opt_any = None) -> None: ...

class BadTimeSignature(BadSignature):
    """Raised if a time-based signature is invalid. This is a subclass
    of :class:`BadSignature`.
    """
    date_signed: Incomplete
    def __init__(self, message: str, payload: _t_opt_any = None, date_signed: datetime | None = None) -> None: ...

class SignatureExpired(BadTimeSignature):
    """Raised if a signature timestamp is older than ``max_age``. This
    is a subclass of :exc:`BadTimeSignature`.
    """

class BadHeader(BadSignature):
    """Raised if a signed header is invalid in some form. This only
    happens for serializers that have a header that goes with the
    signature.

    .. versionadded:: 0.24
    """
    header: Incomplete
    original_error: Incomplete
    def __init__(self, message: str, payload: _t_opt_any = None, header: _t_opt_any = None, original_error: _t_opt_exc = None) -> None: ...

class BadPayload(BadData):
    """Raised if a payload is invalid. This could happen if the payload
    is loaded despite an invalid signature, or if there is a mismatch
    between the serializer and deserializer. The original exception
    that occurred during loading is stored on as :attr:`original_error`.

    .. versionadded:: 0.15
    """
    original_error: Incomplete
    def __init__(self, message: str, original_error: _t_opt_exc = None) -> None: ...
