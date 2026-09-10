from rich.console import RenderableType as RenderableType
from typing import Any

def is_renderable(check_object: Any) -> bool:
    """Check if an object may be rendered by Rich."""
def rich_cast(renderable: object) -> RenderableType:
    """Cast an object to a renderable by calling __rich__ if present.

    Args:
        renderable (object): A potentially renderable object

    Returns:
        object: The result of recursively calling __rich__.
    """
