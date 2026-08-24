import logging
import socket
import typing
import unittest
from _typeshed import Incomplete
from collections.abc import Generator
from tornado import gen as gen, netutil as netutil
from tornado.httpclient import AsyncHTTPClient as AsyncHTTPClient, HTTPResponse as HTTPResponse
from tornado.httpserver import HTTPServer as HTTPServer
from tornado.ioloop import IOLoop as IOLoop, TimeoutError as TimeoutError
from tornado.log import app_log as app_log
from tornado.platform.asyncio import AsyncIOMainLoop as AsyncIOMainLoop
from tornado.process import Subprocess as Subprocess
from tornado.util import basestring_type as basestring_type, raise_exc_info as raise_exc_info
from tornado.web import Application as Application
from types import TracebackType
from typing import Any, Callable, Coroutine, Dict, Tuple, Type

def bind_unused_port(reuse_port: bool = False, address: str = '127.0.0.1') -> Tuple[socket.socket, int]:
    '''Binds a server socket to an available port on localhost.

    Returns a tuple (socket, port).

    .. versionchanged:: 4.4
       Always binds to ``127.0.0.1`` without resolving the name
       ``localhost``.

    .. versionchanged:: 6.2
       Added optional ``address`` argument to
       override the default "127.0.0.1".
    '''
def get_async_test_timeout() -> float:
    """Get the global timeout setting for async tests.

    Returns a float, the timeout in seconds.

    .. versionadded:: 3.1
    """

class _TestMethodWrapper:
    """Wraps a test method to raise an error if it returns a value.

    This is mainly used to detect undecorated generators (if a test
    method yields it must use a decorator to consume the generator),
    but will also detect other kinds of return values (these are not
    necessarily errors, but we alert anyway since there is no good
    reason to return a value from a test).
    """
    orig_method: Incomplete
    __wrapped__: Incomplete
    def __init__(self, orig_method: Callable) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, name: str) -> Any:
        """Proxy all unknown attributes to the original method.

        This is important for some of the decorators in the `unittest`
        module, such as `unittest.skipIf`.
        """

class AsyncTestCase(unittest.TestCase):
    '''`~unittest.TestCase` subclass for testing `.IOLoop`-based
    asynchronous code.

    The unittest framework is synchronous, so the test must be
    complete by the time the test method returns. This means that
    asynchronous code cannot be used in quite the same way as usual
    and must be adapted to fit. To write your tests with coroutines,
    decorate your test methods with `tornado.testing.gen_test` instead
    of `tornado.gen.coroutine`.

    This class also provides the (deprecated) `stop()` and `wait()`
    methods for a more manual style of testing. The test method itself
    must call ``self.wait()``, and asynchronous callbacks should call
    ``self.stop()`` to signal completion.

    By default, a new `.IOLoop` is constructed for each test and is available
    as ``self.io_loop``.  If the code being tested requires a
    reused global `.IOLoop`, subclasses should override `get_new_ioloop` to return it,
    although this is deprecated as of Tornado 6.3.

    The `.IOLoop`\'s ``start`` and ``stop`` methods should not be
    called directly.  Instead, use `self.stop <stop>` and `self.wait
    <wait>`.  Arguments passed to ``self.stop`` are returned from
    ``self.wait``.  It is possible to have multiple ``wait``/``stop``
    cycles in the same test.

    Example::

        # This test uses coroutine style.
        class MyTestCase(AsyncTestCase):
            @tornado.testing.gen_test
            def test_http_fetch(self):
                client = AsyncHTTPClient()
                response = yield client.fetch("http://www.tornadoweb.org")
                # Test contents of response
                self.assertIn("FriendFeed", response.body)

        # This test uses argument passing between self.stop and self.wait.
        class MyTestCase2(AsyncTestCase):
            def test_http_fetch(self):
                client = AsyncHTTPClient()
                client.fetch("http://www.tornadoweb.org/", self.stop)
                response = self.wait()
                # Test contents of response
                self.assertIn("FriendFeed", response.body)
    '''
    def __init__(self, methodName: str = 'runTest') -> None: ...
    io_loop: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def get_new_ioloop(self) -> IOLoop:
        """Returns the `.IOLoop` to use for this test.

        By default, a new `.IOLoop` is created for each test.
        Subclasses may override this method to return
        `.IOLoop.current()` if it is not appropriate to use a new
        `.IOLoop` in each tests (for example, if there are global
        singletons using the default `.IOLoop`) or if a per-test event
        loop is being provided by another system (such as
        ``pytest-asyncio``).

        .. deprecated:: 6.3
           This method will be removed in Tornado 7.0.
        """
    def run(self, result: unittest.TestResult | None = None) -> unittest.TestResult | None: ...
    def stop(self, _arg: Any = None, **kwargs: Any) -> None:
        """Stops the `.IOLoop`, causing one pending (or future) call to `wait()`
        to return.

        Keyword arguments or a single positional argument passed to `stop()` are
        saved and will be returned by `wait()`.

        .. deprecated:: 5.1

           `stop` and `wait` are deprecated; use ``@gen_test`` instead.
        """
    def wait(self, condition: Callable[..., bool] | None = None, timeout: float | None = None) -> Any:
        """Runs the `.IOLoop` until stop is called or timeout has passed.

        In the event of a timeout, an exception will be thrown. The
        default timeout is 5 seconds; it may be overridden with a
        ``timeout`` keyword argument or globally with the
        ``ASYNC_TEST_TIMEOUT`` environment variable.

        If ``condition`` is not ``None``, the `.IOLoop` will be restarted
        after `stop()` until ``condition()`` returns ``True``.

        .. versionchanged:: 3.1
           Added the ``ASYNC_TEST_TIMEOUT`` environment variable.

        .. deprecated:: 5.1

           `stop` and `wait` are deprecated; use ``@gen_test`` instead.
        """

class AsyncHTTPTestCase(AsyncTestCase):
    '''A test case that starts up an HTTP server.

    Subclasses must override `get_app()`, which returns the
    `tornado.web.Application` (or other `.HTTPServer` callback) to be tested.
    Tests will typically use the provided ``self.http_client`` to fetch
    URLs from this server.

    Example, assuming the "Hello, world" example from the user guide is in
    ``hello.py``::

        import hello

        class TestHelloApp(AsyncHTTPTestCase):
            def get_app(self):
                return hello.make_app()

            def test_homepage(self):
                response = self.fetch(\'/\')
                self.assertEqual(response.code, 200)
                self.assertEqual(response.body, \'Hello, world\')

    That call to ``self.fetch()`` is equivalent to ::

        self.http_client.fetch(self.get_url(\'/\'), self.stop)
        response = self.wait()

    which illustrates how AsyncTestCase can turn an asynchronous operation,
    like ``http_client.fetch()``, into a synchronous operation. If you need
    to do other asynchronous operations in tests, you\'ll probably need to use
    ``stop()`` and ``wait()`` yourself.
    '''
    http_client: Incomplete
    http_server: Incomplete
    def setUp(self) -> None: ...
    def get_http_client(self) -> AsyncHTTPClient: ...
    def get_http_server(self) -> HTTPServer: ...
    def get_app(self) -> Application:
        """Should be overridden by subclasses to return a
        `tornado.web.Application` or other `.HTTPServer` callback.
        """
    def fetch(self, path: str, raise_error: bool = False, **kwargs: Any) -> HTTPResponse:
        '''Convenience method to synchronously fetch a URL.

        The given path will be appended to the local server\'s host and
        port.  Any additional keyword arguments will be passed directly to
        `.AsyncHTTPClient.fetch` (and so could be used to pass
        ``method="POST"``, ``body="..."``, etc).

        If the path begins with http:// or https://, it will be treated as a
        full URL and will be fetched as-is.

        If ``raise_error`` is ``True``, a `tornado.httpclient.HTTPError` will
        be raised if the response code is not 200. This is the same behavior
        as the ``raise_error`` argument to `.AsyncHTTPClient.fetch`, but
        the default is ``False`` here (it\'s ``True`` in `.AsyncHTTPClient`)
        because tests often need to deal with non-200 response codes.

        .. versionchanged:: 5.0
           Added support for absolute URLs.

        .. versionchanged:: 5.1

           Added the ``raise_error`` argument.

        .. deprecated:: 5.1

           This method currently turns any exception into an
           `.HTTPResponse` with status code 599. In Tornado 6.0,
           errors other than `tornado.httpclient.HTTPError` will be
           passed through, and ``raise_error=False`` will only
           suppress errors that would be raised due to non-200
           response codes.

        '''
    def get_httpserver_options(self) -> Dict[str, Any]:
        """May be overridden by subclasses to return additional
        keyword arguments for the server.
        """
    def get_http_port(self) -> int:
        """Returns the port used by the server.

        A new port is chosen for each test.
        """
    def get_protocol(self) -> str: ...
    def get_url(self, path: str) -> str:
        """Returns an absolute url for the given path on the test server."""
    def tearDown(self) -> None: ...

class AsyncHTTPSTestCase(AsyncHTTPTestCase):
    """A test case that starts an HTTPS server.

    Interface is generally the same as `AsyncHTTPTestCase`.
    """
    def get_http_client(self) -> AsyncHTTPClient: ...
    def get_httpserver_options(self) -> Dict[str, Any]: ...
    def get_ssl_options(self) -> Dict[str, Any]:
        """May be overridden by subclasses to select SSL options.

        By default includes a self-signed testing certificate.
        """
    @staticmethod
    def default_ssl_options() -> Dict[str, Any]: ...
    def get_protocol(self) -> str: ...

@typing.overload
def gen_test(*, timeout: float | None = None) -> Callable[[Callable[..., Generator | Coroutine]], Callable[..., None]]: ...
@typing.overload
def gen_test(func: Callable[..., Generator | Coroutine]) -> Callable[..., None]: ...

class ExpectLog(logging.Filter):
    '''Context manager to capture and suppress expected log output.

    Useful to make tests of error conditions less noisy, while still
    leaving unexpected log entries visible.  *Not thread safe.*

    The attribute ``logged_stack`` is set to ``True`` if any exception
    stack trace was logged.

    Usage::

        with ExpectLog(\'tornado.application\', "Uncaught exception"):
            error_response = self.fetch("/some_page")

    .. versionchanged:: 4.3
       Added the ``logged_stack`` attribute.
    '''
    logger: Incomplete
    regex: Incomplete
    required: Incomplete
    matched: int
    deprecated_level_matched: int
    logged_stack: bool
    level: Incomplete
    orig_level: Incomplete
    def __init__(self, logger: logging.Logger | basestring_type, regex: str, required: bool = True, level: int | None = None) -> None:
        """Constructs an ExpectLog context manager.

        :param logger: Logger object (or name of logger) to watch.  Pass an
            empty string to watch the root logger.
        :param regex: Regular expression to match.  Any log entries on the
            specified logger that match this regex will be suppressed.
        :param required: If true, an exception will be raised if the end of the
            ``with`` statement is reached without matching any log entries.
        :param level: A constant from the ``logging`` module indicating the
            expected log level. If this parameter is provided, only log messages
            at this level will be considered to match. Additionally, the
            supplied ``logger`` will have its level adjusted if necessary (for
            the duration of the ``ExpectLog`` to enable the expected message.

        .. versionchanged:: 6.1
           Added the ``level`` parameter.

        .. deprecated:: 6.3
           In Tornado 7.0, only ``WARNING`` and higher logging levels will be
           matched by default. To match ``INFO`` and lower levels, the ``level``
           argument must be used. This is changing to minimize differences
           between ``tornado.testing.main`` (which enables ``INFO`` logs by
           default) and most other test runners (including those in IDEs)
           which have ``INFO`` logs disabled by default.
        """
    def filter(self, record: logging.LogRecord) -> bool: ...
    def __enter__(self) -> ExpectLog: ...
    def __exit__(self, typ: Type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> None: ...

def setup_with_context_manager(testcase: unittest.TestCase, cm: Any) -> Any:
    """Use a contextmanager to setUp a test case."""
def main(**kwargs: Any) -> None:
    """A simple test runner.

    This test runner is essentially equivalent to `unittest.main` from
    the standard library, but adds support for Tornado-style option
    parsing and log formatting. It is *not* necessary to use this
    `main` function to run tests using `AsyncTestCase`; these tests
    are self-contained and can run with any test runner.

    The easiest way to run a test is via the command line::

        python -m tornado.testing tornado.test.web_test

    See the standard library ``unittest`` module for ways in which
    tests can be specified.

    Projects with many tests may wish to define a test script like
    ``tornado/test/runtests.py``.  This script should define a method
    ``all()`` which returns a test suite and then call
    `tornado.testing.main()`.  Note that even when a test script is
    used, the ``all()`` test suite may be overridden by naming a
    single test on the command line::

        # Runs all tests
        python -m tornado.test.runtests
        # Runs one test
        python -m tornado.test.runtests tornado.test.web_test

    Additional keyword arguments passed through to ``unittest.main()``.
    For example, use ``tornado.testing.main(verbosity=2)``
    to show many test details as they are run.
    See http://docs.python.org/library/unittest.html#unittest.main
    for full argument list.

    .. versionchanged:: 5.0

       This function produces no output of its own; only that produced
       by the `unittest` module (previously it would add a PASS or FAIL
       log message).
    """
