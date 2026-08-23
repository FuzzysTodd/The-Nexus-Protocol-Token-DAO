from .trait_types import Datetime as Datetime, datetime_serialization as datetime_serialization, naive_serialization as naive_serialization
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete

class DatetimePicker(DescriptionWidget, ValueWidget, CoreWidget):
    """
    Display a widget for picking datetimes.

    Parameters
    ----------

    value: datetime.datetime
        The current value of the widget.

    disabled: bool
        Whether to disable user changes.

    min: datetime.datetime
        The lower allowed datetime bound

    max: datetime.datetime
        The upper allowed datetime bound

    Examples
    --------

    >>> import datetime
    >>> import ipydatetime
    >>> datetime_pick = ipydatetime.DatetimePicker()
    >>> datetime_pick.value = datetime.datetime(2018, 09, 5, 12, 34, 3)
    """
    value: Incomplete
    disabled: Incomplete
    min: Incomplete
    max: Incomplete

class NaiveDatetimePicker(DatetimePicker):
    """
    Display a widget for picking naive datetimes (i.e. timezone unaware).

    Parameters
    ----------

    value: datetime.datetime
        The current value of the widget.

    disabled: bool
        Whether to disable user changes.

    min: datetime.datetime
        The lower allowed datetime bound

    max: datetime.datetime
        The upper allowed datetime bound

    Examples
    --------

    >>> import datetime
    >>> import ipydatetime
    >>> datetime_pick = ipydatetime.NaiveDatetimePicker()
    >>> datetime_pick.value = datetime.datetime(2018, 09, 5, 12, 34, 3)
    """
    value: Incomplete
    min: Incomplete
    max: Incomplete
