from ... import util as util
from .base import BIT as BIT, MySQLCompiler as MySQLCompiler, MySQLDialect as MySQLDialect, MySQLIdentifierPreparer as MySQLIdentifierPreparer
from _typeshed import Incomplete

class MySQLCompiler_mysqlconnector(MySQLCompiler):
    def visit_mod_binary(self, binary, operator, **kw): ...

class MySQLIdentifierPreparer_mysqlconnector(MySQLIdentifierPreparer): ...

class _myconnpyBIT(BIT):
    def result_processor(self, dialect, coltype) -> None:
        """MySQL-connector already converts mysql bits, so."""

class MySQLDialect_mysqlconnector(MySQLDialect):
    driver: str
    supports_statement_cache: bool
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_native_decimal: bool
    default_paramstyle: str
    statement_compiler = MySQLCompiler_mysqlconnector
    preparer = MySQLIdentifierPreparer_mysqlconnector
    colspecs: Incomplete
    @classmethod
    def import_dbapi(cls): ...
    def do_ping(self, dbapi_connection): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...
dialect = MySQLDialect_mysqlconnector
