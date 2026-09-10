from _typeshed import Incomplete

class __config_flags:
    """Internal class for defining compatibility and debugging flags"""
    enable: Incomplete
    disable: Incomplete

def col(loc: int, strg: str) -> int:
    """
    Returns current column within a string, counting newlines as line separators.
    The first column is number 1.

    Note: the default parsing behavior is to expand tabs in the input string
    before starting the parsing process.  See
    :class:`ParserElement.parseString` for more
    information on parsing strings containing ``<TAB>`` s, and suggested
    methods to maintain a consistent view of the parsed string, the parse
    location, and line and column positions within the parsed string.
    """
def lineno(loc: int, strg: str) -> int:
    """Returns current line number within a string, counting newlines as line separators.
    The first line is number 1.

    Note - the default parsing behavior is to expand tabs in the input string
    before starting the parsing process.  See :class:`ParserElement.parseString`
    for more information on parsing strings containing ``<TAB>`` s, and
    suggested methods to maintain a consistent view of the parsed string, the
    parse location, and line and column positions within the parsed string.
    """
def line(loc: int, strg: str) -> str:
    """
    Returns the line of text containing loc within a string, counting newlines as line separators.
    """

class _UnboundedCache:
    not_in_cache: Incomplete
    size: Incomplete
    get: Incomplete
    set: Incomplete
    clear: Incomplete
    def __init__(self) -> None: ...

class _FifoCache:
    not_in_cache: Incomplete
    size: Incomplete
    get: Incomplete
    set: Incomplete
    clear: Incomplete
    def __init__(self, size) -> None: ...

class LRUMemo:
    """
    A memoizing mapping that retains `capacity` deleted items

    The memo tracks retained items by their access order; once `capacity` items
    are retained, the least recently used item is discarded.
    """
    def __init__(self, capacity) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def clear(self) -> None: ...

class UnboundedMemo(dict):
    """
    A memoizing mapping that retains all deleted items
    """
    def __delitem__(self, key) -> None: ...
