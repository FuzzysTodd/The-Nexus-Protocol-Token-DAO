from _typeshed import Incomplete
from typing import Callable, Dict, Generic

__all__ = ['SimpleCache', 'FastDictCache', 'memoized']

class SimpleCache(Generic[_T, _U]):
    """
    Very simple cache that discards the oldest item when the cache size is
    exceeded.

    :param maxsize: Maximum size of the cache. (Don't make it too big.)
    """
    maxsize: Incomplete
    def __init__(self, maxsize: int = 8) -> None: ...
    def get(self, key: _T, getter_func: Callable[[], _U]) -> _U:
        """
        Get object from the cache.
        If not found, call `getter_func` to resolve it, and put that on the top
        of the cache instead.
        """
    def clear(self) -> None:
        """Clear cache."""

class FastDictCache(Dict[_K, _V]):
    """
    Fast, lightweight cache which keeps at most `size` items.
    It will discard the oldest items in the cache first.

    The cache is a dictionary, which doesn't keep track of access counts.
    It is perfect to cache little immutable objects which are not expensive to
    create, but where a dictionary lookup is still much faster than an object
    instantiation.

    :param get_value: Callable that's called in case of a missing key.
    """
    get_value: Incomplete
    size: Incomplete
    def __init__(self, get_value: Callable[..., _V], size: int = 1000000) -> None: ...
    def __missing__(self, key: _K) -> _V: ...

def memoized(maxsize: int = 1024) -> Callable[[_F], _F]:
    """
    Memoization decorator for immutable classes and pure functions.
    """
