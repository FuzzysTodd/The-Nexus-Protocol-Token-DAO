from _typeshed import Incomplete

class ProcessException(Exception):
    msg: Incomplete
    error_index: Incomplete
    pid: Incomplete
    def __init__(self, msg: str, error_index: int, pid: int) -> None: ...
    def __reduce__(self): ...

class ProcessRaisedException(ProcessException):
    """
    Exception is thrown when the process failed due to exception
    raised by the code.
    """
    def __init__(self, msg: str, error_index: int, error_pid: int) -> None: ...

class ProcessExitedException(ProcessException):
    """
    Exception is thrown when the process failed due to signal
    or exited with a specific code.
    """
    exit_code: Incomplete
    signal_name: Incomplete
    def __init__(self, msg: str, error_index: int, error_pid: int, exit_code: int, signal_name: str | None = None) -> None: ...
    def __reduce__(self): ...

class ProcessContext:
    error_queues: Incomplete
    processes: Incomplete
    sentinels: Incomplete
    def __init__(self, processes, error_queues) -> None: ...
    def pids(self): ...
    def join(self, timeout: Incomplete | None = None):
        """
        Tries to join one or more processes in this spawn context.
        If one of them exited with a non-zero exit status, this function
        kills the remaining processes and raises an exception with the cause
        of the first process exiting.

        Returns ``True`` if all processes have been joined successfully,
        ``False`` if there are more processes that need to be joined.

        Args:
            timeout (float): Wait this long before giving up on waiting.
        """

class SpawnContext(ProcessContext):
    def __init__(self, processes, error_queues) -> None: ...

def start_processes(fn, args=(), nprocs: int = 1, join: bool = True, daemon: bool = False, start_method: str = 'spawn'): ...
def spawn(fn, args=(), nprocs: int = 1, join: bool = True, daemon: bool = False, start_method: str = 'spawn'):
    """Spawns ``nprocs`` processes that run ``fn`` with ``args``.

    If one of the processes exits with a non-zero exit status, the
    remaining processes are killed and an exception is raised with the
    cause of termination. In the case an exception was caught in the
    child process, it is forwarded and its traceback is included in
    the exception raised in the parent process.

    Args:
        fn (function): Function is called as the entrypoint of the
            spawned process. This function must be defined at the top
            level of a module so it can be pickled and spawned. This
            is a requirement imposed by multiprocessing.

            The function is called as ``fn(i, *args)``, where ``i`` is
            the process index and ``args`` is the passed through tuple
            of arguments.

        args (tuple): Arguments passed to ``fn``.
        nprocs (int): Number of processes to spawn.
        join (bool): Perform a blocking join on all processes.
        daemon (bool): The spawned processes' daemon flag. If set to True,
                       daemonic processes will be created.
        start_method (str): (deprecated) this method will always use ``spawn``
                               as the start method. To use a different start method
                               use ``start_processes()``.

    Returns:
        None if ``join`` is ``True``,
        :class:`~ProcessContext` if ``join`` is ``False``

    """
