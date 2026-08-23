from _typeshed import Incomplete
from typing import Any, Dict

LOG: Incomplete
parser_cache: Dict[str, Any]

class _NodeCacheItem:
    node: Incomplete
    lines: Incomplete
    change_time: Incomplete
    last_used: Incomplete
    def __init__(self, node, lines, change_time: Incomplete | None = None) -> None: ...

def load_module(hashed_grammar, file_io, cache_path: Incomplete | None = None):
    """
    Returns a module or None, if it fails.
    """
def try_to_save_module(hashed_grammar, file_io, module, lines, pickling: bool = True, cache_path: Incomplete | None = None) -> None: ...
def clear_cache(cache_path: Incomplete | None = None) -> None: ...
def clear_inactive_cache(cache_path: Incomplete | None = None, inactivity_threshold=...): ...
