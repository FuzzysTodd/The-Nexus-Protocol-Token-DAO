import abc
import asyncio
import socket
from . import ClientSession as ClientSession, hdrs as hdrs
from .abc import AbstractCookieJar as AbstractCookieJar
from .client_reqrep import ClientResponse as ClientResponse
from .client_ws import ClientWebSocketResponse as ClientWebSocketResponse
from .helpers import PY_38 as PY_38, sentinel as sentinel
from .http import HttpVersion as HttpVersion, RawRequestMessage as RawRequestMessage
from .web import AppRunner as AppRunner, Application as Application, BaseRunner as BaseRunner, Request as Request, Server as Server, ServerRunner as ServerRunner, SockSite as SockSite, UrlMappingMatchInfo as UrlMappingMatchInfo
from .web_protocol import _RequestHandler
from _typeshed import Incomplete
from abc import ABC
from aiohttp.client import _RequestContextManager, _WSRequestContextManager
from asynctest import TestCase
from ssl import SSLContext
from types import TracebackType
from typing import Any, Callable, Iterator, Type
from yarl import URL

REUSE_ADDRESS: Incomplete

def get_unused_port_socket(host: str, family: socket.AddressFamily = ...) -> socket.socket: ...
def get_port_socket(host: str, port: int, family: socket.AddressFamily) -> socket.socket: ...
def unused_port() -> int:
    """Return a port that is unused on the current host."""

class BaseTestServer(ABC, metaclass=abc.ABCMeta):
    __test__: bool
    runner: Incomplete
    host: Incomplete
    port: Incomplete
    scheme: Incomplete
    skip_url_asserts: Incomplete
    socket_factory: Incomplete
    def __init__(self, *, scheme: str | object = ..., loop: asyncio.AbstractEventLoop | None = None, host: str = '127.0.0.1', port: int | None = None, skip_url_asserts: bool = False, socket_factory: Callable[[str, int, socket.AddressFamily], socket.socket] = ..., **kwargs: Any) -> None: ...
    async def start_server(self, loop: asyncio.AbstractEventLoop | None = None, **kwargs: Any) -> None: ...
    def make_url(self, path: str) -> URL: ...
    @property
    def started(self) -> bool: ...
    @property
    def closed(self) -> bool: ...
    @property
    def handler(self) -> Server: ...
    async def close(self) -> None:
        """Close all fixtures created by the test client.

        After that point, the TestClient is no longer usable.

        This is an idempotent function: running close multiple times
        will not have any additional effects.

        close is also run when the object is garbage collected, and on
        exit when used as a context manager.

        """
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    async def __aenter__(self) -> BaseTestServer: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

class TestServer(BaseTestServer):
    app: Incomplete
    def __init__(self, app: Application, *, scheme: str | object = ..., host: str = '127.0.0.1', port: int | None = None, **kwargs: Any) -> None: ...

class RawTestServer(BaseTestServer):
    def __init__(self, handler: _RequestHandler, *, scheme: str | object = ..., host: str = '127.0.0.1', port: int | None = None, **kwargs: Any) -> None: ...

class TestClient:
    """
    A test client implementation.

    To write functional tests for aiohttp based servers.

    """
    __test__: bool
    def __init__(self, server: BaseTestServer, *, cookie_jar: AbstractCookieJar | None = None, loop: asyncio.AbstractEventLoop | None = None, **kwargs: Any) -> None: ...
    async def start_server(self) -> None: ...
    @property
    def host(self) -> str: ...
    @property
    def port(self) -> int | None: ...
    @property
    def server(self) -> BaseTestServer: ...
    @property
    def app(self) -> Application | None: ...
    @property
    def session(self) -> ClientSession:
        """An internal aiohttp.ClientSession.

        Unlike the methods on the TestClient, client session requests
        do not automatically include the host in the url queried, and
        will require an absolute path to the resource.

        """
    def make_url(self, path: str) -> URL: ...
    def request(self, method: str, path: str, **kwargs: Any) -> _RequestContextManager:
        """Routes a request to tested http server.

        The interface is identical to aiohttp.ClientSession.request,
        except the loop kwarg is overridden by the instance used by the
        test server.

        """
    def get(self, path: str, **kwargs: Any) -> _RequestContextManager:
        """Perform an HTTP GET request."""
    def post(self, path: str, **kwargs: Any) -> _RequestContextManager:
        """Perform an HTTP POST request."""
    def options(self, path: str, **kwargs: Any) -> _RequestContextManager:
        """Perform an HTTP OPTIONS request."""
    def head(self, path: str, **kwargs: Any) -> _RequestContextManager:
        """Perform an HTTP HEAD request."""
    def put(self, path: str, **kwargs: Any) -> _RequestContextManager:
        """Perform an HTTP PUT request."""
    def patch(self, path: str, **kwargs: Any) -> _RequestContextManager:
        """Perform an HTTP PATCH request."""
    def delete(self, path: str, **kwargs: Any) -> _RequestContextManager:
        """Perform an HTTP PATCH request."""
    def ws_connect(self, path: str, **kwargs: Any) -> _WSRequestContextManager:
        """Initiate websocket connection.

        The api corresponds to aiohttp.ClientSession.ws_connect.

        """
    async def close(self) -> None:
        """Close all fixtures created by the test client.

        After that point, the TestClient is no longer usable.

        This is an idempotent function: running close multiple times
        will not have any additional effects.

        close is also run on exit when used as a(n) (asynchronous)
        context manager.

        """
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None: ...
    async def __aenter__(self) -> TestClient: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None: ...

class AioHTTPTestCase(TestCase):
    """A base class to allow for unittest web applications using aiohttp.

    Provides the following:

    * self.client (aiohttp.test_utils.TestClient): an aiohttp test client.
    * self.loop (asyncio.BaseEventLoop): the event loop in which the
        application and server are running.
    * self.app (aiohttp.web.Application): the application returned by
        self.get_application()

    Note that the TestClient's methods are asynchronous: you have to
    execute function on the test client using asynchronous methods.
    """
    async def get_application(self) -> Application:
        """Get application.

        This method should be overridden
        to return the aiohttp.web.Application
        object to test.
        """
    def get_app(self) -> Application:
        """Obsolete method used to constructing web application.

        Use .get_application() coroutine instead.
        """
    def setUp(self) -> None: ...
    loop: Incomplete
    async def asyncSetUp(self) -> None: ...
    app: Incomplete
    server: Incomplete
    client: Incomplete
    async def setUpAsync(self) -> None: ...
    def tearDown(self) -> None: ...
    async def asyncTearDown(self) -> None: ...
    async def tearDownAsync(self) -> None: ...
    async def get_server(self, app: Application) -> TestServer:
        """Return a TestServer instance."""
    async def get_client(self, server: TestServer) -> TestClient:
        """Return a TestClient instance."""

def unittest_run_loop(func: Any, *args: Any, **kwargs: Any) -> Any:
    """
    A decorator dedicated to use with asynchronous AioHTTPTestCase test methods.

    In 3.8+, this does nothing.
    """
def loop_context(loop_factory: _LOOP_FACTORY = ..., fast: bool = False) -> Iterator[asyncio.AbstractEventLoop]:
    """A contextmanager that creates an event_loop, for test purposes.

    Handles the creation and cleanup of a test loop.
    """
def setup_test_loop(loop_factory: _LOOP_FACTORY = ...) -> asyncio.AbstractEventLoop:
    """Create and return an asyncio.BaseEventLoop instance.

    The caller should also call teardown_test_loop,
    once they are done with the loop.
    """
def teardown_test_loop(loop: asyncio.AbstractEventLoop, fast: bool = False) -> None:
    """Teardown and cleanup an event_loop created by setup_test_loop."""
def make_mocked_request(method: str, path: str, headers: Any = None, *, match_info: Any = ..., version: HttpVersion = ..., closing: bool = False, app: Any = None, writer: Any = ..., protocol: Any = ..., transport: Any = ..., payload: Any = ..., sslcontext: SSLContext | None = None, client_max_size: int = ..., loop: Any = ...) -> Request:
    """Creates mocked web.Request testing purposes.

    Useful in unit tests, when spinning full web server is overkill or
    specific conditions and errors are hard to trigger.
    """
def make_mocked_coro(return_value: Any = ..., raise_exception: Any = ...) -> Any:
    """Creates a coroutine mock."""
