import os
from ._common import AIX as AIX, AccessDenied as AccessDenied, BSD as BSD, CONN_CLOSE as CONN_CLOSE, CONN_CLOSE_WAIT as CONN_CLOSE_WAIT, CONN_CLOSING as CONN_CLOSING, CONN_ESTABLISHED as CONN_ESTABLISHED, CONN_FIN_WAIT1 as CONN_FIN_WAIT1, CONN_FIN_WAIT2 as CONN_FIN_WAIT2, CONN_LAST_ACK as CONN_LAST_ACK, CONN_LISTEN as CONN_LISTEN, CONN_NONE as CONN_NONE, CONN_SYN_RECV as CONN_SYN_RECV, CONN_SYN_SENT as CONN_SYN_SENT, CONN_TIME_WAIT as CONN_TIME_WAIT, Error as Error, FREEBSD as FREEBSD, LINUX as LINUX, MACOS as MACOS, NETBSD as NETBSD, NIC_DUPLEX_FULL as NIC_DUPLEX_FULL, NIC_DUPLEX_HALF as NIC_DUPLEX_HALF, NIC_DUPLEX_UNKNOWN as NIC_DUPLEX_UNKNOWN, NoSuchProcess as NoSuchProcess, OPENBSD as OPENBSD, OSX as OSX, POSIX as POSIX, POWER_TIME_UNKNOWN as POWER_TIME_UNKNOWN, POWER_TIME_UNLIMITED as POWER_TIME_UNLIMITED, STATUS_DEAD as STATUS_DEAD, STATUS_DISK_SLEEP as STATUS_DISK_SLEEP, STATUS_IDLE as STATUS_IDLE, STATUS_LOCKED as STATUS_LOCKED, STATUS_PARKED as STATUS_PARKED, STATUS_RUNNING as STATUS_RUNNING, STATUS_SLEEPING as STATUS_SLEEPING, STATUS_STOPPED as STATUS_STOPPED, STATUS_TRACING_STOP as STATUS_TRACING_STOP, STATUS_WAITING as STATUS_WAITING, STATUS_WAKING as STATUS_WAKING, STATUS_ZOMBIE as STATUS_ZOMBIE, SUNOS as SUNOS, TimeoutExpired as TimeoutExpired, WINDOWS as WINDOWS, ZombieProcess as ZombieProcess
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['Error', 'NoSuchProcess', 'ZombieProcess', 'AccessDenied', 'TimeoutExpired', 'version_info', '__version__', 'STATUS_RUNNING', 'STATUS_IDLE', 'STATUS_SLEEPING', 'STATUS_DISK_SLEEP', 'STATUS_STOPPED', 'STATUS_TRACING_STOP', 'STATUS_ZOMBIE', 'STATUS_DEAD', 'STATUS_WAKING', 'STATUS_LOCKED', 'STATUS_WAITING', 'STATUS_LOCKED', 'STATUS_PARKED', 'CONN_ESTABLISHED', 'CONN_SYN_SENT', 'CONN_SYN_RECV', 'CONN_FIN_WAIT1', 'CONN_FIN_WAIT2', 'CONN_TIME_WAIT', 'CONN_CLOSE', 'CONN_CLOSE_WAIT', 'CONN_LAST_ACK', 'CONN_LISTEN', 'CONN_CLOSING', 'CONN_NONE', 'AF_LINK', 'NIC_DUPLEX_FULL', 'NIC_DUPLEX_HALF', 'NIC_DUPLEX_UNKNOWN', 'POWER_TIME_UNKNOWN', 'POWER_TIME_UNLIMITED', 'BSD', 'FREEBSD', 'LINUX', 'NETBSD', 'OPENBSD', 'MACOS', 'OSX', 'POSIX', 'SUNOS', 'WINDOWS', 'AIX', 'Process', 'Popen', 'pid_exists', 'pids', 'process_iter', 'wait_procs', 'virtual_memory', 'swap_memory', 'cpu_times', 'cpu_percent', 'cpu_times_percent', 'cpu_count', 'cpu_stats', 'net_io_counters', 'net_connections', 'net_if_addrs', 'net_if_stats', 'disk_io_counters', 'disk_partitions', 'disk_usage', 'users', 'boot_time', 'cpu_freq', 'getloadavg', 'sensors_temperatures', 'sensors_fans', 'sensors_battery']

AF_LINK: Incomplete
__version__: str
version_info: Incomplete

class Process:
    """Represents an OS process with the given PID.
    If PID is omitted current process PID (os.getpid()) is used.
    Raise NoSuchProcess if PID does not exist.

    Note that most of the methods of this class do not make sure
    the PID of the process being queried has been reused over time.
    That means you might end up retrieving an information referring
    to another process in case the original one this instance
    refers to is gone in the meantime.

    The only exceptions for which process identity is pre-emptively
    checked and guaranteed are:

     - parent()
     - children()
     - nice() (set)
     - ionice() (set)
     - rlimit() (set)
     - cpu_affinity (set)
     - suspend()
     - resume()
     - send_signal()
     - terminate()
     - kill()

    To prevent this problem for all other methods you can:
     - use is_running() before querying the process
     - if you're continuously iterating over a set of Process
       instances use process_iter() which pre-emptively checks
       process identity for every yielded instance
    """
    def __init__(self, pid: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    @property
    def pid(self):
        """The process PID."""
    def oneshot(self) -> Generator[None, None, None]:
        """Utility context manager which considerably speeds up the
        retrieval of multiple process information at the same time.

        Internally different process info (e.g. name, ppid, uids,
        gids, ...) may be fetched by using the same routine, but
        only one information is returned and the others are discarded.
        When using this context manager the internal routine is
        executed once (in the example below on name()) and the
        other info are cached.

        The cache is cleared when exiting the context manager block.
        The advice is to use this every time you retrieve more than
        one information about the process. If you're lucky, you'll
        get a hell of a speedup.

        >>> import psutil
        >>> p = psutil.Process()
        >>> with p.oneshot():
        ...     p.name()  # collect multiple info
        ...     p.cpu_times()  # return cached value
        ...     p.cpu_percent()  # return cached value
        ...     p.create_time()  # return cached value
        ...
        >>>
        """
    def as_dict(self, attrs: Incomplete | None = None, ad_value: Incomplete | None = None):
        """Utility method returning process information as a
        hashable dictionary.
        If *attrs* is specified it must be a list of strings
        reflecting available Process class' attribute names
        (e.g. ['cpu_times', 'name']) else all public (read
        only) attributes are assumed.
        *ad_value* is the value which gets assigned in case
        AccessDenied or ZombieProcess exception is raised when
        retrieving that particular process information.
        """
    def parent(self):
        """Return the parent process as a Process object pre-emptively
        checking whether PID has been reused.
        If no parent is known return None.
        """
    def parents(self):
        """Return the parents of this process as a list of Process
        instances. If no parents are known return an empty list.
        """
    def is_running(self):
        """Return whether this process is running.
        It also checks if PID has been reused by another process in
        which case return False.
        """
    def ppid(self):
        """The process parent PID.
        On Windows the return value is cached after first call.
        """
    def name(self):
        """The process name. The return value is cached after first call."""
    def exe(self):
        """The process executable as an absolute path.
        May also be an empty string.
        The return value is cached after first call.
        """
    def cmdline(self):
        """The command line this process has been called with."""
    def status(self):
        """The process current status as a STATUS_* constant."""
    def username(self):
        """The name of the user that owns the process.
        On UNIX this is calculated by using *real* process uid.
        """
    def create_time(self):
        """The process creation time as a floating point number
        expressed in seconds since the epoch.
        The return value is cached after first call.
        """
    def cwd(self):
        """Process current working directory as an absolute path."""
    def nice(self, value: Incomplete | None = None):
        """Get or set process niceness (priority)."""
    def uids(self):
        """Return process UIDs as a (real, effective, saved)
            namedtuple.
            """
    def gids(self):
        """Return process GIDs as a (real, effective, saved)
            namedtuple.
            """
    def terminal(self):
        """The terminal associated with this process, if any,
            else None.
            """
    def num_fds(self):
        """Return the number of file descriptors opened by this
            process (POSIX only).
            """
    def io_counters(self):
        """Return process I/O statistics as a
            (read_count, write_count, read_bytes, write_bytes)
            namedtuple.
            Those are the number of read/write calls performed and the
            amount of bytes read and written by the process.
            """
    def ionice(self, ioclass: Incomplete | None = None, value: Incomplete | None = None):
        """Get or set process I/O niceness (priority).

            On Linux *ioclass* is one of the IOPRIO_CLASS_* constants.
            *value* is a number which goes from 0 to 7. The higher the
            value, the lower the I/O priority of the process.

            On Windows only *ioclass* is used and it can be set to 2
            (normal), 1 (low) or 0 (very low).

            Available on Linux and Windows > Vista only.
            """
    def rlimit(self, resource, limits: Incomplete | None = None):
        '''Get or set process resource limits as a (soft, hard)
            tuple.

            *resource* is one of the RLIMIT_* constants.
            *limits* is supposed to be a (soft, hard) tuple.

            See "man prlimit" for further info.
            Available on Linux and FreeBSD only.
            '''
    def cpu_affinity(self, cpus: Incomplete | None = None):
        """Get or set process CPU affinity.
            If specified, *cpus* must be a list of CPUs for which you
            want to set the affinity (e.g. [0, 1]).
            If an empty list is passed, all egible CPUs are assumed
            (and set).
            (Windows, Linux and BSD only).
            """
    def cpu_num(self):
        """Return what CPU this process is currently running on.
            The returned number should be <= psutil.cpu_count()
            and <= len(psutil.cpu_percent(percpu=True)).
            It may be used in conjunction with
            psutil.cpu_percent(percpu=True) to observe the system
            workload distributed across CPUs.
            """
    def environ(self):
        """The environment variables of the process as a dict.  Note: this
            might not reflect changes made after the process started.  """
    def num_handles(self):
        """Return the number of handles opened by this process
            (Windows only).
            """
    def num_ctx_switches(self):
        """Return the number of voluntary and involuntary context
        switches performed by this process.
        """
    def num_threads(self):
        """Return the number of threads used by this process."""
    def threads(self):
        """Return threads opened by process as a list of
            (id, user_time, system_time) namedtuples representing
            thread id and thread CPU times (user/system).
            On OpenBSD this method requires root access.
            """
    def children(self, recursive: bool = False):
        """Return the children of this process as a list of Process
        instances, pre-emptively checking whether PID has been reused.
        If *recursive* is True return all the parent descendants.

        Example (A == this process):

         A ─┐
            │
            ├─ B (child) ─┐
            │             └─ X (grandchild) ─┐
            │                                └─ Y (great grandchild)
            ├─ C (child)
            └─ D (child)

        >>> import psutil
        >>> p = psutil.Process()
        >>> p.children()
        B, C, D
        >>> p.children(recursive=True)
        B, X, Y, C, D

        Note that in the example above if process X disappears
        process Y won't be listed as the reference to process A
        is lost.
        """
    def cpu_percent(self, interval: Incomplete | None = None):
        """Return a float representing the current process CPU
        utilization as a percentage.

        When *interval* is 0.0 or None (default) compares process times
        to system CPU times elapsed since last call, returning
        immediately (non-blocking). That means that the first time
        this is called it will return a meaningful 0.0 value.

        When *interval* is > 0.0 compares process times to system CPU
        times elapsed before and after the interval (blocking).

        In this case is recommended for accuracy that this function
        be called with at least 0.1 seconds between calls.

        A value > 100.0 can be returned in case of processes running
        multiple threads on different CPU cores.

        The returned value is explicitly NOT split evenly between
        all available logical CPUs. This means that a busy loop process
        running on a system with 2 logical CPUs will be reported as
        having 100% CPU utilization instead of 50%.

        Examples:

          >>> import psutil
          >>> p = psutil.Process(os.getpid())
          >>> # blocking
          >>> p.cpu_percent(interval=1)
          2.0
          >>> # non-blocking (percentage since last call)
          >>> p.cpu_percent(interval=None)
          2.9
          >>>
        """
    def cpu_times(self):
        """Return a (user, system, children_user, children_system)
        namedtuple representing the accumulated process time, in
        seconds.
        This is similar to os.times() but per-process.
        On macOS and Windows children_user and children_system are
        always set to 0.
        """
    def memory_info(self):
        '''Return a namedtuple with variable fields depending on the
        platform, representing memory information about the process.

        The "portable" fields available on all platforms are `rss` and `vms`.

        All numbers are expressed in bytes.
        '''
    def memory_info_ex(self): ...
    def memory_full_info(self):
        """This method returns the same information as memory_info(),
        plus, on some platform (Linux, macOS, Windows), also provides
        additional metrics (USS, PSS and swap).
        The additional metrics provide a better representation of actual
        process memory usage.

        Namely USS is the memory which is unique to a process and which
        would be freed if the process was terminated right now.

        It does so by passing through the whole process address.
        As such it usually requires higher user privileges than
        memory_info() and is considerably slower.
        """
    def memory_percent(self, memtype: str = 'rss'):
        '''Compare process memory to total physical system memory and
        calculate process memory utilization as a percentage.
        *memtype* argument is a string that dictates what type of
        process memory you want to compare against (defaults to "rss").
        The list of available strings can be obtained like this:

        >>> psutil.Process().memory_info()._fields
        (\'rss\', \'vms\', \'shared\', \'text\', \'lib\', \'data\', \'dirty\', \'uss\', \'pss\')
        '''
    def memory_maps(self, grouped: bool = True):
        """Return process' mapped memory regions as a list of namedtuples
            whose fields are variable depending on the platform.

            If *grouped* is True the mapped regions with the same 'path'
            are grouped together and the different memory fields are summed.

            If *grouped* is False every mapped region is shown as a single
            entity and the namedtuple will also include the mapped region's
            address space ('addr') and permission set ('perms').
            """
    def open_files(self):
        """Return files opened by process as a list of
        (path, fd) namedtuples including the absolute file name
        and file descriptor number.
        """
    def connections(self, kind: str = 'inet'):
        """Return socket connections opened by process as a list of
        (fd, family, type, laddr, raddr, status) namedtuples.
        The *kind* parameter filters for connections that match the
        following criteria:

        +------------+----------------------------------------------------+
        | Kind Value | Connections using                                  |
        +------------+----------------------------------------------------+
        | inet       | IPv4 and IPv6                                      |
        | inet4      | IPv4                                               |
        | inet6      | IPv6                                               |
        | tcp        | TCP                                                |
        | tcp4       | TCP over IPv4                                      |
        | tcp6       | TCP over IPv6                                      |
        | udp        | UDP                                                |
        | udp4       | UDP over IPv4                                      |
        | udp6       | UDP over IPv6                                      |
        | unix       | UNIX socket (both UDP and TCP protocols)           |
        | all        | the sum of all the possible families and protocols |
        +------------+----------------------------------------------------+
        """
    def send_signal(self, sig) -> None:
        """Send a signal *sig* to process pre-emptively checking
        whether PID has been reused (see signal module constants) .
        On Windows only SIGTERM is valid and is treated as an alias
        for kill().
        """
    def suspend(self) -> None:
        """Suspend process execution with SIGSTOP pre-emptively checking
        whether PID has been reused.
        On Windows this has the effect of suspending all process threads.
        """
    def resume(self) -> None:
        """Resume process execution with SIGCONT pre-emptively checking
        whether PID has been reused.
        On Windows this has the effect of resuming all process threads.
        """
    def terminate(self) -> None:
        """Terminate the process with SIGTERM pre-emptively checking
        whether PID has been reused.
        On Windows this is an alias for kill().
        """
    def kill(self) -> None:
        """Kill the current process with SIGKILL pre-emptively checking
        whether PID has been reused.
        """
    def wait(self, timeout: Incomplete | None = None):
        """Wait for process to terminate and, if process is a children
        of os.getpid(), also return its exit code, else None.
        On Windows there's no such limitation (exit code is always
        returned).

        If the process is already terminated immediately return None
        instead of raising NoSuchProcess.

        If *timeout* (in seconds) is specified and process is still
        alive raise TimeoutExpired.

        To wait for multiple Process(es) use psutil.wait_procs().
        """

class Popen(Process):
    '''Same as subprocess.Popen, but in addition it provides all
    psutil.Process methods in a single class.
    For the following methods which are common to both classes, psutil
    implementation takes precedence:

    * send_signal()
    * terminate()
    * kill()

    This is done in order to avoid killing another process in case its
    PID has been reused, fixing BPO-6973.

      >>> import psutil
      >>> from subprocess import PIPE
      >>> p = psutil.Popen(["python", "-c", "print \'hi\'"], stdout=PIPE)
      >>> p.name()
      \'python\'
      >>> p.uids()
      user(real=1000, effective=1000, saved=1000)
      >>> p.username()
      \'giampaolo\'
      >>> p.communicate()
      (\'hi
\', None)
      >>> p.terminate()
      >>> p.wait(timeout=2)
      0
      >>>
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __dir__(self): ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs): ...
    def __getattribute__(self, name): ...
    def wait(self, timeout: Incomplete | None = None): ...

def pids():
    """Return a list of current running PIDs."""
def pid_exists(pid):
    '''Return True if given PID exists in the current process list.
    This is faster than doing "pid in psutil.pids()" and
    should be preferred.
    '''
def process_iter(attrs: Incomplete | None = None, ad_value: Incomplete | None = None) -> Generator[Incomplete, None, Incomplete]:
    """Return a generator yielding a Process instance for all
    running processes.

    Every new Process instance is only created once and then cached
    into an internal table which is updated every time this is used.

    Cached Process instances are checked for identity so that you're
    safe in case a PID has been reused by another process, in which
    case the cached instance is updated.

    The sorting order in which processes are yielded is based on
    their PIDs.

    *attrs* and *ad_value* have the same meaning as in
    Process.as_dict(). If *attrs* is specified as_dict() is called
    and the resulting dict is stored as a 'info' attribute attached
    to returned Process instance.
    If *attrs* is an empty list it will retrieve all process info
    (slow).
    """
def wait_procs(procs, timeout: Incomplete | None = None, callback: Incomplete | None = None):
    '''Convenience function which waits for a list of processes to
    terminate.

    Return a (gone, alive) tuple indicating which processes
    are gone and which ones are still alive.

    The gone ones will have a new *returncode* attribute indicating
    process exit status (may be None).

    *callback* is a function which gets called every time a process
    terminates (a Process instance is passed as callback argument).

    Function will return as soon as all processes terminate or when
    *timeout* occurs.
    Differently from Process.wait() it will not raise TimeoutExpired if
    *timeout* occurs.

    Typical use case is:

     - send SIGTERM to a list of processes
     - give them some time to terminate
     - send SIGKILL to those ones which are still alive

    Example:

    >>> def on_terminate(proc):
    ...     print("process {} terminated".format(proc))
    ...
    >>> for p in procs:
    ...    p.terminate()
    ...
    >>> gone, alive = wait_procs(procs, timeout=3, callback=on_terminate)
    >>> for p in alive:
    ...     p.kill()
    '''
def cpu_count(logical: bool = True):
    """Return the number of logical CPUs in the system (same as
    os.cpu_count() in Python 3.4).

    If *logical* is False return the number of physical cores only
    (e.g. hyper thread CPUs are excluded).

    Return None if undetermined.

    The return value is cached after first call.
    If desired cache can be cleared like this:

    >>> psutil.cpu_count.cache_clear()
    """
def cpu_times(percpu: bool = False):
    """Return system-wide CPU times as a namedtuple.
    Every CPU time represents the seconds the CPU has spent in the
    given mode. The namedtuple's fields availability varies depending on the
    platform:

     - user
     - system
     - idle
     - nice (UNIX)
     - iowait (Linux)
     - irq (Linux, FreeBSD)
     - softirq (Linux)
     - steal (Linux >= 2.6.11)
     - guest (Linux >= 2.6.24)
     - guest_nice (Linux >= 3.2.0)

    When *percpu* is True return a list of namedtuples for each CPU.
    First element of the list refers to first CPU, second element
    to second CPU and so on.
    The order of the list is consistent across calls.
    """
def cpu_percent(interval: Incomplete | None = None, percpu: bool = False):
    """Return a float representing the current system-wide CPU
    utilization as a percentage.

    When *interval* is > 0.0 compares system CPU times elapsed before
    and after the interval (blocking).

    When *interval* is 0.0 or None compares system CPU times elapsed
    since last call or module import, returning immediately (non
    blocking). That means the first time this is called it will
    return a meaningless 0.0 value which you should ignore.
    In this case is recommended for accuracy that this function be
    called with at least 0.1 seconds between calls.

    When *percpu* is True returns a list of floats representing the
    utilization as a percentage for each CPU.
    First element of the list refers to first CPU, second element
    to second CPU and so on.
    The order of the list is consistent across calls.

    Examples:

      >>> # blocking, system-wide
      >>> psutil.cpu_percent(interval=1)
      2.0
      >>>
      >>> # blocking, per-cpu
      >>> psutil.cpu_percent(interval=1, percpu=True)
      [2.0, 1.0]
      >>>
      >>> # non-blocking (percentage since last call)
      >>> psutil.cpu_percent(interval=None)
      2.9
      >>>
    """
def cpu_times_percent(interval: Incomplete | None = None, percpu: bool = False):
    """Same as cpu_percent() but provides utilization percentages
    for each specific CPU time as is returned by cpu_times().
    For instance, on Linux we'll get:

      >>> cpu_times_percent()
      cpupercent(user=4.8, nice=0.0, system=4.8, idle=90.5, iowait=0.0,
                 irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
      >>>

    *interval* and *percpu* arguments have the same meaning as in
    cpu_percent().
    """
def cpu_stats():
    """Return CPU statistics."""
def cpu_freq(percpu: bool = False):
    """Return CPU frequency as a namedtuple including current,
        min and max frequency expressed in Mhz.

        If *percpu* is True and the system supports per-cpu frequency
        retrieval (Linux only) a list of frequencies is returned for
        each CPU. If not a list with one element is returned.
        """
getloadavg = os.getloadavg

def virtual_memory():
    """Return statistics about system memory usage as a namedtuple
    including the following fields, expressed in bytes:

     - total:
       total physical memory available.

     - available:
       the memory that can be given instantly to processes without the
       system going into swap.
       This is calculated by summing different memory values depending
       on the platform and it is supposed to be used to monitor actual
       memory usage in a cross platform fashion.

     - percent:
       the percentage usage calculated as (total - available) / total * 100

     - used:
        memory used, calculated differently depending on the platform and
        designed for informational purposes only:
        macOS: active + wired
        BSD: active + wired + cached
        Linux: total - free

     - free:
       memory not being used at all (zeroed) that is readily available;
       note that this doesn't reflect the actual memory available
       (use 'available' instead)

    Platform-specific fields:

     - active (UNIX):
       memory currently in use or very recently used, and so it is in RAM.

     - inactive (UNIX):
       memory that is marked as not used.

     - buffers (BSD, Linux):
       cache for things like file system metadata.

     - cached (BSD, macOS):
       cache for various things.

     - wired (macOS, BSD):
       memory that is marked to always stay in RAM. It is never moved to disk.

     - shared (BSD):
       memory that may be simultaneously accessed by multiple processes.

    The sum of 'used' and 'available' does not necessarily equal total.
    On Windows 'available' and 'free' are the same.
    """
def swap_memory():
    """Return system swap memory statistics as a namedtuple including
    the following fields:

     - total:   total swap memory in bytes
     - used:    used swap memory in bytes
     - free:    free swap memory in bytes
     - percent: the percentage usage
     - sin:     no. of bytes the system has swapped in from disk (cumulative)
     - sout:    no. of bytes the system has swapped out from disk (cumulative)

    'sin' and 'sout' on Windows are meaningless and always set to 0.
    """
def disk_usage(path):
    """Return disk usage statistics about the given *path* as a
    namedtuple including total, used and free space expressed in bytes
    plus the percentage usage.
    """
def disk_partitions(all: bool = False):
    """Return mounted partitions as a list of
    (device, mountpoint, fstype, opts) namedtuple.
    'opts' field is a raw string separated by commas indicating mount
    options which may vary depending on the platform.

    If *all* parameter is False return physical devices only and ignore
    all others.
    """
def disk_io_counters(perdisk: bool = False, nowrap: bool = True):
    '''Return system disk I/O statistics as a namedtuple including
    the following fields:

     - read_count:  number of reads
     - write_count: number of writes
     - read_bytes:  number of bytes read
     - write_bytes: number of bytes written
     - read_time:   time spent reading from disk (in ms)
     - write_time:  time spent writing to disk (in ms)

    Platform specific:

     - busy_time: (Linux, FreeBSD) time spent doing actual I/Os (in ms)
     - read_merged_count (Linux): number of merged reads
     - write_merged_count (Linux): number of merged writes

    If *perdisk* is True return the same information for every
    physical disk installed on the system as a dictionary
    with partition names as the keys and the namedtuple
    described above as the values.

    If *nowrap* is True it detects and adjust the numbers which overflow
    and wrap (restart from 0) and add "old value" to "new value" so that
    the returned numbers will always be increasing or remain the same,
    but never decrease.
    "disk_io_counters.cache_clear()" can be used to invalidate the
    cache.

    On recent Windows versions \'diskperf -y\' command may need to be
    executed first otherwise this function won\'t find any disk.
    '''
def net_io_counters(pernic: bool = False, nowrap: bool = True):
    '''Return network I/O statistics as a namedtuple including
    the following fields:

     - bytes_sent:   number of bytes sent
     - bytes_recv:   number of bytes received
     - packets_sent: number of packets sent
     - packets_recv: number of packets received
     - errin:        total number of errors while receiving
     - errout:       total number of errors while sending
     - dropin:       total number of incoming packets which were dropped
     - dropout:      total number of outgoing packets which were dropped
                     (always 0 on macOS and BSD)

    If *pernic* is True return the same information for every
    network interface installed on the system as a dictionary
    with network interface names as the keys and the namedtuple
    described above as the values.

    If *nowrap* is True it detects and adjust the numbers which overflow
    and wrap (restart from 0) and add "old value" to "new value" so that
    the returned numbers will always be increasing or remain the same,
    but never decrease.
    "disk_io_counters.cache_clear()" can be used to invalidate the
    cache.
    '''
def net_connections(kind: str = 'inet'):
    """Return system-wide socket connections as a list of
    (fd, family, type, laddr, raddr, status, pid) namedtuples.
    In case of limited privileges 'fd' and 'pid' may be set to -1
    and None respectively.
    The *kind* parameter filters for connections that fit the
    following criteria:

    +------------+----------------------------------------------------+
    | Kind Value | Connections using                                  |
    +------------+----------------------------------------------------+
    | inet       | IPv4 and IPv6                                      |
    | inet4      | IPv4                                               |
    | inet6      | IPv6                                               |
    | tcp        | TCP                                                |
    | tcp4       | TCP over IPv4                                      |
    | tcp6       | TCP over IPv6                                      |
    | udp        | UDP                                                |
    | udp4       | UDP over IPv4                                      |
    | udp6       | UDP over IPv6                                      |
    | unix       | UNIX socket (both UDP and TCP protocols)           |
    | all        | the sum of all the possible families and protocols |
    +------------+----------------------------------------------------+

    On macOS this function requires root privileges.
    """
def net_if_addrs():
    '''Return the addresses associated to each NIC (network interface
    card) installed on the system as a dictionary whose keys are the
    NIC names and value is a list of namedtuples for each address
    assigned to the NIC. Each namedtuple includes 5 fields:

     - family: can be either socket.AF_INET, socket.AF_INET6 or
               psutil.AF_LINK, which refers to a MAC address.
     - address: is the primary address and it is always set.
     - netmask: and \'broadcast\' and \'ptp\' may be None.
     - ptp: stands for "point to point" and references the
            destination address on a point to point interface
            (typically a VPN).
     - broadcast: and *ptp* are mutually exclusive.

    Note: you can have more than one address of the same family
    associated with each interface.
    '''
def net_if_stats():
    """Return information about each NIC (network interface card)
    installed on the system as a dictionary whose keys are the
    NIC names and value is a namedtuple with the following fields:

     - isup: whether the interface is up (bool)
     - duplex: can be either NIC_DUPLEX_FULL, NIC_DUPLEX_HALF or
               NIC_DUPLEX_UNKNOWN
     - speed: the NIC speed expressed in mega bits (MB); if it can't
              be determined (e.g. 'localhost') it will be set to 0.
     - mtu: the maximum transmission unit expressed in bytes.
    """
def sensors_temperatures(fahrenheit: bool = False):
    """Return hardware temperatures. Each entry is a namedtuple
        representing a certain hardware sensor (it may be a CPU, an
        hard disk or something else, depending on the OS and its
        configuration).
        All temperatures are expressed in celsius unless *fahrenheit*
        is set to True.
        """
def sensors_fans():
    """Return fans speed. Each entry is a namedtuple
        representing a certain hardware sensor.
        All speed are expressed in RPM (rounds per minute).
        """
def sensors_battery():
    """Return battery information. If no battery is installed
        returns None.

         - percent: battery power left as a percentage.
         - secsleft: a rough approximation of how many seconds are left
                     before the battery runs out of power. May be
                     POWER_TIME_UNLIMITED or POWER_TIME_UNLIMITED.
         - power_plugged: True if the AC power cable is connected.
        """
def boot_time():
    """Return the system boot time expressed in seconds since the epoch."""
def users():
    """Return users currently connected on the system as a list of
    namedtuples including the following fields.

     - user: the name of the user
     - terminal: the tty or pseudo-tty associated with the user, if any.
     - host: the host name associated with the entry, if any.
     - started: the creation time as a floating point number expressed in
       seconds since the epoch.
    """
