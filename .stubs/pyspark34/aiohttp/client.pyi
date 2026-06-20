import asyncio
from .abc import AbstractCookieJar
from .client_exceptions import ClientConnectionError as ClientConnectionError, ClientConnectorCertificateError as ClientConnectorCertificateError, ClientConnectorError as ClientConnectorError, ClientConnectorSSLError as ClientConnectorSSLError, ClientError as ClientError, ClientHttpProxyError as ClientHttpProxyError, ClientOSError as ClientOSError, ClientPayloadError as ClientPayloadError, ClientProxyConnectionError as ClientProxyConnectionError, ClientResponseError as ClientResponseError, ClientSSLError as ClientSSLError, ContentTypeError as ContentTypeError, InvalidURL as InvalidURL, ServerConnectionError as ServerConnectionError, ServerDisconnectedError as ServerDisconnectedError, ServerFingerprintMismatch as ServerFingerprintMismatch, ServerTimeoutError as ServerTimeoutError, TooManyRedirects as TooManyRedirects, WSServerHandshakeError as WSServerHandshakeError
from .client_reqrep import ClientRequest as ClientRequest, ClientResponse as ClientResponse, Fingerprint as Fingerprint, RequestInfo as RequestInfo
from .client_ws import ClientWebSocketResponse as ClientWebSocketResponse
from .connector import BaseConnector as BaseConnector, NamedPipeConnector as NamedPipeConnector, TCPConnector as TCPConnector, UnixConnector as UnixConnector
from .helpers import BasicAuth
from .http import HttpVersion
from .tracing import TraceConfig
from .typedefs import JSONEncoder, LooseCookies, LooseHeaders, StrOrURL
from _typeshed import Incomplete
from multidict import CIMultiDict, istr
from ssl import SSLContext
from types import TracebackType
from typing import Any, Awaitable, Callable, Coroutine, FrozenSet, Generator, Generic, Iterable, List, Mapping, Tuple, Type

__all__ = ['ClientConnectionError', 'ClientConnectorCertificateError', 'ClientConnectorError', 'ClientConnectorSSLError', 'ClientError', 'ClientHttpProxyError', 'ClientOSError', 'ClientPayloadError', 'ClientProxyConnectionError', 'ClientResponseError', 'ClientSSLError', 'ContentTypeError', 'InvalidURL', 'ServerConnectionError', 'ServerDisconnectedError', 'ServerFingerprintMismatch', 'ServerTimeoutError', 'TooManyRedirects', 'WSServerHandshakeError', 'ClientRequest', 'ClientResponse', 'Fingerprint', 'RequestInfo', 'BaseConnector', 'TCPConnector', 'UnixConnector', 'NamedPipeConnector', 'ClientWebSocketResponse', 'ClientSession', 'ClientTimeout', 'request']

SSLContext = object

class ClientTimeout:
    total: float | None
    connect: float | None
    sock_read: float | None
    sock_connect: float | None
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ClientSession:
    """First-class interface for making HTTP requests."""
    ATTRS: Incomplete
    def __init__(self, base_url: StrOrURL | None = None, *, connector: BaseConnector | None = None, loop: asyncio.AbstractEventLoop | None = None, cookies: LooseCookies | None = None, headers: LooseHeaders | None = None, skip_auto_headers: Iterable[str] | None = None, auth: BasicAuth | None = None, json_serialize: JSONEncoder = ..., request_class: Type[ClientRequest] = ..., response_class: Type[ClientResponse] = ..., ws_response_class: Type[ClientWebSocketResponse] = ..., version: HttpVersion = ..., cookie_jar: AbstractCookieJar | None = None, connector_owner: bool = True, raise_for_status: bool = False, read_timeout: float | object = ..., conn_timeout: float | None = None, timeout: object | ClientTimeout = ..., auto_decompress: bool = True, trust_env: bool = False, requote_redirect_url: bool = True, trace_configs: List[TraceConfig] | None = None, read_bufsize: int = ..., fallback_charset_resolver: _CharsetResolver = ...) -> None: ...
    def __init_subclass__(cls) -> None: ...
    def __setattr__(self, name: str, val: Any) -> None: ...
    def __del__(self, _warnings: Any = ...) -> None: ...
    def request(self, method: str, url: StrOrURL, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP request."""
    def ws_connect(self, url: StrOrURL, *, method: str = ..., protocols: Iterable[str] = (), timeout: float = 10.0, receive_timeout: float | None = None, autoclose: bool = True, autoping: bool = True, heartbeat: float | None = None, auth: BasicAuth | None = None, origin: str | None = None, params: Mapping[str, str] | None = None, headers: LooseHeaders | None = None, proxy: StrOrURL | None = None, proxy_auth: BasicAuth | None = None, ssl: SSLContext | bool | None | Fingerprint = None, verify_ssl: bool | None = None, fingerprint: bytes | None = None, ssl_context: SSLContext | None = None, proxy_headers: LooseHeaders | None = None, compress: int = 0, max_msg_size: int = ...) -> _WSRequestContextManager:
        """Initiate websocket connection."""
    def get(self, url: StrOrURL, *, allow_redirects: bool = True, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP GET request."""
    def options(self, url: StrOrURL, *, allow_redirects: bool = True, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP OPTIONS request."""
    def head(self, url: StrOrURL, *, allow_redirects: bool = False, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP HEAD request."""
    def post(self, url: StrOrURL, *, data: Any = None, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP POST request."""
    def put(self, url: StrOrURL, *, data: Any = None, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP PUT request."""
    def patch(self, url: StrOrURL, *, data: Any = None, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP PATCH request."""
    def delete(self, url: StrOrURL, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP DELETE request."""
    async def close(self) -> None:
        """Close underlying connector.

        Release all acquired resources.
        """
    @property
    def closed(self) -> bool:
        """Is client session closed.

        A readonly property.
        """
    @property
    def connector(self) -> BaseConnector | None:
        """Connector instance used for the session."""
    @property
    def cookie_jar(self) -> AbstractCookieJar:
        """The session cookies."""
    @property
    def version(self) -> Tuple[int, int]:
        """The session HTTP protocol version."""
    @property
    def requote_redirect_url(self) -> bool:
        """Do URL requoting on redirection handling."""
    @requote_redirect_url.setter
    def requote_redirect_url(self, val: bool) -> None:
        """Do URL requoting on redirection handling."""
    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        """Session's loop."""
    @property
    def timeout(self) -> ClientTimeout:
        """Timeout for the session."""
    @property
    def headers(self) -> CIMultiDict[str]:
        """The default headers of the client session."""
    @property
    def skip_auto_headers(self) -> FrozenSet[istr]:
        """Headers for which autogeneration should be skipped"""
    @property
    def auth(self) -> BasicAuth | None:
        """An object that represents HTTP Basic Authorization"""
    @property
    def json_serialize(self) -> JSONEncoder:
        """Json serializer callable"""
    @property
    def connector_owner(self) -> bool:
        """Should connector be closed on session closing"""
    @property
    def raise_for_status(self) -> bool | Callable[[ClientResponse], Awaitable[None]]:
        """Should `ClientResponse.raise_for_status()` be called for each response."""
    @property
    def auto_decompress(self) -> bool:
        """Should the body response be automatically decompressed."""
    @property
    def trust_env(self) -> bool:
        """
        Should proxies information from environment or netrc be trusted.

        Information is from HTTP_PROXY / HTTPS_PROXY environment variables
        or ~/.netrc file if present.
        """
    @property
    def trace_configs(self) -> List[TraceConfig]:
        """A list of TraceConfig instances used for client tracing"""
    def detach(self) -> None:
        """Detach connector from session without closing the former.

        Session is switched to closed state anyway.
        """
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    async def __aenter__(self) -> ClientSession: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

class _BaseRequestContextManager(Coroutine[Any, Any, _RetType], Generic[_RetType]):
    def __init__(self, coro: Coroutine['asyncio.Future[Any]', None, _RetType]) -> None: ...
    def send(self, arg: None) -> asyncio.Future[Any]: ...
    def throw(self, arg: BaseException) -> None: ...
    def close(self) -> None: ...
    def __await__(self) -> Generator[Any, None, _RetType]: ...
    def __iter__(self) -> Generator[Any, None, _RetType]: ...
    async def __aenter__(self) -> _RetType: ...

class _RequestContextManager(_BaseRequestContextManager[ClientResponse]):
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None: ...

class _WSRequestContextManager(_BaseRequestContextManager[ClientWebSocketResponse]):
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None: ...

class _SessionRequestContextManager:
    def __init__(self, coro: Coroutine['asyncio.Future[Any]', None, ClientResponse], session: ClientSession) -> None: ...
    async def __aenter__(self) -> ClientResponse: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None: ...

def request(method: str, url: StrOrURL, *, params: Mapping[str, str] | None = None, data: Any = None, json: Any = None, headers: LooseHeaders | None = None, skip_auto_headers: Iterable[str] | None = None, auth: BasicAuth | None = None, allow_redirects: bool = True, max_redirects: int = 10, compress: str | None = None, chunked: bool | None = None, expect100: bool = False, raise_for_status: bool | None = None, read_until_eof: bool = True, proxy: StrOrURL | None = None, proxy_auth: BasicAuth | None = None, timeout: ClientTimeout | object = ..., cookies: LooseCookies | None = None, version: HttpVersion = ..., connector: BaseConnector | None = None, read_bufsize: int | None = None, loop: asyncio.AbstractEventLoop | None = None) -> _SessionRequestContextManager:
    """Constructs and sends a request.

    Returns response object.
    method - HTTP method
    url - request url
    params - (optional) Dictionary or bytes to be sent in the query
      string of the new request
    data - (optional) Dictionary, bytes, or file-like object to
      send in the body of the request
    json - (optional) Any json compatible python object
    headers - (optional) Dictionary of HTTP Headers to send with
      the request
    cookies - (optional) Dict object to send with the request
    auth - (optional) BasicAuth named tuple represent HTTP Basic Auth
    auth - aiohttp.helpers.BasicAuth
    allow_redirects - (optional) If set to False, do not follow
      redirects
    version - Request HTTP version.
    compress - Set to True if request has to be compressed
       with deflate encoding.
    chunked - Set to chunk size for chunked transfer encoding.
    expect100 - Expect 100-continue response from server.
    connector - BaseConnector sub-class instance to support
       connection pooling.
    read_until_eof - Read response until eof if response
       does not have Content-Length header.
    loop - Optional event loop.
    timeout - Optional ClientTimeout settings structure, 5min
       total timeout by default.
    Usage::
      >>> import aiohttp
      >>> resp = await aiohttp.request('GET', 'http://python.org/')
      >>> resp
      <ClientResponse(python.org/) [200]>
      >>> data = await resp.read()
    """
