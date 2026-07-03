import ctypes
from _typeshed import Incomplete
from shellingham._core import SHELL_NAMES as SHELL_NAMES

INVALID_HANDLE_VALUE: Incomplete
ERROR_NO_MORE_FILES: int
ERROR_INSUFFICIENT_BUFFER: int
TH32CS_SNAPPROCESS: int
PROCESS_QUERY_LIMITED_INFORMATION: int
kernel32: Incomplete

class ProcessEntry32(ctypes.Structure): ...

def get_shell(pid: Incomplete | None = None, max_depth: int = 10): ...
