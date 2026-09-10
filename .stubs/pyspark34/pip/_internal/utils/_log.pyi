import logging
from typing import Any

VERBOSE: int

class VerboseLogger(logging.Logger):
    """Custom Logger, defining a verbose log-level

    VERBOSE is between INFO and DEBUG.
    """
    def verbose(self, msg: str, *args: Any, **kwargs: Any) -> None: ...

def getLogger(name: str) -> VerboseLogger:
    """logging.getLogger, but ensures our VerboseLogger class is returned"""
def init_logging() -> None:
    """Register our VerboseLogger and VERBOSE log level.

    Should be called before any calls to getLogger(),
    i.e. in pip._internal.__init__
    """
