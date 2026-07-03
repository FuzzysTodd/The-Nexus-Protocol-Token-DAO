import ctypes
from _typeshed import Incomplete
from debugpy.common import log as log

JOBOBJECTCLASS = ctypes.c_int
LPDWORD: Incomplete
LPVOID = ctypes.c_void_p
SIZE_T = ctypes.c_size_t
ULONGLONG = ctypes.c_ulonglong

class IO_COUNTERS(ctypes.Structure): ...
class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure): ...
class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure): ...

JobObjectExtendedLimitInformation: Incomplete
JOB_OBJECT_LIMIT_BREAKAWAY_OK: int
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE: int
PROCESS_TERMINATE: int
PROCESS_SET_QUOTA: int
kernel32: Incomplete
