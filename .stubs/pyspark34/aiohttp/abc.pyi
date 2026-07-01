import abc
import asyncio
import logging
from .helpers import get_running_loop as get_running_loop
from .typedefs import LooseCookies as LooseCookies
from .web_app import Application as Application
from .web_exceptions import HTTPException as HTTPException
from .web_request import BaseRequest as BaseRequest, Request as Request
from .web_response import StreamResponse as StreamResponse
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Sized
from http.cookies import BaseCookie, Morsel
from multidict import CIMultiDict
from typing import Any, Awaitable, Callable, Dict, Generator, Iterable, List, Tuple
from yarl import URL

class AbstractRouter(ABC, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    def post_init(self, app: Application) -> None:
        """Post init stage.

        Not an abstract method for sake of backward compatibility,
        but if the router wants to be aware of the application
        it can override this.
        """
    @property
    def frozen(self) -> bool: ...
    def freeze(self) -> None:
        """Freeze router."""
    @abstractmethod
    async def resolve(self, request: Request) -> AbstractMatchInfo:
        """Return MATCH_INFO for given request"""

class AbstractMatchInfo(ABC, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def handler(self) -> Callable[[Request], Awaitable[StreamResponse]]:
        """Execute matched request handler"""
    @property
    @abstractmethod
    def expect_handler(self) -> Callable[[Request], Awaitable[None]]:
        """Expect handler for 100-continue processing"""
    @property
    @abstractmethod
    def http_exception(self) -> HTTPException | None:
        """HTTPException instance raised on router's resolving, or None"""
    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """Return a dict with additional info useful for introspection"""
    @property
    @abstractmethod
    def apps(self) -> Tuple[Application, ...]:
        """Stack of nested applications.

        Top level application is left-most element.

        """
    @abstractmethod
    def add_app(self, app: Application) -> None:
        """Add application to the nested apps stack."""
    @abstractmethod
    def freeze(self) -> None:
        """Freeze the match info.

        The method is called after route resolution.

        After the call .add_app() is forbidden.

        """

class AbstractView(ABC, metaclass=abc.ABCMeta):
    """Abstract class based view."""
    def __init__(self, request: Request) -> None: ...
    @property
    def request(self) -> Request:
        """Request instance."""
    @abstractmethod
    def __await__(self) -> Generator[Any, None, StreamResponse]:
        """Execute the view handler."""

class AbstractResolver(ABC, metaclass=abc.ABCMeta):
    """Abstract DNS resolver."""
    @abstractmethod
    async def resolve(self, host: str, port: int, family: int) -> List[Dict[str, Any]]:
        """Return IP address for given hostname"""
    @abstractmethod
    async def close(self) -> None:
        """Release resolver"""
IterableBase = Iterable[Morsel[str]]
ClearCookiePredicate: Incomplete

class AbstractCookieJar(Sized, IterableBase, metaclass=abc.ABCMeta):
    """Abstract Cookie Jar."""
    def __init__(self, *, loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    @abstractmethod
    def clear(self, predicate: ClearCookiePredicate | None = None) -> None:
        """Clear all cookies if no predicate is passed."""
    @abstractmethod
    def clear_domain(self, domain: str) -> None:
        """Clear all cookies for domain and all subdomains."""
    @abstractmethod
    def update_cookies(self, cookies: LooseCookies, response_url: URL = ...) -> None:
        """Update cookies."""
    @abstractmethod
    def filter_cookies(self, request_url: URL) -> BaseCookie[str]:
        """Return the jar's cookies filtered by their attributes."""

class AbstractStreamWriter(ABC, metaclass=abc.ABCMeta):
    """Abstract stream writer."""
    buffer_size: int
    output_size: int
    length: int | None
    @abstractmethod
    async def write(self, chunk: bytes) -> None:
        """Write chunk into stream."""
    @abstractmethod
    async def write_eof(self, chunk: bytes = b'') -> None:
        """Write last chunk."""
    @abstractmethod
    async def drain(self) -> None:
        """Flush the write buffer."""
    @abstractmethod
    def enable_compression(self, encoding: str = 'deflate') -> None:
        """Enable HTTP body compression"""
    @abstractmethod
    def enable_chunking(self) -> None:
        """Enable HTTP chunked mode"""
    @abstractmethod
    async def write_headers(self, status_line: str, headers: CIMultiDict[str]) -> None:
        """Write HTTP headers"""

class AbstractAccessLogger(ABC, metaclass=abc.ABCMeta):
    """Abstract writer to access log."""
    logger: Incomplete
    log_format: Incomplete
    def __init__(self, logger: logging.Logger, log_format: str) -> None: ...
    @abstractmethod
    def log(self, request: BaseRequest, response: StreamResponse, time: float) -> None:
        """Emit log to logger."""
