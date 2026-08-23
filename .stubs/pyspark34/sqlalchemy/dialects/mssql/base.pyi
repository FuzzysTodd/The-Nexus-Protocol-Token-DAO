from ... import Identity as Identity, Sequence as Sequence, exc as exc, sql as sql, text as text, util as util
from ...engine import default as default, reflection as reflection
from ...engine.reflection import ReflectionDefaults as ReflectionDefaults
from ...sql import coercions as coercions, compiler as compiler, elements as elements, expression as expression, func as func, quoted_name as quoted_name, roles as roles, sqltypes as sqltypes
from ...sql._typing import is_sql_compiler as is_sql_compiler
from ...sql.compiler import InsertmanyvaluesSentinelOpts as InsertmanyvaluesSentinelOpts
from ...sql.dml import DMLState as DMLState
from ...sql.selectable import TableClause as TableClause
from ...types import BIGINT as BIGINT, BINARY as BINARY, CHAR as CHAR, DATE as DATE, DATETIME as DATETIME, DECIMAL as DECIMAL, FLOAT as FLOAT, INTEGER as INTEGER, NCHAR as NCHAR, NUMERIC as NUMERIC, NVARCHAR as NVARCHAR, SMALLINT as SMALLINT, TEXT as TEXT, VARCHAR as VARCHAR
from ...util import update_wrapper as update_wrapper
from ...util.typing import Literal as Literal
from .json import JSON as JSON, JSONIndexType as JSONIndexType, JSONPathType as JSONPathType
from _typeshed import Incomplete
from typing import overload

MS_2017_VERSION: Incomplete
MS_2016_VERSION: Incomplete
MS_2014_VERSION: Incomplete
MS_2012_VERSION: Incomplete
MS_2008_VERSION: Incomplete
MS_2005_VERSION: Incomplete
MS_2000_VERSION: Incomplete
RESERVED_WORDS: Incomplete

class REAL(sqltypes.REAL):
    """the SQL Server REAL datatype."""
    def __init__(self, **kw) -> None: ...

class DOUBLE_PRECISION(sqltypes.DOUBLE_PRECISION):
    """the SQL Server DOUBLE PRECISION datatype.

    .. versionadded:: 2.0.11

    """
    def __init__(self, **kw) -> None: ...

class TINYINT(sqltypes.Integer):
    __visit_name__: str

class _MSDate(sqltypes.Date):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class TIME(sqltypes.TIME):
    precision: Incomplete
    def __init__(self, precision: Incomplete | None = None, **kwargs) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _BASETIMEIMPL(TIME):
    __visit_name__: str

class _DateTimeBase:
    def bind_processor(self, dialect): ...

class _MSDateTime(_DateTimeBase, sqltypes.DateTime): ...

class SMALLDATETIME(_DateTimeBase, sqltypes.DateTime):
    __visit_name__: str

class DATETIME2(_DateTimeBase, sqltypes.DateTime):
    __visit_name__: str
    precision: Incomplete
    def __init__(self, precision: Incomplete | None = None, **kw) -> None: ...

class DATETIMEOFFSET(_DateTimeBase, sqltypes.DateTime):
    __visit_name__: str
    precision: Incomplete
    def __init__(self, precision: Incomplete | None = None, **kw) -> None: ...

class _UnicodeLiteral:
    def literal_processor(self, dialect): ...

class _MSUnicode(_UnicodeLiteral, sqltypes.Unicode): ...
class _MSUnicodeText(_UnicodeLiteral, sqltypes.UnicodeText): ...

class TIMESTAMP(sqltypes._Binary):
    """Implement the SQL Server TIMESTAMP type.

    Note this is **completely different** than the SQL Standard
    TIMESTAMP type, which is not supported by SQL Server.  It
    is a read-only datatype that does not support INSERT of values.

    .. versionadded:: 1.2

    .. seealso::

        :class:`_mssql.ROWVERSION`

    """
    __visit_name__: str
    length: Incomplete
    convert_int: Incomplete
    def __init__(self, convert_int: bool = False) -> None:
        """Construct a TIMESTAMP or ROWVERSION type.

        :param convert_int: if True, binary integer values will
         be converted to integers on read.

        .. versionadded:: 1.2

        """
    def result_processor(self, dialect, coltype): ...

class ROWVERSION(TIMESTAMP):
    """Implement the SQL Server ROWVERSION type.

    The ROWVERSION datatype is a SQL Server synonym for the TIMESTAMP
    datatype, however current SQL Server documentation suggests using
    ROWVERSION for new datatypes going forward.

    The ROWVERSION datatype does **not** reflect (e.g. introspect) from the
    database as itself; the returned datatype will be
    :class:`_mssql.TIMESTAMP`.

    This is a read-only datatype that does not support INSERT of values.

    .. versionadded:: 1.2

    .. seealso::

        :class:`_mssql.TIMESTAMP`

    """
    __visit_name__: str

class NTEXT(sqltypes.UnicodeText):
    """MSSQL NTEXT type, for variable-length unicode text up to 2^30
    characters."""
    __visit_name__: str

class VARBINARY(sqltypes.VARBINARY, sqltypes.LargeBinary):
    '''The MSSQL VARBINARY type.

    This type adds additional features to the core :class:`_types.VARBINARY`
    type, including "deprecate_large_types" mode where
    either ``VARBINARY(max)`` or IMAGE is rendered, as well as the SQL
    Server ``FILESTREAM`` option.

    .. seealso::

        :ref:`mssql_large_type_deprecation`

    '''
    __visit_name__: str
    filestream: Incomplete
    def __init__(self, length: Incomplete | None = None, filestream: bool = False) -> None:
        """
        Construct a VARBINARY type.

        :param length: optional, a length for the column for use in
          DDL statements, for those binary types that accept a length,
          such as the MySQL BLOB type.

        :param filestream=False: if True, renders the ``FILESTREAM`` keyword
          in the table definition. In this case ``length`` must be ``None``
          or ``'max'``.

          .. versionadded:: 1.4.31

        """

class IMAGE(sqltypes.LargeBinary):
    __visit_name__: str

class XML(sqltypes.Text):
    '''MSSQL XML type.

    This is a placeholder type for reflection purposes that does not include
    any Python-side datatype support.   It also does not currently support
    additional arguments, such as "CONTENT", "DOCUMENT",
    "xml_schema_collection".

    '''
    __visit_name__: str

class BIT(sqltypes.Boolean):
    """MSSQL BIT type.

    Both pyodbc and pymssql return values from BIT columns as
    Python <class 'bool'> so just subclass Boolean.

    """
    __visit_name__: str

class MONEY(sqltypes.TypeEngine):
    __visit_name__: str

class SMALLMONEY(sqltypes.TypeEngine):
    __visit_name__: str

class MSUUid(sqltypes.Uuid):
    def bind_processor(self, dialect): ...
    def literal_processor(self, dialect): ...

class UNIQUEIDENTIFIER(sqltypes.Uuid[sqltypes._UUID_RETURN]):
    __visit_name__: str
    @overload
    def __init__(self, as_uuid: Literal[True] = ...) -> None: ...
    @overload
    def __init__(self, as_uuid: Literal[False] = ...) -> None: ...

class SQL_VARIANT(sqltypes.TypeEngine):
    __visit_name__: str

MSDateTime: Incomplete
MSDate: Incomplete
MSReal = REAL
MSTinyInteger = TINYINT
MSTime = TIME
MSSmallDateTime = SMALLDATETIME
MSDateTime2 = DATETIME2
MSDateTimeOffset = DATETIMEOFFSET
MSText = TEXT
MSNText = NTEXT
MSString = VARCHAR
MSNVarchar = NVARCHAR
MSChar = CHAR
MSNChar = NCHAR
MSBinary = BINARY
MSVarBinary = VARBINARY
MSImage = IMAGE
MSBit = BIT
MSMoney = MONEY
MSSmallMoney = SMALLMONEY
MSUniqueIdentifier = UNIQUEIDENTIFIER
MSVariant = SQL_VARIANT
ischema_names: Incomplete

class MSTypeCompiler(compiler.GenericTypeCompiler):
    def visit_double(self, type_, **kw): ...
    def visit_FLOAT(self, type_, **kw): ...
    def visit_TINYINT(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_ROWVERSION(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_DATETIMEOFFSET(self, type_, **kw): ...
    def visit_DATETIME2(self, type_, **kw): ...
    def visit_SMALLDATETIME(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_NTEXT(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_date(self, type_, **kw): ...
    def visit__BASETIMEIMPL(self, type_, **kw): ...
    def visit_time(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_IMAGE(self, type_, **kw): ...
    def visit_XML(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_BIT(self, type_, **kw): ...
    def visit_JSON(self, type_, **kw): ...
    def visit_MONEY(self, type_, **kw): ...
    def visit_SMALLMONEY(self, type_, **kw): ...
    def visit_uuid(self, type_, **kw): ...
    def visit_UNIQUEIDENTIFIER(self, type_, **kw): ...
    def visit_SQL_VARIANT(self, type_, **kw): ...

class MSExecutionContext(default.DefaultExecutionContext):
    dialect: MSDialect
    def pre_exec(self) -> None:
        """Activate IDENTITY_INSERT if needed."""
    cursor_fetch_strategy: Incomplete
    def post_exec(self) -> None:
        """Disable IDENTITY_INSERT if enabled."""
    def get_lastrowid(self): ...
    @property
    def rowcount(self): ...
    def handle_dbapi_exception(self, e) -> None: ...
    def fire_sequence(self, seq, type_): ...
    def get_insert_default(self, column): ...

class MSSQLCompiler(compiler.SQLCompiler):
    returning_precedes_values: bool
    extract_map: Incomplete
    tablealiases: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def visit_now_func(self, fn, **kw): ...
    def visit_current_date_func(self, fn, **kw): ...
    def visit_length_func(self, fn, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_aggregate_strings_func(self, fn, **kw): ...
    def visit_concat_op_expression_clauselist(self, clauselist, operator, **kw): ...
    def visit_concat_op_binary(self, binary, operator, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def get_select_precolumns(self, select, **kw):
        """MS-SQL puts TOP, it's version of LIMIT here"""
    def get_from_hint_text(self, table, text): ...
    def get_crud_hint_text(self, table, text): ...
    def limit_clause(self, cs, **kwargs): ...
    def visit_try_cast(self, element, **kw): ...
    def translate_select_structure(self, select_stmt, **kwargs):
        """Look for ``LIMIT`` and OFFSET in a select statement, and if
        so tries to wrap it in a subquery with ``row_number()`` criterion.
        MSSQL 2012 and above are excluded

        """
    def visit_table(self, table, mssql_aliased: bool = False, iscrud: bool = False, **kwargs): ...
    def visit_alias(self, alias, **kw): ...
    def visit_column(self, column, add_to_result_map: Incomplete | None = None, **kw): ...
    def visit_extract(self, extract, **kw): ...
    def visit_savepoint(self, savepoint_stmt, **kw): ...
    def visit_rollback_to_savepoint(self, savepoint_stmt, **kw): ...
    def visit_binary(self, binary, **kwargs):
        """Move bind parameters to the right-hand side of an operator, where
        possible.

        """
    def returning_clause(self, stmt, returning_cols, *, populate_result_map, **kw): ...
    def get_cte_preamble(self, recursive): ...
    def label_select_column(self, select, column, asfrom): ...
    def for_update_clause(self, select, **kw): ...
    def order_by_clause(self, select, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw):
        """Render the UPDATE..FROM clause specific to MSSQL.

        In MSSQL, if the UPDATE statement involves an alias of the table to
        be updated, then the table itself must be added to the FROM list as
        well. Otherwise, it is optional. Here, we add it regardless.

        """
    def delete_table_clause(self, delete_stmt, from_table, extra_froms, **kw):
        """If we have extra froms make sure we render any alias as hint."""
    def delete_extra_from_clause(self, delete_stmt, from_table, extra_froms, from_hints, **kw):
        """Render the DELETE .. FROM clause specific to MSSQL.

        Yes, it has the FROM keyword twice.

        """
    def visit_empty_set_expr(self, type_, **kw): ...
    def visit_is_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_is_not_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_sequence(self, seq, **kw): ...

class MSSQLStrictCompiler(MSSQLCompiler):
    """A subclass of MSSQLCompiler which disables the usage of bind
    parameters where not allowed natively by MS-SQL.

    A dialect may use this compiler on a platform where native
    binds are used.

    """
    ansi_bind_rules: bool
    def visit_in_op_binary(self, binary, operator, **kw): ...
    def visit_not_in_op_binary(self, binary, operator, **kw): ...
    def render_literal_value(self, value, type_):
        """
        For date and datetime values, convert to a string
        format acceptable to MSSQL. That seems to be the
        so-called ODBC canonical date format which looks
        like this:

            yyyy-mm-dd hh:mi:ss.mmm(24h)

        For other data types, call the base class implementation.
        """

class MSDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kwargs): ...
    def visit_create_index(self, create, include_schema: bool = False, **kw): ...
    def visit_drop_index(self, drop, **kw): ...
    def visit_primary_key_constraint(self, constraint, **kw): ...
    def visit_unique_constraint(self, constraint, **kw): ...
    def visit_computed_column(self, generated, **kw): ...
    def visit_set_table_comment(self, create, **kw): ...
    def visit_drop_table_comment(self, drop, **kw): ...
    def visit_set_column_comment(self, create, **kw): ...
    def visit_drop_column_comment(self, drop, **kw): ...
    def visit_create_sequence(self, create, **kw): ...
    def visit_identity_column(self, identity, **kw): ...

class MSIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = RESERVED_WORDS
    def __init__(self, dialect) -> None: ...
    def quote_schema(self, schema, force: Incomplete | None = None):
        """Prepare a quoted table and schema name."""

class MSDialect(default.DefaultDialect):
    name: str
    supports_statement_cache: bool
    supports_default_values: bool
    supports_empty_insert: bool
    favor_returning_over_lastrowid: bool
    returns_native_bytes: bool
    supports_comments: bool
    supports_default_metavalue: bool
    execution_ctx_cls = MSExecutionContext
    use_scope_identity: bool
    max_identifier_length: int
    schema_name: str
    insert_returning: bool
    update_returning: bool
    delete_returning: bool
    update_returning_multifrom: bool
    delete_returning_multifrom: bool
    colspecs: Incomplete
    engine_config_types: Incomplete
    ischema_names = ischema_names
    supports_sequences: bool
    sequences_optional: bool
    default_sequence_base: int
    supports_native_boolean: bool
    non_native_boolean_check_constraint: bool
    supports_unicode_binds: bool
    postfetch_lastrowid: bool
    supports_multivalues_insert: bool
    use_insertmanyvalues: bool
    use_insertmanyvalues_wo_returning: bool
    insertmanyvalues_implicit_sentinel: Incomplete
    insertmanyvalues_max_parameters: int
    legacy_schema_aliasing: bool
    server_version_info: Incomplete
    statement_compiler = MSSQLCompiler
    ddl_compiler = MSDDLCompiler
    type_compiler_cls = MSTypeCompiler
    preparer = MSIdentifierPreparer
    construct_arguments: Incomplete
    query_timeout: Incomplete
    deprecate_large_types: Incomplete
    ignore_no_transaction_on_rollback: Incomplete
    def __init__(self, query_timeout: Incomplete | None = None, use_scope_identity: bool = True, schema_name: str = 'dbo', deprecate_large_types: Incomplete | None = None, supports_comments: Incomplete | None = None, json_serializer: Incomplete | None = None, json_deserializer: Incomplete | None = None, legacy_schema_aliasing: Incomplete | None = None, ignore_no_transaction_on_rollback: bool = False, **opts) -> None: ...
    def do_savepoint(self, connection, name) -> None: ...
    def do_release_savepoint(self, connection, name) -> None: ...
    def do_rollback(self, dbapi_connection) -> None: ...
    def get_isolation_level_values(self, dbapi_connection): ...
    def set_isolation_level(self, dbapi_connection, level) -> None: ...
    def get_isolation_level(self, dbapi_connection): ...
    def initialize(self, connection) -> None: ...
    def has_table(self, connection, tablename, dbname, owner, schema, **kw): ...
    def has_sequence(self, connection, sequencename, dbname, owner, schema, **kw): ...
    def get_sequence_names(self, connection, dbname, owner, schema, **kw): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, dbname, owner, schema, **kw): ...
    def get_view_names(self, connection, dbname, owner, schema, **kw): ...
    def get_indexes(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_view_definition(self, connection, viewname, dbname, owner, schema, **kw): ...
    def get_table_comment(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_columns(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_pk_constraint(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_foreign_keys(self, connection, tablename, dbname, owner, schema, **kw): ...
