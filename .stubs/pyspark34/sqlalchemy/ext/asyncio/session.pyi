from . import engine as engine
from ... import util as util
from ...engine import Connection as Connection, CursorResult as CursorResult, Engine as Engine, Result as Result, Row as Row, RowMapping as RowMapping, ScalarResult as ScalarResult
from ...engine.interfaces import CoreExecuteOptionsParameter as CoreExecuteOptionsParameter, _CoreAnyExecuteParams
from ...event import dispatcher as dispatcher
from ...orm import Session as Session, SessionTransaction as SessionTransaction, object_session as object_session
from ...orm._typing import OrmExecuteOptionsParameter as OrmExecuteOptionsParameter, _IdentityKeyType, _O
from ...orm.identity import IdentityMap as IdentityMap
from ...orm.interfaces import ORMOption as ORMOption
from ...orm.session import _BindArguments, _EntityBindKey, _PKIdentityArgument, _SessionBind, _SessionBindKey
from ...sql._typing import _InfoType
from ...sql.base import Executable as Executable
from ...sql.dml import UpdateBase as UpdateBase
from ...sql.elements import ClauseElement as ClauseElement
from ...sql.selectable import ForUpdateParameter as ForUpdateParameter, TypedReturnsRows as TypedReturnsRows
from ...util.concurrency import greenlet_spawn as greenlet_spawn
from .base import ReversibleProxy as ReversibleProxy, StartableContext as StartableContext
from .engine import AsyncConnection as AsyncConnection, AsyncEngine as AsyncEngine
from .result import AsyncResult as AsyncResult, AsyncScalarResult as AsyncScalarResult
from _typeshed import Incomplete
from typing import Any, Awaitable, Callable, Dict, Generic, Iterable, Iterator, Sequence, Tuple, Type, overload

class AsyncAttrs:
    '''Mixin class which provides an awaitable accessor for all attributes.

    E.g.::

        from __future__ import annotations

        from typing import List

        from sqlalchemy import ForeignKey
        from sqlalchemy import func
        from sqlalchemy.ext.asyncio import AsyncAttrs
        from sqlalchemy.orm import DeclarativeBase
        from sqlalchemy.orm import Mapped
        from sqlalchemy.orm import mapped_column
        from sqlalchemy.orm import relationship


        class Base(AsyncAttrs, DeclarativeBase):
            pass


        class A(Base):
            __tablename__ = "a"

            id: Mapped[int] = mapped_column(primary_key=True)
            data: Mapped[str]
            bs: Mapped[List[B]] = relationship()


        class B(Base):
            __tablename__ = "b"
            id: Mapped[int] = mapped_column(primary_key=True)
            a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
            data: Mapped[str]

    In the above example, the :class:`_asyncio.AsyncAttrs` mixin is applied to
    the declarative ``Base`` class where it takes effect for all subclasses.
    This mixin adds a single new attribute
    :attr:`_asyncio.AsyncAttrs.awaitable_attrs` to all classes, which will
    yield the value of any attribute as an awaitable. This allows attributes
    which may be subject to lazy loading or deferred / unexpiry loading to be
    accessed such that IO can still be emitted::

        a1 = (await async_session.scalars(select(A).where(A.id == 5))).one()

        # use the lazy loader on ``a1.bs`` via the ``.awaitable_attrs``
        # interface, so that it may be awaited
        for b1 in await a1.awaitable_attrs.bs:
            print(b1)

    The :attr:`_asyncio.AsyncAttrs.awaitable_attrs` performs a call against the
    attribute that is approximately equivalent to using the
    :meth:`_asyncio.AsyncSession.run_sync` method, e.g.::

        for b1 in await async_session.run_sync(lambda sess: a1.bs):
            print(b1)

    .. versionadded:: 2.0.13

    .. seealso::

        :ref:`asyncio_orm_avoid_lazyloads`

    '''
    class _AsyncAttrGetitem:
        def __init__(self, _instance: Any) -> None: ...
        def __getattr__(self, name: str) -> Awaitable[Any]: ...
    @property
    def awaitable_attrs(self) -> AsyncAttrs._AsyncAttrGetitem:
        """provide a namespace of all attributes on this object wrapped
        as awaitables.

        e.g.::


            a1 = (await async_session.scalars(select(A).where(A.id == 5))).one()

            some_attribute = await a1.awaitable_attrs.some_deferred_attribute
            some_collection = await a1.awaitable_attrs.some_collection

        """

class AsyncSession(ReversibleProxy[Session]):
    """Asyncio version of :class:`_orm.Session`.

    The :class:`_asyncio.AsyncSession` is a proxy for a traditional
    :class:`_orm.Session` instance.

    The :class:`_asyncio.AsyncSession` is **not safe for use in concurrent
    tasks.**.  See :ref:`session_faq_threadsafe` for background.

    .. versionadded:: 1.4

    To use an :class:`_asyncio.AsyncSession` with custom :class:`_orm.Session`
    implementations, see the
    :paramref:`_asyncio.AsyncSession.sync_session_class` parameter.


    """
    dispatch: dispatcher[Session]
    bind: Incomplete
    binds: Incomplete
    sync_session_class: Incomplete
    sync_session: Incomplete
    def __init__(self, bind: _AsyncSessionBind | None = None, *, binds: Dict[_SessionBindKey, _AsyncSessionBind] | None = None, sync_session_class: Type[Session] | None = None, **kw: Any) -> None:
        """Construct a new :class:`_asyncio.AsyncSession`.

        All parameters other than ``sync_session_class`` are passed to the
        ``sync_session_class`` callable directly to instantiate a new
        :class:`_orm.Session`. Refer to :meth:`_orm.Session.__init__` for
        parameter documentation.

        :param sync_session_class:
          A :class:`_orm.Session` subclass or other callable which will be used
          to construct the :class:`_orm.Session` which will be proxied. This
          parameter may be used to provide custom :class:`_orm.Session`
          subclasses. Defaults to the
          :attr:`_asyncio.AsyncSession.sync_session_class` class-level
          attribute.

          .. versionadded:: 1.4.24

        """
    async def refresh(self, instance: object, attribute_names: Iterable[str] | None = None, with_for_update: ForUpdateParameter = None) -> None:
        """Expire and refresh the attributes on the given instance.

        A query will be issued to the database and all attributes will be
        refreshed with their current database value.

        This is the async version of the :meth:`_orm.Session.refresh` method.
        See that method for a complete description of all options.

        .. seealso::

            :meth:`_orm.Session.refresh` - main documentation for refresh

        """
    async def run_sync(self, fn: Callable[..., _T], *arg: Any, **kw: Any) -> _T:
        '''Invoke the given synchronous (i.e. not async) callable,
        passing a synchronous-style :class:`_orm.Session` as the first
        argument.

        This method allows traditional synchronous SQLAlchemy functions to
        run within the context of an asyncio application.

        E.g.::

            def some_business_method(session: Session, param: str) -> str:
                \'\'\'A synchronous function that does not require awaiting

                :param session: a SQLAlchemy Session, used synchronously

                :return: an optional return value is supported

                \'\'\'
                session.add(MyObject(param=param))
                session.flush()
                return "success"


            async def do_something_async(async_engine: AsyncEngine) -> None:
                \'\'\'an async function that uses awaiting\'\'\'

                with AsyncSession(async_engine) as async_session:
                    # run some_business_method() with a sync-style
                    # Session, proxied into an awaitable
                    return_code = await async_session.run_sync(some_business_method, param="param1")
                    print(return_code)

        This method maintains the asyncio event loop all the way through
        to the database connection by running the given callable in a
        specially instrumented greenlet.

        .. tip::

            The provided callable is invoked inline within the asyncio event
            loop, and will block on traditional IO calls.  IO within this
            callable should only call into SQLAlchemy\'s asyncio database
            APIs which will be properly adapted to the greenlet context.

        .. seealso::

            :class:`.AsyncAttrs`  - a mixin for ORM mapped classes that provides
            a similar feature more succinctly on a per-attribute basis

            :meth:`.AsyncConnection.run_sync`

            :ref:`session_run_sync`
        '''
    @overload
    async def execute(self, statement: TypedReturnsRows[_T], params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, _parent_execute_state: Any | None = None, _add_event: Any | None = None) -> Result[_T]: ...
    @overload
    async def execute(self, statement: UpdateBase, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, _parent_execute_state: Any | None = None, _add_event: Any | None = None) -> CursorResult[Any]: ...
    @overload
    async def execute(self, statement: Executable, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, _parent_execute_state: Any | None = None, _add_event: Any | None = None) -> Result[Any]: ...
    @overload
    async def scalar(self, statement: TypedReturnsRows[Tuple[_T]], params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> _T | None: ...
    @overload
    async def scalar(self, statement: Executable, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> Any: ...
    @overload
    async def scalars(self, statement: TypedReturnsRows[Tuple[_T]], params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> ScalarResult[_T]: ...
    @overload
    async def scalars(self, statement: Executable, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> ScalarResult[Any]: ...
    async def get(self, entity: _EntityBindKey[_O], ident: _PKIdentityArgument, *, options: Sequence[ORMOption] | None = None, populate_existing: bool = False, with_for_update: ForUpdateParameter = None, identity_token: Any | None = None, execution_options: OrmExecuteOptionsParameter = ...) -> _O | None:
        """Return an instance based on the given primary key identifier,
        or ``None`` if not found.

        .. seealso::

            :meth:`_orm.Session.get` - main documentation for get


        """
    async def get_one(self, entity: _EntityBindKey[_O], ident: _PKIdentityArgument, *, options: Sequence[ORMOption] | None = None, populate_existing: bool = False, with_for_update: ForUpdateParameter = None, identity_token: Any | None = None, execution_options: OrmExecuteOptionsParameter = ...) -> _O:
        """Return an instance based on the given primary key identifier,
        or raise an exception if not found.

        Raises ``sqlalchemy.orm.exc.NoResultFound`` if the query selects
        no rows.

        ..versionadded: 2.0.22

        .. seealso::

            :meth:`_orm.Session.get_one` - main documentation for get_one

        """
    @overload
    async def stream(self, statement: TypedReturnsRows[_T], params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> AsyncResult[_T]: ...
    @overload
    async def stream(self, statement: Executable, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> AsyncResult[Any]: ...
    @overload
    async def stream_scalars(self, statement: TypedReturnsRows[Tuple[_T]], params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> AsyncScalarResult[_T]: ...
    @overload
    async def stream_scalars(self, statement: Executable, params: _CoreAnyExecuteParams | None = None, *, execution_options: OrmExecuteOptionsParameter = ..., bind_arguments: _BindArguments | None = None, **kw: Any) -> AsyncScalarResult[Any]: ...
    async def delete(self, instance: object) -> None:
        """Mark an instance as deleted.

        The database delete operation occurs upon ``flush()``.

        As this operation may need to cascade along unloaded relationships,
        it is awaitable to allow for those queries to take place.

        .. seealso::

            :meth:`_orm.Session.delete` - main documentation for delete

        """
    async def merge(self, instance: _O, *, load: bool = True, options: Sequence[ORMOption] | None = None) -> _O:
        """Copy the state of a given instance into a corresponding instance
        within this :class:`_asyncio.AsyncSession`.

        .. seealso::

            :meth:`_orm.Session.merge` - main documentation for merge

        """
    async def flush(self, objects: Sequence[Any] | None = None) -> None:
        """Flush all the object changes to the database.

        .. seealso::

            :meth:`_orm.Session.flush` - main documentation for flush

        """
    def get_transaction(self) -> AsyncSessionTransaction | None:
        """Return the current root transaction in progress, if any.

        :return: an :class:`_asyncio.AsyncSessionTransaction` object, or
         ``None``.

        .. versionadded:: 1.4.18

        """
    def get_nested_transaction(self) -> AsyncSessionTransaction | None:
        """Return the current nested transaction in progress, if any.

        :return: an :class:`_asyncio.AsyncSessionTransaction` object, or
         ``None``.

        .. versionadded:: 1.4.18

        """
    def get_bind(self, mapper: _EntityBindKey[_O] | None = None, clause: ClauseElement | None = None, bind: _SessionBind | None = None, **kw: Any) -> Engine | Connection:
        '''Return a "bind" to which the synchronous proxied :class:`_orm.Session`
        is bound.

        Unlike the :meth:`_orm.Session.get_bind` method, this method is
        currently **not** used by this :class:`.AsyncSession` in any way
        in order to resolve engines for requests.

        .. note::

            This method proxies directly to the :meth:`_orm.Session.get_bind`
            method, however is currently **not** useful as an override target,
            in contrast to that of the :meth:`_orm.Session.get_bind` method.
            The example below illustrates how to implement custom
            :meth:`_orm.Session.get_bind` schemes that work with
            :class:`.AsyncSession` and :class:`.AsyncEngine`.

        The pattern introduced at :ref:`session_custom_partitioning`
        illustrates how to apply a custom bind-lookup scheme to a
        :class:`_orm.Session` given a set of :class:`_engine.Engine` objects.
        To apply a corresponding :meth:`_orm.Session.get_bind` implementation
        for use with a :class:`.AsyncSession` and :class:`.AsyncEngine`
        objects, continue to subclass :class:`_orm.Session` and apply it to
        :class:`.AsyncSession` using
        :paramref:`.AsyncSession.sync_session_class`. The inner method must
        continue to return :class:`_engine.Engine` instances, which can be
        acquired from a :class:`_asyncio.AsyncEngine` using the
        :attr:`_asyncio.AsyncEngine.sync_engine` attribute::

            # using example from "Custom Vertical Partitioning"


            import random

            from sqlalchemy.ext.asyncio import AsyncSession
            from sqlalchemy.ext.asyncio import create_async_engine
            from sqlalchemy.ext.asyncio import async_sessionmaker
            from sqlalchemy.orm import Session

            # construct async engines w/ async drivers
            engines = {
                \'leader\':create_async_engine("sqlite+aiosqlite:///leader.db"),
                \'other\':create_async_engine("sqlite+aiosqlite:///other.db"),
                \'follower1\':create_async_engine("sqlite+aiosqlite:///follower1.db"),
                \'follower2\':create_async_engine("sqlite+aiosqlite:///follower2.db"),
            }

            class RoutingSession(Session):
                def get_bind(self, mapper=None, clause=None, **kw):
                    # within get_bind(), return sync engines
                    if mapper and issubclass(mapper.class_, MyOtherClass):
                        return engines[\'other\'].sync_engine
                    elif self._flushing or isinstance(clause, (Update, Delete)):
                        return engines[\'leader\'].sync_engine
                    else:
                        return engines[
                            random.choice([\'follower1\',\'follower2\'])
                        ].sync_engine

            # apply to AsyncSession using sync_session_class
            AsyncSessionMaker = async_sessionmaker(
                sync_session_class=RoutingSession
            )

        The :meth:`_orm.Session.get_bind` method is called in a non-asyncio,
        implicitly non-blocking context in the same manner as ORM event hooks
        and functions that are invoked via :meth:`.AsyncSession.run_sync`, so
        routines that wish to run SQL commands inside of
        :meth:`_orm.Session.get_bind` can continue to do so using
        blocking-style code, which will be translated to implicitly async calls
        at the point of invoking IO on the database drivers.

        '''
    async def connection(self, bind_arguments: _BindArguments | None = None, execution_options: CoreExecuteOptionsParameter | None = None, **kw: Any) -> AsyncConnection:
        '''Return a :class:`_asyncio.AsyncConnection` object corresponding to
        this :class:`.Session` object\'s transactional state.

        This method may also be used to establish execution options for the
        database connection used by the current transaction.

        .. versionadded:: 1.4.24  Added \\**kw arguments which are passed
           through to the underlying :meth:`_orm.Session.connection` method.

        .. seealso::

            :meth:`_orm.Session.connection` - main documentation for
            "connection"

        '''
    def begin(self) -> AsyncSessionTransaction:
        '''Return an :class:`_asyncio.AsyncSessionTransaction` object.

        The underlying :class:`_orm.Session` will perform the
        "begin" action when the :class:`_asyncio.AsyncSessionTransaction`
        object is entered::

            async with async_session.begin():
                # .. ORM transaction is begun

        Note that database IO will not normally occur when the session-level
        transaction is begun, as database transactions begin on an
        on-demand basis.  However, the begin block is async to accommodate
        for a :meth:`_orm.SessionEvents.after_transaction_create`
        event hook that may perform IO.

        For a general description of ORM begin, see
        :meth:`_orm.Session.begin`.

        '''
    def begin_nested(self) -> AsyncSessionTransaction:
        '''Return an :class:`_asyncio.AsyncSessionTransaction` object
        which will begin a "nested" transaction, e.g. SAVEPOINT.

        Behavior is the same as that of :meth:`_asyncio.AsyncSession.begin`.

        For a general description of ORM begin nested, see
        :meth:`_orm.Session.begin_nested`.

        '''
    async def rollback(self) -> None:
        '''Rollback the current transaction in progress.

        .. seealso::

            :meth:`_orm.Session.rollback` - main documentation for
            "rollback"
        '''
    async def commit(self) -> None:
        '''Commit the current transaction in progress.

        .. seealso::

            :meth:`_orm.Session.commit` - main documentation for
            "commit"
        '''
    async def close(self) -> None:
        '''Close out the transactional resources and ORM objects used by this
        :class:`_asyncio.AsyncSession`.

        .. seealso::

            :meth:`_orm.Session.close` - main documentation for
            "close"

            :ref:`session_closing` - detail on the semantics of
            :meth:`_asyncio.AsyncSession.close` and
            :meth:`_asyncio.AsyncSession.reset`.

        '''
    async def reset(self) -> None:
        '''Close out the transactional resources and ORM objects used by this
        :class:`_orm.Session`, resetting the session to its initial state.

        .. versionadded:: 2.0.22

        .. seealso::

            :meth:`_orm.Session.reset` - main documentation for
            "reset"

            :ref:`session_closing` - detail on the semantics of
            :meth:`_asyncio.AsyncSession.close` and
            :meth:`_asyncio.AsyncSession.reset`.

        '''
    async def aclose(self) -> None:
        """A synonym for :meth:`_asyncio.AsyncSession.close`.

        The :meth:`_asyncio.AsyncSession.aclose` name is specifically
        to support the Python standard library ``@contextlib.aclosing``
        context manager function.

        .. versionadded:: 2.0.20

        """
    async def invalidate(self) -> None:
        """Close this Session, using connection invalidation.

        For a complete description, see :meth:`_orm.Session.invalidate`.
        """
    @classmethod
    async def close_all(self) -> None:
        """Close all :class:`_asyncio.AsyncSession` sessions."""
    async def __aenter__(self) -> _AS: ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def __contains__(self, instance: object) -> bool:
        """Return True if the instance is associated with this session.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        The instance may be pending or persistent within the Session for a
        result of True.


        """
    def __iter__(self) -> Iterator[object]:
        """Iterate over all pending or persistent instances within this
        Session.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.


        """
    def add(self, instance: object, _warn: bool = True) -> None:
        """Place an object into this :class:`_orm.Session`.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

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

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        See the documentation for :meth:`_orm.Session.add` for a general
        behavioral description.

        .. seealso::

            :meth:`_orm.Session.add`

            :ref:`session_adding` - at :ref:`session_basics`


        """
    def expire(self, instance: object, attribute_names: Iterable[str] | None = None) -> None:
        """Expire the attributes on an instance.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

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
    def expire_all(self) -> None:
        """Expires all persistent instances within this Session.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

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
    def expunge(self, instance: object) -> None:
        """Remove the `instance` from this ``Session``.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This will free all internal references to the instance.  Cascading
        will be applied according to the *expunge* cascade rule.


        """
    def expunge_all(self) -> None:
        """Remove all object instances from this ``Session``.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This is equivalent to calling ``expunge(obj)`` on all objects in this
        ``Session``.


        """
    def is_modified(self, instance: object, include_collections: bool = True) -> bool:
        '''Return ``True`` if the given instance has locally
        modified attributes.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

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
    def in_transaction(self) -> bool:
        """Return True if this :class:`_orm.Session` has begun a transaction.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_orm.Session.is_active`



        """
    def in_nested_transaction(self) -> bool:
        """Return True if this :class:`_orm.Session` has begun a nested
        transaction, e.g. SAVEPOINT.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        .. versionadded:: 1.4


        """
    @property
    def dirty(self) -> Any:
        """The set of all persistent instances considered dirty.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class
            on behalf of the :class:`_asyncio.AsyncSession` class.

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
    def deleted(self) -> Any:
        """The set of all instances marked as 'deleted' within this ``Session``

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class
            on behalf of the :class:`_asyncio.AsyncSession` class.

        """
    @property
    def new(self) -> Any:
        """The set of all instances marked as 'new' within this ``Session``.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class
            on behalf of the :class:`_asyncio.AsyncSession` class.

        """
    @property
    def identity_map(self) -> IdentityMap:
        """Proxy for the :attr:`_orm.Session.identity_map` attribute
        on behalf of the :class:`_asyncio.AsyncSession` class.

        """
    @identity_map.setter
    def identity_map(self, attr: IdentityMap) -> None: ...
    @property
    def is_active(self) -> Any:
        '''True if this :class:`.Session` not in "partial rollback" state.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class
            on behalf of the :class:`_asyncio.AsyncSession` class.

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
    def autoflush(self) -> bool:
        """Proxy for the :attr:`_orm.Session.autoflush` attribute
        on behalf of the :class:`_asyncio.AsyncSession` class.

        """
    @autoflush.setter
    def autoflush(self, attr: bool) -> None: ...
    @property
    def no_autoflush(self) -> Any:
        """Return a context manager that disables autoflush.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class
            on behalf of the :class:`_asyncio.AsyncSession` class.

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
    @property
    def info(self) -> Any:
        """A user-modifiable dictionary.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class
            on behalf of the :class:`_asyncio.AsyncSession` class.

        The initial value of this dictionary can be populated using the
        ``info`` argument to the :class:`.Session` constructor or
        :class:`.sessionmaker` constructor or factory methods.  The dictionary
        here is always local to this :class:`.Session` and can be modified
        independently of all other :class:`.Session` objects.


        """
    @classmethod
    def object_session(cls, instance: object) -> Session | None:
        """Return the :class:`.Session` to which an object belongs.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This is an alias of :func:`.object_session`.


        """
    @classmethod
    def identity_key(cls, class_: Type[Any] | None = None, ident: Any | Tuple[Any, ...] = None, *, instance: Any | None = None, row: Row[Any] | RowMapping | None = None, identity_token: Any | None = None) -> _IdentityKeyType[Any]:
        """Return an identity key.

        .. container:: class_bases

            Proxied for the :class:`_orm.Session` class on
            behalf of the :class:`_asyncio.AsyncSession` class.

        This is an alias of :func:`.util.identity_key`.


        """

class async_sessionmaker(Generic[_AS]):
    '''A configurable :class:`.AsyncSession` factory.

    The :class:`.async_sessionmaker` factory works in the same way as the
    :class:`.sessionmaker` factory, to generate new :class:`.AsyncSession`
    objects when called, creating them given
    the configurational arguments established here.

    e.g.::

        from sqlalchemy.ext.asyncio import create_async_engine
        from sqlalchemy.ext.asyncio import AsyncSession
        from sqlalchemy.ext.asyncio import async_sessionmaker

        async def run_some_sql(async_session: async_sessionmaker[AsyncSession]) -> None:
            async with async_session() as session:
                session.add(SomeObject(data="object"))
                session.add(SomeOtherObject(name="other object"))
                await session.commit()

        async def main() -> None:
            # an AsyncEngine, which the AsyncSession will use for connection
            # resources
            engine = create_async_engine(\'postgresql+asyncpg://scott:tiger@localhost/\')

            # create a reusable factory for new AsyncSession instances
            async_session = async_sessionmaker(engine)

            await run_some_sql(async_session)

            await engine.dispose()

    The :class:`.async_sessionmaker` is useful so that different parts
    of a program can create new :class:`.AsyncSession` objects with a
    fixed configuration established up front.  Note that :class:`.AsyncSession`
    objects may also be instantiated directly when not using
    :class:`.async_sessionmaker`.

    .. versionadded:: 2.0  :class:`.async_sessionmaker` provides a
       :class:`.sessionmaker` class that\'s dedicated to the
       :class:`.AsyncSession` object, including pep-484 typing support.

    .. seealso::

        :ref:`asyncio_orm` - shows example use

        :class:`.sessionmaker`  - general overview of the
         :class:`.sessionmaker` architecture


        :ref:`session_getting` - introductory text on creating
        sessions using :class:`.sessionmaker`.

    '''
    class_: Type[_AS]
    @overload
    def __init__(self, bind: _AsyncSessionBind | None = ..., *, class_: Type[_AS], autoflush: bool = ..., expire_on_commit: bool = ..., info: _InfoType | None = ..., **kw: Any) -> None: ...
    @overload
    def __init__(self, bind: _AsyncSessionBind | None = ..., *, autoflush: bool = ..., expire_on_commit: bool = ..., info: _InfoType | None = ..., **kw: Any) -> None: ...
    def begin(self) -> _AsyncSessionContextManager[_AS]:
        """Produce a context manager that both provides a new
        :class:`_orm.AsyncSession` as well as a transaction that commits.


        e.g.::

            async def main():
                Session = async_sessionmaker(some_engine)

                async with Session.begin() as session:
                    session.add(some_object)

                # commits transaction, closes session


        """
    def __call__(self, **local_kw: Any) -> _AS:
        '''Produce a new :class:`.AsyncSession` object using the configuration
        established in this :class:`.async_sessionmaker`.

        In Python, the ``__call__`` method is invoked on an object when
        it is "called" in the same way as a function::

            AsyncSession = async_sessionmaker(async_engine, expire_on_commit=False)
            session = AsyncSession()  # invokes sessionmaker.__call__()

        '''
    def configure(self, **new_kw: Any) -> None:
        """(Re)configure the arguments for this async_sessionmaker.

        e.g.::

            AsyncSession = async_sessionmaker(some_engine)

            AsyncSession.configure(bind=create_async_engine('sqlite+aiosqlite://'))
        """

class _AsyncSessionContextManager(Generic[_AS]):
    async_session: _AS
    trans: AsyncSessionTransaction
    def __init__(self, async_session: _AS) -> None: ...
    async def __aenter__(self) -> _AS: ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class AsyncSessionTransaction(ReversibleProxy[SessionTransaction], StartableContext['AsyncSessionTransaction']):
    """A wrapper for the ORM :class:`_orm.SessionTransaction` object.

    This object is provided so that a transaction-holding object
    for the :meth:`_asyncio.AsyncSession.begin` may be returned.

    The object supports both explicit calls to
    :meth:`_asyncio.AsyncSessionTransaction.commit` and
    :meth:`_asyncio.AsyncSessionTransaction.rollback`, as well as use as an
    async context manager.


    .. versionadded:: 1.4

    """
    session: AsyncSession
    sync_transaction: SessionTransaction | None
    nested: Incomplete
    def __init__(self, session: AsyncSession, nested: bool = False) -> None: ...
    @property
    def is_active(self) -> bool: ...
    async def rollback(self) -> None:
        """Roll back this :class:`_asyncio.AsyncTransaction`."""
    async def commit(self) -> None:
        """Commit this :class:`_asyncio.AsyncTransaction`."""
    async def start(self, is_ctxmanager: bool = False) -> AsyncSessionTransaction: ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

def async_object_session(instance: object) -> AsyncSession | None:
    """Return the :class:`_asyncio.AsyncSession` to which the given instance
    belongs.

    This function makes use of the sync-API function
    :class:`_orm.object_session` to retrieve the :class:`_orm.Session` which
    refers to the given instance, and from there links it to the original
    :class:`_asyncio.AsyncSession`.

    If the :class:`_asyncio.AsyncSession` has been garbage collected, the
    return value is ``None``.

    This functionality is also available from the
    :attr:`_orm.InstanceState.async_session` accessor.

    :param instance: an ORM mapped instance
    :return: an :class:`_asyncio.AsyncSession` object, or ``None``.

    .. versionadded:: 1.4.18

    """
def async_session(session: Session) -> AsyncSession | None:
    """Return the :class:`_asyncio.AsyncSession` which is proxying the given
    :class:`_orm.Session` object, if any.

    :param session: a :class:`_orm.Session` instance.
    :return: a :class:`_asyncio.AsyncSession` instance, or ``None``.

    .. versionadded:: 1.4.18

    """
