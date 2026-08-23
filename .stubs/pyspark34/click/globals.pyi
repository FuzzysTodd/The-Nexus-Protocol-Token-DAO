import typing as t
import typing_extensions as te
from .core import Context as Context

@t.overload
def get_current_context(silent: te.Literal[False] = False) -> Context: ...
@t.overload
def get_current_context(silent: bool = ...) -> Context | None: ...
def push_context(ctx: Context) -> None:
    """Pushes a new context to the current stack."""
def pop_context() -> None:
    """Removes the top level from the stack."""
def resolve_color_default(color: bool | None = None) -> bool | None:
    """Internal helper to get the default value of the color flag.  If a
    value is passed it's returned unchanged, otherwise it's looked up from
    the current context.
    """
