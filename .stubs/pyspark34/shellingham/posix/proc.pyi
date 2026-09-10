from ._core import Process as Process
from _typeshed import Incomplete

BSD_STAT_PPID: int
LINUX_STAT_PPID: int
STAT_PATTERN: Incomplete

def detect_proc():
    """Detect /proc filesystem style.

    This checks the /proc/{pid} directory for possible formats. Returns one of
    the following as str:

    * `stat`: Linux-style, i.e. ``/proc/{pid}/stat``.
    * `status`: BSD-style, i.e. ``/proc/{pid}/status``.
    """

class ProcFormatError(EnvironmentError): ...

def iter_process_parents(pid, max_depth: int = 10):
    """Try to look up the process tree via the /proc interface."""
