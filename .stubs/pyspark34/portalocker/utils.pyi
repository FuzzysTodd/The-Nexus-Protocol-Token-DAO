import abc
import pathlib
import typing
from . import constants
from _typeshed import Incomplete

__all__ = ['Lock', 'open_atomic']

def open_atomic(filename: Filename, binary: bool = True) -> typing.Iterator[typing.IO]:
    """Open a file for atomic writing. Instead of locking this method allows
    you to write the entire file and move it to the actual location. Note that
    this makes the assumption that a rename is atomic on your platform which
    is generally the case but not a guarantee.

    http://docs.python.org/library/os.html#os.rename

    >>> filename = 'test_file.txt'
    >>> if os.path.exists(filename):
    ...     os.remove(filename)

    >>> with open_atomic(filename) as fh:
    ...     written = fh.write(b'test')
    >>> assert os.path.exists(filename)
    >>> os.remove(filename)

    >>> import pathlib
    >>> path_filename = pathlib.Path('test_file.txt')

    >>> with open_atomic(path_filename) as fh:
    ...     written = fh.write(b'test')
    >>> assert path_filename.exists()
    >>> path_filename.unlink()
    """

class LockBase(abc.ABC, metaclass=abc.ABCMeta):
    timeout: float
    check_interval: float
    fail_when_locked: bool
    def __init__(self, timeout: float | None = None, check_interval: float | None = None, fail_when_locked: bool | None = None) -> None: ...
    @abc.abstractmethod
    def acquire(self, timeout: float | None = None, check_interval: float | None = None, fail_when_locked: bool | None = None): ...
    @abc.abstractmethod
    def release(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: typing.Type[BaseException] | None, exc_value: BaseException | None, traceback: typing.Any) -> bool | None: ...
    def __delete__(self, instance) -> None: ...

class Lock(LockBase):
    """Lock manager with built-in timeout

    Args:
        filename: filename
        mode: the open mode, 'a' or 'ab' should be used for writing. When mode
            contains `w` the file will be truncated to 0 bytes.
        timeout: timeout when trying to acquire a lock
        check_interval: check interval while waiting
        fail_when_locked: after the initial lock failed, return an error
            or lock the file. This does not wait for the timeout.
        **file_open_kwargs: The kwargs for the `open(...)` call

    fail_when_locked is useful when multiple threads/processes can race
    when creating a file. If set to true than the system will wait till
    the lock was acquired and then return an AlreadyLocked exception.

    Note that the file is opened first and locked later. So using 'w' as
    mode will result in truncate _BEFORE_ the lock is checked.
    """
    fh: Incomplete
    filename: Incomplete
    mode: Incomplete
    truncate: Incomplete
    timeout: Incomplete
    check_interval: Incomplete
    fail_when_locked: Incomplete
    flags: Incomplete
    file_open_kwargs: Incomplete
    def __init__(self, filename: Filename, mode: str = 'a', timeout: float | None = None, check_interval: float = ..., fail_when_locked: bool = ..., flags: constants.LockFlags = ..., **file_open_kwargs) -> None: ...
    def acquire(self, timeout: float | None = None, check_interval: float | None = None, fail_when_locked: bool | None = None) -> typing.IO:
        """Acquire the locked filehandle"""
    def release(self) -> None:
        """Releases the currently locked file handle"""

class RLock(Lock):
    """
    A reentrant lock, functions in a similar way to threading.RLock in that it
    can be acquired multiple times.  When the corresponding number of release()
    calls are made the lock will finally release the underlying file lock.
    """
    def __init__(self, filename, mode: str = 'a', timeout=..., check_interval=..., fail_when_locked: bool = False, flags=...) -> None: ...
    def acquire(self, timeout: float | None = None, check_interval: float | None = None, fail_when_locked: bool | None = None) -> typing.IO: ...
    def release(self) -> None: ...

class TemporaryFileLock(Lock):
    def __init__(self, filename: str = '.lock', timeout=..., check_interval=..., fail_when_locked: bool = True, flags=...) -> None: ...
    def release(self) -> None: ...

class BoundedSemaphore(LockBase):
    """
    Bounded semaphore to prevent too many parallel processes from running

    This method is deprecated because multiple processes that are completely
    unrelated could end up using the same semaphore.  To prevent this,
    use `NamedBoundedSemaphore` instead. The
    `NamedBoundedSemaphore` is a drop-in replacement for this class.

    >>> semaphore = BoundedSemaphore(2, directory='')
    >>> str(semaphore.get_filenames()[0])
    'bounded_semaphore.00.lock'
    >>> str(sorted(semaphore.get_random_filenames())[1])
    'bounded_semaphore.01.lock'
    """
    lock: Lock | None
    maximum: Incomplete
    name: Incomplete
    filename_pattern: Incomplete
    directory: Incomplete
    def __init__(self, maximum: int, name: str = 'bounded_semaphore', filename_pattern: str = '{name}.{number:02d}.lock', directory: str = ..., timeout: float | None = ..., check_interval: float | None = ..., fail_when_locked: bool | None = True) -> None: ...
    def get_filenames(self) -> typing.Sequence[pathlib.Path]: ...
    def get_random_filenames(self) -> typing.Sequence[pathlib.Path]: ...
    def get_filename(self, number) -> pathlib.Path: ...
    def acquire(self, timeout: float | None = None, check_interval: float | None = None, fail_when_locked: bool | None = None) -> Lock | None: ...
    def try_lock(self, filenames: typing.Sequence[Filename]) -> bool: ...
    def release(self) -> None: ...

class NamedBoundedSemaphore(BoundedSemaphore):
    """
    Bounded semaphore to prevent too many parallel processes from running

    It's also possible to specify a timeout when acquiring the lock to wait
    for a resource to become available.  This is very similar to
    `threading.BoundedSemaphore` but works across multiple processes and across
    multiple operating systems.

    Because this works across multiple processes it's important to give the
    semaphore a name.  This name is used to create the lock files.  If you
    don't specify a name, a random name will be generated.  This means that
    you can't use the same semaphore in multiple processes unless you pass the
    semaphore object to the other processes.

    >>> semaphore = NamedBoundedSemaphore(2, name='test')
    >>> str(semaphore.get_filenames()[0])
    '...test.00.lock'

    >>> semaphore = NamedBoundedSemaphore(2)
    >>> 'bounded_semaphore' in str(semaphore.get_filenames()[0])
    True

    """
    def __init__(self, maximum: int, name: str | None = None, filename_pattern: str = '{name}.{number:02d}.lock', directory: str = ..., timeout: float | None = ..., check_interval: float | None = ..., fail_when_locked: bool | None = True) -> None: ...
