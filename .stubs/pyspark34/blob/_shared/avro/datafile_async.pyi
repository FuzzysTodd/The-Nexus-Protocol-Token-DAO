from ..avro import avro_io_async as avro_io_async, schema as schema
from .datafile import DataFileException as DataFileException, MAGIC as MAGIC, META_SCHEMA as META_SCHEMA, SCHEMA_KEY as SCHEMA_KEY, SYNC_SIZE as SYNC_SIZE
from _typeshed import Incomplete

PY3: Incomplete
logger: Incomplete
VALID_CODECS: Incomplete

class AsyncDataFileReader:
    """Read files written by DataFileWriter."""
    codec: str
    def __init__(self, reader, datum_reader, **kwargs) -> None:
        """Initializes a new data file reader.

        Args:
          reader: Open file to read from.
          datum_reader: Avro datum reader.
        """
    async def init(self): ...
    async def __aenter__(self): ...
    async def __aexit__(self, data_type, value, traceback) -> None: ...
    def __aiter__(self): ...
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
    async def __anext__(self):
        """Return the next datum in the file."""
    def close(self) -> None:
        """Close this reader."""
