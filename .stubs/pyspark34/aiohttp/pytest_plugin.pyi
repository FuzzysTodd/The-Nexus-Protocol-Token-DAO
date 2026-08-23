import asyncio
from .test_utils import BaseTestServer as BaseTestServer, RawTestServer as RawTestServer, TestClient as TestClient, TestServer as TestServer, loop_context as loop_context, setup_test_loop as setup_test_loop, teardown_test_loop as teardown_test_loop
from _typeshed import Incomplete
from aiohttp.helpers import PY_37 as PY_37, isasyncgenfunction as isasyncgenfunction
from aiohttp.web import Application as Application
from collections.abc import Generator
from typing import Awaitable, Callable

AiohttpClient = Callable[[Application | BaseTestServer], Awaitable[TestClient]]

def pytest_addoption(parser) -> None: ...
def pytest_fixture_setup(fixturedef):
    """Set up pytest fixture.

    Allow fixtures to be coroutines. Run coroutine fixtures in an event loop.
    """
def fast(request):
    """--fast config option"""
def loop_debug(request):
    """--enable-loop-debug config option"""
def pytest_pycollect_makeitem(collector, name, obj):
    """Fix pytest collecting for coroutines."""
def pytest_pyfunc_call(pyfuncitem):
    """Run coroutines in an event loop instead of a normal function call."""
def pytest_generate_tests(metafunc) -> None: ...
def loop(loop_factory, fast, loop_debug) -> Generator[Incomplete, None, None]:
    """Return an instance of the event loop."""
def proactor_loop() -> Generator[Incomplete, None, None]: ...
def unused_port(aiohttp_unused_port): ...
def aiohttp_unused_port():
    """Return a port that is unused on the current host."""
def aiohttp_server(loop) -> Generator[Incomplete, None, Incomplete]:
    """Factory to create a TestServer instance, given an app.

    aiohttp_server(app, **kwargs)
    """
def test_server(aiohttp_server): ...
def aiohttp_raw_server(loop) -> Generator[Incomplete, None, Incomplete]:
    """Factory to create a RawTestServer instance, given a web handler.

    aiohttp_raw_server(handler, **kwargs)
    """
def raw_test_server(aiohttp_raw_server): ...
def aiohttp_client(loop: asyncio.AbstractEventLoop) -> Generator[AiohttpClient, None, None]:
    """Factory to create a TestClient instance.

    aiohttp_client(app, **kwargs)
    aiohttp_client(server, **kwargs)
    aiohttp_client(raw_server, **kwargs)
    """
def test_client(aiohttp_client): ...
