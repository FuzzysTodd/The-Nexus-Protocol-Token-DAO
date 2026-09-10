import abc
import sqlite3
from _typeshed import Incomplete
from abc import abstractmethod
from typing import Iterable

class MetadataStore(metaclass=abc.ABCMeta):
    """Generic interface for metadata storage."""
    @abstractmethod
    def getmtime(self, name: str) -> float:
        """Read the mtime of a metadata entry..

        Raises FileNotFound if the entry does not exist.
        """
    @abstractmethod
    def read(self, name: str) -> str:
        """Read the contents of a metadata entry.

        Raises FileNotFound if the entry does not exist.
        """
    @abstractmethod
    def write(self, name: str, data: str, mtime: float | None = None) -> bool:
        """Write a metadata entry.

        If mtime is specified, set it as the mtime of the entry. Otherwise,
        the current time is used.

        Returns True if the entry is successfully written, False otherwise.
        """
    @abstractmethod
    def remove(self, name: str) -> None:
        """Delete a metadata entry"""
    @abstractmethod
    def commit(self) -> None:
        """If the backing store requires a commit, do it.

        But N.B. that this is not *guaranteed* to do anything, and
        there is no guarantee that changes are not made until it is
        called.
        """
    @abstractmethod
    def list_all(self) -> Iterable[str]: ...

def random_string() -> str: ...

class FilesystemMetadataStore(MetadataStore):
    cache_dir_prefix: Incomplete
    def __init__(self, cache_dir_prefix: str) -> None: ...
    def getmtime(self, name: str) -> float: ...
    def read(self, name: str) -> str: ...
    def write(self, name: str, data: str, mtime: float | None = None) -> bool: ...
    def remove(self, name: str) -> None: ...
    def commit(self) -> None: ...
    def list_all(self) -> Iterable[str]: ...

SCHEMA: str
MIGRATIONS: list[str]

def connect_db(db_file: str) -> sqlite3.Connection: ...

class SqliteMetadataStore(MetadataStore):
    db: Incomplete
    def __init__(self, cache_dir_prefix: str) -> None: ...
    def getmtime(self, name: str) -> float: ...
    def read(self, name: str) -> str: ...
    def write(self, name: str, data: str, mtime: float | None = None) -> bool: ...
    def remove(self, name: str) -> None: ...
    def commit(self) -> None: ...
    def list_all(self) -> Iterable[str]: ...
