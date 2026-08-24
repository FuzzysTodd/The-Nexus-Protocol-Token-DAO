from _typeshed import Incomplete

__all__ = ['BaseProcess', 'current_process', 'active_children', 'parent_process']

def current_process():
    """
    Return process object representing the current process
    """
def active_children():
    """
    Return list of process objects corresponding to live child processes
    """
def parent_process():
    """
    Return process object representing the parent process
    """

class BaseProcess:
    """
    Process objects represent activity that is run in a separate process

    The class is analogous to `threading.Thread`
    """
    def __init__(self, group: Incomplete | None = None, target: Incomplete | None = None, name: Incomplete | None = None, args=(), kwargs={}, *, daemon: Incomplete | None = None) -> None: ...
    def run(self) -> None:
        """
        Method to be run in sub-process; can be overridden in sub-class
        """
    def start(self) -> None:
        """
        Start child process
        """
    def terminate(self) -> None:
        """
        Terminate process; sends SIGTERM signal or uses TerminateProcess()
        """
    def kill(self) -> None:
        """
        Terminate process; sends SIGKILL signal or uses TerminateProcess()
        """
    def join(self, timeout: Incomplete | None = None) -> None:
        """
        Wait until child process terminates
        """
    def is_alive(self):
        """
        Return whether process is alive
        """
    def close(self) -> None:
        """
        Close the Process object.

        This method releases resources held by the Process object.  It is
        an error to call this method if the child process is still running.
        """
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def daemon(self):
        """
        Return whether process is a daemon
        """
    @daemon.setter
    def daemon(self, daemonic) -> None:
        """
        Set whether process is a daemon
        """
    @property
    def authkey(self): ...
    @authkey.setter
    def authkey(self, authkey) -> None:
        """
        Set authorization key of process
        """
    @property
    def exitcode(self):
        """
        Return exit code of process or `None` if it has yet to stop
        """
    @property
    def ident(self):
        """
        Return identifier (PID) of process or `None` if it has yet to start
        """
    pid = ident
    @property
    def sentinel(self):
        """
        Return a file descriptor (Unix) or handle (Windows) suitable for
        waiting for process termination.
        """

class AuthenticationString(bytes):
    def __reduce__(self): ...

class _ParentProcess(BaseProcess):
    def __init__(self, name, pid, sentinel) -> None: ...
    def is_alive(self): ...
    @property
    def ident(self): ...
    def join(self, timeout: Incomplete | None = None) -> None:
        """
        Wait until parent process terminates
        """
    pid = ident

class _MainProcess(BaseProcess):
    def __init__(self) -> None: ...
    def close(self) -> None: ...
