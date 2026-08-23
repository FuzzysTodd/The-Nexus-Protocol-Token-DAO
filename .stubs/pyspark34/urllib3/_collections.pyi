from _typeshed import Incomplete
from collections import MutableMapping, OrderedDict
from collections.abc import Generator

__all__ = ['RecentlyUsedContainer', 'HTTPHeaderDict']

class RLock:
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class RecentlyUsedContainer(MutableMapping):
    """
    Provides a thread-safe dict-like container which maintains up to
    ``maxsize`` keys while throwing away the least-recently-used keys beyond
    ``maxsize``.

    :param maxsize:
        Maximum number of recent elements to retain.

    :param dispose_func:
        Every time an item is evicted from the container,
        ``dispose_func(value)`` is called.  Callback which will get called
    """
    ContainerCls = OrderedDict
    dispose_func: Incomplete
    lock: Incomplete
    def __init__(self, maxsize: int = 10, dispose_func: Incomplete | None = None) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def clear(self) -> None: ...
    def keys(self): ...

class HTTPHeaderDict(MutableMapping):
    """
    :param headers:
        An iterable of field-value pairs. Must not contain multiple field names
        when compared case-insensitively.

    :param kwargs:
        Additional field-value pairs to pass in to ``dict.update``.

    A ``dict`` like container for storing HTTP Headers.

    Field names are stored and compared case-insensitively in compliance with
    RFC 7230. Iteration provides the first case-sensitive key seen for each
    case-insensitive pair.

    Using ``__setitem__`` syntax overwrites fields that compare equal
    case-insensitively in order to maintain ``dict``'s api. For fields that
    compare equal, instead create a new ``HTTPHeaderDict`` and use ``.add``
    in a loop.

    If multiple fields that are equal case-insensitively are passed to the
    constructor or ``.update``, the behavior is undefined and some will be
    lost.

    >>> headers = HTTPHeaderDict()
    >>> headers.add('Set-Cookie', 'foo=bar')
    >>> headers.add('set-cookie', 'baz=quxx')
    >>> headers['content-length'] = '7'
    >>> headers['SET-cookie']
    'foo=bar, baz=quxx'
    >>> headers['Content-Length']
    '7'
    """
    def __init__(self, headers: Incomplete | None = None, **kwargs) -> None: ...
    def __setitem__(self, key, val) -> None: ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def pop(self, key, default=...):
        """D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised.
        """
    def discard(self, key) -> None: ...
    def add(self, key, val) -> None:
        """Adds a (name, value) pair, doesn't overwrite the value if it already
        exists.

        >>> headers = HTTPHeaderDict(foo='bar')
        >>> headers.add('Foo', 'baz')
        >>> headers['foo']
        'bar, baz'
        """
    def extend(self, *args, **kwargs) -> None:
        """Generic import function for any type of header-like object.
        Adapted version of MutableMapping.update in order to insert items
        with self.add instead of self.__setitem__
        """
    def getlist(self, key, default=...):
        """Returns a list of all the values for the named field. Returns an
        empty list if the key doesn't exist."""
    getheaders = getlist
    getallmatchingheaders = getlist
    iget = getlist
    get_all = getlist
    def copy(self): ...
    def iteritems(self) -> Generator[Incomplete, None, None]:
        """Iterate over all header lines, including duplicate ones."""
    def itermerged(self) -> Generator[Incomplete, None, None]:
        """Iterate over all headers, merging duplicate ones together."""
    def items(self): ...
    @classmethod
    def from_httplib(cls, message):
        """Read headers from a Python 2 httplib message object."""
