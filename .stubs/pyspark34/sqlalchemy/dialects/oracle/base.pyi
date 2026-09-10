from . import dictionary as dictionary
from ... import Computed as Computed, exc as exc, sql as sql, util as util
from ...engine import ObjectKind as ObjectKind, ObjectScope as ObjectScope, default as default, reflection as reflection
from ...engine.reflection import ReflectionDefaults as ReflectionDefaults
from ...sql import and_ as and_, bindparam as bindparam, compiler as compiler, expression as expression, func as func, null as null, or_ as or_, select as select, sqltypes as sqltypes, visitors as visitors
from ...sql.visitors import InternalTraversal as InternalTraversal
from ...types import BLOB as BLOB, CHAR as CHAR, CLOB as CLOB, DOUBLE_PRECISION as DOUBLE_PRECISION, INTEGER as INTEGER, NCHAR as NCHAR, NVARCHAR as NVARCHAR, REAL as REAL, VARCHAR as VARCHAR
from .types import BFILE as BFILE, BINARY_DOUBLE as BINARY_DOUBLE, BINARY_FLOAT as BINARY_FLOAT, DATE as DATE, FLOAT as FLOAT, INTERVAL as INTERVAL, LONG as LONG, NCLOB as NCLOB, NUMBER as NUMBER, NVARCHAR2 as NVARCHAR2, OracleRaw as OracleRaw, RAW as RAW, ROWID as ROWID, TIMESTAMP as TIMESTAMP, VARCHAR2 as VARCHAR2
from _typeshed import Incomplete

RESERVED_WORDS: Incomplete
NO_ARG_FNS: Incomplete
colspecs: Incomplete
ischema_names: Incomplete

class OracleTypeCompiler(compiler.GenericTypeCompiler):
    def visit_datetime(self, type_, **kw): ...
    def visit_float(self, type_, **kw): ...
    def visit_double(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_INTERVAL(self, type_, **kw): ...
    def visit_LONG(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_DOUBLE_PRECISION(self, type_, **kw): ...
    def visit_BINARY_DOUBLE(self, type_, **kw): ...
    def visit_BINARY_FLOAT(self, type_, **kw): ...
    def visit_FLOAT(self, type_, **kw): ...
    def visit_NUMBER(self, type_, **kw): ...
    def visit_string(self, type_, **kw): ...
    def visit_VARCHAR2(self, type_, **kw): ...
    def visit_NVARCHAR2(self, type_, **kw): ...
    visit_NVARCHAR = visit_NVARCHAR2
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_big_integer(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_RAW(self, type_, **kw): ...
    def visit_ROWID(self, type_, **kw): ...

class OracleCompiler(compiler.SQLCompiler):
    """Oracle compiler modifies the lexical structure of Select
    statements to work under non-ANSI configured Oracle databases, if
    the use_ansi flag is False.
    """
    compound_keywords: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_now_func(self, fn, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def get_cte_preamble(self, recursive): ...
    def get_select_hint_text(self, byfroms): ...
    def function_argspec(self, fn, **kw): ...
    def visit_function(self, func, **kw): ...
    def visit_table_valued_column(self, element, **kw): ...
    def default_from(self):
        '''Called when a ``SELECT`` statement has no froms,
        and no ``FROM`` clause is to be appended.

        The Oracle compiler tacks a "FROM DUAL" to the statement.
        '''
    def visit_join(self, join, from_linter: Incomplete | None = None, **kwargs): ...
    def visit_outer_join_column(self, vc, **kw): ...
    def visit_sequence(self, seq, **kw): ...
    def get_render_as_alias_suffix(self, alias_name_text):
        """Oracle doesn't like ``FROM table AS alias``"""
    def returning_clause(self, stmt, returning_cols, *, populate_result_map, **kw): ...
    def translate_select_structure(self, select_stmt, **kwargs): ...
    def limit_clause(self, select, **kw): ...
    def visit_empty_set_expr(self, type_, **kw): ...
    def for_update_clause(self, select, **kw): ...
    def visit_is_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_is_not_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw): ...
    def visit_aggregate_strings_func(self, fn, **kw): ...

class OracleDDLCompiler(compiler.DDLCompiler):
    def define_constraint_cascades(self, constraint): ...
    def visit_drop_table_comment(self, drop, **kw): ...
    def visit_create_index(self, create, **kw): ...
    def post_create_table(self, table): ...
    def get_identity_options(self, identity_options): ...
    def visit_computed_column(self, generated, **kw): ...
    def visit_identity_column(self, identity, **kw): ...

class OracleIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Incomplete
    illegal_initial_characters: Incomplete
    def format_savepoint(self, savepoint): ...

class OracleExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_): ...
    statement: Incomplete
    def pre_exec(self) -> None: ...

class OracleDialect(default.DefaultDialect):
    name: str
    supports_statement_cache: bool
    supports_alter: bool
    max_identifier_length: int
    insert_returning: bool
    update_returning: bool
    delete_returning: bool
    div_is_floordiv: bool
    supports_simple_order_by_label: bool
    cte_follows_insert: bool
    returns_native_bytes: bool
    supports_sequences: bool
    sequences_optional: bool
    postfetch_lastrowid: bool
    default_paramstyle: str
    colspecs = colspecs
    ischema_names = ischema_names
    requires_name_normalize: bool
    supports_comments: bool
    supports_default_values: bool
    supports_default_metavalue: bool
    supports_empty_insert: bool
    supports_identity_columns: bool
    statement_compiler = OracleCompiler
    ddl_compiler = OracleDDLCompiler
    type_compiler_cls = OracleTypeCompiler
    preparer = OracleIdentifierPreparer
    execution_ctx_cls = OracleExecutionContext
    reflection_options: Incomplete
    construct_arguments: Incomplete
    use_ansi: Incomplete
    optimize_limits: Incomplete
    exclude_tablespaces: Incomplete
    enable_offset_fetch: Incomplete
    def __init__(self, use_ansi: bool = True, optimize_limits: bool = False, use_binds_for_limits: Incomplete | None = None, use_nchar_for_unicode: bool = False, exclude_tablespaces=('SYSTEM', 'SYSAUX'), enable_offset_fetch: bool = True, **kwargs) -> None: ...
    def initialize(self, connection) -> None: ...
    def do_release_savepoint(self, connection, name) -> None: ...
    def get_isolation_level_values(self, dbapi_connection): ...
    def get_default_isolation_level(self, dbapi_conn): ...
    def has_table(self, connection, table_name, schema: Incomplete | None = None, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def has_sequence(self, connection, sequence_name, schema: Incomplete | None = None, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def denormalize_schema_name(self, name): ...
    def get_schema_names(self, connection, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def get_table_names(self, connection, schema: Incomplete | None = None, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def get_temp_table_names(self, connection, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def get_materialized_view_names(self, connection, schema: Incomplete | None = None, dblink: Incomplete | None = None, _normalize: bool = True, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def get_view_names(self, connection, schema: Incomplete | None = None, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def get_sequence_names(self, connection, schema: Incomplete | None = None, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link."""
    def get_table_options(self, connection, table_name, schema: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_table_options(self, connection, *, schema, filter_names, scope, kind, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_columns(self, connection, table_name, schema: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_columns(self, connection, *, schema, filter_names, scope, kind, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_table_comment(self, connection, table_name, schema: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_table_comment(self, connection, *, schema, filter_names, scope, kind, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_indexes(self, connection, table_name, schema: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_indexes(self, connection, *, schema, filter_names, scope, kind, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_pk_constraint(self, connection, table_name, schema: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_pk_constraint(self, connection, *, scope, schema, filter_names, kind, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_foreign_keys(self, connection, table_name, schema: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_foreign_keys(self, connection, *, scope, schema, filter_names, kind, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_unique_constraints(self, connection, table_name, schema: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_unique_constraints(self, connection, *, scope, schema, filter_names, kind, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_view_definition(self, connection, view_name, schema: Incomplete | None = None, dblink: Incomplete | None = None, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_check_constraints(self, connection, table_name, schema: Incomplete | None = None, include_all: bool = False, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """
    def get_multi_check_constraints(self, connection, *, schema, filter_names, dblink: Incomplete | None = None, scope, kind, include_all: bool = False, **kw):
        """Supported kw arguments are: ``dblink`` to reflect via a db link;
        ``oracle_resolve_synonyms`` to resolve names to synonyms
        """

class _OuterJoinColumn(sql.ClauseElement):
    __visit_name__: str
    column: Incomplete
    def __init__(self, column) -> None: ...
