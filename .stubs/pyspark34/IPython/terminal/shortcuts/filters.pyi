from _typeshed import Incomplete
from prompt_toolkit.filters import Filter
from prompt_toolkit.key_binding import KeyPressEvent

__all__ = ['KEYBINDING_FILTERS', 'filter_from_string']

class PassThrough(Filter):
    """A filter allowing to implement pass-through behaviour of keybindings.

    Prompt toolkit key processor dispatches only one event per binding match,
    which means that adding a new shortcut will suppress the old shortcut
    if the keybindings are the same (unless one is filtered out).

    To stop a shortcut binding from suppressing other shortcuts:
    - add the `pass_through` filter to list of filter, and
    - call `pass_through.reply(event)` in the shortcut handler.
    """
    def __init__(self) -> None: ...
    def reply(self, event: KeyPressEvent): ...
    def __call__(self): ...

KEYBINDING_FILTERS: Incomplete

def filter_from_string(code: str): ...
