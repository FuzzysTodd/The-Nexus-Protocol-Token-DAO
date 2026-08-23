import asyncio
import datetime
import io
from .abc import AbstractStreamWriter
from .helpers import ChainMapProxy, ETag, HeadersMixin
from .http_parser import RawRequestMessage
from .http_writer import HttpVersion
from .multipart import MultipartReader
from .streams import StreamReader
from .typedefs import JSONDecoder, LooseHeaders, RawHeaders, StrOrURL
from .web_app import Application
from .web_protocol import RequestHandler
from .web_urldispatcher import UrlMappingMatchInfo
from _typeshed import Incomplete
from multidict import CIMultiDictProxy, MultiDictProxy
from typing import Any, Dict, Iterator, Mapping, MutableMapping, Tuple
from yarl import URL

__all__ = ['BaseRequest', 'FileField', 'Request']

class FileField:
    name: str
    filename: str
    file: io.BufferedReader
    content_type: str
    headers: CIMultiDictProxy[str]
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class BaseRequest(MutableMapping[str, Any], HeadersMixin):
    POST_METHODS: Incomplete
    ATTRS: Incomplete
    def __init__(self, message: RawRequestMessage, payload: StreamReader, protocol: RequestHandler, payload_writer: AbstractStreamWriter, task: asyncio.Task[None], loop: asyncio.AbstractEventLoop, *, client_max_size: int = ..., state: Dict[str, Any] | None = None, scheme: str | None = None, host: str | None = None, remote: str | None = None) -> None: ...
    def clone(self, *, method: str = ..., rel_url: StrOrURL = ..., headers: LooseHeaders = ..., scheme: str = ..., host: str = ..., remote: str = ...) -> BaseRequest:
        """Clone itself with replacement some attributes.

        Creates and returns a new instance of Request object. If no parameters
        are given, an exact copy is returned. If a parameter is not passed, it
        will reuse the one from the current request object.
        """
    @property
    def task(self) -> asyncio.Task[None]: ...
    @property
    def protocol(self) -> RequestHandler: ...
    @property
    def transport(self) -> asyncio.Transport | None: ...
    @property
    def writer(self) -> AbstractStreamWriter: ...
    def message(self) -> RawRequestMessage: ...
    def rel_url(self) -> URL: ...
    def loop(self) -> asyncio.AbstractEventLoop: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def secure(self) -> bool:
        """A bool indicating if the request is handled with SSL."""
    def forwarded(self) -> Tuple[Mapping[str, str], ...]:
        """A tuple containing all parsed Forwarded header(s).

        Makes an effort to parse Forwarded headers as specified by RFC 7239:

        - It adds one (immutable) dictionary per Forwarded 'field-value', ie
          per proxy. The element corresponds to the data in the Forwarded
          field-value added by the first proxy encountered by the client. Each
          subsequent item corresponds to those added by later proxies.
        - It checks that every value has valid syntax in general as specified
          in section 4: either a 'token' or a 'quoted-string'.
        - It un-escapes found escape sequences.
        - It does NOT validate 'by' and 'for' contents as specified in section
          6.
        - It does NOT validate 'host' contents (Host ABNF).
        - It does NOT validate 'proto' contents for valid URI scheme names.

        Returns a tuple containing one or more immutable dicts
        """
    def scheme(self) -> str:
        """A string representing the scheme of the request.

        Hostname is resolved in this order:

        - overridden value by .clone(scheme=new_scheme) call.
        - type of connection to peer: HTTPS if socket is SSL, HTTP otherwise.

        'http' or 'https'.
        """
    def method(self) -> str:
        """Read only property for getting HTTP method.

        The value is upper-cased str like 'GET', 'POST', 'PUT' etc.
        """
    def version(self) -> HttpVersion:
        """Read only property for getting HTTP version of request.

        Returns aiohttp.protocol.HttpVersion instance.
        """
    def host(self) -> str:
        """Hostname of the request.

        Hostname is resolved in this order:

        - overridden value by .clone(host=new_host) call.
        - HOST HTTP header
        - socket.getfqdn() value
        """
    def remote(self) -> str | None:
        """Remote IP of client initiated HTTP request.

        The IP is resolved in this order:

        - overridden value by .clone(remote=new_remote) call.
        - peername of opened socket
        """
    def url(self) -> URL: ...
    def path(self) -> str:
        """The URL including *PATH INFO* without the host or scheme.

        E.g., ``/app/blog``
        """
    def path_qs(self) -> str:
        """The URL including PATH_INFO and the query string.

        E.g, /app/blog?id=10
        """
    def raw_path(self) -> str:
        """The URL including raw *PATH INFO* without the host or scheme.

        Warning, the path is unquoted and may contains non valid URL characters

        E.g., ``/my%2Fpath%7Cwith%21some%25strange%24characters``
        """
    def query(self) -> MultiDictProxy[str]:
        """A multidict with all the variables in the query string."""
    def query_string(self) -> str:
        """The query string in the URL.

        E.g., id=10
        """
    def headers(self) -> CIMultiDictProxy[str]:
        """A case-insensitive multidict proxy with all headers."""
    def raw_headers(self) -> RawHeaders:
        """A sequence of pairs for all headers."""
    def if_modified_since(self) -> datetime.datetime | None:
        """The value of If-Modified-Since HTTP header, or None.

        This header is represented as a `datetime` object.
        """
    def if_unmodified_since(self) -> datetime.datetime | None:
        """The value of If-Unmodified-Since HTTP header, or None.

        This header is represented as a `datetime` object.
        """
    def if_match(self) -> Tuple[ETag, ...] | None:
        """The value of If-Match HTTP header, or None.

        This header is represented as a `tuple` of `ETag` objects.
        """
    def if_none_match(self) -> Tuple[ETag, ...] | None:
        """The value of If-None-Match HTTP header, or None.

        This header is represented as a `tuple` of `ETag` objects.
        """
    def if_range(self) -> datetime.datetime | None:
        """The value of If-Range HTTP header, or None.

        This header is represented as a `datetime` object.
        """
    def keep_alive(self) -> bool:
        """Is keepalive enabled by client?"""
    def cookies(self) -> Mapping[str, str]:
        """Return request cookies.

        A read-only dictionary-like object.
        """
    def http_range(self) -> slice:
        """The content of Range HTTP header.

        Return a slice instance.

        """
    def content(self) -> StreamReader:
        """Return raw payload stream."""
    @property
    def has_body(self) -> bool:
        """Return True if request's HTTP BODY can be read, False otherwise."""
    @property
    def can_read_body(self) -> bool:
        """Return True if request's HTTP BODY can be read, False otherwise."""
    def body_exists(self) -> bool:
        """Return True if request has HTTP BODY, False otherwise."""
    async def release(self) -> None:
        """Release request.

        Eat unread part of HTTP BODY if present.
        """
    async def read(self) -> bytes:
        """Read request body if present.

        Returns bytes object with full request content.
        """
    async def text(self) -> str:
        """Return BODY as text using encoding from .charset."""
    async def json(self, *, loads: JSONDecoder = ...) -> Any:
        """Return BODY as JSON."""
    async def multipart(self) -> MultipartReader:
        """Return async iterator to process BODY as multipart."""
    async def post(self) -> MultiDictProxy[str | bytes | FileField]:
        """Return POST parameters."""
    def get_extra_info(self, name: str, default: Any = None) -> Any:
        """Extra info from protocol transport"""
    def __eq__(self, other: object) -> bool: ...
    def __bool__(self) -> bool: ...

class Request(BaseRequest):
    ATTRS: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __setattr__(self, name: str, val: Any) -> None: ...
    def clone(self, *, method: str = ..., rel_url: StrOrURL = ..., headers: LooseHeaders = ..., scheme: str = ..., host: str = ..., remote: str = ...) -> Request: ...
    def match_info(self) -> UrlMappingMatchInfo:
        """Result of route resolving."""
    @property
    def app(self) -> Application:
        """Application instance."""
    @property
    def config_dict(self) -> ChainMapProxy: ...
