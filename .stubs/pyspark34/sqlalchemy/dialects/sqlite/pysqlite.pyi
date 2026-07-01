from ... import exc as exc, pool as pool, util as util
from .base import DATE as DATE, DATETIME as DATETIME, SQLiteDialect as SQLiteDialect
from _typeshed import Incomplete

class _SQLite_pysqliteTimeStamp(DATETIME):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _SQLite_pysqliteDate(DATE):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class SQLiteDialect_pysqlite(SQLiteDialect):
    default_paramstyle: str
    supports_statement_cache: bool
    returns_native_bytes: bool
    colspecs: Incomplete
    description_encoding: Incomplete
    driver: str
    @classmethod
    def import_dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def set_isolation_level(self, dbapi_connection, level): ...
    def on_connect(self): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...
dialect = SQLiteDialect_pysqlite

class _SQLiteDialect_pysqlite_numeric(SQLiteDialect_pysqlite):
    """numeric dialect for testing only

    internal use only.  This dialect is **NOT** supported by SQLAlchemy
    and may change at any time.

    """
    supports_statement_cache: bool
    default_paramstyle: str
    driver: str
    def __init__(self, *arg, **kw) -> None: ...
    def create_connect_args(self, url): ...

class _SQLiteDialect_pysqlite_dollar(_SQLiteDialect_pysqlite_numeric):
    """numeric dialect that uses $ for testing only

    internal use only.  This dialect is **NOT** supported by SQLAlchemy
    and may change at any time.

    """
    supports_statement_cache: bool
    default_paramstyle: str
    driver: str
    def __init__(self, *arg, **kw) -> None: ...
