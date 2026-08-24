import enum
from ._common import AccessDenied as AccessDenied, NIC_DUPLEX_FULL as NIC_DUPLEX_FULL, NIC_DUPLEX_HALF as NIC_DUPLEX_HALF, NIC_DUPLEX_UNKNOWN as NIC_DUPLEX_UNKNOWN, NoSuchProcess as NoSuchProcess, ZombieProcess as ZombieProcess, bcat as bcat, cat as cat, debug as debug, decode as decode, get_procfs_path as get_procfs_path, isfile_strict as isfile_strict, memoize as memoize, memoize_when_activated as memoize_when_activated, open_binary as open_binary, open_text as open_text, parse_environ_block as parse_environ_block, path_exists_strict as path_exists_strict, supports_ipv6 as supports_ipv6, usage_percent as usage_percent
from ._compat import FileNotFoundError as FileNotFoundError, PY3 as PY3, PermissionError as PermissionError, ProcessLookupError as ProcessLookupError, b as b, basestring as basestring
from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

__extra__all__: Incomplete
POWER_SUPPLY_PATH: str
HAS_PROC_SMAPS: Incomplete
HAS_PROC_SMAPS_ROLLUP: Incomplete
HAS_PROC_IO_PRIORITY: Incomplete
HAS_CPU_AFFINITY: Incomplete
CLOCK_TICKS: Incomplete
PAGESIZE: Incomplete
BOOT_TIME: Incomplete
LITTLE_ENDIAN: Incomplete
DISK_SECTOR_SIZE: int
AF_LINK: Incomplete
AddressFamily: Incomplete
IOPRIO_CLASS_NONE: int
IOPRIO_CLASS_RT: int
IOPRIO_CLASS_BE: int
IOPRIO_CLASS_IDLE: int

class IOPriority(enum.IntEnum):
    IOPRIO_CLASS_NONE: int
    IOPRIO_CLASS_RT: int
    IOPRIO_CLASS_BE: int
    IOPRIO_CLASS_IDLE: int

PROC_STATUSES: Incomplete
TCP_STATUSES: Incomplete

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
    slab: Incomplete

class sdiskio(NamedTuple):
    read_count: Incomplete
    write_count: Incomplete
    read_bytes: Incomplete
    write_bytes: Incomplete
    read_time: Incomplete
    write_time: Incomplete
    read_merged_count: Incomplete
    write_merged_count: Incomplete
    busy_time: Incomplete

class popenfile(NamedTuple):
    path: Incomplete
    fd: Incomplete
    position: Incomplete
    mode: Incomplete
    flags: Incomplete

class pmem(NamedTuple):
    rss: Incomplete
    vms: Incomplete
    shared: Incomplete
    text: Incomplete
    lib: Incomplete
    data: Incomplete
    dirty: Incomplete

pfullmem: Incomplete

class pmmap_grouped(NamedTuple):
    path: Incomplete
    rss: Incomplete
    size: Incomplete
    pss: Incomplete
    shared_clean: Incomplete
    shared_dirty: Incomplete
    private_clean: Incomplete
    private_dirty: Incomplete
    referenced: Incomplete
    anonymous: Incomplete
    swap: Incomplete

pmmap_ext: Incomplete

class pio(NamedTuple):
    read_count: Incomplete
    write_count: Incomplete
    read_bytes: Incomplete
    write_bytes: Incomplete
    read_chars: Incomplete
    write_chars: Incomplete

class pcputimes(NamedTuple):
    user: Incomplete
    system: Incomplete
    children_user: Incomplete
    children_system: Incomplete
    iowait: Incomplete

def readlink(path):
    """Wrapper around os.readlink()."""
def file_flags_to_mode(flags):
    """Convert file's open() flags into a readable string.
    Used by Process.open_files().
    """
def is_storage_device(name):
    '''Return True if the given name refers to a root device (e.g.
    "sda", "nvme0n1") as opposed to a logical partition (e.g.  "sda1",
    "nvme0n1p1"). If name is a virtual device (e.g. "loop1", "ram")
    return True.
    '''
def set_scputimes_ntuple(procfs_path) -> None:
    """Set a namedtuple of variable fields depending on the CPU times
    available on this Linux kernel version which may be:
    (user, nice, system, idle, iowait, irq, softirq, [steal, [guest,
     [guest_nice]]])
    Used by cpu_times() function.
    """

scputimes: Incomplete
prlimit: Incomplete
libc: Incomplete

def calculate_avail_vmem(mems):
    '''Fallback for kernels < 3.14 where /proc/meminfo does not provide
    "MemAvailable", see:
    https://blog.famzah.net/2014/09/24/

    This code reimplements the algorithm outlined here:
    https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/
        commit/?id=34e431b0ae398fc54ea69ff85ec700722c9da773

    We use this function also when "MemAvailable" returns 0 (possibly a
    kernel bug, see: https://github.com/giampaolo/psutil/issues/1915).
    In that case this routine matches "free" CLI tool result ("available"
    column).

    XXX: on recent kernels this calculation may differ by ~1.5% compared
    to "MemAvailable:", as it\'s calculated slightly differently.
    It is still way more realistic than doing (free + cached) though.
    See:
    * https://gitlab.com/procps-ng/procps/issues/42
    * https://github.com/famzah/linux-memavailable-procfs/issues/2
    '''
def virtual_memory():
    '''Report virtual memory stats.
    This implementation mimicks procps-ng-3.3.12, aka "free" CLI tool:
    https://gitlab.com/procps-ng/procps/blob/
        24fd2605c51fccc375ab0287cec33aa767f06718/proc/sysinfo.c#L778-791
    The returned values are supposed to match both "free" and "vmstat -s"
    CLI tools.
    '''
def swap_memory():
    """Return swap memory metrics."""
def cpu_times():
    """Return a named tuple representing the following system-wide
    CPU times:
    (user, nice, system, idle, iowait, irq, softirq [steal, [guest,
     [guest_nice]]])
    Last 3 fields may not be available on all Linux kernel versions.
    """
def per_cpu_times():
    """Return a list of namedtuple representing the CPU times
    for every CPU available on the system.
    """
def cpu_count_logical():
    """Return the number of logical CPUs in the system."""
def cpu_count_cores():
    """Return the number of CPU cores in the system."""
def cpu_stats():
    """Return various CPU stats as a named tuple."""
def cpu_freq():
    """Return frequency metrics for all CPUs.
        Contrarily to other OSes, Linux updates these values in
        real-time.
        """

net_if_addrs: Incomplete

class _Ipv6UnsupportedError(Exception): ...

class Connections:
    '''A wrapper on top of /proc/net/* files, retrieving per-process
    and system-wide open connections (TCP, UDP, UNIX) similarly to
    "netstat -an".

    Note: in case of UNIX sockets we\'re only able to determine the
    local endpoint/path, not the one it\'s connected to.
    According to [1] it would be possible but not easily.

    [1] http://serverfault.com/a/417946
    '''
    tmap: Incomplete
    def __init__(self) -> None: ...
    def get_proc_inodes(self, pid): ...
    def get_all_inodes(self): ...
    @staticmethod
    def decode_address(addr, family):
        '''Accept an "ip:port" address as displayed in /proc/net/*
        and convert it into a human readable form, like:

        "0500000A:0016" -> ("10.0.0.5", 22)
        "0000000000000000FFFF00000100007F:9E49" -> ("::ffff:127.0.0.1", 40521)

        The IP address portion is a little or big endian four-byte
        hexadecimal number; that is, the least significant byte is listed
        first, so we need to reverse the order of the bytes to convert it
        to an IP address.
        The port is represented as a two-byte hexadecimal number.

        Reference:
        http://linuxdevcenter.com/pub/a/linux/2000/11/16/LinuxAdmin.html
        '''
    @staticmethod
    def process_inet(file, family, type_, inodes, filter_pid: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """Parse /proc/net/tcp* and /proc/net/udp* files."""
    @staticmethod
    def process_unix(file, family, inodes, filter_pid: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """Parse /proc/net/unix files."""
    def retrieve(self, kind, pid: Incomplete | None = None): ...

def net_connections(kind: str = 'inet'):
    """Return system-wide open connections."""
def net_io_counters():
    """Return network I/O statistics for every network interface
    installed on the system as a dict of raw tuples.
    """
def net_if_stats():
    """Get NIC stats (isup, duplex, speed, mtu)."""

disk_usage: Incomplete

def disk_io_counters(perdisk: bool = False):
    """Return disk I/O statistics for every disk installed on the
    system as a dict of raw tuples.
    """

class RootFsDeviceFinder:
    '''disk_partitions() may return partitions with device == "/dev/root"
    or "rootfs". This container class uses different strategies to try to
    obtain the real device path. Resources:
    https://bootlin.com/blog/find-root-device/
    https://www.systutorials.com/how-to-find-the-disk-where-root-is-on-in-bash-on-linux/
    '''
    major: Incomplete
    minor: Incomplete
    def __init__(self) -> None: ...
    def ask_proc_partitions(self): ...
    def ask_sys_dev_block(self): ...
    def ask_sys_class_block(self): ...
    def find(self): ...

def disk_partitions(all: bool = False):
    """Return mounted disk partitions as a list of namedtuples."""
def sensors_temperatures():
    """Return hardware (CPU and others) temperatures as a dict
    including hardware name, label, current, max and critical
    temperatures.

    Implementation notes:
    - /sys/class/hwmon looks like the most recent interface to
      retrieve this info, and this implementation relies on it
      only (old distros will probably use something else)
    - lm-sensors on Ubuntu 16.04 relies on /sys/class/hwmon
    - /sys/class/thermal/thermal_zone* is another one but it's more
      difficult to parse
    """
def sensors_fans():
    """Return hardware fans info (for CPU and other peripherals) as a
    dict including hardware label and current speed.

    Implementation notes:
    - /sys/class/hwmon looks like the most recent interface to
      retrieve this info, and this implementation relies on it
      only (old distros will probably use something else)
    - lm-sensors on Ubuntu 16.04 relies on /sys/class/hwmon
    """
def sensors_battery():
    """Return battery information.
    Implementation note: it appears /sys/class/power_supply/BAT0/
    directory structure may vary and provide files with the same
    meaning but under different names, see:
    https://github.com/giampaolo/psutil/issues/966
    """
def users():
    """Return currently connected users as a list of namedtuples."""
def boot_time():
    """Return the system boot time expressed in seconds since the epoch."""
def pids():
    """Returns a list of PIDs currently running on the system."""
def pid_exists(pid):
    """Check for the existence of a unix PID. Linux TIDs are not
    supported (always return False).
    """
def ppid_map():
    """Obtain a {pid: ppid, ...} dict for all running processes in
    one shot. Used to speed up Process.children().
    """
def wrap_exceptions(fun):
    """Decorator which translates bare OSError and IOError exceptions
    into NoSuchProcess and AccessDenied.
    """

class Process:
    """Linux process implementation."""
    pid: Incomplete
    def __init__(self, pid) -> None: ...
    def oneshot_enter(self) -> None: ...
    def oneshot_exit(self) -> None: ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def environ(self): ...
    def terminal(self): ...
    def io_counters(self): ...
    def cpu_times(self): ...
    def cpu_num(self):
        """What CPU the process is on."""
    def wait(self, timeout: Incomplete | None = None): ...
    def create_time(self): ...
    def memory_info(self): ...
    def memory_full_info(self): ...
    memory_full_info = memory_info
    def memory_maps(self):
        """Return process's mapped memory regions as a list of named
            tuples. Fields are explained in 'man proc'; here is an updated
            (Apr 2012) version: http://goo.gl/fmebo

            /proc/{PID}/smaps does not exist on kernels < 2.6.14 or if
            CONFIG_MMU kernel configuration option is not enabled.
            """
    def cwd(self): ...
    def num_ctx_switches(self, _ctxsw_re=...): ...
    def num_threads(self, _num_threads_re=...): ...
    def threads(self): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def cpu_affinity_get(self): ...
    def cpu_affinity_set(self, cpus) -> None: ...
    def ionice_get(self): ...
    def ionice_set(self, ioclass, value): ...
    def rlimit(self, resource_, limits: Incomplete | None = None): ...
    def status(self): ...
    def open_files(self): ...
    def connections(self, kind: str = 'inet'): ...
    def num_fds(self): ...
    def ppid(self): ...
    def uids(self, _uids_re=...): ...
    def gids(self, _gids_re=...): ...
