from .compat import importlib_metadata_get as importlib_metadata_get
from _typeshed import Incomplete

def update_wrapper(decorated, fn): ...

class PluginLoader:
    group: Incomplete
    impls: Incomplete
    def __init__(self, group) -> None: ...
    def load(self, name): ...
    def register(self, name, modulepath, objname): ...

def verify_directory(dir_) -> None:
    """create and/or verify a filesystem directory."""
def to_list(x, default: Incomplete | None = None): ...

class memoized_property:
    """A read-only @property that is only evaluated once."""
    fget: Incomplete
    __doc__: Incomplete
    def __init__(self, fget, doc: Incomplete | None = None) -> None: ...
    def __get__(self, obj, cls): ...

class memoized_instancemethod:
    """Decorate a method memoize its return value.

    Best applied to no-arg methods: memoization is not sensitive to
    argument values, and will always return the same value even when
    called with different arguments.

    """
    fget: Incomplete
    __doc__: Incomplete
    def __init__(self, fget, doc: Incomplete | None = None) -> None: ...
    def __get__(self, obj, cls): ...

class SetLikeDict(dict):
    """a dictionary that has some setlike methods on it"""
    def union(self, other):
        """produce a 'union' of this dict and another (at the key level).

        values in the second dict take precedence over that of the first"""

class FastEncodingBuffer:
    """a very rudimentary buffer that is faster than StringIO,
    and supports unicode data."""
    data: Incomplete
    encoding: Incomplete
    delim: str
    errors: Incomplete
    write: Incomplete
    def __init__(self, encoding: Incomplete | None = None, errors: str = 'strict') -> None: ...
    def truncate(self) -> None: ...
    def getvalue(self): ...

class LRUCache(dict):
    """A dictionary-like object that stores a limited number of items,
    discarding lesser used items periodically.

    this is a rewrite of LRUCache from Myghty to use a periodic timestamp-based
    paradigm so that synchronization is not really needed.  the size management
    is inexact.
    """
    class _Item:
        key: Incomplete
        value: Incomplete
        timestamp: Incomplete
        def __init__(self, key, value) -> None: ...
    capacity: Incomplete
    threshold: Incomplete
    def __init__(self, capacity, threshold: float = 0.5) -> None: ...
    def __getitem__(self, key): ...
    def values(self): ...
    def setdefault(self, key, value): ...
    def __setitem__(self, key, value) -> None: ...

def parse_encoding(fp):
    """Deduce the encoding of a Python source file (binary mode) from magic
    comment.

    It does this in the same way as the `Python interpreter`__

    .. __: http://docs.python.org/ref/encodings.html

    The ``fp`` argument should be a seekable file object in binary mode.
    """
def sorted_dict_repr(d):
    """repr() a dictionary with the keys in order.

    Used by the lexer unit test to compare parse trees based on strings.

    """
def restore__ast(_ast) -> None:
    """Attempt to restore the required classes to the _ast module if it
    appears to be missing them
    """
def read_file(path, mode: str = 'rb'): ...
def read_python_file(path): ...
