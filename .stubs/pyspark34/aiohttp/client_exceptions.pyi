import asyncio
import ssl
from .client_reqrep import ClientResponse, ConnectionKey, Fingerprint, RequestInfo
from .http_parser import RawResponseMessage
from .typedefs import LooseHeaders
from _typeshed import Incomplete
from typing import Any, Tuple

__all__ = ['ClientError', 'ClientConnectionError', 'ClientOSError', 'ClientConnectorError', 'ClientProxyConnectionError', 'ClientSSLError', 'ClientConnectorSSLError', 'ClientConnectorCertificateError', 'ServerConnectionError', 'ServerTimeoutError', 'ServerDisconnectedError', 'ServerFingerprintMismatch', 'ClientResponseError', 'ClientHttpProxyError', 'WSServerHandshakeError', 'ContentTypeError', 'ClientPayloadError', 'InvalidURL']

SSLContext = ssl.SSLContext

class ClientError(Exception):
    """Base class for client connection errors."""

class ClientResponseError(ClientError):
    """Connection error during reading response.

    request_info: instance of RequestInfo
    """
    request_info: Incomplete
    status: Incomplete
    message: Incomplete
    headers: Incomplete
    history: Incomplete
    args: Incomplete
    def __init__(self, request_info: RequestInfo, history: Tuple[ClientResponse, ...], *, code: int | None = None, status: int | None = None, message: str = '', headers: LooseHeaders | None = None) -> None: ...
    @property
    def code(self) -> int: ...
    @code.setter
    def code(self, value: int) -> None: ...

class ContentTypeError(ClientResponseError):
    """ContentType found is not valid."""
class WSServerHandshakeError(ClientResponseError):
    """websocket server handshake error."""
class ClientHttpProxyError(ClientResponseError):
    """HTTP proxy error.

    Raised in :class:`aiohttp.connector.TCPConnector` if
    proxy responds with status other than ``200 OK``
    on ``CONNECT`` request.
    """
class TooManyRedirects(ClientResponseError):
    """Client was redirected too many times."""
class ClientConnectionError(ClientError):
    """Base class for client socket errors."""
class ClientOSError(ClientConnectionError, OSError):
    """OSError error."""

class ClientConnectorError(ClientOSError):
    """Client connector error.

    Raised in :class:`aiohttp.connector.TCPConnector` if
        a connection can not be established.
    """
    args: Incomplete
    def __init__(self, connection_key: ConnectionKey, os_error: OSError) -> None: ...
    @property
    def os_error(self) -> OSError: ...
    @property
    def host(self) -> str: ...
    @property
    def port(self) -> int | None: ...
    @property
    def ssl(self) -> SSLContext | None | bool | Fingerprint: ...
    __reduce__: Incomplete

class ClientProxyConnectionError(ClientConnectorError):
    """Proxy connection error.

    Raised in :class:`aiohttp.connector.TCPConnector` if
        connection to proxy can not be established.
    """

class UnixClientConnectorError(ClientConnectorError):
    """Unix connector error.

    Raised in :py:class:`aiohttp.connector.UnixConnector`
    if connection to unix socket can not be established.
    """
    def __init__(self, path: str, connection_key: ConnectionKey, os_error: OSError) -> None: ...
    @property
    def path(self) -> str: ...

class ServerConnectionError(ClientConnectionError):
    """Server connection errors."""

class ServerDisconnectedError(ServerConnectionError):
    """Server disconnected."""
    args: Incomplete
    message: Incomplete
    def __init__(self, message: RawResponseMessage | str | None = None) -> None: ...

class ServerTimeoutError(ServerConnectionError, asyncio.TimeoutError):
    """Server timeout error."""

class ServerFingerprintMismatch(ServerConnectionError):
    """SSL certificate does not match expected fingerprint."""
    expected: Incomplete
    got: Incomplete
    host: Incomplete
    port: Incomplete
    args: Incomplete
    def __init__(self, expected: bytes, got: bytes, host: str, port: int) -> None: ...

class ClientPayloadError(ClientError):
    """Response payload error."""

class InvalidURL(ClientError, ValueError):
    """Invalid URL.

    URL used for fetching is malformed, e.g. it doesn't contains host
    part.
    """
    def __init__(self, url: Any) -> None: ...
    @property
    def url(self) -> Any: ...

class ClientSSLError(ClientConnectorError):
    """Base error for ssl.*Errors."""
class ClientConnectorSSLError:
    """Response ssl error."""

class ClientConnectorCertificateError:
    """Response certificate error."""
    args: Incomplete
    def __init__(self, connection_key: ConnectionKey, certificate_error: Exception) -> None: ...
    @property
    def certificate_error(self) -> Exception: ...
    @property
    def host(self) -> str: ...
    @property
    def port(self) -> int | None: ...
    @property
    def ssl(self) -> bool: ...
