from _typeshed import Incomplete
from zope.interface import Interface
from zope.interface.common import collections

class IItemMapping(Interface):
    """Simplest readable mapping object
    """
    def __getitem__(key) -> None:
        """Get a value for a key

        A `KeyError` is raised if there is no value for the key.
        """

class IReadMapping(collections.IContainer, IItemMapping):
    """
    Basic mapping interface.

    .. versionchanged:: 5.0.0
       Extend ``IContainer``
    """
    def get(key, default: Incomplete | None = None) -> None:
        """Get a value for a key

        The default is returned if there is no value for the key.
        """
    def __contains__(key) -> bool:
        """Tell if a key exists in the mapping."""

class IWriteMapping(Interface):
    """Mapping methods for changing data"""
    def __delitem__(key) -> None:
        """Delete a value from the mapping using the key."""
    def __setitem__(key, value) -> None:
        """Set a new item in the mapping."""

class IEnumerableMapping(collections.ISized, IReadMapping):
    """
    Mapping objects whose items can be enumerated.

    .. versionchanged:: 5.0.0
       Extend ``ISized``
    """
    def keys() -> None:
        """Return the keys of the mapping object.
        """
    def __iter__():
        """Return an iterator for the keys of the mapping object.
        """
    def values() -> None:
        """Return the values of the mapping object.
        """
    def items() -> None:
        """Return the items of the mapping object.
        """

class IMapping(IWriteMapping, IEnumerableMapping):
    """ Simple mapping interface """
class IIterableMapping(IEnumerableMapping):
    """A mapping that has distinct methods for iterating
    without copying.

    """

class IClonableMapping(Interface):
    """Something that can produce a copy of itself.

    This is available in `dict`.
    """
    def copy() -> None:
        """return copy of dict"""

class IExtendedReadMapping(IIterableMapping):
    """
    Something with a particular method equivalent to ``__contains__``.

    On Python 2, `dict` provided the ``has_key`` method, but it was removed
    in Python 3.
    """

class IExtendedWriteMapping(IWriteMapping):
    """Additional mutation methods.

    These are all provided by `dict`.
    """
    def clear() -> None:
        """delete all items"""
    def update(d) -> None:
        """ Update D from E: for k in E.keys(): D[k] = E[k]"""
    def setdefault(key, default: Incomplete | None = None) -> None:
        """D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D"""
    def pop(k, default: Incomplete | None = None) -> None:
        """
        pop(k[,default]) -> value

        Remove specified key and return the corresponding value.

        If key is not found, *default* is returned if given, otherwise
        `KeyError` is raised. Note that *default* must not be passed by
        name.
        """
    def popitem() -> None:
        """remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if mapping is empty"""

class IFullMapping(collections.IMutableMapping, IExtendedReadMapping, IExtendedWriteMapping, IClonableMapping, IMapping):
    """
    Full mapping interface.

    Most uses of this interface should instead use
    :class:`~zope.interface.commons.collections.IMutableMapping` (one of the
    bases of this interface). The required methods are the same.

    .. versionchanged:: 5.0.0
       Extend ``IMutableMapping``
    """
