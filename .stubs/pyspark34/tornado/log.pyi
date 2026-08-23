import logging
from _typeshed import Incomplete
from tornado.util import basestring_type as basestring_type, unicode_type as unicode_type
from typing import Any, Dict

access_log: Incomplete
app_log: Incomplete
gen_log: Incomplete

class LogFormatter(logging.Formatter):
    """Log formatter used in Tornado.

    Key features of this formatter are:

    * Color support when logging to a terminal that supports it.
    * Timestamps on every log line.
    * Robust against str/bytes encoding problems.

    This formatter is enabled automatically by
    `tornado.options.parse_command_line` or `tornado.options.parse_config_file`
    (unless ``--logging=none`` is used).

    Color support on Windows versions that do not support ANSI color codes is
    enabled by use of the colorama__ library. Applications that wish to use
    this must first initialize colorama with a call to ``colorama.init``.
    See the colorama documentation for details.

    __ https://pypi.python.org/pypi/colorama

    .. versionchanged:: 4.5
       Added support for ``colorama``. Changed the constructor
       signature to be compatible with `logging.config.dictConfig`.
    """
    DEFAULT_FORMAT: str
    DEFAULT_DATE_FORMAT: str
    DEFAULT_COLORS: Incomplete
    def __init__(self, fmt: str = ..., datefmt: str = ..., style: str = '%', color: bool = True, colors: Dict[int, int] = ...) -> None:
        """
        :arg bool color: Enables color support.
        :arg str fmt: Log message format.
          It will be applied to the attributes dict of log records. The
          text between ``%(color)s`` and ``%(end_color)s`` will be colored
          depending on the level if color support is on.
        :arg dict colors: color mappings from logging level to terminal color
          code
        :arg str datefmt: Datetime format.
          Used for formatting ``(asctime)`` placeholder in ``prefix_fmt``.

        .. versionchanged:: 3.2

           Added ``fmt`` and ``datefmt`` arguments.
        """
    def format(self, record: Any) -> str: ...

def enable_pretty_logging(options: Any = None, logger: logging.Logger | None = None) -> None:
    """Turns on formatted logging output as configured.

    This is called automatically by `tornado.options.parse_command_line`
    and `tornado.options.parse_config_file`.
    """
def define_logging_options(options: Any = None) -> None:
    """Add logging-related flags to ``options``.

    These options are present automatically on the default options instance;
    this method is only necessary if you have created your own `.OptionParser`.

    .. versionadded:: 4.2
        This function existed in prior versions but was broken and undocumented until 4.2.
    """
