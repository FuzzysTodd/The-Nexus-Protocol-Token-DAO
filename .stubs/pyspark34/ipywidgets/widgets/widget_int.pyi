from .trait_types import Color as Color, InstanceDict as InstanceDict, NumberFormat as NumberFormat
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionStyle as DescriptionStyle, DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete
from traitlets import Instance as Instance, default as default

class _Int(DescriptionWidget, ValueWidget, CoreWidget):
    """Base class for widgets that represent an integer."""
    value: Incomplete
    def __init__(self, value: Incomplete | None = None, **kwargs) -> None: ...

class _BoundedInt(_Int):
    """Base class for widgets that represent an integer bounded from above and below.
    """
    max: Incomplete
    min: Incomplete
    def __init__(self, value: Incomplete | None = None, min: Incomplete | None = None, max: Incomplete | None = None, step: Incomplete | None = None, **kwargs) -> None: ...

class IntText(_Int):
    """Textbox widget that represents an integer."""
    disabled: Incomplete
    continuous_update: Incomplete
    step: Incomplete

class BoundedIntText(_BoundedInt):
    """Textbox widget that represents an integer bounded from above and below.
    """
    disabled: Incomplete
    continuous_update: Incomplete
    step: Incomplete

class SliderStyle(DescriptionStyle, CoreWidget):
    """Button style widget."""
    handle_color: Incomplete

class IntSlider(_BoundedInt):
    """Slider widget that represents an integer bounded from above and below.
    """
    step: Incomplete
    orientation: Incomplete
    readout: Incomplete
    readout_format: Incomplete
    continuous_update: Incomplete
    disabled: Incomplete
    style: Incomplete
    behavior: Incomplete

class ProgressStyle(DescriptionStyle, CoreWidget):
    """Button style widget."""
    bar_color: Incomplete

class IntProgress(_BoundedInt):
    """Progress bar that represents an integer bounded from above and below.
    """
    orientation: Incomplete
    bar_style: Incomplete
    style: Incomplete

class _IntRange(_Int):
    value: Incomplete
    @property
    def lower(self): ...
    @lower.setter
    def lower(self, lower) -> None: ...
    @property
    def upper(self): ...
    @upper.setter
    def upper(self, upper) -> None: ...

class Play(_BoundedInt):
    """Play/repeat buttons to step through values automatically, and optionally loop.
    """
    playing: Incomplete
    repeat: Incomplete
    interval: Incomplete
    step: Incomplete
    disabled: Incomplete
    show_repeat: Incomplete

class _BoundedIntRange(_IntRange):
    max: Incomplete
    min: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class IntRangeSlider(_BoundedIntRange):
    """Slider/trackbar that represents a pair of ints bounded by minimum and maximum value.

    Parameters
    ----------
    value : int tuple
        The pair (`lower`, `upper`) of integers
    min : int
        The lowest allowed value for `lower`
    max : int
        The highest allowed value for `upper`
    step : int
        step of the trackbar
    description : str
        name of the slider
    orientation : {'horizontal', 'vertical'}
        default is 'horizontal'
    readout : {True, False}
        default is True, display the current value of the slider next to it
    behavior : str
        slider handle and connector dragging behavior. Default is 'drag-tap'.
    readout_format : str
        default is '.2f', specifier for the format function used to represent
        slider value for human consumption, modeled after Python 3's format
        specification mini-language (PEP 3101).
    """
    step: Incomplete
    orientation: Incomplete
    readout: Incomplete
    readout_format: Incomplete
    continuous_update: Incomplete
    style: Incomplete
    disabled: Incomplete
    behavior: Incomplete
