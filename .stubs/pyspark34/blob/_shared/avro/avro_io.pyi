from ..avro import schema as schema
from _typeshed import Incomplete

PY3: Incomplete
logger: Incomplete
STRUCT_FLOAT: Incomplete
STRUCT_DOUBLE: Incomplete

class SchemaResolutionException(schema.AvroException):
    def __init__(self, fail_msg, writer_schema: Incomplete | None = None) -> None: ...

class BinaryDecoder:
    """Read leaf values."""
    def __init__(self, reader) -> None:
        """
        reader is a Python object on which we can call read, seek, and tell.
        """
    @property
    def reader(self):
        """Reports the reader used by this decoder."""
    def read(self, n):
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
    def read_boolean(self):
        """
        a boolean is written as a single byte
        whose value is either 0 (false) or 1 (true).
        """
    def read_int(self):
        """
        int and long values are written using variable-length, zig-zag coding.
        """
    def read_long(self):
        """
        int and long values are written using variable-length, zig-zag coding.
        """
    def read_float(self):
        """
        A float is written as 4 bytes.
        The float is converted into a 32-bit integer using a method equivalent to
        Java's floatToIntBits and then encoded in little-endian format.
        """
    def read_double(self):
        """
        A double is written as 8 bytes.
        The double is converted into a 64-bit integer using a method equivalent to
        Java's doubleToLongBits and then encoded in little-endian format.
        """
    def read_bytes(self):
        """
        Bytes are encoded as a long followed by that many bytes of data.
        """
    def read_utf8(self):
        """
        A string is encoded as a long followed by
        that many bytes of UTF-8 encoded character data.
        """
    def skip_null(self) -> None: ...
    def skip_boolean(self) -> None: ...
    def skip_int(self) -> None: ...
    def skip_long(self) -> None: ...
    def skip_float(self) -> None: ...
    def skip_double(self) -> None: ...
    def skip_bytes(self) -> None: ...
    def skip_utf8(self) -> None: ...
    def skip(self, n) -> None: ...

class DatumReader:
    """Deserialize Avro-encoded data into a Python data structure."""
    def __init__(self, writer_schema: Incomplete | None = None) -> None:
        '''
        As defined in the Avro specification, we call the schema encoded
        in the data the "writer\'s schema".
        '''
    def set_writer_schema(self, writer_schema) -> None: ...
    writer_schema: Incomplete
    def read(self, decoder): ...
    def read_data(self, writer_schema, decoder): ...
    def skip_data(self, writer_schema, decoder): ...
    @staticmethod
    def read_fixed(writer_schema, decoder): ...
    @staticmethod
    def skip_fixed(writer_schema, decoder): ...
    @staticmethod
    def read_enum(writer_schema, decoder): ...
    @staticmethod
    def skip_enum(decoder): ...
    def read_array(self, writer_schema, decoder): ...
    def skip_array(self, writer_schema, decoder) -> None: ...
    def read_map(self, writer_schema, decoder): ...
    def skip_map(self, writer_schema, decoder) -> None: ...
    def read_union(self, writer_schema, decoder): ...
    def skip_union(self, writer_schema, decoder): ...
    def read_record(self, writer_schema, decoder): ...
    def skip_record(self, writer_schema, decoder) -> None: ...
