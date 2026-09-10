from ..engine.base import Connection, Engine, OptionEngine
from ..orm._typing import OrmExecuteOptionsParameter, _O
from ..orm.interfaces import ORMOption
from ..orm.mapper import Mapper
from ..orm.query import Query
from ..orm.session import ORMExecuteState, Session, _BindArguments, _EntityBindKey, _PKIdentityArgument, _SessionBind
from ..orm.state import InstanceState
from ..sql import Executable
from ..sql.elements import ClauseElement
from ..util.typing import Protocol, Self
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Iterable, Type

__all__ = ['ShardedSession', 'ShardedQuery']

ShardIdentifier = str

class ShardChooser(Protocol):
    def __call__(self, mapper: Mapper[_T] | None, instance: Any, clause: ClauseElement | None) -> Any: ...

class IdentityChooser(Protocol):
    def __call__(self, mapper: Mapper[_T], primary_key: _PKIdentityArgument, *, lazy_loaded_from: InstanceState[Any] | None, execution_options: OrmExecuteOptionsParameter, bind_arguments: _BindArguments, **kw: Any) -> Any: ...

class ShardedQuery(Query[_T]):
    """Query class used with :class:`.ShardedSession`.

    .. legacy:: The :class:`.ShardedQuery` is a subclass of the legacy
       :class:`.Query` class.   The :class:`.ShardedSession` now supports
       2.0 style execution via the :meth:`.ShardedSession.execute` method.

    """
    identity_chooser: Incomplete
    execute_chooser: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_shard(self, shard_id: ShardIdentifier) -> Self:
        '''Return a new query, limited to a single shard ID.

        All subsequent operations with the returned query will
        be against the single shard regardless of other state.

        The shard_id can be passed for a 2.0 style execution to the
        bind_arguments dictionary of :meth:`.Session.execute`::

            results = session.execute(
                stmt,
                bind_arguments={"shard_id": "my_shard"}
            )

        '''

class ShardedSession(Session):
    shard_chooser: ShardChooser
    identity_chooser: IdentityChooser
    execute_chooser: Callable[[ORMExecuteState], Iterable[Any]]
    def __init__(self, shard_chooser: ShardChooser, identity_chooser: IdentityChooser | None = None, execute_chooser: Callable[[ORMExecuteState], Iterable[Any]] | None = None, shards: Dict[str, Any] | None = None, query_cls: Type[Query[_T]] = ..., *, id_chooser: Callable[[Query[_T], Iterable[_T]], Iterable[Any]] | None = None, query_chooser: Callable[[Executable], Iterable[Any]] | None = None, **kwargs: Any) -> None:
        """Construct a ShardedSession.

        :param shard_chooser: A callable which, passed a Mapper, a mapped
          instance, and possibly a SQL clause, returns a shard ID.  This id
          may be based off of the attributes present within the object, or on
          some round-robin scheme. If the scheme is based on a selection, it
          should set whatever state on the instance to mark it in the future as
          participating in that shard.

        :param identity_chooser: A callable, passed a Mapper and primary key
         argument, which should return a list of shard ids where this
         primary key might reside.

          .. versionchanged:: 2.0  The ``identity_chooser`` parameter
             supersedes the ``id_chooser`` parameter.

        :param execute_chooser: For a given :class:`.ORMExecuteState`,
          returns the list of shard_ids
          where the query should be issued.  Results from all shards returned
          will be combined together into a single listing.

          .. versionchanged:: 1.4  The ``execute_chooser`` parameter
             supersedes the ``query_chooser`` parameter.

        :param shards: A dictionary of string shard names
          to :class:`~sqlalchemy.engine.Engine` objects.

        """
    def connection_callable(self, mapper: Mapper[_T] | None = None, instance: Any | None = None, shard_id: ShardIdentifier | None = None, **kw: Any) -> Connection:
        """Provide a :class:`_engine.Connection` to use in the unit of work
        flush process.

        """
    def get_bind(self, mapper: _EntityBindKey[_O] | None = None, *, shard_id: ShardIdentifier | None = None, instance: Any | None = None, clause: ClauseElement | None = None, **kw: Any) -> _SessionBind: ...
    def bind_shard(self, shard_id: ShardIdentifier, bind: Engine | OptionEngine) -> None: ...

class set_shard_id(ORMOption):
    '''a loader option for statements to apply a specific shard id to the
    primary query as well as for additional relationship and column
    loaders.

    The :class:`_horizontal.set_shard_id` option may be applied using
    the :meth:`_sql.Executable.options` method of any executable statement::

        stmt = (
            select(MyObject).
            where(MyObject.name == \'some name\').
            options(set_shard_id("shard1"))
        )

    Above, the statement when invoked will limit to the "shard1" shard
    identifier for the primary query as well as for all relationship and
    column loading strategies, including eager loaders such as
    :func:`_orm.selectinload`, deferred column loaders like :func:`_orm.defer`,
    and the lazy relationship loader :func:`_orm.lazyload`.

    In this way, the :class:`_horizontal.set_shard_id` option has much wider
    scope than using the "shard_id" argument within the
    :paramref:`_orm.Session.execute.bind_arguments` dictionary.


    .. versionadded:: 2.0.0

    '''
    shard_id: Incomplete
    propagate_to_loaders: Incomplete
    def __init__(self, shard_id: ShardIdentifier, propagate_to_loaders: bool = True) -> None:
        """Construct a :class:`_horizontal.set_shard_id` option.

        :param shard_id: shard identifier
        :param propagate_to_loaders: if left at its default of ``True``, the
         shard option will take place for lazy loaders such as
         :func:`_orm.lazyload` and :func:`_orm.defer`; if False, the option
         will not be propagated to loaded objects. Note that :func:`_orm.defer`
         always limits to the shard_id of the parent row in any case, so the
         parameter only has a net effect on the behavior of the
         :func:`_orm.lazyload` strategy.

        """
