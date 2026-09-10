from ... import exc as exc, inspection as inspection, util as util
from ...engine import Connection as Connection, Engine as Engine
from ...engine.base import NestedTransaction as NestedTransaction, Transaction as Transaction
from ...engine.cursor import CursorResult as CursorResult
from ...engine.interfaces import CompiledCacheType as CompiledCacheType, CoreExecuteOptionsParameter as CoreExecuteOptionsParameter, Dialect as Dialect, IsolationLevel as IsolationLevel, SchemaTranslateMapType as SchemaTranslateMapType, _CoreAnyExecuteParams, _CoreSingleExecuteParams, _DBAPIAnyExecuteParams, _ExecuteOptions
from ...engine.result import ScalarResult as ScalarResult
from ...engine.url import URL as URL
from ...exc import ArgumentError as ArgumentError
from ...pool import Pool as Pool, PoolProxiedConnection as PoolProxiedConnection
from ...sql._typing import _InfoType
from ...sql.base import Executable as Executable
from ...sql.selectable import TypedReturnsRows as TypedReturnsRows
from ...util.concurrency import greenlet_spawn as greenlet_spawn
from .base import GeneratorStartableContext as GeneratorStartableContext, ProxyComparable as ProxyComparable, StartableContext as StartableContext, asyncstartablecontext as asyncstartablecontext
from .result import AsyncResult as AsyncResult, AsyncScalarResult as AsyncScalarResult
from _typeshed import Incomplete
from typing import Any, AsyncIterator, Callable, Dict, Generator, NoReturn, Tuple, overload

def create_async_engine(url: str | URL, **kw: Any) -> AsyncEngine:
    """Create a new async engine instance.

    Arguments passed to :func:`_asyncio.create_async_engine` are mostly
    identical to those passed to the :func:`_sa.create_engine` function.
    The specified dialect must be an asyncio-compatible dialect
    such as :ref:`dialect-postgresql-asyncpg`.

    .. versionadded:: 1.4

    :param async_creator: an async callable which returns a driver-level
        asyncio connection. If given, the function should take no arguments,
        and return a new asyncio connection from the underlying asyncio
        database driver; the connection will be wrapped in the appropriate
        structures to be used with the :class:`.AsyncEngine`.   Note that the
        parameters specified in the URL are not applied here, and the creator
        function should use its own connection parameters.

        This parameter is the asyncio equivalent of the
        :paramref:`_sa.create_engine.creator` parameter of the
        :func:`_sa.create_engine` function.

        .. versionadded:: 2.0.16

    """
def async_engine_from_config(configuration: Dict[str, Any], prefix: str = 'sqlalchemy.', **kwargs: Any) -> AsyncEngine:
    """Create a new AsyncEngine instance using a configuration dictionary.

    This function is analogous to the :func:`_sa.engine_from_config` function
    in SQLAlchemy Core, except that the requested dialect must be an
    asyncio-compatible dialect such as :ref:`dialect-postgresql-asyncpg`.
    The argument signature of the function is identical to that
    of :func:`_sa.engine_from_config`.

    .. versionadded:: 1.4.29

    """
def create_async_pool_from_url(url: str | URL, **kwargs: Any) -> Pool:
    """Create a new async engine instance.

    Arguments passed to :func:`_asyncio.create_async_pool_from_url` are mostly
    identical to those passed to the :func:`_sa.create_pool_from_url` function.
    The specified dialect must be an asyncio-compatible dialect
    such as :ref:`dialect-postgresql-asyncpg`.

    .. versionadded:: 2.0.10

    """

class AsyncConnectable: ...

class AsyncConnection(ProxyComparable[Connection], StartableContext['AsyncConnection'], AsyncConnectable):
    '''An asyncio proxy for a :class:`_engine.Connection`.

    :class:`_asyncio.AsyncConnection` is acquired using the
    :meth:`_asyncio.AsyncEngine.connect`
    method of :class:`_asyncio.AsyncEngine`::

        from sqlalchemy.ext.asyncio import create_async_engine
        engine = create_async_engine("postgresql+asyncpg://user:pass@host/dbname")

        async with engine.connect() as conn:
            result = await conn.execute(select(table))

    .. versionadded:: 1.4

    '''
    engine: Incomplete
    sync_engine: Incomplete
    sync_connection: Incomplete
    def __init__(self, async_engine: AsyncEngine, sync_connection: Connection | None = None) -> None: ...
    async def start(self, is_ctxmanager: bool = False) -> AsyncConnection:
        """Start this :class:`_asyncio.AsyncConnection` object's context
        outside of using a Python ``with:`` block.

        """
    @property
    def connection(self) -> NoReturn:
        """Not implemented for async; call
        :meth:`_asyncio.AsyncConnection.get_raw_connection`.
        """
    async def get_raw_connection(self) -> PoolProxiedConnection:
        """Return the pooled DBAPI-level connection in use by this
        :class:`_asyncio.AsyncConnection`.

        This is a SQLAlchemy connection-pool proxied connection
        which then has the attribute
        :attr:`_pool._ConnectionFairy.driver_connection` that refers to the
        actual driver connection. Its
        :attr:`_pool._ConnectionFairy.dbapi_connection` refers instead
        to an :class:`_engine.AdaptedConnection` instance that
        adapts the driver connection to the DBAPI protocol.

        """
    def info(self) -> _InfoType:
        """Return the :attr:`_engine.Connection.info` dictionary of the
        underlying :class:`_engine.Connection`.

        This dictionary is freely writable for user-defined state to be
        associated with the database connection.

        This attribute is only available if the :class:`.AsyncConnection` is
        currently connected.   If the :attr:`.AsyncConnection.closed` attribute
        is ``True``, then accessing this attribute will raise
        :class:`.ResourceClosedError`.

        .. versionadded:: 1.4.0b2

        """
    def begin(self) -> AsyncTransaction:
        """Begin a transaction prior to autobegin occurring."""
    def begin_nested(self) -> AsyncTransaction:
        """Begin a nested transaction and return a transaction handle."""
    async def invalidate(self, exception: BaseException | None = None) -> None:
        """Invalidate the underlying DBAPI connection associated with
        this :class:`_engine.Connection`.

        See the method :meth:`_engine.Connection.invalidate` for full
        detail on this method.

        """
    async def get_isolation_level(self) -> IsolationLevel: ...
    def in_transaction(self) -> bool:
        """Return True if a transaction is in progress."""
    def in_nested_transaction(self) -> bool:
        """Return True if a transaction is in progress.

        .. versionadded:: 1.4.0b2

        """
    def get_transaction(self) -> AsyncTransaction | None:
        """Return an :class:`.AsyncTransaction` representing the current
        transaction, if any.

        This makes use of the underlying synchronous connection's
        :meth:`_engine.Connection.get_transaction` method to get the current
        :class:`_engine.Transaction`, which is then proxied in a new
        :class:`.AsyncTransaction` object.

        .. versionadded:: 1.4.0b2

        """
    def get_nested_transaction(self) -> AsyncTransaction | None:
        """Return an :class:`.AsyncTransaction` representing the current
        nested (savepoint) transaction, if any.

        This makes use of the underlying synchronous connection's
        :meth:`_engine.Connection.get_nested_transaction` method to get the
        current :class:`_engine.Transaction`, which is then proxied in a new
        :class:`.AsyncTransaction` object.

        .. versionadded:: 1.4.0b2

        """
    @overload
    async def execution_options(self, *, compiled_cache: CompiledCacheType | None = ..., logging_token: str = ..., isolation_level: IsolationLevel = ..., no_parameters: bool = False, stream_results: bool = False, max_row_buffer: int = ..., yield_per: int = ..., insertmanyvalues_page_size: int = ..., schema_translate_map: SchemaTranslateMapType | None = ..., **opt: Any) -> AsyncConnection: ...
    @overload
    async def execution_options(self, **opt: Any) -> AsyncConnection: ...
    async def commit(self) -> None:
        """Commit the transaction that is currently in progress.

        This method commits the current transaction if one has been started.
        If no transaction was started, the method has no effect, assuming
        the connection is in a non-invalidated state.

        A transaction is begun on a :class:`_engine.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_engine.Connection.begin` method is called.

        """
    async def rollback(self) -> None:
        """Roll back the transaction that is currently in progress.

        This method rolls back the current transaction if one has been started.
        If no transaction was started, the method has no effect.  If a
        transaction was started and the connection is in an invalidated state,
        the transaction is cleared using this method.

        A transaction is begun on a :class:`_engine.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_engine.Connection.begin` method is called.


        """
    async def close(self) -> None:
        """Close this :class:`_asyncio.AsyncConnection`.

        This has the effect of also rolling back the transaction if one
        is in place.

        """
    async def aclose(self) -> None:
        """A synonym for :meth:`_asyncio.AsyncConnection.close`.

        The :meth:`_asyncio.AsyncConnection.aclose` name is specifically
        to support the Python standard library ``@contextlib.aclosing``
        context manager function.

        .. versionadded:: 2.0.20

        """
    async def exec_driver_sql(self, statement: str, parameters: _DBAPIAnyExecuteParams | None = None, execution_options: CoreExecuteOptionsParameter | None = None) -> CursorResult[Any]:
        """Executes a driver-level SQL string and return buffered
        :class:`_engine.Result`.

        """
    @overload
    def stream(self, statement: TypedReturnsRows[_T], parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> GeneratorStartableContext[AsyncResult[_T]]: ...
    @overload
    def stream(self, statement: Executable, parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> GeneratorStartableContext[AsyncResult[Any]]: ...
    @overload
    async def execute(self, statement: TypedReturnsRows[_T], parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> CursorResult[_T]: ...
    @overload
    async def execute(self, statement: Executable, parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> CursorResult[Any]: ...
    @overload
    async def scalar(self, statement: TypedReturnsRows[Tuple[_T]], parameters: _CoreSingleExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> _T | None: ...
    @overload
    async def scalar(self, statement: Executable, parameters: _CoreSingleExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> Any: ...
    @overload
    async def scalars(self, statement: TypedReturnsRows[Tuple[_T]], parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> ScalarResult[_T]: ...
    @overload
    async def scalars(self, statement: Executable, parameters: _CoreAnyExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> ScalarResult[Any]: ...
    @overload
    def stream_scalars(self, statement: TypedReturnsRows[Tuple[_T]], parameters: _CoreSingleExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> GeneratorStartableContext[AsyncScalarResult[_T]]: ...
    @overload
    def stream_scalars(self, statement: Executable, parameters: _CoreSingleExecuteParams | None = None, *, execution_options: CoreExecuteOptionsParameter | None = None) -> GeneratorStartableContext[AsyncScalarResult[Any]]: ...
    async def run_sync(self, fn: Callable[..., _T], *arg: Any, **kw: Any) -> _T:
        '''Invoke the given synchronous (i.e. not async) callable,
        passing a synchronous-style :class:`_engine.Connection` as the first
        argument.

        This method allows traditional synchronous SQLAlchemy functions to
        run within the context of an asyncio application.

        E.g.::

            def do_something_with_core(conn: Connection, arg1: int, arg2: str) -> str:
                \'\'\'A synchronous function that does not require awaiting

                :param conn: a Core SQLAlchemy Connection, used synchronously

                :return: an optional return value is supported

                \'\'\'
                conn.execute(
                    some_table.insert().values(int_col=arg1, str_col=arg2)
                )
                return "success"


            async def do_something_async(async_engine: AsyncEngine) -> None:
                \'\'\'an async function that uses awaiting\'\'\'

                async with async_engine.begin() as async_conn:
                    # run do_something_with_core() with a sync-style
                    # Connection, proxied into an awaitable
                    return_code = await async_conn.run_sync(do_something_with_core, 5, "strval")
                    print(return_code)

        This method maintains the asyncio event loop all the way through
        to the database connection by running the given callable in a
        specially instrumented greenlet.

        The most rudimentary use of :meth:`.AsyncConnection.run_sync` is to
        invoke methods such as :meth:`_schema.MetaData.create_all`, given
        an :class:`.AsyncConnection` that needs to be provided to
        :meth:`_schema.MetaData.create_all` as a :class:`_engine.Connection`
        object::

            # run metadata.create_all(conn) with a sync-style Connection,
            # proxied into an awaitable
            with async_engine.begin() as conn:
                await conn.run_sync(metadata.create_all)

        .. note::

            The provided callable is invoked inline within the asyncio event
            loop, and will block on traditional IO calls.  IO within this
            callable should only call into SQLAlchemy\'s asyncio database
            APIs which will be properly adapted to the greenlet context.

        .. seealso::

            :meth:`.AsyncSession.run_sync`

            :ref:`session_run_sync`

        '''
    def __await__(self) -> Generator[Any, None, AsyncConnection]: ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    @property
    def closed(self) -> Any:
        """Return True if this connection is closed.

        .. container:: class_bases

            Proxied for the :class:`_engine.Connection` class
            on behalf of the :class:`_asyncio.AsyncConnection` class.

        """
    @property
    def invalidated(self) -> Any:
        """Return True if this connection was invalidated.

        .. container:: class_bases

            Proxied for the :class:`_engine.Connection` class
            on behalf of the :class:`_asyncio.AsyncConnection` class.

        This does not indicate whether or not the connection was
        invalidated at the pool level, however


        """
    @property
    def dialect(self) -> Any:
        """Proxy for the :attr:`_engine.Connection.dialect` attribute
        on behalf of the :class:`_asyncio.AsyncConnection` class.

        """
    @dialect.setter
    def dialect(self, attr: Any) -> None: ...
    @property
    def default_isolation_level(self) -> Any:
        """The initial-connection time isolation level associated with the
        :class:`_engine.Dialect` in use.

        .. container:: class_bases

            Proxied for the :class:`_engine.Connection` class
            on behalf of the :class:`_asyncio.AsyncConnection` class.

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

class AsyncEngine(ProxyComparable[Engine], AsyncConnectable):
    '''An asyncio proxy for a :class:`_engine.Engine`.

    :class:`_asyncio.AsyncEngine` is acquired using the
    :func:`_asyncio.create_async_engine` function::

        from sqlalchemy.ext.asyncio import create_async_engine
        engine = create_async_engine("postgresql+asyncpg://user:pass@host/dbname")

    .. versionadded:: 1.4

    '''
    sync_engine: Engine
    def __init__(self, sync_engine: Engine) -> None: ...
    async def begin(self) -> AsyncIterator[AsyncConnection]:
        '''Return a context manager which when entered will deliver an
        :class:`_asyncio.AsyncConnection` with an
        :class:`_asyncio.AsyncTransaction` established.

        E.g.::

            async with async_engine.begin() as conn:
                await conn.execute(
                    text("insert into table (x, y, z) values (1, 2, 3)")
                )
                await conn.execute(text("my_special_procedure(5)"))


        '''
    def connect(self) -> AsyncConnection:
        """Return an :class:`_asyncio.AsyncConnection` object.

        The :class:`_asyncio.AsyncConnection` will procure a database
        connection from the underlying connection pool when it is entered
        as an async context manager::

            async with async_engine.connect() as conn:
                result = await conn.execute(select(user_table))

        The :class:`_asyncio.AsyncConnection` may also be started outside of a
        context manager by invoking its :meth:`_asyncio.AsyncConnection.start`
        method.

        """
    async def raw_connection(self) -> PoolProxiedConnection:
        '''Return a "raw" DBAPI connection from the connection pool.

        .. seealso::

            :ref:`dbapi_connections`

        '''
    @overload
    def execution_options(self, *, compiled_cache: CompiledCacheType | None = ..., logging_token: str = ..., isolation_level: IsolationLevel = ..., insertmanyvalues_page_size: int = ..., schema_translate_map: SchemaTranslateMapType | None = ..., **opt: Any) -> AsyncEngine: ...
    @overload
    def execution_options(self, **opt: Any) -> AsyncEngine: ...
    async def dispose(self, close: bool = True) -> None:
        """Dispose of the connection pool used by this
        :class:`_asyncio.AsyncEngine`.

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

        .. seealso::

            :meth:`_engine.Engine.dispose`

        """
    def clear_compiled_cache(self) -> None:
        """Clear the compiled cache associated with the dialect.

        .. container:: class_bases

            Proxied for the :class:`_engine.Engine` class on
            behalf of the :class:`_asyncio.AsyncEngine` class.

        This applies **only** to the built-in cache that is established
        via the :paramref:`_engine.create_engine.query_cache_size` parameter.
        It will not impact any dictionary caches that were passed via the
        :paramref:`.Connection.execution_options.query_cache` parameter.

        .. versionadded:: 1.4


        """
    def update_execution_options(self, **opt: Any) -> None:
        """Update the default execution_options dictionary
        of this :class:`_engine.Engine`.

        .. container:: class_bases

            Proxied for the :class:`_engine.Engine` class on
            behalf of the :class:`_asyncio.AsyncEngine` class.

        The given keys/values in \\**opt are added to the
        default execution options that will be used for
        all connections.  The initial contents of this dictionary
        can be sent via the ``execution_options`` parameter
        to :func:`_sa.create_engine`.

        .. seealso::

            :meth:`_engine.Connection.execution_options`

            :meth:`_engine.Engine.execution_options`


        """
    def get_execution_options(self) -> _ExecuteOptions:
        """Get the non-SQL options which will take effect during execution.

        .. container:: class_bases

            Proxied for the :class:`_engine.Engine` class on
            behalf of the :class:`_asyncio.AsyncEngine` class.

        .. versionadded: 1.3

        .. seealso::

            :meth:`_engine.Engine.execution_options`

        """
    @property
    def url(self) -> URL:
        """Proxy for the :attr:`_engine.Engine.url` attribute
        on behalf of the :class:`_asyncio.AsyncEngine` class.

        """
    @url.setter
    def url(self, attr: URL) -> None: ...
    @property
    def pool(self) -> Pool:
        """Proxy for the :attr:`_engine.Engine.pool` attribute
        on behalf of the :class:`_asyncio.AsyncEngine` class.

        """
    @pool.setter
    def pool(self, attr: Pool) -> None: ...
    @property
    def dialect(self) -> Dialect:
        """Proxy for the :attr:`_engine.Engine.dialect` attribute
        on behalf of the :class:`_asyncio.AsyncEngine` class.

        """
    @dialect.setter
    def dialect(self, attr: Dialect) -> None: ...
    @property
    def engine(self) -> Any:
        """Returns this :class:`.Engine`.

        .. container:: class_bases

            Proxied for the :class:`_engine.Engine` class
            on behalf of the :class:`_asyncio.AsyncEngine` class.

        Used for legacy schemes that accept :class:`.Connection` /
        :class:`.Engine` objects within the same variable.


        """
    @property
    def name(self) -> Any:
        """String name of the :class:`~sqlalchemy.engine.interfaces.Dialect`
        in use by this :class:`Engine`.

        .. container:: class_bases

            Proxied for the :class:`_engine.Engine` class
            on behalf of the :class:`_asyncio.AsyncEngine` class.


        """
    @property
    def driver(self) -> Any:
        """Driver name of the :class:`~sqlalchemy.engine.interfaces.Dialect`
        in use by this :class:`Engine`.

        .. container:: class_bases

            Proxied for the :class:`_engine.Engine` class
            on behalf of the :class:`_asyncio.AsyncEngine` class.


        """
    @property
    def echo(self) -> Any:
        """When ``True``, enable log output for this element.

        .. container:: class_bases

            Proxied for the :class:`_engine.Engine` class
            on behalf of the :class:`_asyncio.AsyncEngine` class.

        This has the effect of setting the Python logging level for the namespace
        of this element's class and object reference.  A value of boolean ``True``
        indicates that the loglevel ``logging.INFO`` will be set for the logger,
        whereas the string value ``debug`` will set the loglevel to
        ``logging.DEBUG``.

        """
    @echo.setter
    def echo(self, attr: Any) -> None: ...

class AsyncTransaction(ProxyComparable[Transaction], StartableContext['AsyncTransaction']):
    """An asyncio proxy for a :class:`_engine.Transaction`."""
    sync_transaction: Transaction | None
    connection: AsyncConnection
    nested: bool
    def __init__(self, connection: AsyncConnection, nested: bool = False) -> None: ...
    @property
    def is_valid(self) -> bool: ...
    @property
    def is_active(self) -> bool: ...
    async def close(self) -> None:
        """Close this :class:`.AsyncTransaction`.

        If this transaction is the base transaction in a begin/commit
        nesting, the transaction will rollback().  Otherwise, the
        method returns.

        This is used to cancel a Transaction without affecting the scope of
        an enclosing transaction.

        """
    async def rollback(self) -> None:
        """Roll back this :class:`.AsyncTransaction`."""
    async def commit(self) -> None:
        """Commit this :class:`.AsyncTransaction`."""
    async def start(self, is_ctxmanager: bool = False) -> AsyncTransaction:
        """Start this :class:`_asyncio.AsyncTransaction` object's context
        outside of using a Python ``with:`` block.

        """
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
