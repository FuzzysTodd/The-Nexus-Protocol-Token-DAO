from ..key_bindings import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['load_basic_bindings']

E = KeyPressEvent

def load_basic_bindings() -> KeyBindings: ...
