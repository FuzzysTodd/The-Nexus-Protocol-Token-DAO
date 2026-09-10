import typing as t

def warn(msg: str, category: t.Any, *, stacklevel: int, source: t.Any = None) -> None:
    """Like warnings.warn(), but category and stacklevel are required.

    You pretty much never want the default stacklevel of 1, so this helps
    encourage setting it explicitly."""
def deprecated_method(method: t.Any, cls: t.Any, method_name: str, msg: str) -> None:
    """Show deprecation warning about a magic method definition.

    Uses warn_explicit to bind warning to method definition instead of triggering code,
    which isn't relevant.
    """
def should_warn(key: t.Any) -> bool:
    """Add our own checks for too many deprecation warnings.

    Limit to once per package.
    """
