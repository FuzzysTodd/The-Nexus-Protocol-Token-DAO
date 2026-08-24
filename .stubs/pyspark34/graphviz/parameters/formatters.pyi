from . import base
from _typeshed import Incomplete

__all__ = ['FORMATTERS', 'verify_formatter', 'Formatter']

FORMATTERS: Incomplete

def verify_formatter(formatter: str | None, *, required: bool = ...) -> None: ...

class Formatter(base.ParameterBase):
    """Rendering engine parameter (no default)."""
    def __init__(self, *, formatter: str | None = None, **kwargs) -> None: ...
    @property
    def formatter(self) -> str | None:
        """The output formatter used for rendering
            (``'cairo'``, ``'gd'``, ...)."""
    @formatter.setter
    def formatter(self, formatter: str | None) -> None: ...
