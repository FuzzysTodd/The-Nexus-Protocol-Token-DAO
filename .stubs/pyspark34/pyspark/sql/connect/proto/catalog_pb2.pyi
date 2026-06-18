import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pyspark.sql.connect.proto.types_pb2
import typing
import typing as typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Catalog(google.protobuf.message.Message):
    """Catalog messages are marked as unstable."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CURRENT_DATABASE_FIELD_NUMBER: builtins.int
    SET_CURRENT_DATABASE_FIELD_NUMBER: builtins.int
    LIST_DATABASES_FIELD_NUMBER: builtins.int
    LIST_TABLES_FIELD_NUMBER: builtins.int
    LIST_FUNCTIONS_FIELD_NUMBER: builtins.int
    LIST_COLUMNS_FIELD_NUMBER: builtins.int
    GET_DATABASE_FIELD_NUMBER: builtins.int
    GET_TABLE_FIELD_NUMBER: builtins.int
    GET_FUNCTION_FIELD_NUMBER: builtins.int
    DATABASE_EXISTS_FIELD_NUMBER: builtins.int
    TABLE_EXISTS_FIELD_NUMBER: builtins.int
    FUNCTION_EXISTS_FIELD_NUMBER: builtins.int
    CREATE_EXTERNAL_TABLE_FIELD_NUMBER: builtins.int
    CREATE_TABLE_FIELD_NUMBER: builtins.int
    DROP_TEMP_VIEW_FIELD_NUMBER: builtins.int
    DROP_GLOBAL_TEMP_VIEW_FIELD_NUMBER: builtins.int
    RECOVER_PARTITIONS_FIELD_NUMBER: builtins.int
    IS_CACHED_FIELD_NUMBER: builtins.int
    CACHE_TABLE_FIELD_NUMBER: builtins.int
    UNCACHE_TABLE_FIELD_NUMBER: builtins.int
    CLEAR_CACHE_FIELD_NUMBER: builtins.int
    REFRESH_TABLE_FIELD_NUMBER: builtins.int
    REFRESH_BY_PATH_FIELD_NUMBER: builtins.int
    CURRENT_CATALOG_FIELD_NUMBER: builtins.int
    SET_CURRENT_CATALOG_FIELD_NUMBER: builtins.int
    LIST_CATALOGS_FIELD_NUMBER: builtins.int
    @property
    def current_database(self) -> global___CurrentDatabase: ...
    @property
    def set_current_database(self) -> global___SetCurrentDatabase: ...
    @property
    def list_databases(self) -> global___ListDatabases: ...
    @property
    def list_tables(self) -> global___ListTables: ...
    @property
    def list_functions(self) -> global___ListFunctions: ...
    @property
    def list_columns(self) -> global___ListColumns: ...
    @property
    def get_database(self) -> global___GetDatabase: ...
    @property
    def get_table(self) -> global___GetTable: ...
    @property
    def get_function(self) -> global___GetFunction: ...
    @property
    def database_exists(self) -> global___DatabaseExists: ...
    @property
    def table_exists(self) -> global___TableExists: ...
    @property
    def function_exists(self) -> global___FunctionExists: ...
    @property
    def create_external_table(self) -> global___CreateExternalTable: ...
    @property
    def create_table(self) -> global___CreateTable: ...
    @property
    def drop_temp_view(self) -> global___DropTempView: ...
    @property
    def drop_global_temp_view(self) -> global___DropGlobalTempView: ...
    @property
    def recover_partitions(self) -> global___RecoverPartitions: ...
    @property
    def is_cached(self) -> global___IsCached: ...
    @property
    def cache_table(self) -> global___CacheTable: ...
    @property
    def uncache_table(self) -> global___UncacheTable: ...
    @property
    def clear_cache(self) -> global___ClearCache: ...
    @property
    def refresh_table(self) -> global___RefreshTable: ...
    @property
    def refresh_by_path(self) -> global___RefreshByPath: ...
    @property
    def current_catalog(self) -> global___CurrentCatalog: ...
    @property
    def set_current_catalog(self) -> global___SetCurrentCatalog: ...
    @property
    def list_catalogs(self) -> global___ListCatalogs: ...
    def __init__(self, *, current_database: global___CurrentDatabase | None = ..., set_current_database: global___SetCurrentDatabase | None = ..., list_databases: global___ListDatabases | None = ..., list_tables: global___ListTables | None = ..., list_functions: global___ListFunctions | None = ..., list_columns: global___ListColumns | None = ..., get_database: global___GetDatabase | None = ..., get_table: global___GetTable | None = ..., get_function: global___GetFunction | None = ..., database_exists: global___DatabaseExists | None = ..., table_exists: global___TableExists | None = ..., function_exists: global___FunctionExists | None = ..., create_external_table: global___CreateExternalTable | None = ..., create_table: global___CreateTable | None = ..., drop_temp_view: global___DropTempView | None = ..., drop_global_temp_view: global___DropGlobalTempView | None = ..., recover_partitions: global___RecoverPartitions | None = ..., is_cached: global___IsCached | None = ..., cache_table: global___CacheTable | None = ..., uncache_table: global___UncacheTable | None = ..., clear_cache: global___ClearCache | None = ..., refresh_table: global___RefreshTable | None = ..., refresh_by_path: global___RefreshByPath | None = ..., current_catalog: global___CurrentCatalog | None = ..., set_current_catalog: global___SetCurrentCatalog | None = ..., list_catalogs: global___ListCatalogs | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['cache_table', 'cache_table', 'cat_type', 'cat_type', 'clear_cache', 'clear_cache', 'create_external_table', 'create_external_table', 'create_table', 'create_table', 'current_catalog', 'current_catalog', 'current_database', 'current_database', 'database_exists', 'database_exists', 'drop_global_temp_view', 'drop_global_temp_view', 'drop_temp_view', 'drop_temp_view', 'function_exists', 'function_exists', 'get_database', 'get_database', 'get_function', 'get_function', 'get_table', 'get_table', 'is_cached', 'is_cached', 'list_catalogs', 'list_catalogs', 'list_columns', 'list_columns', 'list_databases', 'list_databases', 'list_functions', 'list_functions', 'list_tables', 'list_tables', 'recover_partitions', 'recover_partitions', 'refresh_by_path', 'refresh_by_path', 'refresh_table', 'refresh_table', 'set_current_catalog', 'set_current_catalog', 'set_current_database', 'set_current_database', 'table_exists', 'table_exists', 'uncache_table', 'uncache_table']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['cache_table', 'cache_table', 'cat_type', 'cat_type', 'clear_cache', 'clear_cache', 'create_external_table', 'create_external_table', 'create_table', 'create_table', 'current_catalog', 'current_catalog', 'current_database', 'current_database', 'database_exists', 'database_exists', 'drop_global_temp_view', 'drop_global_temp_view', 'drop_temp_view', 'drop_temp_view', 'function_exists', 'function_exists', 'get_database', 'get_database', 'get_function', 'get_function', 'get_table', 'get_table', 'is_cached', 'is_cached', 'list_catalogs', 'list_catalogs', 'list_columns', 'list_columns', 'list_databases', 'list_databases', 'list_functions', 'list_functions', 'list_tables', 'list_tables', 'recover_partitions', 'recover_partitions', 'refresh_by_path', 'refresh_by_path', 'refresh_table', 'refresh_table', 'set_current_catalog', 'set_current_catalog', 'set_current_database', 'set_current_database', 'table_exists', 'table_exists', 'uncache_table', 'uncache_table']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['cat_type', 'cat_type']) -> typing_extensions.Literal['current_database', 'set_current_database', 'list_databases', 'list_tables', 'list_functions', 'list_columns', 'get_database', 'get_table', 'get_function', 'database_exists', 'table_exists', 'function_exists', 'create_external_table', 'create_table', 'drop_temp_view', 'drop_global_temp_view', 'recover_partitions', 'is_cached', 'cache_table', 'uncache_table', 'clear_cache', 'refresh_table', 'refresh_by_path', 'current_catalog', 'set_current_catalog', 'list_catalogs'] | None: ...
global___Catalog = Catalog

class CurrentDatabase(google.protobuf.message.Message):
    """See `spark.catalog.currentDatabase`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...
global___CurrentDatabase = CurrentDatabase

class SetCurrentDatabase(google.protobuf.message.Message):
    """See `spark.catalog.setCurrentDatabase`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    def __init__(self, *, db_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['db_name', 'db_name']) -> None: ...
global___SetCurrentDatabase = SetCurrentDatabase

class ListDatabases(google.protobuf.message.Message):
    """See `spark.catalog.listDatabases`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...
global___ListDatabases = ListDatabases

class ListTables(google.protobuf.message.Message):
    """See `spark.catalog.listTables`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    def __init__(self, *, db_name: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_db_name', '_db_name']) -> typing_extensions.Literal['db_name'] | None: ...
global___ListTables = ListTables

class ListFunctions(google.protobuf.message.Message):
    """See `spark.catalog.listFunctions`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    def __init__(self, *, db_name: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_db_name', '_db_name']) -> typing_extensions.Literal['db_name'] | None: ...
global___ListFunctions = ListFunctions

class ListColumns(google.protobuf.message.Message):
    """See `spark.catalog.listColumns`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    db_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ..., db_name: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name', 'table_name', 'table_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_db_name', '_db_name']) -> typing_extensions.Literal['db_name'] | None: ...
global___ListColumns = ListColumns

class GetDatabase(google.protobuf.message.Message):
    """See `spark.catalog.getDatabase`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    def __init__(self, *, db_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['db_name', 'db_name']) -> None: ...
global___GetDatabase = GetDatabase

class GetTable(google.protobuf.message.Message):
    """See `spark.catalog.getTable`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    db_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ..., db_name: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name', 'table_name', 'table_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_db_name', '_db_name']) -> typing_extensions.Literal['db_name'] | None: ...
global___GetTable = GetTable

class GetFunction(google.protobuf.message.Message):
    """See `spark.catalog.getFunction`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FUNCTION_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    function_name: builtins.str
    db_name: builtins.str
    def __init__(self, *, function_name: builtins.str = ..., db_name: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name', 'function_name', 'function_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_db_name', '_db_name']) -> typing_extensions.Literal['db_name'] | None: ...
global___GetFunction = GetFunction

class DatabaseExists(google.protobuf.message.Message):
    """See `spark.catalog.databaseExists`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    def __init__(self, *, db_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['db_name', 'db_name']) -> None: ...
global___DatabaseExists = DatabaseExists

class TableExists(google.protobuf.message.Message):
    """See `spark.catalog.tableExists`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    db_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ..., db_name: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name', 'table_name', 'table_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_db_name', '_db_name']) -> typing_extensions.Literal['db_name'] | None: ...
global___TableExists = TableExists

class FunctionExists(google.protobuf.message.Message):
    """See `spark.catalog.functionExists`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FUNCTION_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    function_name: builtins.str
    db_name: builtins.str
    def __init__(self, *, function_name: builtins.str = ..., db_name: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_db_name', '_db_name', 'db_name', 'db_name', 'function_name', 'function_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_db_name', '_db_name']) -> typing_extensions.Literal['db_name'] | None: ...
global___FunctionExists = FunctionExists

class CreateExternalTable(google.protobuf.message.Message):
    """See `spark.catalog.createExternalTable`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(self, *, key: builtins.str = ..., value: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
    TABLE_NAME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    path: builtins.str
    source: builtins.str
    @property
    def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Optional)"""
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Options could be empty for valid data source format.
        The map key is case insensitive.
        """
    def __init__(self, *, table_name: builtins.str = ..., path: builtins.str | None = ..., source: builtins.str | None = ..., schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_path', '_path', '_schema', '_schema', '_source', '_source', 'path', 'path', 'schema', 'schema', 'source', 'source']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_path', '_path', '_schema', '_schema', '_source', '_source', 'options', 'options', 'path', 'path', 'schema', 'schema', 'source', 'source', 'table_name', 'table_name']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_path', '_path']) -> typing_extensions.Literal['path'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_schema', '_schema']) -> typing_extensions.Literal['schema'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_source', '_source']) -> typing_extensions.Literal['source'] | None: ...
global___CreateExternalTable = CreateExternalTable

class CreateTable(google.protobuf.message.Message):
    """See `spark.catalog.createTable`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(self, *, key: builtins.str = ..., value: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
    TABLE_NAME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    path: builtins.str
    source: builtins.str
    description: builtins.str
    @property
    def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Optional)"""
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Options could be empty for valid data source format.
        The map key is case insensitive.
        """
    def __init__(self, *, table_name: builtins.str = ..., path: builtins.str | None = ..., source: builtins.str | None = ..., description: builtins.str | None = ..., schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_description', '_description', '_path', '_path', '_schema', '_schema', '_source', '_source', 'description', 'description', 'path', 'path', 'schema', 'schema', 'source', 'source']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_description', '_description', '_path', '_path', '_schema', '_schema', '_source', '_source', 'description', 'description', 'options', 'options', 'path', 'path', 'schema', 'schema', 'source', 'source', 'table_name', 'table_name']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_description', '_description']) -> typing_extensions.Literal['description'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_path', '_path']) -> typing_extensions.Literal['path'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_schema', '_schema']) -> typing_extensions.Literal['schema'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_source', '_source']) -> typing_extensions.Literal['source'] | None: ...
global___CreateTable = CreateTable

class DropTempView(google.protobuf.message.Message):
    """See `spark.catalog.dropTempView`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VIEW_NAME_FIELD_NUMBER: builtins.int
    view_name: builtins.str
    def __init__(self, *, view_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['view_name', 'view_name']) -> None: ...
global___DropTempView = DropTempView

class DropGlobalTempView(google.protobuf.message.Message):
    """See `spark.catalog.dropGlobalTempView`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VIEW_NAME_FIELD_NUMBER: builtins.int
    view_name: builtins.str
    def __init__(self, *, view_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['view_name', 'view_name']) -> None: ...
global___DropGlobalTempView = DropGlobalTempView

class RecoverPartitions(google.protobuf.message.Message):
    """See `spark.catalog.recoverPartitions`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['table_name', 'table_name']) -> None: ...
global___RecoverPartitions = RecoverPartitions

class IsCached(google.protobuf.message.Message):
    """See `spark.catalog.isCached`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['table_name', 'table_name']) -> None: ...
global___IsCached = IsCached

class CacheTable(google.protobuf.message.Message):
    """See `spark.catalog.cacheTable`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['table_name', 'table_name']) -> None: ...
global___CacheTable = CacheTable

class UncacheTable(google.protobuf.message.Message):
    """See `spark.catalog.uncacheTable`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['table_name', 'table_name']) -> None: ...
global___UncacheTable = UncacheTable

class ClearCache(google.protobuf.message.Message):
    """See `spark.catalog.clearCache`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...
global___ClearCache = ClearCache

class RefreshTable(google.protobuf.message.Message):
    """See `spark.catalog.refreshTable`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    def __init__(self, *, table_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['table_name', 'table_name']) -> None: ...
global___RefreshTable = RefreshTable

class RefreshByPath(google.protobuf.message.Message):
    """See `spark.catalog.refreshByPath`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: builtins.int
    path: builtins.str
    def __init__(self, *, path: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['path', 'path']) -> None: ...
global___RefreshByPath = RefreshByPath

class CurrentCatalog(google.protobuf.message.Message):
    """See `spark.catalog.currentCatalog`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...
global___CurrentCatalog = CurrentCatalog

class SetCurrentCatalog(google.protobuf.message.Message):
    """See `spark.catalog.setCurrentCatalog`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CATALOG_NAME_FIELD_NUMBER: builtins.int
    catalog_name: builtins.str
    def __init__(self, *, catalog_name: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['catalog_name', 'catalog_name']) -> None: ...
global___SetCurrentCatalog = SetCurrentCatalog

class ListCatalogs(google.protobuf.message.Message):
    """See `spark.catalog.listCatalogs`"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...
global___ListCatalogs = ListCatalogs
