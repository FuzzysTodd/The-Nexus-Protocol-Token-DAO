from _typeshed import Incomplete
from ctypes import Structure, Union

STD_INPUT_HANDLE: Incomplete
STD_OUTPUT_HANDLE: Incomplete
STD_ERROR_HANDLE: Incomplete

class COORD(Structure):
    """
    Struct in wincon.h
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms682119(v=vs.85).aspx
    """
    X: int
    Y: int

class UNICODE_OR_ASCII(Union):
    AsciiChar: bytes
    UnicodeChar: str

class KEY_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms684166(v=vs.85).aspx
    """
    KeyDown: int
    RepeatCount: int
    VirtualKeyCode: int
    VirtualScanCode: int
    uChar: UNICODE_OR_ASCII
    ControlKeyState: int

class MOUSE_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms684239(v=vs.85).aspx
    """
    MousePosition: COORD
    ButtonState: int
    ControlKeyState: int
    EventFlags: int

class WINDOW_BUFFER_SIZE_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms687093(v=vs.85).aspx
    """
    Size: COORD

class MENU_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms684213(v=vs.85).aspx
    """
    CommandId: int

class FOCUS_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms683149(v=vs.85).aspx
    """
    SetFocus: int

class EVENT_RECORD(Union):
    KeyEvent: KEY_EVENT_RECORD
    MouseEvent: MOUSE_EVENT_RECORD
    WindowBufferSizeEvent: WINDOW_BUFFER_SIZE_RECORD
    MenuEvent: MENU_EVENT_RECORD
    FocusEvent: FOCUS_EVENT_RECORD

class INPUT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms683499(v=vs.85).aspx
    """
    EventType: int
    Event: EVENT_RECORD

EventTypes: Incomplete

class SMALL_RECT(Structure):
    """struct in wincon.h."""
    Left: int
    Top: int
    Right: int
    Bottom: int

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    """struct in wincon.h."""
    dwSize: COORD
    dwCursorPosition: COORD
    wAttributes: int
    srWindow: SMALL_RECT
    dwMaximumWindowSize: COORD

class SECURITY_ATTRIBUTES(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa379560(v=vs.85).aspx
    """
    nLength: int
    lpSecurityDescriptor: int
    bInheritHandle: int
