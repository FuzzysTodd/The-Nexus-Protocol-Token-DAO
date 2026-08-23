from ._common import AF_INET6 as AF_INET6, AccessDenied as AccessDenied, NoSuchProcess as NoSuchProcess, ZombieProcess as ZombieProcess, debug as debug, get_procfs_path as get_procfs_path, isfile_strict as isfile_strict, memoize_when_activated as memoize_when_activated, sockfam_to_enum as sockfam_to_enum, socktype_to_enum as socktype_to_enum, usage_percent as usage_percent
from ._compat import FileNotFoundError as FileNotFoundError, PY3 as PY3, PermissionError as PermissionError, ProcessLookupError as ProcessLookupError, b as b
from _typeshed import Incomplete
from typing import NamedTuple

__extra__all__: Incomplete
PAGE_SIZE: Incomplete
AF_LINK: Incomplete
IS_64_BIT: Incomplete
CONN_IDLE: str
CONN_BOUND: str
PROC_STATUSES: Incomplete
TCP_STATUSES: Incomplete
proc_info_map: Incomplete

class scputimes(NamedTuple):
    user: Incomplete
    system: Incomplete
    idle: Incomplete
    iowait: Incomplete

class pcputimes(NamedTuple):
    user: Incomplete
    system: Incomplete
    children_user: Incomplete
    children_system: Incomplete

class svmem(NamedTuple):
    total: Incomplete
    available: Incomplete
    percent: Incomplete
    used: Incomplete
    free: Incomplete

class pmem(NamedTuple):
    rss: Incomplete
    vms: Incomplete
pfullmem = pmem

class pmmap_grouped(NamedTuple):
    path: Incomplete
    rss: Incomplete
    anonymous: Incomplete
    locked: Incomplete

pmmap_ext: Incomplete

def virtual_memory():
    """Report virtual memory metrics."""
def swap_memory():
    """Report swap memory metrics."""
def cpu_times():
    """Return system-wide CPU times as a named tuple"""
def per_cpu_times():
    """Return system per-CPU times as a list of named tuples"""
def cpu_count_logical():
    """Return the number of logical CPUs in the system."""
def cpu_count_cores():
    """Return the number of CPU cores in the system."""
def cpu_stats():
    """Return various CPU stats as a named tuple."""

disk_io_counters: Incomplete
disk_usage: Incomplete

def disk_partitions(all: bool = False):
    """Return system disk partitions."""

net_io_counters: Incomplete
net_if_addrs: Incomplete

def net_connections(kind, _pid: int = -1):
    """Return socket connections.  If pid == -1 return system-wide
    connections (as opposed to connections opened by one process only).
    Only INET sockets are returned (UNIX are not).
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
    def nice_get(self): ...
    def nice_set(self, value): ...
    def ppid(self): ...
    def uids(self): ...
    def gids(self): ...
    def cpu_times(self): ...
    def cpu_num(self): ...
    def terminal(self): ...
    def cwd(self): ...
    def memory_info(self): ...
    memory_full_info = memory_info
    def status(self): ...
    def threads(self): ...
    def open_files(self): ...
    def connections(self, kind: str = 'inet'): ...

    class nt_mmap_grouped(NamedTuple):
        path: Incomplete
        rss: Incomplete
        anon: Incomplete
        locked: Incomplete

    class nt_mmap_ext(NamedTuple):
        addr: Incomplete
        perms: Incomplete
        path: Incomplete
        rss: Incomplete
        anon: Incomplete
        locked: Incomplete
    def memory_maps(self): ...
    def num_fds(self): ...
    def num_ctx_switches(self): ...
    def wait(self, timeout: Incomplete | None = None): ...
