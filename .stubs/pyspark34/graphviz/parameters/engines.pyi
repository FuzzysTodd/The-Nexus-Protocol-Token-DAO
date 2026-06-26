from . import base
from _typeshed import Incomplete

__all__ = ['ENGINES', 'verify_engine', 'Engine']

ENGINES: Incomplete

def verify_engine(engine: str, *, required: bool = ...) -> None: ...

class Engine(base.ParameterBase):
    """Rendering engine parameter with ``'dot''`` default."""
    def __init__(self, *, engine: str | None = None, **kwargs) -> None: ...
    @property
    def engine(self) -> str:
        """The layout engine used for rendering
            (``'dot'``, ``'neato'``, ...)."""
    @engine.setter
    def engine(self, engine: str) -> None: ...
