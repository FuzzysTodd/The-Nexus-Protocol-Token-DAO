from .. import BrokenResourceError as BrokenResourceError, ClosedResourceError as ClosedResourceError, EndOfStream as EndOfStream, TypedAttributeSet as TypedAttributeSet, to_thread as to_thread, typed_attribute as typed_attribute
from ..abc import ByteReceiveStream as ByteReceiveStream, ByteSendStream as ByteSendStream
from os import PathLike
from pathlib import Path
from typing import Any, BinaryIO, Callable, Mapping

class FileStreamAttribute(TypedAttributeSet):
    file: BinaryIO
    path: Path
    fileno: int

class _BaseFileStream:
    def __init__(self, file: BinaryIO) -> None: ...
    async def aclose(self) -> None: ...
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...

class FileReadStream(_BaseFileStream, ByteReceiveStream):
    """
    A byte stream that reads from a file in the file system.

    :param file: a file that has been opened for reading in binary mode

    .. versionadded:: 3.0
    """
    @classmethod
    async def from_path(cls, path: str | PathLike[str]) -> FileReadStream:
        """
        Create a file read stream by opening the given file.

        :param path: path of the file to read from

        """
    async def receive(self, max_bytes: int = 65536) -> bytes: ...
    async def seek(self, position: int, whence: int = ...) -> int:
        """
        Seek the file to the given position.

        .. seealso:: :meth:`io.IOBase.seek`

        .. note:: Not all file descriptors are seekable.

        :param position: position to seek the file to
        :param whence: controls how ``position`` is interpreted
        :return: the new absolute position
        :raises OSError: if the file is not seekable

        """
    async def tell(self) -> int:
        """
        Return the current stream position.

        .. note:: Not all file descriptors are seekable.

        :return: the current absolute position
        :raises OSError: if the file is not seekable

        """

class FileWriteStream(_BaseFileStream, ByteSendStream):
    """
    A byte stream that writes to a file in the file system.

    :param file: a file that has been opened for writing in binary mode

    .. versionadded:: 3.0
    """
    @classmethod
    async def from_path(cls, path: str | PathLike[str], append: bool = False) -> FileWriteStream:
        """
        Create a file write stream by opening the given file for writing.

        :param path: path of the file to write to
        :param append: if ``True``, open the file for appending; if ``False``, any existing file
            at the given path will be truncated

        """
    async def send(self, item: bytes) -> None: ...
