from .docutils import doc_subst as doc_subst
from .trait_types import InstanceDict as InstanceDict, TypedTuple as TypedTuple
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionStyle as DescriptionStyle, DescriptionWidget as DescriptionWidget
from .widget_int import SliderStyle as SliderStyle
from .widget_style import Style as Style
from _typeshed import Incomplete
from traitlets import Dict as Dict, Union as Union

def findvalue(array, value, compare=...):
    """A function that uses the compare function to return a value from the list."""

class _Selection(DescriptionWidget, ValueWidget, CoreWidget):
    """Base class for Selection widgets

    ``options`` can be specified as a list of values or a list of (label, value)
    tuples. The labels are the strings that will be displayed in the UI,
    representing the actual Python choices, and should be unique.
    If labels are not specified, they are generated from the values.

    When programmatically setting the value, a reverse lookup is performed
    among the options to check that the value is valid. The reverse lookup uses
    the equality operator by default, but another predicate may be provided via
    the ``equals`` keyword argument. For example, when dealing with numpy arrays,
    one may set equals=np.array_equal.
    """
    value: Incomplete
    label: Incomplete
    index: Incomplete
    options: Incomplete
    disabled: Incomplete
    equals: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class _MultipleSelection(DescriptionWidget, ValueWidget, CoreWidget):
    """Base class for multiple Selection widgets

    ``options`` can be specified as a list of values, list of (label, value)
    tuples, or a dict of {label: value}. The labels are the strings that will be
    displayed in the UI, representing the actual Python choices, and should be
    unique. If labels are not specified, they are generated from the values.

    When programmatically setting the value, a reverse lookup is performed
    among the options to check that the value is valid. The reverse lookup uses
    the equality operator by default, but another predicate may be provided via
    the ``equals`` keyword argument. For example, when dealing with numpy arrays,
    one may set equals=np.array_equal.
    """
    value: Incomplete
    label: Incomplete
    index: Incomplete
    options: Incomplete
    disabled: Incomplete
    equals: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class ToggleButtonsStyle(DescriptionStyle, CoreWidget):
    """Button style widget.

    Parameters
    ----------
    button_width: str
        The width of each button. This should be a valid CSS
        width, e.g. '10px' or '5em'.

    font_weight: str
        The text font weight of each button, This should be a valid CSS font
        weight unit, for example 'bold' or '600'
    """
    button_width: Incomplete
    font_weight: Incomplete

class ToggleButtons(_Selection):
    """Group of toggle buttons that represent an enumeration.

    Only one toggle button can be toggled at any point in time.

    Parameters
    ----------
    {selection_params}

    tooltips: list
        Tooltip for each button. If specified, must be the
        same length as `options`.

    icons: list
        Icons to show on the buttons. This must be the name
        of a font-awesome icon. See `http://fontawesome.io/icons/`
        for a list of icons.

    button_style: str
        One of 'primary', 'success', 'info', 'warning' or
        'danger'. Applies a predefined style to every button.

    style: ToggleButtonsStyle
        Style parameters for the buttons.
    """
    tooltips: Incomplete
    icons: Incomplete
    style: Incomplete
    button_style: Incomplete

class Dropdown(_Selection):
    """Allows you to select a single item from a dropdown.

    Parameters
    ----------
    {selection_params}
    """
class RadioButtons(_Selection):
    """Group of radio buttons that represent an enumeration.

    Only one radio button can be toggled at any point in time.

    Parameters
    ----------
    {selection_params}
    """

class Select(_Selection):
    """
    Listbox that only allows one item to be selected at any given time.

    Parameters
    ----------
    {selection_params}

    rows: int
        The number of rows to display in the widget.
    """
    rows: Incomplete

class SelectMultiple(_MultipleSelection):
    """
    Listbox that allows many items to be selected at any given time.

    The ``value``, ``label`` and ``index`` attributes are all iterables.

    Parameters
    ----------
    {multiple_selection_params}

    rows: int
        The number of rows to display in the widget.
    """
    rows: Incomplete

class _SelectionNonempty(_Selection):
    """Selection that is guaranteed to have a value selected."""
    value: Incomplete
    label: Incomplete
    index: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class _MultipleSelectionNonempty(_MultipleSelection):
    """Selection that is guaranteed to have an option available."""
    def __init__(self, *args, **kwargs) -> None: ...

class SelectionSlider(_SelectionNonempty):
    """
    Slider to select a single item from a list or dictionary.

    Parameters
    ----------
    {selection_params}

    {slider_params}
    """
    orientation: Incomplete
    readout: Incomplete
    continuous_update: Incomplete
    behavior: Incomplete
    style: Incomplete

class SelectionRangeSlider(_MultipleSelectionNonempty):
    """
    Slider to select multiple contiguous items from a list.

    The index, value, and label attributes contain the start and end of
    the selection range, not all items in the range.

    Parameters
    ----------
    {multiple_selection_params}

    {slider_params}
    """
    value: Incomplete
    label: Incomplete
    index: Incomplete
    orientation: Incomplete
    readout: Incomplete
    continuous_update: Incomplete
    style: Incomplete
    behavior: Incomplete
