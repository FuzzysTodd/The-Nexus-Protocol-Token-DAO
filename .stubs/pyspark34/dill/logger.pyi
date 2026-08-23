import contextlib
import logging
import os
from _typeshed import Incomplete
from typing import TextIO

__all__ = ['adapter', 'logger', 'trace']

class TraceAdapter(logging.LoggerAdapter):
    '''
    Tracks object tree depth and calculates pickled object size.

    A single instance of this wraps the module\'s logger, as the logging API
    doesn\'t allow setting it directly with a custom Logger subclass.  The added
    \'trace()\' method receives a pickle instance as the first argument and
    creates extra values to be added in the LogRecord from it, then calls
    \'info()\'.

    Usage of logger with \'trace()\' method:

    >>> from dill.logger import adapter as logger  #NOTE: not dill.logger.logger
    >>> ...
    >>> def save_atype(pickler, obj):
    >>>     logger.trace(pickler, "Message with %s and %r etc. placeholders", \'text\', obj)
    >>>     ...
    '''
    logger: Incomplete
    def __init__(self, logger) -> None: ...
    def addHandler(self, handler) -> None: ...
    def removeHandler(self, handler) -> None: ...
    def process(self, msg, kwargs): ...
    def trace_setup(self, pickler) -> None: ...
    def trace(self, pickler, msg, *args, **kwargs) -> None: ...

class TraceFormatter(logging.Formatter):
    """
    Generates message prefix and suffix from record.

    This Formatter adds prefix and suffix strings to the log message in trace
    mode (an also provides empty string defaults for normal logs).
    """
    is_utf8: bool
    def __init__(self, *args, handler: Incomplete | None = None, **kwargs) -> None: ...
    def format(self, record): ...

logger: Incomplete
adapter: Incomplete

def trace(arg: bool | TextIO | str | os.PathLike = None, *, mode: str = 'a') -> None:
    '''print a trace through the stack when pickling; useful for debugging

    With a single boolean argument, enable or disable the tracing.

    Example usage:

        >>> import dill
        >>> dill.detect.trace(True)
        >>> dill.dump_session()

    Alternatively, ``trace()`` can be used as a context manager. With no
    arguments, it just takes care of restoring the tracing state on exit.
    Either a file handle, or a file name and (optionally) a file mode may be
    specitfied to redirect the tracing output in the ``with`` block context. A
    log function is yielded by the manager so the user can write extra
    information to the file.

    Example usage:

        >>> from dill import detect
        >>> D = {\'a\': 42, \'b\': {\'x\': None}}
        >>> with detect.trace():
        >>>     dumps(D)
        ┬ D2: <dict object at 0x7f2721804800>
        ├┬ D2: <dict object at 0x7f27217f5c40>
        │└ # D2 [8 B]
        └ # D2 [22 B]
        >>> squared = lambda x: x**2
        >>> with detect.trace(\'output.txt\', mode=\'w\') as log:
        >>>     log("> D = %r", D)
        >>>     dumps(D)
        >>>     log("> squared = %r", squared)
        >>>     dumps(squared)

    Arguments:
        arg: a boolean value, or an optional file-like or path-like object for the context manager
        mode: mode string for ``open()`` if a file name is passed as the first argument
    '''

class TraceManager(contextlib.AbstractContextManager):
    """context manager version of trace(); can redirect the trace to a file"""
    file: Incomplete
    mode: Incomplete
    redirect: Incomplete
    file_is_stream: Incomplete
    def __init__(self, file, mode) -> None: ...
    handler: Incomplete
    old_level: Incomplete
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...
