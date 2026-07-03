import typing
from . import copying

__all__ = ['Base']

class LineIterable:
    """Iterable of DOT Source code lines
        (mimics ``file`` objects in text mode)."""
    def __iter__(self) -> typing.Iterator[str]:
        """Yield the generated DOT source line by line.

        Yields: Line ending with a newline (``'\\n'``).
        """

class Base(LineIterable, copying.CopyBase):
    """LineIterator with ``.source`` attribute, that it returns for ``str()``."""
    @property
    def source(self) -> str: ...
