from .trait_types import Time as Time, time_serialization as time_serialization
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete

class TimePicker(DescriptionWidget, ValueWidget, CoreWidget):
    '''
    Display a widget for picking times.

    Parameters
    ----------

    value: datetime.time
        The current value of the widget.

    disabled: bool
        Whether to disable user changes.

    min: datetime.time
        The lower allowed time bound

    max: datetime.time
        The upper allowed time bound

    step: float | \'any\'
        The time step to use for the picker, in seconds, or "any"

    Examples
    --------

    >>> import datetime
    >>> import ipydatetime
    >>> time_pick = ipydatetime.TimePicker()
    >>> time_pick.value = datetime.time(12, 34, 3)
    '''
    value: Incomplete
    disabled: Incomplete
    min: Incomplete
    max: Incomplete
    step: Incomplete
