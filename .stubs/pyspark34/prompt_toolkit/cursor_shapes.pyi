import abc
from .application import Application
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Callable

__all__ = ['CursorShape', 'CursorShapeConfig', 'SimpleCursorShapeConfig', 'ModalCursorShapeConfig', 'DynamicCursorShapeConfig', 'to_cursor_shape_config']

class CursorShape(Enum):
    BLOCK: str
    BEAM: str
    UNDERLINE: str
    BLINKING_BLOCK: str
    BLINKING_BEAM: str
    BLINKING_UNDERLINE: str

class CursorShapeConfig(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_cursor_shape(self, application: Application[Any]) -> CursorShape:
        """
        Return the cursor shape to be used in the current state.
        """
AnyCursorShapeConfig = CursorShape | CursorShapeConfig | None

class SimpleCursorShapeConfig(CursorShapeConfig):
    """
    Always show the given cursor shape.
    """
    cursor_shape: Incomplete
    def __init__(self, cursor_shape: CursorShape = ...) -> None: ...
    def get_cursor_shape(self, application: Application[Any]) -> CursorShape: ...

class ModalCursorShapeConfig(CursorShapeConfig):
    """
    Show cursor shape according to the current input mode.
    """
    def get_cursor_shape(self, application: Application[Any]) -> CursorShape: ...

class DynamicCursorShapeConfig(CursorShapeConfig):
    get_cursor_shape_config: Incomplete
    def __init__(self, get_cursor_shape_config: Callable[[], AnyCursorShapeConfig]) -> None: ...
    def get_cursor_shape(self, application: Application[Any]) -> CursorShape: ...

def to_cursor_shape_config(value: AnyCursorShapeConfig) -> CursorShapeConfig:
    """
    Take a `CursorShape` instance or `CursorShapeConfig` and turn it into a
    `CursorShapeConfig`.
    """
