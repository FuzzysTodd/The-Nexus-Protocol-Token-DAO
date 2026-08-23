import typing
import typing as _t
import typing_extensions as _te
from .encoding import base64_decode as base64_decode, base64_encode as base64_encode, bytes_to_int as bytes_to_int, int_to_bytes as int_to_bytes, want_bytes as want_bytes
from .exc import BadSignature as BadSignature, BadTimeSignature as BadTimeSignature, SignatureExpired as SignatureExpired
from .serializer import Serializer as Serializer
from .signer import Signer as Signer
from datetime import datetime

class TimestampSigner(Signer):
    """Works like the regular :class:`.Signer` but also records the time
    of the signing and can be used to expire signatures. The
    :meth:`unsign` method can raise :exc:`.SignatureExpired` if the
    unsigning failed because the signature is expired.
    """
    def get_timestamp(self) -> int:
        """Returns the current timestamp. The function must return an
        integer.
        """
    def timestamp_to_datetime(self, ts: int) -> datetime:
        """Convert the timestamp from :meth:`get_timestamp` into an
        aware :class`datetime.datetime` in UTC.

        .. versionchanged:: 2.0
            The timestamp is returned as a timezone-aware ``datetime``
            in UTC rather than a naive ``datetime`` assumed to be UTC.
        """
    def sign(self, value: _t_str_bytes) -> bytes:
        """Signs the given string and also attaches time information."""
    @typing.overload
    def unsign(self, signed_value: _t_str_bytes, max_age: _t_opt_int = None, return_timestamp: _te.Literal[False] = False) -> bytes: ...
    @typing.overload
    def unsign(self, signed_value: _t_str_bytes, max_age: _t_opt_int = None, return_timestamp: _te.Literal[True] = True) -> _t.Tuple[bytes, datetime]: ...
    def validate(self, signed_value: _t_str_bytes, max_age: _t_opt_int = None) -> bool:
        """Only validates the given signed value. Returns ``True`` if
        the signature exists and is valid."""

class TimedSerializer(Serializer):
    """Uses :class:`TimestampSigner` instead of the default
    :class:`.Signer`.
    """
    default_signer: _t.Type[TimestampSigner]
    def iter_unsigners(self, salt: _t_opt_str_bytes = None) -> _t.Iterator[TimestampSigner]: ...
    def loads(self, s: _t_str_bytes, max_age: _t_opt_int = None, return_timestamp: bool = False, salt: _t_opt_str_bytes = None) -> _t.Any:
        """Reverse of :meth:`dumps`, raises :exc:`.BadSignature` if the
        signature validation fails. If a ``max_age`` is provided it will
        ensure the signature is not older than that time in seconds. In
        case the signature is outdated, :exc:`.SignatureExpired` is
        raised. All arguments are forwarded to the signer's
        :meth:`~TimestampSigner.unsign` method.
        """
    def loads_unsafe(self, s: _t_str_bytes, max_age: _t_opt_int = None, salt: _t_opt_str_bytes = None) -> _t.Tuple[bool, _t.Any]: ...
