import json
from .web import Request as Request, StreamResponse as StreamResponse
from _typeshed import Incomplete
from typing import Any, Callable, Tuple
from yarl import URL

DEFAULT_JSON_ENCODER = json.dumps
DEFAULT_JSON_DECODER = json.loads
Byteish = bytes | bytearray | memoryview
JSONEncoder = Callable[[Any], str]
JSONDecoder = Callable[[str], Any]
LooseHeaders: Incomplete
RawHeaders = Tuple[Tuple[bytes, bytes], ...]
StrOrURL = str | URL
LooseCookiesMappings: Incomplete
LooseCookiesIterables: Incomplete
LooseCookies: Incomplete
Handler: Incomplete
PathLike: Incomplete
