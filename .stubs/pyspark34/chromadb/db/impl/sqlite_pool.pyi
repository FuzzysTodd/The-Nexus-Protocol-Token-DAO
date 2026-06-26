import abc
import sqlite3
from abc import ABC, abstractmethod
from typing import Any

class Connection:
    """A threadpool connection that returns itself to the pool on close()"""
    def __init__(self, pool: Pool, db_file: str, is_uri: bool, *args: Any, **kwargs: Any) -> None: ...
    def execute(self, sql: str, parameters=...) -> sqlite3.Cursor: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def cursor(self) -> sqlite3.Cursor: ...
    def close_actual(self) -> None:
        """Actually closes the connection to the db"""

class Pool(ABC, metaclass=abc.ABCMeta):
    """Abstract base class for a pool of connections to a sqlite database."""
    @abstractmethod
    def __init__(self, db_file: str, is_uri: bool): ...
    @abstractmethod
    def connect(self, *args: Any, **kwargs: Any) -> Connection:
        """Return a connection from the pool."""
    @abstractmethod
    def close(self) -> None:
        """Close all connections in the pool."""
    @abstractmethod
    def return_to_pool(self, conn: Connection) -> None:
        """Return a connection to the pool."""

class LockPool(Pool):
    """A pool that has a single connection per thread but uses a lock to ensure that only one thread can use it at a time.
    This is used because sqlite does not support multithreaded access with connection timeouts when using the
    shared cache mode. We use the shared cache mode to allow multiple threads to share a database.
    """
    def __init__(self, db_file: str, is_uri: bool = False) -> None: ...
    def connect(self, *args: Any, **kwargs: Any) -> Connection: ...
    def return_to_pool(self, conn: Connection) -> None: ...
    def close(self) -> None: ...

class PerThreadPool(Pool):
    """Maintains a connection per thread. For now this does not maintain a cap on the number of connections, but it could be
    extended to do so and block on connect() if the cap is reached.
    """
    def __init__(self, db_file: str, is_uri: bool = False) -> None: ...
    def connect(self, *args: Any, **kwargs: Any) -> Connection: ...
    def close(self) -> None: ...
    def return_to_pool(self, conn: Connection) -> None: ...
