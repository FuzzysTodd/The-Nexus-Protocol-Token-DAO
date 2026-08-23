from . import QueryableAttribute as QueryableAttribute, attributes as attributes, relationships as relationships
from .. import util as util
from ..engine import result as result
from ..event import _Dispatch
from ..sql.elements import ColumnElement as ColumnElement
from .base import PassiveFlag as PassiveFlag
from .mapper import Mapper as Mapper
from .query import Query as Query
from .relationships import _RelationshipOrderByArg
from .session import Session as Session, object_session as object_session
from .state import InstanceState as InstanceState
from .util import AliasedClass as AliasedClass
from .writeonly import AbstractCollectionWriter as AbstractCollectionWriter, WriteOnlyAttributeImpl as WriteOnlyAttributeImpl, WriteOnlyHistory as WriteOnlyHistory, WriteOnlyLoader as WriteOnlyLoader
from _typeshed import Incomplete
from typing import Any, Iterable, Iterator, List, Type

class DynamicCollectionHistory(WriteOnlyHistory[_T]):
    unchanged_items: Incomplete
    added_items: Incomplete
    deleted_items: Incomplete
    def __init__(self, attr: DynamicAttributeImpl, state: InstanceState[_T], passive: PassiveFlag, apply_to: DynamicCollectionHistory[_T] | None = None) -> None: ...

class DynamicAttributeImpl(WriteOnlyAttributeImpl):
    collection_history_cls = DynamicCollectionHistory[Any]
    query_class: Type[AppenderMixin[Any]]
    target_mapper: Incomplete
    order_by: Incomplete
    def __init__(self, class_: Type[Any] | AliasedClass[Any], key: str, dispatch: _Dispatch[QueryableAttribute[Any]], target_mapper: Mapper[_T], order_by: _RelationshipOrderByArg, query_class: Type[AppenderMixin[_T]] | None = None, **kw: Any) -> None: ...

class DynaLoader(WriteOnlyLoader):
    impl_class = DynamicAttributeImpl

class AppenderMixin(AbstractCollectionWriter[_T]):
    """A mixin that expects to be mixing in a Query class with
    AbstractAppender.


    """
    query_class: Type[Query[_T]] | None
    def __init__(self, attr: DynamicAttributeImpl, state: InstanceState[_T]) -> None: ...
    @property
    def session(self) -> Session | None: ...
    sess: Incomplete
    @session.setter
    def session(self, session: Session) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, index: Any) -> _T | List[_T]: ...
    def count(self) -> int: ...
    def add_all(self, iterator: Iterable[_T]) -> None:
        """Add an iterable of items to this :class:`_orm.AppenderQuery`.

        The given items will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        This method is provided to assist in delivering forwards-compatibility
        with the :class:`_orm.WriteOnlyCollection` collection class.

        .. versionadded:: 2.0

        """
    def add(self, item: _T) -> None:
        """Add an item to this :class:`_orm.AppenderQuery`.

        The given item will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        This method is provided to assist in delivering forwards-compatibility
        with the :class:`_orm.WriteOnlyCollection` collection class.

        .. versionadded:: 2.0

        """
    def extend(self, iterator: Iterable[_T]) -> None:
        """Add an iterable of items to this :class:`_orm.AppenderQuery`.

        The given items will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        """
    def append(self, item: _T) -> None:
        """Append an item to this :class:`_orm.AppenderQuery`.

        The given item will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        """
    def remove(self, item: _T) -> None:
        """Remove an item from this :class:`_orm.AppenderQuery`.

        The given item will be removed from the parent instance's collection on
        the next flush.

        """

class AppenderQuery(AppenderMixin[_T], Query[_T]):
    """A dynamic query that supports basic collection storage operations.

    Methods on :class:`.AppenderQuery` include all methods of
    :class:`_orm.Query`, plus additional methods used for collection
    persistence.


    """

def mixin_user_query(cls) -> type[AppenderMixin[Any]]:
    """Return a new class with AppenderQuery functionality layered over."""
