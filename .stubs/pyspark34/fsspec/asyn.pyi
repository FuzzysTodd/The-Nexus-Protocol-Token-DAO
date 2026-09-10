import asyncio
from .exceptions import FSTimeoutError as FSTimeoutError
from .implementations.local import LocalFileSystem as LocalFileSystem, make_path_posix as make_path_posix, trailing_sep as trailing_sep
from .spec import AbstractBufferedFile as AbstractBufferedFile, AbstractFileSystem as AbstractFileSystem
from .utils import is_exception as is_exception, other_paths as other_paths
from _typeshed import Incomplete

private: Incomplete
iothread: Incomplete
loop: Incomplete
get_running_loop = asyncio.get_running_loop

def get_lock():
    """Allocate or return a threading lock.

    The lock is allocated on first use to allow setting one lock per forked process.
    """
def reset_lock() -> None:
    """Reset the global lock.

    This should be called only on the init of a forked process to reset the lock to
    None, enabling the new forked process to get a new lock.
    """
def sync(loop, func, *args, timeout: Incomplete | None = None, **kwargs):
    """
    Make loop run coroutine until it returns. Runs in other thread

    Examples
    --------
    >>> fsspec.asyn.sync(fsspec.asyn.get_loop(), func, *args,
                         timeout=timeout, **kwargs)
    """
def sync_wrapper(func, obj: Incomplete | None = None):
    """Given a function, make so can be called in async or blocking contexts

    Leave obj=None if defining within a class. Pass the instance if attaching
    as an attribute of the instance.
    """
def get_loop():
    """Create or return the default fsspec IO loop

    The loop will be running on a separate thread.
    """

ResourceError: Incomplete

def running_async() -> bool:
    """Being executed by an event loop?"""

async_methods: Incomplete

class AsyncFileSystem(AbstractFileSystem):
    """Async file operations, default implementations

    Passes bulk operations to asyncio.gather for concurrent operation.

    Implementations that have concurrent batch operations and/or async methods
    should inherit from this class instead of AbstractFileSystem. Docstrings are
    copied from the un-underscored method in AbstractFileSystem, if not given.
    """
    async_impl: bool
    mirror_sync_methods: bool
    disable_throttling: bool
    asynchronous: Incomplete
    batch_size: Incomplete
    def __init__(self, *args, asynchronous: bool = False, loop: Incomplete | None = None, batch_size: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def loop(self): ...
    async def open_async(self, path, mode: str = 'rb', **kwargs) -> None: ...

def mirror_sync_methods(obj) -> None:
    """Populate sync and async methods for obj

    For each method will create a sync version if the name refers to an async method
    (coroutine) and there is no override in the child class; will create an async
    method for the corresponding sync method if there is no implementation.

    Uses the methods specified in
    - async_methods: the set that an implementation is expected to provide
    - default_async_methods: that can be derived from their sync version in
      AbstractFileSystem
    - AsyncFileSystem: async-specific default coroutines
    """

class FSSpecCoroutineCancel(Exception): ...

class AbstractAsyncStreamedFile(AbstractBufferedFile):
    async def read(self, length: int = -1):
        """
        Return data from cache, or fetch pieces as necessary

        Parameters
        ----------
        length: int (-1)
            Number of bytes to read; if <0, all remaining bytes.
        """
    async def write(self, data):
        """
        Write data to buffer.

        Buffer only sent on flush() or if buffer is greater than
        or equal to blocksize.

        Parameters
        ----------
        data: bytes
            Set of bytes to be written.
        """
    cache: Incomplete
    closed: bool
    async def close(self) -> None:
        """Close file

        Finalizes writes, discards cache
        """
    forced: bool
    offset: int
    buffer: Incomplete
    async def flush(self, force: bool = False) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
