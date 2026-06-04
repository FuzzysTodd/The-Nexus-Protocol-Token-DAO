from .base import BaseStyle
from .style import Style

__all__ = ['default_ui_style', 'default_pygments_style']

def default_ui_style() -> BaseStyle:
    """
    Create a default `Style` object.
    """
def default_pygments_style() -> Style:
    """
    Create a `Style` object that contains the default Pygments style.
    """
