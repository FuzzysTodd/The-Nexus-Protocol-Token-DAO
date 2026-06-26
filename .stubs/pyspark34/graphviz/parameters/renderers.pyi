from . import base
from _typeshed import Incomplete

__all__ = ['RENDERERS', 'verify_renderer', 'Renderer']

RENDERERS: Incomplete

def verify_renderer(renderer: str | None, *, required: bool = ...) -> None: ...

class Renderer(base.ParameterBase):
    """Rendering renderer parameter (no default)."""
    def __init__(self, *, renderer: str | None = None, **kwargs) -> None: ...
    @property
    def renderer(self) -> str | None:
        """The output renderer used for rendering
            (``'cairo'``, ``'gd'``, ...)."""
    @renderer.setter
    def renderer(self, renderer: str | None) -> None: ...
