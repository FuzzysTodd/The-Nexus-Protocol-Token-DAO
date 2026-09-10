from .exceptions import BufferFull as BufferFull, ExtraData as ExtraData, FormatError as FormatError, OutOfData as OutOfData, StackError as StackError
from .ext import ExtType as ExtType, Timestamp as Timestamp
from _typeshed import Incomplete

USING_STRINGBUILDER: bool

class StringIO:
    builder: Incomplete
    def __init__(self, s: bytes = b'') -> None: ...
    def write(self, s) -> None: ...
    def getvalue(self): ...

EX_SKIP: int
EX_CONSTRUCT: int
EX_READ_ARRAY_HEADER: int
EX_READ_MAP_HEADER: int
TYPE_IMMEDIATE: int
TYPE_ARRAY: int
TYPE_MAP: int
TYPE_RAW: int
TYPE_BIN: int
TYPE_EXT: int
DEFAULT_RECURSE_LIMIT: int

def unpackb(packed, **kwargs):
    """
    Unpack an object from `packed`.

    Raises ``ExtraData`` when *packed* contains extra bytes.
    Raises ``ValueError`` when *packed* is incomplete.
    Raises ``FormatError`` when *packed* is not valid msgpack.
    Raises ``StackError`` when *packed* contains too nested.
    Other exceptions can be raised during unpacking.

    See :class:`Unpacker` for options.
    """

class Unpacker:
    """Streaming unpacker.

    Arguments:

    :param file_like:
        File-like object having `.read(n)` method.
        If specified, unpacker reads serialized data from it and `.feed()` is not usable.

    :param int read_size:
        Used as `file_like.read(read_size)`. (default: `min(16*1024, max_buffer_size)`)

    :param bool use_list:
        If true, unpack msgpack array to Python list.
        Otherwise, unpack to Python tuple. (default: True)

    :param bool raw:
        If true, unpack msgpack raw to Python bytes.
        Otherwise, unpack to Python str by decoding with UTF-8 encoding (default).

    :param int timestamp:
        Control how timestamp type is unpacked:

            0 - Timestamp
            1 - float  (Seconds from the EPOCH)
            2 - int  (Nanoseconds from the EPOCH)
            3 - datetime.datetime  (UTC).

    :param bool strict_map_key:
        If true (default), only str or bytes are accepted for map (dict) keys.

    :param object_hook:
        When specified, it should be callable.
        Unpacker calls it with a dict argument after unpacking msgpack map.
        (See also simplejson)

    :param object_pairs_hook:
        When specified, it should be callable.
        Unpacker calls it with a list of key-value pairs after unpacking msgpack map.
        (See also simplejson)

    :param str unicode_errors:
        The error handler for decoding unicode. (default: 'strict')
        This option should be used only when you have msgpack data which
        contains invalid UTF-8 string.

    :param int max_buffer_size:
        Limits size of data waiting unpacked.  0 means 2**32-1.
        The default value is 100*1024*1024 (100MiB).
        Raises `BufferFull` exception when it is insufficient.
        You should set this parameter when unpacking data from untrusted source.

    :param int max_str_len:
        Deprecated, use *max_buffer_size* instead.
        Limits max length of str. (default: max_buffer_size)

    :param int max_bin_len:
        Deprecated, use *max_buffer_size* instead.
        Limits max length of bin. (default: max_buffer_size)

    :param int max_array_len:
        Limits max length of array.
        (default: max_buffer_size)

    :param int max_map_len:
        Limits max length of map.
        (default: max_buffer_size//2)

    :param int max_ext_len:
        Deprecated, use *max_buffer_size* instead.
        Limits max size of ext type.  (default: max_buffer_size)

    Example of streaming deserialize from file-like object::

        unpacker = Unpacker(file_like)
        for o in unpacker:
            process(o)

    Example of streaming deserialize from socket::

        unpacker = Unpacker()
        while True:
            buf = sock.recv(1024**2)
            if not buf:
                break
            unpacker.feed(buf)
            for o in unpacker:
                process(o)

    Raises ``ExtraData`` when *packed* contains extra bytes.
    Raises ``OutOfData`` when *packed* is incomplete.
    Raises ``FormatError`` when *packed* is not valid msgpack.
    Raises ``StackError`` when *packed* contains too nested.
    Other exceptions can be raised during unpacking.
    """
    file_like: Incomplete
    def __init__(self, file_like: Incomplete | None = None, read_size: int = 0, use_list: bool = True, raw: bool = False, timestamp: int = 0, strict_map_key: bool = True, object_hook: Incomplete | None = None, object_pairs_hook: Incomplete | None = None, list_hook: Incomplete | None = None, unicode_errors: Incomplete | None = None, max_buffer_size=..., ext_hook=..., max_str_len: int = -1, max_bin_len: int = -1, max_array_len: int = -1, max_map_len: int = -1, max_ext_len: int = -1) -> None: ...
    def feed(self, next_bytes) -> None: ...
    def read_bytes(self, n): ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__
    def skip(self) -> None: ...
    def unpack(self): ...
    def read_array_header(self): ...
    def read_map_header(self): ...
    def tell(self): ...

class Packer:
    """
    MessagePack Packer

    Usage::

        packer = Packer()
        astream.write(packer.pack(a))
        astream.write(packer.pack(b))

    Packer's constructor has some keyword arguments:

    :param default:
        When specified, it should be callable.
        Convert user type to builtin type that Packer supports.
        See also simplejson's document.

    :param bool use_single_float:
        Use single precision float type for float. (default: False)

    :param bool autoreset:
        Reset buffer after each pack and return its content as `bytes`. (default: True).
        If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.

    :param bool use_bin_type:
        Use bin type introduced in msgpack spec 2.0 for bytes.
        It also enables str8 type for unicode. (default: True)

    :param bool strict_types:
        If set to true, types will be checked to be exact. Derived classes
        from serializable types will not be serialized and will be
        treated as unsupported type and forwarded to default.
        Additionally tuples will not be serialized as lists.
        This is useful when trying to implement accurate serialization
        for python types.

    :param bool datetime:
        If set to true, datetime with tzinfo is packed into Timestamp type.
        Note that the tzinfo is stripped in the timestamp.
        You can get UTC datetime with `timestamp=3` option of the Unpacker.

    :param str unicode_errors:
        The error handler for encoding unicode. (default: 'strict')
        DO NOT USE THIS!!  This option is kept for very specific usage.

    Example of streaming deserialize from file-like object::

        unpacker = Unpacker(file_like)
        for o in unpacker:
            process(o)

    Example of streaming deserialize from socket::

        unpacker = Unpacker()
        while True:
            buf = sock.recv(1024**2)
            if not buf:
                break
            unpacker.feed(buf)
            for o in unpacker:
                process(o)

    Raises ``ExtraData`` when *packed* contains extra bytes.
    Raises ``OutOfData`` when *packed* is incomplete.
    Raises ``FormatError`` when *packed* is not valid msgpack.
    Raises ``StackError`` when *packed* contains too nested.
    Other exceptions can be raised during unpacking.
    """
    def __init__(self, default: Incomplete | None = None, use_single_float: bool = False, autoreset: bool = True, use_bin_type: bool = True, strict_types: bool = False, datetime: bool = False, unicode_errors: Incomplete | None = None) -> None: ...
    def pack(self, obj): ...
    def pack_map_pairs(self, pairs): ...
    def pack_array_header(self, n): ...
    def pack_map_header(self, n): ...
    def pack_ext_type(self, typecode, data) -> None: ...
    def bytes(self):
        """Return internal buffer contents as bytes object"""
    def reset(self) -> None:
        """Reset internal buffer.

        This method is useful only when autoreset=False.
        """
    def getbuffer(self):
        """Return view of internal buffer."""
