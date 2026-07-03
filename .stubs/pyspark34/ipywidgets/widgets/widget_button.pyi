from .domwidget import DOMWidget as DOMWidget
from .trait_types import Color as Color, InstanceDict as InstanceDict
from .utils import deprecation as deprecation
from .widget import CallbackDispatcher as CallbackDispatcher, register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from .widget_style import Style as Style
from _typeshed import Incomplete
from traitlets import Instance as Instance, default as default

class ButtonStyle(Style, CoreWidget):
    """Button style widget."""
    button_color: Incomplete
    font_family: Incomplete
    font_size: Incomplete
    font_style: Incomplete
    font_variant: Incomplete
    font_weight: Incomplete
    text_color: Incomplete
    text_decoration: Incomplete

class Button(DOMWidget, CoreWidget):
    """Button widget.

    This widget has an `on_click` method that allows you to listen for the
    user clicking on the button.  The click event itself is stateless.

    Parameters
    ----------
    description: str
       description displayed on the button
    icon: str
       font-awesome icon names, without the 'fa-' prefix
    disabled: bool
       whether user interaction is enabled
    """
    description: Incomplete
    disabled: Incomplete
    icon: Incomplete
    button_style: Incomplete
    style: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def on_click(self, callback, remove: bool = False) -> None:
        """Register a callback to execute when the button is clicked.

        The callback will be called with one argument, the clicked button
        widget instance.

        Parameters
        ----------
        remove: bool (optional)
            Set to true to remove the callback from the list of callbacks.
        """
    def click(self) -> None:
        """Programmatically trigger a click event.

        This will call the callbacks registered to the clicked button
        widget instance.
        """
