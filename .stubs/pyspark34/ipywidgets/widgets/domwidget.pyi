from .trait_types import InstanceDict as InstanceDict, TypedTuple as TypedTuple
from .widget import Widget as Widget, widget_serialization as widget_serialization
from .widget_layout import Layout as Layout
from .widget_style import Style as Style
from _typeshed import Incomplete

class DOMWidget(Widget):
    """Widget that can be inserted into the DOM

    Parameters
    ----------
    tooltip: str
       tooltip caption
    layout: InstanceDict(Layout)
       widget layout
    """
    tabbable: Incomplete
    tooltip: Incomplete
    layout: Incomplete
    def add_class(self, className):
        """
        Adds a class to the top level element of the widget.

        Doesn't add the class if it already exists.
        """
    def remove_class(self, className):
        """
        Removes a class from the top level element of the widget.

        Doesn't remove the class if it doesn't exist.
        """
    def focus(self) -> None:
        """
        Focus on the widget.
        """
    def blur(self) -> None:
        """
        Blur the widget.
        """
