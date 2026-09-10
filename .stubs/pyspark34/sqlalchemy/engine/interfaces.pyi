from .. import util as util
from ..event import EventTarget as EventTarget, dispatcher as dispatcher
from ..exc import StatementError as StatementError
from ..pool import Pool as Pool, PoolProxiedConnection as PoolProxiedConnection
from ..sql import Executable as Executable
from ..sql.compiler import Compiled as Compiled, DDLCompiler as DDLCompiler, IdentifierPreparer as IdentifierPreparer, InsertmanyvaluesSentinelOpts as InsertmanyvaluesSentinelOpts, Linting as Linting, SQLCompiler as SQLCompiler, TypeCompiler as TypeCompiler
from ..sql.elements import BindParameter as BindParameter, ClauseElement as ClauseElement
from ..sql.schema import Column as Column, DefaultGenerator as DefaultGenerator, SchemaItem as SchemaItem, Sequence as Sequence_SchemaItem
from ..sql.sqltypes import Integer as Integer
from ..sql.type_api import TypeEngine as TypeEngine
from ..util import immutabledict as immutabledict
from ..util.concurrency import await_only as await_only
from ..util.typing import Literal as Literal, NotRequired as NotRequired, Protocol as Protocol, TypedDict as TypedDict
from .base import Connection as Connection, Engine as Engine
from .cursor import CursorResult as CursorResult
from .url import URL as URL
from _typeshed import Incomplete
from enum import Enum
from types import ModuleType
from typing import Any, Awaitable, Callable, ClassVar, Collection, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Set, Tuple, Type

ConnectArgsType = Tuple[Sequence[str], MutableMapping[str, Any]]

class CacheStats(Enum):
    CACHE_HIT: int
    CACHE_MISS: int
    CACHING_DISABLED: int
    NO_CACHE_KEY: int
    NO_DIALECT_SUPPORT: int

class ExecuteStyle(Enum):
    """indicates the :term:`DBAPI` cursor method that will be used to invoke
    a statement."""
    EXECUTE: int
    EXECUTEMANY: int
    INSERTMANYVALUES: int

class DBAPIConnection(Protocol):
    """protocol representing a :pep:`249` database connection.

    .. versionadded:: 2.0

    .. seealso::

        `Connection Objects <https://www.python.org/dev/peps/pep-0249/#connection-objects>`_
        - in :pep:`249`

    """
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def cursor(self) -> DBAPICursor: ...
    def rollback(self) -> None: ...
    autocommit: bool

class DBAPIType(Protocol):
    """protocol representing a :pep:`249` database type.

    .. versionadded:: 2.0

    .. seealso::

        `Type Objects <https://www.python.org/dev/peps/pep-0249/#type-objects>`_
        - in :pep:`249`

    """

class DBAPICursor(Protocol):
    """protocol representing a :pep:`249` database cursor.

    .. versionadded:: 2.0

    .. seealso::

        `Cursor Objects <https://www.python.org/dev/peps/pep-0249/#cursor-objects>`_
        - in :pep:`249`

    """
    @property
    def description(self) -> _DBAPICursorDescription:
        """The description attribute of the Cursor.

        .. seealso::

            `cursor.description <https://www.python.org/dev/peps/pep-0249/#description>`_
            - in :pep:`249`


        """
    @property
    def rowcount(self) -> int: ...
    arraysize: int
    lastrowid: int
    def close(self) -> None: ...
    def execute(self, operation: Any, parameters: _DBAPISingleExecuteParams | None = None) -> Any: ...
    def executemany(self, operation: Any, parameters: Sequence[_DBAPIMultiExecuteParams]) -> Any: ...
    def fetchone(self) -> Any | None: ...
    def fetchmany(self, size: int = ...) -> Sequence[Any]: ...
    def fetchall(self) -> Sequence[Any]: ...
    def setinputsizes(self, sizes: Sequence[Any]) -> None: ...
    def setoutputsize(self, size: Any, column: Any) -> None: ...
    def callproc(self, procname: str, parameters: Sequence[Any] = ...) -> Any: ...
    def nextset(self) -> bool | None: ...
    def __getattr__(self, key: str) -> Any: ...

CompiledCacheType: Incomplete
SchemaTranslateMapType = Mapping[str | None, str | None]
IsolationLevel: Incomplete

class _CoreKnownExecutionOptions(TypedDict, total=False):
    compiled_cache: CompiledCacheType | None
    logging_token: str
    isolation_level: IsolationLevel
    no_parameters: bool
    stream_results: bool
    max_row_buffer: int
    yield_per: int
    insertmanyvalues_page_size: int
    schema_translate_map: SchemaTranslateMapType | None

CoreExecuteOptionsParameter: Incomplete

class ReflectedIdentity(TypedDict):
    """represent the reflected IDENTITY structure of a column, corresponding
    to the :class:`_schema.Identity` construct.

    The :class:`.ReflectedIdentity` structure is part of the
    :class:`.ReflectedColumn` structure, which is returned by the
    :meth:`.Inspector.get_columns` method.

    """
    always: bool
    on_null: bool
    start: int
    increment: int
    minvalue: int
    maxvalue: int
    nominvalue: bool
    nomaxvalue: bool
    cycle: bool
    cache: int | None
    order: bool

class ReflectedComputed(TypedDict):
    """Represent the reflected elements of a computed column, corresponding
    to the :class:`_schema.Computed` construct.

    The :class:`.ReflectedComputed` structure is part of the
    :class:`.ReflectedColumn` structure, which is returned by the
    :meth:`.Inspector.get_columns` method.

    """
    sqltext: str
    persisted: NotRequired[bool]

class ReflectedColumn(TypedDict):
    """Dictionary representing the reflected elements corresponding to
    a :class:`_schema.Column` object.

    The :class:`.ReflectedColumn` structure is returned by the
    :class:`.Inspector.get_columns` method.

    """
    name: str
    type: TypeEngine[Any]
    nullable: bool
    default: str | None
    autoincrement: NotRequired[bool]
    comment: NotRequired[str | None]
    computed: NotRequired[ReflectedComputed]
    identity: NotRequired[ReflectedIdentity]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedConstraint(TypedDict):
    """Dictionary representing the reflected elements corresponding to
    :class:`.Constraint`

    A base class for all constraints
    """
    name: str | None
    comment: NotRequired[str | None]

class ReflectedCheckConstraint(ReflectedConstraint):
    """Dictionary representing the reflected elements corresponding to
    :class:`.CheckConstraint`.

    The :class:`.ReflectedCheckConstraint` structure is returned by the
    :meth:`.Inspector.get_check_constraints` method.

    """
    sqltext: str
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedUniqueConstraint(ReflectedConstraint):
    """Dictionary representing the reflected elements corresponding to
    :class:`.UniqueConstraint`.

    The :class:`.ReflectedUniqueConstraint` structure is returned by the
    :meth:`.Inspector.get_unique_constraints` method.

    """
    column_names: List[str]
    duplicates_index: NotRequired[str | None]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedPrimaryKeyConstraint(ReflectedConstraint):
    """Dictionary representing the reflected elements corresponding to
    :class:`.PrimaryKeyConstraint`.

    The :class:`.ReflectedPrimaryKeyConstraint` structure is returned by the
    :meth:`.Inspector.get_pk_constraint` method.

    """
    constrained_columns: List[str]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedForeignKeyConstraint(ReflectedConstraint):
    """Dictionary representing the reflected elements corresponding to
    :class:`.ForeignKeyConstraint`.

    The :class:`.ReflectedForeignKeyConstraint` structure is returned by
    the :meth:`.Inspector.get_foreign_keys` method.

    """
    constrained_columns: List[str]
    referred_schema: str | None
    referred_table: str
    referred_columns: List[str]
    options: NotRequired[Dict[str, Any]]

class ReflectedIndex(TypedDict):
    """Dictionary representing the reflected elements corresponding to
    :class:`.Index`.

    The :class:`.ReflectedIndex` structure is returned by the
    :meth:`.Inspector.get_indexes` method.

    """
    name: str | None
    column_names: List[str | None]
    expressions: NotRequired[List[str]]
    unique: bool
    duplicates_constraint: NotRequired[str | None]
    include_columns: NotRequired[List[str]]
    column_sorting: NotRequired[Dict[str, Tuple[str]]]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedTableComment(TypedDict):
    """Dictionary representing the reflected comment corresponding to
    the :attr:`_schema.Table.comment` attribute.

    The :class:`.ReflectedTableComment` structure is returned by the
    :meth:`.Inspector.get_table_comment` method.

    """
    text: str | None

class BindTyping(Enum):
    """Define different methods of passing typing information for
    bound parameters in a statement to the database driver.

    .. versionadded:: 2.0

    """
    NONE: int
    SETINPUTSIZES: int
    RENDER_CASTS: int
VersionInfoType = Tuple[int | str, ...]
TableKey = Tuple[str | None, str]

class Dialect(EventTarget):
    """Define the behavior of a specific database and DB-API combination.

    Any aspect of metadata definition, SQL query generation,
    execution, result-set handling, or anything else which varies
    between databases is defined under the general category of the
    Dialect.  The Dialect acts as a factory for other
    database-specific object implementations including
    ExecutionContext, Compiled, DefaultGenerator, and TypeEngine.

    .. note:: Third party dialects should not subclass :class:`.Dialect`
       directly.  Instead, subclass :class:`.default.DefaultDialect` or
       descendant class.

    """
    CACHE_HIT: Incomplete
    CACHE_MISS: Incomplete
    CACHING_DISABLED: Incomplete
    NO_CACHE_KEY: Incomplete
    NO_DIALECT_SUPPORT: Incomplete
    dispatch: dispatcher[Dialect]
    name: str
    driver: str
    dialect_description: str
    dbapi: ModuleType | None
    def loaded_dbapi(self) -> ModuleType:
        """same as .dbapi, but is never None; will raise an error if no
        DBAPI was set up.

        .. versionadded:: 2.0

        """
    positional: bool
    paramstyle: str
    compiler_linting: Linting
    statement_compiler: Type[SQLCompiler]
    ddl_compiler: Type[DDLCompiler]
    type_compiler_cls: ClassVar[Type[TypeCompiler]]
    type_compiler_instance: TypeCompiler
    type_compiler: Any
    preparer: Type[IdentifierPreparer]
    identifier_preparer: IdentifierPreparer
    server_version_info: Tuple[Any, ...] | None
    default_schema_name: str | None
    default_isolation_level: IsolationLevel | None
    execution_ctx_cls: Type[ExecutionContext]
    execute_sequence_format: Type[Tuple[Any, ...]] | Type[Tuple[List[Any]]]
    supports_alter: bool
    max_identifier_length: int
    supports_server_side_cursors: bool
    server_side_cursors: bool
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_empty_insert: bool
    supports_default_values: bool
    supports_default_metavalue: bool
    default_metavalue_token: str
    supports_multivalues_insert: bool
    insert_executemany_returning: bool
    insert_executemany_returning_sort_by_parameter_order: bool
    update_executemany_returning: bool
    delete_executemany_returning: bool
    use_insertmanyvalues: bool
    use_insertmanyvalues_wo_returning: bool
    insertmanyvalues_implicit_sentinel: InsertmanyvaluesSentinelOpts
    insertmanyvalues_page_size: int
    insertmanyvalues_max_parameters: int
    preexecute_autoincrement_sequences: bool
    insert_returning: bool
    update_returning: bool
    update_returning_multifrom: bool
    delete_returning: bool
    delete_returning_multifrom: bool
    favor_returning_over_lastrowid: bool
    supports_identity_columns: bool
    cte_follows_insert: bool
    colspecs: MutableMapping[Type[TypeEngine[Any]], Type[TypeEngine[Any]]]
    supports_sequences: bool
    sequences_optional: bool
    default_sequence_base: int
    supports_native_enum: bool
    supports_native_boolean: bool
    supports_native_decimal: bool
    supports_native_uuid: bool
    returns_native_bytes: bool
    construct_arguments: List[Tuple[Type[SchemaItem | ClauseElement], Mapping[str, Any]]] | None
    reflection_options: Sequence[str]
    dbapi_exception_translation_map: Mapping[str, str]
    supports_comments: bool
    inline_comments: bool
    supports_constraint_comments: bool
    supports_statement_cache: bool
    bind_typing: Incomplete
    is_async: bool
    has_terminate: bool
    engine_config_types: Mapping[str, Any]
    label_length: int | None
    include_set_input_sizes: Set[Any] | None
    exclude_set_input_sizes: Set[Any] | None
    supports_simple_order_by_label: bool
    div_is_floordiv: bool
    tuple_in_values: bool
    def create_connect_args(self, url: URL) -> ConnectArgsType:
        """Build DB-API compatible connection arguments.

        Given a :class:`.URL` object, returns a tuple
        consisting of a ``(*args, **kwargs)`` suitable to send directly
        to the dbapi's connect function.   The arguments are sent to the
        :meth:`.Dialect.connect` method which then runs the DBAPI-level
        ``connect()`` function.

        The method typically makes use of the
        :meth:`.URL.translate_connect_args`
        method in order to generate a dictionary of options.

        The default implementation is::

            def create_connect_args(self, url):
                opts = url.translate_connect_args()
                opts.update(url.query)
                return ([], opts)

        :param url: a :class:`.URL` object

        :return: a tuple of ``(*args, **kwargs)`` which will be passed to the
         :meth:`.Dialect.connect` method.

        .. seealso::

            :meth:`.URL.translate_connect_args`

        """
    @classmethod
    def import_dbapi(cls) -> ModuleType:
        """Import the DBAPI module that is used by this dialect.

        The Python module object returned here will be assigned as an
        instance variable to a constructed dialect under the name
        ``.dbapi``.

        .. versionchanged:: 2.0  The :meth:`.Dialect.import_dbapi` class
           method is renamed from the previous method ``.Dialect.dbapi()``,
           which would be replaced at dialect instantiation time by the
           DBAPI module itself, thus using the same name in two different ways.
           If a ``.Dialect.dbapi()`` classmethod is present on a third-party
           dialect, it will be used and a deprecation warning will be emitted.

        """
    @classmethod
    def type_descriptor(cls, typeobj: TypeEngine[_T]) -> TypeEngine[_T]:
        """Transform a generic type to a dialect-specific type.

        Dialect classes will usually use the
        :func:`_types.adapt_type` function in the types module to
        accomplish this.

        The returned result is cached *per dialect class* so can
        contain no dialect-instance state.

        """
    def initialize(self, connection: Connection) -> None:
        """Called during strategized creation of the dialect with a
        connection.

        Allows dialects to configure options based on server version info or
        other properties.

        The connection passed here is a SQLAlchemy Connection object,
        with full capabilities.

        The initialize() method of the base dialect should be called via
        super().

        .. note:: as of SQLAlchemy 1.4, this method is called **before**
           any :meth:`_engine.Dialect.on_connect` hooks are called.

        """
    def get_columns(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedColumn]:
        """Return information about columns in ``table_name``.

        Given a :class:`_engine.Connection`, a string
        ``table_name``, and an optional string ``schema``, return column
        information as a list of dictionaries
        corresponding to the :class:`.ReflectedColumn` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_columns`.

        """
    def get_multi_columns(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedColumn]]]:
        """Return information about columns in all tables in the
        given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_columns`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def get_pk_constraint(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> ReflectedPrimaryKeyConstraint:
        """Return information about the primary key constraint on
        table_name`.

        Given a :class:`_engine.Connection`, a string
        ``table_name``, and an optional string ``schema``, return primary
        key information as a dictionary corresponding to the
        :class:`.ReflectedPrimaryKeyConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_pk_constraint`.

        """
    def get_multi_pk_constraint(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, ReflectedPrimaryKeyConstraint]]:
        """Return information about primary key constraints in
        all tables in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_pk_constraint`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def get_foreign_keys(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedForeignKeyConstraint]:
        """Return information about foreign_keys in ``table_name``.

        Given a :class:`_engine.Connection`, a string
        ``table_name``, and an optional string ``schema``, return foreign
        key information as a list of dicts corresponding to the
        :class:`.ReflectedForeignKeyConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_foreign_keys`.
        """
    def get_multi_foreign_keys(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedForeignKeyConstraint]]]:
        """Return information about foreign_keys in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_multi_foreign_keys`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def get_table_names(self, connection: Connection, schema: str | None = None, **kw: Any) -> List[str]:
        """Return a list of table names for ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_table_names`.

        """
    def get_temp_table_names(self, connection: Connection, schema: str | None = None, **kw: Any) -> List[str]:
        """Return a list of temporary table names on the given connection,
        if supported by the underlying backend.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_temp_table_names`.

        """
    def get_view_names(self, connection: Connection, schema: str | None = None, **kw: Any) -> List[str]:
        """Return a list of all non-materialized view names available in the
        database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_view_names`.

        :param schema: schema name to query, if not the default schema.

        """
    def get_materialized_view_names(self, connection: Connection, schema: str | None = None, **kw: Any) -> List[str]:
        """Return a list of all materialized view names available in the
        database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_materialized_view_names`.

        :param schema: schema name to query, if not the default schema.

         .. versionadded:: 2.0

        """
    def get_sequence_names(self, connection: Connection, schema: str | None = None, **kw: Any) -> List[str]:
        """Return a list of all sequence names available in the database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_sequence_names`.

        :param schema: schema name to query, if not the default schema.

        .. versionadded:: 1.4
        """
    def get_temp_view_names(self, connection: Connection, schema: str | None = None, **kw: Any) -> List[str]:
        """Return a list of temporary view names on the given connection,
        if supported by the underlying backend.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_temp_view_names`.

        """
    def get_schema_names(self, connection: Connection, **kw: Any) -> List[str]:
        """Return a list of all schema names available in the database.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_schema_names`.
        """
    def get_view_definition(self, connection: Connection, view_name: str, schema: str | None = None, **kw: Any) -> str:
        """Return plain or materialized view definition.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_view_definition`.

        Given a :class:`_engine.Connection`, a string
        ``view_name``, and an optional string ``schema``, return the view
        definition.
        """
    def get_indexes(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedIndex]:
        """Return information about indexes in ``table_name``.

        Given a :class:`_engine.Connection`, a string
        ``table_name`` and an optional string ``schema``, return index
        information as a list of dictionaries corresponding to the
        :class:`.ReflectedIndex` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_indexes`.
        """
    def get_multi_indexes(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedIndex]]]:
        """Return information about indexes in in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_indexes`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def get_unique_constraints(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedUniqueConstraint]:
        """Return information about unique constraints in ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``, return
        unique constraint information as a list of dicts corresponding
        to the :class:`.ReflectedUniqueConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_unique_constraints`.
        """
    def get_multi_unique_constraints(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedUniqueConstraint]]]:
        """Return information about unique constraints in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_unique_constraints`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def get_check_constraints(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedCheckConstraint]:
        """Return information about check constraints in ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``, return
        check constraint information as a list of dicts corresponding
        to the :class:`.ReflectedCheckConstraint` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_check_constraints`.

        """
    def get_multi_check_constraints(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedCheckConstraint]]]:
        """Return information about check constraints in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_multi_check_constraints`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def get_table_options(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> Dict[str, Any]:
        """Return a dictionary of options specified when ``table_name``
        was created.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_table_options`.
        """
    def get_multi_table_options(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, Dict[str, Any]]]:
        """Return a dictionary of options specified when the tables in the
        given schema were created.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_multi_table_options`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def get_table_comment(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> ReflectedTableComment:
        '''Return the "comment" for the table identified by ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``, return
        table comment information as a dictionary corresponding to the
        :class:`.ReflectedTableComment` dictionary.

        This is an internal dialect method. Applications should use
        :meth:`.Inspector.get_table_comment`.

        :raise: ``NotImplementedError`` for dialects that don\'t support
         comments.

        .. versionadded:: 1.2

        '''
    def get_multi_table_comment(self, connection: Connection, schema: str | None = None, filter_names: Collection[str] | None = None, **kw: Any) -> Iterable[Tuple[TableKey, ReflectedTableComment]]:
        """Return information about the table comment in all tables
        in the given ``schema``.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.get_multi_table_comment`.

        .. note:: The :class:`_engine.DefaultDialect` provides a default
          implementation that will call the single table method for
          each object returned by :meth:`Dialect.get_table_names`,
          :meth:`Dialect.get_view_names` or
          :meth:`Dialect.get_materialized_view_names` depending on the
          provided ``kind``. Dialects that want to support a faster
          implementation should implement this method.

        .. versionadded:: 2.0

        """
    def normalize_name(self, name: str) -> str:
        """convert the given name to lowercase if it is detected as
        case insensitive.

        This method is only used if the dialect defines
        requires_name_normalize=True.

        """
    def denormalize_name(self, name: str) -> str:
        """convert the given name to a case insensitive identifier
        for the backend if it is an all-lowercase name.

        This method is only used if the dialect defines
        requires_name_normalize=True.

        """
    def has_table(self, connection: Connection, table_name: str, schema: str | None = None, **kw: Any) -> bool:
        '''For internal dialect use, check the existence of a particular table
        or view in the database.

        Given a :class:`_engine.Connection` object, a string table_name and
        optional schema name, return True if the given table exists in the
        database, False otherwise.

        This method serves as the underlying implementation of the
        public facing :meth:`.Inspector.has_table` method, and is also used
        internally to implement the "checkfirst" behavior for methods like
        :meth:`_schema.Table.create` and :meth:`_schema.MetaData.create_all`.

        .. note:: This method is used internally by SQLAlchemy, and is
           published so that third-party dialects may provide an
           implementation. It is **not** the public API for checking for table
           presence. Please use the :meth:`.Inspector.has_table` method.

        .. versionchanged:: 2.0:: :meth:`_engine.Dialect.has_table` now
           formally supports checking for additional table-like objects:

           * any type of views (plain or materialized)
           * temporary tables of any kind

           Previously, these two checks were not formally specified and
           different dialects would vary in their behavior.   The dialect
           testing suite now includes tests for all of these object types,
           and dialects to the degree that the backing database supports views
           or temporary tables should seek to support locating these objects
           for full compliance.

        '''
    def has_index(self, connection: Connection, table_name: str, index_name: str, schema: str | None = None, **kw: Any) -> bool:
        """Check the existence of a particular index name in the database.

        Given a :class:`_engine.Connection` object, a string
        ``table_name`` and string index name, return ``True`` if an index of
        the given name on the given table exists, ``False`` otherwise.

        The :class:`.DefaultDialect` implements this in terms of the
        :meth:`.Dialect.has_table` and :meth:`.Dialect.get_indexes` methods,
        however dialects can implement a more performant version.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.has_index`.

        .. versionadded:: 1.4

        """
    def has_sequence(self, connection: Connection, sequence_name: str, schema: str | None = None, **kw: Any) -> bool:
        """Check the existence of a particular sequence in the database.

        Given a :class:`_engine.Connection` object and a string
        `sequence_name`, return ``True`` if the given sequence exists in
        the database, ``False`` otherwise.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.has_sequence`.
        """
    def has_schema(self, connection: Connection, schema_name: str, **kw: Any) -> bool:
        """Check the existence of a particular schema name in the database.

        Given a :class:`_engine.Connection` object, a string
        ``schema_name``, return ``True`` if a schema of the
        given exists, ``False`` otherwise.

        The :class:`.DefaultDialect` implements this by checking
        the presence of ``schema_name`` among the schemas returned by
        :meth:`.Dialect.get_schema_names`,
        however dialects can implement a more performant version.

        This is an internal dialect method. Applications should use
        :meth:`_engine.Inspector.has_schema`.

        .. versionadded:: 2.0

        """
    def do_begin(self, dbapi_connection: PoolProxiedConnection) -> None:
        '''Provide an implementation of ``connection.begin()``, given a
        DB-API connection.

        The DBAPI has no dedicated "begin" method and it is expected
        that transactions are implicit.  This hook is provided for those
        DBAPIs that might need additional help in this area.

        :param dbapi_connection: a DBAPI connection, typically
         proxied within a :class:`.ConnectionFairy`.

        '''
    def do_rollback(self, dbapi_connection: PoolProxiedConnection) -> None:
        """Provide an implementation of ``connection.rollback()``, given
        a DB-API connection.

        :param dbapi_connection: a DBAPI connection, typically
         proxied within a :class:`.ConnectionFairy`.

        """
    def do_commit(self, dbapi_connection: PoolProxiedConnection) -> None:
        """Provide an implementation of ``connection.commit()``, given a
        DB-API connection.

        :param dbapi_connection: a DBAPI connection, typically
         proxied within a :class:`.ConnectionFairy`.

        """
    def do_terminate(self, dbapi_connection: DBAPIConnection) -> None:
        """Provide an implementation of ``connection.close()`` that tries as
        much as possible to not block, given a DBAPI
        connection.

        In the vast majority of cases this just calls .close(), however
        for some asyncio dialects may call upon different API features.

        This hook is called by the :class:`_pool.Pool`
        when a connection is being recycled or has been invalidated.

        .. versionadded:: 1.4.41

        """
    def do_close(self, dbapi_connection: DBAPIConnection) -> None:
        """Provide an implementation of ``connection.close()``, given a DBAPI
        connection.

        This hook is called by the :class:`_pool.Pool`
        when a connection has been
        detached from the pool, or is being returned beyond the normal
        capacity of the pool.

        """
    def do_ping(self, dbapi_connection: DBAPIConnection) -> bool:
        """ping the DBAPI connection and return True if the connection is
        usable."""
    def do_set_input_sizes(self, cursor: DBAPICursor, list_of_tuples: _GenericSetInputSizesType, context: ExecutionContext) -> Any:
        """invoke the cursor.setinputsizes() method with appropriate arguments

        This hook is called if the :attr:`.Dialect.bind_typing` attribute is
        set to the
        :attr:`.BindTyping.SETINPUTSIZES` value.
        Parameter data is passed in a list of tuples (paramname, dbtype,
        sqltype), where ``paramname`` is the key of the parameter in the
        statement, ``dbtype`` is the DBAPI datatype and ``sqltype`` is the
        SQLAlchemy type. The order of tuples is in the correct parameter order.

        .. versionadded:: 1.4

        .. versionchanged:: 2.0  - setinputsizes mode is now enabled by
           setting :attr:`.Dialect.bind_typing` to
           :attr:`.BindTyping.SETINPUTSIZES`.  Dialects which accept
           a ``use_setinputsizes`` parameter should set this value
           appropriately.


        """
    def create_xid(self) -> Any:
        """Create a two-phase transaction ID.

        This id will be passed to do_begin_twophase(),
        do_rollback_twophase(), do_commit_twophase().  Its format is
        unspecified.
        """
    def do_savepoint(self, connection: Connection, name: str) -> None:
        """Create a savepoint with the given name.

        :param connection: a :class:`_engine.Connection`.
        :param name: savepoint name.

        """
    def do_rollback_to_savepoint(self, connection: Connection, name: str) -> None:
        """Rollback a connection to the named savepoint.

        :param connection: a :class:`_engine.Connection`.
        :param name: savepoint name.

        """
    def do_release_savepoint(self, connection: Connection, name: str) -> None:
        """Release the named savepoint on a connection.

        :param connection: a :class:`_engine.Connection`.
        :param name: savepoint name.
        """
    def do_begin_twophase(self, connection: Connection, xid: Any) -> None:
        """Begin a two phase transaction on the given connection.

        :param connection: a :class:`_engine.Connection`.
        :param xid: xid

        """
    def do_prepare_twophase(self, connection: Connection, xid: Any) -> None:
        """Prepare a two phase transaction on the given connection.

        :param connection: a :class:`_engine.Connection`.
        :param xid: xid

        """
    def do_rollback_twophase(self, connection: Connection, xid: Any, is_prepared: bool = True, recover: bool = False) -> None:
        """Rollback a two phase transaction on the given connection.

        :param connection: a :class:`_engine.Connection`.
        :param xid: xid
        :param is_prepared: whether or not
         :meth:`.TwoPhaseTransaction.prepare` was called.
        :param recover: if the recover flag was passed.

        """
    def do_commit_twophase(self, connection: Connection, xid: Any, is_prepared: bool = True, recover: bool = False) -> None:
        """Commit a two phase transaction on the given connection.


        :param connection: a :class:`_engine.Connection`.
        :param xid: xid
        :param is_prepared: whether or not
         :meth:`.TwoPhaseTransaction.prepare` was called.
        :param recover: if the recover flag was passed.

        """
    def do_recover_twophase(self, connection: Connection) -> List[Any]:
        """Recover list of uncommitted prepared two phase transaction
        identifiers on the given connection.

        :param connection: a :class:`_engine.Connection`.

        """
    def do_executemany(self, cursor: DBAPICursor, statement: str, parameters: _DBAPIMultiExecuteParams, context: ExecutionContext | None = None) -> None:
        """Provide an implementation of ``cursor.executemany(statement,
        parameters)``."""
    def do_execute(self, cursor: DBAPICursor, statement: str, parameters: _DBAPISingleExecuteParams | None, context: ExecutionContext | None = None) -> None:
        """Provide an implementation of ``cursor.execute(statement,
        parameters)``."""
    def do_execute_no_params(self, cursor: DBAPICursor, statement: str, context: ExecutionContext | None = None) -> None:
        """Provide an implementation of ``cursor.execute(statement)``.

        The parameter collection should not be sent.

        """
    def is_disconnect(self, e: Exception, connection: PoolProxiedConnection | DBAPIConnection | None, cursor: DBAPICursor | None) -> bool:
        """Return True if the given DB-API error indicates an invalid
        connection"""
    def connect(self, *cargs: Any, **cparams: Any) -> DBAPIConnection:
        """Establish a connection using this dialect's DBAPI.

        The default implementation of this method is::

            def connect(self, *cargs, **cparams):
                return self.dbapi.connect(*cargs, **cparams)

        The ``*cargs, **cparams`` parameters are generated directly
        from this dialect's :meth:`.Dialect.create_connect_args` method.

        This method may be used for dialects that need to perform programmatic
        per-connection steps when a new connection is procured from the
        DBAPI.


        :param \\*cargs: positional parameters returned from the
         :meth:`.Dialect.create_connect_args` method

        :param \\*\\*cparams: keyword parameters returned from the
         :meth:`.Dialect.create_connect_args` method.

        :return: a DBAPI connection, typically from the :pep:`249` module
         level ``.connect()`` function.

        .. seealso::

            :meth:`.Dialect.create_connect_args`

            :meth:`.Dialect.on_connect`

        """
    def on_connect_url(self, url: URL) -> Callable[[Any], Any] | None:
        '''return a callable which sets up a newly created DBAPI connection.

        This method is a new hook that supersedes the
        :meth:`_engine.Dialect.on_connect` method when implemented by a
        dialect.   When not implemented by a dialect, it invokes the
        :meth:`_engine.Dialect.on_connect` method directly to maintain
        compatibility with existing dialects.   There is no deprecation
        for :meth:`_engine.Dialect.on_connect` expected.

        The callable should accept a single argument "conn" which is the
        DBAPI connection itself.  The inner callable has no
        return value.

        E.g.::

            class MyDialect(default.DefaultDialect):
                # ...

                def on_connect_url(self, url):
                    def do_on_connect(connection):
                        connection.execute("SET SPECIAL FLAGS etc")

                    return do_on_connect

        This is used to set dialect-wide per-connection options such as
        isolation modes, Unicode modes, etc.

        This method differs from :meth:`_engine.Dialect.on_connect` in that
        it is passed the :class:`_engine.URL` object that\'s relevant to the
        connect args.  Normally the only way to get this is from the
        :meth:`_engine.Dialect.on_connect` hook is to look on the
        :class:`_engine.Engine` itself, however this URL object may have been
        replaced by plugins.

        .. note::

            The default implementation of
            :meth:`_engine.Dialect.on_connect_url` is to invoke the
            :meth:`_engine.Dialect.on_connect` method. Therefore if a dialect
            implements this method, the :meth:`_engine.Dialect.on_connect`
            method **will not be called** unless the overriding dialect calls
            it directly from here.

        .. versionadded:: 1.4.3 added :meth:`_engine.Dialect.on_connect_url`
           which normally calls into :meth:`_engine.Dialect.on_connect`.

        :param url: a :class:`_engine.URL` object representing the
         :class:`_engine.URL` that was passed to the
         :meth:`_engine.Dialect.create_connect_args` method.

        :return: a callable that accepts a single DBAPI connection as an
         argument, or None.

        .. seealso::

            :meth:`_engine.Dialect.on_connect`

        '''
    def on_connect(self) -> Callable[[Any], Any] | None:
        '''return a callable which sets up a newly created DBAPI connection.

        The callable should accept a single argument "conn" which is the
        DBAPI connection itself.  The inner callable has no
        return value.

        E.g.::

            class MyDialect(default.DefaultDialect):
                # ...

                def on_connect(self):
                    def do_on_connect(connection):
                        connection.execute("SET SPECIAL FLAGS etc")

                    return do_on_connect

        This is used to set dialect-wide per-connection options such as
        isolation modes, Unicode modes, etc.

        The "do_on_connect" callable is invoked by using the
        :meth:`_events.PoolEvents.connect` event
        hook, then unwrapping the DBAPI connection and passing it into the
        callable.

        .. versionchanged:: 1.4 the on_connect hook is no longer called twice
           for the first connection of a dialect.  The on_connect hook is still
           called before the :meth:`_engine.Dialect.initialize` method however.

        .. versionchanged:: 1.4.3 the on_connect hook is invoked from a new
           method on_connect_url that passes the URL that was used to create
           the connect args.   Dialects can implement on_connect_url instead
           of on_connect if they need the URL object that was used for the
           connection in order to get additional context.

        If None is returned, no event listener is generated.

        :return: a callable that accepts a single DBAPI connection as an
         argument, or None.

        .. seealso::

            :meth:`.Dialect.connect` - allows the DBAPI ``connect()`` sequence
            itself to be controlled.

            :meth:`.Dialect.on_connect_url` - supersedes
            :meth:`.Dialect.on_connect` to also receive the
            :class:`_engine.URL` object in context.

        '''
    def reset_isolation_level(self, dbapi_connection: DBAPIConnection) -> None:
        """Given a DBAPI connection, revert its isolation to the default.

        Note that this is a dialect-level method which is used as part
        of the implementation of the :class:`_engine.Connection` and
        :class:`_engine.Engine`
        isolation level facilities; these APIs should be preferred for
        most typical use cases.

        .. seealso::

            :meth:`_engine.Connection.get_isolation_level`
            - view current level

            :attr:`_engine.Connection.default_isolation_level`
            - view default level

            :paramref:`.Connection.execution_options.isolation_level` -
            set per :class:`_engine.Connection` isolation level

            :paramref:`_sa.create_engine.isolation_level` -
            set per :class:`_engine.Engine` isolation level

        """
    def set_isolation_level(self, dbapi_connection: DBAPIConnection, level: IsolationLevel) -> None:
        """Given a DBAPI connection, set its isolation level.

        Note that this is a dialect-level method which is used as part
        of the implementation of the :class:`_engine.Connection` and
        :class:`_engine.Engine`
        isolation level facilities; these APIs should be preferred for
        most typical use cases.

        If the dialect also implements the
        :meth:`.Dialect.get_isolation_level_values` method, then the given
        level is guaranteed to be one of the string names within that sequence,
        and the method will not need to anticipate a lookup failure.

        .. seealso::

            :meth:`_engine.Connection.get_isolation_level`
            - view current level

            :attr:`_engine.Connection.default_isolation_level`
            - view default level

            :paramref:`.Connection.execution_options.isolation_level` -
            set per :class:`_engine.Connection` isolation level

            :paramref:`_sa.create_engine.isolation_level` -
            set per :class:`_engine.Engine` isolation level

        """
    def get_isolation_level(self, dbapi_connection: DBAPIConnection) -> IsolationLevel:
        """Given a DBAPI connection, return its isolation level.

        When working with a :class:`_engine.Connection` object,
        the corresponding
        DBAPI connection may be procured using the
        :attr:`_engine.Connection.connection` accessor.

        Note that this is a dialect-level method which is used as part
        of the implementation of the :class:`_engine.Connection` and
        :class:`_engine.Engine` isolation level facilities;
        these APIs should be preferred for most typical use cases.


        .. seealso::

            :meth:`_engine.Connection.get_isolation_level`
            - view current level

            :attr:`_engine.Connection.default_isolation_level`
            - view default level

            :paramref:`.Connection.execution_options.isolation_level` -
            set per :class:`_engine.Connection` isolation level

            :paramref:`_sa.create_engine.isolation_level` -
            set per :class:`_engine.Engine` isolation level


        """
    def get_default_isolation_level(self, dbapi_conn: DBAPIConnection) -> IsolationLevel:
        """Given a DBAPI connection, return its isolation level, or
        a default isolation level if one cannot be retrieved.

        This method may only raise NotImplementedError and
        **must not raise any other exception**, as it is used implicitly upon
        first connect.

        The method **must return a value** for a dialect that supports
        isolation level settings, as this level is what will be reverted
        towards when a per-connection isolation level change is made.

        The method defaults to using the :meth:`.Dialect.get_isolation_level`
        method unless overridden by a dialect.

        .. versionadded:: 1.3.22

        """
    def get_isolation_level_values(self, dbapi_conn: DBAPIConnection) -> List[IsolationLevel]:
        '''return a sequence of string isolation level names that are accepted
        by this dialect.

        The available names should use the following conventions:

        * use UPPERCASE names.   isolation level methods will accept lowercase
          names but these are normalized into UPPERCASE before being passed
          along to the dialect.
        * separate words should be separated by spaces, not underscores, e.g.
          ``REPEATABLE READ``.  isolation level names will have underscores
          converted to spaces before being passed along to the dialect.
        * The names for the four standard isolation names to the extent that
          they are supported by the backend should be ``READ UNCOMMITTED``
          ``READ COMMITTED``, ``REPEATABLE READ``, ``SERIALIZABLE``
        * if the dialect supports an autocommit option it should be provided
          using the isolation level name ``AUTOCOMMIT``.
        * Other isolation modes may also be present, provided that they
          are named in UPPERCASE and use spaces not underscores.

        This function is used so that the default dialect can check that
        a given isolation level parameter is valid, else raises an
        :class:`_exc.ArgumentError`.

        A DBAPI connection is passed to the method, in the unlikely event that
        the dialect needs to interrogate the connection itself to determine
        this list, however it is expected that most backends will return
        a hardcoded list of values.  If the dialect supports "AUTOCOMMIT",
        that value should also be present in the sequence returned.

        The method raises ``NotImplementedError`` by default.  If a dialect
        does not implement this method, then the default dialect will not
        perform any checking on a given isolation level value before passing
        it onto the :meth:`.Dialect.set_isolation_level` method.  This is
        to allow backwards-compatibility with third party dialects that may
        not yet be implementing this method.

        .. versionadded:: 2.0

        '''
    @classmethod
    def get_dialect_cls(cls, url: URL) -> Type[Dialect]:
        """Given a URL, return the :class:`.Dialect` that will be used.

        This is a hook that allows an external plugin to provide functionality
        around an existing dialect, by allowing the plugin to be loaded
        from the url based on an entrypoint, and then the plugin returns
        the actual dialect to be used.

        By default this just returns the cls.

        """
    @classmethod
    def get_async_dialect_cls(cls, url: URL) -> Type[Dialect]:
        """Given a URL, return the :class:`.Dialect` that will be used by
        an async engine.

        By default this is an alias of :meth:`.Dialect.get_dialect_cls` and
        just returns the cls. It may be used if a dialect provides
        both a sync and async version under the same name, like the
        ``psycopg`` driver.

        .. versionadded:: 2

        .. seealso::

            :meth:`.Dialect.get_dialect_cls`

        """
    @classmethod
    def load_provisioning(cls) -> None:
        '''set up the provision.py module for this dialect.

        For dialects that include a provision.py module that sets up
        provisioning followers, this method should initiate that process.

        A typical implementation would be::

            @classmethod
            def load_provisioning(cls):
                __import__("mydialect.provision")

        The default method assumes a module named ``provision.py`` inside
        the owning package of the current dialect, based on the ``__module__``
        attribute::

            @classmethod
            def load_provisioning(cls):
                package = ".".join(cls.__module__.split(".")[0:-1])
                try:
                    __import__(package + ".provision")
                except ImportError:
                    pass

        .. versionadded:: 1.3.14

        '''
    @classmethod
    def engine_created(cls, engine: Engine) -> None:
        """A convenience hook called before returning the final
        :class:`_engine.Engine`.

        If the dialect returned a different class from the
        :meth:`.get_dialect_cls`
        method, then the hook is called on both classes, first on
        the dialect class returned by the :meth:`.get_dialect_cls` method and
        then on the class on which the method was called.

        The hook should be used by dialects and/or wrappers to apply special
        events to the engine or its components.   In particular, it allows
        a dialect-wrapping class to apply dialect-level events.

        """
    def get_driver_connection(self, connection: DBAPIConnection) -> Any:
        """Returns the connection object as returned by the external driver
        package.

        For normal dialects that use a DBAPI compliant driver this call
        will just return the ``connection`` passed as argument.
        For dialects that instead adapt a non DBAPI compliant driver, like
        when adapting an asyncio driver, this call will return the
        connection-like object as returned by the driver.

        .. versionadded:: 1.4.24

        """
    def set_engine_execution_options(self, engine: Engine, opts: CoreExecuteOptionsParameter) -> None:
        """Establish execution options for a given engine.

        This is implemented by :class:`.DefaultDialect` to establish
        event hooks for new :class:`.Connection` instances created
        by the given :class:`.Engine` which will then invoke the
        :meth:`.Dialect.set_connection_execution_options` method for that
        connection.

        """
    def set_connection_execution_options(self, connection: Connection, opts: CoreExecuteOptionsParameter) -> None:
        """Establish execution options for a given connection.

        This is implemented by :class:`.DefaultDialect` in order to implement
        the :paramref:`_engine.Connection.execution_options.isolation_level`
        execution option.  Dialects can intercept various execution options
        which may need to modify state on a particular DBAPI connection.

        .. versionadded:: 1.4

        """
    def get_dialect_pool_class(self, url: URL) -> Type[Pool]:
        """return a Pool class to use for a given URL"""

class CreateEnginePlugin:
    '''A set of hooks intended to augment the construction of an
    :class:`_engine.Engine` object based on entrypoint names in a URL.

    The purpose of :class:`_engine.CreateEnginePlugin` is to allow third-party
    systems to apply engine, pool and dialect level event listeners without
    the need for the target application to be modified; instead, the plugin
    names can be added to the database URL.  Target applications for
    :class:`_engine.CreateEnginePlugin` include:

    * connection and SQL performance tools, e.g. which use events to track
      number of checkouts and/or time spent with statements

    * connectivity plugins such as proxies

    A rudimentary :class:`_engine.CreateEnginePlugin` that attaches a logger
    to an :class:`_engine.Engine` object might look like::


        import logging

        from sqlalchemy.engine import CreateEnginePlugin
        from sqlalchemy import event

        class LogCursorEventsPlugin(CreateEnginePlugin):
            def __init__(self, url, kwargs):
                # consume the parameter "log_cursor_logging_name" from the
                # URL query
                logging_name = url.query.get("log_cursor_logging_name", "log_cursor")

                self.log = logging.getLogger(logging_name)

            def update_url(self, url):
                "update the URL to one that no longer includes our parameters"
                return url.difference_update_query(["log_cursor_logging_name"])

            def engine_created(self, engine):
                "attach an event listener after the new Engine is constructed"
                event.listen(engine, "before_cursor_execute", self._log_event)


            def _log_event(
                self,
                conn,
                cursor,
                statement,
                parameters,
                context,
                executemany):

                self.log.info("Plugin logged cursor event: %s", statement)



    Plugins are registered using entry points in a similar way as that
    of dialects::

        entry_points={
            \'sqlalchemy.plugins\': [
                \'log_cursor_plugin = myapp.plugins:LogCursorEventsPlugin\'
            ]

    A plugin that uses the above names would be invoked from a database
    URL as in::

        from sqlalchemy import create_engine

        engine = create_engine(
            "mysql+pymysql://scott:tiger@localhost/test?"
            "plugin=log_cursor_plugin&log_cursor_logging_name=mylogger"
        )

    The ``plugin`` URL parameter supports multiple instances, so that a URL
    may specify multiple plugins; they are loaded in the order stated
    in the URL::

        engine = create_engine(
          "mysql+pymysql://scott:tiger@localhost/test?"
          "plugin=plugin_one&plugin=plugin_twp&plugin=plugin_three")

    The plugin names may also be passed directly to :func:`_sa.create_engine`
    using the :paramref:`_sa.create_engine.plugins` argument::

        engine = create_engine(
          "mysql+pymysql://scott:tiger@localhost/test",
          plugins=["myplugin"])

    .. versionadded:: 1.2.3  plugin names can also be specified
       to :func:`_sa.create_engine` as a list

    A plugin may consume plugin-specific arguments from the
    :class:`_engine.URL` object as well as the ``kwargs`` dictionary, which is
    the dictionary of arguments passed to the :func:`_sa.create_engine`
    call.  "Consuming" these arguments includes that they must be removed
    when the plugin initializes, so that the arguments are not passed along
    to the :class:`_engine.Dialect` constructor, where they will raise an
    :class:`_exc.ArgumentError` because they are not known by the dialect.

    As of version 1.4 of SQLAlchemy, arguments should continue to be consumed
    from the ``kwargs`` dictionary directly, by removing the values with a
    method such as ``dict.pop``. Arguments from the :class:`_engine.URL` object
    should be consumed by implementing the
    :meth:`_engine.CreateEnginePlugin.update_url` method, returning a new copy
    of the :class:`_engine.URL` with plugin-specific parameters removed::

        class MyPlugin(CreateEnginePlugin):
            def __init__(self, url, kwargs):
                self.my_argument_one = url.query[\'my_argument_one\']
                self.my_argument_two = url.query[\'my_argument_two\']
                self.my_argument_three = kwargs.pop(\'my_argument_three\', None)

            def update_url(self, url):
                return url.difference_update_query(
                    ["my_argument_one", "my_argument_two"]
                )

    Arguments like those illustrated above would be consumed from a
    :func:`_sa.create_engine` call such as::

        from sqlalchemy import create_engine

        engine = create_engine(
          "mysql+pymysql://scott:tiger@localhost/test?"
          "plugin=myplugin&my_argument_one=foo&my_argument_two=bar",
          my_argument_three=\'bat\'
        )

    .. versionchanged:: 1.4

        The :class:`_engine.URL` object is now immutable; a
        :class:`_engine.CreateEnginePlugin` that needs to alter the
        :class:`_engine.URL` should implement the newly added
        :meth:`_engine.CreateEnginePlugin.update_url` method, which
        is invoked after the plugin is constructed.

        For migration, construct the plugin in the following way, checking
        for the existence of the :meth:`_engine.CreateEnginePlugin.update_url`
        method to detect which version is running::

            class MyPlugin(CreateEnginePlugin):
                def __init__(self, url, kwargs):
                    if hasattr(CreateEnginePlugin, "update_url"):
                        # detect the 1.4 API
                        self.my_argument_one = url.query[\'my_argument_one\']
                        self.my_argument_two = url.query[\'my_argument_two\']
                    else:
                        # detect the 1.3 and earlier API - mutate the
                        # URL directly
                        self.my_argument_one = url.query.pop(\'my_argument_one\')
                        self.my_argument_two = url.query.pop(\'my_argument_two\')

                    self.my_argument_three = kwargs.pop(\'my_argument_three\', None)

                def update_url(self, url):
                    # this method is only called in the 1.4 version
                    return url.difference_update_query(
                        ["my_argument_one", "my_argument_two"]
                    )

        .. seealso::

            :ref:`change_5526` - overview of the :class:`_engine.URL` change which
            also includes notes regarding :class:`_engine.CreateEnginePlugin`.


    When the engine creation process completes and produces the
    :class:`_engine.Engine` object, it is again passed to the plugin via the
    :meth:`_engine.CreateEnginePlugin.engine_created` hook.  In this hook, additional
    changes can be made to the engine, most typically involving setup of
    events (e.g. those defined in :ref:`core_event_toplevel`).

    '''
    url: Incomplete
    def __init__(self, url: URL, kwargs: Dict[str, Any]) -> None:
        """Construct a new :class:`.CreateEnginePlugin`.

        The plugin object is instantiated individually for each call
        to :func:`_sa.create_engine`.  A single :class:`_engine.
        Engine` will be
        passed to the :meth:`.CreateEnginePlugin.engine_created` method
        corresponding to this URL.

        :param url: the :class:`_engine.URL` object.  The plugin may inspect
         the :class:`_engine.URL` for arguments.  Arguments used by the
         plugin should be removed, by returning an updated :class:`_engine.URL`
         from the :meth:`_engine.CreateEnginePlugin.update_url` method.

         .. versionchanged::  1.4

            The :class:`_engine.URL` object is now immutable, so a
            :class:`_engine.CreateEnginePlugin` that needs to alter the
            :class:`_engine.URL` object should implement the
            :meth:`_engine.CreateEnginePlugin.update_url` method.

        :param kwargs: The keyword arguments passed to
         :func:`_sa.create_engine`.

        """
    def update_url(self, url: URL) -> URL:
        """Update the :class:`_engine.URL`.

        A new :class:`_engine.URL` should be returned.   This method is
        typically used to consume configuration arguments from the
        :class:`_engine.URL` which must be removed, as they will not be
        recognized by the dialect.  The
        :meth:`_engine.URL.difference_update_query` method is available
        to remove these arguments.   See the docstring at
        :class:`_engine.CreateEnginePlugin` for an example.


        .. versionadded:: 1.4

        """
    def handle_dialect_kwargs(self, dialect_cls: Type[Dialect], dialect_args: Dict[str, Any]) -> None:
        """parse and modify dialect kwargs"""
    def handle_pool_kwargs(self, pool_cls: Type[Pool], pool_args: Dict[str, Any]) -> None:
        """parse and modify pool kwargs"""
    def engine_created(self, engine: Engine) -> None:
        """Receive the :class:`_engine.Engine`
        object when it is fully constructed.

        The plugin may make additional changes to the engine, such as
        registering engine or connection pool events.

        """

class ExecutionContext:
    """A messenger object for a Dialect that corresponds to a single
    execution.

    """
    engine: Engine
    connection: Connection
    root_connection: Connection
    dialect: Dialect
    cursor: DBAPICursor
    compiled: Compiled | None
    statement: str
    invoked_statement: Executable | None
    parameters: _AnyMultiExecuteParams
    no_parameters: bool
    isinsert: bool
    isupdate: bool
    execute_style: ExecuteStyle
    executemany: bool
    prefetch_cols: util.generic_fn_descriptor[Sequence[Column[Any]] | None]
    postfetch_cols: util.generic_fn_descriptor[Sequence[Column[Any]] | None]
    def fire_sequence(self, seq: Sequence_SchemaItem, type_: Integer) -> int:
        """given a :class:`.Sequence`, invoke it and return the next int
        value"""
    def create_cursor(self) -> DBAPICursor:
        '''Return a new cursor generated from this ExecutionContext\'s
        connection.

        Some dialects may wish to change the behavior of
        connection.cursor(), such as postgresql which may return a PG
        "server side" cursor.
        '''
    def pre_exec(self) -> None:
        """Called before an execution of a compiled statement.

        If a compiled statement was passed to this ExecutionContext,
        the `statement` and `parameters` datamembers must be
        initialized after this statement is complete.
        """
    def get_out_parameter_values(self, out_param_names: Sequence[str]) -> Sequence[Any]:
        """Return a sequence of OUT parameter values from a cursor.

        For dialects that support OUT parameters, this method will be called
        when there is a :class:`.SQLCompiler` object which has the
        :attr:`.SQLCompiler.has_out_parameters` flag set.  This flag in turn
        will be set to True if the statement itself has :class:`.BindParameter`
        objects that have the ``.isoutparam`` flag set which are consumed by
        the :meth:`.SQLCompiler.visit_bindparam` method.  If the dialect
        compiler produces :class:`.BindParameter` objects with ``.isoutparam``
        set which are not handled by :meth:`.SQLCompiler.visit_bindparam`, it
        should set this flag explicitly.

        The list of names that were rendered for each bound parameter
        is passed to the method.  The method should then return a sequence of
        values corresponding to the list of parameter objects. Unlike in
        previous SQLAlchemy versions, the values can be the **raw values** from
        the DBAPI; the execution context will apply the appropriate type
        handler based on what's present in self.compiled.binds and update the
        values.  The processed dictionary will then be made available via the
        ``.out_parameters`` collection on the result object.  Note that
        SQLAlchemy 1.4 has multiple kinds of result object as part of the 2.0
        transition.

        .. versionadded:: 1.4 - added
           :meth:`.ExecutionContext.get_out_parameter_values`, which is invoked
           automatically by the :class:`.DefaultExecutionContext` when there
           are :class:`.BindParameter` objects with the ``.isoutparam`` flag
           set.  This replaces the practice of setting out parameters within
           the now-removed ``get_result_proxy()`` method.

        """
    def post_exec(self) -> None:
        """Called after the execution of a compiled statement.

        If a compiled statement was passed to this ExecutionContext,
        the `last_insert_ids`, `last_inserted_params`, etc.
        datamembers should be available after this method completes.
        """
    def handle_dbapi_exception(self, e: BaseException) -> None:
        """Receive a DBAPI exception which occurred upon execute, result
        fetch, etc."""
    def lastrow_has_defaults(self) -> bool:
        """Return True if the last INSERT or UPDATE row contained
        inlined or database-side defaults.
        """
    def get_rowcount(self) -> int | None:
        """Return the DBAPI ``cursor.rowcount`` value, or in some
        cases an interpreted value.

        See :attr:`_engine.CursorResult.rowcount` for details on this.

        """
    def fetchall_for_returning(self, cursor: DBAPICursor) -> Sequence[Any]:
        '''For a RETURNING result, deliver cursor.fetchall() from the
        DBAPI cursor.

        This is a dialect-specific hook for dialects that have special
        considerations when calling upon the rows delivered for a
        "RETURNING" statement.   Default implementation is
        ``cursor.fetchall()``.

        This hook is currently used only by the :term:`insertmanyvalues`
        feature.   Dialects that don\'t set ``use_insertmanyvalues=True``
        don\'t need to consider this hook.

        .. versionadded:: 2.0.10

        '''

class ConnectionEventsTarget(EventTarget):
    """An object which can accept events from :class:`.ConnectionEvents`.

    Includes :class:`_engine.Connection` and :class:`_engine.Engine`.

    .. versionadded:: 2.0

    """
    dispatch: dispatcher[ConnectionEventsTarget]
Connectable = ConnectionEventsTarget

class ExceptionContext:
    """Encapsulate information about an error condition in progress.

    This object exists solely to be passed to the
    :meth:`_events.DialectEvents.handle_error` event,
    supporting an interface that
    can be extended without backwards-incompatibility.


    """
    dialect: Dialect
    connection: Connection | None
    engine: Engine | None
    cursor: DBAPICursor | None
    statement: str | None
    parameters: _DBAPIAnyExecuteParams | None
    original_exception: BaseException
    sqlalchemy_exception: StatementError | None
    chained_exception: BaseException | None
    execution_context: ExecutionContext | None
    is_disconnect: bool
    invalidate_pool_on_disconnect: bool
    is_pre_ping: bool

class AdaptedConnection:
    """Interface of an adapted connection object to support the DBAPI protocol.

    Used by asyncio dialects to provide a sync-style pep-249 facade on top
    of the asyncio connection/cursor API provided by the driver.

    .. versionadded:: 1.4.24

    """
    @property
    def driver_connection(self) -> Any:
        """The connection object as returned by the driver after a connect."""
    def run_async(self, fn: Callable[[Any], Awaitable[_T]]) -> _T:
        '''Run the awaitable returned by the given function, which is passed
        the raw asyncio driver connection.

        This is used to invoke awaitable-only methods on the driver connection
        within the context of a "synchronous" method, like a connection
        pool event handler.

        E.g.::

            engine = create_async_engine(...)

            @event.listens_for(engine.sync_engine, "connect")
            def register_custom_types(dbapi_connection, ...):
                dbapi_connection.run_async(
                    lambda connection: connection.set_type_codec(
                        \'MyCustomType\', encoder, decoder, ...
                    )
                )

        .. versionadded:: 1.4.30

        .. seealso::

            :ref:`asyncio_events_run_async`

        '''
