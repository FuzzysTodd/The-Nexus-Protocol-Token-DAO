from prompt_toolkit.key_binding.key_bindings import Binding
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['get_by_name']

E = KeyPressEvent

def get_by_name(name: str) -> Binding:
    """
    Return the handler for the (Readline) command with the given name.
    """
