from .base import PipeInput
from .vt100 import Vt100Input
from _typeshed import Incomplete
from typing import ContextManager, Iterator

__all__ = ['PosixPipeInput']

class _Pipe:
    """Wrapper around os.pipe, that ensures we don't double close any end."""
    def __init__(self) -> None: ...
    def close_read(self) -> None:
        """Close read-end if not yet closed."""
    def close_write(self) -> None:
        """Close write-end if not yet closed."""
    def close(self) -> None:
        """Close both read and write ends."""

class PosixPipeInput(Vt100Input, PipeInput):
    """
    Input that is send through a pipe.
    This is useful if we want to send the input programmatically into the
    application. Mostly useful for unit testing.

    Usage::

        with PosixPipeInput.create() as input:
            input.send_text('inputdata')
    """
    pipe: Incomplete
    def __init__(self, _pipe: _Pipe, _text: str = '') -> None: ...
    @classmethod
    def create(cls, text: str = '') -> Iterator[PosixPipeInput]: ...
    def send_bytes(self, data: bytes) -> None: ...
    def send_text(self, data: str) -> None:
        """Send text to the input."""
    def raw_mode(self) -> ContextManager[None]: ...
    def cooked_mode(self) -> ContextManager[None]: ...
    def close(self) -> None:
        """Close pipe fds."""
    def typeahead_hash(self) -> str:
        """
        This needs to be unique for every `PipeInput`.
        """
