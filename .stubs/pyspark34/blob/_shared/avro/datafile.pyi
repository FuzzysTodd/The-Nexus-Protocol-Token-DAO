from ..avro import avro_io as avro_io, schema as schema
from _typeshed import Incomplete

PY3: Incomplete
logger: Incomplete
VERSION: int
MAGIC: Incomplete
MAGIC_SIZE: Incomplete
SYNC_SIZE: int
META_SCHEMA: Incomplete
VALID_CODECS: Incomplete
SCHEMA_KEY: str

class DataFileException(schema.AvroException):
    """Problem reading or writing file object containers."""

class DataFileReader:
    """Read files written by DataFileWriter."""
    codec: str
    def __init__(self, reader, datum_reader, **kwargs) -> None:
        """Initializes a new data file reader.

        Args:
          reader: Open file to read from.
          datum_reader: Avro datum reader.
        """
    def __enter__(self): ...
    def __exit__(self, data_type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __iter__(self): ...
    @property
    def reader(self): ...
    @property
    def raw_decoder(self): ...
    @property
    def datum_decoder(self): ...
    @property
    def datum_reader(self): ...
    @property
    def sync_marker(self): ...
    @property
    def meta(self): ...
    @property
    def block_count(self): ...
    def get_meta(self, key):
        """Reports the value of a given metadata key.

        :param str key: Metadata key to report the value of.
        :returns: Value associated to the metadata key, as bytes.
        :rtype: bytes
        """
    def __next__(self):
        """Return the next datum in the file."""
    def close(self) -> None:
        """Close this reader."""
