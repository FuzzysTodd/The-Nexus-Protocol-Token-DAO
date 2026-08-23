from ... import exc as exc, sql as sql, text as text, types as sqltypes, util as util
from ...engine import default as default, processors as processors, reflection as reflection
from ...engine.reflection import ReflectionDefaults as ReflectionDefaults
from ...sql import ColumnElement as ColumnElement, coercions as coercions, compiler as compiler, elements as elements, roles as roles, schema as schema
from ...types import BLOB as BLOB, BOOLEAN as BOOLEAN, CHAR as CHAR, DECIMAL as DECIMAL, FLOAT as FLOAT, INTEGER as INTEGER, NUMERIC as NUMERIC, REAL as REAL, SMALLINT as SMALLINT, TEXT as TEXT, TIMESTAMP as TIMESTAMP, VARCHAR as VARCHAR
from .json import JSON as JSON, JSONIndexType as JSONIndexType, JSONPathType as JSONPathType
from _typeshed import Incomplete

class _SQliteJson(JSON):
    def result_processor(self, dialect, coltype): ...

class _DateTimeMixin:
    def __init__(self, storage_format: Incomplete | None = None, regexp: Incomplete | None = None, **kw) -> None: ...
    @property
    def format_is_text_affinity(self):
        """return True if the storage format will automatically imply
        a TEXT affinity.

        If the storage format contains no non-numeric characters,
        it will imply a NUMERIC storage format on SQLite; in this case,
        the type will generate its DDL as DATE_CHAR, DATETIME_CHAR,
        TIME_CHAR.

        """
    def adapt(self, cls, **kw): ...
    def literal_processor(self, dialect): ...

class DATETIME(_DateTimeMixin, sqltypes.DateTime):
    '''Represent a Python datetime object in SQLite using a string.

    The default string storage format is::

        "%(year)04d-%(month)02d-%(day)02d %(hour)02d:%(minute)02d:%(second)02d.%(microsecond)06d"

    e.g.::

        2021-03-15 12:05:57.105542

    The incoming storage format is by default parsed using the
    Python ``datetime.fromisoformat()`` function.

    .. versionchanged:: 2.0  ``datetime.fromisoformat()`` is used for default
       datetime string parsing.

    The storage format can be customized to some degree using the
    ``storage_format`` and ``regexp`` parameters, such as::

        import re
        from sqlalchemy.dialects.sqlite import DATETIME

        dt = DATETIME(storage_format="%(year)04d/%(month)02d/%(day)02d "
                                     "%(hour)02d:%(minute)02d:%(second)02d",
                      regexp=r"(\\d+)/(\\d+)/(\\d+) (\\d+)-(\\d+)-(\\d+)"
        )

    :param storage_format: format string which will be applied to the dict
     with keys year, month, day, hour, minute, second, and microsecond.

    :param regexp: regular expression which will be applied to incoming result
     rows, replacing the use of ``datetime.fromisoformat()`` to parse incoming
     strings. If the regexp contains named groups, the resulting match dict is
     applied to the Python datetime() constructor as keyword arguments.
     Otherwise, if positional groups are used, the datetime() constructor
     is called with positional arguments via
     ``*map(int, match_obj.groups(0))``.

    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class DATE(_DateTimeMixin, sqltypes.Date):
    '''Represent a Python date object in SQLite using a string.

    The default string storage format is::

        "%(year)04d-%(month)02d-%(day)02d"

    e.g.::

        2011-03-15

    The incoming storage format is by default parsed using the
    Python ``date.fromisoformat()`` function.

    .. versionchanged:: 2.0  ``date.fromisoformat()`` is used for default
       date string parsing.


    The storage format can be customized to some degree using the
    ``storage_format`` and ``regexp`` parameters, such as::

        import re
        from sqlalchemy.dialects.sqlite import DATE

        d = DATE(
                storage_format="%(month)02d/%(day)02d/%(year)04d",
                regexp=re.compile("(?P<month>\\d+)/(?P<day>\\d+)/(?P<year>\\d+)")
            )

    :param storage_format: format string which will be applied to the
     dict with keys year, month, and day.

    :param regexp: regular expression which will be applied to
     incoming result rows, replacing the use of ``date.fromisoformat()`` to
     parse incoming strings. If the regexp contains named groups, the resulting
     match dict is applied to the Python date() constructor as keyword
     arguments. Otherwise, if positional groups are used, the date()
     constructor is called with positional arguments via
     ``*map(int, match_obj.groups(0))``.

    '''
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class TIME(_DateTimeMixin, sqltypes.Time):
    '''Represent a Python time object in SQLite using a string.

    The default string storage format is::

        "%(hour)02d:%(minute)02d:%(second)02d.%(microsecond)06d"

    e.g.::

        12:05:57.10558

    The incoming storage format is by default parsed using the
    Python ``time.fromisoformat()`` function.

    .. versionchanged:: 2.0  ``time.fromisoformat()`` is used for default
       time string parsing.

    The storage format can be customized to some degree using the
    ``storage_format`` and ``regexp`` parameters, such as::

        import re
        from sqlalchemy.dialects.sqlite import TIME

        t = TIME(storage_format="%(hour)02d-%(minute)02d-"
                                "%(second)02d-%(microsecond)06d",
                 regexp=re.compile("(\\d+)-(\\d+)-(\\d+)-(?:-(\\d+))?")
        )

    :param storage_format: format string which will be applied to the dict
     with keys hour, minute, second, and microsecond.

    :param regexp: regular expression which will be applied to incoming result
     rows, replacing the use of ``datetime.fromisoformat()`` to parse incoming
     strings. If the regexp contains named groups, the resulting match dict is
     applied to the Python time() constructor as keyword arguments. Otherwise,
     if positional groups are used, the time() constructor is called with
     positional arguments via ``*map(int, match_obj.groups(0))``.

    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

colspecs: Incomplete
ischema_names: Incomplete

class SQLiteCompiler(compiler.SQLCompiler):
    extract_map: Incomplete
    def visit_truediv_binary(self, binary, operator, **kw): ...
    def visit_now_func(self, fn, **kw): ...
    def visit_localtimestamp_func(self, func, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_aggregate_strings_func(self, fn, **kw): ...
    def visit_cast(self, cast, **kwargs): ...
    def visit_extract(self, extract, **kw): ...
    def returning_clause(self, stmt, returning_cols, *, populate_result_map, **kw): ...
    def limit_clause(self, select, **kw): ...
    def for_update_clause(self, select, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def visit_is_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_is_not_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_empty_set_op_expr(self, type_, expand_op, **kw): ...
    def visit_empty_set_expr(self, element_types, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_on_conflict_do_nothing(self, on_conflict, **kw): ...
    def visit_on_conflict_do_update(self, on_conflict, **kw): ...

class SQLiteDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kwargs): ...
    def visit_primary_key_constraint(self, constraint, **kw): ...
    def visit_unique_constraint(self, constraint, **kw): ...
    def visit_check_constraint(self, constraint, **kw): ...
    def visit_column_check_constraint(self, constraint, **kw): ...
    def visit_foreign_key_constraint(self, constraint, **kw): ...
    def define_constraint_remote_table(self, constraint, table, preparer):
        """Format the remote table clause of a CREATE CONSTRAINT clause."""
    def visit_create_index(self, create, include_schema: bool = False, include_table_schema: bool = True, **kw): ...
    def post_create_table(self, table): ...

class SQLiteTypeCompiler(compiler.GenericTypeCompiler):
    def visit_large_binary(self, type_, **kw): ...
    def visit_DATETIME(self, type_, **kw): ...
    def visit_DATE(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_JSON(self, type_, **kw): ...

class SQLiteIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Incomplete

class SQLiteExecutionContext(default.DefaultExecutionContext): ...

class SQLiteDialect(default.DefaultDialect):
    name: str
    supports_alter: bool
    supports_default_values: bool
    supports_default_metavalue: bool
    supports_sane_rowcount_returning: bool
    supports_empty_insert: bool
    supports_cast: bool
    supports_multivalues_insert: bool
    use_insertmanyvalues: bool
    tuple_in_values: bool
    supports_statement_cache: bool
    insert_null_pk_still_autoincrements: bool
    insert_returning: bool
    update_returning: bool
    update_returning_multifrom: bool
    delete_returning: bool
    default_metavalue_token: str
    default_paramstyle: str
    execution_ctx_cls = SQLiteExecutionContext
    statement_compiler = SQLiteCompiler
    ddl_compiler = SQLiteDDLCompiler
    type_compiler_cls = SQLiteTypeCompiler
    preparer = SQLiteIdentifierPreparer
    ischema_names = ischema_names
    colspecs = colspecs
    construct_arguments: Incomplete
    native_datetime: Incomplete
    insertmanyvalues_max_parameters: int
    def __init__(self, native_datetime: bool = False, json_serializer: Incomplete | None = None, json_deserializer: Incomplete | None = None, _json_serializer: Incomplete | None = None, _json_deserializer: Incomplete | None = None, **kwargs) -> None: ...
    def get_isolation_level_values(self, dbapi_connection): ...
    def set_isolation_level(self, dbapi_connection, level) -> None: ...
    def get_isolation_level(self, dbapi_connection): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema: Incomplete | None = None, sqlite_include_internal: bool = False, **kw): ...
    def get_temp_table_names(self, connection, sqlite_include_internal: bool = False, **kw): ...
    def get_temp_view_names(self, connection, sqlite_include_internal: bool = False, **kw): ...
    def has_table(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_view_names(self, connection, schema: Incomplete | None = None, sqlite_include_internal: bool = False, **kw): ...
    def get_view_definition(self, connection, view_name, schema: Incomplete | None = None, **kw): ...
    def get_columns(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_unique_constraints(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_check_constraints(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_indexes(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
