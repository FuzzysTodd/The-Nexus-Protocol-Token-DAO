from _typeshed import Incomplete

__all__ = ['Pool', 'ThreadPool']

class RemoteTraceback(Exception):
    tb: Incomplete
    def __init__(self, tb) -> None: ...

class ExceptionWithTraceback:
    exc: Incomplete
    tb: Incomplete
    def __init__(self, exc, tb) -> None: ...
    def __reduce__(self): ...

class MaybeEncodingError(Exception):
    """Wraps possible unpickleable errors, so they can be
    safely sent through the socket."""
    exc: Incomplete
    value: Incomplete
    def __init__(self, exc, value) -> None: ...

class _PoolCache(dict):
    """
    Class that implements a cache for the Pool class that will notify
    the pool management threads every time the cache is emptied. The
    notification is done by the use of a queue that is provided when
    instantiating the cache.
    """
    notifier: Incomplete
    def __init__(self, *args, notifier: Incomplete | None = None, **kwds) -> None: ...
    def __delitem__(self, item) -> None: ...

class Pool:
    """
    Class which supports an async version of applying functions to arguments.
    """
    @staticmethod
    def Process(ctx, *args, **kwds): ...
    def __init__(self, processes: Incomplete | None = None, initializer: Incomplete | None = None, initargs=(), maxtasksperchild: Incomplete | None = None, context: Incomplete | None = None) -> None: ...
    def __del__(self, _warn=..., RUN=...) -> None: ...
    def apply(self, func, args=(), kwds={}):
        """
        Equivalent of `func(*args, **kwds)`.
        Pool must be running.
        """
    def map(self, func, iterable, chunksize: Incomplete | None = None):
        """
        Apply `func` to each element in `iterable`, collecting the results
        in a list that is returned.
        """
    def starmap(self, func, iterable, chunksize: Incomplete | None = None):
        """
        Like `map()` method but the elements of the `iterable` are expected to
        be iterables as well and will be unpacked as arguments. Hence
        `func` and (a, b) becomes func(a, b).
        """
    def starmap_async(self, func, iterable, chunksize: Incomplete | None = None, callback: Incomplete | None = None, error_callback: Incomplete | None = None):
        """
        Asynchronous version of `starmap()` method.
        """
    def imap(self, func, iterable, chunksize: int = 1):
        """
        Equivalent of `map()` -- can be MUCH slower than `Pool.map()`.
        """
    def imap_unordered(self, func, iterable, chunksize: int = 1):
        """
        Like `imap()` method but ordering of results is arbitrary.
        """
    def apply_async(self, func, args=(), kwds={}, callback: Incomplete | None = None, error_callback: Incomplete | None = None):
        """
        Asynchronous version of `apply()` method.
        """
    def map_async(self, func, iterable, chunksize: Incomplete | None = None, callback: Incomplete | None = None, error_callback: Incomplete | None = None):
        """
        Asynchronous version of `map()` method.
        """
    def __reduce__(self) -> None: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class ApplyResult:
    def __init__(self, pool, callback, error_callback) -> None: ...
    def ready(self): ...
    def successful(self): ...
    def wait(self, timeout: Incomplete | None = None) -> None: ...
    def get(self, timeout: Incomplete | None = None): ...
    __class_getitem__: Incomplete
AsyncResult = ApplyResult

class MapResult(ApplyResult):
    def __init__(self, pool, chunksize, length, callback, error_callback) -> None: ...

class IMapIterator:
    def __init__(self, pool) -> None: ...
    def __iter__(self): ...
    def next(self, timeout: Incomplete | None = None): ...
    __next__ = next

class IMapUnorderedIterator(IMapIterator): ...

class ThreadPool(Pool):
    @staticmethod
    def Process(ctx, *args, **kwds): ...
    def __init__(self, processes: Incomplete | None = None, initializer: Incomplete | None = None, initargs=()) -> None: ...
