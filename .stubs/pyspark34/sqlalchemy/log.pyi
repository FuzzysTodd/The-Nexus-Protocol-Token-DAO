from .util import py311 as py311, py38 as py38
from .util.typing import Literal as Literal
from _typeshed import Incomplete
from typing import Any, Type, overload

STACKLEVEL: bool
STACKLEVEL_OFFSET: Incomplete
rootlogger: Incomplete

def class_logger(cls) -> Type[_IT]: ...

class Identified:
    logging_name: str | None
    logger: _IdentifiedLoggerType

class InstanceLogger:
    """A logger adapter (wrapper) for :class:`.Identified` subclasses.

    This allows multiple instances (e.g. Engine or Pool instances)
    to share a logger, but have its verbosity controlled on a
    per-instance basis.

    The basic functionality is to return a logging level
    which is based on an instance's echo setting.

    Default implementation is:

    'debug' -> logging.DEBUG
    True    -> logging.INFO
    False   -> Effective level of underlying logger (
    logging.WARNING by default)
    None    -> same as False
    """
    echo: Incomplete
    logger: Incomplete
    def __init__(self, echo: _EchoFlagType, name: str) -> None: ...
    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Delegate a debug call to the underlying logger."""
    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Delegate an info call to the underlying logger."""
    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Delegate a warning call to the underlying logger."""
    warn = warning
    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """
        Delegate an error call to the underlying logger.
        """
    def exception(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Delegate an exception call to the underlying logger."""
    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Delegate a critical call to the underlying logger."""
    def log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        """Delegate a log call to the underlying logger.

        The level here is determined by the echo
        flag as well as that of the underlying logger, and
        logger._log() is called directly.

        """
    def isEnabledFor(self, level: int) -> bool:
        """Is this logger enabled for level 'level'?"""
    def getEffectiveLevel(self) -> int:
        """What's the effective level for this logger?"""

def instance_logger(instance: Identified, echoflag: _EchoFlagType = None) -> None:
    """create a logger for an instance that implements :class:`.Identified`."""

class echo_property:
    __doc__: str
    @overload
    def __get__(self, instance: Literal[None], owner: Type[Identified]) -> echo_property: ...
    @overload
    def __get__(self, instance: Identified, owner: Type[Identified]) -> _EchoFlagType: ...
    def __set__(self, instance: Identified, value: _EchoFlagType) -> None: ...
