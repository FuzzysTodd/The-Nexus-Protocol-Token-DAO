from .trait_types import Color as Color, InstanceDict as InstanceDict, TypedTuple as TypedTuple
from .utils import deprecation as deprecation
from .valuewidget import ValueWidget as ValueWidget
from .widget import CallbackDispatcher as CallbackDispatcher, register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionStyle as DescriptionStyle, DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete

class _StringStyle(DescriptionStyle, CoreWidget):
    """Text input style widget."""
    background: Incomplete
    font_size: Incomplete
    text_color: Incomplete

class LabelStyle(_StringStyle):
    """Label style widget."""
    font_family: Incomplete
    font_style: Incomplete
    font_variant: Incomplete
    font_weight: Incomplete
    text_decoration: Incomplete

class TextStyle(_StringStyle):
    """Text input style widget."""
class HTMLStyle(_StringStyle):
    """HTML style widget."""
class HTMLMathStyle(_StringStyle):
    """HTML with math style widget."""

class _String(DescriptionWidget, ValueWidget, CoreWidget):
    """Base class used to create widgets that represent a string."""
    value: Incomplete
    placeholder: Incomplete
    style: Incomplete
    def __init__(self, value: Incomplete | None = None, **kwargs) -> None: ...

class HTML(_String):
    """Renders the string `value` as HTML."""
    style: Incomplete

class HTMLMath(_String):
    """Renders the string `value` as HTML, and render mathematics."""
    style: Incomplete

class Label(_String):
    """Label widget.

    It also renders math inside the string `value` as Latex (requires $ $ or
    $$ $$ and similar latex tags).
    """
    style: Incomplete

class Textarea(_String):
    """Multiline text area widget."""
    rows: Incomplete
    disabled: Incomplete
    continuous_update: Incomplete
    style: Incomplete

class Text(_String):
    """Single line textbox widget."""
    disabled: Incomplete
    continuous_update: Incomplete
    style: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def on_submit(self, callback, remove: bool = False) -> None:
        """(Un)Register a callback to handle text submission.

        Triggered when the user clicks enter.

        Parameters
        ----------
        callback: callable
            Will be called with exactly one argument: the Widget instance
        remove: bool (optional)
            Whether to unregister the callback
        """

class Password(Text):
    """Single line textbox widget."""
    disabled: Incomplete

class Combobox(Text):
    """Single line textbox widget with a dropdown and autocompletion.
    """
    options: Incomplete
    ensure_option: Incomplete
