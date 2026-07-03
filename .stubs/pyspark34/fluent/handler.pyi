import logging
from _typeshed import Incomplete
from fluent import sender as sender

class FluentRecordFormatter(logging.Formatter):
    """ A structured formatter for Fluent.

    Best used with server storing data in an ElasticSearch cluster for example.

    :param fmt: a dict or a callable with format string as values to map to provided keys.
        If callable, should accept a single argument `LogRecord` and return a dict,
        and have a field `usesTime` that is callable and return a bool as would
        `FluentRecordFormatter.usesTime`
    :param datefmt: strftime()-compatible date/time format string.
    :param style: '%', '{' or '$' (used only with Python 3.2 or above)
    :param fill_missing_fmt_key: if True, do not raise a KeyError if the format
        key is not found. Put None if not found.
    :param format_json: if True, will attempt to parse message as json. If not,
        will use message as-is. Defaults to True
    :param exclude_attrs: switches this formatter into a mode where all attributes
        except the ones specified by `exclude_attrs` are logged with the record as is.
        If `None`, operates as before, otherwise `fmt` is ignored.
        Can be an iterable.
    """
    hostname: Incomplete
    fill_missing_fmt_key: Incomplete
    def __init__(self, fmt: Incomplete | None = None, datefmt: Incomplete | None = None, style: str = '%', fill_missing_fmt_key: bool = False, format_json: bool = True, exclude_attrs: Incomplete | None = None) -> None: ...
    def format(self, record): ...
    def usesTime(self) -> None:
        """This method is substituted on construction based on settings for performance reasons"""

class FluentHandler(logging.Handler):
    """
    Logging Handler for fluent.
    """
    tag: Incomplete
    def __init__(self, tag, host: str = 'localhost', port: int = 24224, timeout: float = 3.0, verbose: bool = False, buffer_overflow_handler: Incomplete | None = None, msgpack_kwargs: Incomplete | None = None, nanosecond_precision: bool = False, **kwargs) -> None: ...
    def getSenderClass(self): ...
    @property
    def sender(self): ...
    def getSenderInstance(self, tag, host, port, timeout, verbose, buffer_overflow_handler, msgpack_kwargs, nanosecond_precision, **kwargs): ...
    def emit(self, record): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
