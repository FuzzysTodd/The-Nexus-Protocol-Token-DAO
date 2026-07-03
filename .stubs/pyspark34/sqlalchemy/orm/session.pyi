import contextlib
from . import bulk_persistence, context
from .. import util
from ..engine import Connection, CursorResult, Engine, Result, Row, RowMapping
from ..engine.interfaces import CoreExecuteOptionsParameter, _CoreAnyExecuteParams, _CoreSingleExecuteParams, _ExecuteOptions
from ..engine.result import ScalarResult
from ..engine.util import TransactionalContext
from ..event import EventTarget, _InstanceLevelDispatch, dispatcher
from ..sql import TableClause
from ..sql._typing import _ColumnsClauseArgument, _InfoType, _T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _TypedColumnClauseArgument as _TCCA
from ..sql.base import Executable, _NoArg
from ..sql.dml import UpdateBase
from ..sql.elements import ClauseElement
from ..sql.roles import TypedColumnsClauseRole
from ..sql.selectable import ForUpdateParameter, TypedReturnsRows
from ..util import IdentitySet
from ..util.typing import Literal, Protocol
from ._typing import OrmExecuteOptionsParameter, _EntityType, _IdentityKeyType, _O
from .context import ORMCompileState
from .identity import IdentityMap
from .interfaces import ORMOption, UserDefinedOption
from .mapper import Mapper
from .path_registry import PathRegistry
from .query import Query, RowReturningQuery
from .state import InstanceState
from .state_changes import _StateChange, _StateChangeState
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Dict, Generic, Iterable, Iterator, List, Sequence, Tuple, Type, overload

__all__ = ['Session', 'SessionTransaction', 'sessionmaker', 'ORMExecuteState', 'close_all_sessions', 'make_transient', 'make_transient_to_detached', 'object_session']

class _ConnectionCallableProto(Protocol):
    """a callable that returns a :class:`.Connection` given an instance.

    This callable, when present on a :class:`.Session`, is called only from the
    ORM's persistence mechanism (i.e. the unit of work flush process) to allow
    for connection-per-instance schemes (i.e. horizontal sharding) to be used
    as persistence time.

    This callable is not present on a plain :class:`.Session`, however
    is established when using the horizontal sharding extension.

    """
    def __call__(self, mapper: Mapper[Any] | None = None, instance: object | None = None, **kw: Any) -> Connection: ...

class _SessionClassMethods:
    """Class-level methods for :class:`.Session`, :class:`.sessionmaker`."""
    @classmethod
    def close_all(cls) -> None:
        """Close *all* sessions in memory."""
    @classmethod
    def identity_key(cls, class_: Type[Any] | None = None, ident: Any | Tuple[Any, ...] = None, *, instance: Any | None = None, row: Row[Any] | RowMapping | None = None, identity_token: Any | None = None) -> _IdentityKeyType[Any]:
        """Return an identity key.

        This is an alias of :func:`.util.identity_key`.

        """
    @classmethod
    def object_session(cls, instance: object) -> Session | None:
        """Return the :class:`.Session` to which an object belongs.

        This is an alias of :func:`.object_session`.

        """

class SessionTransactionState(_StateChangeState):
    ACTIVE: int
    PREPARED: int
    COMMITTED: int
    DEACTIVE: int
    CLOSED: int
    PROVISIONING_CONNECTION: int

class ORMExecuteState(util.MemoizedSlots):
    """Represents a call to the :meth:`_orm.Session.execute` method, as passed
    to the :meth:`.SessionEvents.do_orm_execute` event hook.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`session_execute_events` - top level documentation on how
        to use :meth:`_orm.SessionEvents.do_orm_execute`

    """
    session: Session
    statement: Executable
    parameters: _CoreAnyExecuteParams | None
    execution_options: _ExecuteOptions
    local_execution_options: _ExecuteOptions
    bind_arguments: _BindArguments
    def __init__(self, session: Session, statement: Executable, parameters: _CoreAnyExecuteParams | None, execution_options: _ExecuteOptions, bind_arguments: _BindArguments, compile_state_cls: Type[ORMCompileState] | None, events_todo: List[_InstanceLevelDispatch[Session]]) -> None:
        """Construct a new :class:`_orm.ORMExecuteState`.

        this object is constructed internally.

        """
    def invoke_statement(self, statement: Executable | None = None, params: _CoreAnyExecuteParams | None = None, execution_options: OrmExecuteOptionsParameter | None = None, bind_arguments: _BindArguments | None = None) -> Result[Any]:
        """Execute the statement represented by this
        :class:`.ORMExecuteState`, without re-invoking events that have
        already proceeded.

        This method essentially performs a re-entrant execution of the current
        statement for which the :meth:`.SessionEvents.do_orm_execute` event is
        being currently invoked.    The use case for this is for event handlers
        that want to override how the ultimate
        :class:`_engine.Result` object is returned, such as for schemes that
        retrieve results from an offline cache or which concatenate results
        from multiple executions.

        When the :class:`_engine.Result` object is returned by the actual
        handler function within :meth:`_orm.SessionEvents.do_orm_execute` and
        is propagated to the calling
        :meth:`_orm.Session.execute` method, the remainder of the
        :meth:`_orm.Session.execute` method is preempted and the
        :class:`_engine.Result` object is returned to the caller of
        :meth:`_orm.Session.execute` immediately.

        :param statement: optional statement to be invoked, in place of the
         statement currently represented by :attr:`.ORMExecuteState.statement`.

        :param params: optional dictionary of parameters or list of parameters
         which will be merged into the existing
         :attr:`.ORMExecuteState.parameters` of this :class:`.ORMExecuteState`.

         .. versionchanged:: 2.0 a list of parameter dictionaries is accepted
            for executemany executions.

        :param execution_options: optional dictionary of execution options
         will be merged into the existing
         :attr:`.ORMExecuteState.execution_options` of this
         :class:`.ORMExecuteState`.

        :param bind_arguments: optional dictionary of bind_arguments
         which will be merged amongst the current
         :attr:`.ORMExecuteState.bind_arguments`
         of this :class:`.ORMExecuteState`.

        :return: a :class:`_engine.Result` object with ORM-level results.

        .. seealso::

            :ref:`do_orm_execute_re_executing` - background and examples on the
            appropriate usage of :meth:`_orm.ORMExecuteState.invoke_statement`.


        """
    @property
    def bind_mapper(self) -> Mapper[Any] | None:
        '''Return the :class:`_orm.Mapper` that is the primary "bind" mapper.

        For an :class:`_orm.ORMExecuteState` object invoking an ORM
        statement, that is, the :attr:`_orm.ORMExecuteState.is_orm_statement`
        attribute is ``True``, this attribute will return the
        :class:`_orm.Mapper` that is considered to be the "primary" mapper
        of the statement.   The term "bind mapper" refers to the fact that
        a :class:`_orm.Session` object may be "bound" to multiple
        :class:`_engine.Engine` objects keyed to mapped classes, and the
        "bind mapper" determines which of those :class:`_engine.Engine` objects
        would be selected.

        For a statement that is invoked against a single mapped class,
        :attr:`_orm.ORMExecuteState.bind_mapper` is intended to be a reliable
        way of getting this mapper.

        .. versionadded:: 1.4.0b2

        .. seealso::

            :attr:`_orm.ORMExecuteState.all_mappers`


        '''
    @property
    def all_mappers(self) -> Sequence[Mapper[Any]]:
        '''Return a sequence of all :class:`_orm.Mapper` objects that are
        involved at the top level of this statement.

        By "top level" we mean those :class:`_orm.Mapper` objects that would
        be represented in the result set rows for a :func:`_sql.select`
        query, or for a :func:`_dml.update` or :func:`_dml.delete` query,
        the mapper that is the main subject of the UPDATE or DELETE.

        .. versionadded:: 1.4.0b2

        .. seealso::

            :attr:`_orm.ORMExecuteState.bind_mapper`



        '''
    @property
    def is_orm_statement(self) -> bool:
        """return True if the operation is an ORM statement.

        This indicates that the select(), insert(), update(), or delete()
        being invoked contains ORM entities as subjects.   For a statement
        that does not have ORM entities and instead refers only to
        :class:`.Table` metadata, it is invoked as a Core SQL statement
        and no ORM-level automation takes place.

        """
    @property
    def is_executemany(self) -> bool:
        """return True if the parameters are a multi-element list of
        dictionaries with more than one dictionary.

        .. versionadded:: 2.0

        """
    @property
    def is_select(self) -> bool:
        """return True if this is a SELECT operation."""
    @property
    def is_insert(self) -> bool:
        """return True if this is an INSERT operation."""
    @property
    def is_update(self) -> bool:
        """return True if this is an UPDATE operation."""
    @property
    def is_delete(self) -> bool:
        """return True if this is a DELETE operation."""
    def update_execution_options(self, **opts: Any) -> None:
        """Update the local execution options with new values."""
    @property
    def lazy_loaded_from(self) -> InstanceState[Any] | None:
        """An :class:`.InstanceState` that is using this statement execution
        for a lazy load operation.

        The primary rationale for this attribute is to support the horizontal
        sharding extension, where it is available within specific query
        execution time hooks created by this extension.   To that end, the
        attribute is only intended to be meaningful at **query execution
        time**, and importantly not any time prior to that, including query
        compilation time.

        """
    @property
    def loader_strategy_path(self) -> PathRegistry | None:
        '''Return the :class:`.PathRegistry` for the current load path.

        This object represents the "path" in a query along relationships
        when a particular object or collection is being loaded.

        '''
    @property
    def is_column_load(self) -> bool:
        """Return True if the operation is refreshing column-oriented
        attributes on an existing ORM object.

        This occurs during operations such as :meth:`_orm.Session.refresh`,
        as well as when an attribute deferred by :func:`_orm.defer` is
        being loaded, or an attribute that was expired either directly
        by :meth:`_orm.Session.expire` or via a commit operation is being
        loaded.

        Handlers will very likely not want to add any options to queries
        when such an operation is occurring as the query should be a straight
        primary key fetch which should not have any additional WHERE criteria,
        and loader options travelling with the instance
        will have already been added to the query.

        .. versionadded:: 1.4.0b2

        .. seealso::

            :attr:`_orm.ORMExecuteState.is_relationship_load`

        """
    @property
    def is_relationship_load(self) -> bool:
        """Return True if this load is loading objects on behalf of a
        relationship.

        This means, the loader in effect is either a LazyLoader,
        SelectInLoader, SubqueryLoader, or similar, and the entire
        SELECT statement being emitted is on behalf of a relationship
        load.

        Handlers will very likely not want to add any options to queries
        when such an operation is occurring, as loader options are already
        capable of being propagated to relationship loaders and should
        be already present.

        .. seealso::

            :attr:`_orm.ORMExecuteState.is_column_load`

        """
    @property
    def load_options(self) -> context.QueryContext.default_load_options | Type[context.QueryContext.default_load_options]:
        """Return the load_options that will be used for this execution."""
    @property
    def update_delete_options(self) -> bulk_persistence.BulkUDCompileState.default_update_options | Type[bulk_persistence.BulkUDCompileState.default_update_options]:
        """Return the update_delete_options that will be used for this
        execution."""
    @property
    def user_defined_options(self) -> Sequence[UserDefinedOption]:
        """The sequence of :class:`.UserDefinedOptions` that have been
        associated with the statement being invoked.

        """

class SessionTransactionOrigin(Enum):
    """indicates the origin of a :class:`.SessionTransaction`.

    This enumeration is present on the
    :attr:`.SessionTransaction.origin` attribute of any
    :class:`.SessionTransaction` object.

    .. versionadded:: 2.0

    """
    AUTOBEGIN: int
    BEGIN: int
    BEGIN_NESTED: int
    SUBTRANSACTION: int

class SessionTransaction(_StateChange, TransactionalContext):
    """A :class:`.Session`-level transaction.

    :class:`.SessionTransaction` is produced from the
    :meth:`_orm.Session.begin`
    and :meth:`_orm.Session.begin_nested` methods.   It's largely an internal
    object that in modern use provides a context manager for session
    transactions.

    Documentation on interacting with :class:`_orm.SessionTransaction` is
    at: :ref:`unitofwork_transaction`.


    .. versionchanged:: 1.4  The scoping and API methods to work with the
       :class:`_orm.SessionTransaction` object directly have been simplified.

    .. seealso::

        :ref:`unitofwork_transaction`

        :meth:`.Session.begin`

        :meth:`.Session.begin_nested`

        :meth:`.Session.rollback`

        :meth:`.Session.commit`

        :meth:`.Session.in_transaction`

        :meth:`.Session.in_nested_transaction`

        :meth:`.Session.get_transaction`

        :meth:`.Session.get_nested_transaction`


    """
    session: Session
    origin: SessionTransactionOrigin
    nested: bool
    def __init__(self, session: Session, origin: SessionTransactionOrigin, parent: SessionTransaction | None = None) -> None: ...
    @property
    def parent(self) -> SessionTransaction | None:
        '''The parent :class:`.SessionTransaction` of this
        :class:`.SessionTransaction`.

        If this attribute is ``None``, indicates this
        :class:`.SessionTransaction` is at the top of the stack, and
        corresponds to a real "COMMIT"/"ROLLBACK"
        block.  If non-``None``, then this is either a "subtransaction"
        (an internal marker object used by the flush process) or a
        "nested" / SAVEPOINT transaction.  If the
        :attr:`.SessionTransaction.nested` attribute is ``True``, then
        this is a SAVEPOINT, and if ``False``, indicates this a subtransaction.

        '''
    @property
    def is_active(self) -> bool: ...
    def connection(self, bindkey: Mapper[Any] | None, execution_options: _ExecuteOptions | None = None, **kwargs: Any) -> Connection: ...
    def prepare(self) -> None: ...
    def commit(self, _to_root: bool = False) -> None: ...
    def rollback(self, _capture_exception: bool = False, _to_root: bool = False) -> None: ...
    def close(self, invalidate: bool = False) -> None: ...

class _SessionCloseState(Enum):
    ACTIVE: int
    CLOSED: int
    CLOSE_IS_RESET: int

class Session(_SessionClassMethods, EventTarget):
    """Manages persistence operations for ORM-mapped objects.

    The :class:`_orm.Session` is **not safe for use in concurrent threads.**.
    See :ref:`session_faq_threadsafe` for background.

    The Session's usage paradigm is described at :doc:`/orm/session`.


    """
    dispatch: dispatcher[Session]
    identity_map: IdentityMap
    bind: Engine | Connection | None
    hash_key: int
    autoflush: bool
    expire_on_commit: bool
    enable_baked_queries: bool
    twophase: bool
    join_transaction_mode: JoinTransactionMode
    autobegin: Incomplete
    def __init__(self, bind: _SessionBind | None = None, *, autoflush: bool = True, future: Literal[True] = True, expire_on_commit: bool = True, autobegin: bool = True, twophase: bool = False, binds: Dict[_SessionBindKey, _SessionBind] | None = None, enable_baked_queries: bool = True, info: _InfoType | None = None, query_cls: Type[Query[Any]] | None = None, autocommit: Literal[False] = False, join_transaction_mode: JoinTransactionMode = 'conditional_savepoint', close_resets_only: bool | _NoArg = ...) -> None:
        '''Construct a new :class:`_orm.Session`.

        See also the :class:`.sessionmaker` function which is used to
        generate a :class:`.Session`-producing callable with a given
        set of arguments.

        :param autoflush: When ``True``, all query operations will issue a
           :meth:`~.Session.flush` call to this ``Session`` before proceeding.
           This is a convenience feature so that :meth:`~.Session.flush` need
           not be called repeatedly in order for database queries to retrieve
           results.

           .. seealso::

               :ref:`session_flushing` - additional background on autoflush

        :param autobegin: Automatically start transactions (i.e. equivalent to
           invoking :meth:`_orm.Session.begin`) when database access is
           requested by an operation.   Defaults to ``True``.    Set to
           ``False`` to prevent a :class:`_orm.Session` from implicitly
           beginning transactions after construction, as well as after any of
           the :meth:`_orm.Session.rollback`, :meth:`_orm.Session.commit`,
           or :meth:`_orm.Session.close` methods are called.

           .. versionadded:: 2.0

           .. seealso::

                :ref:`session_autobegin_disable`

        :param bind: An optional :class:`_engine.Engine` or
           :class:`_engine.Connection` to
           which this ``Session`` should be bound. When specified, all SQL
           operations performed by this session will execute via this
           connectable.

        :param binds: A dictionary which may specify any number of
           :class:`_engine.Engine` or :class:`_engine.Connection`
           objects as the source of
           connectivity for SQL operations on a per-entity basis.   The keys
           of the dictionary consist of any series of mapped classes,
           arbitrary Python classes that are bases for mapped classes,
           :class:`_schema.Table` objects and :class:`_orm.Mapper` objects.
           The
           values of the dictionary are then instances of
           :class:`_engine.Engine`
           or less commonly :class:`_engine.Connection` objects.
           Operations which
           proceed relative to a particular mapped class will consult this
           dictionary for the closest matching entity in order to determine
           which :class:`_engine.Engine` should be used for a particular SQL
           operation.    The complete heuristics for resolution are
           described at :meth:`.Session.get_bind`.  Usage looks like::

            Session = sessionmaker(binds={
                SomeMappedClass: create_engine(\'postgresql+psycopg2://engine1\'),
                SomeDeclarativeBase: create_engine(\'postgresql+psycopg2://engine2\'),
                some_mapper: create_engine(\'postgresql+psycopg2://engine3\'),
                some_table: create_engine(\'postgresql+psycopg2://engine4\'),
                })

           .. seealso::

                :ref:`session_partitioning`

                :meth:`.Session.bind_mapper`

                :meth:`.Session.bind_table`

                :meth:`.Session.get_bind`


        :param \\class_: Specify an alternate class other than
           ``sqlalchemy.orm.session.Session`` which should be used by the
           returned class. This is the only argument that is local to the
           :class:`.sessionmaker` function, and is not sent directly to the
           constructor for ``Session``.

        :param enable_baked_queries: legacy; defaults to ``True``.
           A parameter consumed
           by the :mod:`sqlalchemy.ext.baked` extension to determine if
           "baked queries" should be cached, as is the normal operation
           of this extension.  When set to ``False``, caching as used by
           this particular extension is disabled.

           .. versionchanged:: 1.4 The ``sqlalchemy.ext.baked`` extension is
              legacy and is not used by any of SQLAlchemy\'s internals. This
              flag therefore only affects applications that are making explicit
              use of this extension within their own code.

        :param expire_on_commit:  Defaults to ``True``. When ``True``, all
           instances will be fully expired after each :meth:`~.commit`,
           so that all attribute/object access subsequent to a completed
           transaction will load from the most recent database state.

            .. seealso::

                :ref:`session_committing`

        :param future: Deprecated; this flag is always True.

          .. seealso::

            :ref:`migration_20_toplevel`

        :param info: optional dictionary of arbitrary data to be associated
           with this :class:`.Session`.  Is available via the
           :attr:`.Session.info` attribute.  Note the dictionary is copied at
           construction time so that modifications to the per-
           :class:`.Session` dictionary will be local to that
           :class:`.Session`.

        :param query_cls:  Class which should be used to create new Query
          objects, as returned by the :meth:`~.Session.query` method.
          Defaults to :class:`_query.Query`.

        :param twophase:  When ``True``, all transactions will be started as
            a "two phase" transaction, i.e. using the "two phase" semantics
            of the database in use along with an XID.  During a
            :meth:`~.commit`, after :meth:`~.flush` has been issued for all
            attached databases, the :meth:`~.TwoPhaseTransaction.prepare`
            method on each database\'s :class:`.TwoPhaseTransaction` will be
            called. This allows each database to roll back the entire
            transaction, before each transaction is committed.

        :param autocommit: the "autocommit" keyword is present for backwards
            compatibility but must remain at its default value of ``False``.

        :param join_transaction_mode: Describes the transactional behavior to
          take when a given bind is a :class:`_engine.Connection` that
          has already begun a transaction outside the scope of this
          :class:`_orm.Session`; in other words the
          :meth:`_engine.Connection.in_transaction()` method returns True.

          The following behaviors only take effect when the :class:`_orm.Session`
          **actually makes use of the connection given**; that is, a method
          such as :meth:`_orm.Session.execute`, :meth:`_orm.Session.connection`,
          etc. are actually invoked:

          * ``"conditional_savepoint"`` - this is the default.  if the given
            :class:`_engine.Connection` is begun within a transaction but
            does not have a SAVEPOINT, then ``"rollback_only"`` is used.
            If the :class:`_engine.Connection` is additionally within
            a SAVEPOINT, in other words
            :meth:`_engine.Connection.in_nested_transaction()` method returns
            True, then ``"create_savepoint"`` is used.

            ``"conditional_savepoint"`` behavior attempts to make use of
            savepoints in order to keep the state of the existing transaction
            unchanged, but only if there is already a savepoint in progress;
            otherwise, it is not assumed that the backend in use has adequate
            support for SAVEPOINT, as availability of this feature varies.
            ``"conditional_savepoint"`` also seeks to establish approximate
            backwards compatibility with previous :class:`_orm.Session`
            behavior, for applications that are not setting a specific mode. It
            is recommended that one of the explicit settings be used.

          * ``"create_savepoint"`` - the :class:`_orm.Session` will use
            :meth:`_engine.Connection.begin_nested()` in all cases to create
            its own transaction.  This transaction by its nature rides
            "on top" of any existing transaction that\'s opened on the given
            :class:`_engine.Connection`; if the underlying database and
            the driver in use has full, non-broken support for SAVEPOINT, the
            external transaction will remain unaffected throughout the
            lifespan of the :class:`_orm.Session`.

            The ``"create_savepoint"`` mode is the most useful for integrating
            a :class:`_orm.Session` into a test suite where an externally
            initiated transaction should remain unaffected; however, it relies
            on proper SAVEPOINT support from the underlying driver and
            database.

            .. tip:: When using SQLite, the SQLite driver included through
               Python 3.11 does not handle SAVEPOINTs correctly in all cases
               without workarounds. See the section
               :ref:`pysqlite_serializable` for details on current workarounds.

          * ``"control_fully"`` - the :class:`_orm.Session` will take
            control of the given transaction as its own;
            :meth:`_orm.Session.commit` will call ``.commit()`` on the
            transaction, :meth:`_orm.Session.rollback` will call
            ``.rollback()`` on the transaction, :meth:`_orm.Session.close` will
            call ``.rollback`` on the transaction.

            .. tip:: This mode of use is equivalent to how SQLAlchemy 1.4 would
               handle a :class:`_engine.Connection` given with an existing
               SAVEPOINT (i.e. :meth:`_engine.Connection.begin_nested`); the
               :class:`_orm.Session` would take full control of the existing
               SAVEPOINT.

          * ``"rollback_only"`` - the :class:`_orm.Session` will take control
            of the given transaction for ``.rollback()`` calls only;
            ``.commit()`` calls will not be propagated to the given
            transaction.  ``.close()`` calls will have no effect on the
            given transaction.

            .. tip:: This mode of use is equivalent to how SQLAlchemy 1.4 would
               handle a :class:`_engine.Connection` given with an existing
               regular database transaction (i.e.
               :meth:`_engine.Connection.begin`); the :class:`_orm.Session`
               would propagate :meth:`_orm.Session.rollback` calls to the
               underlying transaction, but not :meth:`_orm.Session.commit` or
               :meth:`_orm.Session.close` calls.

          .. versionadded:: 2.0.0rc1

        :param close_resets_only: Defaults to ``True``. Determines if
          the session should reset itself after calling ``.close()``
          or should pass in a no longer usable state, disabling re-use.

          .. versionadded:: 2.0.22 added flag ``close_resets_only``.
            A future SQLAlchemy version may change the default value of
            this flag to ``False``.

          .. seealso::

            :ref:`session_closing` - Detail on the semantics of
            :meth:`_orm.Session.close` and :meth:`_orm.Session.reset`.

        '''
    connection_callable: _ConnectionCallableProto | None
    def __enter__(self) -> _S: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def in_transaction(self) -> bool:
        """Return True if this :class:`_orm.Session` has begun a transaction.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_orm.Session.is_active`


        """
    def in_nested_transaction(self) -> bool:
        """Return True if this :class:`_orm.Session` has begun a nested
        transaction, e.g. SAVEPOINT.

        .. versionadded:: 1.4

        """
    def get_transaction(self) -> SessionTransaction | None:
        """Return the current root transaction in progress, if any.

        .. versionadded:: 1.4

        """
    def get_nested_transaction(self) -> SessionTransaction | None:
        """Return the current nested transaction in progress, if any.

        .. versionadded:: 1.4

        """
    def info(self) -> _InfoType:
        """A user-modifiable dictionary.

        The initial value of this dictionary can be populated using the
        ``info`` argument to the :class:`.Session` constructor or
        :class:`.sessionmaker` constructor or factory methods.  The dictionary
        here is always local to this :class:`.Session` and can be modified
        independently of all other :class:`.Session` objects.

        """
    def begin(self, nested: bool = False) -> SessionTransaction:
        '''Begin a transaction, or nested transaction,
        on this :class:`.Session`, if one is not already begun.

        The :class:`_orm.Session` object features **autobegin** behavior,
        so that normally it is not necessary to call the
        :meth:`_orm.Session.begin`
        method explicitly. However, it may be used in order to control
        the scope of when the transactional state is begun.

        When used to begin the outermost transaction, an error is raised
        if this :class:`.Session` is already inside of a transaction.

        :param nested: if True, begins a SAVEPOINT transaction and is
         equivalent to calling :meth:`~.Session.begin_nested`. For
         documentation on SAVEPOINT transactions, please see
         :ref:`session_begin_nested`.

        :return: the :class:`.SessionTransaction` object.  Note that
         :class:`.SessionTransaction`
         acts as a Python context manager, allowing :meth:`.Session.begin`
         to be used in a "with" block.  See :ref:`session_explicit_begin` for
         an example.

        .. seealso::

            :ref:`session_autobegin`

            :ref:`unitofwork_transaction`

            :meth:`.Session.begin_nested`


        '''
    def begin_nested(self) -> SessionTransaction:
        '''Begin a "nested" transaction on this Session, e.g. SAVEPOINT.

        The target database(s) and associated drivers must support SQL
        SAVEPOINT for this method to function correctly.

        For documentation on SAVEPOINT
        transactions, please see :ref:`session_begin_nested`.

        :return: the :class:`.SessionTransaction` object.  Note that
         :class:`.SessionTransaction` acts as a context manager, allowing
         :meth:`.Session.begin_nested` to be used in a "with" block.
         See :ref:`session_begin_nested` for a usage example.

        .. seealso::

            :ref:`session_begin_nested`

            :ref:`pysqlite_serializable` - special workarounds required
            with the SQLite driver in order for SAVEPOINT to work
            correctly.

        '''
    def rollback(self) -> None:
        """Rollback the current transaction in progress.

        If no transaction is in progress, this method is a pass-through.

        The method always rolls back
        the topmost database transaction, discarding any nested
        transactions that may be in progress.

        .. seealso::

            :ref:`session_rollback`

            :ref:`unitofwork_transaction`

        """
    def commit(self) -> None:
        '''Flush pending changes and commit the current transaction.

        When the COMMIT operation is complete, all objects are fully
        :term:`expired`, erasing their internal contents, which will be
        automatically re-loaded when the objects are next accessed. In the
        interim, these objects are in an expired state and will not function if
        they are :term:`detached` from the :class:`.Session`. Additionally,
        this re-load operation is not supported when using asyncio-oriented
        APIs. The :paramref:`.Session.expire_on_commit` parameter may be used
        to disable this behavior.

        When there is no transaction in place for the :class:`.Session`,
        indicating that no operations were invoked on this :class:`.Session`
        since the previous call to :meth:`.Session.commit`, the method will
        begin and commit an internal-only "logical" transaction, that does not
        normally affect the database unless pending flush changes were
        detected, but will still invoke event handlers and object expiration
        rules.

        The outermost database transaction is committed unconditionally,
        automatically releasing any SAVEPOINTs in effect.

        .. seealso::

            :ref:`session_committing`

            :ref:`unitofwork_transaction`

            :ref:`asyncio_orm_avoid_lazyloads`

        '''
    def prepare(self) -> None:
        """Prepare the current transaction in progress for two phase commit.

        If no transaction is in progress, this method raises an
        :exc:`~sqlalchemy.exc.InvalidRequestError`.

        Only root transactions of two phase sessions can be prepared. If the
        current transaction is not such, an
        :exc:`~sqlalchemy.exc.InvalidRequestError` is raised.

        """
    def connection(self, bind_arguments: _BindArguments | None = None, execution_options: CoreExecuteOptionsParameter | None = None) -> Connection:
        '''Return a :class:`_engine.Connection` object corresponding to this
        :class:`.Session` object\'s transactional state.

        Either the :class:`_engine.Connection` corresponding to the current
        transaction is returned, or if no transaction is in progress, a new
        one is begun and the :class:`_engine.Connection`
        returned (note that no
        transactional state is established with the DBAPI until the first
        SQL statement is emitted).

        Ambiguity in multi-bind or unbound :class:`.Session` objects can be
        resolved through any of the optional keyword arguments.   This
        ultimately makes usage of the :meth:`.get_bind` method for resolution.

        :param bind_arguments: dictionary of bind arguments.  May include
         "mapper", "bind", "clause", other custom arguments that are passed
         to :meth:`.Session.get_bind`.

        :param execution_options: a dictionary of execution options that will
         be passed to :meth:`_engine.Connection.execution_options`, **when the
         connection is first procured only**.   If the connection is already
         present within the :class:`.Session`, a warning is emitted and
         the arguments are ignored.

         .. seealso::

            :ref:`session_transaction_isolation`

        '''
    @overload
    def execute(self, statement: TypedReturnsRows[_T], params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, _parent_execute_state: Any | None = None, _add_event: Any | None = None) -> Result[_T]: ...
    @overload
    def execute(self, statement: UpdateBase, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, _parent_execute_state: Any | None = None, _add_event: Any | None = None) -> CursorResult[Any]: ...
    @overload
    def execute(self, statement: Executable, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, _parent_execute_state: Any | None = None, _add_event: Any | None = None) -> Result[Any]: ...
    @overload
    def scalar(self, statement: TypedReturnsRows[Tuple[_T]], params: _CoreSingleExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> _T | None: ...
    @overload
    def scalar(self, statement: Executable, params: _CoreSingleExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> Any: ...
    @overload
    def scalars(self, statement: TypedReturnsRows[Tuple[_T]], params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> ScalarResult[_T]: ...
    @overload
    def scalars(self, statement: Executable, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> ScalarResult[Any]: ...
    def close(self) -> None:
        '''Close out the transactional resources and ORM objects used by this
        :class:`_orm.Session`.

        This expunges all ORM objects associated with this
        :class:`_orm.Session`, ends any transaction in progress and
        :term:`releases` any :class:`_engine.Connection` objects which this
        :class:`_orm.Session` itself has checked out from associated
        :class:`_engine.Engine` objects. The operation then leaves the
        :class:`_orm.Session` in a state which it may be used again.

        .. tip::

            In the default running mode the :meth:`_orm.Session.close`
            method **does not prevent the Session from being used again**.
            The :class:`_orm.Session` itself does not actually have a
            distinct "closed" state; it merely means
            the :class:`_orm.Session` will release all database connections
            and ORM objects.

            Setting the parameter :paramref:`_orm.Session.close_resets_only`
            to ``False`` will instead make the ``close`` final, meaning that
            any further action on the session will be forbidden.

        .. versionchanged:: 1.4  The :meth:`.Session.close` method does not
           immediately create a new :class:`.SessionTransaction` object;
           instead, the new :class:`.SessionTransaction` is created only if
           the :class:`.Session` is used again for a database operation.

        .. seealso::

            :ref:`session_closing` - detail on the semantics of
            :meth:`_orm.Session.close` and :meth:`_orm.Session.reset`.

            :meth:`_orm.Session.reset` - a similar method that behaves like
            ``close()`` with  the parameter
            :paramref:`_orm.Session.close_resets_only` set to ``True``.

        '''
    def reset(self) -> None:
        '''Close out the transactional resources and ORM objects used by this
        :class:`_orm.Session`, resetting the session to its initial state.

        This method provides for same "reset-only" behavior that the
        :meth:_orm.Session.close method has provided historically, where the
        state of the :class:`_orm.Session` is reset as though the object were
        brand new, and ready to be used again.
        The method may then be useful for :class:`_orm.Session` objects
        which set :paramref:`_orm.Session.close_resets_only` to ``False``,
        so that "reset only" behavior is still available from this method.

        .. versionadded:: 2.0.22

        .. seealso::

            :ref:`session_closing` - detail on the semantics of
            :meth:`_orm.Session.close` and :meth:`_orm.Session.reset`.

            :meth:`_orm.Session.close` - a similar method will additionally
            prevent re-use of the Session when the parameter
            :paramref:`_orm.Session.close_resets_only` is set to ``False``.
        '''
    def invalidate(self) -> None:
        """Close this Session, using connection invalidation.

        This is a variant of :meth:`.Session.close` that will additionally
        ensure that the :meth:`_engine.Connection.invalidate`
        method will be called on each :class:`_engine.Connection` object
        that is currently in use for a transaction (typically there is only
        one connection unless the :class:`_orm.Session` is used with
        multiple engines).

        This can be called when the database is known to be in a state where
        the connections are no longer safe to be used.

        Below illustrates a scenario when using `gevent
        <https://www.gevent.org/>`_, which can produce ``Timeout`` exceptions
        that may mean the underlying connection should be discarded::

            import gevent

            try:
                sess = Session()
                sess.add(User())
                sess.commit()
            except gevent.Timeout:
                sess.invalidate()
                raise
            except:
                sess.rollback()
                raise

        The method additionally does everything that :meth:`_orm.Session.close`
        does, including that all ORM objects are expunged.

        """
    def expunge_all(self) -> None:
        """Remove all object instances from this ``Session``.

        This is equivalent to calling ``expunge(obj)`` on all objects in this
        ``Session``.

        """
    def bind_mapper(self, mapper: _EntityBindKey[_O], bind: _SessionBind) -> None:
        '''Associate a :class:`_orm.Mapper` or arbitrary Python class with a
        "bind", e.g. an :class:`_engine.Engine` or
        :class:`_engine.Connection`.

        The given entity is added to a lookup used by the
        :meth:`.Session.get_bind` method.

        :param mapper: a :class:`_orm.Mapper` object,
         or an instance of a mapped
         class, or any Python class that is the base of a set of mapped
         classes.

        :param bind: an :class:`_engine.Engine` or :class:`_engine.Connection`
                    object.

        .. seealso::

            :ref:`session_partitioning`

            :paramref:`.Session.binds`

            :meth:`.Session.bind_table`


        '''
    def bind_table(self, table: TableClause, bind: _SessionBind) -> None:
        '''Associate a :class:`_schema.Table` with a "bind", e.g. an
        :class:`_engine.Engine`
        or :class:`_engine.Connection`.

        The given :class:`_schema.Table` is added to a lookup used by the
        :meth:`.Session.get_bind` method.

        :param table: a :class:`_schema.Table` object,
         which is typically the target
         of an ORM mapping, or is present within a selectable that is
         mapped.

        :param bind: an :class:`_engine.Engine` or :class:`_engine.Connection`
         object.

        .. seealso::

            :ref:`session_partitioning`

            :paramref:`.Session.binds`

            :meth:`.Session.bind_mapper`


        '''
    def get_bind(self, mapper: _EntityBindKey[_O] | None = None, *, clause: ClauseElement | None = None, bind: _SessionBind | None = None, _sa_skip_events: bool | None = None, _sa_skip_for_implicit_returning: bool = False, **kw: Any) -> Engine | Connection:
        '''Return a "bind" to which this :class:`.Session` is bound.

        The "bind" is usually an instance of :class:`_engine.Engine`,
        except in the case where the :class:`.Session` has been
        explicitly bound directly to a :class:`_engine.Connection`.

        For a multiply-bound or unbound :class:`.Session`, the
        ``mapper`` or ``clause`` arguments are used to determine the
        appropriate bind to return.

        Note that the "mapper" argument is usually present
        when :meth:`.Session.get_bind` is called via an ORM
        operation such as a :meth:`.Session.query`, each
        individual INSERT/UPDATE/DELETE operation within a
        :meth:`.Session.flush`, call, etc.

        The order of resolution is:

        1. if mapper given and :paramref:`.Session.binds` is present,
           locate a bind based first on the mapper in use, then
           on the mapped class in use, then on any base classes that are
           present in the ``__mro__`` of the mapped class, from more specific
           superclasses to more general.
        2. if clause given and ``Session.binds`` is present,
           locate a bind based on :class:`_schema.Table` objects
           found in the given clause present in ``Session.binds``.
        3. if ``Session.binds`` is present, return that.
        4. if clause given, attempt to return a bind
           linked to the :class:`_schema.MetaData` ultimately
           associated with the clause.
        5. if mapper given, attempt to return a bind
           linked to the :class:`_schema.MetaData` ultimately
           associated with the :class:`_schema.Table` or other
           selectable to which the mapper is mapped.
        6. No bind can be found, :exc:`~sqlalchemy.exc.UnboundExecutionError`
           is raised.

        Note that the :meth:`.Session.get_bind` method can be overridden on
        a user-defined subclass of :class:`.Session` to provide any kind
        of bind resolution scheme.  See the example at
        :ref:`session_custom_partitioning`.

        :param mapper:
          Optional mapped class or corresponding :class:`_orm.Mapper` instance.
          The bind can be derived from a :class:`_orm.Mapper` first by
          consulting the "binds" map associated with this :class:`.Session`,
          and secondly by consulting the :class:`_schema.MetaData` associated
          with the :class:`_schema.Table` to which the :class:`_orm.Mapper` is
          mapped for a bind.

        :param clause:
            A :class:`_expression.ClauseElement` (i.e.
            :func:`_expression.select`,
            :func:`_expression.text`,
            etc.).  If the ``mapper`` argument is not present or could not
            produce a bind, the given expression construct will be searched
            for a bound element, typically a :class:`_schema.Table`
            associated with
            bound :class:`_schema.MetaData`.

        .. seealso::

             :ref:`session_partitioning`

             :paramref:`.Session.binds`

             :meth:`.Session.bind_mapper`

             :meth:`.Session.bind_table`

        '''
    @overload
    def query(self, _entity: _EntityType[_O]) -> Query[_O]: ...
    @overload
    def query(self, _colexpr: TypedColumnsClauseRole[_T]) -> RowReturningQuery[Tuple[_T]]: ...
    @overload
    def query(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1]) -> RowReturningQuery[Tuple[_T0, _T1]]: ...
    @overload
    def query(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2]) -> RowReturningQuery[Tuple[_T0, _T1, _T2]]: ...
    @overload
    def query(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3]]: ...
    @overload
    def query(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4]]: ...
    @overload
    def query(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def query(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6]]: ...
    @overload
    def query(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6], __ent7: _TCCA[_T7]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
    @overload
    def query(self, *entities: _ColumnsClauseArgument[Any], **kwargs: Any) -> Query[Any]: ...
    def no_autoflush(self) -> Iterator[Session]:
        """Return a context manager that disables autoflush.

        e.g.::

            with session.no_autoflush:

                some_object = SomeClass()
                session.add(some_object)
                # won't autoflush
                some_object.related_thing = session.query(SomeRelated).first()

        Operations that proceed within the ``with:`` block
        will not be subject to flushes occurring upon query
        access.  This is useful when initializing a series
        of objects which involve existing database queries,
        where the uncompleted object should not yet be flushed.

        """
    def refresh(self, instance: object, attribute_names: Iterable[str] | None = None, with_for_update: ForUpdateParameter = None) -> None:
        '''Expire and refresh attributes on the given instance.

        The selected attributes will first be expired as they would when using
        :meth:`_orm.Session.expire`; then a SELECT statement will be issued to
        the database to refresh column-oriented attributes with the current
        value available in the current transaction.

        :func:`_orm.relationship` oriented attributes will also be immediately
        loaded if they were already eagerly loaded on the object, using the
        same eager loading strategy that they were loaded with originally.

        .. versionadded:: 1.4 - the :meth:`_orm.Session.refresh` method
           can also refresh eagerly loaded attributes.

        :func:`_orm.relationship` oriented attributes that would normally
        load using the ``select`` (or "lazy") loader strategy will also
        load **if they are named explicitly in the attribute_names
        collection**, emitting a SELECT statement for the attribute using the
        ``immediate`` loader strategy.  If lazy-loaded relationships are not
        named in :paramref:`_orm.Session.refresh.attribute_names`, then
        they remain as "lazy loaded" attributes and are not implicitly
        refreshed.

        .. versionchanged:: 2.0.4  The :meth:`_orm.Session.refresh` method
           will now refresh lazy-loaded :func:`_orm.relationship` oriented
           attributes for those which are named explicitly in the
           :paramref:`_orm.Session.refresh.attribute_names` collection.

        .. tip::

            While the :meth:`_orm.Session.refresh` method is capable of
            refreshing both column and relationship oriented attributes, its
            primary focus is on refreshing of local column-oriented attributes
            on a single instance. For more open ended "refresh" functionality,
            including the ability to refresh the attributes on many objects at
            once while having explicit control over relationship loader
            strategies, use the
            :ref:`populate existing <orm_queryguide_populate_existing>` feature
            instead.

        Note that a highly isolated transaction will return the same values as
        were previously read in that same transaction, regardless of changes
        in database state outside of that transaction.   Refreshing
        attributes usually only makes sense at the start of a transaction
        where database rows have not yet been accessed.

        :param attribute_names: optional.  An iterable collection of
          string attribute names indicating a subset of attributes to
          be refreshed.

        :param with_for_update: optional boolean ``True`` indicating FOR UPDATE
          should be used, or may be a dictionary containing flags to
          indicate a more specific set of FOR UPDATE flags for the SELECT;
          flags should match the parameters of
          :meth:`_query.Query.with_for_update`.
          Supersedes the :paramref:`.Session.refresh.lockmode` parameter.

        .. seealso::

            :ref:`session_expire` - introductory material

            :meth:`.Session.expire`

            :meth:`.Session.expire_all`

            :ref:`orm_queryguide_populate_existing` - allows any ORM query
            to refresh objects as they would be loaded normally.

        '''
    def expire_all(self) -> None:
        """Expires all persistent instances within this Session.

        When any attributes on a persistent instance is next accessed,
        a query will be issued using the
        :class:`.Session` object's current transactional context in order to
        load all expired attributes for the given instance.   Note that
        a highly isolated transaction will return the same values as were
        previously read in that same transaction, regardless of changes
        in database state outside of that transaction.

        To expire individual objects and individual attributes
        on those objects, use :meth:`Session.expire`.

        The :class:`.Session` object's default behavior is to
        expire all state whenever the :meth:`Session.rollback`
        or :meth:`Session.commit` methods are called, so that new
        state can be loaded for the new transaction.   For this reason,
        calling :meth:`Session.expire_all` is not usually needed,
        assuming the transaction is isolated.

        .. seealso::

            :ref:`session_expire` - introductory material

            :meth:`.Session.expire`

            :meth:`.Session.refresh`

            :meth:`_orm.Query.populate_existing`

        """
    def expire(self, instance: object, attribute_names: Iterable[str] | None = None) -> None:
        """Expire the attributes on an instance.

        Marks the attributes of an instance as out of date. When an expired
        attribute is next accessed, a query will be issued to the
        :class:`.Session` object's current transactional context in order to
        load all expired attributes for the given instance.   Note that
        a highly isolated transaction will return the same values as were
        previously read in that same transaction, regardless of changes
        in database state outside of that transaction.

        To expire all objects in the :class:`.Session` simultaneously,
        use :meth:`Session.expire_all`.

        The :class:`.Session` object's default behavior is to
        expire all state whenever the :meth:`Session.rollback`
        or :meth:`Session.commit` methods are called, so that new
        state can be loaded for the new transaction.   For this reason,
        calling :meth:`Session.expire` only makes sense for the specific
        case that a non-ORM SQL statement was emitted in the current
        transaction.

        :param instance: The instance to be refreshed.
        :param attribute_names: optional list of string attribute names
          indicating a subset of attributes to be expired.

        .. seealso::

            :ref:`session_expire` - introductory material

            :meth:`.Session.expire`

            :meth:`.Session.refresh`

            :meth:`_orm.Query.populate_existing`

        """
    def expunge(self, instance: object) -> None:
        """Remove the `instance` from this ``Session``.

        This will free all internal references to the instance.  Cascading
        will be applied according to the *expunge* cascade rule.

        """
    def add(self, instance: object, _warn: bool = True) -> None:
        """Place an object into this :class:`_orm.Session`.

        Objects that are in the :term:`transient` state when passed to the
        :meth:`_orm.Session.add` method will move to the
        :term:`pending` state, until the next flush, at which point they
        will move to the :term:`persistent` state.

        Objects that are in the :term:`detached` state when passed to the
        :meth:`_orm.Session.add` method will move to the :term:`persistent`
        state directly.

        If the transaction used by the :class:`_orm.Session` is rolled back,
        objects which were transient when they were passed to
        :meth:`_orm.Session.add` will be moved back to the
        :term:`transient` state, and will no longer be present within this
        :class:`_orm.Session`.

        .. seealso::

            :meth:`_orm.Session.add_all`

            :ref:`session_adding` - at :ref:`session_basics`

        """
    def add_all(self, instances: Iterable[object]) -> None:
        """Add the given collection of instances to this :class:`_orm.Session`.

        See the documentation for :meth:`_orm.Session.add` for a general
        behavioral description.

        .. seealso::

            :meth:`_orm.Session.add`

            :ref:`session_adding` - at :ref:`session_basics`

        """
    def delete(self, instance: object) -> None:
        """Mark an instance as deleted.

        The object is assumed to be either :term:`persistent` or
        :term:`detached` when passed; after the method is called, the
        object will remain in the :term:`persistent` state until the next
        flush proceeds.  During this time, the object will also be a member
        of the :attr:`_orm.Session.deleted` collection.

        When the next flush proceeds, the object will move to the
        :term:`deleted` state, indicating a ``DELETE`` statement was emitted
        for its row within the current transaction.   When the transaction
        is successfully committed,
        the deleted object is moved to the :term:`detached` state and is
        no longer present within this :class:`_orm.Session`.

        .. seealso::

            :ref:`session_deleting` - at :ref:`session_basics`

        """
    def get(self, entity: _EntityBindKey[_O], ident: _PKIdentityArgument, *, options: Sequence[ORMOption] | None = None, populate_existing: bool = False, with_for_update: ForUpdateParameter = None, identity_token: Any | None = None, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None) -> _O | None:
        '''Return an instance based on the given primary key identifier,
        or ``None`` if not found.

        E.g.::

            my_user = session.get(User, 5)

            some_object = session.get(VersionedFoo, (5, 10))

            some_object = session.get(
                VersionedFoo,
                {"id": 5, "version_id": 10}
            )

        .. versionadded:: 1.4 Added :meth:`_orm.Session.get`, which is moved
           from the now legacy :meth:`_orm.Query.get` method.

        :meth:`_orm.Session.get` is special in that it provides direct
        access to the identity map of the :class:`.Session`.
        If the given primary key identifier is present
        in the local identity map, the object is returned
        directly from this collection and no SQL is emitted,
        unless the object has been marked fully expired.
        If not present,
        a SELECT is performed in order to locate the object.

        :meth:`_orm.Session.get` also will perform a check if
        the object is present in the identity map and
        marked as expired - a SELECT
        is emitted to refresh the object as well as to
        ensure that the row is still present.
        If not, :class:`~sqlalchemy.orm.exc.ObjectDeletedError` is raised.

        :param entity: a mapped class or :class:`.Mapper` indicating the
         type of entity to be loaded.

        :param ident: A scalar, tuple, or dictionary representing the
         primary key.  For a composite (e.g. multiple column) primary key,
         a tuple or dictionary should be passed.

         For a single-column primary key, the scalar calling form is typically
         the most expedient.  If the primary key of a row is the value "5",
         the call looks like::

            my_object = session.get(SomeClass, 5)

         The tuple form contains primary key values typically in
         the order in which they correspond to the mapped
         :class:`_schema.Table`
         object\'s primary key columns, or if the
         :paramref:`_orm.Mapper.primary_key` configuration parameter were
         used, in
         the order used for that parameter. For example, if the primary key
         of a row is represented by the integer
         digits "5, 10" the call would look like::

             my_object = session.get(SomeClass, (5, 10))

         The dictionary form should include as keys the mapped attribute names
         corresponding to each element of the primary key.  If the mapped class
         has the attributes ``id``, ``version_id`` as the attributes which
         store the object\'s primary key value, the call would look like::

            my_object = session.get(SomeClass, {"id": 5, "version_id": 10})

        :param options: optional sequence of loader options which will be
         applied to the query, if one is emitted.

        :param populate_existing: causes the method to unconditionally emit
         a SQL query and refresh the object with the newly loaded data,
         regardless of whether or not the object is already present.

        :param with_for_update: optional boolean ``True`` indicating FOR UPDATE
          should be used, or may be a dictionary containing flags to
          indicate a more specific set of FOR UPDATE flags for the SELECT;
          flags should match the parameters of
          :meth:`_query.Query.with_for_update`.
          Supersedes the :paramref:`.Session.refresh.lockmode` parameter.

        :param execution_options: optional dictionary of execution options,
         which will be associated with the query execution if one is emitted.
         This dictionary can provide a subset of the options that are
         accepted by :meth:`_engine.Connection.execution_options`, and may
         also provide additional options understood only in an ORM context.

         .. versionadded:: 1.4.29

         .. seealso::

            :ref:`orm_queryguide_execution_options` - ORM-specific execution
            options

        :param bind_arguments: dictionary of additional arguments to determine
         the bind.  May include "mapper", "bind", or other custom arguments.
         Contents of this dictionary are passed to the
         :meth:`.Session.get_bind` method.

         .. versionadded: 2.0.0rc1

        :return: The object instance, or ``None``.

        '''
    def get_one(self, entity: _EntityBindKey[_O], ident: _PKIdentityArgument, *, options: Sequence[ORMOption] | None = None, populate_existing: bool = False, with_for_update: ForUpdateParameter = None, identity_token: Any | None = None, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None) -> _O:
        """Return exactly one instance based on the given primary key
        identifier, or raise an exception if not found.

        Raises ``sqlalchemy.orm.exc.NoResultFound`` if the query
        selects no rows.

        For a detailed documentation of the arguments see the
        method :meth:`.Session.get`.

        .. versionadded:: 2.0.22

        :return: The object instance, or ``None``.

        .. seealso::

            :meth:`.Session.get` - equivalent method that instead
              returns ``None`` if no row was found with the provided primary
              key

        """
    def merge(self, instance: _O, *, load: bool = True, options: Sequence[ORMOption] | None = None) -> _O:
        '''Copy the state of a given instance into a corresponding instance
        within this :class:`.Session`.

        :meth:`.Session.merge` examines the primary key attributes of the
        source instance, and attempts to reconcile it with an instance of the
        same primary key in the session.   If not found locally, it attempts
        to load the object from the database based on primary key, and if
        none can be located, creates a new instance.  The state of each
        attribute on the source instance is then copied to the target
        instance.  The resulting target instance is then returned by the
        method; the original source instance is left unmodified, and
        un-associated with the :class:`.Session` if not already.

        This operation cascades to associated instances if the association is
        mapped with ``cascade="merge"``.

        See :ref:`unitofwork_merging` for a detailed discussion of merging.

        :param instance: Instance to be merged.
        :param load: Boolean, when False, :meth:`.merge` switches into
         a "high performance" mode which causes it to forego emitting history
         events as well as all database access.  This flag is used for
         cases such as transferring graphs of objects into a :class:`.Session`
         from a second level cache, or to transfer just-loaded objects
         into the :class:`.Session` owned by a worker thread or process
         without re-querying the database.

         The ``load=False`` use case adds the caveat that the given
         object has to be in a "clean" state, that is, has no pending changes
         to be flushed - even if the incoming object is detached from any
         :class:`.Session`.   This is so that when
         the merge operation populates local attributes and
         cascades to related objects and
         collections, the values can be "stamped" onto the
         target object as is, without generating any history or attribute
         events, and without the need to reconcile the incoming data with
         any existing related objects or collections that might not
         be loaded.  The resulting objects from ``load=False`` are always
         produced as "clean", so it is only appropriate that the given objects
         should be "clean" as well, else this suggests a mis-use of the
         method.
        :param options: optional sequence of loader options which will be
         applied to the :meth:`_orm.Session.get` method when the merge
         operation loads the existing version of the object from the database.

         .. versionadded:: 1.4.24


        .. seealso::

            :func:`.make_transient_to_detached` - provides for an alternative
            means of "merging" a single object into the :class:`.Session`

        '''
    def enable_relationship_loading(self, obj: object) -> None:
        '''Associate an object with this :class:`.Session` for related
        object loading.

        .. warning::

            :meth:`.enable_relationship_loading` exists to serve special
            use cases and is not recommended for general use.

        Accesses of attributes mapped with :func:`_orm.relationship`
        will attempt to load a value from the database using this
        :class:`.Session` as the source of connectivity.  The values
        will be loaded based on foreign key and primary key values
        present on this object - if not present, then those relationships
        will be unavailable.

        The object will be attached to this session, but will
        **not** participate in any persistence operations; its state
        for almost all purposes will remain either "transient" or
        "detached", except for the case of relationship loading.

        Also note that backrefs will often not work as expected.
        Altering a relationship-bound attribute on the target object
        may not fire off a backref event, if the effective value
        is what was already loaded from a foreign-key-holding value.

        The :meth:`.Session.enable_relationship_loading` method is
        similar to the ``load_on_pending`` flag on :func:`_orm.relationship`.
        Unlike that flag, :meth:`.Session.enable_relationship_loading` allows
        an object to remain transient while still being able to load
        related items.

        To make a transient object associated with a :class:`.Session`
        via :meth:`.Session.enable_relationship_loading` pending, add
        it to the :class:`.Session` using :meth:`.Session.add` normally.
        If the object instead represents an existing identity in the database,
        it should be merged using :meth:`.Session.merge`.

        :meth:`.Session.enable_relationship_loading` does not improve
        behavior when the ORM is used normally - object references should be
        constructed at the object level, not at the foreign key level, so
        that they are present in an ordinary way before flush()
        proceeds.  This method is not intended for general use.

        .. seealso::

            :paramref:`_orm.relationship.load_on_pending` - this flag
            allows per-relationship loading of many-to-ones on items that
            are pending.

            :func:`.make_transient_to_detached` - allows for an object to
            be added to a :class:`.Session` without SQL emitted, which then
            will unexpire attributes on access.

        '''
    def __contains__(self, instance: object) -> bool:
        """Return True if the instance is associated with this session.

        The instance may be pending or persistent within the Session for a
        result of True.

        """
    def __iter__(self) -> Iterator[object]:
        """Iterate over all pending or persistent instances within this
        Session.

        """
    def flush(self, objects: Sequence[Any] | None = None) -> None:
        """Flush all the object changes to the database.

        Writes out all pending object creations, deletions and modifications
        to the database as INSERTs, DELETEs, UPDATEs, etc.  Operations are
        automatically ordered by the Session's unit of work dependency
        solver.

        Database operations will be issued in the current transactional
        context and do not affect the state of the transaction, unless an
        error occurs, in which case the entire transaction is rolled back.
        You may flush() as often as you like within a transaction to move
        changes from Python to the database's transaction buffer.

        :param objects: Optional; restricts the flush operation to operate
          only on elements that are in the given collection.

          This feature is for an extremely narrow set of use cases where
          particular objects may need to be operated upon before the
          full flush() occurs.  It is not intended for general use.

        """
    def bulk_save_objects(self, objects: Iterable[object], return_defaults: bool = False, update_changed_only: bool = True, preserve_order: bool = True) -> None:
        '''Perform a bulk save of the given list of objects.

        .. legacy::

            This method is a legacy feature as of the 2.0 series of
            SQLAlchemy.   For modern bulk INSERT and UPDATE, see
            the sections :ref:`orm_queryguide_bulk_insert` and
            :ref:`orm_queryguide_bulk_update`.

            For general INSERT and UPDATE of existing ORM mapped objects,
            prefer standard :term:`unit of work` data management patterns,
            introduced in the :ref:`unified_tutorial` at
            :ref:`tutorial_orm_data_manipulation`.  SQLAlchemy 2.0
            now uses :ref:`engine_insertmanyvalues` with modern dialects
            which solves previous issues of bulk INSERT slowness.

        :param objects: a sequence of mapped object instances.  The mapped
         objects are persisted as is, and are **not** associated with the
         :class:`.Session` afterwards.

         For each object, whether the object is sent as an INSERT or an
         UPDATE is dependent on the same rules used by the :class:`.Session`
         in traditional operation; if the object has the
         :attr:`.InstanceState.key`
         attribute set, then the object is assumed to be "detached" and
         will result in an UPDATE.  Otherwise, an INSERT is used.

         In the case of an UPDATE, statements are grouped based on which
         attributes have changed, and are thus to be the subject of each
         SET clause.  If ``update_changed_only`` is False, then all
         attributes present within each object are applied to the UPDATE
         statement, which may help in allowing the statements to be grouped
         together into a larger executemany(), and will also reduce the
         overhead of checking history on attributes.

        :param return_defaults: when True, rows that are missing values which
         generate defaults, namely integer primary key defaults and sequences,
         will be inserted **one at a time**, so that the primary key value
         is available.  In particular this will allow joined-inheritance
         and other multi-table mappings to insert correctly without the need
         to provide primary key values ahead of time; however,
         :paramref:`.Session.bulk_save_objects.return_defaults` **greatly
         reduces the performance gains** of the method overall.  It is strongly
         advised to please use the standard :meth:`_orm.Session.add_all`
         approach.

        :param update_changed_only: when True, UPDATE statements are rendered
         based on those attributes in each state that have logged changes.
         When False, all attributes present are rendered into the SET clause
         with the exception of primary key attributes.

        :param preserve_order: when True, the order of inserts and updates
         matches exactly the order in which the objects are given.   When
         False, common types of objects are grouped into inserts
         and updates, to allow for more batching opportunities.

        .. seealso::

            :doc:`queryguide/dml`

            :meth:`.Session.bulk_insert_mappings`

            :meth:`.Session.bulk_update_mappings`

        '''
    def bulk_insert_mappings(self, mapper: Mapper[Any], mappings: Iterable[Dict[str, Any]], return_defaults: bool = False, render_nulls: bool = False) -> None:
        """Perform a bulk insert of the given list of mapping dictionaries.

        .. legacy::

            This method is a legacy feature as of the 2.0 series of
            SQLAlchemy.   For modern bulk INSERT and UPDATE, see
            the sections :ref:`orm_queryguide_bulk_insert` and
            :ref:`orm_queryguide_bulk_update`.  The 2.0 API shares
            implementation details with this method and adds new features
            as well.

        :param mapper: a mapped class, or the actual :class:`_orm.Mapper`
         object,
         representing the single kind of object represented within the mapping
         list.

        :param mappings: a sequence of dictionaries, each one containing the
         state of the mapped row to be inserted, in terms of the attribute
         names on the mapped class.   If the mapping refers to multiple tables,
         such as a joined-inheritance mapping, each dictionary must contain all
         keys to be populated into all tables.

        :param return_defaults: when True, the INSERT process will be altered
         to ensure that newly generated primary key values will be fetched.
         The rationale for this parameter is typically to enable
         :ref:`Joined Table Inheritance <joined_inheritance>` mappings to
         be bulk inserted.

         .. note:: for backends that don't support RETURNING, the
            :paramref:`_orm.Session.bulk_insert_mappings.return_defaults`
            parameter can significantly decrease performance as INSERT
            statements can no longer be batched.   See
            :ref:`engine_insertmanyvalues`
            for background on which backends are affected.

        :param render_nulls: When True, a value of ``None`` will result
         in a NULL value being included in the INSERT statement, rather
         than the column being omitted from the INSERT.   This allows all
         the rows being INSERTed to have the identical set of columns which
         allows the full set of rows to be batched to the DBAPI.  Normally,
         each column-set that contains a different combination of NULL values
         than the previous row must omit a different series of columns from
         the rendered INSERT statement, which means it must be emitted as a
         separate statement.   By passing this flag, the full set of rows
         are guaranteed to be batchable into one batch; the cost however is
         that server-side defaults which are invoked by an omitted column will
         be skipped, so care must be taken to ensure that these are not
         necessary.

         .. warning::

            When this flag is set, **server side default SQL values will
            not be invoked** for those columns that are inserted as NULL;
            the NULL value will be sent explicitly.   Care must be taken
            to ensure that no server-side default functions need to be
            invoked for the operation as a whole.

        .. seealso::

            :doc:`queryguide/dml`

            :meth:`.Session.bulk_save_objects`

            :meth:`.Session.bulk_update_mappings`

        """
    def bulk_update_mappings(self, mapper: Mapper[Any], mappings: Iterable[Dict[str, Any]]) -> None:
        """Perform a bulk update of the given list of mapping dictionaries.

        .. legacy::

            This method is a legacy feature as of the 2.0 series of
            SQLAlchemy.   For modern bulk INSERT and UPDATE, see
            the sections :ref:`orm_queryguide_bulk_insert` and
            :ref:`orm_queryguide_bulk_update`.  The 2.0 API shares
            implementation details with this method and adds new features
            as well.

        :param mapper: a mapped class, or the actual :class:`_orm.Mapper`
         object,
         representing the single kind of object represented within the mapping
         list.

        :param mappings: a sequence of dictionaries, each one containing the
         state of the mapped row to be updated, in terms of the attribute names
         on the mapped class.   If the mapping refers to multiple tables, such
         as a joined-inheritance mapping, each dictionary may contain keys
         corresponding to all tables.   All those keys which are present and
         are not part of the primary key are applied to the SET clause of the
         UPDATE statement; the primary key values, which are required, are
         applied to the WHERE clause.


        .. seealso::

            :doc:`queryguide/dml`

            :meth:`.Session.bulk_insert_mappings`

            :meth:`.Session.bulk_save_objects`

        """
    def is_modified(self, instance: object, include_collections: bool = True) -> bool:
        '''Return ``True`` if the given instance has locally
        modified attributes.

        This method retrieves the history for each instrumented
        attribute on the instance and performs a comparison of the current
        value to its previously committed value, if any.

        It is in effect a more expensive and accurate
        version of checking for the given instance in the
        :attr:`.Session.dirty` collection; a full test for
        each attribute\'s net "dirty" status is performed.

        E.g.::

            return session.is_modified(someobject)

        A few caveats to this method apply:

        * Instances present in the :attr:`.Session.dirty` collection may
          report ``False`` when tested with this method.  This is because
          the object may have received change events via attribute mutation,
          thus placing it in :attr:`.Session.dirty`, but ultimately the state
          is the same as that loaded from the database, resulting in no net
          change here.
        * Scalar attributes may not have recorded the previously set
          value when a new value was applied, if the attribute was not loaded,
          or was expired, at the time the new value was received - in these
          cases, the attribute is assumed to have a change, even if there is
          ultimately no net change against its database value. SQLAlchemy in
          most cases does not need the "old" value when a set event occurs, so
          it skips the expense of a SQL call if the old value isn\'t present,
          based on the assumption that an UPDATE of the scalar value is
          usually needed, and in those few cases where it isn\'t, is less
          expensive on average than issuing a defensive SELECT.

          The "old" value is fetched unconditionally upon set only if the
          attribute container has the ``active_history`` flag set to ``True``.
          This flag is set typically for primary key attributes and scalar
          object references that are not a simple many-to-one.  To set this
          flag for any arbitrary mapped column, use the ``active_history``
          argument with :func:`.column_property`.

        :param instance: mapped instance to be tested for pending changes.
        :param include_collections: Indicates if multivalued collections
         should be included in the operation.  Setting this to ``False`` is a
         way to detect only local-column based properties (i.e. scalar columns
         or many-to-one foreign keys) that would result in an UPDATE for this
         instance upon flush.

        '''
    @property
    def is_active(self) -> bool:
        '''True if this :class:`.Session` not in "partial rollback" state.

        .. versionchanged:: 1.4 The :class:`_orm.Session` no longer begins
           a new transaction immediately, so this attribute will be False
           when the :class:`_orm.Session` is first instantiated.

        "partial rollback" state typically indicates that the flush process
        of the :class:`_orm.Session` has failed, and that the
        :meth:`_orm.Session.rollback` method must be emitted in order to
        fully roll back the transaction.

        If this :class:`_orm.Session` is not in a transaction at all, the
        :class:`_orm.Session` will autobegin when it is first used, so in this
        case :attr:`_orm.Session.is_active` will return True.

        Otherwise, if this :class:`_orm.Session` is within a transaction,
        and that transaction has not been rolled back internally, the
        :attr:`_orm.Session.is_active` will also return True.

        .. seealso::

            :ref:`faq_session_rollback`

            :meth:`_orm.Session.in_transaction`

        '''
    @property
    def dirty(self) -> IdentitySet:
        """The set of all persistent instances considered dirty.

        E.g.::

            some_mapped_object in session.dirty

        Instances are considered dirty when they were modified but not
        deleted.

        Note that this 'dirty' calculation is 'optimistic'; most
        attribute-setting or collection modification operations will
        mark an instance as 'dirty' and place it in this set, even if
        there is no net change to the attribute's value.  At flush
        time, the value of each attribute is compared to its
        previously saved value, and if there's no net change, no SQL
        operation will occur (this is a more expensive operation so
        it's only done at flush time).

        To check if an instance has actionable net changes to its
        attributes, use the :meth:`.Session.is_modified` method.

        """
    @property
    def deleted(self) -> IdentitySet:
        """The set of all instances marked as 'deleted' within this ``Session``"""
    @property
    def new(self) -> IdentitySet:
        """The set of all instances marked as 'new' within this ``Session``."""

class sessionmaker(_SessionClassMethods, Generic[_S]):
    """A configurable :class:`.Session` factory.

    The :class:`.sessionmaker` factory generates new
    :class:`.Session` objects when called, creating them given
    the configurational arguments established here.

    e.g.::

        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        # an Engine, which the Session will use for connection
        # resources
        engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/')

        Session = sessionmaker(engine)

        with Session() as session:
            session.add(some_object)
            session.add(some_other_object)
            session.commit()

    Context manager use is optional; otherwise, the returned
    :class:`_orm.Session` object may be closed explicitly via the
    :meth:`_orm.Session.close` method.   Using a
    ``try:/finally:`` block is optional, however will ensure that the close
    takes place even if there are database errors::

        session = Session()
        try:
            session.add(some_object)
            session.add(some_other_object)
            session.commit()
        finally:
            session.close()

    :class:`.sessionmaker` acts as a factory for :class:`_orm.Session`
    objects in the same way as an :class:`_engine.Engine` acts as a factory
    for :class:`_engine.Connection` objects.  In this way it also includes
    a :meth:`_orm.sessionmaker.begin` method, that provides a context
    manager which both begins and commits a transaction, as well as closes
    out the :class:`_orm.Session` when complete, rolling back the transaction
    if any errors occur::

        Session = sessionmaker(engine)

        with Session.begin() as session:
            session.add(some_object)
            session.add(some_other_object)
        # commits transaction, closes session

    .. versionadded:: 1.4

    When calling upon :class:`_orm.sessionmaker` to construct a
    :class:`_orm.Session`, keyword arguments may also be passed to the
    method; these arguments will override that of the globally configured
    parameters.  Below we use a :class:`_orm.sessionmaker` bound to a certain
    :class:`_engine.Engine` to produce a :class:`_orm.Session` that is instead
    bound to a specific :class:`_engine.Connection` procured from that engine::

        Session = sessionmaker(engine)

        # bind an individual session to a connection

        with engine.connect() as connection:
            with Session(bind=connection) as session:
                # work with session

    The class also includes a method :meth:`_orm.sessionmaker.configure`, which
    can be used to specify additional keyword arguments to the factory, which
    will take effect for subsequent :class:`.Session` objects generated. This
    is usually used to associate one or more :class:`_engine.Engine` objects
    with an existing
    :class:`.sessionmaker` factory before it is first used::

        # application starts, sessionmaker does not have
        # an engine bound yet
        Session = sessionmaker()

        # ... later, when an engine URL is read from a configuration
        # file or other events allow the engine to be created
        engine = create_engine('sqlite:///foo.db')
        Session.configure(bind=engine)

        sess = Session()
        # work with session

    .. seealso::

        :ref:`session_getting` - introductory text on creating
        sessions using :class:`.sessionmaker`.

    """
    class_: Type[_S]
    @overload
    def __init__(self, bind: _SessionBind | None = ..., *, class_: Type[_S], autoflush: bool = ..., expire_on_commit: bool = ..., info: _InfoType | None = ..., **kw: Any) -> None: ...
    @overload
    def __init__(self, bind: _SessionBind | None = ..., *, autoflush: bool = ..., expire_on_commit: bool = ..., info: _InfoType | None = ..., **kw: Any) -> None: ...
    def begin(self) -> contextlib.AbstractContextManager[_S]:
        """Produce a context manager that both provides a new
        :class:`_orm.Session` as well as a transaction that commits.


        e.g.::

            Session = sessionmaker(some_engine)

            with Session.begin() as session:
                session.add(some_object)

            # commits transaction, closes session

        .. versionadded:: 1.4


        """
    def __call__(self, **local_kw: Any) -> _S:
        '''Produce a new :class:`.Session` object using the configuration
        established in this :class:`.sessionmaker`.

        In Python, the ``__call__`` method is invoked on an object when
        it is "called" in the same way as a function::

            Session = sessionmaker(some_engine)
            session = Session()  # invokes sessionmaker.__call__()

        '''
    def configure(self, **new_kw: Any) -> None:
        """(Re)configure the arguments for this sessionmaker.

        e.g.::

            Session = sessionmaker()

            Session.configure(bind=create_engine('sqlite://'))
        """

def close_all_sessions() -> None:
    """Close all sessions in memory.

    This function consults a global registry of all :class:`.Session` objects
    and calls :meth:`.Session.close` on them, which resets them to a clean
    state.

    This function is not for general use but may be useful for test suites
    within the teardown scheme.

    .. versionadded:: 1.3

    """
def make_transient(instance: object) -> None:
    '''Alter the state of the given instance so that it is :term:`transient`.

    .. note::

        :func:`.make_transient` is a special-case function for
        advanced use cases only.

    The given mapped instance is assumed to be in the :term:`persistent` or
    :term:`detached` state.   The function will remove its association with any
    :class:`.Session` as well as its :attr:`.InstanceState.identity`. The
    effect is that the object will behave as though it were newly constructed,
    except retaining any attribute / collection values that were loaded at the
    time of the call.   The :attr:`.InstanceState.deleted` flag is also reset
    if this object had been deleted as a result of using
    :meth:`.Session.delete`.

    .. warning::

        :func:`.make_transient` does **not** "unexpire" or otherwise eagerly
        load ORM-mapped attributes that are not currently loaded at the time
        the function is called.   This includes attributes which:

        * were expired via :meth:`.Session.expire`

        * were expired as the natural effect of committing a session
          transaction, e.g. :meth:`.Session.commit`

        * are normally :term:`lazy loaded` but are not currently loaded

        * are "deferred" (see :ref:`orm_queryguide_column_deferral`) and are
          not yet loaded

        * were not present in the query which loaded this object, such as that
          which is common in joined table inheritance and other scenarios.

        After :func:`.make_transient` is called, unloaded attributes such
        as those above will normally resolve to the value ``None`` when
        accessed, or an empty collection for a collection-oriented attribute.
        As the object is transient and un-associated with any database
        identity, it will no longer retrieve these values.

    .. seealso::

        :func:`.make_transient_to_detached`

    '''
def make_transient_to_detached(instance: object) -> None:
    '''Make the given transient instance :term:`detached`.

    .. note::

        :func:`.make_transient_to_detached` is a special-case function for
        advanced use cases only.

    All attribute history on the given instance
    will be reset as though the instance were freshly loaded
    from a query.  Missing attributes will be marked as expired.
    The primary key attributes of the object, which are required, will be made
    into the "key" of the instance.

    The object can then be added to a session, or merged
    possibly with the load=False flag, at which point it will look
    as if it were loaded that way, without emitting SQL.

    This is a special use case function that differs from a normal
    call to :meth:`.Session.merge` in that a given persistent state
    can be manufactured without any SQL calls.

    .. seealso::

        :func:`.make_transient`

        :meth:`.Session.enable_relationship_loading`

    '''
def object_session(instance: object) -> Session | None:
    """Return the :class:`.Session` to which the given instance belongs.

    This is essentially the same as the :attr:`.InstanceState.session`
    accessor.  See that attribute for details.

    """
