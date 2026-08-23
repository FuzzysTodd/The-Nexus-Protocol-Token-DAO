from . import get_console as get_console
from ._log_render import FormatTimeCallable as FormatTimeCallable, LogRender as LogRender
from .console import Console as Console, ConsoleRenderable as ConsoleRenderable
from .highlighter import Highlighter as Highlighter, ReprHighlighter as ReprHighlighter
from .text import Text as Text
from .traceback import Traceback as Traceback
from _typeshed import Incomplete
from logging import Handler, LogRecord
from rich._null_file import NullFile as NullFile
from types import ModuleType
from typing import ClassVar, Iterable, List, Type

class RichHandler(Handler):
    '''A logging handler that renders output with Rich. The time / level / message and file are displayed in columns.
    The level is color coded, and the message is syntax highlighted.

    Note:
        Be careful when enabling console markup in log messages if you have configured logging for libraries not
        under your control. If a dependency writes messages containing square brackets, it may not produce the intended output.

    Args:
        level (Union[int, str], optional): Log level. Defaults to logging.NOTSET.
        console (:class:`~rich.console.Console`, optional): Optional console instance to write logs.
            Default will use a global console instance writing to stdout.
        show_time (bool, optional): Show a column for the time. Defaults to True.
        omit_repeated_times (bool, optional): Omit repetition of the same time. Defaults to True.
        show_level (bool, optional): Show a column for the level. Defaults to True.
        show_path (bool, optional): Show the path to the original log call. Defaults to True.
        enable_link_path (bool, optional): Enable terminal link of path column to file. Defaults to True.
        highlighter (Highlighter, optional): Highlighter to style log messages, or None to use ReprHighlighter. Defaults to None.
        markup (bool, optional): Enable console markup in log messages. Defaults to False.
        rich_tracebacks (bool, optional): Enable rich tracebacks with syntax highlighting and formatting. Defaults to False.
        tracebacks_width (Optional[int], optional): Number of characters used to render tracebacks, or None for full width. Defaults to None.
        tracebacks_extra_lines (int, optional): Additional lines of code to render tracebacks, or None for full width. Defaults to None.
        tracebacks_theme (str, optional): Override pygments theme used in traceback.
        tracebacks_word_wrap (bool, optional): Enable word wrapping of long tracebacks lines. Defaults to True.
        tracebacks_show_locals (bool, optional): Enable display of locals in tracebacks. Defaults to False.
        tracebacks_suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        log_time_format (Union[str, TimeFormatterCallable], optional): If ``log_time`` is enabled, either string for strftime or callable that formats the time. Defaults to "[%x %X] ".
        keywords (List[str], optional): List of words to highlight instead of ``RichHandler.KEYWORDS``.
    '''
    KEYWORDS: ClassVar[List[str] | None]
    HIGHLIGHTER_CLASS: ClassVar[Type[Highlighter]]
    console: Incomplete
    highlighter: Incomplete
    enable_link_path: Incomplete
    markup: Incomplete
    rich_tracebacks: Incomplete
    tracebacks_width: Incomplete
    tracebacks_extra_lines: Incomplete
    tracebacks_theme: Incomplete
    tracebacks_word_wrap: Incomplete
    tracebacks_show_locals: Incomplete
    tracebacks_suppress: Incomplete
    locals_max_length: Incomplete
    locals_max_string: Incomplete
    keywords: Incomplete
    def __init__(self, level: int | str = ..., console: Console | None = None, *, show_time: bool = True, omit_repeated_times: bool = True, show_level: bool = True, show_path: bool = True, enable_link_path: bool = True, highlighter: Highlighter | None = None, markup: bool = False, rich_tracebacks: bool = False, tracebacks_width: int | None = None, tracebacks_extra_lines: int = 3, tracebacks_theme: str | None = None, tracebacks_word_wrap: bool = True, tracebacks_show_locals: bool = False, tracebacks_suppress: Iterable[str | ModuleType] = (), locals_max_length: int = 10, locals_max_string: int = 80, log_time_format: str | FormatTimeCallable = '[%x %X]', keywords: List[str] | None = None) -> None: ...
    def get_level_text(self, record: LogRecord) -> Text:
        """Get the level name from the record.

        Args:
            record (LogRecord): LogRecord instance.

        Returns:
            Text: A tuple of the style and level name.
        """
    def emit(self, record: LogRecord) -> None:
        """Invoked by logging."""
    def render_message(self, record: LogRecord, message: str) -> ConsoleRenderable:
        """Render message text in to Text.

        Args:
            record (LogRecord): logging Record.
            message (str): String containing log message.

        Returns:
            ConsoleRenderable: Renderable to display log message.
        """
    def render(self, *, record: LogRecord, traceback: Traceback | None, message_renderable: ConsoleRenderable) -> ConsoleRenderable:
        """Render log for display.

        Args:
            record (LogRecord): logging Record.
            traceback (Optional[Traceback]): Traceback instance or None for no Traceback.
            message_renderable (ConsoleRenderable): Renderable (typically Text) containing log message contents.

        Returns:
            ConsoleRenderable: Renderable to display log.
        """
