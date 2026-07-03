from . import TTLCache

__all__ = ['fifo_cache', 'lfu_cache', 'lru_cache', 'mru_cache', 'rr_cache', 'ttl_cache']

class _UnboundTTLCache(TTLCache):
    def __init__(self, ttl, timer) -> None: ...
    @property
    def maxsize(self) -> None: ...

def fifo_cache(maxsize: int = 128, typed: bool = False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a First In First Out (FIFO)
    algorithm.

    """
def lfu_cache(maxsize: int = 128, typed: bool = False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Frequently Used (LFU)
    algorithm.

    """
def lru_cache(maxsize: int = 128, typed: bool = False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm.

    """
def mru_cache(maxsize: int = 128, typed: bool = False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU)
    algorithm.
    """
def rr_cache(maxsize: int = 128, choice=..., typed: bool = False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Random Replacement (RR)
    algorithm.

    """
def ttl_cache(maxsize: int = 128, ttl: int = 600, timer=..., typed: bool = False):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
