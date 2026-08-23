import binascii
import os
from _typeshed import Incomplete
from gitdb.const import NULL_BIN_SHA as NULL_BIN_SHA, NULL_HEX_SHA as NULL_HEX_SHA
from smmap import StaticWindowMapManager as StaticWindowMapManager
from struct import unpack_from as unpack_from

mman: Incomplete
hex_to_bin = binascii.a2b_hex
bin_to_hex = binascii.b2a_hex
ENOENT: Incomplete
exists = os.path.exists
mkdir = os.mkdir
chmod = os.chmod
isdir = os.path.isdir
isfile = os.path.isfile
rename = os.rename
dirname: Incomplete
basename: Incomplete
join: Incomplete
read = os.read
write = os.write
close = os.close
fsync = os.fsync

def remove(*args, **kwargs): ...

class _RandomAccessBytesIO:
    """Wrapper to provide required functionality in case memory maps cannot or may
    not be used. This is only really required in python 2.4"""
    def __init__(self, buf: str = '') -> None: ...
    def __getattr__(self, attr): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __getslice__(self, start, end): ...

def byte_ord(b):
    """
    Return the integer representation of the byte string.  This supports Python
    3 byte arrays as well as standard strings.
    """
def make_sha(source: bytes = b''):
    """A python2.4 workaround for the sha/hashlib module fiasco

    **Note** From the dulwich project """
def allocate_memory(size):
    """:return: a file-protocol accessible memory block of the given size"""
def file_contents_ro(fd, stream: bool = False, allow_mmap: bool = True):
    """:return: read-only contents of the file represented by the file descriptor fd

    :param fd: file descriptor opened for reading
    :param stream: if False, random access is provided, otherwise the stream interface
        is provided.
    :param allow_mmap: if True, its allowed to map the contents into memory, which
        allows large files to be handled and accessed efficiently. The file-descriptor
        will change its position if this is False"""
def file_contents_ro_filepath(filepath, stream: bool = False, allow_mmap: bool = True, flags: int = 0):
    """Get the file contents at filepath as fast as possible

    :return: random access compatible memory of the given filepath
    :param stream: see ``file_contents_ro``
    :param allow_mmap: see ``file_contents_ro``
    :param flags: additional flags to pass to os.open
    :raise OSError: If the file could not be opened

    **Note** for now we don't try to use O_NOATIME directly as the right value needs to be
    shared per database in fact. It only makes a real difference for loose object
    databases anyway, and they use it with the help of the ``flags`` parameter"""
def sliding_ro_buffer(filepath, flags: int = 0):
    """
    :return: a buffer compatible object which uses our mapped memory manager internally
        ready to read the whole given filepath"""
def to_hex_sha(sha):
    """:return: hexified version  of sha"""
def to_bin_sha(sha): ...

class LazyMixin:
    """
    Base class providing an interface to lazily retrieve attribute values upon
    first access. If slots are used, memory will only be reserved once the attribute
    is actually accessed and retrieved the first time. All future accesses will
    return the cached value as stored in the Instance's dict or slot.
    """
    def __getattr__(self, attr):
        """
        Whenever an attribute is requested that we do not know, we allow it
        to be created and set. Next time the same attribute is requested, it is simply
        returned from our dict/slots. """

class LockedFD:
    """
    This class facilitates a safe read and write operation to a file on disk.
    If we write to 'file', we obtain a lock file at 'file.lock' and write to
    that instead. If we succeed, the lock file will be renamed to overwrite
    the original file.

    When reading, we obtain a lock file, but to prevent other writers from
    succeeding while we are reading the file.

    This type handles error correctly in that it will assure a consistent state
    on destruction.

    **note** with this setup, parallel reading is not possible"""
    def __init__(self, filepath) -> None:
        """Initialize an instance with the givne filepath"""
    def __del__(self) -> None: ...
    def open(self, write: bool = False, stream: bool = False):
        """
        Open the file descriptor for reading or writing, both in binary mode.

        :param write: if True, the file descriptor will be opened for writing. Other
            wise it will be opened read-only.
        :param stream: if True, the file descriptor will be wrapped into a simple stream
            object which supports only reading or writing
        :return: fd to read from or write to. It is still maintained by this instance
            and must not be closed directly
        :raise IOError: if the lock could not be retrieved
        :raise OSError: If the actual file could not be opened for reading

        **note** must only be called once"""
    def commit(self) -> None:
        """When done writing, call this function to commit your changes into the
        actual file.
        The file descriptor will be closed, and the lockfile handled.

        **Note** can be called multiple times"""
    def rollback(self) -> None:
        """Abort your operation without any changes. The file descriptor will be
        closed, and the lock released.

        **Note** can be called multiple times"""
