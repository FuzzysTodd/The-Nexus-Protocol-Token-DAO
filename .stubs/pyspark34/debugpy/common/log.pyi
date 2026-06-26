from _typeshed import Incomplete
from collections.abc import Generator
from debugpy.common import json as json, timestamp as timestamp, util as util

LEVELS: Incomplete
log_dir: Incomplete
timestamp_format: str

class LogFile:
    filename: Incomplete
    file: Incomplete
    close_file: Incomplete
    def __init__(self, filename, file, levels=..., close_file: bool = True) -> None: ...
    @property
    def levels(self): ...
    @levels.setter
    def levels(self, value) -> None: ...
    def write(self, level, output) -> None: ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class NoLog:
    file: Incomplete
    filename: Incomplete
    __bool__: Incomplete
    __nonzero__: Incomplete
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def newline(level: str = 'info') -> None: ...
def write(level, text, _to_files=...): ...
def write_format(level, format_string, *args, **kwargs): ...

debug: Incomplete
info: Incomplete
warning: Incomplete

def error(*args, **kwargs):
    """Logs an error.

    Returns the output wrapped in AssertionError. Thus, the following::

        raise log.error(s, ...)

    has the same effect as::

        log.error(...)
        assert False, (s.format(...))
    """
def swallow_exception(format_string: str = '', *args, **kwargs) -> None:
    '''Logs an exception with full traceback.

    If format_string is specified, it is formatted with format(*args, **kwargs), and
    prepended to the exception traceback on a separate line.

    If exc_info is specified, the exception it describes will be logged. Otherwise,
    sys.exc_info() - i.e. the exception being handled currently - will be logged.

    If level is specified, the exception will be logged as a message of that level.
    The default is "error".
    '''
def reraise_exception(format_string: str = '', *args, **kwargs) -> None:
    """Like swallow_exception(), but re-raises the current exception after logging it."""
def to_file(filename: Incomplete | None = None, prefix: Incomplete | None = None, levels=...):
    '''Starts logging all messages at the specified levels to the designated file.

    Either filename or prefix must be specified, but not both.

    If filename is specified, it designates the log file directly.

    If prefix is specified, the log file is automatically created in options.log_dir,
    with filename computed as prefix + os.getpid(). If log_dir is None, no log file
    is created, and the function returns immediately.

    If the file with the specified or computed name is already being used as a log
    file, it is not overwritten, but its levels are updated as specified.

    The function returns an object with a close() method. When the object is closed,
    logs are not written into that file anymore. Alternatively, the returned object
    can be used in a with-statement:

        with log.to_file("some.log"):
            # now also logging to some.log
        # not logging to some.log anymore
    '''
def prefixed(format_string, *args, **kwargs) -> Generator[None, None, None]:
    """Adds a prefix to all messages logged from the current thread for the duration
    of the context manager.
    """
def get_environment_description(header): ...
def describe_environment(header) -> None: ...

stderr: Incomplete
