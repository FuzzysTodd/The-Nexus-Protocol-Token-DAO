from ... import util as util
from ...engine import CursorResult as CursorResult, Result as Result
from ...engine.result import FilterResult as FilterResult, FrozenResult as FrozenResult, ResultMetaData as ResultMetaData, _KeyIndexType, _R, _UniqueFilterType, _WithKeys
from ...engine.row import Row as Row, RowMapping as RowMapping
from ...util.concurrency import greenlet_spawn as greenlet_spawn
from ...util.typing import Literal as Literal, Self as Self
from typing import Any, AsyncIterator, Sequence, overload

class AsyncCommon(FilterResult[_R]):
    async def close(self) -> None:
        """Close this result."""
    @property
    def closed(self) -> bool:
        """proxies the .closed attribute of the underlying result object,
        if any, else raises ``AttributeError``.

        .. versionadded:: 2.0.0b3

        """

class AsyncResult(_WithKeys, AsyncCommon[Row[_TP]]):
    """An asyncio wrapper around a :class:`_result.Result` object.

    The :class:`_asyncio.AsyncResult` only applies to statement executions that
    use a server-side cursor.  It is returned only from the
    :meth:`_asyncio.AsyncConnection.stream` and
    :meth:`_asyncio.AsyncSession.stream` methods.

    .. note:: As is the case with :class:`_engine.Result`, this object is
       used for ORM results returned by :meth:`_asyncio.AsyncSession.execute`,
       which can yield instances of ORM mapped objects either individually or
       within tuple-like rows.  Note that these result objects do not
       deduplicate instances or rows automatically as is the case with the
       legacy :class:`_orm.Query` object. For in-Python de-duplication of
       instances or rows, use the :meth:`_asyncio.AsyncResult.unique` modifier
       method.

    .. versionadded:: 1.4

    """
    def __init__(self, real_result: Result[_TP]) -> None: ...
    @property
    def t(self) -> AsyncTupleResult[_TP]:
        '''Apply a "typed tuple" typing filter to returned rows.

        The :attr:`_asyncio.AsyncResult.t` attribute is a synonym for
        calling the :meth:`_asyncio.AsyncResult.tuples` method.

        .. versionadded:: 2.0

        '''
    def tuples(self) -> AsyncTupleResult[_TP]:
        '''Apply a "typed tuple" typing filter to returned rows.

        This method returns the same :class:`_asyncio.AsyncResult` object
        at runtime,
        however annotates as returning a :class:`_asyncio.AsyncTupleResult`
        object that will indicate to :pep:`484` typing tools that plain typed
        ``Tuple`` instances are returned rather than rows.  This allows
        tuple unpacking and ``__getitem__`` access of :class:`_engine.Row`
        objects to by typed, for those cases where the statement invoked
        itself included typing information.

        .. versionadded:: 2.0

        :return: the :class:`_result.AsyncTupleResult` type at typing time.

        .. seealso::

            :attr:`_asyncio.AsyncResult.t` - shorter synonym

            :attr:`_engine.Row.t` - :class:`_engine.Row` version

        '''
    def unique(self, strategy: _UniqueFilterType | None = None) -> Self:
        """Apply unique filtering to the objects returned by this
        :class:`_asyncio.AsyncResult`.

        Refer to :meth:`_engine.Result.unique` in the synchronous
        SQLAlchemy API for a complete behavioral description.

        """
    def columns(self, *col_expressions: _KeyIndexType) -> Self:
        """Establish the columns that should be returned in each row.

        Refer to :meth:`_engine.Result.columns` in the synchronous
        SQLAlchemy API for a complete behavioral description.

        """
    async def partitions(self, size: int | None = None) -> AsyncIterator[Sequence[Row[_TP]]]:
        '''Iterate through sub-lists of rows of the size given.

        An async iterator is returned::

            async def scroll_results(connection):
                result = await connection.stream(select(users_table))

                async for partition in result.partitions(100):
                    print("list of rows: %s" % partition)

        Refer to :meth:`_engine.Result.partitions` in the synchronous
        SQLAlchemy API for a complete behavioral description.

        '''
    async def fetchall(self) -> Sequence[Row[_TP]]:
        """A synonym for the :meth:`_asyncio.AsyncResult.all` method.

        .. versionadded:: 2.0

        """
    async def fetchone(self) -> Row[_TP] | None:
        """Fetch one row.

        When all rows are exhausted, returns None.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch the first row of a result only, use the
        :meth:`_asyncio.AsyncResult.first` method.  To iterate through all
        rows, iterate the :class:`_asyncio.AsyncResult` object directly.

        :return: a :class:`_engine.Row` object if no filters are applied,
         or ``None`` if no rows remain.

        """
    async def fetchmany(self, size: int | None = None) -> Sequence[Row[_TP]]:
        """Fetch many rows.

        When all rows are exhausted, returns an empty list.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch rows in groups, use the
        :meth:`._asyncio.AsyncResult.partitions` method.

        :return: a list of :class:`_engine.Row` objects.

        .. seealso::

            :meth:`_asyncio.AsyncResult.partitions`

        """
    async def all(self) -> Sequence[Row[_TP]]:
        """Return all rows in a list.

        Closes the result set after invocation.   Subsequent invocations
        will return an empty list.

        :return: a list of :class:`_engine.Row` objects.

        """
    def __aiter__(self) -> AsyncResult[_TP]: ...
    async def __anext__(self) -> Row[_TP]: ...
    async def first(self) -> Row[_TP] | None:
        """Fetch the first row or ``None`` if no row is present.

        Closes the result set and discards remaining rows.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_asyncio.AsyncResult.scalar` method,
           or combine :meth:`_asyncio.AsyncResult.scalars` and
           :meth:`_asyncio.AsyncResult.first`.

           Additionally, in contrast to the behavior of the legacy  ORM
           :meth:`_orm.Query.first` method, **no limit is applied** to the
           SQL query which was invoked to produce this
           :class:`_asyncio.AsyncResult`;
           for a DBAPI driver that buffers results in memory before yielding
           rows, all rows will be sent to the Python process and all but
           the first row will be discarded.

           .. seealso::

                :ref:`migration_20_unify_select`

        :return: a :class:`_engine.Row` object, or None
         if no rows remain.

        .. seealso::

            :meth:`_asyncio.AsyncResult.scalar`

            :meth:`_asyncio.AsyncResult.one`

        """
    async def one_or_none(self) -> Row[_TP] | None:
        """Return at most one result or raise an exception.

        Returns ``None`` if the result has no rows.
        Raises :class:`.MultipleResultsFound`
        if multiple rows are returned.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row` or ``None`` if no row
         is available.

        :raises: :class:`.MultipleResultsFound`

        .. seealso::

            :meth:`_asyncio.AsyncResult.first`

            :meth:`_asyncio.AsyncResult.one`

        """
    @overload
    async def scalar_one(self) -> _T: ...
    @overload
    async def scalar_one(self) -> Any: ...
    @overload
    async def scalar_one_or_none(self) -> _T | None: ...
    @overload
    async def scalar_one_or_none(self) -> Any | None: ...
    async def one(self) -> Row[_TP]:
        """Return exactly one row or raise an exception.

        Raises :class:`.NoResultFound` if the result returns no
        rows, or :class:`.MultipleResultsFound` if multiple rows
        would be returned.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_asyncio.AsyncResult.scalar_one` method, or combine
           :meth:`_asyncio.AsyncResult.scalars` and
           :meth:`_asyncio.AsyncResult.one`.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row`.

        :raises: :class:`.MultipleResultsFound`, :class:`.NoResultFound`

        .. seealso::

            :meth:`_asyncio.AsyncResult.first`

            :meth:`_asyncio.AsyncResult.one_or_none`

            :meth:`_asyncio.AsyncResult.scalar_one`

        """
    @overload
    async def scalar(self) -> _T | None: ...
    @overload
    async def scalar(self) -> Any: ...
    async def freeze(self) -> FrozenResult[_TP]:
        """Return a callable object that will produce copies of this
        :class:`_asyncio.AsyncResult` when invoked.

        The callable object returned is an instance of
        :class:`_engine.FrozenResult`.

        This is used for result set caching.  The method must be called
        on the result when it has been unconsumed, and calling the method
        will consume the result fully.   When the :class:`_engine.FrozenResult`
        is retrieved from a cache, it can be called any number of times where
        it will produce a new :class:`_engine.Result` object each time
        against its stored set of rows.

        .. seealso::

            :ref:`do_orm_execute_re_executing` - example usage within the
            ORM to implement a result-set cache.

        """
    @overload
    def scalars(self, index: Literal[0]) -> AsyncScalarResult[_T]: ...
    @overload
    def scalars(self) -> AsyncScalarResult[_T]: ...
    @overload
    def scalars(self, index: _KeyIndexType = 0) -> AsyncScalarResult[Any]: ...
    def mappings(self) -> AsyncMappingResult:
        """Apply a mappings filter to returned rows, returning an instance of
        :class:`_asyncio.AsyncMappingResult`.

        When this filter is applied, fetching rows will return
        :class:`_engine.RowMapping` objects instead of :class:`_engine.Row`
        objects.

        :return: a new :class:`_asyncio.AsyncMappingResult` filtering object
         referring to the underlying :class:`_result.Result` object.

        """

class AsyncScalarResult(AsyncCommon[_R]):
    """A wrapper for a :class:`_asyncio.AsyncResult` that returns scalar values
    rather than :class:`_row.Row` values.

    The :class:`_asyncio.AsyncScalarResult` object is acquired by calling the
    :meth:`_asyncio.AsyncResult.scalars` method.

    Refer to the :class:`_result.ScalarResult` object in the synchronous
    SQLAlchemy API for a complete behavioral description.

    .. versionadded:: 1.4

    """
    def __init__(self, real_result: Result[Any], index: _KeyIndexType) -> None: ...
    def unique(self, strategy: _UniqueFilterType | None = None) -> Self:
        """Apply unique filtering to the objects returned by this
        :class:`_asyncio.AsyncScalarResult`.

        See :meth:`_asyncio.AsyncResult.unique` for usage details.

        """
    async def partitions(self, size: int | None = None) -> AsyncIterator[Sequence[_R]]:
        """Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_asyncio.AsyncResult.partitions` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    async def fetchall(self) -> Sequence[_R]:
        """A synonym for the :meth:`_asyncio.AsyncScalarResult.all` method."""
    async def fetchmany(self, size: int | None = None) -> Sequence[_R]:
        """Fetch many objects.

        Equivalent to :meth:`_asyncio.AsyncResult.fetchmany` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    async def all(self) -> Sequence[_R]:
        """Return all scalar values in a list.

        Equivalent to :meth:`_asyncio.AsyncResult.all` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    def __aiter__(self) -> AsyncScalarResult[_R]: ...
    async def __anext__(self) -> _R: ...
    async def first(self) -> _R | None:
        """Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_asyncio.AsyncResult.first` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    async def one_or_none(self) -> _R | None:
        """Return at most one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one_or_none` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    async def one(self) -> _R:
        """Return exactly one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """

class AsyncMappingResult(_WithKeys, AsyncCommon[RowMapping]):
    """A wrapper for a :class:`_asyncio.AsyncResult` that returns dictionary
    values rather than :class:`_engine.Row` values.

    The :class:`_asyncio.AsyncMappingResult` object is acquired by calling the
    :meth:`_asyncio.AsyncResult.mappings` method.

    Refer to the :class:`_result.MappingResult` object in the synchronous
    SQLAlchemy API for a complete behavioral description.

    .. versionadded:: 1.4

    """
    def __init__(self, result: Result[Any]) -> None: ...
    def unique(self, strategy: _UniqueFilterType | None = None) -> Self:
        """Apply unique filtering to the objects returned by this
        :class:`_asyncio.AsyncMappingResult`.

        See :meth:`_asyncio.AsyncResult.unique` for usage details.

        """
    def columns(self, *col_expressions: _KeyIndexType) -> Self:
        """Establish the columns that should be returned in each row."""
    async def partitions(self, size: int | None = None) -> AsyncIterator[Sequence[RowMapping]]:
        """Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_asyncio.AsyncResult.partitions` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    async def fetchall(self) -> Sequence[RowMapping]:
        """A synonym for the :meth:`_asyncio.AsyncMappingResult.all` method."""
    async def fetchone(self) -> RowMapping | None:
        """Fetch one object.

        Equivalent to :meth:`_asyncio.AsyncResult.fetchone` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    async def fetchmany(self, size: int | None = None) -> Sequence[RowMapping]:
        """Fetch many rows.

        Equivalent to :meth:`_asyncio.AsyncResult.fetchmany` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    async def all(self) -> Sequence[RowMapping]:
        """Return all rows in a list.

        Equivalent to :meth:`_asyncio.AsyncResult.all` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    def __aiter__(self) -> AsyncMappingResult: ...
    async def __anext__(self) -> RowMapping: ...
    async def first(self) -> RowMapping | None:
        """Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_asyncio.AsyncResult.first` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    async def one_or_none(self) -> RowMapping | None:
        """Return at most one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one_or_none` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    async def one(self) -> RowMapping:
        """Return exactly one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """

class AsyncTupleResult(AsyncCommon[_R], util.TypingOnly):
    """A :class:`_asyncio.AsyncResult` that's typed as returning plain
    Python tuples instead of rows.

    Since :class:`_engine.Row` acts like a tuple in every way already,
    this class is a typing only class, regular :class:`_asyncio.AsyncResult` is
    still used at runtime.

    """
    async def partitions(self, size: int | None = None) -> AsyncIterator[Sequence[_R]]:
        """Iterate through sub-lists of elements of the size given.

            Equivalent to :meth:`_result.Result.partitions` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    async def fetchone(self) -> _R | None:
        """Fetch one tuple.

            Equivalent to :meth:`_result.Result.fetchone` except that
            tuple values, rather than :class:`_engine.Row`
            objects, are returned.

            """
    async def fetchall(self) -> Sequence[_R]:
        """A synonym for the :meth:`_engine.ScalarResult.all` method."""
    async def fetchmany(self, size: int | None = None) -> Sequence[_R]:
        """Fetch many objects.

            Equivalent to :meth:`_result.Result.fetchmany` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    async def all(self) -> Sequence[_R]:
        """Return all scalar values in a list.

            Equivalent to :meth:`_result.Result.all` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    async def __aiter__(self) -> AsyncIterator[_R]: ...
    async def __anext__(self) -> _R: ...
    async def first(self) -> _R | None:
        """Fetch the first object or ``None`` if no object is present.

            Equivalent to :meth:`_result.Result.first` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.


            """
    async def one_or_none(self) -> _R | None:
        """Return at most one object or raise an exception.

            Equivalent to :meth:`_result.Result.one_or_none` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    async def one(self) -> _R:
        """Return exactly one object or raise an exception.

            Equivalent to :meth:`_result.Result.one` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    @overload
    async def scalar_one(self) -> _T: ...
    @overload
    async def scalar_one(self) -> Any: ...
    @overload
    async def scalar_one_or_none(self) -> _T | None: ...
    @overload
    async def scalar_one_or_none(self) -> Any | None: ...
    @overload
    async def scalar(self) -> _T | None: ...
    @overload
    async def scalar(self) -> Any: ...
