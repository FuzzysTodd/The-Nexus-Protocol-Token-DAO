from _typeshed import Incomplete
from io import TextIOBase
from logging import Formatter, LogRecord

__all__ = ['enable_global_logging', 'silence_stdout']

def silence_stdout() -> None:
    """
    Stop NNI from printing to stdout.

    By default NNI prints log messages of ``INFO`` and higher levels to console.
    Use this function if you want a clean stdout, or if you want to handle logs by yourself.
    """
def enable_global_logging(enable: bool = True) -> None:
    """
    Let NNI to handle all logs. Useful for debugging.

    By default only NNI's logs are printed to stdout and saved to ``nni-experiments`` log files.
    The function will extend these settings to all modules' logs.

    Use ``enable_global_logging(False)`` to reverse it.
    The log level of root logger will not be reversed though.
    """

class _StdoutFormatter(Formatter):
    def __init__(self) -> None: ...
    def formatMessage(self, record: LogRecord) -> str: ...

class _LogFileFormatter(Formatter):
    def __init__(self) -> None: ...
    def formatMessage(self, record: LogRecord) -> str: ...

class _LogFileWrapper(TextIOBase):
    file: Incomplete
    line_buffer: Incomplete
    line_start_time: Incomplete
    def __init__(self, log_file: TextIOBase) -> None: ...
    def write(self, s: str) -> int: ...
    def flush(self) -> None: ...
