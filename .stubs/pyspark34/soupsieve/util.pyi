from _typeshed import Incomplete
from typing import Any, Callable

DEBUG: int
RE_PATTERN_LINE_SPLIT: Incomplete
UC_A: Incomplete
UC_Z: Incomplete

def lower(string: str) -> str:
    """Lower."""

class SelectorSyntaxError(Exception):
    """Syntax error in a CSS selector."""
    line: Incomplete
    col: Incomplete
    context: Incomplete
    def __init__(self, msg: str, pattern: str | None = None, index: int | None = None) -> None:
        """Initialize."""

def deprecated(message: str, stacklevel: int = 2) -> Callable[..., Any]:
    '''
    Raise a `DeprecationWarning` when wrapped function/method is called.

    Usage:

        @deprecated("This method will be removed in version X; use Y instead.")
        def some_method()"
            pass
    '''
def warn_deprecated(message: str, stacklevel: int = 2) -> None:
    """Warn deprecated."""
def get_pattern_context(pattern: str, index: int) -> tuple[str, int, int]:
    """Get the pattern context."""
