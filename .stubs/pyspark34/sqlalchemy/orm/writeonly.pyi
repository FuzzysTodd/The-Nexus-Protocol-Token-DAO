from . import QueryableAttribute as QueryableAttribute, attributes as attributes, interfaces as interfaces, relationships as relationships, strategies as strategies
from .. import exc as exc, inspect as inspect, log as log, util as util
from ..event import _Dispatch
from ..sql import delete as delete, insert as insert, select as select, update as update
from ..sql.dml import Delete as Delete, Insert as Insert, Update as Update
from ..sql.selectable import FromClause as FromClause, Select as Select
from ..util.typing import Literal as Literal
from ._typing import _InstanceDict
from .attributes import AttributeEventToken as AttributeEventToken
from .base import LoaderCallableStatus as LoaderCallableStatus, NEVER_SET as NEVER_SET, PassiveFlag as PassiveFlag, RelationshipDirection as RelationshipDirection, object_mapper as object_mapper
from .collections import CollectionAdapter as CollectionAdapter, _AdaptedCollectionProtocol
from .mapper import Mapper as Mapper
from .relationships import _RelationshipOrderByArg
from .state import InstanceState as InstanceState
from .util import AliasedClass as AliasedClass
from _typeshed import Incomplete
from sqlalchemy.sql import bindparam as bindparam
from typing import Any, Collection, Generic, Iterable, Iterator, List, NoReturn, Tuple, Type, overload

class WriteOnlyHistory(Generic[_T]):
    """Overrides AttributeHistory to receive append/remove events directly."""
    unchanged_items: util.OrderedIdentitySet
    added_items: util.OrderedIdentitySet
    deleted_items: util.OrderedIdentitySet
    def __init__(self, attr: WriteOnlyAttributeImpl, state: InstanceState[_T], passive: PassiveFlag, apply_to: WriteOnlyHistory[_T] | None = None) -> None: ...
    @property
    def added_plus_unchanged(self) -> List[_T]: ...
    @property
    def all_items(self) -> List[_T]: ...
    def as_history(self) -> attributes.History: ...
    def indexed(self, index: int | slice) -> List[_T] | _T: ...
    def add_added(self, value: _T) -> None: ...
    def add_removed(self, value: _T) -> None: ...

class WriteOnlyAttributeImpl(attributes.HasCollectionAdapter, attributes.AttributeImpl):
    uses_objects: bool
    default_accepts_scalar_loader: bool
    supports_population: bool
    collection: bool
    dynamic: bool
    order_by: _RelationshipOrderByArg
    collection_history_cls: Type[WriteOnlyHistory[Any]]
    query_class: Type[WriteOnlyCollection[Any]]
    target_mapper: Incomplete
    def __init__(self, class_: Type[Any] | AliasedClass[Any], key: str, dispatch: _Dispatch[QueryableAttribute[Any]], target_mapper: Mapper[_T], order_by: _RelationshipOrderByArg, **kw: Any) -> None: ...
    def get(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> util.OrderedIdentitySet | WriteOnlyCollection[Any]: ...
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: Literal[None] = ..., passive: Literal[PassiveFlag.PASSIVE_OFF] = ...) -> CollectionAdapter: ...
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: _AdaptedCollectionProtocol = ..., passive: PassiveFlag = ...) -> CollectionAdapter: ...
    @overload
    def get_collection(self, state: InstanceState[Any], dict_: _InstanceDict, user_data: _AdaptedCollectionProtocol | None = ..., passive: PassiveFlag = ...) -> Literal[LoaderCallableStatus.PASSIVE_NO_RESULT] | CollectionAdapter: ...
    def fire_append_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, collection_history: WriteOnlyHistory[Any] | None = None) -> None: ...
    def fire_remove_event(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, collection_history: WriteOnlyHistory[Any] | None = None) -> None: ...
    def set(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None = None, passive: PassiveFlag = ..., check_old: Any = None, pop: bool = False, _adapt: bool = True) -> None: ...
    def delete(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def set_committed_value(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any) -> NoReturn: ...
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> attributes.History: ...
    def get_all_pending(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> List[Tuple[InstanceState[Any], Any]]: ...
    def append(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def remove(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...
    def pop(self, state: InstanceState[Any], dict_: _InstanceDict, value: Any, initiator: AttributeEventToken | None, passive: PassiveFlag = ...) -> None: ...

class WriteOnlyLoader(strategies.AbstractRelationshipLoader, log.Identified):
    impl_class = WriteOnlyAttributeImpl
    is_class_level: bool
    def init_class_attribute(self, mapper: Mapper[Any]) -> None: ...

class DynamicCollectionAdapter:
    """simplified CollectionAdapter for internal API consistency"""
    data: Collection[Any]
    def __init__(self, data: Collection[Any]) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...

class AbstractCollectionWriter(Generic[_T]):
    """Virtual collection which includes append/remove methods that synchronize
    into the attribute event system.

    """
    instance: _T
    attr: Incomplete
    def __init__(self, attr: WriteOnlyAttributeImpl, state: InstanceState[_T]) -> None: ...

class WriteOnlyCollection(AbstractCollectionWriter[_T]):
    '''Write-only collection which can synchronize changes into the
    attribute event system.

    The :class:`.WriteOnlyCollection` is used in a mapping by
    using the ``"write_only"`` lazy loading strategy with
    :func:`_orm.relationship`.     For background on this configuration,
    see :ref:`write_only_relationship`.

    .. versionadded:: 2.0

    .. seealso::

        :ref:`write_only_relationship`

    '''
    def __iter__(self) -> NoReturn: ...
    def select(self) -> Select[Tuple[_T]]:
        """Produce a :class:`_sql.Select` construct that represents the
        rows within this instance-local :class:`_orm.WriteOnlyCollection`.

        """
    def insert(self) -> Insert:
        """For one-to-many collections, produce a :class:`_dml.Insert` which
        will insert new rows in terms of this this instance-local
        :class:`_orm.WriteOnlyCollection`.

        This construct is only supported for a :class:`_orm.Relationship`
        that does **not** include the :paramref:`_orm.relationship.secondary`
        parameter.  For relationships that refer to a many-to-many table,
        use ordinary bulk insert techniques to produce new objects, then
        use :meth:`_orm.AbstractCollectionWriter.add_all` to associate them
        with the collection.


        """
    def update(self) -> Update:
        """Produce a :class:`_dml.Update` which will refer to rows in terms
        of this instance-local :class:`_orm.WriteOnlyCollection`.

        """
    def delete(self) -> Delete:
        """Produce a :class:`_dml.Delete` which will refer to rows in terms
        of this instance-local :class:`_orm.WriteOnlyCollection`.

        """
    def add_all(self, iterator: Iterable[_T]) -> None:
        """Add an iterable of items to this :class:`_orm.WriteOnlyCollection`.

        The given items will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        """
    def add(self, item: _T) -> None:
        """Add an item to this :class:`_orm.WriteOnlyCollection`.

        The given item will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        """
    def remove(self, item: _T) -> None:
        """Remove an item from this :class:`_orm.WriteOnlyCollection`.

        The given item will be removed from the parent instance's collection on
        the next flush.

        """
