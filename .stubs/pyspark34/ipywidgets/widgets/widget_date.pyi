from .trait_types import Date as Date, date_serialization as date_serialization
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete

class DatePicker(DescriptionWidget, ValueWidget, CoreWidget):
    """
    Display a widget for picking dates.

    Parameters
    ----------

    value: datetime.date
        The current value of the widget.

    disabled: bool
        Whether to disable user changes.

    Examples
    --------

    >>> import datetime
    >>> import ipywidgets as widgets
    >>> date_pick = widgets.DatePicker()
    >>> date_pick.value = datetime.date(2019, 7, 9)
    """
    value: Incomplete
    disabled: Incomplete
    min: Incomplete
    max: Incomplete
    step: Incomplete
