import dataclasses
import weakref
from .. import event as event, exc as exc, log as log, util as util
from ..engine.interfaces import DBAPIConnection as DBAPIConnection, DBAPICursor as DBAPICursor, Dialect as Dialect
from ..event import _DispatchCommon, _ListenerFnType, dispatcher as dispatcher
from ..sql._typing import _InfoType
from ..util.typing import Literal as Literal, Protocol as Protocol
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Callable, Deque, List, Tuple

@dataclasses.dataclass(frozen=True)
class PoolResetState:
    """describes the state of a DBAPI connection as it is being passed to
    the :meth:`.PoolEvents.reset` connection pool event.

    .. versionadded:: 2.0.0b3

    """
    transaction_was_reset: bool
    terminate_only: bool
    asyncio_safe: bool
    def __init__(self, transaction_was_reset, terminate_only, asyncio_safe) -> None: ...

class ResetStyle(Enum):
    '''Describe options for "reset on return" behaviors.'''
    reset_rollback: int
    reset_commit: int
    reset_none: int

reset_rollback: Incomplete
reset_commit: Incomplete
reset_none: Incomplete

class _ConnDialect:
    """partial implementation of :class:`.Dialect`
    which provides DBAPI connection methods.

    When a :class:`_pool.Pool` is combined with an :class:`_engine.Engine`,
    the :class:`_engine.Engine` replaces this with its own
    :class:`.Dialect`.

    """
    is_async: bool
    has_terminate: bool
    def do_rollback(self, dbapi_connection: PoolProxiedConnection) -> None: ...
    def do_commit(self, dbapi_connection: PoolProxiedConnection) -> None: ...
    def do_terminate(self, dbapi_connection: DBAPIConnection) -> None: ...
    def do_close(self, dbapi_connection: DBAPIConnection) -> None: ...
    def get_driver_connection(self, connection: DBAPIConnection) -> Any: ...

class _AsyncConnDialect(_ConnDialect):
    is_async: bool

class _CreatorFnType(Protocol):
    def __call__(self) -> DBAPIConnection: ...

class _CreatorWRecFnType(Protocol):
    def __call__(self, rec: ConnectionPoolEntry) -> DBAPIConnection: ...

class Pool(log.Identified, event.EventTarget):
    """Abstract base class for connection pools."""
    dispatch: dispatcher[Pool]
    echo: log._EchoFlagType
    logging_name: Incomplete
    def __init__(self, creator: _CreatorFnType | _CreatorWRecFnType, recycle: int = -1, echo: log._EchoFlagType = None, logging_name: str | None = None, reset_on_return: _ResetStyleArgType = True, events: List[Tuple[_ListenerFnType, str]] | None = None, dialect: _ConnDialect | Dialect | None = None, pre_ping: bool = False, _dispatch: _DispatchCommon[Pool] | None = None) -> None:
        '''
        Construct a Pool.

        :param creator: a callable function that returns a DB-API
          connection object.  The function will be called with
          parameters.

        :param recycle: If set to a value other than -1, number of
          seconds between connection recycling, which means upon
          checkout, if this timeout is surpassed the connection will be
          closed and replaced with a newly opened connection. Defaults to -1.

        :param logging_name:  String identifier which will be used within
          the "name" field of logging records generated within the
          "sqlalchemy.pool" logger. Defaults to a hexstring of the object\'s
          id.

        :param echo: if True, the connection pool will log
         informational output such as when connections are invalidated
         as well as when connections are recycled to the default log handler,
         which defaults to ``sys.stdout`` for output..   If set to the string
         ``"debug"``, the logging will include pool checkouts and checkins.

         The :paramref:`_pool.Pool.echo` parameter can also be set from the
         :func:`_sa.create_engine` call by using the
         :paramref:`_sa.create_engine.echo_pool` parameter.

         .. seealso::

             :ref:`dbengine_logging` - further detail on how to configure
             logging.

        :param reset_on_return: Determine steps to take on
         connections as they are returned to the pool, which were
         not otherwise handled by a :class:`_engine.Connection`.
         Available from :func:`_sa.create_engine` via the
         :paramref:`_sa.create_engine.pool_reset_on_return` parameter.

         :paramref:`_pool.Pool.reset_on_return` can have any of these values:

         * ``"rollback"`` - call rollback() on the connection,
           to release locks and transaction resources.
           This is the default value.  The vast majority
           of use cases should leave this value set.
         * ``"commit"`` - call commit() on the connection,
           to release locks and transaction resources.
           A commit here may be desirable for databases that
           cache query plans if a commit is emitted,
           such as Microsoft SQL Server.  However, this
           value is more dangerous than \'rollback\' because
           any data changes present on the transaction
           are committed unconditionally.
         * ``None`` - don\'t do anything on the connection.
           This setting may be appropriate if the database / DBAPI
           works in pure "autocommit" mode at all times, or if
           a custom reset handler is established using the
           :meth:`.PoolEvents.reset` event handler.

         * ``True`` - same as \'rollback\', this is here for
           backwards compatibility.
         * ``False`` - same as None, this is here for
           backwards compatibility.

         For further customization of reset on return, the
         :meth:`.PoolEvents.reset` event hook may be used which can perform
         any connection activity desired on reset.

         .. seealso::

            :ref:`pool_reset_on_return`

            :meth:`.PoolEvents.reset`

        :param events: a list of 2-tuples, each of the form
         ``(callable, target)`` which will be passed to :func:`.event.listen`
         upon construction.   Provided here so that event listeners
         can be assigned via :func:`_sa.create_engine` before dialect-level
         listeners are applied.

        :param dialect: a :class:`.Dialect` that will handle the job
         of calling rollback(), close(), or commit() on DBAPI connections.
         If omitted, a built-in "stub" dialect is used.   Applications that
         make use of :func:`_sa.create_engine` should not use this parameter
         as it is handled by the engine creation strategy.

        :param pre_ping: if True, the pool will emit a "ping" (typically
         "SELECT 1", but is dialect-specific) on the connection
         upon checkout, to test if the connection is alive or not.   If not,
         the connection is transparently re-connected and upon success, all
         other pooled connections established prior to that timestamp are
         invalidated.     Requires that a dialect is passed as well to
         interpret the disconnection error.

         .. versionadded:: 1.2

        '''
    def recreate(self) -> Pool:
        """Return a new :class:`_pool.Pool`, of the same class as this one
        and configured with identical creation arguments.

        This method is used in conjunction with :meth:`dispose`
        to close out an entire :class:`_pool.Pool` and create a new one in
        its place.

        """
    def dispose(self) -> None:
        """Dispose of this pool.

        This method leaves the possibility of checked-out connections
        remaining open, as it only affects connections that are
        idle in the pool.

        .. seealso::

            :meth:`Pool.recreate`

        """
    def connect(self) -> PoolProxiedConnection:
        """Return a DBAPI connection from the pool.

        The connection is instrumented such that when its
        ``close()`` method is called, the connection will be returned to
        the pool.

        """
    def status(self) -> str: ...

class ManagesConnection:
    """Common base for the two connection-management interfaces
    :class:`.PoolProxiedConnection` and :class:`.ConnectionPoolEntry`.

    These two objects are typically exposed in the public facing API
    via the connection pool event hooks, documented at :class:`.PoolEvents`.

    .. versionadded:: 2.0

    """
    dbapi_connection: DBAPIConnection | None
    driver_connection: Any | None
    def info(self) -> _InfoType:
        """Info dictionary associated with the underlying DBAPI connection
        referred to by this :class:`.ManagesConnection` instance, allowing
        user-defined data to be associated with the connection.

        The data in this dictionary is persistent for the lifespan
        of the DBAPI connection itself, including across pool checkins
        and checkouts.  When the connection is invalidated
        and replaced with a new one, this dictionary is cleared.

        For a :class:`.PoolProxiedConnection` instance that's not associated
        with a :class:`.ConnectionPoolEntry`, such as if it were detached, the
        attribute returns a dictionary that is local to that
        :class:`.ConnectionPoolEntry`. Therefore the
        :attr:`.ManagesConnection.info` attribute will always provide a Python
        dictionary.

        .. seealso::

            :attr:`.ManagesConnection.record_info`


        """
    def record_info(self) -> _InfoType | None:
        """Persistent info dictionary associated with this
        :class:`.ManagesConnection`.

        Unlike the :attr:`.ManagesConnection.info` dictionary, the lifespan
        of this dictionary is that of the :class:`.ConnectionPoolEntry`
        which owns it; therefore this dictionary will persist across
        reconnects and connection invalidation for a particular entry
        in the connection pool.

        For a :class:`.PoolProxiedConnection` instance that's not associated
        with a :class:`.ConnectionPoolEntry`, such as if it were detached, the
        attribute returns None. Contrast to the :attr:`.ManagesConnection.info`
        dictionary which is never None.


        .. seealso::

            :attr:`.ManagesConnection.info`

        """
    def invalidate(self, e: BaseException | None = None, soft: bool = False) -> None:
        """Mark the managed connection as invalidated.

        :param e: an exception object indicating a reason for the invalidation.

        :param soft: if True, the connection isn't closed; instead, this
         connection will be recycled on next checkout.

        .. seealso::

            :ref:`pool_connection_invalidation`


        """

class ConnectionPoolEntry(ManagesConnection):
    '''Interface for the object that maintains an individual database
    connection on behalf of a :class:`_pool.Pool` instance.

    The :class:`.ConnectionPoolEntry` object represents the long term
    maintainance of a particular connection for a pool, including expiring or
    invalidating that connection to have it replaced with a new one, which will
    continue to be maintained by that same :class:`.ConnectionPoolEntry`
    instance. Compared to :class:`.PoolProxiedConnection`, which is the
    short-term, per-checkout connection manager, this object lasts for the
    lifespan of a particular "slot" within a connection pool.

    The :class:`.ConnectionPoolEntry` object is mostly visible to public-facing
    API code when it is delivered to connection pool event hooks, such as
    :meth:`_events.PoolEvents.connect` and :meth:`_events.PoolEvents.checkout`.

    .. versionadded:: 2.0  :class:`.ConnectionPoolEntry` provides the public
       facing interface for the :class:`._ConnectionRecord` internal class.

    '''
    @property
    def in_use(self) -> bool:
        """Return True the connection is currently checked out"""
    def close(self) -> None:
        """Close the DBAPI connection managed by this connection pool entry."""

class _ConnectionRecord(ConnectionPoolEntry):
    """Maintains a position in a connection pool which references a pooled
    connection.

    This is an internal object used by the :class:`_pool.Pool` implementation
    to provide context management to a DBAPI connection maintained by
    that :class:`_pool.Pool`.   The public facing interface for this class
    is described by the :class:`.ConnectionPoolEntry` class.  See that
    class for public API details.

    .. seealso::

        :class:`.ConnectionPoolEntry`

        :class:`.PoolProxiedConnection`

    """
    finalize_callback: Deque[Callable[[DBAPIConnection], None]]
    fresh: bool
    fairy_ref: weakref.ref[_ConnectionFairy] | None
    starttime: float
    dbapi_connection: Incomplete
    def __init__(self, pool: Pool, connect: bool = True) -> None: ...
    @property
    def driver_connection(self) -> Any | None: ...
    @property
    def connection(self) -> DBAPIConnection | None: ...
    def info(self) -> _InfoType: ...
    def record_info(self) -> _InfoType | None: ...
    @classmethod
    def checkout(cls, pool: Pool) -> _ConnectionFairy: ...
    def checkin(self, _fairy_was_created: bool = True) -> None: ...
    @property
    def in_use(self) -> bool: ...
    @property
    def last_connect_time(self) -> float: ...
    def close(self) -> None: ...
    def invalidate(self, e: BaseException | None = None, soft: bool = False) -> None: ...
    def get_connection(self) -> DBAPIConnection: ...

class PoolProxiedConnection(ManagesConnection):
    """A connection-like adapter for a :pep:`249` DBAPI connection, which
    includes additional methods specific to the :class:`.Pool` implementation.

    :class:`.PoolProxiedConnection` is the public-facing interface for the
    internal :class:`._ConnectionFairy` implementation object; users familiar
    with :class:`._ConnectionFairy` can consider this object to be equivalent.

    .. versionadded:: 2.0  :class:`.PoolProxiedConnection` provides the public-
       facing interface for the :class:`._ConnectionFairy` internal class.

    """
    def commit(self) -> None: ...
    def cursor(self) -> DBAPICursor: ...
    def rollback(self) -> None: ...
    @property
    def is_valid(self) -> bool:
        """Return True if this :class:`.PoolProxiedConnection` still refers
        to an active DBAPI connection."""
    @property
    def is_detached(self) -> bool:
        """Return True if this :class:`.PoolProxiedConnection` is detached
        from its pool."""
    def detach(self) -> None:
        """Separate this connection from its Pool.

        This means that the connection will no longer be returned to the
        pool when closed, and will instead be literally closed.  The
        associated :class:`.ConnectionPoolEntry` is de-associated from this
        DBAPI connection.

        Note that any overall connection limiting constraints imposed by a
        Pool implementation may be violated after a detach, as the detached
        connection is removed from the pool's knowledge and control.

        """
    def close(self) -> None:
        '''Release this connection back to the pool.

        The :meth:`.PoolProxiedConnection.close` method shadows the
        :pep:`249` ``.close()`` method, altering its behavior to instead
        :term:`release` the proxied connection back to the connection pool.

        Upon release to the pool, whether the connection stays "opened" and
        pooled in the Python process, versus actually closed out and removed
        from the Python process, is based on the pool implementation in use and
        its configuration and current state.

        '''

class _AdhocProxiedConnection(PoolProxiedConnection):
    """provides the :class:`.PoolProxiedConnection` interface for cases where
    the DBAPI connection is not actually proxied.

    This is used by the engine internals to pass a consistent
    :class:`.PoolProxiedConnection` object to consuming dialects in response to
    pool events that may not always have the :class:`._ConnectionFairy`
    available.

    """
    dbapi_connection: DBAPIConnection
    def __init__(self, dbapi_connection: DBAPIConnection, connection_record: ConnectionPoolEntry) -> None: ...
    @property
    def driver_connection(self) -> Any: ...
    @property
    def connection(self) -> DBAPIConnection: ...
    @property
    def is_valid(self) -> bool:
        '''Implement is_valid state attribute.

        for the adhoc proxied connection it\'s assumed the connection is valid
        as there is no "invalidate" routine.

        '''
    def invalidate(self, e: BaseException | None = None, soft: bool = False) -> None: ...
    def record_info(self) -> _InfoType | None: ...
    def cursor(self, *args: Any, **kwargs: Any) -> DBAPICursor: ...
    def __getattr__(self, key: Any) -> Any: ...

class _ConnectionFairy(PoolProxiedConnection):
    '''Proxies a DBAPI connection and provides return-on-dereference
    support.

    This is an internal object used by the :class:`_pool.Pool` implementation
    to provide context management to a DBAPI connection delivered by
    that :class:`_pool.Pool`.   The public facing interface for this class
    is described by the :class:`.PoolProxiedConnection` class.  See that
    class for public API details.

    The name "fairy" is inspired by the fact that the
    :class:`._ConnectionFairy` object\'s lifespan is transitory, as it lasts
    only for the length of a specific DBAPI connection being checked out from
    the pool, and additionally that as a transparent proxy, it is mostly
    invisible.

    .. seealso::

        :class:`.PoolProxiedConnection`

        :class:`.ConnectionPoolEntry`


    '''
    pool: Pool
    dbapi_connection: DBAPIConnection
    def __init__(self, pool: Pool, dbapi_connection: DBAPIConnection, connection_record: _ConnectionRecord, echo: log._EchoFlagType) -> None: ...
    @property
    def driver_connection(self) -> Any | None: ...
    @property
    def connection(self) -> DBAPIConnection: ...
    @property
    def is_valid(self) -> bool: ...
    @property
    def is_detached(self) -> bool: ...
    def info(self) -> _InfoType: ...
    def record_info(self) -> _InfoType | None: ...
    def invalidate(self, e: BaseException | None = None, soft: bool = False) -> None: ...
    def cursor(self, *args: Any, **kwargs: Any) -> DBAPICursor: ...
    def __getattr__(self, key: str) -> Any: ...
    def detach(self) -> None: ...
    def close(self) -> None: ...
