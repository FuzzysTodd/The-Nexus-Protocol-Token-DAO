from ... import exc as exc
from .cx_oracle import OracleDialect_cx_oracle as _OracleDialect_cx_oracle
from _typeshed import Incomplete

class OracleDialect_oracledb(_OracleDialect_cx_oracle):
    supports_statement_cache: bool
    driver: str
    def __init__(self, auto_convert_lobs: bool = True, coerce_to_decimal: bool = True, arraysize: int = 50, encoding_errors: Incomplete | None = None, thick_mode: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def import_dbapi(cls): ...
    @classmethod
    def is_thin_mode(cls, connection): ...
dialect = OracleDialect_oracledb
