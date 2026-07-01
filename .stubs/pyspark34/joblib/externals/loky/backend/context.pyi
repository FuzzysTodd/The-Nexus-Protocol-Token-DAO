from .process import LokyInitMainProcess as LokyInitMainProcess, LokyProcess as LokyProcess
from _typeshed import Incomplete
from multiprocessing.context import BaseContext

START_METHODS: Incomplete
physical_cores_cache: Incomplete

def get_context(method: Incomplete | None = None): ...
def set_start_method(method, force: bool = False) -> None: ...
def get_start_method(): ...
def cpu_count(only_physical_cores: bool = False):
    """Return the number of CPUs the current process can use.

    The returned number of CPUs accounts for:
     * the number of CPUs in the system, as given by
       ``multiprocessing.cpu_count``;
     * the CPU affinity settings of the current process
       (available on some Unix systems);
     * Cgroup CPU bandwidth limit (available on Linux only, typically
       set by docker and similar container orchestration systems);
     * the value of the LOKY_MAX_CPU_COUNT environment variable if defined.
    and is given as the minimum of these constraints.

    If ``only_physical_cores`` is True, return the number of physical cores
    instead of the number of logical cores (hyperthreading / SMT). Note that
    this option is not enforced if the number of usable cores is controlled in
    any other way such as: process affinity, Cgroup restricted CPU bandwidth
    or the LOKY_MAX_CPU_COUNT environment variable. If the number of physical
    cores is not found, return the number of logical cores.

    Note that on Windows, the returned number of CPUs cannot exceed 61 (or 60 for
    Python < 3.10), see:
    https://bugs.python.org/issue26903.

    It is also always larger or equal to 1.
    """

class LokyContext(BaseContext):
    """Context relying on the LokyProcess."""
    Process = LokyProcess
    cpu_count: Incomplete
    def Queue(self, maxsize: int = 0, reducers: Incomplete | None = None):
        """Returns a queue object"""
    def SimpleQueue(self, reducers: Incomplete | None = None):
        """Returns a queue object"""
    def Semaphore(self, value: int = 1):
        """Returns a semaphore object"""
    def BoundedSemaphore(self, value):
        """Returns a bounded semaphore object"""
    def Lock(self):
        """Returns a lock object"""
    def RLock(self):
        """Returns a recurrent lock object"""
    def Condition(self, lock: Incomplete | None = None):
        """Returns a condition object"""
    def Event(self):
        """Returns an event object"""

class LokyInitMainContext(LokyContext):
    '''Extra context with LokyProcess, which does load the main module

    This context is used for compatibility in the case ``cloudpickle`` is not
    present on the running system. This permits to load functions defined in
    the ``main`` module, using proper safeguards. The declaration of the
    ``executor`` should be protected by ``if __name__ == "__main__":`` and the
    functions and variable used from main should be out of this block.

    This mimics the default behavior of multiprocessing under Windows and the
    behavior of the ``spawn`` start method on a posix system.
    For more details, see the end of the following section of python doc
    https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming
    '''
    Process = LokyInitMainProcess

ctx_loky: Incomplete
