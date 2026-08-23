from ._shared.avro.avro_io import DatumReader as DatumReader
from ._shared.avro.datafile import DataFileReader as DataFileReader
from _typeshed import Incomplete
from typing import IO, Iterable

class BlobQueryReader:
    """A streaming object to read query results.

    :ivar str name:
        The name of the blob being quered.
    :ivar str container:
        The name of the container where the blob is.
    :ivar dict response_headers:
        The response_headers of the quick query request.
    :ivar bytes record_delimiter:
        The delimiter used to separate lines, or records with the data. The `records`
        method will return these lines via a generator.
    """
    name: Incomplete
    container: Incomplete
    response_headers: Incomplete
    record_delimiter: Incomplete
    def __init__(self, name: Incomplete | None = None, container: Incomplete | None = None, errors: Incomplete | None = None, record_delimiter: str = '\n', encoding: Incomplete | None = None, headers: Incomplete | None = None, response: Incomplete | None = None, error_cls: Incomplete | None = None) -> None: ...
    def __len__(self) -> int: ...
    def readall(self) -> bytes | str:
        """Return all query results.

        This operation is blocking until all data is downloaded.
        If encoding has been configured - this will be used to decode individual
        records are they are received.

        :returns: The query results.
        :rtype: Union[bytes, str]
        """
    def readinto(self, stream: IO) -> None:
        """Download the query result to a stream.

        :param IO stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream.
        :returns: None
        """
    def records(self) -> Iterable[bytes | str]:
        """Returns a record generator for the query result.

        Records will be returned line by line.
        If encoding has been configured - this will be used to decode individual
        records are they are received.

        :returns: A record generator for the query result.
        :rtype: Iterable[Union[bytes, str]]
        """

class QuickQueryStreamer:
    """
    File-like streaming iterator.
    """
    generator: Incomplete
    iterator: Incomplete
    file_length: Incomplete
    def __init__(self, generator) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @staticmethod
    def seekable(): ...
    def __next__(self): ...
    def tell(self): ...
    def seek(self, offset, whence: int = 0) -> None: ...
    def read(self, size): ...
