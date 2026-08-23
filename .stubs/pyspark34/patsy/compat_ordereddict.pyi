from _typeshed import Incomplete
from collections.abc import Generator

class OrderedDict(dict):
    """Dictionary that remembers insertion order"""
    def __init__(self, *args, **kwds) -> None:
        """Initialize an ordered dictionary.  Signature is the same as for
        regular dictionaries, but keyword arguments are not recommended
        because their insertion order is arbitrary.

        """
    def __setitem__(self, key, value, dict_setitem=...) -> None:
        """od.__setitem__(i, y) <==> od[i]=y"""
    def __delitem__(self, key, dict_delitem=...) -> None:
        """od.__delitem__(y) <==> del od[y]"""
    def __iter__(self):
        """od.__iter__() <==> iter(od)"""
    def __reversed__(self) -> Generator[Incomplete, None, None]:
        """od.__reversed__() <==> reversed(od)"""
    def clear(self) -> None:
        """od.clear() -> None.  Remove all items from od."""
    def popitem(self, last: bool = True):
        """od.popitem() -> (k, v), return and remove a (key, value) pair.
        Pairs are returned in LIFO order if last is true or FIFO order if false.

        """
    def keys(self):
        """od.keys() -> list of keys in od"""
    def values(self):
        """od.values() -> list of values in od"""
    def items(self):
        """od.items() -> list of (key, value) pairs in od"""
    def iterkeys(self):
        """od.iterkeys() -> an iterator over the keys in od"""
    def itervalues(self) -> Generator[Incomplete, None, None]:
        """od.itervalues -> an iterator over the values in od"""
    def iteritems(self) -> Generator[Incomplete, None, None]:
        """od.iteritems -> an iterator over the (key, value) items in od"""
    def update(*args, **kwds) -> None:
        """od.update(E, **F) -> None.  Update od from dict/iterable E and F.

        If E is a dict instance, does:           for k in E: od[k] = E[k]
        If E has a .keys() method, does:         for k in E.keys(): od[k] = E[k]
        Or if E is an iterable of items, does:   for k, v in E: od[k] = v
        In either case, this is followed by:     for k, v in F.items(): od[k] = v

        """
    def pop(self, key, default=...):
        """od.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised.

        """
    def setdefault(self, key, default: Incomplete | None = None):
        """od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od"""
    def __reduce__(self):
        """Return state information for pickling"""
    def copy(self):
        """od.copy() -> a shallow copy of od"""
    @classmethod
    def fromkeys(cls, iterable, value: Incomplete | None = None):
        """OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S
        and values equal to v (which defaults to None).

        """
    def __eq__(self, other):
        """od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
        while comparison to a regular mapping is order-insensitive.

        """
    def __ne__(self, other): ...
    def viewkeys(self):
        """od.viewkeys() -> a set-like object providing a view on od's keys"""
    def viewvalues(self):
        """od.viewvalues() -> an object providing a view on od's values"""
    def viewitems(self):
        """od.viewitems() -> a set-like object providing a view on od's items"""
