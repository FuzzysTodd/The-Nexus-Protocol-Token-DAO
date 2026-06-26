from pasta.base import ast_utils as ast_utils, scope as scope

class InlineError(Exception): ...

def inline_name(t, name) -> None:
    """Inline a constant name into a module."""
