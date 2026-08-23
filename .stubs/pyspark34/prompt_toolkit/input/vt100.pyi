from ..key_binding import KeyPress
from .base import Input
from _typeshed import Incomplete
from typing import Callable, ContextManager, TextIO

__all__ = ['Vt100Input', 'raw_mode', 'cooked_mode']

class Vt100Input(Input):
    """
    Vt100 input for Posix systems.
    (This uses a posix file descriptor that can be registered in the event loop.)
    """
    stdin: Incomplete
    stdin_reader: Incomplete
    vt100_parser: Incomplete
    def __init__(self, stdin: TextIO) -> None: ...
    def attach(self, input_ready_callback: Callable[[], None]) -> ContextManager[None]:
        """
        Return a context manager that makes this input active in the current
        event loop.
        """
    def detach(self) -> ContextManager[None]:
        """
        Return a context manager that makes sure that this input is not active
        in the current event loop.
        """
    def read_keys(self) -> list[KeyPress]:
        """Read list of KeyPress."""
    def flush_keys(self) -> list[KeyPress]:
        """
        Flush pending keys and return them.
        (Used for flushing the 'escape' key.)
        """
    @property
    def closed(self) -> bool: ...
    def raw_mode(self) -> ContextManager[None]: ...
    def cooked_mode(self) -> ContextManager[None]: ...
    def fileno(self) -> int: ...
    def typeahead_hash(self) -> str: ...

class raw_mode:
    """
    ::

        with raw_mode(stdin):
            ''' the pseudo-terminal stdin is now used in raw mode '''

    We ignore errors when executing `tcgetattr` fails.
    """
    fileno: Incomplete
    attrs_before: Incomplete
    def __init__(self, fileno: int) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *a: object) -> None: ...

class cooked_mode(raw_mode):
    """
    The opposite of ``raw_mode``, used when we need cooked mode inside a
    `raw_mode` block.  Used in `Application.run_in_terminal`.::

        with cooked_mode(stdin):
            ''' the pseudo-terminal stdin is now used in cooked mode. '''
    """
