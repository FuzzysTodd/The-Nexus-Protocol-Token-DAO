from _typeshed import Incomplete
from typing import IO, Iterable

class DataLakeFileQueryReader:
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
    file_system: Incomplete
    response_headers: Incomplete
    record_delimiter: Incomplete
    def __init__(self, blob_query_reader) -> None: ...
    def __len__(self) -> int: ...
    def readall(self) -> bytes | str:
        """Return all query results.

        This operation is blocking until all data is downloaded.
        If encoding has been configured - this will be used to decode individual
        records are they are received.

        :rtype: Union[bytes, str]
        """
    def readinto(self, stream: IO) -> None:
        """Download the query result to a stream.

        :param stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream.
        :returns: None
        """
    def records(self) -> Iterable[bytes | str]:
        """Returns a record generator for the query result.

        Records will be returned line by line.
        If encoding has been configured - this will be used to decode individual
        records are they are received.

        :rtype: Iterable[Union[bytes, str]]
        """
