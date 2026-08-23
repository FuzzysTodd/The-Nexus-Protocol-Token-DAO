from _typeshed import Incomplete
from zope.interface import Interface
from zope.interface.common import collections

__docformat__: str

class IMinimalSequence(collections.IIterable):
    """Most basic sequence interface.

    All sequences are iterable.  This requires at least one of the
    following:

    - a `__getitem__()` method that takes a single argument; integer
      values starting at 0 must be supported, and `IndexError` should
      be raised for the first index for which there is no value, or

    - an `__iter__()` method that returns an iterator as defined in
      the Python documentation (http://docs.python.org/lib/typeiter.html).

    """
    def __getitem__(index) -> None:
        """``x.__getitem__(index) <==> x[index]``

        Declaring this interface does not specify whether `__getitem__`
        supports slice objects."""

class IFiniteSequence(collections.ISized, IMinimalSequence):
    """
    A sequence of bound size.

    .. versionchanged:: 5.0.0
       Extend ``ISized``
    """

class IReadSequence(collections.IContainer, IFiniteSequence):
    """
    read interface shared by tuple and list

    This interface is similar to
    :class:`~zope.interface.common.collections.ISequence`, but
    requires that all instances be totally ordered. Most users
    should prefer ``ISequence``.

    .. versionchanged:: 5.0.0
       Extend ``IContainer``
    """
    def __contains__(item) -> bool:
        """``x.__contains__(item) <==> item in x``"""
    def __lt__(other):
        """``x.__lt__(other) <==> x < other``"""
    def __le__(other):
        """``x.__le__(other) <==> x <= other``"""
    def __eq__(other):
        """``x.__eq__(other) <==> x == other``"""
    def __ne__(other):
        """``x.__ne__(other) <==> x != other``"""
    def __gt__(other):
        """``x.__gt__(other) <==> x > other``"""
    def __ge__(other):
        """``x.__ge__(other) <==> x >= other``"""
    def __add__(other) -> None:
        """``x.__add__(other) <==> x + other``"""
    def __mul__(n) -> None:
        """``x.__mul__(n) <==> x * n``"""
    def __rmul__(n) -> None:
        """``x.__rmul__(n) <==> n * x``"""

class IExtendedReadSequence(IReadSequence):
    """Full read interface for lists"""
    def count(item) -> None:
        """Return number of occurrences of value"""
    def index(item, *args) -> None:
        """index(value, [start, [stop]]) -> int

        Return first index of *value*
        """

class IUniqueMemberWriteSequence(Interface):
    """The write contract for a sequence that may enforce unique members"""
    def __setitem__(index, item) -> None:
        """``x.__setitem__(index, item) <==> x[index] = item``

        Declaring this interface does not specify whether `__setitem__`
        supports slice objects.
        """
    def __delitem__(index) -> None:
        """``x.__delitem__(index) <==> del x[index]``

        Declaring this interface does not specify whether `__delitem__`
        supports slice objects.
        """
    def __iadd__(y) -> None:
        """``x.__iadd__(y) <==> x += y``"""
    def append(item) -> None:
        """Append item to end"""
    def insert(index, item) -> None:
        """Insert item before index"""
    def pop(index: int = -1) -> None:
        """Remove and return item at index (default last)"""
    def remove(item) -> None:
        """Remove first occurrence of value"""
    def reverse() -> None:
        """Reverse *IN PLACE*"""
    def sort(cmpfunc: Incomplete | None = None) -> None:
        """Stable sort *IN PLACE*; `cmpfunc(x, y)` -> -1, 0, 1"""
    def extend(iterable) -> None:
        """Extend list by appending elements from the iterable"""

class IWriteSequence(IUniqueMemberWriteSequence):
    """Full write contract for sequences"""
    def __imul__(n) -> None:
        """``x.__imul__(n) <==> x *= n``"""

class ISequence(IReadSequence, IWriteSequence):
    """
    Full sequence contract.

    New code should prefer
    :class:`~zope.interface.common.collections.IMutableSequence`.

    Compared to that interface, which is implemented by :class:`list`
    (:class:`~zope.interface.common.builtins.IList`), among others,
    this interface is missing the following methods:

        - clear

        - count

        - index

    This interface adds the following methods:

        - sort
    """
