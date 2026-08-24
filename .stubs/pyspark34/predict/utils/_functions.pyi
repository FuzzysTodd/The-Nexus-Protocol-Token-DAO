from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class BaseFunction:
    """
    The base schema of the functions. This schema has been inited.
    """
    functional: Callable | None = ...
    def __init__(self, functional) -> None: ...

@dataclass(frozen=True)
class ProcessFunction(BaseFunction):
    """Data Process Function."""
    def __init__(self, functional) -> None: ...

@dataclass(frozen=True)
class LoadFunction(BaseFunction):
    """Model Loading Function."""
    def __init__(self, functional) -> None: ...

@dataclass(frozen=True)
class PredictFunction(BaseFunction):
    """Predict Function."""
    def __init__(self, functional) -> None: ...
