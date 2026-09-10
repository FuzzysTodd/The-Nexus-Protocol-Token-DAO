from ._common import AccessDenied as AccessDenied, NIC_DUPLEX_FULL as NIC_DUPLEX_FULL, NIC_DUPLEX_HALF as NIC_DUPLEX_HALF, NIC_DUPLEX_UNKNOWN as NIC_DUPLEX_UNKNOWN, NoSuchProcess as NoSuchProcess, ZombieProcess as ZombieProcess, conn_to_ntuple as conn_to_ntuple, get_procfs_path as get_procfs_path, memoize_when_activated as memoize_when_activated, usage_percent as usage_percent
from ._compat import FileNotFoundError as FileNotFoundError, PY3 as PY3, PermissionError as PermissionError, ProcessLookupError as ProcessLookupError
from _typeshed import Incomplete
from typing import NamedTuple

__extra__all__: Incomplete
HAS_THREADS: Incomplete
HAS_NET_IO_COUNTERS: Incomplete
HAS_PROC_IO_COUNTERS: Incomplete
PAGE_SIZE: Incomplete
AF_LINK: Incomplete
PROC_STATUSES: Incomplete
TCP_STATUSES: Incomplete
proc_info_map: Incomplete

class pmem(NamedTuple):
    rss: Incomplete
    vms: Incomplete
pfullmem = pmem

class scputimes(NamedTuple):
    user: Incomplete
    system: Incomplete
    idle: Incomplete
    iowait: Incomplete

class svmem(NamedTuple):
    total: Incomplete
    available: Incomplete
    percent: Incomplete
    used: Incomplete
    free: Incomplete

def virtual_memory(): ...
def swap_memory():
    """Swap system memory as a (total, used, free, sin, sout) tuple."""
def cpu_times():
    """Return system-wide CPU times as a named tuple"""
def per_cpu_times():
    """Return system per-CPU times as a list of named tuples"""
def cpu_count_logical():
    """Return the number of logical CPUs in the system."""
def cpu_count_cores(): ...
def cpu_stats():
    """Return various CPU stats as a named tuple."""

disk_io_counters: Incomplete
disk_usage: Incomplete

def disk_partitions(all: bool = False):
    """Return system disk partitions."""

net_if_addrs: Incomplete
net_io_counters: Incomplete

def net_connections(kind, _pid: int = -1):
    """Return socket connections.  If pid == -1 return system-wide
    connections (as opposed to connections opened by one process only).
    """
def net_if_stats():
    """Get NIC stats (isup, duplex, speed, mtu)."""
def boot_time():
    """The system boot time expressed in seconds since the epoch."""
def users():
    """Return currently connected users as a list of namedtuples."""
def pids():
    """Returns a list of PIDs currently running on the system."""
def pid_exists(pid):
    """Check for the existence of a unix pid."""
def wrap_exceptions(fun):
    """Call callable into a try/except clause and translate ENOENT,
    EACCES and EPERM in NoSuchProcess or AccessDenied exceptions.
    """

class Process:
    """Wrapper class around underlying C implementation."""
    pid: Incomplete
    def __init__(self, pid) -> None: ...
    def oneshot_enter(self) -> None: ...
    def oneshot_exit(self) -> None: ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def environ(self): ...
    def create_time(self): ...
    def num_threads(self): ...
    def threads(self): ...
    def connections(self, kind: str = 'inet'): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def ppid(self): ...
    def uids(self): ...
    def gids(self): ...
    def cpu_times(self): ...
    def terminal(self): ...
    def cwd(self): ...
    def memory_info(self): ...
    memory_full_info = memory_info
    def status(self): ...
    def open_files(self): ...
    def num_fds(self): ...
    def num_ctx_switches(self): ...
    def wait(self, timeout: Incomplete | None = None): ...
    def io_counters(self): ...
