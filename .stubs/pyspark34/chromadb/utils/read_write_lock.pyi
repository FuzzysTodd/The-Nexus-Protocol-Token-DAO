from _typeshed import Incomplete
from types import TracebackType
from typing import Type

class ReadWriteLock:
    '''A lock object that allows many simultaneous "read locks", but
    only one "write lock." '''
    def __init__(self) -> None: ...
    def acquire_read(self) -> None:
        """Acquire a read lock. Blocks only if a thread has
        acquired the write lock."""
    def release_read(self) -> None:
        """Release a read lock."""
    def acquire_write(self) -> None:
        """Acquire a write lock. Blocks until there are no
        acquired read or write locks."""
    def release_write(self) -> None:
        """Release a write lock."""

class ReadRWLock:
    rwLock: Incomplete
    def __init__(self, rwLock: ReadWriteLock) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

class WriteRWLock:
    rwLock: Incomplete
    def __init__(self, rwLock: ReadWriteLock) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
