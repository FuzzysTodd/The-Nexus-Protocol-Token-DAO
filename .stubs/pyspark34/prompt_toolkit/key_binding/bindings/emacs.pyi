from ..key_bindings import KeyBindingsBase
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['load_emacs_bindings', 'load_emacs_search_bindings', 'load_emacs_shift_selection_bindings']

E = KeyPressEvent

def load_emacs_bindings() -> KeyBindingsBase:
    """
    Some e-macs extensions.
    """
def load_emacs_search_bindings() -> KeyBindingsBase: ...
def load_emacs_shift_selection_bindings() -> KeyBindingsBase:
    """
    Bindings to select text with shift + cursor movements
    """
