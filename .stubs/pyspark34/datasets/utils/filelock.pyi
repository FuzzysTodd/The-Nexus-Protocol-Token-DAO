from _typeshed import Incomplete

__all__ = ['Timeout', 'BaseFileLock', 'WindowsFileLock', 'UnixFileLock', 'SoftFileLock', 'FileLock']

TimeoutError = OSError

class Timeout(TimeoutError):
    """
    Raised when the lock could not be acquired in *timeout*
    seconds.
    """
    lock_file: Incomplete
    def __init__(self, lock_file) -> None:
        """ """

class _Acquire_ReturnProxy:
    lock: Incomplete
    def __init__(self, lock) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class BaseFileLock:
    """
    Implements the base class of a file lock.
    """
    def __init__(self, lock_file, timeout: int = -1, max_filename_length: Incomplete | None = None) -> None:
        """ """
    @property
    def lock_file(self):
        """
        The path to the lock file.
        """
    @property
    def timeout(self):
        """
        You can set a default timeout for the filelock. It will be used as
        fallback value in the acquire method, if no timeout value (*None*) is
        given.

        If you want to disable the timeout, set it to a negative value.

        A timeout of 0 means, that there is exactly one attempt to acquire the
        file lock.

        *New in version 2.0.0*
        """
    @timeout.setter
    def timeout(self, value) -> None:
        """ """
    @property
    def is_locked(self):
        """
        True, if the object holds the file lock.

            This was previously a method and is now a property.
        """
    def acquire(self, timeout: Incomplete | None = None, poll_intervall: float = 0.05):
        """
        Acquires the file lock or fails with a :exc:`Timeout` error.

        ```py
        # You can use this method in the context manager (recommended)
        with lock.acquire():
            pass

        # Or use an equivalent try-finally construct:
        lock.acquire()
        try:
            pass
        finally:
            lock.release()
        ```

        :arg float timeout:
            The maximum time waited for the file lock.
            If ``timeout < 0``, there is no timeout and this method will
            block until the lock could be acquired.
            If ``timeout`` is None, the default :attr:`~timeout` is used.

        :arg float poll_intervall:
            We check once in *poll_intervall* seconds if we can acquire the
            file lock.

        :raises Timeout:
            if the lock could not be acquired in *timeout* seconds.

            This method returns now a *proxy* object instead of *self*,
            so that it can be used in a with statement without side effects.
        """
    def release(self, force: bool = False) -> None:
        """
        Releases the file lock.

        Please note, that the lock is only completly released, if the lock
        counter is 0.

        Also note, that the lock file itself is not automatically deleted.

        :arg bool force:
            If true, the lock counter is ignored and the lock is released in
            every case.
        """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __del__(self) -> None: ...
    def hash_filename_if_too_long(self, path: str, max_length: int) -> str: ...

class WindowsFileLock(BaseFileLock):
    """
    Uses the :func:`msvcrt.locking` function to hard lock the lock file on
    windows systems.
    """
    def __init__(self, lock_file, timeout: int = -1, max_filename_length: Incomplete | None = None) -> None: ...

class UnixFileLock(BaseFileLock):
    """
    Uses the :func:`fcntl.flock` to hard lock the lock file on unix systems.
    """
    def __init__(self, lock_file, timeout: int = -1, max_filename_length: Incomplete | None = None) -> None: ...

class SoftFileLock(BaseFileLock):
    """
    Simply watches the existence of the lock file.
    """

FileLock: Incomplete
FileLock = WindowsFileLock
FileLock = UnixFileLock
FileLock = SoftFileLock
