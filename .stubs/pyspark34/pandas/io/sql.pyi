import abc
import numpy as np
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator
from contextlib import ExitStack
from pandas import get_option as get_option
from pandas._libs import lib as lib
from pandas._typing import DateTimeErrorChoices as DateTimeErrorChoices, DtypeArg as DtypeArg, DtypeBackend as DtypeBackend, IndexLabel as IndexLabel
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.api import DataFrame as DataFrame, Series as Series
from pandas.core.arrays import ArrowExtensionArray as ArrowExtensionArray
from pandas.core.base import PandasObject as PandasObject
from pandas.core.dtypes.common import is_datetime64tz_dtype as is_datetime64tz_dtype, is_dict_like as is_dict_like, is_integer as is_integer, is_list_like as is_list_like
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.internals.construction import convert_object_array as convert_object_array
from pandas.core.tools.datetimes import to_datetime as to_datetime
from pandas.errors import AbstractMethodError as AbstractMethodError, DatabaseError as DatabaseError
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from sqlalchemy import Table
from sqlalchemy.sql.expression import Select as Select, TextClause as TextClause
from typing import Iterator, Literal, overload

def execute(sql, con, params: Incomplete | None = None):
    """
    Execute the given SQL query using the provided connection object.

    Parameters
    ----------
    sql : string
        SQL query to be executed.
    con : SQLAlchemy connection or sqlite3 connection
        If a DBAPI2 object, only sqlite3 is supported.
    params : list or tuple, optional, default: None
        List of parameters to pass to execute method.

    Returns
    -------
    Results Iterable
    """
@overload
def read_sql_table(table_name, con, schema=..., index_col: str | list[str] | None = ..., coerce_float=..., parse_dates: list[str] | dict[str, str] | None = ..., columns: list[str] | None = ..., chunksize: None = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
@overload
def read_sql_table(table_name, con, schema=..., index_col: str | list[str] | None = ..., coerce_float=..., parse_dates: list[str] | dict[str, str] | None = ..., columns: list[str] | None = ..., chunksize: int = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> Iterator[DataFrame]: ...
@overload
def read_sql_query(sql, con, index_col: str | list[str] | None = ..., coerce_float=..., params: list[str] | dict[str, str] | None = ..., parse_dates: list[str] | dict[str, str] | None = ..., chunksize: None = ..., dtype: DtypeArg | None = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
@overload
def read_sql_query(sql, con, index_col: str | list[str] | None = ..., coerce_float=..., params: list[str] | dict[str, str] | None = ..., parse_dates: list[str] | dict[str, str] | None = ..., chunksize: int = ..., dtype: DtypeArg | None = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> Iterator[DataFrame]: ...
@overload
def read_sql(sql, con, index_col: str | list[str] | None = ..., coerce_float=..., params=..., parse_dates=..., columns: list[str] = ..., chunksize: None = ..., dtype_backend: DtypeBackend | lib.NoDefault = ..., dtype: DtypeArg | None = None) -> DataFrame: ...
@overload
def read_sql(sql, con, index_col: str | list[str] | None = ..., coerce_float=..., params=..., parse_dates=..., columns: list[str] = ..., chunksize: int = ..., dtype_backend: DtypeBackend | lib.NoDefault = ..., dtype: DtypeArg | None = None) -> Iterator[DataFrame]: ...
def to_sql(frame, name: str, con, schema: str | None = None, if_exists: Literal['fail', 'replace', 'append'] = 'fail', index: bool = True, index_label: IndexLabel = None, chunksize: int | None = None, dtype: DtypeArg | None = None, method: str | None = None, engine: str = 'auto', **engine_kwargs) -> int | None:
    """
    Write records stored in a DataFrame to a SQL database.

    Parameters
    ----------
    frame : DataFrame, Series
    name : str
        Name of SQL table.
    con : SQLAlchemy connectable(engine/connection) or database string URI
        or sqlite3 DBAPI2 connection
        Using SQLAlchemy makes it possible to use any DB supported by that
        library.
        If a DBAPI2 object, only sqlite3 is supported.
    schema : str, optional
        Name of SQL schema in database to write to (if database flavor
        supports this). If None, use default schema (default).
    if_exists : {'fail', 'replace', 'append'}, default 'fail'
        - fail: If table exists, do nothing.
        - replace: If table exists, drop it, recreate it, and insert data.
        - append: If table exists, insert data. Create if does not exist.
    index : bool, default True
        Write DataFrame index as a column.
    index_label : str or sequence, optional
        Column label for index column(s). If None is given (default) and
        `index` is True, then the index names are used.
        A sequence should be given if the DataFrame uses MultiIndex.
    chunksize : int, optional
        Specify the number of rows in each batch to be written at a time.
        By default, all rows will be written at once.
    dtype : dict or scalar, optional
        Specifying the datatype for columns. If a dictionary is used, the
        keys should be the column names and the values should be the
        SQLAlchemy types or strings for the sqlite3 fallback mode. If a
        scalar is provided, it will be applied to all columns.
    method : {None, 'multi', callable}, optional
        Controls the SQL insertion clause used:

        - None : Uses standard SQL ``INSERT`` clause (one per row).
        - ``'multi'``: Pass multiple values in a single ``INSERT`` clause.
        - callable with signature ``(pd_table, conn, keys, data_iter) -> int | None``.

        Details and a sample callable implementation can be found in the
        section :ref:`insert method <io.sql.method>`.
    engine : {'auto', 'sqlalchemy'}, default 'auto'
        SQL engine library to use. If 'auto', then the option
        ``io.sql.engine`` is used. The default ``io.sql.engine``
        behavior is 'sqlalchemy'

        .. versionadded:: 1.3.0

    **engine_kwargs
        Any additional kwargs are passed to the engine.

    Returns
    -------
    None or int
        Number of rows affected by to_sql. None is returned if the callable
        passed into ``method`` does not return an integer number of rows.

        .. versionadded:: 1.4.0

    Notes
    -----
    The returned rows affected is the sum of the ``rowcount`` attribute of ``sqlite3.Cursor``
    or SQLAlchemy connectable. The returned value may not reflect the exact number of written
    rows as stipulated in the
    `sqlite3 <https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.rowcount>`__ or
    `SQLAlchemy <https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.BaseCursorResult.rowcount>`__
    """
def has_table(table_name: str, con, schema: str | None = None) -> bool:
    """
    Check if DataBase has named table.

    Parameters
    ----------
    table_name: string
        Name of SQL table.
    con: SQLAlchemy connectable(engine/connection) or sqlite3 DBAPI2 connection
        Using SQLAlchemy makes it possible to use any DB supported by that
        library.
        If a DBAPI2 object, only sqlite3 is supported.
    schema : string, default None
        Name of SQL schema in database to write to (if database flavor supports
        this). If None, use default schema (default).

    Returns
    -------
    boolean
    """
table_exists = has_table

def pandasSQL_builder(con, schema: str | None = None, need_transaction: bool = False) -> PandasSQL:
    """
    Convenience function to return the correct PandasSQL subclass based on the
    provided parameters.  Also creates a sqlalchemy connection and transaction
    if necessary.
    """

class SQLTable(PandasObject):
    """
    For mapping Pandas tables to SQL tables.
    Uses fact that table is reflected by SQLAlchemy to
    do better type conversions.
    Also holds various flags needed to avoid having to
    pass them between functions all the time.
    """
    name: Incomplete
    pd_sql: Incomplete
    prefix: Incomplete
    frame: Incomplete
    index: Incomplete
    schema: Incomplete
    if_exists: Incomplete
    keys: Incomplete
    dtype: Incomplete
    table: Incomplete
    def __init__(self, name: str, pandas_sql_engine, frame: Incomplete | None = None, index: bool | str | list[str] | None = True, if_exists: Literal['fail', 'replace', 'append'] = 'fail', prefix: str = 'pandas', index_label: Incomplete | None = None, schema: Incomplete | None = None, keys: Incomplete | None = None, dtype: DtypeArg | None = None) -> None: ...
    def exists(self): ...
    def sql_schema(self) -> str: ...
    def create(self) -> None: ...
    def insert_data(self) -> tuple[list[str], list[np.ndarray]]: ...
    def insert(self, chunksize: int | None = None, method: str | None = None) -> int | None: ...
    def read(self, exit_stack: ExitStack, coerce_float: bool = True, parse_dates: Incomplete | None = None, columns: Incomplete | None = None, chunksize: Incomplete | None = None, dtype_backend: DtypeBackend | Literal['numpy'] = 'numpy') -> DataFrame | Iterator[DataFrame]: ...

class PandasSQL(PandasObject, ABC, metaclass=abc.ABCMeta):
    """
    Subclasses Should define read_query and to_sql.
    """
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def read_table(self, table_name: str, index_col: str | list[str] | None = None, coerce_float: bool = True, parse_dates: Incomplete | None = None, columns: Incomplete | None = None, schema: str | None = None, chunksize: int | None = None, dtype_backend: DtypeBackend | Literal['numpy'] = 'numpy') -> DataFrame | Iterator[DataFrame]: ...
    @abstractmethod
    def read_query(self, sql: str, index_col: str | list[str] | None = None, coerce_float: bool = True, parse_dates: Incomplete | None = None, params: Incomplete | None = None, chunksize: int | None = None, dtype: DtypeArg | None = None, dtype_backend: DtypeBackend | Literal['numpy'] = 'numpy') -> DataFrame | Iterator[DataFrame]: ...
    @abstractmethod
    def to_sql(self, frame, name, if_exists: Literal['fail', 'replace', 'append'] = 'fail', index: bool = True, index_label: Incomplete | None = None, schema: Incomplete | None = None, chunksize: Incomplete | None = None, dtype: DtypeArg | None = None, method: Incomplete | None = None, engine: str = 'auto', **engine_kwargs) -> int | None: ...
    @abstractmethod
    def execute(self, sql: str | Select | TextClause, params: Incomplete | None = None): ...
    @abstractmethod
    def has_table(self, name: str, schema: str | None = None) -> bool: ...

class BaseEngine:
    def insert_records(self, table: SQLTable, con, frame, name, index: bool | str | list[str] | None = True, schema: Incomplete | None = None, chunksize: Incomplete | None = None, method: Incomplete | None = None, **engine_kwargs) -> int | None:
        """
        Inserts data into already-prepared table
        """

class SQLAlchemyEngine(BaseEngine):
    def __init__(self) -> None: ...
    def insert_records(self, table: SQLTable, con, frame, name, index: bool | str | list[str] | None = True, schema: Incomplete | None = None, chunksize: Incomplete | None = None, method: Incomplete | None = None, **engine_kwargs) -> int | None: ...

def get_engine(engine: str) -> BaseEngine:
    """return our implementation"""

class SQLDatabase(PandasSQL):
    """
    This class enables conversion between DataFrame and SQL databases
    using SQLAlchemy to handle DataBase abstraction.

    Parameters
    ----------
    con : SQLAlchemy Connectable or URI string.
        Connectable to connect with the database. Using SQLAlchemy makes it
        possible to use any DB supported by that library.
    schema : string, default None
        Name of SQL schema in database to write to (if database flavor
        supports this). If None, use default schema (default).
    need_transaction : bool, default False
        If True, SQLDatabase will create a transaction.

    """
    exit_stack: Incomplete
    con: Incomplete
    meta: Incomplete
    returns_generator: bool
    def __init__(self, con, schema: str | None = None, need_transaction: bool = False) -> None: ...
    def __exit__(self, *args) -> None: ...
    def run_transaction(self) -> Generator[Incomplete, None, None]: ...
    def execute(self, sql: str | Select | TextClause, params: Incomplete | None = None):
        """Simple passthrough to SQLAlchemy connectable"""
    def read_table(self, table_name: str, index_col: str | list[str] | None = None, coerce_float: bool = True, parse_dates: Incomplete | None = None, columns: Incomplete | None = None, schema: str | None = None, chunksize: int | None = None, dtype_backend: DtypeBackend | Literal['numpy'] = 'numpy') -> DataFrame | Iterator[DataFrame]:
        '''
        Read SQL database table into a DataFrame.

        Parameters
        ----------
        table_name : str
            Name of SQL table in database.
        index_col : string, optional, default: None
            Column to set as index.
        coerce_float : bool, default True
            Attempts to convert values of non-string, non-numeric objects
            (like decimal.Decimal) to floating point. This can result in
            loss of precision.
        parse_dates : list or dict, default: None
            - List of column names to parse as dates.
            - Dict of ``{column_name: format string}`` where format string is
              strftime compatible in case of parsing string times, or is one of
              (D, s, ns, ms, us) in case of parsing integer timestamps.
            - Dict of ``{column_name: arg}``, where the arg corresponds
              to the keyword arguments of :func:`pandas.to_datetime`.
              Especially useful with databases without native Datetime support,
              such as SQLite.
        columns : list, default: None
            List of column names to select from SQL table.
        schema : string, default None
            Name of SQL schema in database to query (if database flavor
            supports this).  If specified, this overwrites the default
            schema of the SQL database object.
        chunksize : int, default None
            If specified, return an iterator where `chunksize` is the number
            of rows to include in each chunk.
        dtype_backend : {{"numpy_nullable", "pyarrow"}}, defaults to NumPy dtypes
            Which dtype_backend to use, e.g. whether a DataFrame should have NumPy
            arrays, nullable dtypes are used for all dtypes that have a nullable
            implementation when "numpy_nullable" is set, pyarrow is used for all
            dtypes if "pyarrow" is set.

            The dtype_backends are still experimential.

            .. versionadded:: 2.0

        Returns
        -------
        DataFrame

        See Also
        --------
        pandas.read_sql_table
        SQLDatabase.read_query

        '''
    def read_query(self, sql: str, index_col: str | list[str] | None = None, coerce_float: bool = True, parse_dates: Incomplete | None = None, params: Incomplete | None = None, chunksize: int | None = None, dtype: DtypeArg | None = None, dtype_backend: DtypeBackend | Literal['numpy'] = 'numpy') -> DataFrame | Iterator[DataFrame]:
        """
        Read SQL query into a DataFrame.

        Parameters
        ----------
        sql : str
            SQL query to be executed.
        index_col : string, optional, default: None
            Column name to use as index for the returned DataFrame object.
        coerce_float : bool, default True
            Attempt to convert values of non-string, non-numeric objects (like
            decimal.Decimal) to floating point, useful for SQL result sets.
        params : list, tuple or dict, optional, default: None
            List of parameters to pass to execute method.  The syntax used
            to pass parameters is database driver dependent. Check your
            database driver documentation for which of the five syntax styles,
            described in PEP 249's paramstyle, is supported.
            Eg. for psycopg2, uses %(name)s so use params={'name' : 'value'}
        parse_dates : list or dict, default: None
            - List of column names to parse as dates.
            - Dict of ``{column_name: format string}`` where format string is
              strftime compatible in case of parsing string times, or is one of
              (D, s, ns, ms, us) in case of parsing integer timestamps.
            - Dict of ``{column_name: arg dict}``, where the arg dict
              corresponds to the keyword arguments of
              :func:`pandas.to_datetime` Especially useful with databases
              without native Datetime support, such as SQLite.
        chunksize : int, default None
            If specified, return an iterator where `chunksize` is the number
            of rows to include in each chunk.
        dtype : Type name or dict of columns
            Data type for data or columns. E.g. np.float64 or
            {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}

            .. versionadded:: 1.3.0

        Returns
        -------
        DataFrame

        See Also
        --------
        read_sql_table : Read SQL database table into a DataFrame.
        read_sql

        """
    read_sql = read_query
    def prep_table(self, frame, name, if_exists: Literal['fail', 'replace', 'append'] = 'fail', index: bool | str | list[str] | None = True, index_label: Incomplete | None = None, schema: Incomplete | None = None, dtype: DtypeArg | None = None) -> SQLTable:
        """
        Prepares table in the database for data insertion. Creates it if needed, etc.
        """
    def check_case_sensitive(self, name: str, schema: str | None) -> None:
        """
        Checks table name for issues with case-sensitivity.
        Method is called after data is inserted.
        """
    def to_sql(self, frame, name: str, if_exists: Literal['fail', 'replace', 'append'] = 'fail', index: bool = True, index_label: Incomplete | None = None, schema: str | None = None, chunksize: Incomplete | None = None, dtype: DtypeArg | None = None, method: Incomplete | None = None, engine: str = 'auto', **engine_kwargs) -> int | None:
        """
        Write records stored in a DataFrame to a SQL database.

        Parameters
        ----------
        frame : DataFrame
        name : string
            Name of SQL table.
        if_exists : {'fail', 'replace', 'append'}, default 'fail'
            - fail: If table exists, do nothing.
            - replace: If table exists, drop it, recreate it, and insert data.
            - append: If table exists, insert data. Create if does not exist.
        index : boolean, default True
            Write DataFrame index as a column.
        index_label : string or sequence, default None
            Column label for index column(s). If None is given (default) and
            `index` is True, then the index names are used.
            A sequence should be given if the DataFrame uses MultiIndex.
        schema : string, default None
            Name of SQL schema in database to write to (if database flavor
            supports this). If specified, this overwrites the default
            schema of the SQLDatabase object.
        chunksize : int, default None
            If not None, then rows will be written in batches of this size at a
            time.  If None, all rows will be written at once.
        dtype : single type or dict of column name to SQL type, default None
            Optional specifying the datatype for columns. The SQL type should
            be a SQLAlchemy type. If all columns are of the same type, one
            single value can be used.
        method : {None', 'multi', callable}, default None
            Controls the SQL insertion clause used:

            * None : Uses standard SQL ``INSERT`` clause (one per row).
            * 'multi': Pass multiple values in a single ``INSERT`` clause.
            * callable with signature ``(pd_table, conn, keys, data_iter)``.

            Details and a sample callable implementation can be found in the
            section :ref:`insert method <io.sql.method>`.
        engine : {'auto', 'sqlalchemy'}, default 'auto'
            SQL engine library to use. If 'auto', then the option
            ``io.sql.engine`` is used. The default ``io.sql.engine``
            behavior is 'sqlalchemy'

            .. versionadded:: 1.3.0

        **engine_kwargs
            Any additional kwargs are passed to the engine.
        """
    @property
    def tables(self): ...
    def has_table(self, name: str, schema: str | None = None) -> bool: ...
    def get_table(self, table_name: str, schema: str | None = None) -> Table: ...
    def drop_table(self, table_name: str, schema: str | None = None) -> None: ...

class SQLiteTable(SQLTable):
    """
    Patch the SQLTable for fallback support.
    Instead of a table variable just use the Create Table statement.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def sql_schema(self) -> str: ...
    def insert_statement(self, *, num_rows: int) -> str: ...

class SQLiteDatabase(PandasSQL):
    """
    Version of SQLDatabase to support SQLite connections (fallback without
    SQLAlchemy). This should only be used internally.

    Parameters
    ----------
    con : sqlite connection object

    """
    con: Incomplete
    def __init__(self, con) -> None: ...
    def run_transaction(self) -> Generator[Incomplete, None, None]: ...
    def execute(self, sql: str | Select | TextClause, params: Incomplete | None = None): ...
    def read_query(self, sql, index_col: Incomplete | None = None, coerce_float: bool = True, parse_dates: Incomplete | None = None, params: Incomplete | None = None, chunksize: int | None = None, dtype: DtypeArg | None = None, dtype_backend: DtypeBackend | Literal['numpy'] = 'numpy') -> DataFrame | Iterator[DataFrame]: ...
    def to_sql(self, frame, name, if_exists: str = 'fail', index: bool = True, index_label: Incomplete | None = None, schema: Incomplete | None = None, chunksize: Incomplete | None = None, dtype: DtypeArg | None = None, method: Incomplete | None = None, engine: str = 'auto', **engine_kwargs) -> int | None:
        """
        Write records stored in a DataFrame to a SQL database.

        Parameters
        ----------
        frame: DataFrame
        name: string
            Name of SQL table.
        if_exists: {'fail', 'replace', 'append'}, default 'fail'
            fail: If table exists, do nothing.
            replace: If table exists, drop it, recreate it, and insert data.
            append: If table exists, insert data. Create if it does not exist.
        index : bool, default True
            Write DataFrame index as a column
        index_label : string or sequence, default None
            Column label for index column(s). If None is given (default) and
            `index` is True, then the index names are used.
            A sequence should be given if the DataFrame uses MultiIndex.
        schema : string, default None
            Ignored parameter included for compatibility with SQLAlchemy
            version of ``to_sql``.
        chunksize : int, default None
            If not None, then rows will be written in batches of this
            size at a time. If None, all rows will be written at once.
        dtype : single type or dict of column name to SQL type, default None
            Optional specifying the datatype for columns. The SQL type should
            be a string. If all columns are of the same type, one single value
            can be used.
        method : {None, 'multi', callable}, default None
            Controls the SQL insertion clause used:

            * None : Uses standard SQL ``INSERT`` clause (one per row).
            * 'multi': Pass multiple values in a single ``INSERT`` clause.
            * callable with signature ``(pd_table, conn, keys, data_iter)``.

            Details and a sample callable implementation can be found in the
            section :ref:`insert method <io.sql.method>`.
        """
    def has_table(self, name: str, schema: str | None = None) -> bool: ...
    def get_table(self, table_name: str, schema: str | None = None) -> None: ...
    def drop_table(self, name: str, schema: str | None = None) -> None: ...

def get_schema(frame, name: str, keys: Incomplete | None = None, con: Incomplete | None = None, dtype: DtypeArg | None = None, schema: str | None = None) -> str:
    """
    Get the SQL db table schema for the given frame.

    Parameters
    ----------
    frame : DataFrame
    name : str
        name of SQL table
    keys : string or sequence, default: None
        columns to use a primary key
    con: an open SQL database connection object or a SQLAlchemy connectable
        Using SQLAlchemy makes it possible to use any DB supported by that
        library, default: None
        If a DBAPI2 object, only sqlite3 is supported.
    dtype : dict of column name to SQL type, default None
        Optional specifying the datatype for columns. The SQL type should
        be a SQLAlchemy type, or a string for sqlite3 fallback connection.
    schema: str, default: None
        Optional specifying the schema to be used in creating the table.

        .. versionadded:: 1.2.0
    """
