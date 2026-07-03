from _typeshed import Incomplete

LOGGING_LINE_FORMAT: str
LOGGING_DATETIME_FORMAT: str

class MlflowLoggingStream:
    """
    A Python stream for use with event logging APIs throughout MLflow (`eprint()`,
    `logger.info()`, etc.). This stream wraps `sys.stderr`, forwarding `write()` and
    `flush()` calls to the stream referred to by `sys.stderr` at the time of the call.
    It also provides capabilities for disabling the stream to silence event logs.
    """
    def __init__(self) -> None: ...
    def write(self, text) -> None: ...
    def flush(self) -> None: ...
    @property
    def enabled(self): ...
    @enabled.setter
    def enabled(self, value) -> None: ...

MLFLOW_LOGGING_STREAM: Incomplete

def disable_logging() -> None:
    """
    Disables the `MlflowLoggingStream` used by event logging APIs throughout MLflow
    (`eprint()`, `logger.info()`, etc), silencing all subsequent event logs.
    """
def enable_logging() -> None:
    """
    Enables the `MlflowLoggingStream` used by event logging APIs throughout MLflow
    (`eprint()`, `logger.info()`, etc), emitting all subsequent event logs. This
    reverses the effects of `disable_logging()`.
    """
def eprint(*args, **kwargs) -> None: ...
