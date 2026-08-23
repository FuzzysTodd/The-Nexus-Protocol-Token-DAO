from .console import ConsoleRenderable as ConsoleRenderable
from .highlighter import ReprHighlighter as ReprHighlighter
from .panel import Panel as Panel
from .pretty import Pretty as Pretty
from .table import Table as Table
from .text import Text as Text, TextType as TextType
from collections.abc import Mapping
from typing import Any

def render_scope(scope: Mapping[str, Any], *, title: TextType | None = None, sort_keys: bool = True, indent_guides: bool = False, max_length: int | None = None, max_string: int | None = None) -> ConsoleRenderable:
    """Render python variables in a given scope.

    Args:
        scope (Mapping): A mapping containing variable names and values.
        title (str, optional): Optional title. Defaults to None.
        sort_keys (bool, optional): Enable sorting of items. Defaults to True.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.

    Returns:
        ConsoleRenderable: A renderable object.
    """
