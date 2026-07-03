from _typeshed import Incomplete
from ctypes import LibraryLoader as LibraryLoader
from dataclasses import dataclass
from rich._win32_console import ENABLE_VIRTUAL_TERMINAL_PROCESSING as ENABLE_VIRTUAL_TERMINAL_PROCESSING, GetConsoleMode as GetConsoleMode, GetStdHandle as GetStdHandle, LegacyWindowsError as LegacyWindowsError

@dataclass
class WindowsConsoleFeatures:
    """Windows features available."""
    vt: bool = ...
    truecolor: bool = ...
    def __init__(self, vt, truecolor) -> None: ...

windll: Incomplete

def get_windows_console_features() -> WindowsConsoleFeatures: ...
