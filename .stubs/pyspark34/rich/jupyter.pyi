from . import get_console as get_console
from .segment import Segment as Segment
from .terminal_theme import DEFAULT_TERMINAL_THEME as DEFAULT_TERMINAL_THEME
from _typeshed import Incomplete
from rich.console import ConsoleRenderable as ConsoleRenderable
from typing import Any, Iterable

JUPYTER_HTML_FORMAT: str

class JupyterRenderable:
    """A shim to write html to Jupyter notebook."""
    html: Incomplete
    text: Incomplete
    def __init__(self, html: str, text: str) -> None: ...

class JupyterMixin:
    """Add to an Rich renderable to make it render in Jupyter notebook."""

def display(segments: Iterable[Segment], text: str) -> None:
    """Render segments to Jupyter."""
def print(*args: Any, **kwargs: Any) -> None:
    """Proxy for Console print."""
