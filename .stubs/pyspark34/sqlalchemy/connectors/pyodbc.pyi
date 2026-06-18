from . import Connector as Connector
from .. import ExecutionContext as ExecutionContext, pool as pool, util as util
from ..engine import ConnectArgsType as ConnectArgsType, Connection as Connection, URL as URL, interfaces as interfaces
from ..engine.interfaces import IsolationLevel as IsolationLevel
from ..sql.type_api import TypeEngine as TypeEngine
from _typeshed import Incomplete
from types import ModuleType
from typing import Any, List, Tuple

class PyODBCConnector(Connector):
    driver: str
    supports_sane_rowcount_returning: bool
    supports_sane_multi_rowcount: bool
    supports_native_decimal: bool
    default_paramstyle: str
    fast_executemany: bool
    pyodbc_driver_name: str | None
    dbapi: ModuleType
    bind_typing: Incomplete
    def __init__(self, use_setinputsizes: bool = False, **kw: Any) -> None: ...
    @classmethod
    def import_dbapi(cls) -> ModuleType: ...
    def create_connect_args(self, url: URL) -> ConnectArgsType: ...
    def is_disconnect(self, e: Exception, connection: pool.PoolProxiedConnection | interfaces.DBAPIConnection | None, cursor: interfaces.DBAPICursor | None) -> bool: ...
    def do_set_input_sizes(self, cursor: interfaces.DBAPICursor, list_of_tuples: List[Tuple[str, Any, TypeEngine[Any]]], context: ExecutionContext) -> None: ...
    def get_isolation_level_values(self, dbapi_connection: interfaces.DBAPIConnection) -> List[IsolationLevel]: ...
    def set_isolation_level(self, dbapi_connection: interfaces.DBAPIConnection, level: IsolationLevel) -> None: ...
