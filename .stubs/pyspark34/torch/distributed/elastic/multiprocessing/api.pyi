import abc
import signal
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import IntFlag
from torch.distributed.elastic.multiprocessing.errors import ProcessFailure
from typing import Any, Callable, Dict, Tuple

__all__ = ['SignalException', 'Std', 'to_map', 'RunProcsResult', 'PContext', 'get_std_cm', 'MultiprocessContext', 'SubprocessHandler', 'SubprocessContext']

class SignalException(Exception):
    """
    Exception is raised inside the torchelastic agent process by the termination handler
    if the death signal got received by the process.
    """
    sigval: Incomplete
    def __init__(self, msg: str, sigval: signal.Signals) -> None: ...

class Std(IntFlag):
    NONE: int
    OUT: int
    ERR: int
    ALL: Incomplete
    @classmethod
    def from_str(cls, vm: str) -> Std | Dict[int, 'Std']:
        '''
        Example:

        ::

         from_str("0") -> Std.NONE
         from_str("1") -> Std.OUT
         from_str("0:3,1:0,2:1,3:2") -> {0: Std.ALL, 1: Std.NONE, 2: Std.OUT, 3: Std.ERR}

        Any other input raises an exception
        '''

def to_map(val_or_map: Std | Dict[int, Std], local_world_size: int) -> Dict[int, Std]:
    """
    Certain APIs take redirect settings either as a single value (e.g. apply to all
    local ranks) or as an explicit user-provided mapping. This method is a convenience
    method that converts a value or mapping into a mapping.

    Example:

    ::

     to_map(Std.OUT, local_world_size=2) # returns: {0: Std.OUT, 1: Std.OUT}
     to_map({1: Std.OUT}, local_world_size=2) # returns: {0: Std.NONE, 1: Std.OUT}
     to_map({0: Std.OUT, 1: Std.OUT}, local_world_size=2) # returns: {0: Std.OUT, 1: Std.OUT}
    """

@dataclass
class RunProcsResult:
    """
    Results of a completed run of processes started with ``start_processes()``.
    Returned by ``PContext``.

    Note the following:

    1. All fields are mapped by local rank
    2. ``return_values`` - only populated for functions (not the binaries).
    3. ``stdouts`` - path to stdout.log (empty string if no redirect)
    4. ``stderrs`` - path to stderr.log (empty string if no redirect)

    """
    return_values: Dict[int, Any] = ...
    failures: Dict[int, ProcessFailure] = ...
    stdouts: Dict[int, str] = ...
    stderrs: Dict[int, str] = ...
    def is_failed(self) -> bool: ...
    def __init__(self, return_values, failures, stdouts, stderrs) -> None: ...

class PContext(abc.ABC, metaclass=abc.ABCMeta):
    """
    The base class that standardizes operations over a set of processes
    that are launched via different mechanisms. The name ``PContext``
    is intentional to disambiguate with ``torch.multiprocessing.ProcessContext``.

    .. warning:: stdouts and stderrs should ALWAYS be a superset of
                 tee_stdouts and tee_stderrs (respectively) this is b/c
                 tee is implemented as a redirect + tail -f <stdout/stderr.log>
    """
    name: Incomplete
    entrypoint: Incomplete
    args: Incomplete
    envs: Incomplete
    stdouts: Incomplete
    stderrs: Incomplete
    error_files: Incomplete
    nprocs: Incomplete
    def __init__(self, name: str, entrypoint: Callable | str, args: Dict[int, Tuple], envs: Dict[int, Dict[str, str]], stdouts: Dict[int, str], stderrs: Dict[int, str], tee_stdouts: Dict[int, str], tee_stderrs: Dict[int, str], error_files: Dict[int, str]) -> None: ...
    def start(self) -> None:
        """
        Start processes using parameters defined in the constructor.
        """
    def wait(self, timeout: float = -1, period: float = 1) -> RunProcsResult | None:
        '''
        Waits for the specified ``timeout`` seconds, polling every ``period`` seconds
        for the processes to be done. Returns ``None`` if the processes are still running
        on timeout expiry. Negative timeout values are interpreted as "wait-forever".
        A timeout value of zero simply queries the status of the processes (e.g. equivalent
        to a poll).

        ..note: Multiprocesing library registers SIGTERM and SIGINT signal handlers that raise
                ``SignalException`` when the signals received. It is up to the consumer of the code
                to properly handle the exception. It is important not to swallow the exception otherwise
                the process would not terminate. Example of the typical workflow can be:

        .. code-block:: python
            pc = start_processes(...)
            try:
                pc.wait(1)
                .. do some other work
            except SignalException as e:
                pc.shutdown(e.sigval, timeout=30)

        If SIGTERM or SIGINT occurs, the code above will try to shutdown child processes by propagating
        received signal. If child processes will not terminate in the timeout time, the process will send
        the SIGKILL.
        '''
    @abc.abstractmethod
    def pids(self) -> Dict[int, int]:
        """
        Returns pids of processes mapped by their respective local_ranks
        """
    def close(self, death_sig: signal.Signals | None = None, timeout: int = 30) -> None:
        """
        Terminates all processes managed by this context and cleans up any
        meta resources (e.g. redirect, error_file files).

        Args:
            death_sig: Death signal to terminate porcesses.
            timeout: Time to wait for processes to finish, if process is
                still alive after this time, it will be terminated via SIGKILL.
        """

def get_std_cm(std_rd: str, redirect_fn): ...

class MultiprocessContext(PContext):
    """
    ``PContext`` holding worker processes invoked as a function.
    """
    start_method: Incomplete
    def __init__(self, name: str, entrypoint: Callable, args: Dict[int, Tuple], envs: Dict[int, Dict[str, str]], stdouts: Dict[int, str], stderrs: Dict[int, str], tee_stdouts: Dict[int, str], tee_stderrs: Dict[int, str], error_files: Dict[int, str], start_method: str) -> None: ...
    def pids(self) -> Dict[int, int]: ...

class SubprocessHandler:
    """
    Convenience wrapper around python's ``subprocess.Popen``. Keeps track of
    meta-objects associated to the process (e.g. stdout and stderr redirect fds).
    """
    proc: Incomplete
    def __init__(self, entrypoint: str, args: Tuple, env: Dict[str, str], stdout: str, stderr: str) -> None: ...
    def close(self, death_sig: signal.Signals | None = None) -> None: ...

class SubprocessContext(PContext):
    """
    ``PContext`` holding worker processes invoked as a binary.
    """
    subprocess_handlers: Incomplete
    def __init__(self, name: str, entrypoint: str, args: Dict[int, Tuple], envs: Dict[int, Dict[str, str]], stdouts: Dict[int, str], stderrs: Dict[int, str], tee_stdouts: Dict[int, str], tee_stderrs: Dict[int, str], error_files: Dict[int, str]) -> None: ...
    def pids(self) -> Dict[int, int]: ...
