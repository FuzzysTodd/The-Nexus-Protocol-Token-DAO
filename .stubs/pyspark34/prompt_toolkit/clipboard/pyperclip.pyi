from .base import Clipboard, ClipboardData

__all__ = ['PyperclipClipboard']

class PyperclipClipboard(Clipboard):
    """
    Clipboard that synchronizes with the Windows/Mac/Linux system clipboard,
    using the pyperclip module.
    """
    def __init__(self) -> None: ...
    def set_data(self, data: ClipboardData) -> None: ...
    def get_data(self) -> ClipboardData: ...
