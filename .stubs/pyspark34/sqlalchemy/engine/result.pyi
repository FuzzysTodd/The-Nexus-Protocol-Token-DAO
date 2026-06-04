import typing
from .. import exc as exc, util as util
from ..sql.base import HasMemoized as HasMemoized, InPlaceGenerative as InPlaceGenerative
from ..sql.schema import Column as Column
from ..util import HasMemoized_ro_memoized_attribute as HasMemoized_ro_memoized_attribute, NONE_SET as NONE_SET
from ..util._has_cy import HAS_CYEXTENSION as HAS_CYEXTENSION
from ..util.typing import Literal as Literal, Self as Self
from .row import Row as Row, RowMapping as RowMapping
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Callable, Generic, Iterable, Iterator, Sequence, overload

class ResultMetaData:
    """Base for metadata about result rows."""
    @property
    def keys(self) -> RMKeyView: ...

class RMKeyView(typing.KeysView[Any]):
    def __init__(self, parent: ResultMetaData) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __contains__(self, item: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class SimpleResultMetaData(ResultMetaData):
    """result metadata for in-memory collections."""
    def __init__(self, keys: Sequence[str], extra: Sequence[Any] | None = None, _processors: _ProcessorsType | None = None, _tuplefilter: _TupleGetterType | None = None, _translated_indexes: Sequence[int] | None = None, _unique_filters: Sequence[Callable[[Any], Any]] | None = None) -> None: ...

def result_tuple(fields: Sequence[str], extra: Any | None = None) -> Callable[[Iterable[Any]], Row[Any]]: ...

class _NoRow(Enum): ...
class ResultInternal(InPlaceGenerative, Generic[_R]): ...

class _WithKeys:
    def keys(self) -> RMKeyView:
        """Return an iterable view which yields the string keys that would
        be represented by each :class:`_engine.Row`.

        The keys can represent the labels of the columns returned by a core
        statement or the names of the orm classes returned by an orm
        execution.

        The view also can be tested for key containment using the Python
        ``in`` operator, which will test both for the string keys represented
        in the view, as well as for alternate keys such as column objects.

        .. versionchanged:: 1.4 a key view object is returned rather than a
           plain list.


        """

class Result(_WithKeys, ResultInternal[Row[_TP]]):
    """Represent a set of database results.

    .. versionadded:: 1.4  The :class:`_engine.Result` object provides a
       completely updated usage model and calling facade for SQLAlchemy
       Core and SQLAlchemy ORM.   In Core, it forms the basis of the
       :class:`_engine.CursorResult` object which replaces the previous
       :class:`_engine.ResultProxy` interface.   When using the ORM, a
       higher level object called :class:`_engine.ChunkedIteratorResult`
       is normally used.

    .. note:: In SQLAlchemy 1.4 and above, this object is
       used for ORM results returned by :meth:`_orm.Session.execute`, which can
       yield instances of ORM mapped objects either individually or within
       tuple-like rows. Note that the :class:`_engine.Result` object does not
       deduplicate instances or rows automatically as is the case with the
       legacy :class:`_orm.Query` object. For in-Python de-duplication of
       instances or rows, use the :meth:`_engine.Result.unique` modifier
       method.

    .. seealso::

        :ref:`tutorial_fetching_rows` - in the :doc:`/tutorial/index`

    """
    def __init__(self, cursor_metadata: ResultMetaData) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def close(self) -> None:
        """close this :class:`_engine.Result`.

        The behavior of this method is implementation specific, and is
        not implemented by default.    The method should generally end
        the resources in use by the result object and also cause any
        subsequent iteration or row fetching to raise
        :class:`.ResourceClosedError`.

        .. versionadded:: 1.4.27 - ``.close()`` was previously not generally
           available for all :class:`_engine.Result` classes, instead only
           being available on the :class:`_engine.CursorResult` returned for
           Core statement executions. As most other result objects, namely the
           ones used by the ORM, are proxying a :class:`_engine.CursorResult`
           in any case, this allows the underlying cursor result to be closed
           from the outside facade for the case when the ORM query is using
           the ``yield_per`` execution option where it does not immediately
           exhaust and autoclose the database cursor.

        """
    @property
    def closed(self) -> bool:
        """return ``True`` if this :class:`_engine.Result` reports .closed

        .. versionadded:: 1.4.43

        """
    def yield_per(self, num: int) -> Self:
        '''Configure the row-fetching strategy to fetch ``num`` rows at a time.

        This impacts the underlying behavior of the result when iterating over
        the result object, or otherwise making use of  methods such as
        :meth:`_engine.Result.fetchone` that return one row at a time.   Data
        from the underlying cursor or other data source will be buffered up to
        this many rows in memory, and the buffered collection will then be
        yielded out one row at a time or as many rows are requested. Each time
        the buffer clears, it will be refreshed to this many rows or as many
        rows remain if fewer remain.

        The :meth:`_engine.Result.yield_per` method is generally used in
        conjunction with the
        :paramref:`_engine.Connection.execution_options.stream_results`
        execution option, which will allow the database dialect in use to make
        use of a server side cursor, if the DBAPI supports a specific "server
        side cursor" mode separate from its default mode of operation.

        .. tip::

            Consider using the
            :paramref:`_engine.Connection.execution_options.yield_per`
            execution option, which will simultaneously set
            :paramref:`_engine.Connection.execution_options.stream_results`
            to ensure the use of server side cursors, as well as automatically
            invoke the :meth:`_engine.Result.yield_per` method to establish
            a fixed row buffer size at once.

            The :paramref:`_engine.Connection.execution_options.yield_per`
            execution option is available for ORM operations, with
            :class:`_orm.Session`-oriented use described at
            :ref:`orm_queryguide_yield_per`. The Core-only version which works
            with :class:`_engine.Connection` is new as of SQLAlchemy 1.4.40.

        .. versionadded:: 1.4

        :param num: number of rows to fetch each time the buffer is refilled.
         If set to a value below 1, fetches all rows for the next buffer.

        .. seealso::

            :ref:`engine_stream_results` - describes Core behavior for
            :meth:`_engine.Result.yield_per`

            :ref:`orm_queryguide_yield_per` - in the :ref:`queryguide_toplevel`

        '''
    def unique(self, strategy: _UniqueFilterType | None = None) -> Self:
        """Apply unique filtering to the objects returned by this
        :class:`_engine.Result`.

        When this filter is applied with no arguments, the rows or objects
        returned will filtered such that each row is returned uniquely. The
        algorithm used to determine this uniqueness is by default the Python
        hashing identity of the whole tuple.   In some cases a specialized
        per-entity hashing scheme may be used, such as when using the ORM, a
        scheme is applied which  works against the primary key identity of
        returned objects.

        The unique filter is applied **after all other filters**, which means
        if the columns returned have been refined using a method such as the
        :meth:`_engine.Result.columns` or :meth:`_engine.Result.scalars`
        method, the uniquing is applied to **only the column or columns
        returned**.   This occurs regardless of the order in which these
        methods have been called upon the :class:`_engine.Result` object.

        The unique filter also changes the calculus used for methods like
        :meth:`_engine.Result.fetchmany` and :meth:`_engine.Result.partitions`.
        When using :meth:`_engine.Result.unique`, these methods will continue
        to yield the number of rows or objects requested, after uniquing
        has been applied.  However, this necessarily impacts the buffering
        behavior of the underlying cursor or datasource, such that multiple
        underlying calls to ``cursor.fetchmany()`` may be necessary in order
        to accumulate enough objects in order to provide a unique collection
        of the requested size.

        :param strategy: a callable that will be applied to rows or objects
         being iterated, which should return an object that represents the
         unique value of the row.   A Python ``set()`` is used to store
         these identities.   If not passed, a default uniqueness strategy
         is used which may have been assembled by the source of this
         :class:`_engine.Result` object.

        """
    def columns(self, *col_expressions: _KeyIndexType) -> Self:
        """Establish the columns that should be returned in each row.

        This method may be used to limit the columns returned as well
        as to reorder them.   The given list of expressions are normally
        a series of integers or string key names.   They may also be
        appropriate :class:`.ColumnElement` objects which correspond to
        a given statement construct.

        .. versionchanged:: 2.0  Due to a bug in 1.4, the
           :meth:`_engine.Result.columns` method had an incorrect behavior
           where calling upon the method with just one index would cause the
           :class:`_engine.Result` object to yield scalar values rather than
           :class:`_engine.Row` objects.   In version 2.0, this behavior
           has been corrected such that calling upon
           :meth:`_engine.Result.columns` with a single index will
           produce a :class:`_engine.Result` object that continues
           to yield :class:`_engine.Row` objects, which include
           only a single column.

        E.g.::

            statement = select(table.c.x, table.c.y, table.c.z)
            result = connection.execute(statement)

            for z, y in result.columns('z', 'y'):
                # ...


        Example of using the column objects from the statement itself::

            for z, y in result.columns(
                    statement.selected_columns.c.z,
                    statement.selected_columns.c.y
            ):
                # ...

        .. versionadded:: 1.4

        :param \\*col_expressions: indicates columns to be returned.  Elements
         may be integer row indexes, string column names, or appropriate
         :class:`.ColumnElement` objects corresponding to a select construct.

        :return: this :class:`_engine.Result` object with the modifications
         given.

        """
    @overload
    def scalars(self) -> ScalarResult[_T]: ...
    @overload
    def scalars(self, index: Literal[0]) -> ScalarResult[_T]: ...
    @overload
    def scalars(self, index: _KeyIndexType = 0) -> ScalarResult[Any]: ...
    def mappings(self) -> MappingResult:
        """Apply a mappings filter to returned rows, returning an instance of
        :class:`_engine.MappingResult`.

        When this filter is applied, fetching rows will return
        :class:`_engine.RowMapping` objects instead of :class:`_engine.Row`
        objects.

        .. versionadded:: 1.4

        :return: a new :class:`_engine.MappingResult` filtering object
         referring to this :class:`_engine.Result` object.

        """
    @property
    def t(self) -> TupleResult[_TP]:
        '''Apply a "typed tuple" typing filter to returned rows.

        The :attr:`_engine.Result.t` attribute is a synonym for
        calling the :meth:`_engine.Result.tuples` method.

        .. versionadded:: 2.0

        '''
    def tuples(self) -> TupleResult[_TP]:
        '''Apply a "typed tuple" typing filter to returned rows.

        This method returns the same :class:`_engine.Result` object
        at runtime,
        however annotates as returning a :class:`_engine.TupleResult` object
        that will indicate to :pep:`484` typing tools that plain typed
        ``Tuple`` instances are returned rather than rows.  This allows
        tuple unpacking and ``__getitem__`` access of :class:`_engine.Row`
        objects to by typed, for those cases where the statement invoked
        itself included typing information.

        .. versionadded:: 2.0

        :return: the :class:`_engine.TupleResult` type at typing time.

        .. seealso::

            :attr:`_engine.Result.t` - shorter synonym

            :attr:`_engine.Row._t` - :class:`_engine.Row` version

        '''
    def __iter__(self) -> Iterator[Row[_TP]]: ...
    def __next__(self) -> Row[_TP]: ...
    def partitions(self, size: int | None = None) -> Iterator[Sequence[Row[_TP]]]:
        """Iterate through sub-lists of rows of the size given.

        Each list will be of the size given, excluding the last list to
        be yielded, which may have a small number of rows.  No empty
        lists will be yielded.

        The result object is automatically closed when the iterator
        is fully consumed.

        Note that the backend driver will usually buffer the entire result
        ahead of time unless the
        :paramref:`.Connection.execution_options.stream_results` execution
        option is used indicating that the driver should not pre-buffer
        results, if possible.   Not all drivers support this option and
        the option is silently ignored for those who do not.

        When using the ORM, the :meth:`_engine.Result.partitions` method
        is typically more effective from a memory perspective when it is
        combined with use of the
        :ref:`yield_per execution option <orm_queryguide_yield_per>`,
        which instructs both the DBAPI driver to use server side cursors,
        if available, as well as instructs the ORM loading internals to only
        build a certain amount of ORM objects from a result at a time before
        yielding them out.

        .. versionadded:: 1.4

        :param size: indicate the maximum number of rows to be present
         in each list yielded.  If None, makes use of the value set by
         the :meth:`_engine.Result.yield_per`, method, if it were called,
         or the :paramref:`_engine.Connection.execution_options.yield_per`
         execution option, which is equivalent in this regard.  If
         yield_per weren't set, it makes use of the
         :meth:`_engine.Result.fetchmany` default, which may be backend
         specific and not well defined.

        :return: iterator of lists

        .. seealso::

            :ref:`engine_stream_results`

            :ref:`orm_queryguide_yield_per` - in the :ref:`queryguide_toplevel`

        """
    def fetchall(self) -> Sequence[Row[_TP]]:
        """A synonym for the :meth:`_engine.Result.all` method."""
    def fetchone(self) -> Row[_TP] | None:
        """Fetch one row.

        When all rows are exhausted, returns None.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch the first row of a result only, use the
        :meth:`_engine.Result.first` method.  To iterate through all
        rows, iterate the :class:`_engine.Result` object directly.

        :return: a :class:`_engine.Row` object if no filters are applied,
         or ``None`` if no rows remain.

        """
    def fetchmany(self, size: int | None = None) -> Sequence[Row[_TP]]:
        """Fetch many rows.

        When all rows are exhausted, returns an empty list.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch rows in groups, use the :meth:`_engine.Result.partitions`
        method.

        :return: a list of :class:`_engine.Row` objects.

        .. seealso::

            :meth:`_engine.Result.partitions`

        """
    def all(self) -> Sequence[Row[_TP]]:
        """Return all rows in a list.

        Closes the result set after invocation.   Subsequent invocations
        will return an empty list.

        .. versionadded:: 1.4

        :return: a list of :class:`_engine.Row` objects.

        .. seealso::

            :ref:`engine_stream_results` - How to stream a large result set
            without loading it completely in python.

        """
    def first(self) -> Row[_TP] | None:
        """Fetch the first row or ``None`` if no row is present.

        Closes the result set and discards remaining rows.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_engine.Result.scalar` method,
           or combine :meth:`_engine.Result.scalars` and
           :meth:`_engine.Result.first`.

           Additionally, in contrast to the behavior of the legacy  ORM
           :meth:`_orm.Query.first` method, **no limit is applied** to the
           SQL query which was invoked to produce this
           :class:`_engine.Result`;
           for a DBAPI driver that buffers results in memory before yielding
           rows, all rows will be sent to the Python process and all but
           the first row will be discarded.

           .. seealso::

                :ref:`migration_20_unify_select`

        :return: a :class:`_engine.Row` object, or None
         if no rows remain.

        .. seealso::

            :meth:`_engine.Result.scalar`

            :meth:`_engine.Result.one`

        """
    def one_or_none(self) -> Row[_TP] | None:
        """Return at most one result or raise an exception.

        Returns ``None`` if the result has no rows.
        Raises :class:`.MultipleResultsFound`
        if multiple rows are returned.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row` or ``None`` if no row
         is available.

        :raises: :class:`.MultipleResultsFound`

        .. seealso::

            :meth:`_engine.Result.first`

            :meth:`_engine.Result.one`

        """
    @overload
    def scalar_one(self) -> _T: ...
    @overload
    def scalar_one(self) -> Any: ...
    @overload
    def scalar_one_or_none(self) -> _T | None: ...
    @overload
    def scalar_one_or_none(self) -> Any | None: ...
    def one(self) -> Row[_TP]:
        """Return exactly one row or raise an exception.

        Raises :class:`.NoResultFound` if the result returns no
        rows, or :class:`.MultipleResultsFound` if multiple rows
        would be returned.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_engine.Result.scalar_one` method, or combine
           :meth:`_engine.Result.scalars` and
           :meth:`_engine.Result.one`.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row`.

        :raises: :class:`.MultipleResultsFound`, :class:`.NoResultFound`

        .. seealso::

            :meth:`_engine.Result.first`

            :meth:`_engine.Result.one_or_none`

            :meth:`_engine.Result.scalar_one`

        """
    @overload
    def scalar(self) -> _T | None: ...
    @overload
    def scalar(self) -> Any: ...
    def freeze(self) -> FrozenResult[_TP]:
        """Return a callable object that will produce copies of this
        :class:`_engine.Result` when invoked.

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
    def merge(self, *others: Result[Any]) -> MergedResult[_TP]:
        """Merge this :class:`_engine.Result` with other compatible result
        objects.

        The object returned is an instance of :class:`_engine.MergedResult`,
        which will be composed of iterators from the given result
        objects.

        The new result will use the metadata from this result object.
        The subsequent result objects must be against an identical
        set of result / cursor metadata, otherwise the behavior is
        undefined.

        """

class FilterResult(ResultInternal[_R]):
    """A wrapper for a :class:`_engine.Result` that returns objects other than
    :class:`_engine.Row` objects, such as dictionaries or scalar objects.

    :class:`_engine.FilterResult` is the common base for additional result
    APIs including :class:`_engine.MappingResult`,
    :class:`_engine.ScalarResult` and :class:`_engine.AsyncResult`.

    """
    def __enter__(self) -> Self: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def yield_per(self, num: int) -> Self:
        """Configure the row-fetching strategy to fetch ``num`` rows at a time.

        The :meth:`_engine.FilterResult.yield_per` method is a pass through
        to the :meth:`_engine.Result.yield_per` method.  See that method's
        documentation for usage notes.

        .. versionadded:: 1.4.40 - added :meth:`_engine.FilterResult.yield_per`
           so that the method is available on all result set implementations

        .. seealso::

            :ref:`engine_stream_results` - describes Core behavior for
            :meth:`_engine.Result.yield_per`

            :ref:`orm_queryguide_yield_per` - in the :ref:`queryguide_toplevel`

        """
    @property
    def closed(self) -> bool:
        """Return ``True`` if the underlying :class:`_engine.Result` reports
        closed

        .. versionadded:: 1.4.43

        """
    def close(self) -> None:
        """Close this :class:`_engine.FilterResult`.

        .. versionadded:: 1.4.43

        """

class ScalarResult(FilterResult[_R]):
    """A wrapper for a :class:`_engine.Result` that returns scalar values
    rather than :class:`_row.Row` values.

    The :class:`_engine.ScalarResult` object is acquired by calling the
    :meth:`_engine.Result.scalars` method.

    A special limitation of :class:`_engine.ScalarResult` is that it has
    no ``fetchone()`` method; since the semantics of ``fetchone()`` are that
    the ``None`` value indicates no more results, this is not compatible
    with :class:`_engine.ScalarResult` since there is no way to distinguish
    between ``None`` as a row value versus ``None`` as an indicator.  Use
    ``next(result)`` to receive values individually.

    """
    def __init__(self, real_result: Result[Any], index: _KeyIndexType) -> None: ...
    def unique(self, strategy: _UniqueFilterType | None = None) -> Self:
        """Apply unique filtering to the objects returned by this
        :class:`_engine.ScalarResult`.

        See :meth:`_engine.Result.unique` for usage details.

        """
    def partitions(self, size: int | None = None) -> Iterator[Sequence[_R]]:
        """Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_engine.Result.partitions` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    def fetchall(self) -> Sequence[_R]:
        """A synonym for the :meth:`_engine.ScalarResult.all` method."""
    def fetchmany(self, size: int | None = None) -> Sequence[_R]:
        """Fetch many objects.

        Equivalent to :meth:`_engine.Result.fetchmany` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    def all(self) -> Sequence[_R]:
        """Return all scalar values in a list.

        Equivalent to :meth:`_engine.Result.all` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    def __iter__(self) -> Iterator[_R]: ...
    def __next__(self) -> _R: ...
    def first(self) -> _R | None:
        """Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_engine.Result.first` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.


        """
    def one_or_none(self) -> _R | None:
        """Return at most one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one_or_none` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """
    def one(self) -> _R:
        """Return exactly one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        """

class TupleResult(FilterResult[_R], util.TypingOnly):
    """A :class:`_engine.Result` that's typed as returning plain
    Python tuples instead of rows.

    Since :class:`_engine.Row` acts like a tuple in every way already,
    this class is a typing only class, regular :class:`_engine.Result` is
    still used at runtime.

    """
    def partitions(self, size: int | None = None) -> Iterator[Sequence[_R]]:
        """Iterate through sub-lists of elements of the size given.

            Equivalent to :meth:`_engine.Result.partitions` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    def fetchone(self) -> _R | None:
        """Fetch one tuple.

            Equivalent to :meth:`_engine.Result.fetchone` except that
            tuple values, rather than :class:`_engine.Row`
            objects, are returned.

            """
    def fetchall(self) -> Sequence[_R]:
        """A synonym for the :meth:`_engine.ScalarResult.all` method."""
    def fetchmany(self, size: int | None = None) -> Sequence[_R]:
        """Fetch many objects.

            Equivalent to :meth:`_engine.Result.fetchmany` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    def all(self) -> Sequence[_R]:
        """Return all scalar values in a list.

            Equivalent to :meth:`_engine.Result.all` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    def __iter__(self) -> Iterator[_R]: ...
    def __next__(self) -> _R: ...
    def first(self) -> _R | None:
        """Fetch the first object or ``None`` if no object is present.

            Equivalent to :meth:`_engine.Result.first` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.


            """
    def one_or_none(self) -> _R | None:
        """Return at most one object or raise an exception.

            Equivalent to :meth:`_engine.Result.one_or_none` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    def one(self) -> _R:
        """Return exactly one object or raise an exception.

            Equivalent to :meth:`_engine.Result.one` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            """
    @overload
    def scalar_one(self) -> _T: ...
    @overload
    def scalar_one(self) -> Any: ...
    @overload
    def scalar_one_or_none(self) -> _T | None: ...
    @overload
    def scalar_one_or_none(self) -> Any | None: ...
    @overload
    def scalar(self) -> _T | None: ...
    @overload
    def scalar(self) -> Any: ...

class MappingResult(_WithKeys, FilterResult[RowMapping]):
    """A wrapper for a :class:`_engine.Result` that returns dictionary values
    rather than :class:`_engine.Row` values.

    The :class:`_engine.MappingResult` object is acquired by calling the
    :meth:`_engine.Result.mappings` method.

    """
    def __init__(self, result: Result[Any]) -> None: ...
    def unique(self, strategy: _UniqueFilterType | None = None) -> Self:
        """Apply unique filtering to the objects returned by this
        :class:`_engine.MappingResult`.

        See :meth:`_engine.Result.unique` for usage details.

        """
    def columns(self, *col_expressions: _KeyIndexType) -> Self:
        """Establish the columns that should be returned in each row."""
    def partitions(self, size: int | None = None) -> Iterator[Sequence[RowMapping]]:
        """Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_engine.Result.partitions` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    def fetchall(self) -> Sequence[RowMapping]:
        """A synonym for the :meth:`_engine.MappingResult.all` method."""
    def fetchone(self) -> RowMapping | None:
        """Fetch one object.

        Equivalent to :meth:`_engine.Result.fetchone` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    def fetchmany(self, size: int | None = None) -> Sequence[RowMapping]:
        """Fetch many objects.

        Equivalent to :meth:`_engine.Result.fetchmany` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    def all(self) -> Sequence[RowMapping]:
        """Return all scalar values in a list.

        Equivalent to :meth:`_engine.Result.all` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    def __iter__(self) -> Iterator[RowMapping]: ...
    def __next__(self) -> RowMapping: ...
    def first(self) -> RowMapping | None:
        """Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_engine.Result.first` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.


        """
    def one_or_none(self) -> RowMapping | None:
        """Return at most one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one_or_none` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """
    def one(self) -> RowMapping:
        """Return exactly one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        """

class FrozenResult(Generic[_TP]):
    '''Represents a :class:`_engine.Result` object in a "frozen" state suitable
    for caching.

    The :class:`_engine.FrozenResult` object is returned from the
    :meth:`_engine.Result.freeze` method of any :class:`_engine.Result`
    object.

    A new iterable :class:`_engine.Result` object is generated from a fixed
    set of data each time the :class:`_engine.FrozenResult` is invoked as
    a callable::


        result = connection.execute(query)

        frozen = result.freeze()

        unfrozen_result_one = frozen()

        for row in unfrozen_result_one:
            print(row)

        unfrozen_result_two = frozen()
        rows = unfrozen_result_two.all()

        # ... etc

    .. versionadded:: 1.4

    .. seealso::

        :ref:`do_orm_execute_re_executing` - example usage within the
        ORM to implement a result-set cache.

        :func:`_orm.loading.merge_frozen_result` - ORM function to merge
        a frozen result back into a :class:`_orm.Session`.

    '''
    data: Sequence[Any]
    metadata: Incomplete
    def __init__(self, result: Result[_TP]) -> None: ...
    def rewrite_rows(self) -> Sequence[Sequence[Any]]: ...
    def with_new_rows(self, tuple_data: Sequence[Row[_TP]]) -> FrozenResult[_TP]: ...
    def __call__(self) -> Result[_TP]: ...

class IteratorResult(Result[_TP]):
    """A :class:`_engine.Result` that gets data from a Python iterator of
    :class:`_engine.Row` objects or similar row-like data.

    .. versionadded:: 1.4

    """
    iterator: Incomplete
    raw: Incomplete
    def __init__(self, cursor_metadata: ResultMetaData, iterator: Iterator[_InterimSupportsScalarsRowType], raw: Result[Any] | None = None, _source_supports_scalars: bool = False) -> None: ...
    @property
    def closed(self) -> bool:
        """Return ``True`` if this :class:`_engine.IteratorResult` has
        been closed

        .. versionadded:: 1.4.43

        """

def null_result() -> IteratorResult[Any]: ...

class ChunkedIteratorResult(IteratorResult[_TP]):
    """An :class:`_engine.IteratorResult` that works from an
    iterator-producing callable.

    The given ``chunks`` argument is a function that is given a number of rows
    to return in each chunk, or ``None`` for all rows.  The function should
    then return an un-consumed iterator of lists, each list of the requested
    size.

    The function can be called at any time again, in which case it should
    continue from the same result set but adjust the chunk size as given.

    .. versionadded:: 1.4

    """
    chunks: Incomplete
    raw: Incomplete
    iterator: Incomplete
    dynamic_yield_per: Incomplete
    def __init__(self, cursor_metadata: ResultMetaData, chunks: Callable[[int | None], Iterator[Sequence[_InterimRowType[_R]]]], source_supports_scalars: bool = False, raw: Result[Any] | None = None, dynamic_yield_per: bool = False) -> None: ...
    def yield_per(self, num: int) -> Self: ...

class MergedResult(IteratorResult[_TP]):
    """A :class:`_engine.Result` that is merged from any number of
    :class:`_engine.Result` objects.

    Returned by the :meth:`_engine.Result.merge` method.

    .. versionadded:: 1.4

    """
    closed: bool
    rowcount: int | None
    def __init__(self, cursor_metadata: ResultMetaData, results: Sequence[Result[_TP]]) -> None: ...
