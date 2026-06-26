import optuna
from _typeshed import Incomplete
from types import TracebackType
from typing import Type

STORAGE_MODES: Incomplete
SQLITE3_TIMEOUT: int

class StorageSupplier:
    storage_specifier: Incomplete
    tempfile: Incomplete
    def __init__(self, storage_specifier: str) -> None: ...
    def __enter__(self) -> optuna.storages.BaseStorage: ...
    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> None: ...
