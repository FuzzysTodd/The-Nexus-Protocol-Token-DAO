import weakref
from . import base as base, interfaces as interfaces
from .. import inspection as inspection, util as util
from ..engine import Row as Row
from ..ext.asyncio.session import AsyncSession as AsyncSession
from ..util.typing import Literal as Literal, Protocol as Protocol
from ._typing import _IdentityKeyType, _InstanceDict, _O, is_collection_impl as is_collection_impl
from .attributes import AttributeImpl as AttributeImpl, History as History
from .base import ATTR_WAS_SET as ATTR_WAS_SET, INIT_OK as INIT_OK, LoaderCallableStatus as LoaderCallableStatus, NEVER_SET as NEVER_SET, NO_VALUE as NO_VALUE, PASSIVE_NO_INITIALIZE as PASSIVE_NO_INITIALIZE, PASSIVE_NO_RESULT as PASSIVE_NO_RESULT, PASSIVE_OFF as PASSIVE_OFF, PassiveFlag as PassiveFlag, SQL_OK as SQL_OK
from .identity import IdentityMap as IdentityMap
from .instrumentation import ClassManager as ClassManager
from .interfaces import ORMOption as ORMOption
from .mapper import Mapper as Mapper
from .path_registry import PathRegistry as PathRegistry
from .session import Session as Session
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Generic, Iterable, Set, Tuple

class _InstanceDictProto(Protocol):
    def __call__(self) -> IdentityMap | None: ...

class _InstallLoaderCallableProto(Protocol[_O]):
    """used at result loading time to install a _LoaderCallable callable
    upon a specific InstanceState, which will be used to populate an
    attribute when that attribute is accessed.

    Concrete examples are per-instance deferred column loaders and
    relationship lazy loaders.

    """
    def __call__(self, state: InstanceState[_O], dict_: _InstanceDict, row: Row[Any]) -> None: ...

class InstanceState(interfaces.InspectionAttrInfo, Generic[_O]):
    """tracks state information at the instance level.

    The :class:`.InstanceState` is a key object used by the
    SQLAlchemy ORM in order to track the state of an object;
    it is created the moment an object is instantiated, typically
    as a result of :term:`instrumentation` which SQLAlchemy applies
    to the ``__init__()`` method of the class.

    :class:`.InstanceState` is also a semi-public object,
    available for runtime inspection as to the state of a
    mapped instance, including information such as its current
    status within a particular :class:`.Session` and details
    about data on individual attributes.  The public API
    in order to acquire a :class:`.InstanceState` object
    is to use the :func:`_sa.inspect` system::

        >>> from sqlalchemy import inspect
        >>> insp = inspect(some_mapped_object)
        >>> insp.attrs.nickname.history
        History(added=['new nickname'], unchanged=(), deleted=['nickname'])

    .. seealso::

        :ref:`orm_mapper_inspection_instancestate`

    """
    manager: ClassManager[_O]
    session_id: int | None
    key: _IdentityKeyType[_O] | None
    runid: int | None
    load_options: Tuple[ORMOption, ...]
    load_path: PathRegistry
    insert_order: int | None
    obj: weakref.ref[_O]
    committed_state: Dict[str, Any]
    modified: bool
    expired: bool
    is_instance: bool
    identity_token: object
    expired_attributes: Set[str]
    callables: Dict[str, Callable[[InstanceState[_O], PassiveFlag], Any]]
    class_: Incomplete
    def __init__(self, obj: _O, manager: ClassManager[_O]) -> None: ...
    def attrs(self) -> util.ReadOnlyProperties[AttributeState]:
        """Return a namespace representing each attribute on
        the mapped object, including its current value
        and history.

        The returned object is an instance of :class:`.AttributeState`.
        This object allows inspection of the current data
        within an attribute as well as attribute history
        since the last flush.

        """
    @property
    def transient(self) -> bool:
        """Return ``True`` if the object is :term:`transient`.

        .. seealso::

            :ref:`session_object_states`

        """
    @property
    def pending(self) -> bool:
        """Return ``True`` if the object is :term:`pending`.


        .. seealso::

            :ref:`session_object_states`

        """
    @property
    def deleted(self) -> bool:
        '''Return ``True`` if the object is :term:`deleted`.

        An object that is in the deleted state is guaranteed to
        not be within the :attr:`.Session.identity_map` of its parent
        :class:`.Session`; however if the session\'s transaction is rolled
        back, the object will be restored to the persistent state and
        the identity map.

        .. note::

            The :attr:`.InstanceState.deleted` attribute refers to a specific
            state of the object that occurs between the "persistent" and
            "detached" states; once the object is :term:`detached`, the
            :attr:`.InstanceState.deleted` attribute **no longer returns
            True**; in order to detect that a state was deleted, regardless
            of whether or not the object is associated with a
            :class:`.Session`, use the :attr:`.InstanceState.was_deleted`
            accessor.

        .. versionadded: 1.1

        .. seealso::

            :ref:`session_object_states`

        '''
    @property
    def was_deleted(self) -> bool:
        '''Return True if this object is or was previously in the
        "deleted" state and has not been reverted to persistent.

        This flag returns True once the object was deleted in flush.
        When the object is expunged from the session either explicitly
        or via transaction commit and enters the "detached" state,
        this flag will continue to report True.

        .. seealso::

            :attr:`.InstanceState.deleted` - refers to the "deleted" state

            :func:`.orm.util.was_deleted` - standalone function

            :ref:`session_object_states`

        '''
    @property
    def persistent(self) -> bool:
        """Return ``True`` if the object is :term:`persistent`.

        An object that is in the persistent state is guaranteed to
        be within the :attr:`.Session.identity_map` of its parent
        :class:`.Session`.

        .. seealso::

            :ref:`session_object_states`

        """
    @property
    def detached(self) -> bool:
        """Return ``True`` if the object is :term:`detached`.

        .. seealso::

            :ref:`session_object_states`

        """
    @property
    def session(self) -> Session | None:
        """Return the owning :class:`.Session` for this instance,
        or ``None`` if none available.

        Note that the result here can in some cases be *different*
        from that of ``obj in session``; an object that's been deleted
        will report as not ``in session``, however if the transaction is
        still in progress, this attribute will still refer to that session.
        Only when the transaction is completed does the object become
        fully detached under normal circumstances.

        .. seealso::

            :attr:`_orm.InstanceState.async_session`

        """
    @property
    def async_session(self) -> AsyncSession | None:
        """Return the owning :class:`_asyncio.AsyncSession` for this instance,
        or ``None`` if none available.

        This attribute is only non-None when the :mod:`sqlalchemy.ext.asyncio`
        API is in use for this ORM object. The returned
        :class:`_asyncio.AsyncSession` object will be a proxy for the
        :class:`_orm.Session` object that would be returned from the
        :attr:`_orm.InstanceState.session` attribute for this
        :class:`_orm.InstanceState`.

        .. versionadded:: 1.4.18

        .. seealso::

            :ref:`asyncio_toplevel`

        """
    @property
    def object(self) -> _O | None:
        """Return the mapped object represented by this
        :class:`.InstanceState`.

        Returns None if the object has been garbage collected

        """
    @property
    def identity(self) -> Tuple[Any, ...] | None:
        """Return the mapped identity of the mapped object.
        This is the primary key identity as persisted by the ORM
        which can always be passed directly to
        :meth:`_query.Query.get`.

        Returns ``None`` if the object has no primary key identity.

        .. note::
            An object which is :term:`transient` or :term:`pending`
            does **not** have a mapped identity until it is flushed,
            even if its attributes include primary key values.

        """
    @property
    def identity_key(self) -> _IdentityKeyType[_O] | None:
        """Return the identity key for the mapped object.

        This is the key used to locate the object within
        the :attr:`.Session.identity_map` mapping.   It contains
        the identity as returned by :attr:`.identity` within it.


        """
    def parents(self) -> Dict[int, Literal[False] | InstanceState[Any]]: ...
    def mapper(self) -> Mapper[_O]:
        """Return the :class:`_orm.Mapper` used for this mapped object."""
    @property
    def has_identity(self) -> bool:
        """Return ``True`` if this object has an identity key.

        This should always have the same value as the
        expression ``state.persistent`` or ``state.detached``.

        """
    @property
    def dict(self) -> _InstanceDict:
        """Return the instance dict used by the object.

        Under normal circumstances, this is always synonymous
        with the ``__dict__`` attribute of the mapped object,
        unless an alternative instrumentation system has been
        configured.

        In the case that the actual object has been garbage
        collected, this accessor returns a blank dictionary.

        """
    def get_history(self, key: str, passive: PassiveFlag) -> History: ...
    def get_impl(self, key: str) -> AttributeImpl: ...
    @property
    def unmodified(self) -> Set[str]:
        """Return the set of keys which have no uncommitted changes"""
    def unmodified_intersection(self, keys: Iterable[str]) -> Set[str]:
        """Return self.unmodified.intersection(keys)."""
    @property
    def unloaded(self) -> Set[str]:
        """Return the set of keys which do not have a loaded value.

        This includes expired attributes and any other attribute that was never
        populated or modified.

        """
    @property
    def unloaded_expirable(self) -> Set[str]:
        """Synonymous with :attr:`.InstanceState.unloaded`.

        This attribute was added as an implementation-specific detail at some
        point and should be considered to be private.

        """

class AttributeState:
    """Provide an inspection interface corresponding
    to a particular attribute on a particular mapped object.

    The :class:`.AttributeState` object is accessed
    via the :attr:`.InstanceState.attrs` collection
    of a particular :class:`.InstanceState`::

        from sqlalchemy import inspect

        insp = inspect(some_mapped_object)
        attr_state = insp.attrs.some_attribute

    """
    state: InstanceState[Any]
    key: str
    def __init__(self, state: InstanceState[Any], key: str) -> None: ...
    @property
    def loaded_value(self) -> Any:
        """The current value of this attribute as loaded from the database.

        If the value has not been loaded, or is otherwise not present
        in the object's dictionary, returns NO_VALUE.

        """
    @property
    def value(self) -> Any:
        """Return the value of this attribute.

        This operation is equivalent to accessing the object's
        attribute directly or via ``getattr()``, and will fire
        off any pending loader callables if needed.

        """
    @property
    def history(self) -> History:
        """Return the current **pre-flush** change history for
        this attribute, via the :class:`.History` interface.

        This method will **not** emit loader callables if the value of the
        attribute is unloaded.

        .. note::

            The attribute history system tracks changes on a **per flush
            basis**. Each time the :class:`.Session` is flushed, the history
            of each attribute is reset to empty.   The :class:`.Session` by
            default autoflushes each time a :class:`_query.Query` is invoked.
            For
            options on how to control this, see :ref:`session_flushing`.


        .. seealso::

            :meth:`.AttributeState.load_history` - retrieve history
            using loader callables if the value is not locally present.

            :func:`.attributes.get_history` - underlying function

        """
    def load_history(self) -> History:
        """Return the current **pre-flush** change history for
        this attribute, via the :class:`.History` interface.

        This method **will** emit loader callables if the value of the
        attribute is unloaded.

        .. note::

            The attribute history system tracks changes on a **per flush
            basis**. Each time the :class:`.Session` is flushed, the history
            of each attribute is reset to empty.   The :class:`.Session` by
            default autoflushes each time a :class:`_query.Query` is invoked.
            For
            options on how to control this, see :ref:`session_flushing`.

        .. seealso::

            :attr:`.AttributeState.history`

            :func:`.attributes.get_history` - underlying function

        """

class PendingCollection:
    """A writable placeholder for an unloaded collection.

    Stores items appended to and removed from a collection that has not yet
    been loaded. When the collection is loaded, the changes stored in
    PendingCollection are applied to it to produce the final result.

    """
    deleted_items: util.IdentitySet
    added_items: util.OrderedIdentitySet
    def __init__(self) -> None: ...
    def merge_with_history(self, history: History) -> History: ...
    def append(self, value: Any) -> None: ...
    def remove(self, value: Any) -> None: ...
