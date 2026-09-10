from .domwidget import DOMWidget as DOMWidget
from .trait_types import TypedTuple as TypedTuple
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from _typeshed import Incomplete

class Button(DOMWidget, ValueWidget, CoreWidget):
    """Represents a gamepad or joystick button."""
    value: Incomplete
    pressed: Incomplete

class Axis(DOMWidget, ValueWidget, CoreWidget):
    """Represents a gamepad or joystick axis."""
    value: Incomplete

class Controller(DOMWidget, CoreWidget):
    """Represents a game controller."""
    index: Incomplete
    name: Incomplete
    mapping: Incomplete
    connected: Incomplete
    timestamp: Incomplete
    buttons: Incomplete
    axes: Incomplete
