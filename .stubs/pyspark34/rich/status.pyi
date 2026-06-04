from .console import Console as Console, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .live import Live as Live
from .spinner import Spinner as Spinner
from .style import StyleType as StyleType
from _typeshed import Incomplete
from types import TracebackType
from typing import Type

class Status(JupyterMixin):
    '''Displays a status indicator with a \'spinner\' animation.

    Args:
        status (RenderableType): A status renderable (str or Text typically).
        console (Console, optional): Console instance to use, or None for global console. Defaults to None.
        spinner (str, optional): Name of spinner animation (see python -m rich.spinner). Defaults to "dots".
        spinner_style (StyleType, optional): Style of spinner. Defaults to "status.spinner".
        speed (float, optional): Speed factor for spinner animation. Defaults to 1.0.
        refresh_per_second (float, optional): Number of refreshes per second. Defaults to 12.5.
    '''
    status: Incomplete
    spinner_style: Incomplete
    speed: Incomplete
    def __init__(self, status: RenderableType, *, console: Console | None = None, spinner: str = 'dots', spinner_style: StyleType = 'status.spinner', speed: float = 1.0, refresh_per_second: float = 12.5) -> None: ...
    @property
    def renderable(self) -> Spinner: ...
    @property
    def console(self) -> Console:
        """Get the Console used by the Status objects."""
    def update(self, status: RenderableType | None = None, *, spinner: str | None = None, spinner_style: StyleType | None = None, speed: float | None = None) -> None:
        """Update status.

        Args:
            status (Optional[RenderableType], optional): New status renderable or None for no change. Defaults to None.
            spinner (Optional[str], optional): New spinner or None for no change. Defaults to None.
            spinner_style (Optional[StyleType], optional): New spinner style or None for no change. Defaults to None.
            speed (Optional[float], optional): Speed factor for spinner animation or None for no change. Defaults to None.
        """
    def start(self) -> None:
        """Start the status animation."""
    def stop(self) -> None:
        """Stop the spinner animation."""
    def __rich__(self) -> RenderableType: ...
    def __enter__(self) -> Status: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
