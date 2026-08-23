from ._common import AccessDenied as AccessDenied, NoSuchProcess as NoSuchProcess, ZombieProcess as ZombieProcess, conn_tmap as conn_tmap, conn_to_ntuple as conn_to_ntuple, isfile_strict as isfile_strict, memoize_when_activated as memoize_when_activated, parse_environ_block as parse_environ_block, usage_percent as usage_percent
from ._compat import PermissionError as PermissionError, ProcessLookupError as ProcessLookupError
from _typeshed import Incomplete
from typing import NamedTuple

__extra__all__: Incomplete
PAGESIZE: Incomplete
AF_LINK: Incomplete
TCP_STATUSES: Incomplete
PROC_STATUSES: Incomplete
kinfo_proc_map: Incomplete
pidtaskinfo_map: Incomplete

class scputimes(NamedTuple):
    user: Incomplete
    nice: Incomplete
    system: Incomplete
    idle: Incomplete

class svmem(NamedTuple):
    total: Incomplete
    available: Incomplete
    percent: Incomplete
    used: Incomplete
    free: Incomplete
    active: Incomplete
    inactive: Incomplete
    wired: Incomplete

class pmem(NamedTuple):
    rss: Incomplete
    vms: Incomplete
    pfaults: Incomplete
    pageins: Incomplete

pfullmem: Incomplete

def virtual_memory():
    """System virtual memory as a namedtuple."""
def swap_memory():
    """Swap system memory as a (total, used, free, sin, sout) tuple."""
def cpu_times():
    """Return system CPU times as a namedtuple."""
def per_cpu_times():
    """Return system CPU times as a named tuple"""
def cpu_count_logical():
    """Return the number of logical CPUs in the system."""
def cpu_count_cores():
    """Return the number of CPU cores in the system."""
def cpu_stats(): ...
def cpu_freq():
    """Return CPU frequency.
    On macOS per-cpu frequency is not supported.
    Also, the returned frequency never changes, see:
    https://arstechnica.com/civis/viewtopic.php?f=19&t=465002
    """

disk_usage: Incomplete
disk_io_counters: Incomplete

def disk_partitions(all: bool = False):
    """Return mounted disk partitions as a list of namedtuples."""
def sensors_battery():
    """Return battery information."""

net_io_counters: Incomplete
net_if_addrs: Incomplete

def net_connections(kind: str = 'inet'):
    """System-wide network connections."""
def net_if_stats():
    """Get NIC stats (isup, duplex, speed, mtu)."""
def boot_time():
    """The system boot time expressed in seconds since the epoch."""
def users():
    """Return currently connected users as a list of namedtuples."""
def pids(): ...

pid_exists: Incomplete

def is_zombie(pid): ...
def wrap_exceptions(fun):
    """Decorator which translates bare OSError exceptions into
    NoSuchProcess and AccessDenied.
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
    def ppid(self): ...
    def cwd(self): ...
    def uids(self): ...
    def gids(self): ...
    def terminal(self): ...
    def memory_info(self): ...
    def memory_full_info(self): ...
    def cpu_times(self): ...
    def create_time(self): ...
    def num_ctx_switches(self): ...
    def num_threads(self): ...
    def open_files(self): ...
    def connections(self, kind: str = 'inet'): ...
    def num_fds(self): ...
    def wait(self, timeout: Incomplete | None = None): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def status(self): ...
    def threads(self): ...
