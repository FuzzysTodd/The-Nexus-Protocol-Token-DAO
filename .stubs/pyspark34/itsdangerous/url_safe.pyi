import typing as _t
from .encoding import base64_decode as base64_decode, base64_encode as base64_encode
from .exc import BadPayload as BadPayload
from .serializer import Serializer as Serializer
from .timed import TimedSerializer as TimedSerializer
from _typeshed import Incomplete

class URLSafeSerializerMixin(Serializer):
    """Mixed in with a regular serializer it will attempt to zlib
    compress the string to make it shorter if necessary. It will also
    base64 encode the string so that it can safely be placed in a URL.
    """
    default_serializer: Incomplete
    def load_payload(self, payload: bytes, *args: _t.Any, serializer: _t.Any | None = None, **kwargs: _t.Any) -> _t.Any: ...
    def dump_payload(self, obj: _t.Any) -> bytes: ...

class URLSafeSerializer(URLSafeSerializerMixin, Serializer):
    """Works like :class:`.Serializer` but dumps and loads into a URL
    safe string consisting of the upper and lowercase character of the
    alphabet as well as ``'_'``, ``'-'`` and ``'.'``.
    """
class URLSafeTimedSerializer(URLSafeSerializerMixin, TimedSerializer):
    """Works like :class:`.TimedSerializer` but dumps and loads into a
    URL safe string consisting of the upper and lowercase character of
    the alphabet as well as ``'_'``, ``'-'`` and ``'.'``.
    """
