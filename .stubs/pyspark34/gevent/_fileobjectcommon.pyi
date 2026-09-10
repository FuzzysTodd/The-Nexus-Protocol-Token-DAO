import io
from _typeshed import Incomplete
from gevent._compat import fspath as fspath, integer_types as integer_types, reraise as reraise
from gevent.lock import DummySemaphore as DummySemaphore, Semaphore as Semaphore

class cancel_wait_ex(IOError):
    def __init__(self) -> None: ...

class FileObjectClosed(IOError):
    def __init__(self) -> None: ...

class UniversalNewlineBytesWrapper(io.TextIOWrapper):
    """
    Uses TextWrapper to decode universal newlines, but returns the
    results as bytes.

    This is for Python 2 where the 'rU' mode did that.
    """
    mode: Incomplete
    def __init__(self, fobj, line_buffering) -> None: ...
    def read(self, *args, **kwargs): ...
    def readline(self, limit: int = -1): ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class FlushingBufferedWriter(io.BufferedWriter):
    def write(self, b): ...

class WriteallMixin:
    def writeall(self, value):
        """
        Similar to :meth:`socket.socket.sendall`, ensures that all the contents of
        *value* have been written (though not necessarily flushed) before returning.

        Returns the length of *value*.

        .. versionadded:: 20.12.0
        """

class FileIO(io.FileIO):
    """A subclass that we can dynamically assign __class__ for."""

class WriteIsWriteallMixin(WriteallMixin):
    def write(self, value): ...

class WriteallFileIO(WriteIsWriteallMixin, io.FileIO): ...

class OpenDescriptor:
    """
    Interprets the arguments to `open`. Internal use only.

    Originally based on code in the stdlib's _pyio.py (Python implementation of
    the :mod:`io` module), but modified for gevent:

    - Native strings are returned on Python 2 when neither
      'b' nor 't' are in the mode string and no encoding is specified.
    - Universal newlines work in that mode.
    - Allows externally unbuffered text IO.

    :keyword bool atomic_write: If true, then if the opened, wrapped, stream
        is unbuffered (meaning that ``write`` can produce short writes and the return
        value needs to be checked), then the implementation will be adjusted so that
        ``write`` behaves like Python 2 on a built-in file object and writes the
        entire value. Only set this on Python 2; the only intended user is
        :class:`gevent.subprocess.Popen`.
    """
    fileio_mode: Incomplete
    mode: Incomplete
    creating: Incomplete
    reading: Incomplete
    writing: Incomplete
    appending: Incomplete
    updating: Incomplete
    text: Incomplete
    binary: Incomplete
    can_write: Incomplete
    can_read: Incomplete
    native: Incomplete
    universal: Incomplete
    buffering: Incomplete
    encoding: Incomplete
    errors: Incomplete
    newline: Incomplete
    closefd: Incomplete
    atomic_write: Incomplete
    def __init__(self, fobj, mode: str = 'r', bufsize: Incomplete | None = None, close: Incomplete | None = None, encoding: Incomplete | None = None, errors: Incomplete | None = None, newline: Incomplete | None = None, buffering: Incomplete | None = None, closefd: Incomplete | None = None, atomic_write: bool = False) -> None: ...
    default_buffer_size: Incomplete
    def is_fd(self): ...
    def opened(self):
        """
        Return the :meth:`wrapped` file object.
        """
    def opened_raw(self): ...
    @staticmethod
    def is_buffered(stream): ...
    @classmethod
    def buffer_size_for_stream(cls, stream): ...

class _ClosedIO:
    name: Incomplete
    def __init__(self, io_obj) -> None: ...
    def __getattr__(self, name) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__

class FileObjectBase:
    """
    Internal base class to ensure a level of consistency
    between :class:`~.FileObjectPosix`, :class:`~.FileObjectThread`
    and :class:`~.FileObjectBlock`.
    """
    def __init__(self, descriptor: OpenDescriptor) -> None: ...
    io: Incomplete
    @property
    def closed(self):
        """True if the file is closed"""
    def close(self) -> None: ...
    def __getattr__(self, name): ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__

class FileObjectBlock(FileObjectBase):
    """
    FileObjectBlock()

    A simple synchronous wrapper around a file object.

    Adds no concurrency or gevent compatibility.
    """
    def __init__(self, fobj, *args, **kwargs) -> None: ...

class FileObjectThread(FileObjectBase):
    """
    FileObjectThread()

    A file-like object wrapping another file-like object, performing all blocking
    operations on that object in a background thread.

    .. caution::
        Attempting to change the threadpool or lock of an existing FileObjectThread
        has undefined consequences.

    .. versionchanged:: 1.1b1
       The file object is closed using the threadpool. Note that whether or
       not this action is synchronous or asynchronous is not documented.
    """
    threadpool: Incomplete
    lock: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        :keyword bool lock: If True (the default) then all operations will
           be performed one-by-one. Note that this does not guarantee that, if using
           this file object from multiple threads/greenlets, operations will be performed
           in any particular order, only that no two operations will be attempted at the
           same time. You can also pass your own :class:`gevent.lock.Semaphore` to synchronize
           file operations with an external resource.
        :keyword bool closefd: If True (the default) then when this object is closed,
           the underlying object is closed as well. If *fobj* is a path, then
           *closefd* must be True.
        """
