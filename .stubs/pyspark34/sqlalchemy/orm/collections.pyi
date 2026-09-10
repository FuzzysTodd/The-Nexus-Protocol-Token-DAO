from ..util.typing import Protocol
from .attributes import AttributeEventToken, CollectionAttributeImpl
from .mapped_collection import KeyFuncDict as KeyFuncDict, attribute_keyed_dict as attribute_keyed_dict, column_keyed_dict as column_keyed_dict, keyfunc_mapping as keyfunc_mapping
from .state import InstanceState
from _typeshed import Incomplete
from typing import Any, Collection, Dict, Iterable, List, Set

__all__ = ['collection', 'collection_adapter', 'keyfunc_mapping', 'column_keyed_dict', 'attribute_keyed_dict', 'column_keyed_dict', 'attribute_keyed_dict', 'MappedCollection', 'KeyFuncDict']

class _CollectionConverterProtocol(Protocol):
    def __call__(self, collection: _COL) -> _COL: ...

class _AdaptedCollectionProtocol(Protocol): ...

class collection:
    """Decorators for entity collection classes.

    The decorators fall into two groups: annotations and interception recipes.

    The annotating decorators (appender, remover, iterator, converter,
    internally_instrumented) indicate the method's purpose and take no
    arguments.  They are not written with parens::

        @collection.appender
        def append(self, append): ...

    The recipe decorators all require parens, even those that take no
    arguments::

        @collection.adds('entity')
        def insert(self, position, entity): ...

        @collection.removes_return()
        def popitem(self): ...

    """
    @staticmethod
    def appender(fn):
        """Tag the method as the collection appender.

        The appender method is called with one positional argument: the value
        to append. The method will be automatically decorated with 'adds(1)'
        if not already decorated::

            @collection.appender
            def add(self, append): ...

            # or, equivalently
            @collection.appender
            @collection.adds(1)
            def add(self, append): ...

            # for mapping type, an 'append' may kick out a previous value
            # that occupies that slot.  consider d['a'] = 'foo'- any previous
            # value in d['a'] is discarded.
            @collection.appender
            @collection.replaces(1)
            def add(self, entity):
                key = some_key_func(entity)
                previous = None
                if key in self:
                    previous = self[key]
                self[key] = entity
                return previous

        If the value to append is not allowed in the collection, you may
        raise an exception.  Something to remember is that the appender
        will be called for each object mapped by a database query.  If the
        database contains rows that violate your collection semantics, you
        will need to get creative to fix the problem, as access via the
        collection will not work.

        If the appender method is internally instrumented, you must also
        receive the keyword argument '_sa_initiator' and ensure its
        promulgation to collection events.

        """
    @staticmethod
    def remover(fn):
        """Tag the method as the collection remover.

        The remover method is called with one positional argument: the value
        to remove. The method will be automatically decorated with
        :meth:`removes_return` if not already decorated::

            @collection.remover
            def zap(self, entity): ...

            # or, equivalently
            @collection.remover
            @collection.removes_return()
            def zap(self, ): ...

        If the value to remove is not present in the collection, you may
        raise an exception or return None to ignore the error.

        If the remove method is internally instrumented, you must also
        receive the keyword argument '_sa_initiator' and ensure its
        promulgation to collection events.

        """
    @staticmethod
    def iterator(fn):
        """Tag the method as the collection remover.

        The iterator method is called with no arguments.  It is expected to
        return an iterator over all collection members::

            @collection.iterator
            def __iter__(self): ...

        """
    @staticmethod
    def internally_instrumented(fn):
        """Tag the method as instrumented.

        This tag will prevent any decoration from being applied to the
        method. Use this if you are orchestrating your own calls to
        :func:`.collection_adapter` in one of the basic SQLAlchemy
        interface methods, or to prevent an automatic ABC method
        decoration from wrapping your implementation::

            # normally an 'extend' method on a list-like class would be
            # automatically intercepted and re-implemented in terms of
            # SQLAlchemy events and append().  your implementation will
            # never be called, unless:
            @collection.internally_instrumented
            def extend(self, items): ...

        """
    @staticmethod
    def converter(fn):
        """Tag the method as the collection converter.

        This optional method will be called when a collection is being
        replaced entirely, as in::

            myobj.acollection = [newvalue1, newvalue2]

        The converter method will receive the object being assigned and should
        return an iterable of values suitable for use by the ``appender``
        method.  A converter must not assign values or mutate the collection,
        its sole job is to adapt the value the user provides into an iterable
        of values for the ORM's use.

        The default converter implementation will use duck-typing to do the
        conversion.  A dict-like collection will be convert into an iterable
        of dictionary values, and other types will simply be iterated::

            @collection.converter
            def convert(self, other): ...

        If the duck-typing of the object does not match the type of this
        collection, a TypeError is raised.

        Supply an implementation of this method if you want to expand the
        range of possible types that can be assigned in bulk or perform
        validation on the values about to be assigned.

        """
    @staticmethod
    def adds(arg):
        '''Mark the method as adding an entity to the collection.

        Adds "add to collection" handling to the method.  The decorator
        argument indicates which method argument holds the SQLAlchemy-relevant
        value.  Arguments can be specified positionally (i.e. integer) or by
        name::

            @collection.adds(1)
            def push(self, item): ...

            @collection.adds(\'entity\')
            def do_stuff(self, thing, entity=None): ...

        '''
    @staticmethod
    def replaces(arg):
        '''Mark the method as replacing an entity in the collection.

        Adds "add to collection" and "remove from collection" handling to
        the method.  The decorator argument indicates which method argument
        holds the SQLAlchemy-relevant value to be added, and return value, if
        any will be considered the value to remove.

        Arguments can be specified positionally (i.e. integer) or by name::

            @collection.replaces(2)
            def __setitem__(self, index, item): ...

        '''
    @staticmethod
    def removes(arg):
        '''Mark the method as removing an entity in the collection.

        Adds "remove from collection" handling to the method.  The decorator
        argument indicates which method argument holds the SQLAlchemy-relevant
        value to be removed. Arguments can be specified positionally (i.e.
        integer) or by name::

            @collection.removes(1)
            def zap(self, item): ...

        For methods where the value to remove is not known at call-time, use
        collection.removes_return.

        '''
    @staticmethod
    def removes_return():
        '''Mark the method as removing an entity in the collection.

        Adds "remove from collection" handling to the method.  The return
        value of the method, if any, is considered the value to remove.  The
        method arguments are not inspected::

            @collection.removes_return()
            def pop(self): ...

        For methods where the value to remove is known at call-time, use
        collection.remove.

        '''

def collection_adapter(collection: Collection[Any]) -> CollectionAdapter:
    """Fetch the :class:`.CollectionAdapter` for a collection."""

class CollectionAdapter:
    """Bridges between the ORM and arbitrary Python collections.

    Proxies base-level collection operations (append, remove, iterate)
    to the underlying Python collection, and emits add/remove events for
    entities entering or leaving the collection.

    The ORM uses :class:`.CollectionAdapter` exclusively for interaction with
    entity collections.


    """
    attr: CollectionAttributeImpl
    owner_state: InstanceState[Any]
    invalidated: bool
    empty: bool
    def __init__(self, attr: CollectionAttributeImpl, owner_state: InstanceState[Any], data: _AdaptedCollectionProtocol) -> None: ...
    @property
    def data(self) -> _AdaptedCollectionProtocol:
        """The entity collection being adapted."""
    def bulk_appender(self): ...
    def append_with_event(self, item: Any, initiator: AttributeEventToken | None = None) -> None:
        """Add an entity to the collection, firing mutation events."""
    def append_without_event(self, item: Any) -> None:
        """Add or restore an entity to the collection, firing no events."""
    def append_multiple_without_event(self, items: Iterable[Any]) -> None:
        """Add or restore an entity to the collection, firing no events."""
    def bulk_remover(self): ...
    def remove_with_event(self, item: Any, initiator: AttributeEventToken | None = None) -> None:
        """Remove an entity from the collection, firing mutation events."""
    def remove_without_event(self, item: Any) -> None:
        """Remove an entity from the collection, firing no events."""
    def clear_with_event(self, initiator: AttributeEventToken | None = None) -> None:
        """Empty the collection, firing a mutation event for each entity."""
    def clear_without_event(self) -> None:
        """Empty the collection, firing no events."""
    def __iter__(self):
        """Iterate over entities in the collection."""
    def __len__(self) -> int:
        """Count entities in the collection."""
    def __bool__(self) -> bool: ...
    def fire_append_wo_mutation_event(self, item, initiator: Incomplete | None = None, key=...):
        """Notify that a entity is entering the collection but is already
        present.


        Initiator is a token owned by the InstrumentedAttribute that
        initiated the membership mutation, and should be left as None
        unless you are passing along an initiator value from a chained
        operation.

        .. versionadded:: 1.4.15

        """
    def fire_append_event(self, item, initiator: Incomplete | None = None, key=...):
        """Notify that a entity has entered the collection.

        Initiator is a token owned by the InstrumentedAttribute that
        initiated the membership mutation, and should be left as None
        unless you are passing along an initiator value from a chained
        operation.

        """
    def fire_remove_event(self, item, initiator: Incomplete | None = None, key=...) -> None:
        """Notify that a entity has been removed from the collection.

        Initiator is the InstrumentedAttribute that initiated the membership
        mutation, and should be left as None unless you are passing along
        an initiator value from a chained operation.

        """
    def fire_pre_remove_event(self, initiator: Incomplete | None = None, key=...) -> None:
        """Notify that an entity is about to be removed from the collection.

        Only called if the entity cannot be removed after calling
        fire_remove_event().

        """

class InstrumentedList(List[_T]):
    """An instrumented version of the built-in list."""
class InstrumentedSet(Set[_T]):
    """An instrumented version of the built-in set."""
class InstrumentedDict(Dict[_KT, _VT]):
    """An instrumented version of the built-in dict."""

# Names in __all__ with no definition:
#   MappedCollection
