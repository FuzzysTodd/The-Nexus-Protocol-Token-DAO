import dataclasses
from . import collections as collections, interfaces as interfaces
from .. import event as event, exc as exc, inspection as inspection, util as util
from ..event import EventTarget as EventTarget, dispatcher as dispatcher
from ..event.base import _Dispatch
from ..sql import base as sql_base, cache_key as cache_key, coercions as coercions, roles as roles, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument, _InfoType
from ..sql.cache_key import HasCacheKey as HasCacheKey
from ..sql.elements import ColumnElement as ColumnElement, Label as Label
from ..sql.operators import OperatorType as OperatorType
from ..sql.selectable import FromClause as FromClause
from ..sql.visitors import InternalTraversal as InternalTraversal
from ..util.typing import Literal as Literal, Self as Self, TypeGuard as TypeGuard
from ._typing import _EntityType, _ExternalEntityType, _InstanceDict, _InternalEntityType, _LoaderCallable, _O, insp_is_aliased_class as insp_is_aliased_class
from .base import ATTR_EMPTY as ATTR_EMPTY, ATTR_WAS_SET as ATTR_WAS_SET, CALLABLES_OK as CALLABLES_OK, DEFERRED_HISTORY_LOAD as DEFERRED_HISTORY_LOAD, INCLUDE_PENDING_MUTATIONS as INCLUDE_PENDING_MUTATIONS, INIT_OK as INIT_OK, LOAD_AGAINST_COMMITTED as LOAD_AGAINST_COMMITTED, LoaderCallableStatus as LoaderCallableStatus, NEVER_SET as NEVER_SET, NON_PERSISTENT_OK as NON_PERSISTENT_OK, NO_AUTOFLUSH as NO_AUTOFLUSH, NO_CHANGE as NO_CHANGE, NO_KEY as NO_KEY, NO_RAISE as NO_RAISE, NO_VALUE as NO_VALUE, PASSIVE_CLASS_MISMATCH as PASSIVE_CLASS_MISMATCH, PASSIVE_NO_FETCH as PASSIVE_NO_FETCH, PASSIVE_NO_FETCH_RELATED as PASSIVE_NO_FETCH_RELATED, PASSIVE_NO_INITIALIZE as PASSIVE_NO_INITIALIZE, PASSIVE_NO_RESULT as PASSIVE_NO_RESULT, PASSIVE_OFF as PASSIVE_OFF, PASSIVE_ONLY_PERSISTENT as PASSIVE_ONLY_PERSISTENT, PASSIVE_RETURN_NO_VALUE as PASSIVE_RETURN_NO_VALUE, PassiveFlag as PassiveFlag, RELATED_OBJECT_OK as RELATED_OBJECT_OK, SQLORMExpression as SQLORMExpression, SQL_OK as SQL_OK, _DeclarativeMapped, instance_str as instance_str, state_str as state_str
from .collections import CollectionAdapter as CollectionAdapter, _AdaptedCollectionProtocol
from .interfaces import MapperProperty as MapperProperty
from .relationships import RelationshipProperty as RelationshipProperty
from .state import InstanceState as InstanceState
from .util import AliasedInsp as AliasedInsp
from .writeonly import WriteOnlyAttributeImpl as WriteOnlyAttributeImpl
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, Dict, List, NamedTuple, Sequence, Tuple, Type, overload

class QueryableAttribute(_DeclarativeMapped[_T_co], SQLORMExpression[_T_co], interfaces.InspectionAttr, interfaces.PropComparator[_T_co], roles.JoinTargetRole, roles.OnClauseRole, sql_base.Immutable, cache_key.SlotsMemoizedHasCacheKey, util.MemoizedSlots, EventTarget):
    """Base class for :term:`descriptor` objects that intercept
    attribute events on behalf of a :class:`.MapperProperty`
    object.  The actual :class:`.MapperProperty` is accessible
    via the :attr:`.QueryableAttribute.property`
    attribute.


    .. seealso::

        :class:`.InstrumentedAttribute`

        :class:`.MapperProperty`

        :attr:`_orm.Mapper.all_orm_descriptors`

        :attr:`_orm.Mapper.attrs`
    """
    is_attribute: bool
    dispatch: dispatcher[QueryableAttribute[_T_co]]
    class_: _ExternalEntityType[Any]
    key: str
    parententity: _InternalEntityType[Any]
    impl: AttributeImpl
    comparator: interfaces.PropComparator[_T_co]
    __visit_name__: str
    def __init__(self, class_: _ExternalEntityType[_O], key: str, parententity: _InternalEntityType[_O], comparator: interfaces.PropComparator[_T_co], impl: AttributeImpl | None = None, of_type: _InternalEntityType[Any] | None = None, extra_criteria: Tuple[ColumnElement[bool], ...] = ()) -> None: ...
    def __reduce__(self) -> Any: ...
    def get_history(self, instance: Any, passive: PassiveFlag = ...) -> History: ...
    @property
    def info(self) -> _InfoType:
        """Return the 'info' dictionary for the underlying SQL element.

        The behavior here is as follows:

        * If the attribute is a column-mapped property, i.e.
          :class:`.ColumnProperty`, which is mapped directly
          to a schema-level :class:`_schema.Column` object, this attribute
          will return the :attr:`.SchemaItem.info` dictionary associated
          with the core-level :class:`_schema.Column` object.

        * If the attribute is a :class:`.ColumnProperty` but is mapped to
          any other kind of SQL expression other than a
          :class:`_schema.Column`,
          the attribute will refer to the :attr:`.MapperProperty.info`
          dictionary associated directly with the :class:`.ColumnProperty`,
          assuming the SQL expression itself does not have its own ``.info``
          attribute (which should be the case, unless a user-defined SQL
          construct has defined one).

        * If the attribute refers to any other kind of
          :class:`.MapperProperty`, including :class:`.Relationship`,
          the attribute will refer to the :attr:`.MapperProperty.info`
          dictionary associated with that :class:`.MapperProperty`.

        * To access the :attr:`.MapperProperty.info` dictionary of the
          :class:`.MapperProperty` unconditionally, including for a
          :class:`.ColumnProperty` that's associated directly with a
          :class:`_schema.Column`, the attribute can be referred to using
          :attr:`.QueryableAttribute.property` attribute, as
          ``MyClass.someattribute.property.info``.

        .. seealso::

            :attr:`.SchemaItem.info`

            :attr:`.MapperProperty.info`

        """
    parent: _InternalEntityType[Any]
    expression: ColumnElement[_T_co]
    def __clause_element__(self) -> ColumnElement[_T_co]: ...
    def adapt_to_entity(self, adapt_to_entity: AliasedInsp[Any]) -> Self: ...
    def of_type(self, entity: _EntityType[Any]) -> QueryableAttribute[_T]: ...
    def and_(self, *clauses: _ColumnExpressionArgument[bool]) -> QueryableAttribute[bool]: ...
    def label(self, name: str | None) -> Label[_T_co]: ...
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def hasparent(self, state: InstanceState[Any], optimistic: bool = False) -> bool: ...
    def __getattr__(self, key: str) -> Any: ...

class InstrumentedAttribute(QueryableAttribute[_T]):
    """Class bound instrumented attribute which adds basic
    :term:`descriptor` methods.

    See :class:`.QueryableAttribute` for a description of most features.


    """
    inherit_cache: bool
    def __set__(self, instance: object, value: Any) -> None: ...
    def __delete__(self, instance: object) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T: ...

@dataclasses.dataclass(frozen=True)
class AdHocHasEntityNamespace(HasCacheKey):
    is_mapper: ClassVar[bool] = ...
    is_aliased_class: ClassVar[bool] = ...
    @property
    def entity_namespace(self): ...
    def __init__(self, _entity_namespace) -> None: ...

def create_proxied_attribute(descriptor: Any) -> Callable[..., QueryableAttribute[Any]]:
    """Create an QueryableAttribute / user descriptor hybrid.

    Returns a new QueryableAttribute type that delegates descriptor
    behavior and getattr() to the given descriptor.
    """

OP_REMOVE: Incomplete
OP_APPEND: Incomplete
OP_REPLACE: Incomplete
OP_BULK_REPLACE: Incomplete
OP_MODIFIED: Incomplete

class AttributeEventToken:
    """A token propagated throughout the course of a chain of attribute
    events.

    Serves as an indicator of the source of the event and also provides
    a means of controlling propagation across a chain of attribute
    operations.

    The :class:`.Event` object is sent as the ``initiator`` argument
    when dealing with events such as :meth:`.AttributeEvents.append`,
    :meth:`.AttributeEvents.set`,
    and :meth:`.AttributeEvents.remove`.

    The :class:`.Event` object is currently interpreted by the backref
    event handlers, and is used to control the propagation of operations
    across two mutually-dependent attributes.

    .. versionchanged:: 2.0  Changed the name from ``AttributeEvent``
       to ``AttributeEventToken``.

    :attribute impl: The :class:`.AttributeImpl` which is the current event
     initiator.

    :attribute op: The symbol :attr:`.OP_APPEND`, :attr:`.OP_REMOVE`,
     :attr:`.OP_REPLACE`, or :attr:`.OP_BULK_REPLACE`, indicating the
     source operation.

    """
    impl: Incomplete
    op: Incomplete
    parent_token: Incomplete
    def __init__(self, attribute_impl: AttributeImpl, op: util.symbol) -> None: ...
    def __eq__(self, other): ...
    @property
    def key(self): ...
    def hasparent(self, state): ...
AttributeEvent = AttributeEventToken
Event = AttributeEventToken

class AttributeImpl:
    """internal implementation for instrumented attributes."""
    collection: bool
    default_accepts_scalar_loader: bool
    uses_objects: bool
    supports_population: bool
    dynamic: bool
    class_: Incomplete
    key: Incomplete
    callable_: Incomplete
    dispatch: Incomplete
    trackparent: Incomplete
    parent_token: Incomplete
    send_modified_events: Incomplete
    is_equal: Incomplete
    accepts_scalar_loader: Incomplete
    load_on_unexpire: Incomplete
    def __init__(self, class_: _ExternalEntityType[_O], key: str, callable_: _LoaderCallable | None, dispatch: _Dispatch[QueryableAttribute[Any]], trackparent: bool = False, compare_function: Callable[..., bool] | None = None, active_history: bool = False, parent_token: AttributeEventToken | None = None, load_on_unexpire: bool = True, send_modified_events: bool = True, accepts_scalar_loader: bool | None = None, **kwargs: Any) -> None:
        '''Construct an AttributeImpl.

        :param \\class_: associated class

        :param key: string name of the attribute

        :param \\callable_:
          optional function which generates a callable based on a parent
          instance, which produces the "default" values for a scalar or
          collection attribute when it\'s first accessed, if not present
          already.

        :param trackparent:
          if True, attempt to track if an instance has a parent attached
          to it via this attribute.

        :param compare_function:
          a function that compares two values which are normally
          assignable to this attribute.

        :param active_history:
          indicates that get_history() should always return the "old" value,
          even if it means executing a lazy callable upon attribute change.

        :param parent_token:
          Usually references the MapperProperty, used as a key for
          the hasparent() function to identify an "owning" attribute.
          Allows multiple AttributeImpls to all match a single
          owner attribute.

        :param load_on_unexpire:
          if False, don\'t include this attribute in a load-on-expired
          operation, i.e. the "expired_attribute_loader" process.
          The attribute can still be in the "expired" list and be
          considered to be "expired".   Previously, this flag was called
          "expire_missing" and is only used by a deferred column
          attribute.

        :param send_modified_events:
          if False, the InstanceState._modified_event method will have no
          effect; this means the attribute will never show up as changed in a
          history entry.

        '''
    active_history: Incomplete
    def hasparent(self, state: InstanceState[Any], optimistic: bool = False) -> bool:
        """Return the boolean value of a `hasparent` flag attached to
        the given state.

        The `optimistic` flag determines what the default return value
        should be if no `hasparent` flag can be located.

        As this function is used to determine if an instance is an
        *orphan*, instances that were loaded from storage should be
        assumed to not be orphans, until a True/False value for this
        flag is set.

        An instance attribute that is loaded by a callable function
        will also not have a `hasparent` flag.

        """
    def sethasparent(self, state: InstanceState[Any], parent_state: InstanceState[Any], value: bool) -> None:
        """Set a boolean flag on the given item corresponding to
        whether or not it is attached to a parent object via the
        attribute represented by this ``InstrumentedAttribute``.

        """
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    def get_all_pending(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> _AllPendingType:
        """Return a list of tuples of (state, obj)
        for all objects in this attribute's current state
        + history.

        Only applies to object-based attributes.

        This is an inlining of existing functionality
        which roughly corresponds to:

            get_state_history(
                        state,
                        key,
                        passive=PASSIVE_NO_INITIALIZE).sum()

        """
    def get(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> Any:
        """Retrieve a value from the given object.
        If a callable is assembled on this object's attribute, and
        passive is False, the callable will be executed and the
        resulting value will be set as the new value for this attribute.
        """
    def append(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def remove(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def pop(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def set(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None = None, passive: PassiveFlag = ..., check_old: Any = None, pop: bool = False) -> None: ...
    def delete(self, state: InstanceState[Any], dict_: _InstanceDict) -> None: ...
    def get_committed_value(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> Any:
        """return the unchanged value of this attribute"""
    def set_committed_value(self, state, dict_, value):
        """set an attribute value on the given instance and 'commit' it."""

class ScalarAttributeImpl(AttributeImpl):
    """represents a scalar value-holding InstrumentedAttribute."""
    default_accepts_scalar_loader: bool
    uses_objects: bool
    supports_population: bool
    collection: bool
    dynamic: bool
    def __init__(self, *arg, **kw) -> None: ...
    def delete(self, state: InstanceState[Any], dict_: _InstanceDict) -> None: ...
    def get_history(self, state: InstanceState[Any], dict_: Dict[str, Any], passive: PassiveFlag = ...) -> History: ...
    def set(self, state: InstanceState[Any], dict_: Dict[str, Any], value: Any, initiator: AttributeEventToken | None = None, passive: PassiveFlag = ..., check_old: object | None = None, pop: bool = False) -> None: ...
    def fire_replace_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: _T, previous: Any, initiator: AttributeEventToken | None) -> _T: ...
    def fire_remove_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None) -> None: ...

class ScalarObjectAttributeImpl(ScalarAttributeImpl):
    """represents a scalar-holding InstrumentedAttribute,
    where the target object is also instrumented.

    Adds events to delete/set operations.

    """
    default_accepts_scalar_loader: bool
    uses_objects: bool
    supports_population: bool
    collection: bool
    def delete(self, state: InstanceState[Any], dict_: _InstanceDict) -> None: ...
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    def get_all_pending(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> _AllPendingType: ...
    def set(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None = None, passive: PassiveFlag = ..., check_old: Any = None, pop: bool = False) -> None:
        """Set a value on the given InstanceState."""
    def fire_remove_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None) -> None: ...
    def fire_replace_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: _T, previous: Any, initiator: AttributeEventToken | None) -> _T: ...

class HasCollectionAdapter:
    collection: bool
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: Literal[None] = ..., passive: Literal[PassiveFlag.PASSIVE_OFF] = ...) -> CollectionAdapter: ...
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: _AdaptedCollectionProtocol = ..., passive: PassiveFlag = ...) -> CollectionAdapter: ...
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: _AdaptedCollectionProtocol | None = ..., passive: PassiveFlag = ...) -> Literal[LoaderCallableStatus.PASSIVE_NO_RESULT] | CollectionAdapter: ...
    def set(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None = None, passive: PassiveFlag = ..., check_old: Any = None, pop: bool = False, _adapt: bool = True) -> None: ...

class CollectionAttributeImpl(HasCollectionAdapter, AttributeImpl):
    '''A collection-holding attribute that instruments changes in membership.

    Only handles collections of instrumented objects.

    InstrumentedCollectionAttribute holds an arbitrary, user-specified
    container object (defaulting to a list) and brokers access to the
    CollectionAdapter, a "view" onto that object that presents consistent bag
    semantics to the orm layer independent of the user data implementation.

    '''
    uses_objects: bool
    collection: bool
    default_accepts_scalar_loader: bool
    supports_population: bool
    dynamic: bool
    copy: Incomplete
    collection_factory: Incomplete
    def __init__(self, class_, key, callable_, dispatch, typecallable: Incomplete | None = None, trackparent: bool = False, copy_function: Incomplete | None = None, compare_function: Incomplete | None = None, **kwargs) -> None: ...
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    def get_all_pending(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> _AllPendingType: ...
    def fire_append_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: _T, initiator: AttributeEventToken | None, key: Any | None) -> _T: ...
    def fire_append_wo_mutation_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: _T, initiator: AttributeEventToken | None, key: Any | None) -> _T: ...
    def fire_pre_remove_event(self, state: InstanceState[Any], dict_: _InstanceDict, initiator: AttributeEventToken | None, key: Any | None) -> None:
        '''A special event used for pop() operations.

        The "remove" event needs to have the item to be removed passed to
        it, which in the case of pop from a set, we don\'t have a way to access
        the item before the operation.   the event is used for all pop()
        operations (even though set.pop is the one where it is really needed).

        '''
    def fire_remove_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, key: Any | None) -> None: ...
    def delete(self, state: InstanceState[Any], dict_: _InstanceDict) -> None: ...
    def append(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def remove(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def pop(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def set(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None = None, passive: PassiveFlag = ..., check_old: Any = None, pop: bool = False, _adapt: bool = True) -> None: ...
    def set_committed_value(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any) -> _AdaptedCollectionProtocol:
        """Set an attribute value on the given instance and 'commit' it."""
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: Literal[None] = ..., passive: Literal[PassiveFlag.PASSIVE_OFF] = ...) -> CollectionAdapter: ...
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: _AdaptedCollectionProtocol = ..., passive: PassiveFlag = ...) -> CollectionAdapter: ...
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: _AdaptedCollectionProtocol | None = ..., passive: PassiveFlag = ...) -> Literal[LoaderCallableStatus.PASSIVE_NO_RESULT] | CollectionAdapter: ...

def backref_listeners(attribute: QueryableAttribute[Any], key: str, uselist: bool) -> None:
    """Apply listeners to synchronize a two-way relationship."""

class History(NamedTuple):
    """A 3-tuple of added, unchanged and deleted values,
    representing the changes which have occurred on an instrumented
    attribute.

    The easiest way to get a :class:`.History` object for a particular
    attribute on an object is to use the :func:`_sa.inspect` function::

        from sqlalchemy import inspect

        hist = inspect(myobject).attrs.myattribute.history

    Each tuple member is an iterable sequence:

    * ``added`` - the collection of items added to the attribute (the first
      tuple element).

    * ``unchanged`` - the collection of items that have not changed on the
      attribute (the second tuple element).

    * ``deleted`` - the collection of items that have been removed from the
      attribute (the third tuple element).

    """
    added: Tuple | List[Any]
    unchanged: Tuple | List[Any]
    deleted: Tuple | List[Any]
    def __bool__(self) -> bool: ...
    def empty(self) -> bool:
        """Return True if this :class:`.History` has no changes
        and no existing, unchanged state.

        """
    def sum(self) -> Sequence[Any]:
        """Return a collection of added + unchanged + deleted."""
    def non_deleted(self) -> Sequence[Any]:
        """Return a collection of added + unchanged."""
    def non_added(self) -> Sequence[Any]:
        """Return a collection of unchanged + deleted."""
    def has_changes(self) -> bool:
        """Return True if this :class:`.History` has changes."""
    def as_state(self) -> History: ...
    @classmethod
    def from_scalar_attribute(cls, attribute: ScalarAttributeImpl, state: InstanceState[Any], current: Any) -> History: ...
    @classmethod
    def from_object_attribute(cls, attribute: ScalarObjectAttributeImpl, state: InstanceState[Any], current: Any, original: Any = ...) -> History: ...
    @classmethod
    def from_collection(cls, attribute: CollectionAttributeImpl, state: InstanceState[Any], current: Any) -> History: ...

HISTORY_BLANK: Incomplete

def get_history(obj: object, key: str, passive: PassiveFlag = ...) -> History:
    """Return a :class:`.History` record for the given object
    and attribute key.

    This is the **pre-flush** history for a given attribute, which is
    reset each time the :class:`.Session` flushes changes to the
    current database transaction.

    .. note::

        Prefer to use the :attr:`.AttributeState.history` and
        :meth:`.AttributeState.load_history` accessors to retrieve the
        :class:`.History` for instance attributes.


    :param obj: an object whose class is instrumented by the
      attributes package.

    :param key: string attribute name.

    :param passive: indicates loading behavior for the attribute
       if the value is not already present.   This is a
       bitflag attribute, which defaults to the symbol
       :attr:`.PASSIVE_OFF` indicating all necessary SQL
       should be emitted.

    .. seealso::

        :attr:`.AttributeState.history`

        :meth:`.AttributeState.load_history` - retrieve history
        using loader callables if the value is not locally present.

    """
def get_state_history(state: InstanceState[Any], key: str, passive: PassiveFlag = ...) -> History: ...
def has_parent(cls, obj: _O, key: str, optimistic: bool = False) -> bool:
    """TODO"""
def register_attribute(class_: Type[_O], key: str, *, comparator: interfaces.PropComparator[_T], parententity: _InternalEntityType[_O], doc: str | None = None, **kw: Any) -> InstrumentedAttribute[_T]: ...
def register_attribute_impl(class_: Type[_O], key: str, uselist: bool = False, callable_: _LoaderCallable | None = None, useobject: bool = False, impl_class: Type[AttributeImpl] | None = None, backref: str | None = None, **kw: Any) -> QueryableAttribute[Any]: ...
def register_descriptor(class_: Type[Any], key: str, *, comparator: interfaces.PropComparator[_T], parententity: _InternalEntityType[Any], doc: str | None = None) -> InstrumentedAttribute[_T]: ...
def unregister_attribute(class_: Type[Any], key: str) -> None: ...
def init_collection(obj: object, key: str) -> CollectionAdapter:
    """Initialize a collection attribute and return the collection adapter.

    This function is used to provide direct access to collection internals
    for a previously unloaded attribute.  e.g.::

        collection_adapter = init_collection(someobject, 'elements')
        for elem in values:
            collection_adapter.append_without_event(elem)

    For an easier way to do the above, see
    :func:`~sqlalchemy.orm.attributes.set_committed_value`.

    :param obj: a mapped object

    :param key: string attribute name where the collection is located.

    """
def init_state_collection(state: InstanceState[Any], dict_: _InstanceDict, key: str) -> CollectionAdapter:
    """Initialize a collection attribute and return the collection adapter.

    Discards any existing collection which may be there.

    """
def set_committed_value(instance, key, value) -> None:
    """Set the value of an attribute with no history events.

    Cancels any previous history present.  The value should be
    a scalar value for scalar-holding attributes, or
    an iterable for any collection-holding attribute.

    This is the same underlying method used when a lazy loader
    fires off and loads additional data from the database.
    In particular, this method can be used by application code
    which has loaded additional attributes or collections through
    separate queries, which can then be attached to an instance
    as though it were part of its original loaded state.

    """
def set_attribute(instance: object, key: str, value: Any, initiator: AttributeEventToken | None = None) -> None:
    """Set the value of an attribute, firing history events.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.
    Custom attribute management schemes will need to make usage
    of this method to establish attribute state as understood
    by SQLAlchemy.

    :param instance: the object that will be modified

    :param key: string name of the attribute

    :param value: value to assign

    :param initiator: an instance of :class:`.Event` that would have
     been propagated from a previous event listener.  This argument
     is used when the :func:`.set_attribute` function is being used within
     an existing event listening function where an :class:`.Event` object
     is being supplied; the object may be used to track the origin of the
     chain of events.

     .. versionadded:: 1.2.3

    """
def get_attribute(instance: object, key: str) -> Any:
    """Get the value of an attribute, firing any callables required.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.
    Custom attribute management schemes will need to make usage
    of this method to make usage of attribute state as understood
    by SQLAlchemy.

    """
def del_attribute(instance: object, key: str) -> None:
    """Delete the value of an attribute, firing history events.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.
    Custom attribute management schemes will need to make usage
    of this method to establish attribute state as understood
    by SQLAlchemy.

    """
def flag_modified(instance: object, key: str) -> None:
    '''Mark an attribute on an instance as \'modified\'.

    This sets the \'modified\' flag on the instance and
    establishes an unconditional change event for the given attribute.
    The attribute must have a value present, else an
    :class:`.InvalidRequestError` is raised.

    To mark an object "dirty" without referring to any specific attribute
    so that it is considered within a flush, use the
    :func:`.attributes.flag_dirty` call.

    .. seealso::

        :func:`.attributes.flag_dirty`

    '''
def flag_dirty(instance: object) -> None:
    """Mark an instance as 'dirty' without any specific attribute mentioned.

    This is a special operation that will allow the object to travel through
    the flush process for interception by events such as
    :meth:`.SessionEvents.before_flush`.   Note that no SQL will be emitted in
    the flush process for an object that has no changes, even if marked dirty
    via this method.  However, a :meth:`.SessionEvents.before_flush` handler
    will be able to see the object in the :attr:`.Session.dirty` collection and
    may establish changes on it, which will then be included in the SQL
    emitted.

    .. versionadded:: 1.2

    .. seealso::

        :func:`.attributes.flag_modified`

    """
