from .layout import Layout
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['create_dummy_layout']

E = KeyPressEvent

def create_dummy_layout() -> Layout:
    """
    Create a dummy layout for use in an 'Application' that doesn't have a
    layout specified. When ENTER is pressed, the application quits.
    """
