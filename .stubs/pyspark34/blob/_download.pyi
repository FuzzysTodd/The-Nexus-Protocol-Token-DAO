from ._deserialize import deserialize_blob_properties as deserialize_blob_properties, get_page_ranges_result as get_page_ranges_result
from ._encryption import adjust_blob_size_for_encryption as adjust_blob_size_for_encryption, decrypt_blob as decrypt_blob, get_adjusted_download_range_and_offset as get_adjusted_download_range_and_offset, is_encryption_v2 as is_encryption_v2, parse_encryption_data as parse_encryption_data
from ._shared.request_handlers import validate_and_format_range_headers as validate_and_format_range_headers
from ._shared.response_handlers import parse_length_from_content_range as parse_length_from_content_range, process_storage_error as process_storage_error
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Generic, IO, Iterator, TypeVar

T = TypeVar('T', bytes, str)

def process_range_and_offset(start_range, end_range, length, encryption_options, encryption_data): ...
def process_content(data, start_offset, end_offset, encryption): ...

class _ChunkDownloader:
    client: Incomplete
    non_empty_ranges: Incomplete
    chunk_size: Incomplete
    total_size: Incomplete
    start_index: Incomplete
    end_index: Incomplete
    stream: Incomplete
    stream_lock: Incomplete
    progress_lock: Incomplete
    progress_hook: Incomplete
    stream_start: Incomplete
    progress_total: Incomplete
    encryption_options: Incomplete
    encryption_data: Incomplete
    validate_content: Incomplete
    request_options: Incomplete
    def __init__(self, client: Incomplete | None = None, non_empty_ranges: Incomplete | None = None, total_size: Incomplete | None = None, chunk_size: Incomplete | None = None, current_progress: Incomplete | None = None, start_range: Incomplete | None = None, end_range: Incomplete | None = None, stream: Incomplete | None = None, parallel: Incomplete | None = None, validate_content: Incomplete | None = None, encryption_options: Incomplete | None = None, encryption_data: Incomplete | None = None, progress_hook: Incomplete | None = None, **kwargs) -> None: ...
    def get_chunk_offsets(self) -> Generator[Incomplete, None, None]: ...
    def process_chunk(self, chunk_start) -> None: ...
    def yield_chunk(self, chunk_start): ...

class _ChunkIterator:
    """Async iterator for chunks in blob download stream."""
    size: Incomplete
    def __init__(self, size, content, downloader, chunk_size) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class StorageStreamDownloader(Generic[T]):
    """A streaming object to download from Azure Storage.

    :ivar str name:
        The name of the blob being downloaded.
    :ivar str container:
        The name of the container where the blob is.
    :ivar ~azure.storage.blob.BlobProperties properties:
        The properties of the blob being downloaded. If only a range of the data is being
        downloaded, this will be reflected in the properties.
    :ivar int size:
        The size of the total data in the stream. This will be the byte range if specified,
        otherwise the total size of the blob.
    """
    name: Incomplete
    container: Incomplete
    properties: Incomplete
    size: Incomplete
    def __init__(self, clients: Incomplete | None = None, config: Incomplete | None = None, start_range: Incomplete | None = None, end_range: Incomplete | None = None, validate_content: Incomplete | None = None, encryption_options: Incomplete | None = None, max_concurrency: int = 1, name: Incomplete | None = None, container: Incomplete | None = None, encoding: Incomplete | None = None, download_cls: Incomplete | None = None, **kwargs) -> None: ...
    def __len__(self) -> int: ...
    def chunks(self) -> Iterator[bytes]:
        """Iterate over chunks in the download stream.

        :returns: An iterator of the chunks in the download stream.
        :rtype: Iterator[bytes]

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_hello_world.py
                :start-after: [START download_a_blob_in_chunk]
                :end-before: [END download_a_blob_in_chunk]
                :language: python
                :dedent: 12
                :caption: Download a blob using chunks().
        """
    def read(self, size: int | None = -1) -> T:
        """
        Read up to size bytes from the stream and return them. If size
        is unspecified or is -1, all bytes will be read.

        :param Optional[int] size:
            The number of bytes to download from the stream. Leave unspecified
            or set to -1 to download all bytes.
        :returns:
            The requested data as bytes or a string if encoding was specified. If
            the return value is empty, there is no more data to read.
        :rtype: T
        """
    def readall(self) -> T:
        """
        Read the entire contents of this blob.
        This operation is blocking until all data is downloaded.

        :returns: The requested data as bytes or a string if encoding was specified.
        :rtype: T
        """
    def content_as_bytes(self, max_concurrency: int = 1):
        """DEPRECATED: Download the contents of this file.

        This operation is blocking until all data is downloaded.

        This method is deprecated, use func:`readall` instead.

        :param int max_concurrency:
            The number of parallel connections with which to download.
        :returns: The contents of the file as bytes.
        :rtype: bytes
        """
    def content_as_text(self, max_concurrency: int = 1, encoding: str = 'UTF-8'):
        """DEPRECATED: Download the contents of this blob, and decode as text.

        This operation is blocking until all data is downloaded.

        This method is deprecated, use func:`readall` instead.

        :param int max_concurrency:
            The number of parallel connections with which to download.
        :param str encoding:
            Test encoding to decode the downloaded bytes. Default is UTF-8.
        :returns: The content of the file as a str.
        :rtype: str
        """
    def readinto(self, stream: IO[T]) -> int:
        """Download the contents of this file to a stream.

        :param IO[T] stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream. The stream must be seekable if the download
            uses more than one parallel connection.
        :returns: The number of bytes read.
        :rtype: int
        """
    def download_to_stream(self, stream, max_concurrency: int = 1):
        """DEPRECATED: Download the contents of this blob to a stream.

        This method is deprecated, use func:`readinto` instead.

        :param IO[T] stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream. The stream must be seekable if the download
            uses more than one parallel connection.
        :param int max_concurrency:
            The number of parallel connections with which to download.
        :returns: The properties of the downloaded blob.
        :rtype: Any
        """
