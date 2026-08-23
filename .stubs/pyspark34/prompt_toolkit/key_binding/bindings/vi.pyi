from ..key_bindings import KeyBindingsBase
from _typeshed import Incomplete
from enum import Enum
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.clipboard import ClipboardData
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.selection import SelectionType
from typing import Callable

__all__ = ['load_vi_bindings', 'load_vi_search_bindings']

E = KeyPressEvent

class TextObjectType(Enum):
    EXCLUSIVE: str
    INCLUSIVE: str
    LINEWISE: str
    BLOCK: str

class TextObject:
    """
    Return struct for functions wrapped in ``text_object``.
    Both `start` and `end` are relative to the current cursor position.
    """
    start: Incomplete
    end: Incomplete
    type: Incomplete
    def __init__(self, start: int, end: int = 0, type: TextObjectType = ...) -> None: ...
    @property
    def selection_type(self) -> SelectionType: ...
    def sorted(self) -> tuple[int, int]:
        """
        Return a (start, end) tuple where start <= end.
        """
    def operator_range(self, document: Document) -> tuple[int, int]:
        """
        Return a (start, end) tuple with start <= end that indicates the range
        operators should operate on.
        `buffer` is used to get start and end of line positions.

        This should return something that can be used in a slice, so the `end`
        position is *not* included.
        """
    def get_line_numbers(self, buffer: Buffer) -> tuple[int, int]:
        """
        Return a (start_line, end_line) pair.
        """
    def cut(self, buffer: Buffer) -> tuple[Document, ClipboardData]:
        """
        Turn text object into `ClipboardData` instance.
        """
TextObjectFunction = Callable[[E], TextObject]
OperatorFunction = Callable[[E, TextObject], None]

def load_vi_bindings() -> KeyBindingsBase:
    """
    Vi extensions.

    # Overview of Readline Vi commands:
    # http://www.catonmat.net/download/bash-vi-editing-mode-cheat-sheet.pdf
    """
def load_vi_search_bindings() -> KeyBindingsBase: ...
