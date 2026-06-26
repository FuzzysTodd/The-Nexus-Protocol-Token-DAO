from ._common import AccessDenied as AccessDenied, FREEBSD as FREEBSD, NETBSD as NETBSD, NoSuchProcess as NoSuchProcess, OPENBSD as OPENBSD, ZombieProcess as ZombieProcess, conn_tmap as conn_tmap, conn_to_ntuple as conn_to_ntuple, memoize as memoize, memoize_when_activated as memoize_when_activated, usage_percent as usage_percent
from ._compat import FileNotFoundError as FileNotFoundError, PermissionError as PermissionError, ProcessLookupError as ProcessLookupError, which as which
from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

__extra__all__: Incomplete
PROC_STATUSES: Incomplete
TCP_STATUSES: Incomplete
PAGESIZE: Incomplete
AF_LINK: Incomplete
HAS_PER_CPU_TIMES: Incomplete
HAS_PROC_NUM_THREADS: Incomplete
HAS_PROC_OPEN_FILES: Incomplete
HAS_PROC_NUM_FDS: Incomplete
kinfo_proc_map: Incomplete

class svmem(NamedTuple):
    total: Incomplete
    available: Incomplete
    percent: Incomplete
    used: Incomplete
    free: Incomplete
    active: Incomplete
    inactive: Incomplete
    buffers: Incomplete
    cached: Incomplete
    shared: Incomplete
    wired: Incomplete

class scputimes(NamedTuple):
    user: Incomplete
    nice: Incomplete
    system: Incomplete
    idle: Incomplete
    irq: Incomplete

class pmem(NamedTuple):
    rss: Incomplete
    vms: Incomplete
    text: Incomplete
    data: Incomplete
    stack: Incomplete
pfullmem = pmem

class pcputimes(NamedTuple):
    user: Incomplete
    system: Incomplete
    children_user: Incomplete
    children_system: Incomplete

class pmmap_grouped(NamedTuple):
    path: Incomplete
    rss: Incomplete
    private: Incomplete
    ref_count: Incomplete
    shadow_count: Incomplete

class pmmap_ext(NamedTuple):
    addr: Incomplete
    perms: Incomplete
    path: Incomplete
    rss: Incomplete
    private: Incomplete
    ref_count: Incomplete
    shadow_count: Incomplete

class sdiskio(NamedTuple):
    read_count: Incomplete
    write_count: Incomplete
    read_bytes: Incomplete
    write_bytes: Incomplete
    read_time: Incomplete
    write_time: Incomplete
    busy_time: Incomplete

class sdiskio(NamedTuple):
    read_count: Incomplete
    write_count: Incomplete
    read_bytes: Incomplete
    write_bytes: Incomplete

def virtual_memory(): ...
def swap_memory():
    """System swap memory as (total, used, free, sin, sout) namedtuple."""
def cpu_times():
    """Return system per-CPU times as a namedtuple"""
def per_cpu_times():
    """Return system CPU times as a namedtuple"""
def cpu_count_logical():
    """Return the number of logical CPUs in the system."""
def cpu_count_cores(): ...
def cpu_stats():
    """Return various CPU stats as a named tuple."""
def cpu_freq():
    """Return frequency metrics for CPUs. As of Dec 2018 only
        CPU 0 appears to be supported by FreeBSD and all other cores
        match the frequency of CPU 0.
        """
def disk_partitions(all: bool = False):
    """Return mounted disk partitions as a list of namedtuples.
    'all' argument is ignored, see:
    https://github.com/giampaolo/psutil/issues/906
    """

disk_usage: Incomplete
disk_io_counters: Incomplete
net_io_counters: Incomplete
net_if_addrs: Incomplete

def net_if_stats():
    """Get NIC stats (isup, duplex, speed, mtu)."""
def net_connections(kind):
    """System-wide network connections."""
def sensors_battery():
    """Return battery info."""
def sensors_temperatures():
    """Return CPU cores temperatures if available, else an empty dict."""
def boot_time():
    """The system boot time expressed in seconds since the epoch."""
def users():
    """Return currently connected users as a list of namedtuples."""
def pids():
    """Returns a list of PIDs currently running on the system."""
def pid_exists(pid):
    """Return True if pid exists."""

pid_exists: Incomplete

def is_zombie(pid): ...
def wrap_exceptions(fun):
    """Decorator which translates bare OSError exceptions into
    NoSuchProcess and AccessDenied.
    """
def wrap_exceptions_procfs(inst) -> Generator[None, None, None]:
    """Same as above, for routines relying on reading /proc fs."""

class Process:
    """Wrapper class around underlying C implementation."""
    pid: Incomplete
    def __init__(self, pid) -> None: ...
    def oneshot(self):
        """Retrieves multiple process info in one shot as a raw tuple."""
    def oneshot_enter(self) -> None: ...
    def oneshot_exit(self) -> None: ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def environ(self): ...
    def terminal(self): ...
    def ppid(self): ...
    def uids(self): ...
    def gids(self): ...
    def cpu_times(self): ...
    def cpu_num(self): ...
    def memory_info(self): ...
    memory_full_info = memory_info
    def create_time(self): ...
    def num_threads(self): ...
    def num_ctx_switches(self): ...
    def threads(self): ...
    def connections(self, kind: str = 'inet'): ...
    def wait(self, timeout: Incomplete | None = None): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def status(self): ...
    def io_counters(self): ...
    def cwd(self):
        """Return process current working directory."""

    class nt_mmap_grouped(NamedTuple):
        path: Incomplete
        rss: Incomplete
        private: Incomplete
        ref_count: Incomplete
        shadow_count: Incomplete

    class nt_mmap_ext(NamedTuple):
        addr: Incomplete
        perms: Incomplete
        path: Incomplete
        rss: Incomplete
        private: Incomplete
        ref_count: Incomplete
        shadow_count: Incomplete
    def open_files(self):
        """Return files opened by process as a list of namedtuples."""
    open_files: Incomplete
    def num_fds(self):
        """Return the number of file descriptors opened by this process."""
    num_fds: Incomplete
    def cpu_affinity_get(self): ...
    def cpu_affinity_set(self, cpus) -> None: ...
    def memory_maps(self): ...
    def rlimit(self, resource, limits: Incomplete | None = None): ...
