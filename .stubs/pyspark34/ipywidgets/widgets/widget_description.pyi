from .domwidget import DOMWidget as DOMWidget
from .trait_types import InstanceDict as InstanceDict
from .utils import deprecation as deprecation
from .widget import Widget as Widget, register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from .widget_style import Style as Style
from _typeshed import Incomplete

class DescriptionStyle(Style, CoreWidget, Widget):
    """Description style widget."""
    description_width: Incomplete

class DescriptionWidget(DOMWidget, CoreWidget):
    """Widget that has a description label to the side."""
    description: Incomplete
    description_allow_html: Incomplete
    style: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def description_tooltip(self):
        """The tooltip information.
        .. deprecated :: 8.0.0
           Use tooltip attribute instead.
        """
    tooltip: Incomplete
    @description_tooltip.setter
    def description_tooltip(self, tooltip) -> None: ...
