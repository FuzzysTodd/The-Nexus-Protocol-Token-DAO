from rich._win32_console import LegacyWindowsTerm as LegacyWindowsTerm, WindowsCoordinates as WindowsCoordinates
from rich.segment import ControlCode as ControlCode, ControlType as ControlType, Segment as Segment
from typing import Iterable

def legacy_windows_render(buffer: Iterable[Segment], term: LegacyWindowsTerm) -> None:
    """Makes appropriate Windows Console API calls based on the segments in the buffer.

    Args:
        buffer (Iterable[Segment]): Iterable of Segments to convert to Win32 API calls.
        term (LegacyWindowsTerm): Used to call the Windows Console API.
    """
