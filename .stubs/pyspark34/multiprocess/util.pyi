import threading
from _typeshed import Incomplete

__all__ = ['sub_debug', 'debug', 'info', 'sub_warning', 'get_logger', 'log_to_stderr', 'get_temp_dir', 'register_after_fork', 'is_exiting', 'Finalize', 'ForkAwareThreadLock', 'ForkAwareLocal', 'close_all_fds_except', 'SUBDEBUG', 'SUBWARNING']

SUBDEBUG: int
SUBWARNING: int

def sub_debug(msg, *args) -> None: ...
def debug(msg, *args) -> None: ...
def info(msg, *args) -> None: ...
def sub_warning(msg, *args) -> None: ...
def get_logger():
    """
    Returns logger used by multiprocess
    """
def log_to_stderr(level: Incomplete | None = None):
    """
    Turn on logging and add a handler which prints to stderr
    """
def get_temp_dir(): ...
def register_after_fork(obj, func) -> None: ...

class Finalize:
    """
    Class which supports object finalization using weakrefs
    """
    def __init__(self, obj, callback, args=(), kwargs: Incomplete | None = None, exitpriority: Incomplete | None = None) -> None: ...
    def __call__(self, wr: Incomplete | None = None, _finalizer_registry=..., sub_debug=..., getpid=...):
        """
        Run the callback unless it has already been called or cancelled
        """
    def cancel(self) -> None:
        """
        Cancel finalization of the object
        """
    def still_active(self):
        """
        Return whether this finalizer is still waiting to invoke callback
        """

def is_exiting():
    """
    Returns true if the process is shutting down
    """

class ForkAwareThreadLock:
    acquire: Incomplete
    release: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

class ForkAwareLocal(threading.local):
    def __init__(self) -> None: ...
    def __reduce__(self): ...

def close_all_fds_except(fds) -> None: ...
