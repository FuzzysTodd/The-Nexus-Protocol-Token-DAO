from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from prompt_toolkit.selection import SelectionType
from typing import Callable

__all__ = ['Clipboard', 'ClipboardData', 'DummyClipboard', 'DynamicClipboard']

class ClipboardData:
    """
    Text on the clipboard.

    :param text: string
    :param type: :class:`~prompt_toolkit.selection.SelectionType`
    """
    text: Incomplete
    type: Incomplete
    def __init__(self, text: str = '', type: SelectionType = ...) -> None: ...

class Clipboard(metaclass=ABCMeta):
    """
    Abstract baseclass for clipboards.
    (An implementation can be in memory, it can share the X11 or Windows
    keyboard, or can be persistent.)
    """
    @abstractmethod
    def set_data(self, data: ClipboardData) -> None:
        """
        Set data to the clipboard.

        :param data: :class:`~.ClipboardData` instance.
        """
    def set_text(self, text: str) -> None:
        """
        Shortcut for setting plain text on clipboard.
        """
    def rotate(self) -> None:
        """
        For Emacs mode, rotate the kill ring.
        """
    @abstractmethod
    def get_data(self) -> ClipboardData:
        """
        Return clipboard data.
        """

class DummyClipboard(Clipboard):
    """
    Clipboard implementation that doesn't remember anything.
    """
    def set_data(self, data: ClipboardData) -> None: ...
    def set_text(self, text: str) -> None: ...
    def rotate(self) -> None: ...
    def get_data(self) -> ClipboardData: ...

class DynamicClipboard(Clipboard):
    """
    Clipboard class that can dynamically returns any Clipboard.

    :param get_clipboard: Callable that returns a :class:`.Clipboard` instance.
    """
    get_clipboard: Incomplete
    def __init__(self, get_clipboard: Callable[[], Clipboard | None]) -> None: ...
    def set_data(self, data: ClipboardData) -> None: ...
    def set_text(self, text: str) -> None: ...
    def rotate(self) -> None: ...
    def get_data(self) -> ClipboardData: ...
