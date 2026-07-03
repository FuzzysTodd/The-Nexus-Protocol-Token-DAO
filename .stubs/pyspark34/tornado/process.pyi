import subprocess
from _typeshed import Incomplete
from tornado import ioloop as ioloop
from tornado.concurrent import Future as Future, future_set_exception_unless_cancelled as future_set_exception_unless_cancelled, future_set_result_unless_cancelled as future_set_result_unless_cancelled
from tornado.iostream import PipeIOStream as PipeIOStream
from tornado.log import gen_log as gen_log
from typing import Any, Callable

CalledProcessError = subprocess.CalledProcessError

def cpu_count() -> int:
    """Returns the number of processors on this machine."""
def fork_processes(num_processes: int | None, max_restarts: int | None = None) -> int:
    """Starts multiple worker processes.

    If ``num_processes`` is None or <= 0, we detect the number of cores
    available on this machine and fork that number of child
    processes. If ``num_processes`` is given and > 0, we fork that
    specific number of sub-processes.

    Since we use processes and not threads, there is no shared memory
    between any server code.

    Note that multiple processes are not compatible with the autoreload
    module (or the ``autoreload=True`` option to `tornado.web.Application`
    which defaults to True when ``debug=True``).
    When using multiple processes, no IOLoops can be created or
    referenced until after the call to ``fork_processes``.

    In each child process, ``fork_processes`` returns its *task id*, a
    number between 0 and ``num_processes``.  Processes that exit
    abnormally (due to a signal or non-zero exit status) are restarted
    with the same id (up to ``max_restarts`` times).  In the parent
    process, ``fork_processes`` calls ``sys.exit(0)`` after all child
    processes have exited normally.

    max_restarts defaults to 100.

    Availability: Unix
    """
def task_id() -> int | None:
    """Returns the current task id, if any.

    Returns None if this process was not created by `fork_processes`.
    """

class Subprocess:
    """Wraps ``subprocess.Popen`` with IOStream support.

    The constructor is the same as ``subprocess.Popen`` with the following
    additions:

    * ``stdin``, ``stdout``, and ``stderr`` may have the value
      ``tornado.process.Subprocess.STREAM``, which will make the corresponding
      attribute of the resulting Subprocess a `.PipeIOStream`. If this option
      is used, the caller is responsible for closing the streams when done
      with them.

    The ``Subprocess.STREAM`` option and the ``set_exit_callback`` and
    ``wait_for_exit`` methods do not work on Windows. There is
    therefore no reason to use this class instead of
    ``subprocess.Popen`` on that platform.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.

    """
    STREAM: Incomplete
    io_loop: Incomplete
    stdin: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    proc: Incomplete
    pid: Incomplete
    returncode: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_exit_callback(self, callback: Callable[[int], None]) -> None:
        """Runs ``callback`` when this process exits.

        The callback takes one argument, the return code of the process.

        This method uses a ``SIGCHLD`` handler, which is a global setting
        and may conflict if you have other libraries trying to handle the
        same signal.  If you are using more than one ``IOLoop`` it may
        be necessary to call `Subprocess.initialize` first to designate
        one ``IOLoop`` to run the signal handlers.

        In many cases a close callback on the stdout or stderr streams
        can be used as an alternative to an exit callback if the
        signal handler is causing a problem.

        Availability: Unix
        """
    def wait_for_exit(self, raise_error: bool = True) -> Future[int]:
        """Returns a `.Future` which resolves when the process exits.

        Usage::

            ret = yield proc.wait_for_exit()

        This is a coroutine-friendly alternative to `set_exit_callback`
        (and a replacement for the blocking `subprocess.Popen.wait`).

        By default, raises `subprocess.CalledProcessError` if the process
        has a non-zero exit status. Use ``wait_for_exit(raise_error=False)``
        to suppress this behavior and return the exit status without raising.

        .. versionadded:: 4.2

        Availability: Unix
        """
    @classmethod
    def initialize(cls) -> None:
        """Initializes the ``SIGCHLD`` handler.

        The signal handler is run on an `.IOLoop` to avoid locking issues.
        Note that the `.IOLoop` used for signal handling need not be the
        same one used by individual Subprocess objects (as long as the
        ``IOLoops`` are each running in separate threads).

        .. versionchanged:: 5.0
           The ``io_loop`` argument (deprecated since version 4.1) has been
           removed.

        Availability: Unix
        """
    @classmethod
    def uninitialize(cls) -> None:
        """Removes the ``SIGCHLD`` handler."""
