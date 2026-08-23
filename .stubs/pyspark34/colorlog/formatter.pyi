import logging
import typing
from _typeshed import Incomplete

__all__ = ['default_log_colors', 'ColoredFormatter', 'LevelFormatter', 'TTYColoredFormatter']

default_log_colors: Incomplete

class ColoredRecord:
    """
    Wraps a LogRecord, adding escape codes to the internal dict.

    The internal dict is used when formatting the message (by the PercentStyle,
    StrFormatStyle, and StringTemplateStyle classes).
    """
    def __init__(self, record: logging.LogRecord, escapes: EscapeCodes) -> None: ...

class ColoredFormatter(logging.Formatter):
    """
    A formatter that allows colors to be placed in the format string.

    Intended to help in creating more readable logging output.
    """
    log_colors: Incomplete
    secondary_log_colors: Incomplete
    reset: Incomplete
    stream: Incomplete
    no_color: Incomplete
    force_color: Incomplete
    def __init__(self, fmt: str | None = None, datefmt: str | None = None, style: _FormatStyle = '%', log_colors: LogColors | None = None, reset: bool = True, secondary_log_colors: SecondaryLogColors | None = None, validate: bool = True, stream: typing.IO | None = None, no_color: bool = False, force_color: bool = False, defaults: typing.Mapping[str, typing.Any] | None = None) -> None:
        """
        Set the format and colors the ColoredFormatter will use.

        The ``fmt``, ``datefmt``, ``style``, and ``default`` args are passed on to the
        ``logging.Formatter`` constructor.

        The ``secondary_log_colors`` argument can be used to create additional
        ``log_color`` attributes. Each key in the dictionary will set
        ``{key}_log_color``, using the value to select from a different
        ``log_colors`` set.

        :Parameters:
        - fmt (str): The format string to use.
        - datefmt (str): A format string for the date.
        - log_colors (dict):
            A mapping of log level names to color names.
        - reset (bool):
            Implicitly append a color reset to all records unless False.
        - style ('%' or '{' or '$'):
            The format style to use.
        - secondary_log_colors (dict):
            Map secondary ``log_color`` attributes. (*New in version 2.6.*)
        - validate (bool)
            Validate the format string.
        - stream (typing.IO)
            The stream formatted messages will be printed to. Used to toggle colour
            on non-TTY outputs. Optional.
        - no_color (bool):
            Disable color output.
        - force_color (bool):
            Enable color output. Takes precedence over `no_color`.
        """
    def formatMessage(self, record: logging.LogRecord) -> str:
        """Format a message from a record object."""

class LevelFormatter:
    """An extension of ColoredFormatter that uses per-level format strings."""
    formatters: Incomplete
    def __init__(self, fmt: typing.Mapping[str, str], **kwargs: typing.Any) -> None:
        '''
        Configure a ColoredFormatter with its own format string for each log level.

        Supports fmt as a dict. All other args are passed on to the
        ``colorlog.ColoredFormatter`` constructor.

        :Parameters:
        - fmt (dict):
            A mapping of log levels (represented as strings, e.g. \'WARNING\') to
            format strings. (*New in version 2.7.0)
        (All other parameters are the same as in colorlog.ColoredFormatter)

        Example:

        formatter = colorlog.LevelFormatter(
            fmt={
                "DEBUG": "%(log_color)s%(message)s (%(module)s:%(lineno)d)",
                "INFO": "%(log_color)s%(message)s",
                "WARNING": "%(log_color)sWRN: %(message)s (%(module)s:%(lineno)d)",
                "ERROR": "%(log_color)sERR: %(message)s (%(module)s:%(lineno)d)",
                "CRITICAL": "%(log_color)sCRT: %(message)s (%(module)s:%(lineno)d)",
            }
        )
        '''
    def format(self, record: logging.LogRecord) -> str: ...
TTYColoredFormatter = ColoredFormatter
