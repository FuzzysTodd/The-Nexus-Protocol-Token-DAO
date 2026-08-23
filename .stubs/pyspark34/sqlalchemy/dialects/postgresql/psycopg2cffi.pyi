from ... import util as util
from .psycopg2 import PGDialect_psycopg2 as PGDialect_psycopg2
from _typeshed import Incomplete

class PGDialect_psycopg2cffi(PGDialect_psycopg2):
    driver: str
    supports_unicode_statements: bool
    supports_statement_cache: bool
    FEATURE_VERSION_MAP: Incomplete
    @classmethod
    def import_dbapi(cls): ...
dialect = PGDialect_psycopg2cffi
