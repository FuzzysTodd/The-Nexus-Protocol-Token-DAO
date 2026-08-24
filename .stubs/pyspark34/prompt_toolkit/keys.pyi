from enum import Enum

__all__ = ['Keys', 'ALL_KEYS']

class Keys(str, Enum):
    '''
    List of keys for use in key bindings.

    Note that this is an "StrEnum", all values can be compared against
    strings.
    '''
    value: str
    Escape: str
    ShiftEscape: str
    ControlAt: str
    ControlA: str
    ControlB: str
    ControlC: str
    ControlD: str
    ControlE: str
    ControlF: str
    ControlG: str
    ControlH: str
    ControlI: str
    ControlJ: str
    ControlK: str
    ControlL: str
    ControlM: str
    ControlN: str
    ControlO: str
    ControlP: str
    ControlQ: str
    ControlR: str
    ControlS: str
    ControlT: str
    ControlU: str
    ControlV: str
    ControlW: str
    ControlX: str
    ControlY: str
    ControlZ: str
    Control1: str
    Control2: str
    Control3: str
    Control4: str
    Control5: str
    Control6: str
    Control7: str
    Control8: str
    Control9: str
    Control0: str
    ControlShift1: str
    ControlShift2: str
    ControlShift3: str
    ControlShift4: str
    ControlShift5: str
    ControlShift6: str
    ControlShift7: str
    ControlShift8: str
    ControlShift9: str
    ControlShift0: str
    ControlBackslash: str
    ControlSquareClose: str
    ControlCircumflex: str
    ControlUnderscore: str
    Left: str
    Right: str
    Up: str
    Down: str
    Home: str
    End: str
    Insert: str
    Delete: str
    PageUp: str
    PageDown: str
    ControlLeft: str
    ControlRight: str
    ControlUp: str
    ControlDown: str
    ControlHome: str
    ControlEnd: str
    ControlInsert: str
    ControlDelete: str
    ControlPageUp: str
    ControlPageDown: str
    ShiftLeft: str
    ShiftRight: str
    ShiftUp: str
    ShiftDown: str
    ShiftHome: str
    ShiftEnd: str
    ShiftInsert: str
    ShiftDelete: str
    ShiftPageUp: str
    ShiftPageDown: str
    ControlShiftLeft: str
    ControlShiftRight: str
    ControlShiftUp: str
    ControlShiftDown: str
    ControlShiftHome: str
    ControlShiftEnd: str
    ControlShiftInsert: str
    ControlShiftDelete: str
    ControlShiftPageUp: str
    ControlShiftPageDown: str
    BackTab: str
    F1: str
    F2: str
    F3: str
    F4: str
    F5: str
    F6: str
    F7: str
    F8: str
    F9: str
    F10: str
    F11: str
    F12: str
    F13: str
    F14: str
    F15: str
    F16: str
    F17: str
    F18: str
    F19: str
    F20: str
    F21: str
    F22: str
    F23: str
    F24: str
    ControlF1: str
    ControlF2: str
    ControlF3: str
    ControlF4: str
    ControlF5: str
    ControlF6: str
    ControlF7: str
    ControlF8: str
    ControlF9: str
    ControlF10: str
    ControlF11: str
    ControlF12: str
    ControlF13: str
    ControlF14: str
    ControlF15: str
    ControlF16: str
    ControlF17: str
    ControlF18: str
    ControlF19: str
    ControlF20: str
    ControlF21: str
    ControlF22: str
    ControlF23: str
    ControlF24: str
    Any: str
    ScrollUp: str
    ScrollDown: str
    CPRResponse: str
    Vt100MouseEvent: str
    WindowsMouseEvent: str
    BracketedPaste: str
    SIGINT: str
    Ignore: str
    ControlSpace = ControlAt
    Tab = ControlI
    Enter = ControlM
    Backspace = ControlH
    ShiftControlLeft = ControlShiftLeft
    ShiftControlRight = ControlShiftRight
    ShiftControlHome = ControlShiftHome
    ShiftControlEnd = ControlShiftEnd

ALL_KEYS: list[str]
