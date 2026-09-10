from ... import exc as exc, util as util
from ...connectors.pyodbc import PyODBCConnector as PyODBCConnector
from ...sql.sqltypes import Time as Time
from .base import MySQLDialect as MySQLDialect, MySQLExecutionContext as MySQLExecutionContext
from .types import TIME as TIME
from _typeshed import Incomplete

class _pyodbcTIME(TIME):
    def result_processor(self, dialect, coltype): ...

class MySQLExecutionContext_pyodbc(MySQLExecutionContext):
    def get_lastrowid(self): ...

class MySQLDialect_pyodbc(PyODBCConnector, MySQLDialect):
    supports_statement_cache: bool
    colspecs: Incomplete
    supports_unicode_statements: bool
    execution_ctx_cls = MySQLExecutionContext_pyodbc
    pyodbc_driver_name: str
    def on_connect(self): ...
dialect = MySQLDialect_pyodbc
