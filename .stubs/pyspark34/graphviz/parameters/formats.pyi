from . import base
from _typeshed import Incomplete

__all__ = ['FORMATS', 'verify_format', 'Format']

FORMATS: Incomplete

def verify_format(format: str, *, required: bool = ...) -> None: ...

class Format(base.ParameterBase):
    """Rendering format parameter with ``'pdf'`` default."""
    def __init__(self, *, format: str | None = None, **kwargs) -> None: ...
    @property
    def format(self) -> str:
        """The output format used for rendering
            (``'pdf'``, ``'png'``, ...)."""
    @format.setter
    def format(self, format: str) -> None: ...
