from _typeshed import Incomplete
from ctypes import Structure

STDOUT: int
STDERR: int
ENABLE_VIRTUAL_TERMINAL_PROCESSING: int
windll: Incomplete
SetConsoleTextAttribute: Incomplete
winapi_test: Incomplete
COORD: Incomplete

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    """struct in wincon.h."""

def GetConsoleScreenBufferInfo(stream_id=...): ...
def SetConsoleCursorPosition(stream_id, position, adjust: bool = True): ...
def FillConsoleOutputCharacter(stream_id, char, length, start): ...
def FillConsoleOutputAttribute(stream_id, attr, length, start):
    """ FillConsoleOutputAttribute( hConsole, csbi.wAttributes, dwConSize, coordScreen, &cCharsWritten )"""
def SetConsoleTitle(title): ...
def GetConsoleMode(handle): ...
def SetConsoleMode(handle, mode) -> None: ...
