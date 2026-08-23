from ..key_bindings import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['load_mouse_bindings']

E = KeyPressEvent

def load_mouse_bindings() -> KeyBindings:
    """
    Key bindings, required for mouse support.
    (Mouse events enter through the key binding system.)
    """
