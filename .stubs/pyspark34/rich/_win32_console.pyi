import ctypes
from _typeshed import Incomplete
from ctypes import Structure, wintypes
from rich.color import ColorSystem as ColorSystem
from rich.style import Style as Style
from typing import Any, IO, NamedTuple

windll: Any
STDOUT: int
ENABLE_VIRTUAL_TERMINAL_PROCESSING: int
COORD: Incomplete

class LegacyWindowsError(Exception): ...

class WindowsCoordinates(NamedTuple):
    """Coordinates in the Windows Console API are (y, x), not (x, y).
    This class is intended to prevent that confusion.
    Rows and columns are indexed from 0.
    This class can be used in place of wintypes._COORD in arguments and argtypes.
    """
    row: int
    col: int
    @classmethod
    def from_param(cls, value: WindowsCoordinates) -> COORD:
        """Converts a WindowsCoordinates into a wintypes _COORD structure.
        This classmethod is internally called by ctypes to perform the conversion.

        Args:
            value (WindowsCoordinates): The input coordinates to convert.

        Returns:
            wintypes._COORD: The converted coordinates struct.
        """

class CONSOLE_SCREEN_BUFFER_INFO(Structure): ...
class CONSOLE_CURSOR_INFO(ctypes.Structure): ...

def GetStdHandle(handle: int = ...) -> wintypes.HANDLE:
    """Retrieves a handle to the specified standard device (standard input, standard output, or standard error).

    Args:
        handle (int): Integer identifier for the handle. Defaults to -11 (stdout).

    Returns:
        wintypes.HANDLE: The handle
    """
def GetConsoleMode(std_handle: wintypes.HANDLE) -> int:
    """Retrieves the current input mode of a console's input buffer
    or the current output mode of a console screen buffer.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.

    Raises:
        LegacyWindowsError: If any error occurs while calling the Windows console API.

    Returns:
        int: Value representing the current console mode as documented at
            https://docs.microsoft.com/en-us/windows/console/getconsolemode#parameters
    """
def FillConsoleOutputCharacter(std_handle: wintypes.HANDLE, char: str, length: int, start: WindowsCoordinates) -> int:
    """Writes a character to the console screen buffer a specified number of times, beginning at the specified coordinates.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        char (str): The character to write. Must be a string of length 1.
        length (int): The number of times to write the character.
        start (WindowsCoordinates): The coordinates to start writing at.

    Returns:
        int: The number of characters written.
    """
def FillConsoleOutputAttribute(std_handle: wintypes.HANDLE, attributes: int, length: int, start: WindowsCoordinates) -> int:
    """Sets the character attributes for a specified number of character cells,
    beginning at the specified coordinates in a screen buffer.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        attributes (int): Integer value representing the foreground and background colours of the cells.
        length (int): The number of cells to set the output attribute of.
        start (WindowsCoordinates): The coordinates of the first cell whose attributes are to be set.

    Returns:
        int: The number of cells whose attributes were actually set.
    """
def SetConsoleTextAttribute(std_handle: wintypes.HANDLE, attributes: wintypes.WORD) -> bool:
    """Set the colour attributes for all text written after this function is called.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        attributes (int): Integer value representing the foreground and background colours.


    Returns:
        bool: True if the attribute was set successfully, otherwise False.
    """
def GetConsoleScreenBufferInfo(std_handle: wintypes.HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
    """Retrieves information about the specified console screen buffer.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.

    Returns:
        CONSOLE_SCREEN_BUFFER_INFO: A CONSOLE_SCREEN_BUFFER_INFO ctype struct contain information about
            screen size, cursor position, colour attributes, and more."""
def SetConsoleCursorPosition(std_handle: wintypes.HANDLE, coords: WindowsCoordinates) -> bool:
    """Set the position of the cursor in the console screen

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        coords (WindowsCoordinates): The coordinates to move the cursor to.

    Returns:
        bool: True if the function succeeds, otherwise False.
    """
def GetConsoleCursorInfo(std_handle: wintypes.HANDLE, cursor_info: CONSOLE_CURSOR_INFO) -> bool:
    """Get the cursor info - used to get cursor visibility and width

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        cursor_info (CONSOLE_CURSOR_INFO): CONSOLE_CURSOR_INFO ctype struct that receives information
            about the console's cursor.

    Returns:
          bool: True if the function succeeds, otherwise False.
    """
def SetConsoleCursorInfo(std_handle: wintypes.HANDLE, cursor_info: CONSOLE_CURSOR_INFO) -> bool:
    """Set the cursor info - used for adjusting cursor visibility and width

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        cursor_info (CONSOLE_CURSOR_INFO): CONSOLE_CURSOR_INFO ctype struct containing the new cursor info.

    Returns:
          bool: True if the function succeeds, otherwise False.
    """
def SetConsoleTitle(title: str) -> bool:
    """Sets the title of the current console window

    Args:
        title (str): The new title of the console window.

    Returns:
        bool: True if the function succeeds, otherwise False.
    """

class LegacyWindowsTerm:
    """This class allows interaction with the legacy Windows Console API. It should only be used in the context
    of environments where virtual terminal processing is not available. However, if it is used in a Windows environment,
    the entire API should work.

    Args:
        file (IO[str]): The file which the Windows Console API HANDLE is retrieved from, defaults to sys.stdout.
    """
    BRIGHT_BIT: int
    ANSI_TO_WINDOWS: Incomplete
    write: Incomplete
    flush: Incomplete
    def __init__(self, file: IO[str]) -> None: ...
    @property
    def cursor_position(self) -> WindowsCoordinates:
        """Returns the current position of the cursor (0-based)

        Returns:
            WindowsCoordinates: The current cursor position.
        """
    @property
    def screen_size(self) -> WindowsCoordinates:
        """Returns the current size of the console screen buffer, in character columns and rows

        Returns:
            WindowsCoordinates: The width and height of the screen as WindowsCoordinates.
        """
    def write_text(self, text: str) -> None:
        """Write text directly to the terminal without any modification of styles

        Args:
            text (str): The text to write to the console
        """
    def write_styled(self, text: str, style: Style) -> None:
        """Write styled text to the terminal.

        Args:
            text (str): The text to write
            style (Style): The style of the text
        """
    def move_cursor_to(self, new_position: WindowsCoordinates) -> None:
        """Set the position of the cursor

        Args:
            new_position (WindowsCoordinates): The WindowsCoordinates representing the new position of the cursor.
        """
    def erase_line(self) -> None:
        """Erase all content on the line the cursor is currently located at"""
    def erase_end_of_line(self) -> None:
        """Erase all content from the cursor position to the end of that line"""
    def erase_start_of_line(self) -> None:
        """Erase all content from the cursor position to the start of that line"""
    def move_cursor_up(self) -> None:
        """Move the cursor up a single cell"""
    def move_cursor_down(self) -> None:
        """Move the cursor down a single cell"""
    def move_cursor_forward(self) -> None:
        """Move the cursor forward a single cell. Wrap to the next line if required."""
    def move_cursor_to_column(self, column: int) -> None:
        """Move cursor to the column specified by the zero-based column index, staying on the same row

        Args:
            column (int): The zero-based column index to move the cursor to.
        """
    def move_cursor_backward(self) -> None:
        """Move the cursor backward a single cell. Wrap to the previous line if required."""
    def hide_cursor(self) -> None:
        """Hide the cursor"""
    def show_cursor(self) -> None:
        """Show the cursor"""
    def set_title(self, title: str) -> None:
        """Set the title of the terminal window

        Args:
            title (str): The new title of the console window
        """
