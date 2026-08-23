from prompt_toolkit.key_binding.key_bindings import KeyBindingsBase

__all__ = ['load_key_bindings']

def load_key_bindings() -> KeyBindingsBase:
    """
    Create a KeyBindings object that contains the default key bindings.
    """
