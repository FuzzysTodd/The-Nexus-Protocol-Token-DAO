from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['AdapterRegistry', 'VerifyingAdapterRegistry']

class BaseAdapterRegistry:
    '''
    A basic implementation of the data storage and algorithms required
    for a :class:`zope.interface.interfaces.IAdapterRegistry`.

    Subclasses can set the following attributes to control how the data
    is stored; in particular, these hooks can be helpful for ZODB
    persistence. They can be class attributes that are the named (or similar) type, or
    they can be methods that act as a constructor for an object that behaves
    like the types defined here; this object will not assume that they are type
    objects, but subclasses are free to do so:

    _sequenceType = list
      This is the type used for our two mutable top-level "byorder" sequences.
      Must support mutation operations like ``append()`` and ``del seq[index]``.
      These are usually small (< 10). Although at least one of them is
      accessed when performing lookups or queries on this object, the other
      is untouched. In many common scenarios, both are only required when
      mutating registrations and subscriptions (like what
      :meth:`zope.interface.interfaces.IComponents.registerUtility` does).
      This use pattern makes it an ideal candidate to be a
      :class:`~persistent.list.PersistentList`.
    _leafSequenceType = tuple
      This is the type used for the leaf sequences of subscribers.
      It could be set to a ``PersistentList`` to avoid many unnecessary data
      loads when subscribers aren\'t being used. Mutation operations are directed
      through :meth:`_addValueToLeaf` and :meth:`_removeValueFromLeaf`; if you use
      a mutable type, you\'ll need to override those.
    _mappingType = dict
      This is the mutable mapping type used for the keyed mappings.
      A :class:`~persistent.mapping.PersistentMapping`
      could be used to help reduce the number of data loads when the registry is large
      and parts of it are rarely used. Further reductions in data loads can come from
      using a :class:`~BTrees.OOBTree.OOBTree`, but care is required
      to be sure that all required/provided
      values are fully ordered (e.g., no required or provided values that are classes
      can be used).
    _providedType = dict
      This is the mutable mapping type used for the ``_provided`` mapping.
      This is separate from the generic mapping type because the values
      are always integers, so one might choose to use a more optimized data
      structure such as a :class:`~BTrees.OIBTree.OIBTree`.
      The same caveats regarding key types
      apply as for ``_mappingType``.

    It is possible to also set these on an instance, but because of the need to
    potentially also override :meth:`_addValueToLeaf` and :meth:`_removeValueFromLeaf`,
    this may be less useful in a persistent scenario; using a subclass is recommended.

    .. versionchanged:: 5.3.0
        Add support for customizing the way internal data
        structures are created.
    .. versionchanged:: 5.3.0
        Add methods :meth:`rebuild`, :meth:`allRegistrations`
        and :meth:`allSubscriptions`.
    '''
    __bases__: Incomplete
    def __init__(self, bases=()) -> None: ...
    def changed(self, originally_changed) -> None: ...
    def register(self, required, provided, name, value) -> None: ...
    def registered(self, required, provided, name: str = ''): ...
    def allRegistrations(self) -> Generator[Incomplete, Incomplete, None]:
        """
        Yields tuples ``(required, provided, name, value)`` for all
        the registrations that this object holds.

        These tuples could be passed as the arguments to the
        :meth:`register` method on another adapter registry to
        duplicate the registrations this object holds.

        .. versionadded:: 5.3.0
        """
    def unregister(self, required, provided, name, value: Incomplete | None = None): ...
    def subscribe(self, required, provided, value) -> None: ...
    def subscribed(self, required, provided, subscriber): ...
    def allSubscriptions(self) -> Generator[Incomplete, None, None]:
        """
        Yields tuples ``(required, provided, value)`` for all the
        subscribers that this object holds.

        These tuples could be passed as the arguments to the
        :meth:`subscribe` method on another adapter registry to
        duplicate the registrations this object holds.

        .. versionadded:: 5.3.0
        """
    def unsubscribe(self, required, provided, value: Incomplete | None = None) -> None: ...
    def rebuild(self):
        """
        Rebuild (and replace) all the internal data structures of this
        object.

        This is useful, especially for persistent implementations, if
        you suspect an issue with reference counts keeping interfaces
        alive even though they are no longer used.

        It is also useful if you or a subclass change the data types
        (``_mappingType`` and friends) that are to be used.

        This method replaces all internal data structures with new objects;
        it specifically does not re-use any storage.

        .. versionadded:: 5.3.0
        """
    def get(self, _): ...

class LookupBase:
    def __init__(self) -> None: ...
    def changed(self, ignored: Incomplete | None = None) -> None: ...
    def lookup(self, required, provided, name: str = '', default: Incomplete | None = None): ...
    def lookup1(self, required, provided, name: str = '', default: Incomplete | None = None): ...
    def queryAdapter(self, object, provided, name: str = '', default: Incomplete | None = None): ...
    def adapter_hook(self, provided, object, name: str = '', default: Incomplete | None = None): ...
    def lookupAll(self, required, provided): ...
    def subscriptions(self, required, provided): ...

class VerifyingBase(LookupBaseFallback):
    def changed(self, originally_changed) -> None: ...
    def lookupAll(self, required, provided): ...
    def subscriptions(self, required, provided): ...

class AdapterLookupBase:
    def __init__(self, registry) -> None: ...
    def changed(self, ignored: Incomplete | None = None) -> None: ...
    def init_extendors(self) -> None: ...
    def add_extendor(self, provided) -> None: ...
    def remove_extendor(self, provided) -> None: ...
    def queryMultiAdapter(self, objects, provided, name: str = '', default: Incomplete | None = None): ...
    def names(self, required, provided): ...
    def subscribers(self, objects, provided): ...

class AdapterLookup(AdapterLookupBase, LookupBase): ...

class AdapterRegistry(BaseAdapterRegistry):
    """
    A full implementation of ``IAdapterRegistry`` that adds support for
    sub-registries.
    """
    LookupClass = AdapterLookup
    def __init__(self, bases=()) -> None: ...
    def changed(self, originally_changed) -> None: ...

class VerifyingAdapterLookup(AdapterLookupBase, VerifyingBase): ...

class VerifyingAdapterRegistry(BaseAdapterRegistry):
    """
    The most commonly-used adapter registry.
    """
    LookupClass = VerifyingAdapterLookup
