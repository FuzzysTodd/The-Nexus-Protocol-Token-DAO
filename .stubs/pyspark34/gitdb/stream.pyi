from _typeshed import Incomplete
from gitdb.util import LazyMixin

__all__ = ['DecompressMemMapReader', 'FDCompressedSha1Writer', 'DeltaApplyReader', 'Sha1Writer', 'FlexibleSha1Writer', 'ZippedStoreShaWriter', 'FDCompressedSha1Writer', 'FDStream', 'NullStream']

class DecompressMemMapReader(LazyMixin):
    """Reads data in chunks from a memory map and decompresses it. The client sees
    only the uncompressed data, respective file-like read calls are handling on-demand
    buffered decompression accordingly

    A constraint on the total size of bytes is activated, simulating
    a logical file within a possibly larger physical memory area

    To read efficiently, you clearly don't want to read individual bytes, instead,
    read a few kilobytes at least.

    **Note:** The chunk-size should be carefully selected as it will involve quite a bit
        of string copying due to the way the zlib is implemented. Its very wasteful,
        hence we try to find a good tradeoff between allocation time and number of
        times we actually allocate. An own zlib implementation would be good here
        to better support streamed reading - it would only need to keep the mmap
        and decompress it into chunks, that's all ... """
    max_read_size: Incomplete
    def __init__(self, m, close_on_deletion, size: Incomplete | None = None) -> None:
        """Initialize with mmap for stream reading
        :param m: must be content data - use new if you have object data and no size"""
    def __del__(self) -> None: ...
    @classmethod
    def new(self, m, close_on_deletion: bool = False):
        """Create a new DecompressMemMapReader instance for acting as a read-only stream
        This method parses the object header from m and returns the parsed
        type and size, as well as the created stream instance.

        :param m: memory map on which to operate. It must be object data ( header + contents )
        :param close_on_deletion: if True, the memory map will be closed once we are
            being deleted"""
    def data(self):
        """:return: random access compatible data we are working on"""
    def close(self) -> None:
        """Close our underlying stream of compressed bytes if this was allowed during initialization
        :return: True if we closed the underlying stream
        :note: can be called safely
        """
    def compressed_bytes_read(self):
        """
        :return: number of compressed bytes read. This includes the bytes it
            took to decompress the header ( if there was one )"""
    def seek(self, offset, whence=...) -> None:
        """Allows to reset the stream to restart reading
        :raise ValueError: If offset and whence are not 0"""
    def read(self, size: int = -1): ...

class DeltaApplyReader(LazyMixin):
    """A reader which dynamically applies pack deltas to a base object, keeping the
    memory demands to a minimum.

    The size of the final object is only obtainable once all deltas have been
    applied, unless it is retrieved from a pack index.

    The uncompressed Delta has the following layout (MSB being a most significant
    bit encoded dynamic size):

    * MSB Source Size - the size of the base against which the delta was created
    * MSB Target Size - the size of the resulting data after the delta was applied
    * A list of one byte commands (cmd) which are followed by a specific protocol:

     * cmd & 0x80 - copy delta_data[offset:offset+size]

      * Followed by an encoded offset into the delta data
      * Followed by an encoded size of the chunk to copy

     *  cmd & 0x7f - insert

      * insert cmd bytes from the delta buffer into the output stream

     * cmd == 0 - invalid operation ( or error in delta stream )
    """
    k_max_memory_move: Incomplete
    def __init__(self, stream_list) -> None:
        """Initialize this instance with a list of streams, the first stream being
        the delta to apply on top of all following deltas, the last stream being the
        base object onto which to apply the deltas"""
    def read(self, count: int = 0): ...
    def seek(self, offset, whence=...) -> None:
        """Allows to reset the stream to restart reading

        :raise ValueError: If offset and whence are not 0"""
    @classmethod
    def new(cls, stream_list):
        """
        Convert the given list of streams into a stream which resolves deltas
        when reading from it.

        :param stream_list: two or more stream objects, first stream is a Delta
            to the object that you want to resolve, followed by N additional delta
            streams. The list's last stream must be a non-delta stream.

        :return: Non-Delta OPackStream object whose stream can be used to obtain
            the decompressed resolved data
        :raise ValueError: if the stream list cannot be handled"""
    @property
    def type(self): ...
    @property
    def type_id(self): ...
    @property
    def size(self):
        """:return: number of uncompressed bytes in the stream"""

class Sha1Writer:
    """Simple stream writer which produces a sha whenever you like as it degests
    everything it is supposed to write"""
    sha1: Incomplete
    def __init__(self) -> None: ...
    def write(self, data):
        """:raise IOError: If not all bytes could be written
        :param data: byte object
        :return: length of incoming data"""
    def sha(self, as_hex: bool = False):
        """:return: sha so far
        :param as_hex: if True, sha will be hex-encoded, binary otherwise"""

class FlexibleSha1Writer(Sha1Writer):
    """Writer producing a sha1 while passing on the written bytes to the given
    write function"""
    writer: Incomplete
    def __init__(self, writer) -> None: ...
    def write(self, data) -> None: ...

class ZippedStoreShaWriter(Sha1Writer):
    """Remembers everything someone writes to it and generates a sha"""
    buf: Incomplete
    zip: Incomplete
    def __init__(self) -> None: ...
    def __getattr__(self, attr): ...
    def write(self, data): ...
    def close(self) -> None: ...
    def seek(self, offset, whence=...) -> None:
        """Seeking currently only supports to rewind written data
        Multiple writes are not supported"""
    def getvalue(self):
        """:return: string value from the current stream position to the end"""

class FDCompressedSha1Writer(Sha1Writer):
    """Digests data written to it, making the sha available, then compress the
    data and write it to the file descriptor

    **Note:** operates on raw file descriptors
    **Note:** for this to work, you have to use the close-method of this instance"""
    exc: Incomplete
    fd: Incomplete
    zip: Incomplete
    def __init__(self, fd) -> None: ...
    def write(self, data):
        """:raise IOError: If not all bytes could be written
        :return: length of incoming data"""
    def close(self): ...

class FDStream:
    """A simple wrapper providing the most basic functions on a file descriptor
    with the fileobject interface. Cannot use os.fdopen as the resulting stream
    takes ownership"""
    def __init__(self, fd) -> None: ...
    def write(self, data) -> None: ...
    def read(self, count: int = 0): ...
    def fileno(self): ...
    def tell(self): ...
    def close(self) -> None: ...

class NullStream:
    """A stream that does nothing but providing a stream interface.
    Use it like /dev/null"""
    def read(self, size: int = 0): ...
    def close(self) -> None: ...
    def write(self, data): ...
