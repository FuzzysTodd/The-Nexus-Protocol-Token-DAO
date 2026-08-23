import logging
from _typeshed import Incomplete
from absl import flags as flags
from absl.logging import converter as converter
from typing import Any, NoReturn

FLAGS: Incomplete
FATAL: Incomplete
ERROR: Incomplete
WARNING: Incomplete
WARN: Incomplete
INFO: Incomplete
DEBUG: Incomplete
ABSL_LOGGING_PREFIX_REGEX: str

class _VerbosityFlag(flags.Flag):
    """Flag class for -v/--verbosity."""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, v) -> None: ...

class _LoggerLevelsFlag(flags.Flag):
    """Flag class for --logger_levels."""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, v) -> None: ...

class _LoggerLevelsParser(flags.ArgumentParser):
    """Parser for --logger_levels flag."""
    def parse(self, value): ...

class _LoggerLevelsSerializer:
    """Serializer for --logger_levels flag."""
    def serialize(self, value): ...

class _StderrthresholdFlag(flags.Flag):
    """Flag class for --stderrthreshold."""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, v) -> None: ...

LOGTOSTDERR: Incomplete
ALSOLOGTOSTDERR: Incomplete
LOG_DIR: Incomplete
VERBOSITY: Incomplete
LOGGER_LEVELS: Incomplete
STDERRTHRESHOLD: Incomplete
SHOWPREFIXFORINFO: Incomplete

def get_verbosity():
    """Returns the logging verbosity."""
def set_verbosity(v) -> None:
    """Sets the logging verbosity.

  Causes all messages of level <= v to be logged,
  and all messages of level > v to be silently discarded.

  Args:
    v: int|str, the verbosity level as an integer or string. Legal string values
        are those that can be coerced to an integer as well as case-insensitive
        'debug', 'info', 'warning', 'error', and 'fatal'.
  """
def set_stderrthreshold(s) -> None:
    """Sets the stderr threshold to the value passed in.

  Args:
    s: str|int, valid strings values are case-insensitive 'debug',
        'info', 'warning', 'error', and 'fatal'; valid integer values are
        logging.DEBUG|INFO|WARNING|ERROR|FATAL.

  Raises:
      ValueError: Raised when s is an invalid value.
  """
def fatal(msg: Any, *args: Any, **kwargs: Any) -> NoReturn:
    """Logs a fatal message."""
def error(msg, *args, **kwargs) -> None:
    """Logs an error message."""
def warning(msg, *args, **kwargs) -> None:
    """Logs a warning message."""
def warn(msg, *args, **kwargs) -> None:
    """Deprecated, use 'warning' instead."""
def info(msg, *args, **kwargs) -> None:
    """Logs an info message."""
def debug(msg, *args, **kwargs) -> None:
    """Logs a debug message."""
def exception(msg, *args, exc_info: bool = True, **kwargs) -> None:
    """Logs an exception, with traceback and message."""
def log_every_n(level, msg, n, *args) -> None:
    """Logs ``msg % args`` at level 'level' once per 'n' times.

  Logs the 1st call, (N+1)st call, (2N+1)st call,  etc.
  Not threadsafe.

  Args:
    level: int, the absl logging level at which to log.
    msg: str, the message to be logged.
    n: int, the number of times this should be called before it is logged.
    *args: The args to be substituted into the msg.
  """
def log_every_n_seconds(level, msg, n_seconds, *args) -> None:
    """Logs ``msg % args`` at level ``level`` iff ``n_seconds`` elapsed since last call.

  Logs the first call, logs subsequent calls if 'n' seconds have elapsed since
  the last logging call from the same call site (file + line). Not thread-safe.

  Args:
    level: int, the absl logging level at which to log.
    msg: str, the message to be logged.
    n_seconds: float or int, seconds which should elapse before logging again.
    *args: The args to be substituted into the msg.
  """
def log_first_n(level, msg, n, *args) -> None:
    """Logs ``msg % args`` at level ``level`` only first ``n`` times.

  Not threadsafe.

  Args:
    level: int, the absl logging level at which to log.
    msg: str, the message to be logged.
    n: int, the maximal number of times the message is logged.
    *args: The args to be substituted into the msg.
  """
def log_if(level, msg, condition, *args) -> None:
    """Logs ``msg % args`` at level ``level`` only if condition is fulfilled."""
def log(level, msg, *args, **kwargs) -> None:
    """Logs ``msg % args`` at absl logging level ``level``.

  If no args are given just print msg, ignoring any interpolation specifiers.

  Args:
    level: int, the absl logging level at which to log the message
        (logging.DEBUG|INFO|WARNING|ERROR|FATAL). While some C++ verbose logging
        level constants are also supported, callers should prefer explicit
        logging.vlog() calls for such purpose.

    msg: str, the message to be logged.
    *args: The args to be substituted into the msg.
    **kwargs: May contain exc_info to add exception traceback to message.
  """
def vlog(level, msg, *args, **kwargs) -> None:
    """Log ``msg % args`` at C++ vlog level ``level``.

  Args:
    level: int, the C++ verbose logging level at which to log the message,
        e.g. 1, 2, 3, 4... While absl level constants are also supported,
        callers should prefer logging.log|debug|info|... calls for such purpose.
    msg: str, the message to be logged.
    *args: The args to be substituted into the msg.
    **kwargs: May contain exc_info to add exception traceback to message.
  """
def vlog_is_on(level):
    """Checks if vlog is enabled for the given level in caller's source file.

  Args:
    level: int, the C++ verbose logging level at which to log the message,
        e.g. 1, 2, 3, 4... While absl level constants are also supported,
        callers should prefer level_debug|level_info|... calls for
        checking those.

  Returns:
    True if logging is turned on for that level.
  """
def flush() -> None:
    """Flushes all log files."""
def level_debug():
    """Returns True if debug logging is turned on."""
def level_info():
    """Returns True if info logging is turned on."""
def level_warning():
    """Returns True if warning logging is turned on."""
level_warn = level_warning

def level_error():
    """Returns True if error logging is turned on."""
def get_log_file_name(level=...):
    """Returns the name of the log file.

  For Python logging, only one file is used and level is ignored. And it returns
  empty string if it logs to stderr/stdout or the log stream has no `name`
  attribute.

  Args:
    level: int, the absl.logging level.

  Raises:
    ValueError: Raised when `level` has an invalid value.
  """
def find_log_dir_and_names(program_name: Incomplete | None = None, log_dir: Incomplete | None = None):
    """Computes the directory and filename prefix for log file.

  Args:
    program_name: str|None, the filename part of the path to the program that
        is running without its extension.  e.g: if your program is called
        ``usr/bin/foobar.py`` this method should probably be called with
        ``program_name='foobar`` However, this is just a convention, you can
        pass in any string you want, and it will be used as part of the
        log filename. If you don't pass in anything, the default behavior
        is as described in the example.  In python standard logging mode,
        the program_name will be prepended with ``py_`` if it is the
        ``program_name`` argument is omitted.
    log_dir: str|None, the desired log directory.

  Returns:
    (log_dir, file_prefix, symlink_prefix)

  Raises:
    FileNotFoundError: raised in Python 3 when it cannot find a log directory.
    OSError: raised in Python 2 when it cannot find a log directory.
  """
def find_log_dir(log_dir: Incomplete | None = None):
    """Returns the most suitable directory to put log files into.

  Args:
    log_dir: str|None, if specified, the logfile(s) will be created in that
        directory.  Otherwise if the --log_dir command-line flag is provided,
        the logfile will be created in that directory.  Otherwise the logfile
        will be created in a standard location.

  Raises:
    FileNotFoundError: raised in Python 3 when it cannot find a log directory.
    OSError: raised in Python 2 when it cannot find a log directory.
  """
def get_absl_log_prefix(record):
    """Returns the absl log prefix for the log record.

  Args:
    record: logging.LogRecord, the record to get prefix for.
  """
def skip_log_prefix(func):
    """Skips reporting the prefix of a given function or name by :class:`~absl.logging.ABSLLogger`.

  This is a convenience wrapper function / decorator for
  :meth:`~absl.logging.ABSLLogger.register_frame_to_skip`.

  If a callable function is provided, only that function will be skipped.
  If a function name is provided, all functions with the same name in the
  file that this is called in will be skipped.

  This can be used as a decorator of the intended function to be skipped.

  Args:
    func: Callable function or its name as a string.

  Returns:
    func (the input, unchanged).

  Raises:
    ValueError: The input is callable but does not have a function code object.
    TypeError: The input is neither callable nor a string.
  """

class PythonHandler(logging.StreamHandler):
    """The handler class used by Abseil Python logging implementation."""
    def __init__(self, stream: Incomplete | None = None, formatter: Incomplete | None = None) -> None: ...
    stream: Incomplete
    def start_logging_to_file(self, program_name: Incomplete | None = None, log_dir: Incomplete | None = None) -> None:
        """Starts logging messages to files instead of standard error."""
    def use_absl_log_file(self, program_name: Incomplete | None = None, log_dir: Incomplete | None = None) -> None:
        """Conditionally logs to files, based on --logtostderr."""
    def flush(self) -> None:
        """Flushes all log files."""
    def emit(self, record) -> None:
        """Prints a record out to some streams.

    1. If ``FLAGS.logtostderr`` is set, it will print to ``sys.stderr`` ONLY.
    2. If ``FLAGS.alsologtostderr`` is set, it will print to ``sys.stderr``.
    3. If ``FLAGS.logtostderr`` is not set, it will log to the stream
        associated with the current thread.

    Args:
      record: :class:`logging.LogRecord`, the record to emit.
    """
    def close(self) -> None:
        """Closes the stream to which we are writing."""

class ABSLHandler(logging.Handler):
    """Abseil Python logging module's log handler."""
    def __init__(self, python_logging_formatter) -> None: ...
    def format(self, record): ...
    def setFormatter(self, fmt) -> None: ...
    def emit(self, record) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def handle(self, record): ...
    @property
    def python_handler(self): ...
    def activate_python_handler(self) -> None:
        """Uses the Python logging handler as the current logging handler."""
    def use_absl_log_file(self, program_name: Incomplete | None = None, log_dir: Incomplete | None = None) -> None: ...
    def start_logging_to_file(self, program_name: Incomplete | None = None, log_dir: Incomplete | None = None) -> None: ...

class PythonFormatter(logging.Formatter):
    """Formatter class used by :class:`~absl.logging.PythonHandler`."""
    def format(self, record):
        """Appends the message from the record to the results of the prefix.

    Args:
      record: logging.LogRecord, the record to be formatted.

    Returns:
      The formatted string representing the record.
    """

class ABSLLogger(Incomplete):
    """A logger that will create LogRecords while skipping some stack frames.

  This class maintains an internal list of filenames and method names
  for use when determining who called the currently executing stack
  frame.  Any method names from specific source files are skipped when
  walking backwards through the stack.

  Client code should use the register_frame_to_skip method to let the
  ABSLLogger know which method from which file should be
  excluded from the walk backwards through the stack.
  """
    def findCaller(self, stack_info: bool = False, stacklevel: int = 1):
        """Finds the frame of the calling method on the stack.

    This method skips any frames registered with the
    ABSLLogger and any methods from this file, and whatever
    method is currently being used to generate the prefix for the log
    line.  Then it returns the file name, line number, and method name
    of the calling method.  An optional fourth item may be returned,
    callers who only need things from the first three are advised to
    always slice or index the result rather than using direct unpacking
    assignment.

    Args:
      stack_info: bool, when True, include the stack trace as a fourth item
          returned.  On Python 3 there are always four items returned - the
          fourth will be None when this is False.  On Python 2 the stdlib
          base class API only returns three items.  We do the same when this
          new parameter is unspecified or False for compatibility.

    Returns:
      (filename, lineno, methodname[, sinfo]) of the calling method.
    """
    def critical(self, msg, *args, **kwargs) -> None:
        """Logs ``msg % args`` with severity ``CRITICAL``."""
    def fatal(self, msg, *args, **kwargs) -> None:
        """Logs ``msg % args`` with severity ``FATAL``."""
    def error(self, msg, *args, **kwargs) -> None:
        """Logs ``msg % args`` with severity ``ERROR``."""
    def warn(self, msg, *args, **kwargs) -> None:
        """Logs ``msg % args`` with severity ``WARN``."""
    def warning(self, msg, *args, **kwargs) -> None:
        """Logs ``msg % args`` with severity ``WARNING``."""
    def info(self, msg, *args, **kwargs) -> None:
        """Logs ``msg % args`` with severity ``INFO``."""
    def debug(self, msg, *args, **kwargs) -> None:
        """Logs ``msg % args`` with severity ``DEBUG``."""
    def log(self, level, msg, *args, **kwargs) -> None:
        """Logs a message at a cetain level substituting in the supplied arguments.

    This method behaves differently in python and c++ modes.

    Args:
      level: int, the standard logging level at which to log the message.
      msg: str, the text of the message to log.
      *args: The arguments to substitute in the message.
      **kwargs: The keyword arguments to substitute in the message.
    """
    def handle(self, record) -> None:
        """Calls handlers without checking ``Logger.disabled``.

    Non-root loggers are set to disabled after setup with :func:`logging.config`
    if it's not explicitly specified. Historically, absl logging will not be
    disabled by that. To maintaining this behavior, this function skips
    checking the ``Logger.disabled`` bit.

    This logger can still be disabled by adding a filter that filters out
    everything.

    Args:
      record: logging.LogRecord, the record to handle.
    """
    @classmethod
    def register_frame_to_skip(cls, file_name, function_name, line_number: Incomplete | None = None) -> None:
        """Registers a function name to skip when walking the stack.

    The :class:`~absl.logging.ABSLLogger` sometimes skips method calls on the
    stack to make the log messages meaningful in their appropriate context.
    This method registers a function from a particular file as one
    which should be skipped.

    Args:
      file_name: str, the name of the file that contains the function.
      function_name: str, the name of the function to skip.
      line_number: int, if provided, only the function with this starting line
          number will be skipped. Otherwise, all functions with the same name
          in the file will be skipped.
    """

def get_absl_logger():
    """Returns the absl logger instance."""
def get_absl_handler():
    """Returns the absl handler instance."""
def use_python_logging(quiet: bool = False) -> None:
    """Uses the python implementation of the logging code.

  Args:
    quiet: No logging message about switching logging type.
  """
def use_absl_handler() -> None:
    """Uses the ABSL logging handler for logging.

  This method is called in :func:`app.run()<absl.app.run>` so the absl handler
  is used in absl apps.
  """
