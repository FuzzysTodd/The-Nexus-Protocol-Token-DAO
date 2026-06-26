from . import characteristics as characteristics, interfaces as interfaces
from .. import event as event, exc as exc, pool as pool, util as util
from ..pool import Pool as Pool, PoolProxiedConnection as PoolProxiedConnection
from ..sql import Executable as Executable, compiler as compiler, dml as dml, expression as expression, type_api as type_api
from ..sql._typing import is_tuple_type as is_tuple_type
from ..sql.base import _NoArg
from ..sql.compiler import Compiled as Compiled, DDLCompiler as DDLCompiler, InsertmanyvaluesSentinelOpts as InsertmanyvaluesSentinelOpts, Linting as Linting, ResultColumnsEntry as ResultColumnsEntry, SQLCompiler as SQLCompiler
from ..sql.dml import DMLState as DMLState, UpdateBase as UpdateBase
from ..sql.elements import BindParameter as BindParameter, quoted_name as quoted_name
from ..sql.schema import Column as Column
from ..sql.type_api import TypeEngine as TypeEngine
from ..util.typing import Final as Final, Literal as Literal
from .base import Connection as Connection, Engine as Engine
from .cursor import ResultFetchStrategy as ResultFetchStrategy
from .interfaces import CacheStats as CacheStats, DBAPIConnection as DBAPIConnection, DBAPICursor as DBAPICursor, Dialect as Dialect, ExecuteStyle as ExecuteStyle, ExecutionContext as ExecutionContext, IsolationLevel as IsolationLevel, _CoreSingleExecuteParams, _DBAPIMultiExecuteParams, _ExecuteOptions, _MutableCoreSingleExecuteParams, _ParamStyle
from .reflection import ObjectKind as ObjectKind, ObjectScope as ObjectScope
from .row import Row as Row
from .url import URL as URL
from _typeshed import Incomplete
from types import ModuleType
from typing import Any, List, Mapping, MutableMapping, Sequence, Set, Tuple, Type

SERVER_SIDE_CURSOR_RE: Incomplete
CACHE_HIT: Incomplete
CACHE_MISS: Incomplete
CACHING_DISABLED: Incomplete
NO_CACHE_KEY: Incomplete
NO_DIALECT_SUPPORT: Incomplete

class DefaultDialect(Dialect):
    """Default implementation of Dialect"""
    statement_compiler = compiler.SQLCompiler
    ddl_compiler = compiler.DDLCompiler
    type_compiler_cls = compiler.GenericTypeCompiler
    preparer = compiler.IdentifierPreparer
    supports_alter: bool
    supports_comments: bool
    supports_constraint_comments: bool
    inline_comments: bool
    supports_statement_cache: bool
    div_is_floordiv: bool
    bind_typing: Incomplete
    include_set_input_sizes: Set[Any] | None
    exclude_set_input_sizes: Set[Any] | None
    default_sequence_base: int
    execute_sequence_format = tuple
    supports_schemas: bool
    supports_views: bool
    supports_sequences: bool
    sequences_optional: bool
    preexecute_autoincrement_sequences: bool
    supports_identity_columns: bool
    postfetch_lastrowid: bool
    favor_returning_over_lastrowid: bool
    insert_null_pk_still_autoincrements: bool
    update_returning: bool
    delete_returning: bool
    update_returning_multifrom: bool
    delete_returning_multifrom: bool
    insert_returning: bool
    cte_follows_insert: bool
    supports_native_enum: bool
    supports_native_boolean: bool
    supports_native_uuid: bool
    returns_native_bytes: bool
    non_native_boolean_check_constraint: bool
    supports_simple_order_by_label: bool
    tuple_in_values: bool
    connection_characteristics: Incomplete
    engine_config_types: Mapping[str, Any]
    supports_native_decimal: bool
    name: str
    max_identifier_length: int
    isolation_level: str | None
    max_index_name_length: int | None
    max_constraint_name_length: int | None
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    colspecs: MutableMapping[Type[TypeEngine[Any]], Type[TypeEngine[Any]]]
    default_paramstyle: str
    supports_default_values: bool
    supports_default_metavalue: bool
    default_metavalue_token: str
    supports_empty_insert: bool
    supports_multivalues_insert: bool
    use_insertmanyvalues: bool
    use_insertmanyvalues_wo_returning: bool
    insertmanyvalues_implicit_sentinel: InsertmanyvaluesSentinelOpts
    insertmanyvalues_page_size: int
    insertmanyvalues_max_parameters: int
    supports_is_distinct_from: bool
    supports_server_side_cursors: bool
    server_side_cursors: bool
    supports_for_update_of: bool
    server_version_info: Incomplete
    default_schema_name: str | None
    requires_name_normalize: bool
    is_async: bool
    has_terminate: bool
    positional: bool
    dbapi: Incomplete
    paramstyle: Incomplete
    identifier_preparer: Incomplete
    type_compiler_instance: Incomplete
    label_length: Incomplete
    compiler_linting: Incomplete
    def __init__(self, paramstyle: _ParamStyle | None = None, isolation_level: IsolationLevel | None = None, dbapi: ModuleType | None = None, implicit_returning: Literal[True] = True, supports_native_boolean: bool | None = None, max_identifier_length: int | None = None, label_length: int | None = None, insertmanyvalues_page_size: _NoArg | int = ..., use_insertmanyvalues: bool | None = None, compiler_linting: Linting = ..., server_side_cursors: bool = False, **kwargs: Any) -> None: ...
    @property
    def full_returning(self): ...
    def insert_executemany_returning(self):
        '''Default implementation for insert_executemany_returning, if not
        otherwise overridden by the specific dialect.

        The default dialect determines "insert_executemany_returning" is
        available if the dialect in use has opted into using the
        "use_insertmanyvalues" feature. If they haven\'t opted into that, then
        this attribute is False, unless the dialect in question overrides this
        and provides some other implementation (such as the Oracle dialect).

        '''
    def insert_executemany_returning_sort_by_parameter_order(self):
        '''Default implementation for
        insert_executemany_returning_deterministic_order, if not otherwise
        overridden by the specific dialect.

        The default dialect determines "insert_executemany_returning" can have
        deterministic order only if the dialect in use has opted into using the
        "use_insertmanyvalues" feature, which implements deterministic ordering
        using client side sentinel columns only by default.  The
        "insertmanyvalues" feature also features alternate forms that can
        use server-generated PK values as "sentinels", but those are only
        used if the :attr:`.Dialect.insertmanyvalues_implicit_sentinel`
        bitflag enables those alternate SQL forms, which are disabled
        by default.

        If the dialect in use hasn\'t opted into that, then this attribute is
        False, unless the dialect in question overrides this and provides some
        other implementation (such as the Oracle dialect).

        '''
    update_executemany_returning: bool
    delete_executemany_returning: bool
    def loaded_dbapi(self) -> ModuleType: ...
    @property
    def dialect_description(self): ...
    @property
    def supports_sane_rowcount_returning(self):
        """True if this dialect supports sane rowcount even if RETURNING is
        in use.

        For dialects that don't support RETURNING, this is synonymous with
        ``supports_sane_rowcount``.

        """
    @classmethod
    def get_pool_class(cls, url: URL) -> Type[Pool]: ...
    def get_dialect_pool_class(self, url: URL) -> Type[Pool]: ...
    @classmethod
    def load_provisioning(cls) -> None: ...
    default_isolation_level: Incomplete
    def initialize(self, connection) -> None: ...
    def on_connect(self) -> None: ...
    def get_default_isolation_level(self, dbapi_conn):
        '''Given a DBAPI connection, return its isolation level, or
        a default isolation level if one cannot be retrieved.

        May be overridden by subclasses in order to provide a
        "fallback" isolation level for databases that cannot reliably
        retrieve the actual isolation level.

        By default, calls the :meth:`_engine.Interfaces.get_isolation_level`
        method, propagating any exceptions raised.

        .. versionadded:: 1.3.22

        '''
    def type_descriptor(self, typeobj):
        """Provide a database-specific :class:`.TypeEngine` object, given
        the generic object which comes from the types module.

        This method looks for a dictionary called
        ``colspecs`` as a class or instance-level variable,
        and passes on to :func:`_types.adapt_type`.

        """
    def has_index(self, connection, table_name, index_name, schema: Incomplete | None = None, **kw): ...
    def has_schema(self, connection: Connection, schema_name: str, **kw: Any) -> bool: ...
    def validate_identifier(self, ident) -> None: ...
    def connect(self, *cargs, **cparams): ...
    def create_connect_args(self, url): ...
    def set_engine_execution_options(self, engine: Engine, opts: Mapping[str, Any]) -> None: ...
    def set_connection_execution_options(self, connection: Connection, opts: Mapping[str, Any]) -> None: ...
    def do_begin(self, dbapi_connection) -> None: ...
    def do_rollback(self, dbapi_connection) -> None: ...
    def do_commit(self, dbapi_connection) -> None: ...
    def do_terminate(self, dbapi_connection) -> None: ...
    def do_close(self, dbapi_connection) -> None: ...
    def do_ping(self, dbapi_connection: DBAPIConnection) -> bool: ...
    def create_xid(self):
        """Create a random two-phase transaction ID.

        This id will be passed to do_begin_twophase(), do_rollback_twophase(),
        do_commit_twophase().  Its format is unspecified.
        """
    def do_savepoint(self, connection, name) -> None: ...
    def do_rollback_to_savepoint(self, connection, name) -> None: ...
    def do_release_savepoint(self, connection, name) -> None: ...
    def do_executemany(self, cursor, statement, parameters, context: Incomplete | None = None) -> None: ...
    def do_execute(self, cursor, statement, parameters, context: Incomplete | None = None) -> None: ...
    def do_execute_no_params(self, cursor, statement, context: Incomplete | None = None) -> None: ...
    def is_disconnect(self, e, connection, cursor): ...
    def reset_isolation_level(self, dbapi_conn) -> None: ...
    def normalize_name(self, name): ...
    def denormalize_name(self, name): ...
    def get_driver_connection(self, connection): ...
    def get_multi_table_options(self, connection, **kw): ...
    def get_multi_columns(self, connection, **kw): ...
    def get_multi_pk_constraint(self, connection, **kw): ...
    def get_multi_foreign_keys(self, connection, **kw): ...
    def get_multi_indexes(self, connection, **kw): ...
    def get_multi_unique_constraints(self, connection, **kw): ...
    def get_multi_check_constraints(self, connection, **kw): ...
    def get_multi_table_comment(self, connection, **kw): ...

class StrCompileDialect(DefaultDialect):
    statement_compiler = compiler.StrSQLCompiler
    ddl_compiler = compiler.DDLCompiler
    type_compiler_cls = compiler.StrSQLTypeCompiler
    preparer = compiler.IdentifierPreparer
    insert_returning: bool
    update_returning: bool
    delete_returning: bool
    supports_statement_cache: bool
    supports_identity_columns: bool
    supports_sequences: bool
    sequences_optional: bool
    preexecute_autoincrement_sequences: bool
    supports_native_boolean: bool
    supports_multivalues_insert: bool
    supports_simple_order_by_label: bool

class DefaultExecutionContext(ExecutionContext):
    isinsert: bool
    isupdate: bool
    isdelete: bool
    is_crud: bool
    is_text: bool
    isddl: bool
    execute_style: ExecuteStyle
    compiled: Compiled | None
    result_column_struct: Tuple[List[ResultColumnsEntry], bool, bool, bool, bool] | None
    returned_default_rows: Sequence[Row[Any]] | None
    execution_options: _ExecuteOptions
    cursor_fetch_strategy: Incomplete
    invoked_statement: Executable | None
    cache_hit = NO_CACHE_KEY
    root_connection: Connection
    dialect: Dialect
    unicode_statement: str
    cursor: DBAPICursor
    compiled_parameters: List[_MutableCoreSingleExecuteParams]
    parameters: _DBAPIMultiExecuteParams
    extracted_parameters: Sequence[BindParameter[Any]] | None
    @property
    def executemany(self): ...
    def identifier_preparer(self): ...
    def engine(self): ...
    def postfetch_cols(self) -> Sequence[Column[Any]] | None: ...
    def prefetch_cols(self) -> Sequence[Column[Any]] | None: ...
    def no_parameters(self): ...
    def connection(self): ...
    def create_cursor(self): ...
    def fetchall_for_returning(self, cursor): ...
    def create_default_cursor(self): ...
    def create_server_side_cursor(self) -> None: ...
    def pre_exec(self) -> None: ...
    def get_out_parameter_values(self, names) -> None: ...
    def post_exec(self) -> None: ...
    def get_result_processor(self, type_, colname, coltype):
        """Return a 'result processor' for a given type as present in
        cursor.description.

        This has a default implementation that dialects can override
        for context-sensitive result type handling.

        """
    def get_lastrowid(self):
        '''return self.cursor.lastrowid, or equivalent, after an INSERT.

        This may involve calling special cursor functions, issuing a new SELECT
        on the cursor (or a new one), or returning a stored value that was
        calculated within post_exec().

        This function will only be called for dialects which support "implicit"
        primary key generation, keep preexecute_autoincrement_sequences set to
        False, and when no explicit id value was bound to the statement.

        The function is called once for an INSERT statement that would need to
        return the last inserted primary key for those dialects that make use
        of the lastrowid concept.  In these cases, it is called directly after
        :meth:`.ExecutionContext.post_exec`.

        '''
    def handle_dbapi_exception(self, e) -> None: ...
    def rowcount(self) -> int: ...
    def supports_sane_rowcount(self): ...
    def supports_sane_multi_rowcount(self): ...
    def inserted_primary_key_rows(self): ...
    def lastrow_has_defaults(self): ...
    current_parameters: _CoreSingleExecuteParams | None
    def get_current_parameters(self, isolate_multiinsert_groups: bool = True):
        """Return a dictionary of parameters applied to the current row.

        This method can only be used in the context of a user-defined default
        generation function, e.g. as described at
        :ref:`context_default_functions`. When invoked, a dictionary is
        returned which includes entries for each column/value pair that is part
        of the INSERT or UPDATE statement. The keys of the dictionary will be
        the key value of each :class:`_schema.Column`,
        which is usually synonymous
        with the name.

        :param isolate_multiinsert_groups=True: indicates that multi-valued
         INSERT constructs created using :meth:`_expression.Insert.values`
         should be
         handled by returning only the subset of parameters that are local
         to the current column default invocation.   When ``False``, the
         raw parameters of the statement are returned including the
         naming convention used in the case of multi-valued INSERT.

        .. versionadded:: 1.2  added
           :meth:`.DefaultExecutionContext.get_current_parameters`
           which provides more functionality over the existing
           :attr:`.DefaultExecutionContext.current_parameters`
           attribute.

        .. seealso::

            :attr:`.DefaultExecutionContext.current_parameters`

            :ref:`context_default_functions`

        """
    def get_insert_default(self, column): ...
    def get_update_default(self, column): ...
