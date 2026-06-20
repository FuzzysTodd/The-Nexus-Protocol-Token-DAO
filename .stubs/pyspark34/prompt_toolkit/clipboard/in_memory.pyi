from .base import Clipboard, ClipboardData
from _typeshed import Incomplete

__all__ = ['InMemoryClipboard']

class InMemoryClipboard(Clipboard):
    """
    Default clipboard implementation.
    Just keep the data in memory.

    This implements a kill-ring, for Emacs mode.
    """
    max_size: Incomplete
    def __init__(self, data: ClipboardData | None = None, max_size: int = 60) -> None: ...
    def set_data(self, data: ClipboardData) -> None: ...
    def get_data(self) -> ClipboardData: ...
    def rotate(self) -> None: ...
