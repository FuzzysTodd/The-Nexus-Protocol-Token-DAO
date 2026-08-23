from ..key_binding.key_processor import KeyPress
from _typeshed import Incomplete
from typing import Callable, Dict

__all__ = ['Vt100Parser']

class _Flush:
    """Helper object to indicate flush operation to the parser."""

class _IsPrefixOfLongerMatchCache(Dict[str, bool]):
    """
    Dictionary that maps input sequences to a boolean indicating whether there is
    any key that start with this characters.
    """
    def __missing__(self, prefix: str) -> bool: ...

class Vt100Parser:
    """
    Parser for VT100 input stream.
    Data can be fed through the `feed` method and the given callback will be
    called with KeyPress objects.

    ::

        def callback(key):
            pass
        i = Vt100Parser(callback)
        i.feed('data\x01...')

    :attr feed_key_callback: Function that will be called when a key is parsed.
    """
    feed_key_callback: Incomplete
    def __init__(self, feed_key_callback: Callable[[KeyPress], None]) -> None: ...
    def reset(self, request: bool = False) -> None: ...
    def feed(self, data: str) -> None:
        """
        Feed the input stream.

        :param data: Input string (unicode).
        """
    def flush(self) -> None:
        """
        Flush the buffer of the input stream.

        This will allow us to handle the escape key (or maybe meta) sooner.
        The input received by the escape key is actually the same as the first
        characters of e.g. Arrow-Up, so without knowing what follows the escape
        sequence, we don't know whether escape has been pressed, or whether
        it's something else. This flush function should be called after a
        timeout, and processes everything that's still in the buffer as-is, so
        without assuming any characters will follow.
        """
    def feed_and_flush(self, data: str) -> None:
        """
        Wrapper around ``feed`` and ``flush``.
        """
