from ._spinners import SPINNERS as SPINNERS
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .measure import Measurement as Measurement
from .style import StyleType as StyleType
from .table import Table as Table
from .text import Text as Text
from _typeshed import Incomplete

class Spinner:
    '''A spinner animation.

    Args:
        name (str): Name of spinner (run python -m rich.spinner).
        text (RenderableType, optional): A renderable to display at the right of the spinner (str or Text typically). Defaults to "".
        style (StyleType, optional): Style for spinner animation. Defaults to None.
        speed (float, optional): Speed factor for animation. Defaults to 1.0.

    Raises:
        KeyError: If name isn\'t one of the supported spinner animations.
    '''
    text: Incomplete
    frames: Incomplete
    interval: Incomplete
    start_time: Incomplete
    style: Incomplete
    speed: Incomplete
    frame_no_offset: float
    def __init__(self, name: str, text: RenderableType = '', *, style: StyleType | None = None, speed: float = 1.0) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def render(self, time: float) -> RenderableType:
        """Render the spinner for a given time.

        Args:
            time (float): Time in seconds.

        Returns:
            RenderableType: A renderable containing animation frame.
        """
    def update(self, *, text: RenderableType = '', style: StyleType | None = None, speed: float | None = None) -> None:
        '''Updates attributes of a spinner after it has been started.

        Args:
            text (RenderableType, optional): A renderable to display at the right of the spinner (str or Text typically). Defaults to "".
            style (StyleType, optional): Style for spinner animation. Defaults to None.
            speed (float, optional): Speed factor for animation. Defaults to None.
        '''
