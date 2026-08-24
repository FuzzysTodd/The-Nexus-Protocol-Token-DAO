from .trait_types import Color as Color, InstanceDict as InstanceDict
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionStyle as DescriptionStyle, DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete

class CheckboxStyle(DescriptionStyle, CoreWidget):
    """Checkbox widget style."""
    background: Incomplete

class ToggleButtonStyle(DescriptionStyle, CoreWidget):
    """ToggleButton widget style."""
    font_family: Incomplete
    font_size: Incomplete
    font_style: Incomplete
    font_variant: Incomplete
    font_weight: Incomplete
    text_color: Incomplete
    text_decoration: Incomplete

class _Bool(DescriptionWidget, ValueWidget, CoreWidget):
    """A base class for creating widgets that represent booleans."""
    value: Incomplete
    disabled: Incomplete
    def __init__(self, value: Incomplete | None = None, **kwargs) -> None: ...

class Checkbox(_Bool):
    """Displays a boolean `value` in the form of a checkbox.

    Parameters
    ----------
    value : {True,False}
        value of the checkbox: True-checked, False-unchecked
    description : str
        description displayed next to the checkbox
    indent : {True,False}
        indent the control to align with other controls with a description. The style.description_width attribute controls this width for consistence with other controls.
    """
    indent: Incomplete
    style: Incomplete

class ToggleButton(_Bool):
    """Displays a boolean `value` in the form of a toggle button.

    Parameters
    ----------
    value : {True,False}
        value of the toggle button: True-pressed, False-unpressed
    description : str
        description displayed on the button
    icon: str
        font-awesome icon name
    style: instance of DescriptionStyle
        styling customizations
    button_style: enum
        button predefined styling
    """
    icon: Incomplete
    button_style: Incomplete
    style: Incomplete

class Valid(_Bool):
    """Displays a boolean `value` in the form of a green check (True / valid)
    or a red cross (False / invalid).

    Parameters
    ----------
    value: {True,False}
        value of the Valid widget
    """
    readout: Incomplete
