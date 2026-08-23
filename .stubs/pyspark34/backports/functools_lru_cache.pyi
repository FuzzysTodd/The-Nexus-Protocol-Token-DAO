from _typeshed import Incomplete
from typing import NamedTuple

class _CacheInfo(NamedTuple):
    hits: Incomplete
    misses: Incomplete
    maxsize: Incomplete
    currsize: Incomplete

def update_wrapper(wrapper, wrapped, assigned=..., updated=...):
    """
    Patch two bugs in functools.update_wrapper.
    """

class _HashedSeq(list):
    hashvalue: Incomplete
    def __init__(self, tup, hash=...) -> None: ...
    def __hash__(self): ...

def lru_cache(maxsize: int = 100, typed: bool = False):
    """Least-recently-used cache decorator.

    If *maxsize* is set to None, the LRU features are disabled and the cache
    can grow without bound.

    If *typed* is True, arguments of different types will be cached separately.
    For example, f(3.0) and f(3) will be treated as distinct calls with
    distinct results.

    Arguments to the cached function must be hashable.

    View the cache statistics named tuple (hits, misses, maxsize, currsize) with
    f.cache_info().  Clear the cache and statistics with f.cache_clear().
    Access the underlying function with f.__wrapped__.

    See:  http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used

    """
