from _typeshed import Incomplete
from enum import Enum

__all__ = ['SelectionType', 'PasteMode', 'SelectionState']

class SelectionType(Enum):
    """
    Type of selection.
    """
    CHARACTERS: str
    LINES: str
    BLOCK: str

class PasteMode(Enum):
    EMACS: str
    VI_AFTER: str
    VI_BEFORE: str

class SelectionState:
    """
    State of the current selection.

    :param original_cursor_position: int
    :param type: :class:`~.SelectionType`
    """
    original_cursor_position: Incomplete
    type: Incomplete
    shift_mode: bool
    def __init__(self, original_cursor_position: int = 0, type: SelectionType = ...) -> None: ...
    def enter_shift_mode(self) -> None: ...
