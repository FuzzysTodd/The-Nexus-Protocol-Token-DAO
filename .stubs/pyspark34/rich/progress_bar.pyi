from .color import Color as Color, blend_rgb as blend_rgb
from .color_triplet import ColorTriplet as ColorTriplet
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from _typeshed import Incomplete

PULSE_SIZE: int

class ProgressBar(JupyterMixin):
    '''Renders a (progress) bar. Used by rich.progress.

    Args:
        total (float, optional): Number of steps in the bar. Defaults to 100. Set to None to render a pulsing animation.
        completed (float, optional): Number of steps completed. Defaults to 0.
        width (int, optional): Width of the bar, or ``None`` for maximum width. Defaults to None.
        pulse (bool, optional): Enable pulse effect. Defaults to False. Will pulse if a None total was passed.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        animation_time (Optional[float], optional): Time in seconds to use for animation, or None to use system time.
    '''
    total: Incomplete
    completed: Incomplete
    width: Incomplete
    pulse: Incomplete
    style: Incomplete
    complete_style: Incomplete
    finished_style: Incomplete
    pulse_style: Incomplete
    animation_time: Incomplete
    def __init__(self, total: float | None = 100.0, completed: float = 0, width: int | None = None, pulse: bool = False, style: StyleType = 'bar.back', complete_style: StyleType = 'bar.complete', finished_style: StyleType = 'bar.finished', pulse_style: StyleType = 'bar.pulse', animation_time: float | None = None) -> None: ...
    @property
    def percentage_completed(self) -> float | None:
        """Calculate percentage complete."""
    def update(self, completed: float, total: float | None = None) -> None:
        """Update progress with new values.

        Args:
            completed (float): Number of steps completed.
            total (float, optional): Total number of steps, or ``None`` to not change. Defaults to None.
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
