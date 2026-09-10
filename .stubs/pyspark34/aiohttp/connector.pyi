import asyncio
import ssl
from .abc import AbstractResolver
from .client import ClientTimeout
from .client_proto import ResponseHandler
from .client_reqrep import ClientRequest, ConnectionKey, Fingerprint
from .tracing import Trace
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, Awaitable, Callable, Dict, List, Tuple, Type

__all__ = ['BaseConnector', 'TCPConnector', 'UnixConnector', 'NamedPipeConnector']

SSLContext = ssl.SSLContext
SSLContext = object

class _DeprecationWaiter:
    def __init__(self, awaitable: Awaitable[Any]) -> None: ...
    def __await__(self) -> Any: ...
    def __del__(self) -> None: ...

class Connection:
    def __init__(self, connector: BaseConnector, key: ConnectionKey, protocol: ResponseHandler, loop: asyncio.AbstractEventLoop) -> None: ...
    def __del__(self, _warnings: Any = ...) -> None: ...
    @property
    def loop(self) -> asyncio.AbstractEventLoop: ...
    @property
    def transport(self) -> asyncio.Transport | None: ...
    @property
    def protocol(self) -> ResponseHandler | None: ...
    def add_callback(self, callback: Callable[[], None]) -> None: ...
    def close(self) -> None: ...
    def release(self) -> None: ...
    @property
    def closed(self) -> bool: ...

class _TransportPlaceholder:
    """placeholder for BaseConnector.connect function"""
    def close(self) -> None: ...

class BaseConnector:
    """Base connector class.

    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    enable_cleanup_closed - Enables clean-up closed ssl transports.
                            Disabled by default.
    loop - Optional event loop.
    """
    cookies: Incomplete
    def __init__(self, *, keepalive_timeout: object | None | float = ..., force_close: bool = False, limit: int = 100, limit_per_host: int = 0, enable_cleanup_closed: bool = False, loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    def __del__(self, _warnings: Any = ...) -> None: ...
    def __enter__(self) -> BaseConnector: ...
    def __exit__(self, *exc: Any) -> None: ...
    async def __aenter__(self) -> BaseConnector: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, exc_traceback: TracebackType | None = None) -> None: ...
    @property
    def force_close(self) -> bool:
        """Ultimately close connection on releasing if True."""
    @property
    def limit(self) -> int:
        """The total number for simultaneous connections.

        If limit is 0 the connector has no limit.
        The default limit size is 100.
        """
    @property
    def limit_per_host(self) -> int:
        """The limit for simultaneous connections to the same endpoint.

        Endpoints are the same if they are have equal
        (host, port, is_ssl) triple.
        """
    def close(self) -> Awaitable[None]:
        """Close all opened transports."""
    @property
    def closed(self) -> bool:
        """Is connector closed.

        A readonly property.
        """
    async def connect(self, req: ClientRequest, traces: List['Trace'], timeout: ClientTimeout) -> Connection:
        """Get from pool or create new connection."""

class _DNSCacheTable:
    def __init__(self, ttl: float | None = None) -> None: ...
    def __contains__(self, host: object) -> bool: ...
    def add(self, key: Tuple[str, int], addrs: List[Dict[str, Any]]) -> None: ...
    def remove(self, key: Tuple[str, int]) -> None: ...
    def clear(self) -> None: ...
    def next_addrs(self, key: Tuple[str, int]) -> List[Dict[str, Any]]: ...
    def expired(self, key: Tuple[str, int]) -> bool: ...

class TCPConnector(BaseConnector):
    """TCP connector.

    verify_ssl - Set to True to check ssl certifications.
    fingerprint - Pass the binary sha256
        digest of the expected certificate in DER format to verify
        that the certificate the server presents matches. See also
        https://en.wikipedia.org/wiki/Transport_Layer_Security#Certificate_pinning
    resolver - Enable DNS lookups and use this
        resolver
    use_dns_cache - Use memory cache for DNS lookups.
    ttl_dns_cache - Max seconds having cached a DNS entry, None forever.
    family - socket address family
    local_addr - local tuple of (host, port) to bind socket to

    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    enable_cleanup_closed - Enables clean-up closed ssl transports.
                            Disabled by default.
    loop - Optional event loop.
    """
    def __init__(self, *, verify_ssl: bool = True, fingerprint: bytes | None = None, use_dns_cache: bool = True, ttl_dns_cache: int | None = 10, family: int = 0, ssl_context: SSLContext | None = None, ssl: None | bool | Fingerprint | SSLContext = None, local_addr: Tuple[str, int] | None = None, resolver: AbstractResolver | None = None, keepalive_timeout: None | float | object = ..., force_close: bool = False, limit: int = 100, limit_per_host: int = 0, enable_cleanup_closed: bool = False, loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    def close(self) -> Awaitable[None]:
        """Close all ongoing DNS calls."""
    @property
    def family(self) -> int:
        """Socket family like AF_INET."""
    @property
    def use_dns_cache(self) -> bool:
        """True if local DNS caching is enabled."""
    def clear_dns_cache(self, host: str | None = None, port: int | None = None) -> None:
        """Remove specified host/port or clear all dns local cache."""

class UnixConnector(BaseConnector):
    """Unix socket connector.

    path - Unix socket path.
    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    loop - Optional event loop.
    """
    def __init__(self, path: str, force_close: bool = False, keepalive_timeout: object | float | None = ..., limit: int = 100, limit_per_host: int = 0, loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    @property
    def path(self) -> str:
        """Path to unix socket."""

class NamedPipeConnector(BaseConnector):
    """Named pipe connector.

    Only supported by the proactor event loop.
    See also: https://docs.python.org/3.7/library/asyncio-eventloop.html

    path - Windows named pipe path.
    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    loop - Optional event loop.
    """
    def __init__(self, path: str, force_close: bool = False, keepalive_timeout: object | float | None = ..., limit: int = 100, limit_per_host: int = 0, loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    @property
    def path(self) -> str:
        """Path to the named pipe."""
