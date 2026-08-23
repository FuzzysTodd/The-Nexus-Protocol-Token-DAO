from .data_structures import Point
from _typeshed import Incomplete
from enum import Enum

__all__ = ['MouseEventType', 'MouseButton', 'MouseModifier', 'MouseEvent']

class MouseEventType(Enum):
    MOUSE_UP: str
    MOUSE_DOWN: str
    SCROLL_UP: str
    SCROLL_DOWN: str
    MOUSE_MOVE: str

class MouseButton(Enum):
    LEFT: str
    MIDDLE: str
    RIGHT: str
    NONE: str
    UNKNOWN: str

class MouseModifier(Enum):
    SHIFT: str
    ALT: str
    CONTROL: str

class MouseEvent:
    """
    Mouse event, sent to `UIControl.mouse_handler`.

    :param position: `Point` instance.
    :param event_type: `MouseEventType`.
    """
    position: Incomplete
    event_type: Incomplete
    button: Incomplete
    modifiers: Incomplete
    def __init__(self, position: Point, event_type: MouseEventType, button: MouseButton, modifiers: frozenset[MouseModifier]) -> None: ...
