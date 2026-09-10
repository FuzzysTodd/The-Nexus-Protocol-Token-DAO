from ..frames import Frame
from ..typing import Data
from _typeshed import Incomplete
from typing import Iterator

__all__ = ['Assembler']

class Assembler:
    """
    Assemble messages from frames.

    """
    mutex: Incomplete
    message_complete: Incomplete
    message_fetched: Incomplete
    get_in_progress: bool
    put_in_progress: bool
    decoder: Incomplete
    chunks: Incomplete
    chunks_queue: Incomplete
    closed: bool
    def __init__(self) -> None: ...
    def get(self, timeout: float | None = None) -> Data:
        """
        Read the next message.

        :meth:`get` returns a single :class:`str` or :class:`bytes`.

        If the message is fragmented, :meth:`get` waits until the last frame is
        received, then it reassembles the message and returns it. To receive
        messages frame by frame, use :meth:`get_iter` instead.

        Args:
            timeout: If a timeout is provided and elapses before a complete
                message is received, :meth:`get` raises :exc:`TimeoutError`.

        Raises:
            EOFError: If the stream of frames has ended.
            RuntimeError: If two threads run :meth:`get` or :meth:``get_iter`
                concurrently.

        """
    def get_iter(self) -> Iterator[Data]:
        """
        Stream the next message.

        Iterating the return value of :meth:`get_iter` yields a :class:`str` or
        :class:`bytes` for each frame in the message.

        The iterator must be fully consumed before calling :meth:`get_iter` or
        :meth:`get` again. Else, :exc:`RuntimeError` is raised.

        This method only makes sense for fragmented messages. If messages aren't
        fragmented, use :meth:`get` instead.

        Raises:
            EOFError: If the stream of frames has ended.
            RuntimeError: If two threads run :meth:`get` or :meth:``get_iter`
                concurrently.

        """
    def put(self, frame: Frame) -> None:
        """
        Add ``frame`` to the next message.

        When ``frame`` is the final frame in a message, :meth:`put` waits until
        the message is fetched, either by calling :meth:`get` or by fully
        consuming the return value of :meth:`get_iter`.

        :meth:`put` assumes that the stream of frames respects the protocol. If
        it doesn't, the behavior is undefined.

        Raises:
            EOFError: If the stream of frames has ended.
            RuntimeError: If two threads run :meth:`put` concurrently.

        """
    def close(self) -> None:
        """
        End the stream of frames.

        Callling :meth:`close` concurrently with :meth:`get`, :meth:`get_iter`,
        or :meth:`put` is safe. They will raise :exc:`EOFError`.

        """
