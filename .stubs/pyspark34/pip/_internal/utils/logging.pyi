import logging
import logging.handlers
from _typeshed import Incomplete
from dataclasses import dataclass
from logging import Filter
from pip._internal.utils._log import VERBOSE as VERBOSE, getLogger as getLogger
from pip._internal.utils.compat import WINDOWS as WINDOWS
from pip._internal.utils.deprecation import DEPRECATION_MSG_PREFIX as DEPRECATION_MSG_PREFIX
from pip._internal.utils.misc import ensure_dir as ensure_dir
from pip._vendor.rich.console import Console as Console, ConsoleOptions as ConsoleOptions, ConsoleRenderable as ConsoleRenderable, RenderResult as RenderResult, RenderableType as RenderableType, RichCast as RichCast
from pip._vendor.rich.highlighter import NullHighlighter as NullHighlighter
from pip._vendor.rich.logging import RichHandler as RichHandler
from pip._vendor.rich.segment import Segment as Segment
from pip._vendor.rich.style import Style as Style
from typing import Any, ClassVar, Generator, List, TextIO

subprocess_logger: Incomplete

class BrokenStdoutLoggingError(Exception):
    """
    Raised if BrokenPipeError occurs for the stdout stream while logging.
    """

def indent_log(num: int = 2) -> Generator[None, None, None]:
    """
    A context manager which will cause the log output to be indented for any
    log messages emitted inside it.
    """
def get_indentation() -> int: ...

class IndentingFormatter(logging.Formatter):
    default_time_format: str
    add_timestamp: Incomplete
    def __init__(self, *args: Any, add_timestamp: bool = False, **kwargs: Any) -> None:
        """
        A logging.Formatter that obeys the indent_log() context manager.

        :param add_timestamp: A bool indicating output lines should be prefixed
            with their record's timestamp.
        """
    def get_message_start(self, formatted: str, levelno: int) -> str:
        """
        Return the start of the formatted log message (not counting the
        prefix to add to each line).
        """
    def format(self, record: logging.LogRecord) -> str:
        """
        Calls the standard formatter, but will indent all of the log message
        lines by our current indentation level.
        """

@dataclass
class IndentedRenderable:
    renderable: RenderableType
    indent: int
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __init__(self, renderable, indent) -> None: ...

class RichPipStreamHandler(RichHandler):
    KEYWORDS: ClassVar[List[str] | None]
    def __init__(self, stream: TextIO | None, no_color: bool) -> None: ...
    def emit(self, record: logging.LogRecord) -> None: ...
    def handleError(self, record: logging.LogRecord) -> None:
        """Called when logging is unable to log some output."""

class BetterRotatingFileHandler(logging.handlers.RotatingFileHandler): ...

class MaxLevelFilter(Filter):
    level: Incomplete
    def __init__(self, level: int) -> None: ...
    def filter(self, record: logging.LogRecord) -> bool: ...

class ExcludeLoggerFilter(Filter):
    """
    A logging Filter that excludes records from a logger (or its children).
    """
    def filter(self, record: logging.LogRecord) -> bool: ...

def setup_logging(verbosity: int, no_color: bool, user_log_file: str | None) -> int:
    """Configures and sets up all of the logging

    Returns the requested logging level, as its integer value.
    """
