from .filters import pass_through as pass_through
from IPython.core.getipython import get_ipython as get_ipython
from IPython.utils.tokenutil import generate_tokens as generate_tokens
from _typeshed import Incomplete
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory, Suggestion
from prompt_toolkit.buffer import Buffer as Buffer
from prompt_toolkit.document import Document as Document
from prompt_toolkit.history import History as History
from prompt_toolkit.key_binding import KeyPressEvent as KeyPressEvent
from prompt_toolkit.layout.processors import Processor, Transformation, TransformationInput as TransformationInput
from prompt_toolkit.shortcuts import PromptSession as PromptSession

class AppendAutoSuggestionInAnyLine(Processor):
    """
    Append the auto suggestion to lines other than the last (appending to the
    last line is natively supported by the prompt toolkit).
    """
    style: Incomplete
    def __init__(self, style: str = 'class:auto-suggestion') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class NavigableAutoSuggestFromHistory(AutoSuggestFromHistory):
    """
    A subclass of AutoSuggestFromHistory that allow navigation to next/previous
    suggestion from history. To do so it remembers the current position, but it
    state need to carefully be cleared on the right events.
    """
    skip_lines: int
    def __init__(self) -> None: ...
    def reset_history_position(self, _: Buffer): ...
    def disconnect(self) -> None: ...
    def connect(self, pt_app: PromptSession): ...
    def get_suggestion(self, buffer: Buffer, document: Document) -> Suggestion | None: ...
    def up(self, query: str, other_than: str, history: History) -> None: ...
    def down(self, query: str, other_than: str, history: History) -> None: ...

def accept_or_jump_to_end(event: KeyPressEvent):
    """Apply autosuggestion or jump to end of line."""
def accept(event: KeyPressEvent):
    """Accept autosuggestion"""
def discard(event: KeyPressEvent):
    """Discard autosuggestion"""
def accept_word(event: KeyPressEvent):
    """Fill partial autosuggestion by word"""
def accept_character(event: KeyPressEvent):
    """Fill partial autosuggestion by character"""
def accept_and_keep_cursor(event: KeyPressEvent):
    """Accept autosuggestion and keep cursor in place"""
def accept_and_move_cursor_left(event: KeyPressEvent):
    """Accept autosuggestion and move cursor left in place"""
def backspace_and_resume_hint(event: KeyPressEvent):
    """Resume autosuggestions after deleting last character"""
def resume_hinting(event: KeyPressEvent):
    """Resume autosuggestions"""
def up_and_update_hint(event: KeyPressEvent):
    """Go up and update hint"""
def down_and_update_hint(event: KeyPressEvent):
    """Go down and update hint"""
def accept_token(event: KeyPressEvent):
    """Fill partial autosuggestion by token"""
Provider = AutoSuggestFromHistory | NavigableAutoSuggestFromHistory | None

def swap_autosuggestion_up(event: KeyPressEvent):
    """Get next autosuggestion from history."""
def swap_autosuggestion_down(event: KeyPressEvent):
    """Get previous autosuggestion from history."""
def __getattr__(key): ...
