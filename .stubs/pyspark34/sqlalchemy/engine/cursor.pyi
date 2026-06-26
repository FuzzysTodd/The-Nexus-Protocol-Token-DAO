from .. import exc as exc, util as util
from ..sql import elements as elements, sqltypes as sqltypes
from ..sql.compiler import RM_NAME as RM_NAME, RM_OBJECTS as RM_OBJECTS, RM_RENDERED_NAME as RM_RENDERED_NAME, RM_TYPE as RM_TYPE, ResultColumnsEntry as ResultColumnsEntry
from ..sql.type_api import TypeEngine as TypeEngine
from ..util import compat as compat
from ..util.typing import Literal as Literal, Self as Self
from .base import Connection as Connection
from .default import DefaultExecutionContext as DefaultExecutionContext
from .interfaces import DBAPICursor as DBAPICursor, Dialect as Dialect, ExecutionContext as ExecutionContext, _DBAPICursorDescription
from .result import IteratorResult as IteratorResult, MergedResult as MergedResult, Result as Result, ResultMetaData as ResultMetaData, SimpleResultMetaData as SimpleResultMetaData, tuplegetter as tuplegetter
from .row import Row as Row
from _typeshed import Incomplete
from typing import Any, ClassVar, NoReturn

MD_INDEX: Literal[0]
MD_RESULT_MAP_INDEX: Literal[1]
MD_OBJECTS: Literal[2]
MD_LOOKUP_KEY: Literal[3]
MD_RENDERED_NAME: Literal[4]
MD_PROCESSOR: Literal[5]
MD_UNTRANSLATED: Literal[6]

class CursorResultMetaData(ResultMetaData):
    """Result metadata for DBAPI cursors."""
    returns_rows: ClassVar[bool]
    def __init__(self, parent: CursorResult[Any], cursor_description: _DBAPICursorDescription) -> None: ...

class ResultFetchStrategy:
    """Define a fetching strategy for a result object.


    .. versionadded:: 1.4

    """
    alternate_cursor_description: _DBAPICursorDescription | None
    def soft_close(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None) -> None: ...
    def hard_close(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None) -> None: ...
    def yield_per(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None, num: int) -> None: ...
    def fetchone(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor, hard_close: bool = False) -> Any: ...
    def fetchmany(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor, size: int | None = None) -> Any: ...
    def fetchall(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor) -> Any: ...
    def handle_exception(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None, err: BaseException) -> NoReturn: ...

class NoCursorFetchStrategy(ResultFetchStrategy):
    """Cursor strategy for a result that has no open cursor.

    There are two varieties of this strategy, one for DQL and one for
    DML (and also DDL), each of which represent a result that had a cursor
    but no longer has one.

    """
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = False): ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = None): ...
    def fetchall(self, result, dbapi_cursor): ...

class NoCursorDQLFetchStrategy(NoCursorFetchStrategy):
    '''Cursor strategy for a DQL result that has no open cursor.

    This is a result set that can return rows, i.e. for a SELECT, or for an
    INSERT, UPDATE, DELETE that includes RETURNING. However it is in the state
    where the cursor is closed and no rows remain available.  The owning result
    object may or may not be "hard closed", which determines if the fetch
    methods send empty results or raise for closed result.

    '''
class NoCursorDMLFetchStrategy(NoCursorFetchStrategy):
    """Cursor strategy for a DML result that has no open cursor.

    This is a result set that does not return rows, i.e. for an INSERT,
    UPDATE, DELETE that does not include RETURNING.

    """

class CursorFetchStrategy(ResultFetchStrategy):
    """Call fetch methods from a DBAPI cursor.

    Alternate versions of this class may instead buffer the rows from
    cursors or not use cursors at all.

    """
    def soft_close(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None) -> None: ...
    def hard_close(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None) -> None: ...
    def handle_exception(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None, err: BaseException) -> NoReturn: ...
    def yield_per(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor | None, num: int) -> None: ...
    def fetchone(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor, hard_close: bool = False) -> Any: ...
    def fetchmany(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor, size: int | None = None) -> Any: ...
    def fetchall(self, result: CursorResult[Any], dbapi_cursor: DBAPICursor) -> Any: ...

class BufferedRowCursorFetchStrategy(CursorFetchStrategy):
    '''A cursor fetch strategy with row buffering behavior.

    This strategy buffers the contents of a selection of rows
    before ``fetchone()`` is called.  This is to allow the results of
    ``cursor.description`` to be available immediately, when
    interfacing with a DB-API that requires rows to be consumed before
    this information is available (currently psycopg2, when used with
    server-side cursors).

    The pre-fetching behavior fetches only one row initially, and then
    grows its buffer size by a fixed amount with each successive need
    for additional rows up the ``max_row_buffer`` size, which defaults
    to 1000::

        with psycopg2_engine.connect() as conn:

            result = conn.execution_options(
                stream_results=True, max_row_buffer=50
                ).execute(text("select * from table"))

    .. versionadded:: 1.4 ``max_row_buffer`` may now exceed 1000 rows.

    .. seealso::

        :ref:`psycopg2_execution_options`
    '''
    def __init__(self, dbapi_cursor, execution_options, growth_factor: int = 5, initial_buffer: Incomplete | None = None) -> None: ...
    @classmethod
    def create(cls, result): ...
    def yield_per(self, result, dbapi_cursor, num) -> None: ...
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = False): ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = None): ...
    def fetchall(self, result, dbapi_cursor): ...

class FullyBufferedCursorFetchStrategy(CursorFetchStrategy):
    """A cursor strategy that buffers rows fully upon creation.

    Used for operations where a result is to be delivered
    after the database conversation can not be continued,
    such as MSSQL INSERT...OUTPUT after an autocommit.

    """
    alternate_cursor_description: Incomplete
    def __init__(self, dbapi_cursor, alternate_description: Incomplete | None = None, initial_buffer: Incomplete | None = None) -> None: ...
    def yield_per(self, result, dbapi_cursor, num) -> None: ...
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = False): ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = None): ...
    def fetchall(self, result, dbapi_cursor): ...

class _NoResultMetaData(ResultMetaData):
    returns_rows: bool
    @property
    def keys(self) -> None: ...

def null_dml_result() -> IteratorResult[Any]: ...

class CursorResult(Result[_T]):
    """A Result that is representing state from a DBAPI cursor.

    .. versionchanged:: 1.4  The :class:`.CursorResult``
       class replaces the previous :class:`.ResultProxy` interface.
       This classes are based on the :class:`.Result` calling API
       which provides an updated usage model and calling facade for
       SQLAlchemy Core and SQLAlchemy ORM.

    Returns database rows via the :class:`.Row` class, which provides
    additional API features and behaviors on top of the raw data returned by
    the DBAPI.   Through the use of filters such as the :meth:`.Result.scalars`
    method, other kinds of objects may also be returned.

    .. seealso::

        :ref:`tutorial_selecting_data` - introductory material for accessing
        :class:`_engine.CursorResult` and :class:`.Row` objects.

    """
    closed: bool
    context: DefaultExecutionContext
    dialect: Dialect
    cursor_strategy: ResultFetchStrategy
    connection: Connection
    cursor: Incomplete
    def __init__(self, context: DefaultExecutionContext, cursor_strategy: ResultFetchStrategy, cursor_description: _DBAPICursorDescription | None) -> None: ...
    @property
    def inserted_primary_key_rows(self):
        '''Return the value of
        :attr:`_engine.CursorResult.inserted_primary_key`
        as a row contained within a list; some dialects may support a
        multiple row form as well.

        .. note:: As indicated below, in current SQLAlchemy versions this
           accessor is only useful beyond what\'s already supplied by
           :attr:`_engine.CursorResult.inserted_primary_key` when using the
           :ref:`postgresql_psycopg2` dialect.   Future versions hope to
           generalize this feature to more dialects.

        This accessor is added to support dialects that offer the feature
        that is currently implemented by the :ref:`psycopg2_executemany_mode`
        feature, currently **only the psycopg2 dialect**, which provides
        for many rows to be INSERTed at once while still retaining the
        behavior of being able to return server-generated primary key values.

        * **When using the psycopg2 dialect, or other dialects that may support
          "fast executemany" style inserts in upcoming releases** : When
          invoking an INSERT statement while passing a list of rows as the
          second argument to :meth:`_engine.Connection.execute`, this accessor
          will then provide a list of rows, where each row contains the primary
          key value for each row that was INSERTed.

        * **When using all other dialects / backends that don\'t yet support
          this feature**: This accessor is only useful for **single row INSERT
          statements**, and returns the same information as that of the
          :attr:`_engine.CursorResult.inserted_primary_key` within a
          single-element list. When an INSERT statement is executed in
          conjunction with a list of rows to be INSERTed, the list will contain
          one row per row inserted in the statement, however it will contain
          ``None`` for any server-generated values.

        Future releases of SQLAlchemy will further generalize the
        "fast execution helper" feature of psycopg2 to suit other dialects,
        thus allowing this accessor to be of more general use.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.CursorResult.inserted_primary_key`

        '''
    @property
    def inserted_primary_key(self):
        '''Return the primary key for the row just inserted.

        The return value is a :class:`_result.Row` object representing
        a named tuple of primary key values in the order in which the
        primary key columns are configured in the source
        :class:`_schema.Table`.

        .. versionchanged:: 1.4.8 - the
           :attr:`_engine.CursorResult.inserted_primary_key`
           value is now a named tuple via the :class:`_result.Row` class,
           rather than a plain tuple.

        This accessor only applies to single row :func:`_expression.insert`
        constructs which did not explicitly specify
        :meth:`_expression.Insert.returning`.    Support for multirow inserts,
        while not yet available for most backends, would be accessed using
        the :attr:`_engine.CursorResult.inserted_primary_key_rows` accessor.

        Note that primary key columns which specify a server_default clause, or
        otherwise do not qualify as "autoincrement" columns (see the notes at
        :class:`_schema.Column`), and were generated using the database-side
        default, will appear in this list as ``None`` unless the backend
        supports "returning" and the insert statement executed with the
        "implicit returning" enabled.

        Raises :class:`~sqlalchemy.exc.InvalidRequestError` if the executed
        statement is not a compiled expression construct
        or is not an insert() construct.

        '''
    def last_updated_params(self):
        """Return the collection of updated parameters from this
        execution.

        Raises :class:`~sqlalchemy.exc.InvalidRequestError` if the executed
        statement is not a compiled expression construct
        or is not an update() construct.

        """
    def last_inserted_params(self):
        """Return the collection of inserted parameters from this
        execution.

        Raises :class:`~sqlalchemy.exc.InvalidRequestError` if the executed
        statement is not a compiled expression construct
        or is not an insert() construct.

        """
    @property
    def returned_defaults_rows(self):
        """Return a list of rows each containing the values of default
        columns that were fetched using
        the :meth:`.ValuesBase.return_defaults` feature.

        The return value is a list of :class:`.Row` objects.

        .. versionadded:: 1.4

        """
    def splice_horizontally(self, other):
        '''Return a new :class:`.CursorResult` that "horizontally splices"
        together the rows of this :class:`.CursorResult` with that of another
        :class:`.CursorResult`.

        .. tip::  This method is for the benefit of the SQLAlchemy ORM and is
           not intended for general use.

        "horizontally splices" means that for each row in the first and second
        result sets, a new row that concatenates the two rows together is
        produced, which then becomes the new row.  The incoming
        :class:`.CursorResult` must have the identical number of rows.  It is
        typically expected that the two result sets come from the same sort
        order as well, as the result rows are spliced together based on their
        position in the result.

        The expected use case here is so that multiple INSERT..RETURNING
        statements (which definitely need to be sorted) against different
        tables can produce a single result that looks like a JOIN of those two
        tables.

        E.g.::

            r1 = connection.execute(
                users.insert().returning(
                    users.c.user_name,
                    users.c.user_id,
                    sort_by_parameter_order=True
                ),
                user_values
            )

            r2 = connection.execute(
                addresses.insert().returning(
                    addresses.c.address_id,
                    addresses.c.address,
                    addresses.c.user_id,
                    sort_by_parameter_order=True
                ),
                address_values
            )

            rows = r1.splice_horizontally(r2).all()
            assert (
                rows ==
                [
                    ("john", 1, 1, "foo@bar.com", 1),
                    ("jack", 2, 2, "bar@bat.com", 2),
                ]
            )

        .. versionadded:: 2.0

        .. seealso::

            :meth:`.CursorResult.splice_vertically`


        '''
    def splice_vertically(self, other):
        '''Return a new :class:`.CursorResult` that "vertically splices",
        i.e. "extends", the rows of this :class:`.CursorResult` with that of
        another :class:`.CursorResult`.

        .. tip::  This method is for the benefit of the SQLAlchemy ORM and is
           not intended for general use.

        "vertically splices" means the rows of the given result are appended to
        the rows of this cursor result. The incoming :class:`.CursorResult`
        must have rows that represent the identical list of columns in the
        identical order as they are in this :class:`.CursorResult`.

        .. versionadded:: 2.0

        .. seealso::

            :meth:`.CursorResult.splice_horizontally`

        '''
    @property
    def returned_defaults(self):
        """Return the values of default columns that were fetched using
        the :meth:`.ValuesBase.return_defaults` feature.

        The value is an instance of :class:`.Row`, or ``None``
        if :meth:`.ValuesBase.return_defaults` was not used or if the
        backend does not support RETURNING.

        .. seealso::

            :meth:`.ValuesBase.return_defaults`

        """
    def lastrow_has_defaults(self):
        """Return ``lastrow_has_defaults()`` from the underlying
        :class:`.ExecutionContext`.

        See :class:`.ExecutionContext` for details.

        """
    def postfetch_cols(self):
        """Return ``postfetch_cols()`` from the underlying
        :class:`.ExecutionContext`.

        See :class:`.ExecutionContext` for details.

        Raises :class:`~sqlalchemy.exc.InvalidRequestError` if the executed
        statement is not a compiled expression construct
        or is not an insert() or update() construct.

        """
    def prefetch_cols(self):
        """Return ``prefetch_cols()`` from the underlying
        :class:`.ExecutionContext`.

        See :class:`.ExecutionContext` for details.

        Raises :class:`~sqlalchemy.exc.InvalidRequestError` if the executed
        statement is not a compiled expression construct
        or is not an insert() or update() construct.

        """
    def supports_sane_rowcount(self):
        """Return ``supports_sane_rowcount`` from the dialect.

        See :attr:`_engine.CursorResult.rowcount` for background.

        """
    def supports_sane_multi_rowcount(self):
        """Return ``supports_sane_multi_rowcount`` from the dialect.

        See :attr:`_engine.CursorResult.rowcount` for background.

        """
    def rowcount(self) -> int:
        """Return the 'rowcount' for this result.

        The 'rowcount' reports the number of rows *matched*
        by the WHERE criterion of an UPDATE or DELETE statement.

        .. note::

           Notes regarding :attr:`_engine.CursorResult.rowcount`:


           * This attribute returns the number of rows *matched*,
             which is not necessarily the same as the number of rows
             that were actually *modified* - an UPDATE statement, for example,
             may have no net change on a given row if the SET values
             given are the same as those present in the row already.
             Such a row would be matched but not modified.
             On backends that feature both styles, such as MySQL,
             rowcount is configured by default to return the match
             count in all cases.

           * :attr:`_engine.CursorResult.rowcount`
             is *only* useful in conjunction
             with an UPDATE or DELETE statement.  Contrary to what the Python
             DBAPI says, it does *not* reliably return the
             number of rows available from the results of a SELECT statement
             as DBAPIs cannot support this functionality when rows are
             unbuffered.

           * :attr:`_engine.CursorResult.rowcount`
             may not be fully implemented by
             all dialects.  In particular, most DBAPIs do not support an
             aggregate rowcount result from an executemany call.
             The :meth:`_engine.CursorResult.supports_sane_rowcount` and
             :meth:`_engine.CursorResult.supports_sane_multi_rowcount` methods
             will report from the dialect if each usage is known to be
             supported.

           * Statements that use RETURNING may not return a correct
             rowcount.

        .. seealso::

            :ref:`tutorial_update_delete_rowcount` - in the :ref:`unified_tutorial`

        """
    @property
    def lastrowid(self):
        """Return the 'lastrowid' accessor on the DBAPI cursor.

        This is a DBAPI specific method and is only functional
        for those backends which support it, for statements
        where it is appropriate.  It's behavior is not
        consistent across backends.

        Usage of this method is normally unnecessary when
        using insert() expression constructs; the
        :attr:`~CursorResult.inserted_primary_key` attribute provides a
        tuple of primary key values for a newly inserted row,
        regardless of database backend.

        """
    @property
    def returns_rows(self):
        """True if this :class:`_engine.CursorResult` returns zero or more
        rows.

        I.e. if it is legal to call the methods
        :meth:`_engine.CursorResult.fetchone`,
        :meth:`_engine.CursorResult.fetchmany`
        :meth:`_engine.CursorResult.fetchall`.

        Overall, the value of :attr:`_engine.CursorResult.returns_rows` should
        always be synonymous with whether or not the DBAPI cursor had a
        ``.description`` attribute, indicating the presence of result columns,
        noting that a cursor that returns zero rows still has a
        ``.description`` if a row-returning statement was emitted.

        This attribute should be True for all results that are against
        SELECT statements, as well as for DML statements INSERT/UPDATE/DELETE
        that use RETURNING.   For INSERT/UPDATE/DELETE statements that were
        not using RETURNING, the value will usually be False, however
        there are some dialect-specific exceptions to this, such as when
        using the MSSQL / pyodbc dialect a SELECT is emitted inline in
        order to retrieve an inserted primary key value.


        """
    @property
    def is_insert(self):
        '''True if this :class:`_engine.CursorResult` is the result
        of a executing an expression language compiled
        :func:`_expression.insert` construct.

        When True, this implies that the
        :attr:`inserted_primary_key` attribute is accessible,
        assuming the statement did not include
        a user defined "returning" construct.

        '''
    def merge(self, *others: Result[Any]) -> MergedResult[Any]: ...
    def close(self) -> Any:
        """Close this :class:`_engine.CursorResult`.

        This closes out the underlying DBAPI cursor corresponding to the
        statement execution, if one is still present.  Note that the DBAPI
        cursor is automatically released when the :class:`_engine.CursorResult`
        exhausts all available rows.  :meth:`_engine.CursorResult.close` is
        generally an optional method except in the case when discarding a
        :class:`_engine.CursorResult` that still has additional rows pending
        for fetch.

        After this method is called, it is no longer valid to call upon
        the fetch methods, which will raise a :class:`.ResourceClosedError`
        on subsequent use.

        .. seealso::

            :ref:`connections_toplevel`

        """
    def yield_per(self, num: int) -> Self: ...
ResultProxy = CursorResult
