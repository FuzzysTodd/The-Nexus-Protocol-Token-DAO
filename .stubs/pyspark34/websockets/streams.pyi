from _typeshed import Incomplete
from typing import Generator

class StreamReader:
    """
    Generator-based stream reader.

    This class doesn't support concurrent calls to :meth:`read_line`,
    :meth:`read_exact`, or :meth:`read_to_eof`. Make sure calls are
    serialized.

    """
    buffer: Incomplete
    eof: bool
    def __init__(self) -> None: ...
    def read_line(self, m: int) -> Generator[None, None, bytes]:
        """
        Read a LF-terminated line from the stream.

        This is a generator-based coroutine.

        The return value includes the LF character.

        Args:
            m: maximum number bytes to read; this is a security limit.

        Raises:
            EOFError: if the stream ends without a LF.
            RuntimeError: if the stream ends in more than ``m`` bytes.

        """
    def read_exact(self, n: int) -> Generator[None, None, bytes]:
        """
        Read a given number of bytes from the stream.

        This is a generator-based coroutine.

        Args:
            n: how many bytes to read.

        Raises:
            EOFError: if the stream ends in less than ``n`` bytes.

        """
    def read_to_eof(self, m: int) -> Generator[None, None, bytes]:
        """
        Read all bytes from the stream.

        This is a generator-based coroutine.

        Args:
            m: maximum number bytes to read; this is a security limit.

        Raises:
            RuntimeError: if the stream ends in more than ``m`` bytes.

        """
    def at_eof(self) -> Generator[None, None, bool]:
        """
        Tell whether the stream has ended and all data was read.

        This is a generator-based coroutine.

        """
    def feed_data(self, data: bytes) -> None:
        """
        Write data to the stream.

        :meth:`feed_data` cannot be called after :meth:`feed_eof`.

        Args:
            data: data to write.

        Raises:
            EOFError: if the stream has ended.

        """
    def feed_eof(self) -> None:
        """
        End the stream.

        :meth:`feed_eof` cannot be called more than once.

        Raises:
            EOFError: if the stream has ended.

        """
    def discard(self) -> None:
        """
        Discard all buffered data, but don't end the stream.

        """
