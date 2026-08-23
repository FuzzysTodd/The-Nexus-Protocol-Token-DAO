from .trait_types import Color as Color
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete

class ColorPicker(DescriptionWidget, ValueWidget, CoreWidget):
    value: Incomplete
    concise: Incomplete
    disabled: Incomplete
