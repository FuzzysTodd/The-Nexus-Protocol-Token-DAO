import asyncio
import types
import typing
from _typeshed import Incomplete
from concurrent import futures
from tornado.log import app_log as app_log
from typing import Any, Callable, Tuple

class ReturnValueIgnoredError(Exception): ...
Future = asyncio.Future
FUTURES: Incomplete

def is_future(x: Any) -> bool: ...

class DummyExecutor(futures.Executor):
    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> futures.Future[_T]: ...
    def shutdown(self, wait: bool = True) -> None: ...

dummy_executor: Incomplete

def run_on_executor(*args: Any, **kwargs: Any) -> Callable:
    """Decorator to run a synchronous method asynchronously on an executor.

    Returns a future.

    The executor to be used is determined by the ``executor``
    attributes of ``self``. To use a different attribute name, pass a
    keyword argument to the decorator::

        @run_on_executor(executor='_thread_pool')
        def foo(self):
            pass

    This decorator should not be confused with the similarly-named
    `.IOLoop.run_in_executor`. In general, using ``run_in_executor``
    when *calling* a blocking method is recommended instead of using
    this decorator when *defining* a method. If compatibility with older
    versions of Tornado is required, consider defining an executor
    and using ``executor.submit()`` at the call site.

    .. versionchanged:: 4.2
       Added keyword arguments to use alternative attributes.

    .. versionchanged:: 5.0
       Always uses the current IOLoop instead of ``self.io_loop``.

    .. versionchanged:: 5.1
       Returns a `.Future` compatible with ``await`` instead of a
       `concurrent.futures.Future`.

    .. deprecated:: 5.1

       The ``callback`` argument is deprecated and will be removed in
       6.0. The decorator itself is discouraged in new code but will
       not be removed in 6.0.

    .. versionchanged:: 6.0

       The ``callback`` argument was removed.
    """
def chain_future(a: Future[_T], b: Future[_T]) -> None:
    """Chain two futures together so that when one completes, so does the other.

    The result (success or failure) of ``a`` will be copied to ``b``, unless
    ``b`` has already been completed or cancelled by the time ``a`` finishes.

    .. versionchanged:: 5.0

       Now accepts both Tornado/asyncio `Future` objects and
       `concurrent.futures.Future`.

    """
def future_set_result_unless_cancelled(future: futures.Future[_T] | Future[_T], value: _T) -> None:
    """Set the given ``value`` as the `Future`'s result, if not cancelled.

    Avoids ``asyncio.InvalidStateError`` when calling ``set_result()`` on
    a cancelled `asyncio.Future`.

    .. versionadded:: 5.0
    """
def future_set_exception_unless_cancelled(future: futures.Future[_T] | Future[_T], exc: BaseException) -> None:
    """Set the given ``exc`` as the `Future`'s exception.

    If the Future is already canceled, logs the exception instead. If
    this logging is not desired, the caller should explicitly check
    the state of the Future and call ``Future.set_exception`` instead of
    this wrapper.

    Avoids ``asyncio.InvalidStateError`` when calling ``set_exception()`` on
    a cancelled `asyncio.Future`.

    .. versionadded:: 6.0

    """
def future_set_exc_info(future: futures.Future[_T] | Future[_T], exc_info: Tuple[type | None, BaseException | None, types.TracebackType | None]) -> None:
    """Set the given ``exc_info`` as the `Future`'s exception.

    Understands both `asyncio.Future` and the extensions in older
    versions of Tornado to enable better tracebacks on Python 2.

    .. versionadded:: 5.0

    .. versionchanged:: 6.0

       If the future is already cancelled, this function is a no-op.
       (previously ``asyncio.InvalidStateError`` would be raised)

    """
@typing.overload
def future_add_done_callback(future: futures.Future[_T], callback: Callable[[futures.Future[_T]], None]) -> None: ...
@typing.overload
def future_add_done_callback(future: Future[_T], callback: Callable[[Future[_T]], None]) -> None: ...
