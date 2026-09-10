from ..avro import schema as schema
from .avro_io import STRUCT_DOUBLE as STRUCT_DOUBLE, STRUCT_FLOAT as STRUCT_FLOAT, SchemaResolutionException as SchemaResolutionException
from _typeshed import Incomplete

PY3: Incomplete
logger: Incomplete

class AsyncBinaryDecoder:
    """Read leaf values."""
    def __init__(self, reader) -> None:
        """
        reader is a Python object on which we can call read, seek, and tell.
        """
    @property
    def reader(self):
        """Reports the reader used by this decoder."""
    async def read(self, n):
        """Read n bytes.

        :param int n: Number of bytes to read.
        :returns: The next n bytes from the input.
        :rtype: bytes
        """
    @staticmethod
    def read_null() -> None:
        """
        null is written as zero bytes
        """
    async def read_boolean(self):
        """
        a boolean is written as a single byte
        whose value is either 0 (false) or 1 (true).
        """
    async def read_int(self):
        """
        int and long values are written using variable-length, zig-zag coding.
        """
    async def read_long(self):
        """
        int and long values are written using variable-length, zig-zag coding.
        """
    async def read_float(self):
        """
        A float is written as 4 bytes.
        The float is converted into a 32-bit integer using a method equivalent to
        Java's floatToIntBits and then encoded in little-endian format.
        """
    async def read_double(self):
        """
        A double is written as 8 bytes.
        The double is converted into a 64-bit integer using a method equivalent to
        Java's doubleToLongBits and then encoded in little-endian format.
        """
    async def read_bytes(self):
        """
        Bytes are encoded as a long followed by that many bytes of data.
        """
    async def read_utf8(self):
        """
        A string is encoded as a long followed by
        that many bytes of UTF-8 encoded character data.
        """
    def skip_null(self) -> None: ...
    async def skip_boolean(self) -> None: ...
    async def skip_int(self) -> None: ...
    async def skip_long(self) -> None: ...
    async def skip_float(self) -> None: ...
    async def skip_double(self) -> None: ...
    async def skip_bytes(self) -> None: ...
    async def skip_utf8(self) -> None: ...
    async def skip(self, n) -> None: ...

class AsyncDatumReader:
    """Deserialize Avro-encoded data into a Python data structure."""
    def __init__(self, writer_schema: Incomplete | None = None) -> None:
        '''
        As defined in the Avro specification, we call the schema encoded
        in the data the "writer\'s schema", and the schema expected by the
        reader the "reader\'s schema".
        '''
    def set_writer_schema(self, writer_schema) -> None: ...
    writer_schema: Incomplete
    async def read(self, decoder): ...
    async def read_data(self, writer_schema, decoder): ...
    async def skip_data(self, writer_schema, decoder): ...
    @staticmethod
    async def read_fixed(writer_schema, decoder): ...
    @staticmethod
    async def skip_fixed(writer_schema, decoder): ...
    @staticmethod
    async def read_enum(writer_schema, decoder): ...
    @staticmethod
    async def skip_enum(decoder): ...
    async def read_array(self, writer_schema, decoder): ...
    async def skip_array(self, writer_schema, decoder) -> None: ...
    async def read_map(self, writer_schema, decoder): ...
    async def skip_map(self, writer_schema, decoder) -> None: ...
    async def read_union(self, writer_schema, decoder): ...
    async def skip_union(self, writer_schema, decoder): ...
    async def read_record(self, writer_schema, decoder): ...
    async def skip_record(self, writer_schema, decoder) -> None: ...
