from ... import types as sqltypes, util as util
from ...engine import processors as processors
from .base import MSDialect as MSDialect, MSIdentifierPreparer as MSIdentifierPreparer
from _typeshed import Incomplete

class _MSNumeric_pymssql(sqltypes.Numeric):
    def result_processor(self, dialect, type_): ...

class MSIdentifierPreparer_pymssql(MSIdentifierPreparer):
    def __init__(self, dialect) -> None: ...

class MSDialect_pymssql(MSDialect):
    supports_statement_cache: bool
    supports_native_decimal: bool
    supports_native_uuid: bool
    driver: str
    preparer = MSIdentifierPreparer_pymssql
    colspecs: Incomplete
    @classmethod
    def import_dbapi(cls): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...
    def get_isolation_level_values(self, dbapi_connection): ...
    def set_isolation_level(self, dbapi_connection, level) -> None: ...
dialect = MSDialect_pymssql
