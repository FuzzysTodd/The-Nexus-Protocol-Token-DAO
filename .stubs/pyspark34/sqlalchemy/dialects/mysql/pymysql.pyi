from ...util import langhelpers as langhelpers
from .mysqldb import MySQLDialect_mysqldb as MySQLDialect_mysqldb
from _typeshed import Incomplete

class MySQLDialect_pymysql(MySQLDialect_mysqldb):
    driver: str
    supports_statement_cache: bool
    description_encoding: Incomplete
    def supports_server_side_cursors(self): ...
    @classmethod
    def import_dbapi(cls): ...
    def create_connect_args(self, url, _translate_args: Incomplete | None = None): ...
    def is_disconnect(self, e, connection, cursor): ...
dialect = MySQLDialect_pymysql
