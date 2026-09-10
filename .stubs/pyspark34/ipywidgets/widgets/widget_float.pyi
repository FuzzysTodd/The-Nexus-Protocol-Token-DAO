from .trait_types import InstanceDict as InstanceDict, NumberFormat as NumberFormat
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionWidget as DescriptionWidget
from .widget_int import ProgressStyle as ProgressStyle, SliderStyle as SliderStyle
from _typeshed import Incomplete
from traitlets import Instance as Instance, default as default

class _Float(DescriptionWidget, ValueWidget, CoreWidget):
    value: Incomplete
    def __init__(self, value: Incomplete | None = None, **kwargs) -> None: ...

class _BoundedFloat(_Float):
    max: Incomplete
    min: Incomplete

class _BoundedLogFloat(_Float):
    max: Incomplete
    min: Incomplete
    base: Incomplete
    value: Incomplete

class FloatText(_Float):
    """ Displays a float value within a textbox. For a textbox in
    which the value must be within a specific range, use BoundedFloatText.

    Parameters
    ----------
    value : float
        value displayed
    step : float
        step of the increment (if None, any step is allowed)
    description : str
        description displayed next to the text box
    """
    disabled: Incomplete
    continuous_update: Incomplete
    step: Incomplete

class BoundedFloatText(_BoundedFloat):
    """ Displays a float value within a textbox. Value must be within the range specified.

    For a textbox in which the value doesn't need to be within a specific range, use FloatText.

    Parameters
    ----------
    value : float
        value displayed
    min : float
        minimal value of the range of possible values displayed
    max : float
        maximal value of the range of possible values displayed
    step : float
        step of the increment (if None, any step is allowed)
    description : str
        description displayed next to the textbox
    """
    disabled: Incomplete
    continuous_update: Incomplete
    step: Incomplete

class FloatSlider(_BoundedFloat):
    """ Slider/trackbar of floating values with the specified range.

    Parameters
    ----------
    value : float
        position of the slider
    min : float
        minimal position of the slider
    max : float
        maximal position of the slider
    step : float
        step of the trackbar
    description : str
        name of the slider
    orientation : {'horizontal', 'vertical'}
        default is 'horizontal', orientation of the slider
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
    disabled: Incomplete
    style: Incomplete
    behavior: Incomplete

class FloatLogSlider(_BoundedLogFloat):
    """ Slider/trackbar of logarithmic floating values with the specified range.

    Parameters
    ----------
    value : float
        position of the slider
    base : float
        base of the logarithmic scale. Default is 10
    min : float
        minimal position of the slider in log scale, i.e., actual minimum is base ** min
    max : float
        maximal position of the slider in log scale, i.e., actual maximum is base ** max
    step : float
        step of the trackbar, denotes steps for the exponent, not the actual value
    description : str
        name of the slider
    orientation : {'horizontal', 'vertical'}
        default is 'horizontal', orientation of the slider
    readout : {True, False}
        default is True, display the current value of the slider next to it
    behavior : str
        slider handle and connector dragging behavior. Default is 'drag-tap'.
    readout_format : str
        default is '.3g', specifier for the format function used to represent
        slider value for human consumption, modeled after Python 3's format
        specification mini-language (PEP 3101).
    """
    step: Incomplete
    orientation: Incomplete
    readout: Incomplete
    readout_format: Incomplete
    continuous_update: Incomplete
    disabled: Incomplete
    base: Incomplete
    style: Incomplete
    behavior: Incomplete

class FloatProgress(_BoundedFloat):
    """ Displays a progress bar.

    Parameters
    -----------
    value : float
        position within the range of the progress bar
    min : float
        minimal position of the slider
    max : float
        maximal position of the slider
    description : str
        name of the progress bar
    orientation : {'horizontal', 'vertical'}
        default is 'horizontal', orientation of the progress bar
    bar_style: {'success', 'info', 'warning', 'danger', ''}
        color of the progress bar, default is '' (blue)
        colors are: 'success'-green, 'info'-light blue, 'warning'-orange, 'danger'-red
    """
    orientation: Incomplete
    bar_style: Incomplete
    style: Incomplete

class _FloatRange(_Float):
    value: Incomplete
    @property
    def lower(self): ...
    @lower.setter
    def lower(self, lower) -> None: ...
    @property
    def upper(self): ...
    @upper.setter
    def upper(self, upper) -> None: ...

class _BoundedFloatRange(_FloatRange):
    step: Incomplete
    max: Incomplete
    min: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class FloatRangeSlider(_BoundedFloatRange):
    """ Slider/trackbar that represents a pair of floats bounded by minimum and maximum value.

    Parameters
    ----------
    value : float tuple
        range of the slider displayed
    min : float
        minimal position of the slider
    max : float
        maximal position of the slider
    step : float
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
    disabled: Incomplete
    style: Incomplete
    behavior: Incomplete
