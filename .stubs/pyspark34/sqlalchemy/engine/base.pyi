from . import CursorResult as CursorResult, ScalarResult as ScalarResult
from .. import exc as exc, inspection as inspection, log as log, util as util
from ..event import dispatcher as dispatcher
from ..log import _EchoFlagType
from ..pool import Pool as Pool, PoolProxiedConnection as PoolProxiedConnection
from ..sql import Executable as Executable, compiler as compiler
from ..sql._typing import _InfoType
from ..sql.compiler import Compiled as Compiled
from ..sql.ddl import ExecutableDDLElement as ExecutableDDLElement, SchemaDropper as SchemaDropper, SchemaGenerator as SchemaGenerator
from ..sql.functions import FunctionElement as FunctionElement
from ..sql.schema import DefaultGenerator as DefaultGenerator, HasSchemaAttr as HasSchemaAttr, SchemaItem as SchemaItem
from ..sql.selectable import TypedReturnsRows as TypedReturnsRows
from .interfaces import BindTyping as BindTyping, CompiledCacheType as CompiledCacheType, ConnectionEventsTarget as ConnectionEventsTarget, CoreExecuteOptionsParameter as CoreExecuteOptionsParameter, DBAPICursor as DBAPICursor, Dialect as Dialect, ExceptionContext as ExceptionContext, ExecuteStyle as ExecuteStyle, ExecutionContext as ExecutionContext, IsolationLevel as IsolationLevel, SchemaTranslateMapType as SchemaTranslateMapType, _CoreAnyExecuteParams, _CoreSingleExecuteParams, _DBAPIAnyExecuteParams, _ExecuteOptions
from .reflection import Inspector as Inspector
from .url import URL as URL
from .util import TransactionalContext as TransactionalContext
from _typeshed import Incomplete
from typing import Any, Iterator, List, Mapping, Tuple, overload

NO_OPTIONS: Mapping[str, Any]

class Connection(ConnectionEventsTarget, inspection.Inspectable['Inspector']):
    """Provides high-level functionality for a wrapped DB-API connection.

    The :class:`_engine.Connection` object is procured by calling the
    :meth:`_engine.Engine.connect` method of the :class:`_engine.Engine`
    object, and provides services for execution of SQL statements as well
    as transaction control.

    The Connection object is **not** thread-safe. While a Connection can be
    shared among threads using properly synchronized access, it is still
    possible that the underlying DBAPI connection may not support shared
    access between threads. Check the DBAPI documentation for details.

    The Connection object represents a single DBAPI connection checked out
    from the connection pool. In this state, the connection pool has no
    affect upon the connection, including its expiration or timeout state.
    For the connection pool to properly manage connections, connections
    should be returned to the connection pool (i.e. ``connection.close()``)
    whenever the connection is not in use.

    .. index::
      single: thread safety; Connection

    """
    dispatch: dispatcher[ConnectionEventsTarget]
    should_close_with_result: bool
    engine: Incomplete
    dialect: Incomplete
    def __init__(self, engine: Engine, connection: PoolProxiedConnection | None = None, _has_events: bool | None = None, _allow_revalidate: bool = True, _allow_autobegin: bool = True) -> None:
        """Construct a new Connection."""
    def schema_for_object(self, obj: HasSchemaAttr) -> str | None:
        """Return the schema name for the given schema item taking into
        account current schema translate map.

        """
    def __enter__(self) -> Connection: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    @overload
    def execution_options(self, *, compiled_cache: CompiledCacheType | None = ..., logging_token: str = ..., isolation_level: IsolationLevel = ..., no_parameters: bool = False, stream_results: bool = False, max_row_buffer: int = ..., yield_per: int = ..., insertmanyvalues_page_size: int = ..., schema_translate_map: SchemaTranslateMapType | None = ..., **opt: Any) -> Connection: ...
    @overload
    def execution_options(self, **opt: Any) -> Connection: ...
    def get_execution_options(self) -> _ExecuteOptions:
        """Get the non-SQL options which will take effect during execution.

        .. versionadded:: 1.3

        .. seealso::

            :meth:`_engine.Connection.execution_options`
        """
    @property
    def closed(self) -> bool:
        """Return True if this connection is closed."""
    @property
    def invalidated(self) -> bool:
        """Return True if this connection was invalidated.

        This does not indicate whether or not the connection was
        invalidated at the pool level, however

        """
    @property
    def connection(self) -> PoolProxiedConnection:
        """The underlying DB-API connection managed by this Connection.

        This is a SQLAlchemy connection-pool proxied connection
        which then has the attribute
        :attr:`_pool._ConnectionFairy.dbapi_connection` that refers to the
        actual driver connection.

        .. seealso::


            :ref:`dbapi_connections`

        """
    def get_isolation_level(self) -> IsolationLevel:
        '''Return the current **actual** isolation level that\'s present on
        the database within the scope of this connection.

        This attribute will perform a live SQL operation against the database
        in order to procure the current isolation level, so the value returned
        is the actual level on the underlying DBAPI connection regardless of
        how this state was set. This will be one of the four actual isolation
        modes ``READ UNCOMMITTED``, ``READ COMMITTED``, ``REPEATABLE READ``,
        ``SERIALIZABLE``. It will **not** include the ``AUTOCOMMIT`` isolation
        level setting. Third party dialects may also feature additional
        isolation level settings.

        .. note::  This method **will not report** on the ``AUTOCOMMIT``
          isolation level, which is a separate :term:`dbapi` setting that\'s
          independent of **actual** isolation level.  When ``AUTOCOMMIT`` is
          in use, the database connection still has a "traditional" isolation
          mode in effect, that is typically one of the four values
          ``READ UNCOMMITTED``, ``READ COMMITTED``, ``REPEATABLE READ``,
          ``SERIALIZABLE``.

        Compare to the :attr:`_engine.Connection.default_isolation_level`
        accessor which returns the isolation level that is present on the
        database at initial connection time.

        .. seealso::

            :attr:`_engine.Connection.default_isolation_level`
            - view default level

            :paramref:`_sa.create_engine.isolation_level`
            - set per :class:`_engine.Engine` isolation level

            :paramref:`.Connection.execution_options.isolation_level`
            - set per :class:`_engine.Connection` isolation level

        '''
    @property
    def default_isolation_level(self) -> IsolationLevel | None:
        """The initial-connection time isolation level associated with the
        :class:`_engine.Dialect` in use.

        This value is independent of the
        :paramref:`.Connection.execution_options.isolation_level` and
        :paramref:`.Engine.execution_options.isolation_level` execution
        options, and is determined by the :class:`_engine.Dialect` when the
        first connection is created, by performing a SQL query against the
        database for the current isolation level before any additional commands
        have been emitted.

        Calling this accessor does not invoke any new SQL queries.

        .. seealso::

            :meth:`_engine.Connection.get_isolation_level`
            - view current actual isolation level

            :paramref:`_sa.create_engine.isolation_level`
            - set per :class:`_engine.Engine` isolation level

            :paramref:`.Connection.execution_options.isolation_level`
            - set per :class:`_engine.Connection` isolation level

        """
    @property
    def info(self) -> _InfoType:
        """Info dictionary associated with the underlying DBAPI connection
        referred to by this :class:`_engine.Connection`, allowing user-defined
        data to be associated with the connection.

        The data here will follow along with the DBAPI connection including
        after it is returned to the connection pool and used again
        in subsequent instances of :class:`_engine.Connection`.

        """
    def invalidate(self, exception: BaseException | None = None) -> None:
        '''Invalidate the underlying DBAPI connection associated with
        this :class:`_engine.Connection`.

        An attempt will be made to close the underlying DBAPI connection
        immediately; however if this operation fails, the error is logged
        but not raised.  The connection is then discarded whether or not
        close() succeeded.

        Upon the next use (where "use" typically means using the
        :meth:`_engine.Connection.execute` method or similar),
        this :class:`_engine.Connection` will attempt to
        procure a new DBAPI connection using the services of the
        :class:`_pool.Pool` as a source of connectivity (e.g.
        a "reconnection").

        If a transaction was in progress (e.g. the
        :meth:`_engine.Connection.begin` method has been called) when
        :meth:`_engine.Connection.invalidate` method is called, at the DBAPI
        level all state associated with this transaction is lost, as
        the DBAPI connection is closed.  The :class:`_engine.Connection`
        will not allow a reconnection to proceed until the
        :class:`.Transaction` object is ended, by calling the
        :meth:`.Transaction.rollback` method; until that point, any attempt at
        continuing to use the :class:`_engine.Connection` will raise an
        :class:`~sqlalchemy.exc.InvalidRequestError`.
        This is to prevent applications from accidentally
        continuing an ongoing transactional operations despite the
        fact that the transaction has been lost due to an
        invalidation.

        The :meth:`_engine.Connection.invalidate` method,
        just like auto-invalidation,
        will at the connection pool level invoke the
        :meth:`_events.PoolEvents.invalidate` event.

        :param exception: an optional ``Exception`` instance that\'s the
         reason for the invalidation.  is passed along to event handlers
         and logging functions.

        .. seealso::

            :ref:`pool_connection_invalidation`

        '''
    def detach(self) -> None:
        '''Detach the underlying DB-API connection from its connection pool.

        E.g.::

            with engine.connect() as conn:
                conn.detach()
                conn.execute(text("SET search_path TO schema1, schema2"))

                # work with connection

            # connection is fully closed (since we used "with:", can
            # also call .close())

        This :class:`_engine.Connection` instance will remain usable.
        When closed
        (or exited from a context manager context as above),
        the DB-API connection will be literally closed and not
        returned to its originating pool.

        This method can be used to insulate the rest of an application
        from a modified state on a connection (such as a transaction
        isolation level or similar).

        '''
    def begin(self) -> RootTransaction:
        '''Begin a transaction prior to autobegin occurring.

        E.g.::

            with engine.connect() as conn:
                with conn.begin() as trans:
                    conn.execute(table.insert(), {"username": "sandy"})


        The returned object is an instance of :class:`_engine.RootTransaction`.
        This object represents the "scope" of the transaction,
        which completes when either the :meth:`_engine.Transaction.rollback`
        or :meth:`_engine.Transaction.commit` method is called; the object
        also works as a context manager as illustrated above.

        The :meth:`_engine.Connection.begin` method begins a
        transaction that normally will be begun in any case when the connection
        is first used to execute a statement.  The reason this method might be
        used would be to invoke the :meth:`_events.ConnectionEvents.begin`
        event at a specific time, or to organize code within the scope of a
        connection checkout in terms of context managed blocks, such as::

            with engine.connect() as conn:
                with conn.begin():
                    conn.execute(...)
                    conn.execute(...)

                with conn.begin():
                    conn.execute(...)
                    conn.execute(...)

        The above code is not  fundamentally any different in its behavior than
        the following code  which does not use
        :meth:`_engine.Connection.begin`; the below style is known
        as "commit as you go" style::

            with engine.connect() as conn:
                conn.execute(...)
                conn.execute(...)
                conn.commit()

                conn.execute(...)
                conn.execute(...)
                conn.commit()

        From a database point of view, the :meth:`_engine.Connection.begin`
        method does not emit any SQL or change the state of the underlying
        DBAPI connection in any way; the Python DBAPI does not have any
        concept of explicit transaction begin.

        .. seealso::

            :ref:`tutorial_working_with_transactions` - in the
            :ref:`unified_tutorial`

            :meth:`_engine.Connection.begin_nested` - use a SAVEPOINT

            :meth:`_engine.Connection.begin_twophase` -
            use a two phase /XID transaction

            :meth:`_engine.Engine.begin` - context manager available from
            :class:`_engine.Engine`

        '''
    def begin_nested(self) -> NestedTransaction:
        '''Begin a nested transaction (i.e. SAVEPOINT) and return a transaction
        handle that controls the scope of the SAVEPOINT.

        E.g.::

            with engine.begin() as connection:
                with connection.begin_nested():
                    connection.execute(table.insert(), {"username": "sandy"})

        The returned object is an instance of
        :class:`_engine.NestedTransaction`, which includes transactional
        methods :meth:`_engine.NestedTransaction.commit` and
        :meth:`_engine.NestedTransaction.rollback`; for a nested transaction,
        these methods correspond to the operations "RELEASE SAVEPOINT <name>"
        and "ROLLBACK TO SAVEPOINT <name>". The name of the savepoint is local
        to the :class:`_engine.NestedTransaction` object and is generated
        automatically. Like any other :class:`_engine.Transaction`, the
        :class:`_engine.NestedTransaction` may be used as a context manager as
        illustrated above which will "release" or "rollback" corresponding to
        if the operation within the block were successful or raised an
        exception.

        Nested transactions require SAVEPOINT support in the underlying
        database, else the behavior is undefined. SAVEPOINT is commonly used to
        run operations within a transaction that may fail, while continuing the
        outer transaction. E.g.::

            from sqlalchemy import exc

            with engine.begin() as connection:
                trans = connection.begin_nested()
                try:
                    connection.execute(table.insert(), {"username": "sandy"})
                    trans.commit()
                except exc.IntegrityError:  # catch for duplicate username
                    trans.rollback()  # rollback to savepoint

                # outer transaction continues
                connection.execute( ... )

        If :meth:`_engine.Connection.begin_nested` is called without first
        calling :meth:`_engine.Connection.begin` or
        :meth:`_engine.Engine.begin`, the :class:`_engine.Connection` object
        will "autobegin" the outer transaction first. This outer transaction
        may be committed using "commit-as-you-go" style, e.g.::

            with engine.connect() as connection:  # begin() wasn\'t called

                with connection.begin_nested(): will auto-"begin()" first
                    connection.execute( ... )
                # savepoint is released

                connection.execute( ... )

                # explicitly commit outer transaction
                connection.commit()

                # can continue working with connection here

        .. versionchanged:: 2.0

            :meth:`_engine.Connection.begin_nested` will now participate
            in the connection "autobegin" behavior that is new as of
            2.0 / "future" style connections in 1.4.

        .. seealso::

            :meth:`_engine.Connection.begin`

            :ref:`session_begin_nested` - ORM support for SAVEPOINT

        '''
    def begin_twophase(self, xid: Any | None = None) -> TwoPhaseTransaction:
        """Begin a two-phase or XA transaction and return a transaction
        handle.

        The returned object is an instance of :class:`.TwoPhaseTransaction`,
        which in addition to the methods provided by
        :class:`.Transaction`, also provides a
        :meth:`~.TwoPhaseTransaction.prepare` method.

        :param xid: the two phase transaction id.  If not supplied, a
          random id will be generated.

        .. seealso::

            :meth:`_engine.Connection.begin`

            :meth:`_engine.Connection.begin_twophase`

        """
    def commit(self) -> None:
        """Commit the transaction that is currently in progress.

        This method commits the current transaction if one has been started.
        If no transaction was started, the method has no effect, assuming
        the connection is in a non-invalidated state.

        A transaction is begun on a :class:`_engine.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_engine.Connection.begin` method is called.

        .. note:: The :meth:`_engine.Connection.commit` method only acts upon
          the primary database transaction that is linked to the
          :class:`_engine.Connection` object.  It does not operate upon a
          SAVEPOINT that would have been invoked from the
          :meth:`_engine.Connection.begin_nested` method; for control of a
          SAVEPOINT, call :meth:`_engine.NestedTransaction.commit` on the
          :class:`_engine.NestedTransaction` that is returned by the
          :meth:`_engine.Connection.begin_nested` method itself.


        """
    def rollback(self) -> None:
        """Roll back the transaction that is currently in progress.

        This method rolls back the current transaction if one has been started.
        If no transaction was started, the method has no effect.  If a
        transaction was started and the connection is in an invalidated state,
        the transaction is cleared using this method.

        A transaction is begun on a :class:`_engine.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_engine.Connection.begin` method is called.

        .. note:: The :meth:`_engine.Connection.rollback` method only acts
          upon the primary database transaction that is linked to the
          :class:`_engine.Connection` object.  It does not operate upon a
          SAVEPOINT that would have been invoked from the
          :meth:`_engine.Connection.begin_nested` method; for control of a
          SAVEPOINT, call :meth:`_engine.NestedTransaction.rollback` on the
          :class:`_engine.NestedTransaction` that is returned by the
          :meth:`_engine.Connection.begin_nested` method itself.


        """
    def recover_twophase(self) -> List[Any]: ...
    def rollback_prepared(self, xid: Any, recover: bool = False) -> None: ...
    def commit_prepared(self, xid: Any, recover: bool = False) -> None: ...
    def in_transaction(self) -> bool:
        """Return True if a transaction is in progress."""
    def in_nested_transaction(self) -> bool:
        """Return True if a transaction is in progress."""
    def get_transaction(self) -> RootTransaction | None:
        """Return the current root transaction in progress, if any.

        .. versionadded:: 1.4

        """
    def get_nested_transaction(self) -> NestedTransaction | None:
        """Return the current nested transaction in progress, if any.

        .. versionadded:: 1.4

        """
    def close(self) -> None:
        """Close this :class:`_engine.Connection`.

        This results in a release of the underlying database
        resources, that is, the DBAPI connection referenced
        internally. The DBAPI connection is typically restored
        back to the connection-holding :class:`_pool.Pool` referenced
        by the :class:`_engine.Engine` that produced this
        :class:`_engine.Connection`. Any transactional state present on
        the DBAPI connection is also unconditionally released via
        the DBAPI connection's ``rollback()`` method, regardless
        of any :class:`.Transaction` object that may be
        outstanding with regards to this :class:`_engine.Connection`.

        This has the effect of also calling :meth:`_engine.Connection.rollback`
        if any transaction is in place.

        After :meth:`_engine.Connection.close` is called, the
        :class:`_engine.Connection` is permanently in a closed state,
        and will allow no further operations.

        """
    @overload
    def scalar(self, statement: TypedReturnsRows[Tuple[_T]], parameters: _CoreSingleExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> _T | None: ...
    @overload
    def scalar(self, statement: Executable, parameters: _CoreSingleExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> Any: ...
    @overload
    def scalars(self, statement: TypedReturnsRows[Tuple[_T]], parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> ScalarResult[_T]: ...
    @overload
    def scalars(self, statement: Executable, parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> ScalarResult[Any]: ...
    @overload
    def execute(self, statement: TypedReturnsRows[_T], parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> CursorResult[_T]: ...
    @overload
    def execute(self, statement: Executable, parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> CursorResult[Any]: ...
    def exec_driver_sql(self, statement: str, parameters: _DBAPIAnyExecuteParams | None = None, execution_options: CoreExecuteOptionsParameter | None = None) -> CursorResult[Any]:
        '''Executes a string SQL statement on the DBAPI cursor directly,
        without any SQL compilation steps.

        This can be used to pass any string directly to the
        ``cursor.execute()`` method of the DBAPI in use.

        :param statement: The statement str to be executed.   Bound parameters
         must use the underlying DBAPI\'s paramstyle, such as "qmark",
         "pyformat", "format", etc.

        :param parameters: represent bound parameter values to be used in the
         execution.  The format is one of:   a dictionary of named parameters,
         a tuple of positional parameters, or a list containing either
         dictionaries or tuples for multiple-execute support.

        :return: a :class:`_engine.CursorResult`.

         E.g. multiple dictionaries::


             conn.exec_driver_sql(
                 "INSERT INTO table (id, value) VALUES (%(id)s, %(value)s)",
                 [{"id":1, "value":"v1"}, {"id":2, "value":"v2"}]
             )

         Single dictionary::

             conn.exec_driver_sql(
                 "INSERT INTO table (id, value) VALUES (%(id)s, %(value)s)",
                 dict(id=1, value="v1")
             )

         Single tuple::

             conn.exec_driver_sql(
                 "INSERT INTO table (id, value) VALUES (?, ?)",
                 (1, \'v1\')
             )

         .. note:: The :meth:`_engine.Connection.exec_driver_sql` method does
             not participate in the
             :meth:`_events.ConnectionEvents.before_execute` and
             :meth:`_events.ConnectionEvents.after_execute` events.   To
             intercept calls to :meth:`_engine.Connection.exec_driver_sql`, use
             :meth:`_events.ConnectionEvents.before_cursor_execute` and
             :meth:`_events.ConnectionEvents.after_cursor_execute`.

         .. seealso::

            :pep:`249`

        '''

class ExceptionContextImpl(ExceptionContext):
    """Implement the :class:`.ExceptionContext` interface."""
    engine: Incomplete
    dialect: Incomplete
    connection: Incomplete
    sqlalchemy_exception: Incomplete
    original_exception: Incomplete
    execution_context: Incomplete
    statement: Incomplete
    parameters: Incomplete
    is_disconnect: Incomplete
    invalidate_pool_on_disconnect: Incomplete
    is_pre_ping: Incomplete
    def __init__(self, exception: BaseException, sqlalchemy_exception: exc.StatementError | None, engine: Engine | None, dialect: Dialect, connection: Connection | None, cursor: DBAPICursor | None, statement: str | None, parameters: _DBAPIAnyExecuteParams | None, context: ExecutionContext | None, is_disconnect: bool, invalidate_pool_on_disconnect: bool, is_pre_ping: bool) -> None: ...

class Transaction(TransactionalContext):
    '''Represent a database transaction in progress.

    The :class:`.Transaction` object is procured by
    calling the :meth:`_engine.Connection.begin` method of
    :class:`_engine.Connection`::

        from sqlalchemy import create_engine
        engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/test")
        connection = engine.connect()
        trans = connection.begin()
        connection.execute(text("insert into x (a, b) values (1, 2)"))
        trans.commit()

    The object provides :meth:`.rollback` and :meth:`.commit`
    methods in order to control transaction boundaries.  It
    also implements a context manager interface so that
    the Python ``with`` statement can be used with the
    :meth:`_engine.Connection.begin` method::

        with connection.begin():
            connection.execute(text("insert into x (a, b) values (1, 2)"))

    The Transaction object is **not** threadsafe.

    .. seealso::

        :meth:`_engine.Connection.begin`

        :meth:`_engine.Connection.begin_twophase`

        :meth:`_engine.Connection.begin_nested`

    .. index::
      single: thread safety; Transaction
    '''
    is_active: bool
    connection: Connection
    def __init__(self, connection: Connection) -> None: ...
    @property
    def is_valid(self) -> bool: ...
    def close(self) -> None:
        """Close this :class:`.Transaction`.

        If this transaction is the base transaction in a begin/commit
        nesting, the transaction will rollback().  Otherwise, the
        method returns.

        This is used to cancel a Transaction without affecting the scope of
        an enclosing transaction.

        """
    def rollback(self) -> None:
        '''Roll back this :class:`.Transaction`.

        The implementation of this may vary based on the type of transaction in
        use:

        * For a simple database transaction (e.g. :class:`.RootTransaction`),
          it corresponds to a ROLLBACK.

        * For a :class:`.NestedTransaction`, it corresponds to a
          "ROLLBACK TO SAVEPOINT" operation.

        * For a :class:`.TwoPhaseTransaction`, DBAPI-specific methods for two
          phase transactions may be used.


        '''
    def commit(self) -> None:
        '''Commit this :class:`.Transaction`.

        The implementation of this may vary based on the type of transaction in
        use:

        * For a simple database transaction (e.g. :class:`.RootTransaction`),
          it corresponds to a COMMIT.

        * For a :class:`.NestedTransaction`, it corresponds to a
          "RELEASE SAVEPOINT" operation.

        * For a :class:`.TwoPhaseTransaction`, DBAPI-specific methods for two
          phase transactions may be used.

        '''

class RootTransaction(Transaction):
    '''Represent the "root" transaction on a :class:`_engine.Connection`.

    This corresponds to the current "BEGIN/COMMIT/ROLLBACK" that\'s occurring
    for the :class:`_engine.Connection`. The :class:`_engine.RootTransaction`
    is created by calling upon the :meth:`_engine.Connection.begin` method, and
    remains associated with the :class:`_engine.Connection` throughout its
    active span. The current :class:`_engine.RootTransaction` in use is
    accessible via the :attr:`_engine.Connection.get_transaction` method of
    :class:`_engine.Connection`.

    In :term:`2.0 style` use, the :class:`_engine.Connection` also employs
    "autobegin" behavior that will create a new
    :class:`_engine.RootTransaction` whenever a connection in a
    non-transactional state is used to emit commands on the DBAPI connection.
    The scope of the :class:`_engine.RootTransaction` in 2.0 style
    use can be controlled using the :meth:`_engine.Connection.commit` and
    :meth:`_engine.Connection.rollback` methods.


    '''
    connection: Incomplete
    is_active: bool
    def __init__(self, connection: Connection) -> None: ...

class NestedTransaction(Transaction):
    '''Represent a \'nested\', or SAVEPOINT transaction.

    The :class:`.NestedTransaction` object is created by calling the
    :meth:`_engine.Connection.begin_nested` method of
    :class:`_engine.Connection`.

    When using :class:`.NestedTransaction`, the semantics of "begin" /
    "commit" / "rollback" are as follows:

    * the "begin" operation corresponds to the "BEGIN SAVEPOINT" command, where
      the savepoint is given an explicit name that is part of the state
      of this object.

    * The :meth:`.NestedTransaction.commit` method corresponds to a
      "RELEASE SAVEPOINT" operation, using the savepoint identifier associated
      with this :class:`.NestedTransaction`.

    * The :meth:`.NestedTransaction.rollback` method corresponds to a
      "ROLLBACK TO SAVEPOINT" operation, using the savepoint identifier
      associated with this :class:`.NestedTransaction`.

    The rationale for mimicking the semantics of an outer transaction in
    terms of savepoints so that code may deal with a "savepoint" transaction
    and an "outer" transaction in an agnostic way.

    .. seealso::

        :ref:`session_begin_nested` - ORM version of the SAVEPOINT API.

    '''
    connection: Incomplete
    is_active: bool
    def __init__(self, connection: Connection) -> None: ...

class TwoPhaseTransaction(RootTransaction):
    """Represent a two-phase transaction.

    A new :class:`.TwoPhaseTransaction` object may be procured
    using the :meth:`_engine.Connection.begin_twophase` method.

    The interface is the same as that of :class:`.Transaction`
    with the addition of the :meth:`prepare` method.

    """
    xid: Any
    def __init__(self, connection: Connection, xid: Any) -> None: ...
    def prepare(self) -> None:
        """Prepare this :class:`.TwoPhaseTransaction`.

        After a PREPARE, the transaction can be committed.

        """

class Engine(ConnectionEventsTarget, log.Identified, inspection.Inspectable['Inspector']):
    """
    Connects a :class:`~sqlalchemy.pool.Pool` and
    :class:`~sqlalchemy.engine.interfaces.Dialect` together to provide a
    source of database connectivity and behavior.

    An :class:`_engine.Engine` object is instantiated publicly using the
    :func:`~sqlalchemy.create_engine` function.

    .. seealso::

        :doc:`/core/engines`

        :ref:`connections_toplevel`

    """
    dispatch: dispatcher[ConnectionEventsTarget]
    dialect: Dialect
    pool: Pool
    url: URL
    hide_parameters: bool
    logging_name: Incomplete
    echo: Incomplete
    def __init__(self, pool: Pool, dialect: Dialect, url: URL, logging_name: str | None = None, echo: _EchoFlagType | None = None, query_cache_size: int = 500, execution_options: Mapping[str, Any] | None = None, hide_parameters: bool = False) -> None: ...
    @property
    def engine(self) -> Engine:
        """Returns this :class:`.Engine`.

        Used for legacy schemes that accept :class:`.Connection` /
        :class:`.Engine` objects within the same variable.

        """
    def clear_compiled_cache(self) -> None:
        """Clear the compiled cache associated with the dialect.

        This applies **only** to the built-in cache that is established
        via the :paramref:`_engine.create_engine.query_cache_size` parameter.
        It will not impact any dictionary caches that were passed via the
        :paramref:`.Connection.execution_options.query_cache` parameter.

        .. versionadded:: 1.4

        """
    def update_execution_options(self, **opt: Any) -> None:
        """Update the default execution_options dictionary
        of this :class:`_engine.Engine`.

        The given keys/values in \\**opt are added to the
        default execution options that will be used for
        all connections.  The initial contents of this dictionary
        can be sent via the ``execution_options`` parameter
        to :func:`_sa.create_engine`.

        .. seealso::

            :meth:`_engine.Connection.execution_options`

            :meth:`_engine.Engine.execution_options`

        """
    @overload
    def execution_options(self, *, compiled_cache: CompiledCacheType | None = ..., logging_token: str = ..., isolation_level: IsolationLevel = ..., insertmanyvalues_page_size: int = ..., schema_translate_map: SchemaTranslateMapType | None = ..., **opt: Any) -> OptionEngine: ...
    @overload
    def execution_options(self, **opt: Any) -> OptionEngine: ...
    def get_execution_options(self) -> _ExecuteOptions:
        """Get the non-SQL options which will take effect during execution.

        .. versionadded: 1.3

        .. seealso::

            :meth:`_engine.Engine.execution_options`
        """
    @property
    def name(self) -> str:
        """String name of the :class:`~sqlalchemy.engine.interfaces.Dialect`
        in use by this :class:`Engine`.

        """
    @property
    def driver(self) -> str:
        """Driver name of the :class:`~sqlalchemy.engine.interfaces.Dialect`
        in use by this :class:`Engine`.

        """
    def dispose(self, close: bool = True) -> None:
        """Dispose of the connection pool used by this
        :class:`_engine.Engine`.

        A new connection pool is created immediately after the old one has been
        disposed. The previous connection pool is disposed either actively, by
        closing out all currently checked-in connections in that pool, or
        passively, by losing references to it but otherwise not closing any
        connections. The latter strategy is more appropriate for an initializer
        in a forked Python process.

        :param close: if left at its default of ``True``, has the
         effect of fully closing all **currently checked in**
         database connections.  Connections that are still checked out
         will **not** be closed, however they will no longer be associated
         with this :class:`_engine.Engine`,
         so when they are closed individually, eventually the
         :class:`_pool.Pool` which they are associated with will
         be garbage collected and they will be closed out fully, if
         not already closed on checkin.

         If set to ``False``, the previous connection pool is de-referenced,
         and otherwise not touched in any way.

        .. versionadded:: 1.4.33  Added the :paramref:`.Engine.dispose.close`
            parameter to allow the replacement of a connection pool in a child
            process without interfering with the connections used by the parent
            process.


        .. seealso::

            :ref:`engine_disposal`

            :ref:`pooling_multiprocessing`

        """
    def begin(self) -> Iterator[Connection]:
        '''Return a context manager delivering a :class:`_engine.Connection`
        with a :class:`.Transaction` established.

        E.g.::

            with engine.begin() as conn:
                conn.execute(
                    text("insert into table (x, y, z) values (1, 2, 3)")
                )
                conn.execute(text("my_special_procedure(5)"))

        Upon successful operation, the :class:`.Transaction`
        is committed.  If an error is raised, the :class:`.Transaction`
        is rolled back.

        .. seealso::

            :meth:`_engine.Engine.connect` - procure a
            :class:`_engine.Connection` from
            an :class:`_engine.Engine`.

            :meth:`_engine.Connection.begin` - start a :class:`.Transaction`
            for a particular :class:`_engine.Connection`.

        '''
    def connect(self) -> Connection:
        '''Return a new :class:`_engine.Connection` object.

        The :class:`_engine.Connection` acts as a Python context manager, so
        the typical use of this method looks like::

            with engine.connect() as connection:
                connection.execute(text("insert into table values (\'foo\')"))
                connection.commit()

        Where above, after the block is completed, the connection is "closed"
        and its underlying DBAPI resources are returned to the connection pool.
        This also has the effect of rolling back any transaction that
        was explicitly begun or was begun via autobegin, and will
        emit the :meth:`_events.ConnectionEvents.rollback` event if one was
        started and is still in progress.

        .. seealso::

            :meth:`_engine.Engine.begin`

        '''
    def raw_connection(self) -> PoolProxiedConnection:
        '''Return a "raw" DBAPI connection from the connection pool.

        The returned object is a proxied version of the DBAPI
        connection object used by the underlying driver in use.
        The object will have all the same behavior as the real DBAPI
        connection, except that its ``close()`` method will result in the
        connection being returned to the pool, rather than being closed
        for real.

        This method provides direct DBAPI connection access for
        special situations when the API provided by
        :class:`_engine.Connection`
        is not needed.   When a :class:`_engine.Connection` object is already
        present, the DBAPI connection is available using
        the :attr:`_engine.Connection.connection` accessor.

        .. seealso::

            :ref:`dbapi_connections`

        '''

class OptionEngineMixin(log.Identified):
    dispatch: dispatcher[ConnectionEventsTarget]
    dialect: Dialect
    pool: Pool
    url: URL
    hide_parameters: bool
    echo: log.echo_property
    logging_name: Incomplete
    def __init__(self, proxied: Engine, execution_options: CoreExecuteOptionsParameter) -> None: ...
    def update_execution_options(self, **opt: Any) -> None: ...

class OptionEngine(OptionEngineMixin, Engine):
    def update_execution_options(self, **opt: Any) -> None: ...
