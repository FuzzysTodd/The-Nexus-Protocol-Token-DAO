from .disk import mkdirp as mkdirp
from _typeshed import Incomplete

def format_time(t): ...
def short_format_time(t): ...
def pformat(obj, indent: int = 0, depth: int = 3): ...

class Logger:
    """ Base class for logging messages.
    """
    depth: Incomplete
    def __init__(self, depth: int = 3, name: Incomplete | None = None) -> None:
        """
            Parameters
            ----------
            depth: int, optional
                The depth of objects printed.
            name: str, optional
                The namespace to log to. If None, defaults to joblib.
        """
    def warn(self, msg) -> None: ...
    def info(self, msg) -> None: ...
    def debug(self, msg) -> None: ...
    def format(self, obj, indent: int = 0):
        """Return the formatted representation of the object."""

class PrintTime:
    """ Print and log messages while keeping track of time.
    """
    last_time: Incomplete
    start_time: Incomplete
    logfile: Incomplete
    def __init__(self, logfile: Incomplete | None = None, logdir: Incomplete | None = None) -> None: ...
    def __call__(self, msg: str = '', total: bool = False) -> None:
        """ Print the time elapsed between the last call and the current
            call, with an optional message.
        """
