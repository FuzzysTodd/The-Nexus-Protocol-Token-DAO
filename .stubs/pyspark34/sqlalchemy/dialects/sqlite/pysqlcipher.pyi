from ... import pool as pool
from .pysqlite import SQLiteDialect_pysqlite as SQLiteDialect_pysqlite
from _typeshed import Incomplete

class SQLiteDialect_pysqlcipher(SQLiteDialect_pysqlite):
    driver: str
    supports_statement_cache: bool
    pragmas: Incomplete
    @classmethod
    def import_dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def on_connect_url(self, url): ...
    def create_connect_args(self, url): ...
dialect = SQLiteDialect_pysqlcipher
