from . import get_console as get_console
from .console import Console as Console, ConsoleRenderable as ConsoleRenderable, RenderHook as RenderHook, RenderableType as RenderableType
from .control import Control as Control
from .file_proxy import FileProxy as FileProxy
from .jupyter import JupyterMixin as JupyterMixin
from .live_render import LiveRender as LiveRender, VerticalOverflowMethod as VerticalOverflowMethod
from .screen import Screen as Screen
from .text import Text as Text
from _typeshed import Incomplete
from threading import Thread
from types import TracebackType
from typing import Callable, List, Type

class _RefreshThread(Thread):
    """A thread that calls refresh() at regular intervals."""
    live: Incomplete
    refresh_per_second: Incomplete
    done: Incomplete
    def __init__(self, live: Live, refresh_per_second: float) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...

class Live(JupyterMixin, RenderHook):
    '''Renders an auto-updating live display of any given renderable.

    Args:
        renderable (RenderableType, optional): The renderable to live display. Defaults to displaying nothing.
        console (Console, optional): Optional Console instance. Default will an internal Console instance writing to stdout.
        screen (bool, optional): Enable alternate screen mode. Defaults to False.
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()` or `update()` with refresh flag. Defaults to True
        refresh_per_second (float, optional): Number of times per second to refresh the live display. Defaults to 4.
        transient (bool, optional): Clear the renderable on exit (has no effect when screen=True). Defaults to False.
        redirect_stdout (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True.
        redirect_stderr (bool, optional): Enable redirection of stderr. Defaults to True.
        vertical_overflow (VerticalOverflowMethod, optional): How to handle renderable when it is too tall for the console. Defaults to "ellipsis".
        get_renderable (Callable[[], RenderableType], optional): Optional callable to get renderable. Defaults to None.
    '''
    console: Incomplete
    ipy_widget: Incomplete
    auto_refresh: Incomplete
    transient: Incomplete
    refresh_per_second: Incomplete
    vertical_overflow: Incomplete
    def __init__(self, renderable: RenderableType | None = None, *, console: Console | None = None, screen: bool = False, auto_refresh: bool = True, refresh_per_second: float = 4, transient: bool = False, redirect_stdout: bool = True, redirect_stderr: bool = True, vertical_overflow: VerticalOverflowMethod = 'ellipsis', get_renderable: Callable[[], RenderableType] | None = None) -> None: ...
    @property
    def is_started(self) -> bool:
        """Check if live display has been started."""
    def get_renderable(self) -> RenderableType: ...
    def start(self, refresh: bool = False) -> None:
        """Start live rendering display.

        Args:
            refresh (bool, optional): Also refresh. Defaults to False.
        """
    def stop(self) -> None:
        """Stop live rendering display."""
    def __enter__(self) -> Live: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    @property
    def renderable(self) -> RenderableType:
        """Get the renderable that is being displayed

        Returns:
            RenderableType: Displayed renderable.
        """
    def update(self, renderable: RenderableType, *, refresh: bool = False) -> None:
        """Update the renderable that is being displayed

        Args:
            renderable (RenderableType): New renderable to use.
            refresh (bool, optional): Refresh the display. Defaults to False.
        """
    def refresh(self) -> None:
        """Update the display of the Live Render."""
    def process_renderables(self, renderables: List[ConsoleRenderable]) -> List[ConsoleRenderable]:
        """Process renderables to restore cursor and display progress."""
