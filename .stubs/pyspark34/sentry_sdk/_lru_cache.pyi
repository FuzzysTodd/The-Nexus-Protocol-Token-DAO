from _typeshed import Incomplete

SENTINEL: Incomplete
PREV: int
NEXT: int
KEY: int
VALUE: int

class LRUCache:
    max_size: Incomplete
    full: bool
    cache: Incomplete
    root: Incomplete
    hits: int
    def __init__(self, max_size) -> None: ...
    def set(self, key, value) -> None: ...
    def get(self, key, default: Incomplete | None = None): ...
