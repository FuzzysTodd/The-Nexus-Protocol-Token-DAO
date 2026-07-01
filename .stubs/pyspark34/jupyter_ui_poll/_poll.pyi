from ._async_thread import AsyncThread as AsyncThread
from collections import abc
from typing import AsyncIterable, AsyncIterator, Callable, Generic, Iterable, Iterator, TypeVar

T = TypeVar('T')
ZMQ_POLLOUT: int

class KernelWrapper:
    def __init__(self, shell, loop) -> None: ...
    def restore(self) -> None: ...
    async def replay(self) -> None: ...
    async def do_one_iteration(self) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    @staticmethod
    def get() -> KernelWrapper: ...

class IteratorWrapperAsync(abc.AsyncIterable, Generic[T]):
    def __init__(self, its: AsyncIterable[T], n: int = 1) -> None: ...
    def __aiter__(self) -> AsyncIterator[T]: ...

class IteratorWrapper(abc.Iterable, Generic[T]):
    def __init__(self, its: Iterable[T], n: int = 1) -> None: ...
    def __iter__(self) -> Iterator[T]: ...
    def __aiter__(self) -> AsyncIterator[T]: ...

def ui_events():
    """
    Gives you a function you can call to process UI events while running a long
    task inside a Jupyter cell.

    .. code-block:: python

       with ui_events() as ui_poll:
          while some_condition:
             ui_poll(10)  # Process upto 10 UI events if any happened
             do_some_more_compute()

    Async mode is also supported:

    .. code-block:: python

       async with ui_events() as ui_poll:
          while some_condition:
             await ui_poll(10)  # Process upto 10 UI events if any happened
             do_some_more_compute()


    #. Call ``kernel.do_one_iteration()`` taking care of IO redirects
    #. Intercept ``execute_request`` IPython kernel events and delay their execution
    #. Schedule replay of any blocked ``execute_request`` events when
       cell execution is finished.
    """
def with_ui_events(its, n: int = 1):
    """
    Deal with kernel ui events while processing a long sequence

    Iterable returned from this can be used in both async and sync contexts.

    .. code-block:: python

       for x in with_ui_events(some_data_stream, n=10):
          do_things_with(x)

       async for x in with_ui_events(some_data_stream, n=10):
          await do_things_with(x)


    This is basically equivalent to:

    .. code-block:: python

       with ui_events() as poll:
         for x in some_data_stream:
             poll(10)
             do_things_with(x)


    :param its:
      Iterator to pass through, this should be either
      :class:`~collections.abc.Iterable` or :class:`~collections.abc.AsyncIterable`

    :param n:
      Number of events to process in between items

    :returns:
      :class:`~collections.abc.AsyncIterable` when input is
      :class:`~collections.abc.AsyncIterable`

    :returns:
      Object that implements both :class:`~collections.abc.Iterable` and
      :class:`~collections.abc.AsyncIterable` interfaces when input is normal
      :class:`~collections.abc.Iterable`
    """
def with_ui_events_sync(its: Iterable[T], n: int = 1) -> IteratorWrapper[T]: ...
def with_ui_events_async(its: AsyncIterable[T], n: int = 1) -> AsyncIterable[T]: ...
def run_ui_poll_loop(f: Callable[[], T | None], sleep: float = 0.02, n: int = 1) -> T:
    """
    Repeatedly call ``f()`` until it returns something other than ``None``
    while also responding to widget events.

    This blocks execution of cells below in the notebook while still preserving
    interactivity of jupyter widgets.

    :param f:
       Function to periodically call (``f()`` should not block for long)

    :param sleep:
       Amount of time to sleep in between polling (in seconds, 1/50 is the default)

    :param n:
       Number of events to process per iteration

    :returns:
       First non-``None`` value returned from ``f()``
    """
