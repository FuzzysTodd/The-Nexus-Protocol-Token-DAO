import enum
from _typeshed import Incomplete
from socket import AF_INET6 as AF_INET6
from typing import NamedTuple

__all__ = ['FREEBSD', 'BSD', 'LINUX', 'NETBSD', 'OPENBSD', 'MACOS', 'OSX', 'POSIX', 'SUNOS', 'WINDOWS', 'CONN_CLOSE', 'CONN_CLOSE_WAIT', 'CONN_CLOSING', 'CONN_ESTABLISHED', 'CONN_FIN_WAIT1', 'CONN_FIN_WAIT2', 'CONN_LAST_ACK', 'CONN_LISTEN', 'CONN_NONE', 'CONN_SYN_RECV', 'CONN_SYN_SENT', 'CONN_TIME_WAIT', 'NIC_DUPLEX_FULL', 'NIC_DUPLEX_HALF', 'NIC_DUPLEX_UNKNOWN', 'STATUS_DEAD', 'STATUS_DISK_SLEEP', 'STATUS_IDLE', 'STATUS_LOCKED', 'STATUS_RUNNING', 'STATUS_SLEEPING', 'STATUS_STOPPED', 'STATUS_SUSPENDED', 'STATUS_TRACING_STOP', 'STATUS_WAITING', 'STATUS_WAKE_KILL', 'STATUS_WAKING', 'STATUS_ZOMBIE', 'STATUS_PARKED', 'ENCODING', 'ENCODING_ERRS', 'AF_INET6', 'pconn', 'pcputimes', 'pctxsw', 'pgids', 'pio', 'pionice', 'popenfile', 'pthread', 'puids', 'sconn', 'scpustats', 'sdiskio', 'sdiskpart', 'sdiskusage', 'snetio', 'snicaddr', 'snicstats', 'sswap', 'suser', 'conn_tmap', 'deprecated_method', 'isfile_strict', 'memoize', 'parse_environ_block', 'path_exists_strict', 'usage_percent', 'supports_ipv6', 'sockfam_to_enum', 'socktype_to_enum', 'wrap_numbers', 'open_text', 'open_binary', 'cat', 'bcat', 'bytes2human', 'conn_to_ntuple', 'debug', 'hilite', 'term_supports_colors', 'print_color']

POSIX: Incomplete
WINDOWS: Incomplete
LINUX: Incomplete
MACOS: Incomplete
OSX = MACOS
FREEBSD: Incomplete
OPENBSD: Incomplete
NETBSD: Incomplete
BSD: Incomplete
SUNOS: Incomplete
STATUS_RUNNING: str
STATUS_SLEEPING: str
STATUS_DISK_SLEEP: str
STATUS_STOPPED: str
STATUS_TRACING_STOP: str
STATUS_ZOMBIE: str
STATUS_DEAD: str
STATUS_WAKE_KILL: str
STATUS_WAKING: str
STATUS_IDLE: str
STATUS_LOCKED: str
STATUS_WAITING: str
STATUS_SUSPENDED: str
STATUS_PARKED: str
CONN_ESTABLISHED: str
CONN_SYN_SENT: str
CONN_SYN_RECV: str
CONN_FIN_WAIT1: str
CONN_FIN_WAIT2: str
CONN_TIME_WAIT: str
CONN_CLOSE: str
CONN_CLOSE_WAIT: str
CONN_LAST_ACK: str
CONN_LISTEN: str
CONN_CLOSING: str
CONN_NONE: str
NIC_DUPLEX_FULL: int
NIC_DUPLEX_HALF: int
NIC_DUPLEX_UNKNOWN: int

class NicDuplex(enum.IntEnum):
    NIC_DUPLEX_FULL: int
    NIC_DUPLEX_HALF: int
    NIC_DUPLEX_UNKNOWN: int

class BatteryTime(enum.IntEnum):
    POWER_TIME_UNKNOWN: int
    POWER_TIME_UNLIMITED: int

ENCODING: Incomplete
ENCODING_ERRS: Incomplete

class sswap(NamedTuple):
    total: Incomplete
    used: Incomplete
    free: Incomplete
    percent: Incomplete
    sin: Incomplete
    sout: Incomplete

class sdiskusage(NamedTuple):
    total: Incomplete
    used: Incomplete
    free: Incomplete
    percent: Incomplete

class sdiskio(NamedTuple):
    read_count: Incomplete
    write_count: Incomplete
    read_bytes: Incomplete
    write_bytes: Incomplete
    read_time: Incomplete
    write_time: Incomplete

class sdiskpart(NamedTuple):
    device: Incomplete
    mountpoint: Incomplete
    fstype: Incomplete
    opts: Incomplete
    maxfile: Incomplete
    maxpath: Incomplete

class snetio(NamedTuple):
    bytes_sent: Incomplete
    bytes_recv: Incomplete
    packets_sent: Incomplete
    packets_recv: Incomplete
    errin: Incomplete
    errout: Incomplete
    dropin: Incomplete
    dropout: Incomplete

class suser(NamedTuple):
    name: Incomplete
    terminal: Incomplete
    host: Incomplete
    started: Incomplete
    pid: Incomplete

class sconn(NamedTuple):
    fd: Incomplete
    family: Incomplete
    type: Incomplete
    laddr: Incomplete
    raddr: Incomplete
    status: Incomplete
    pid: Incomplete

class snicaddr(NamedTuple):
    family: Incomplete
    address: Incomplete
    netmask: Incomplete
    broadcast: Incomplete
    ptp: Incomplete

class snicstats(NamedTuple):
    isup: Incomplete
    duplex: Incomplete
    speed: Incomplete
    mtu: Incomplete
    flags: Incomplete

class scpustats(NamedTuple):
    ctx_switches: Incomplete
    interrupts: Incomplete
    soft_interrupts: Incomplete
    syscalls: Incomplete

class scpufreq(NamedTuple):
    current: Incomplete
    min: Incomplete
    max: Incomplete

class shwtemp(NamedTuple):
    label: Incomplete
    current: Incomplete
    high: Incomplete
    critical: Incomplete

class sbattery(NamedTuple):
    percent: Incomplete
    secsleft: Incomplete
    power_plugged: Incomplete

class sfan(NamedTuple):
    label: Incomplete
    current: Incomplete

class pcputimes(NamedTuple):
    user: Incomplete
    system: Incomplete
    children_user: Incomplete
    children_system: Incomplete

class popenfile(NamedTuple):
    path: Incomplete
    fd: Incomplete

class pthread(NamedTuple):
    id: Incomplete
    user_time: Incomplete
    system_time: Incomplete

class puids(NamedTuple):
    real: Incomplete
    effective: Incomplete
    saved: Incomplete

class pgids(NamedTuple):
    real: Incomplete
    effective: Incomplete
    saved: Incomplete

class pio(NamedTuple):
    read_count: Incomplete
    write_count: Incomplete
    read_bytes: Incomplete
    write_bytes: Incomplete

class pionice(NamedTuple):
    ioclass: Incomplete
    value: Incomplete

class pctxsw(NamedTuple):
    voluntary: Incomplete
    involuntary: Incomplete

class pconn(NamedTuple):
    fd: Incomplete
    family: Incomplete
    type: Incomplete
    laddr: Incomplete
    raddr: Incomplete
    status: Incomplete

class addr(NamedTuple):
    ip: Incomplete
    port: Incomplete

conn_tmap: Incomplete

class Error(Exception):
    """Base exception class. All other psutil exceptions inherit
    from this one.
    """
    __module__: str

class NoSuchProcess(Error):
    """Exception raised when a process with a certain PID doesn't
    or no longer exists.
    """
    __module__: str
    pid: Incomplete
    name: Incomplete
    msg: Incomplete
    def __init__(self, pid, name: Incomplete | None = None, msg: Incomplete | None = None) -> None: ...

class ZombieProcess(NoSuchProcess):
    """Exception raised when querying a zombie process. This is
    raised on macOS, BSD and Solaris only, and not always: depending
    on the query the OS may be able to succeed anyway.
    On Linux all zombie processes are querable (hence this is never
    raised). Windows doesn't have zombie processes.
    """
    __module__: str
    ppid: Incomplete
    msg: Incomplete
    def __init__(self, pid, name: Incomplete | None = None, ppid: Incomplete | None = None, msg: Incomplete | None = None) -> None: ...

class AccessDenied(Error):
    """Exception raised when permission to perform an action is denied."""
    __module__: str
    pid: Incomplete
    name: Incomplete
    msg: Incomplete
    def __init__(self, pid: Incomplete | None = None, name: Incomplete | None = None, msg: Incomplete | None = None) -> None: ...

class TimeoutExpired(Error):
    """Raised on Process.wait(timeout) if timeout expires and process
    is still alive.
    """
    __module__: str
    seconds: Incomplete
    pid: Incomplete
    name: Incomplete
    msg: Incomplete
    def __init__(self, seconds, pid: Incomplete | None = None, name: Incomplete | None = None) -> None: ...

def usage_percent(used, total, round_: Incomplete | None = None):
    """Calculate percentage usage of 'used' against 'total'."""
def memoize(fun):
    """A simple memoize decorator for functions supporting (hashable)
    positional arguments.
    It also provides a cache_clear() function for clearing the cache:

    >>> @memoize
    ... def foo()
    ...     return 1
        ...
    >>> foo()
    1
    >>> foo.cache_clear()
    >>>

    It supports:
     - functions
     - classes (acts as a @singleton)
     - staticmethods
     - classmethods

    It does NOT support:
     - methods
    """
def isfile_strict(path):
    """Same as os.path.isfile() but does not swallow EACCES / EPERM
    exceptions, see:
    http://mail.python.org/pipermail/python-dev/2012-June/120787.html
    """
def path_exists_strict(path):
    """Same as os.path.exists() but does not swallow EACCES / EPERM
    exceptions, see:
    http://mail.python.org/pipermail/python-dev/2012-June/120787.html
    """
def supports_ipv6():
    """Return True if IPv6 is supported on this platform."""
def parse_environ_block(data):
    """Parse a C environ block of environment variables into a dictionary."""
def sockfam_to_enum(num):
    """Convert a numeric socket family value to an IntEnum member.
    If it's not a known member, return the numeric value itself.
    """
def socktype_to_enum(num):
    """Convert a numeric socket type value to an IntEnum member.
    If it's not a known member, return the numeric value itself.
    """
def conn_to_ntuple(fd, fam, type_, laddr, raddr, status, status_map, pid: Incomplete | None = None):
    """Convert a raw connection tuple to a proper ntuple."""
def deprecated_method(replacement):
    """A decorator which can be used to mark a method as deprecated
    'replcement' is the method name which will be called instead.
    """

class _WrapNumbers:
    """Watches numbers so that they don't overflow and wrap
    (reset to zero).
    """
    lock: Incomplete
    cache: Incomplete
    reminders: Incomplete
    reminder_keys: Incomplete
    def __init__(self) -> None: ...
    def run(self, input_dict, name):
        """Cache dict and sum numbers which overflow and wrap.
        Return an updated copy of `input_dict`
        """
    def cache_clear(self, name: Incomplete | None = None) -> None:
        """Clear the internal cache, optionally only for function 'name'."""
    def cache_info(self):
        """Return internal cache dicts as a tuple of 3 elements."""

def wrap_numbers(input_dict, name):
    '''Given an `input_dict` and a function `name`, adjust the numbers
    which "wrap" (restart from zero) across different calls by adding
    "old value" to "new value" and return an updated dict.
    '''
def open_binary(fname): ...
def open_text(fname):
    """On Python 3 opens a file in text mode by using fs encoding and
    a proper en/decoding errors handler.
    On Python 2 this is just an alias for open(name, 'rt').
    """
def cat(fname, fallback=..., _open=...):
    """Read entire file content and return it as a string. File is
    opened in text mode. If specified, `fallback` is the value
    returned in case of error, either if the file does not exist or
    it can't be read().
    """
def bcat(fname, fallback=...):
    """Same as above but opens file in binary mode."""
def bytes2human(n, format: str = '%(value).1f%(symbol)s'):
    """Used by various scripts. See:
    http://goo.gl/zeJZl

    >>> bytes2human(10000)
    '9.8K'
    >>> bytes2human(100001221)
    '95.4M'
    """
def term_supports_colors(file=...): ...
def hilite(s, color: Incomplete | None = None, bold: bool = False):
    """Return an highlighted version of 'string'."""
def print_color(s, color: Incomplete | None = None, bold: bool = False, file=...) -> None:
    """Print a colorized version of string."""
def debug(msg) -> None:
    """If PSUTIL_DEBUG env var is set, print a debug message to stderr."""

# Names in __all__ with no definition:
#   pconn
#   pcputimes
#   pctxsw
#   pgids
#   pio
#   pionice
#   popenfile
#   pthread
#   puids
#   sconn
#   scpustats
#   sdiskio
#   sdiskpart
#   sdiskusage
#   snetio
#   snicaddr
#   snicstats
#   sswap
#   suser
