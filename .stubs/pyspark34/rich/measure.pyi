from . import errors as errors
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderableType as RenderableType
from .protocol import is_renderable as is_renderable, rich_cast as rich_cast
from typing import NamedTuple, Sequence

class Measurement(NamedTuple):
    """Stores the minimum and maximum widths (in characters) required to render an object."""
    minimum: int
    maximum: int
    @property
    def span(self) -> int:
        """Get difference between maximum and minimum."""
    def normalize(self) -> Measurement:
        """Get measurement that ensures that minimum <= maximum and minimum >= 0

        Returns:
            Measurement: A normalized measurement.
        """
    def with_maximum(self, width: int) -> Measurement:
        """Get a RenderableWith where the widths are <= width.

        Args:
            width (int): Maximum desired width.

        Returns:
            Measurement: New Measurement object.
        """
    def with_minimum(self, width: int) -> Measurement:
        """Get a RenderableWith where the widths are >= width.

        Args:
            width (int): Minimum desired width.

        Returns:
            Measurement: New Measurement object.
        """
    def clamp(self, min_width: int | None = None, max_width: int | None = None) -> Measurement:
        """Clamp a measurement within the specified range.

        Args:
            min_width (int): Minimum desired width, or ``None`` for no minimum. Defaults to None.
            max_width (int): Maximum desired width, or ``None`` for no maximum. Defaults to None.

        Returns:
            Measurement: New Measurement object.
        """
    @classmethod
    def get(cls, console: Console, options: ConsoleOptions, renderable: RenderableType) -> Measurement:
        """Get a measurement for a renderable.

        Args:
            console (~rich.console.Console): Console instance.
            options (~rich.console.ConsoleOptions): Console options.
            renderable (RenderableType): An object that may be rendered with Rich.

        Raises:
            errors.NotRenderableError: If the object is not renderable.

        Returns:
            Measurement: Measurement object containing range of character widths required to render the object.
        """

def measure_renderables(console: Console, options: ConsoleOptions, renderables: Sequence['RenderableType']) -> Measurement:
    """Get a measurement that would fit a number of renderables.

    Args:
        console (~rich.console.Console): Console instance.
        options (~rich.console.ConsoleOptions): Console options.
        renderables (Iterable[RenderableType]): One or more renderable objects.

    Returns:
        Measurement: Measurement object containing range of character widths required to
            contain all given renderables.
    """
