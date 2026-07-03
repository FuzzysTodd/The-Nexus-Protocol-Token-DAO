import logging
from _typeshed import Incomplete

DEBUG: Incomplete
INFO: Incomplete
WARN: Incomplete
ERROR: Incomplete
FATAL: Incomplete
log: Incomplete
debug: Incomplete
info: Incomplete
warn: Incomplete
error: Incomplete
fatal: Incomplete

def set_threshold(level): ...
def set_verbosity(v) -> None: ...

class Log(logging.Logger):
    """distutils.log.Log is deprecated, please use an alternative from `logging`."""
    def __init__(self, threshold=...) -> None: ...
    @property
    def threshold(self): ...
    @threshold.setter
    def threshold(self, level) -> None: ...
    warn: Incomplete
