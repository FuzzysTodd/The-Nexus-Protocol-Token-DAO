from _typeshed import Incomplete
from typing import Any, Callable, Generic, TypeVar

K = TypeVar('K')
V = TypeVar('V')

class LRUCache(Generic[K, V]):
    """A simple LRU cache implementation, based on the OrderedDict class, which allows
    for a callback to be invoked when an item is evicted from the cache."""
    capacity: Incomplete
    cache: Incomplete
    callback: Incomplete
    def __init__(self, capacity: int, callback: Callable[[K, V], Any] | None = None) -> None: ...
    def get(self, key: K) -> V | None: ...
    def set(self, key: K, value: V) -> None: ...
