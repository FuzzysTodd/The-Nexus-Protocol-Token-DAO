import abc
import contextlib
import os
from _typeshed import Incomplete
from abc import ABC
from dataclasses import dataclass
from threading import local
from types import TracebackType
from typing_extensions import Self

__all__ = ['BaseFileLock', 'AcquireReturnProxy']

class AcquireReturnProxy:
    """A context aware object that will release the lock file when exiting."""
    lock: Incomplete
    def __init__(self, lock: BaseFileLock) -> None: ...
    def __enter__(self) -> BaseFileLock: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

@dataclass
class FileLockContext:
    """A dataclass which holds the context for a ``BaseFileLock`` object."""
    lock_file: str
    timeout: float
    mode: int
    lock_file_fd: int | None = ...
    lock_counter: int = ...
    def __init__(self, lock_file, timeout, mode, lock_file_fd, lock_counter) -> None: ...

class ThreadLocalFileContext(FileLockContext, local):
    """A thread local version of the ``FileLockContext`` class."""

class BaseFileLock(ABC, contextlib.ContextDecorator, metaclass=abc.ABCMeta):
    """Abstract base class for a file lock object."""
    def __init__(self, lock_file: str | os.PathLike[str], timeout: float = -1, mode: int = 420, thread_local: bool = True) -> None:
        """
        Create a new lock object.

        :param lock_file: path to the file
        :param timeout: default timeout when acquiring the lock, in seconds. It will be used as fallback value in
        the acquire method, if no timeout value (``None``) is given. If you want to disable the timeout, set it
        to a negative value. A timeout of 0 means, that there is exactly one attempt to acquire the file lock.
        :param mode: file permissions for the lockfile.
        :param thread_local: Whether this object's internal context should be thread local or not.
        If this is set to ``False`` then the lock will be reentrant across threads.
        """
    def is_thread_local(self) -> bool:
        """:return: a flag indicating if this lock is thread local or not"""
    @property
    def lock_file(self) -> str:
        """:return: path to the lock file"""
    @property
    def timeout(self) -> float:
        """
        :return: the default timeout value, in seconds

        .. versionadded:: 2.0.0
        """
    @timeout.setter
    def timeout(self, value: float | str) -> None:
        """
        Change the default timeout value.

        :param value: the new value, in seconds
        """
    @property
    def is_locked(self) -> bool:
        """

        :return: A boolean indicating if the lock file is holding the lock currently.

        .. versionchanged:: 2.0.0

            This was previously a method and is now a property.
        """
    @property
    def lock_counter(self) -> int:
        """:return: The number of times this lock has been acquired (but not yet released)."""
    def acquire(self, timeout: float | None = None, poll_interval: float = 0.05, *, poll_intervall: float | None = None, blocking: bool = True) -> AcquireReturnProxy:
        """
        Try to acquire the file lock.

        :param timeout: maximum wait time for acquiring the lock, ``None`` means use the default :attr:`~timeout` is and
         if ``timeout < 0``, there is no timeout and this method will block until the lock could be acquired
        :param poll_interval: interval of trying to acquire the lock file
        :param poll_intervall: deprecated, kept for backwards compatibility, use ``poll_interval`` instead
        :param blocking: defaults to True. If False, function will return immediately if it cannot obtain a lock on the
         first attempt. Otherwise, this method will block until the timeout expires or the lock is acquired.
        :raises Timeout: if fails to acquire lock within the timeout period
        :return: a context object that will unlock the file when the context is exited

        .. code-block:: python

            # You can use this method in the context manager (recommended)
            with lock.acquire():
                pass

            # Or use an equivalent try-finally construct:
            lock.acquire()
            try:
                pass
            finally:
                lock.release()

        .. versionchanged:: 2.0.0

            This method returns now a *proxy* object instead of *self*,
            so that it can be used in a with statement without side effects.

        """
    def release(self, force: bool = False) -> None:
        """
        Releases the file lock. Please note, that the lock is only completely released, if the lock counter is 0. Also
        note, that the lock file itself is not automatically deleted.

        :param force: If true, the lock counter is ignored and the lock is released in every case/
        """
    def __enter__(self) -> Self:
        """
        Acquire the lock.

        :return: the lock object
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        """
        Release the lock.

        :param exc_type: the exception type if raised
        :param exc_value: the exception value if raised
        :param traceback: the exception traceback if raised
        """
    def __del__(self) -> None:
        """Called when the lock object is deleted."""
