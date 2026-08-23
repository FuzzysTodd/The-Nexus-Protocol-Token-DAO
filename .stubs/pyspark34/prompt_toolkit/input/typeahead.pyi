from ..key_binding import KeyPress
from .base import Input

__all__ = ['store_typeahead', 'get_typeahead', 'clear_typeahead']

def store_typeahead(input_obj: Input, key_presses: list[KeyPress]) -> None:
    """
    Insert typeahead key presses for the given input.
    """
def get_typeahead(input_obj: Input) -> list[KeyPress]:
    """
    Retrieve typeahead and reset the buffer for this input.
    """
def clear_typeahead(input_obj: Input) -> None:
    """
    Clear typeahead buffer.
    """
