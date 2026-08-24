from . import process as process, reduction as reduction
from _typeshed import Incomplete

class ProcessError(Exception): ...
class BufferTooShort(ProcessError): ...
class TimeoutError(ProcessError): ...
class AuthenticationError(ProcessError): ...

class BaseContext:
    ProcessError = ProcessError
    BufferTooShort = BufferTooShort
    TimeoutError = TimeoutError
    AuthenticationError = AuthenticationError
    current_process: Incomplete
    parent_process: Incomplete
    active_children: Incomplete
    def cpu_count(self):
        """Returns the number of CPUs in the system"""
    def Manager(self):
        """Returns a manager associated with a running server process

        The managers methods such as `Lock()`, `Condition()` and `Queue()`
        can be used to create shared objects.
        """
    def Pipe(self, duplex: bool = True):
        """Returns two connection object connected by a pipe"""
    def Lock(self):
        """Returns a non-recursive lock object"""
    def RLock(self):
        """Returns a recursive lock object"""
    def Condition(self, lock: Incomplete | None = None):
        """Returns a condition object"""
    def Semaphore(self, value: int = 1):
        """Returns a semaphore object"""
    def BoundedSemaphore(self, value: int = 1):
        """Returns a bounded semaphore object"""
    def Event(self):
        """Returns an event object"""
    def Barrier(self, parties, action: Incomplete | None = None, timeout: Incomplete | None = None):
        """Returns a barrier object"""
    def Queue(self, maxsize: int = 0):
        """Returns a queue object"""
    def JoinableQueue(self, maxsize: int = 0):
        """Returns a queue object"""
    def SimpleQueue(self):
        """Returns a queue object"""
    def Pool(self, processes: Incomplete | None = None, initializer: Incomplete | None = None, initargs=(), maxtasksperchild: Incomplete | None = None):
        """Returns a process pool object"""
    def RawValue(self, typecode_or_type, *args):
        """Returns a shared object"""
    def RawArray(self, typecode_or_type, size_or_initializer):
        """Returns a shared array"""
    def Value(self, typecode_or_type, *args, lock: bool = True):
        """Returns a synchronized shared object"""
    def Array(self, typecode_or_type, size_or_initializer, *, lock: bool = True):
        """Returns a synchronized shared array"""
    def freeze_support(self) -> None:
        """Check whether this is a fake forked process in a frozen executable.
        If so then run code specified by commandline and exit.
        """
    def get_logger(self):
        """Return package logger -- if it does not already exist then
        it is created.
        """
    def log_to_stderr(self, level: Incomplete | None = None):
        """Turn on logging and add a handler which prints to stderr"""
    def allow_connection_pickling(self) -> None:
        """Install support for sending connections and sockets
        between processes
        """
    def set_executable(self, executable) -> None:
        """Sets the path to a python.exe or pythonw.exe binary used to run
        child processes instead of sys.executable when using the 'spawn'
        start method.  Useful for people embedding Python.
        """
    def set_forkserver_preload(self, module_names) -> None:
        """Set list of module names to try to load in forkserver process.
        This is really just a hint.
        """
    def get_context(self, method: Incomplete | None = None): ...
    def get_start_method(self, allow_none: bool = False): ...
    def set_start_method(self, method, force: bool = False) -> None: ...
    @property
    def reducer(self):
        """Controls how objects will be reduced to a form that can be
        shared with other processes."""
    @reducer.setter
    def reducer(self, reduction) -> None: ...

class Process(process.BaseProcess): ...

class DefaultContext(BaseContext):
    Process = Process
    def __init__(self, context) -> None: ...
    def get_context(self, method: Incomplete | None = None): ...
    def set_start_method(self, method, force: bool = False) -> None: ...
    def get_start_method(self, allow_none: bool = False): ...
    def get_all_start_methods(self): ...

class ForkProcess(process.BaseProcess): ...
class SpawnProcess(process.BaseProcess): ...
class ForkServerProcess(process.BaseProcess): ...

class ForkContext(BaseContext):
    Process = ForkProcess

class SpawnContext(BaseContext):
    Process = SpawnProcess

class ForkServerContext(BaseContext):
    Process = ForkServerProcess

def get_spawning_popen(): ...
def set_spawning_popen(popen) -> None: ...
def assert_spawning(obj) -> None: ...
