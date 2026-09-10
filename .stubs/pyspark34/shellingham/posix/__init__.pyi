from . import proc as proc, ps as ps
from _typeshed import Incomplete

QEMU_BIN_REGEX: Incomplete

def get_shell(pid: Incomplete | None = None, max_depth: int = 10):
    """Get the shell that the supplied pid or os.getpid() is running in."""
