from .trait_types import TypedTuple as TypedTuple
from .widget import register as register
from .widget_box import Box as Box
from .widget_core import CoreWidget as CoreWidget
from _typeshed import Incomplete
from traitlets import Dict as Dict

def pad(iterable, padding: Incomplete | None = None, length: Incomplete | None = None):
    """Returns the sequence elements and then returns None up to the given size (or indefinitely if size is None)."""

class _SelectionContainer(Box, CoreWidget):
    """Base class used to display multiple child widgets."""
    titles: Incomplete
    selected_index: Incomplete
    def set_title(self, index, title) -> None:
        """Sets the title of a container page.
        Parameters
        ----------
        index : int
            Index of the container page
        title : unicode
            New title
        """
    def get_title(self, index):
        """Gets the title of a container page.
        Parameters
        ----------
        index : int
            Index of the container page
        """

class Accordion(_SelectionContainer):
    """Displays children each on a separate accordion page."""

class Tab(_SelectionContainer):
    """Displays children each on a separate accordion tab."""
    def __init__(self, children=(), **kwargs) -> None: ...

class Stack(_SelectionContainer):
    """Displays only the selected child."""
