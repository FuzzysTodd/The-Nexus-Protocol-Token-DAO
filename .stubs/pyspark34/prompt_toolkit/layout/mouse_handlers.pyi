from _typeshed import Incomplete
from prompt_toolkit.key_binding.key_bindings import NotImplementedOrNone
from prompt_toolkit.mouse_events import MouseEvent
from typing import Callable

__all__ = ['MouseHandler', 'MouseHandlers']

MouseHandler: Incomplete

class MouseHandlers:
    """
    Two dimensional raster of callbacks for mouse events.
    """
    mouse_handlers: Incomplete
    def __init__(self) -> None: ...
    def set_mouse_handler_for_range(self, x_min: int, x_max: int, y_min: int, y_max: int, handler: Callable[[MouseEvent], NotImplementedOrNone]) -> None:
        """
        Set mouse handler for a region.
        """
