from _typeshed import Incomplete
from gevent._compat import reraise as reraise
from gevent._fileobjectcommon import FileObjectBase as FileObjectBase, OpenDescriptor as OpenDescriptor, WriteIsWriteallMixin as WriteIsWriteallMixin, cancel_wait_ex as cancel_wait_ex
from gevent._hub_primitives import wait_on_watcher as wait_on_watcher
from gevent.hub import get_hub as get_hub
from gevent.os import ignored_errors as ignored_errors, make_nonblocking as make_nonblocking
from io import DEFAULT_BUFFER_SIZE, RawIOBase

class GreenFileDescriptorIO(RawIOBase):
    name: Incomplete
    mode: Incomplete
    hub: Incomplete
    def __init__(self, fileno, open_descriptor, closefd: bool = True) -> None: ...
    def isatty(self): ...
    def readable(self): ...
    def writable(self): ...
    def seekable(self): ...
    def fileno(self): ...
    @property
    def closed(self): ...
    def close(self) -> None: ...
    def readall(self): ...
    def readinto(self, b): ...
    def write(self, b): ...
    def seek(self, offset, whence: int = 0): ...

class GreenFileDescriptorIOWriteall(WriteIsWriteallMixin, GreenFileDescriptorIO): ...
class GreenOpenDescriptor(OpenDescriptor): ...

class FileObjectPosix(FileObjectBase):
    """
    FileObjectPosix()

    A file-like object that operates on non-blocking files but
    provides a synchronous, cooperative interface.

    .. caution::
         This object is only effective wrapping files that can be used meaningfully
         with :func:`select.select` such as sockets and pipes.

         In general, on most platforms, operations on regular files
         (e.g., ``open('a_file.txt')``) are considered non-blocking
         already, even though they can take some time to complete as
         data is copied to the kernel and flushed to disk: this time
         is relatively bounded compared to sockets or pipes, though.
         A :func:`~os.read` or :func:`~os.write` call on such a file
         will still effectively block for some small period of time.
         Therefore, wrapping this class around a regular file is
         unlikely to make IO gevent-friendly: reading or writing large
         amounts of data could still block the event loop.

         If you'll be working with regular files and doing IO in large
         chunks, you may consider using
         :class:`~gevent.fileobject.FileObjectThread` or
         :func:`~gevent.os.tp_read` and :func:`~gevent.os.tp_write` to bypass this
         concern.

    .. tip::
         Although this object provides a :meth:`fileno` method and so
         can itself be passed to :func:`fcntl.fcntl`, setting the
         :data:`os.O_NONBLOCK` flag will have no effect (reads will
         still block the greenlet, although other greenlets can run).
         However, removing that flag *will cause this object to no
         longer be cooperative* (other greenlets will no longer run).

         You can use the internal ``fileio`` attribute of this object
         (a :class:`io.RawIOBase`) to perform non-blocking byte reads.
         Note, however, that once you begin directly using this
         attribute, the results from using methods of *this* object
         are undefined, especially in text mode. (See :issue:`222`.)

    .. versionchanged:: 1.1
       Now uses the :mod:`io` package internally. Under Python 2, previously
       used the undocumented class :class:`socket._fileobject`. This provides
       better file-like semantics (and portability to Python 3).
    .. versionchanged:: 1.2a1
       Document the ``fileio`` attribute for non-blocking reads.
    .. versionchanged:: 1.2a1

        A bufsize of 0 in write mode is no longer forced to be 1.
        Instead, the underlying buffer is flushed after every write
        operation to simulate a bufsize of 0. In gevent 1.0, a
        bufsize of 0 was flushed when a newline was written, while
        in gevent 1.1 it was flushed when more than one byte was
        written. Note that this may have performance impacts.
    .. versionchanged:: 1.3a1
        On Python 2, enabling universal newlines no longer forces unicode
        IO.
    .. versionchanged:: 1.5
       The default value for *mode* was changed from ``rb`` to ``r``. This is consistent
       with :func:`open`, :func:`io.open`, and :class:`~.FileObjectThread`, which is the
       default ``FileObject`` on some platforms.
    .. versionchanged:: 1.5
       Stop forcing buffering. Previously, given a ``buffering=0`` argument,
       *buffering* would be set to 1, and ``buffering=1`` would be forced to
       the default buffer size. This was a workaround for a long-standing concurrency
       issue. Now the *buffering* argument is interpreted as intended.
    """
    default_bufsize = DEFAULT_BUFFER_SIZE
    fileio: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
