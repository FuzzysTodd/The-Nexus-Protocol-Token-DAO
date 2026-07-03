from .._deserialize import from_blob_properties as from_blob_properties
from _typeshed import Incomplete
from typing import AsyncIterator, IO

class StorageStreamDownloader:
    """A streaming object to download from Azure Storage.

    :ivar str name:
        The name of the file being downloaded.
    :ivar ~azure.storage.filedatalake.FileProperties properties:
        The properties of the file being downloaded. If only a range of the data is being
        downloaded, this will be reflected in the properties.
    :ivar int size:
        The size of the total data in the stream. This will be the byte range if specified,
        otherwise the total size of the file.
    """
    name: Incomplete
    properties: Incomplete
    size: Incomplete
    def __init__(self, downloader) -> None: ...
    def __len__(self) -> int: ...
    def chunks(self) -> AsyncIterator[bytes]:
        """Iterate over chunks in the download stream.

        :rtype: AsyncIterator[bytes]
        """
    async def read(self, size: int | None = -1) -> bytes:
        """
        Read up to size bytes from the stream and return them. If size
        is unspecified or is -1, all bytes will be read.

        :param size:
            The number of bytes to download from the stream. Leave unspecified
            or set to -1 to download all bytes.
        :returns:
            The requested data as bytes. If the return value is empty, there is no more data to read.
        :rtype: bytes
        """
    async def readall(self) -> bytes:
        """Download the contents of this file.

        This operation is blocking until all data is downloaded.
        :rtype: bytes
        """
    async def readinto(self, stream: IO[bytes]) -> int:
        """Download the contents of this file to a stream.

        :param stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream. The stream must be seekable if the download
            uses more than one parallel connection.
        :returns: The number of bytes read.
        :rtype: int
        """
