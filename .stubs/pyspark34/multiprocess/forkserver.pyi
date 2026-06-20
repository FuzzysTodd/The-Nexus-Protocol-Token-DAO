from _typeshed import Incomplete

__all__ = ['ensure_running', 'get_inherited_fds', 'connect_to_new_process', 'set_forkserver_preload']

class ForkServer:
    def __init__(self) -> None: ...
    def set_forkserver_preload(self, modules_names) -> None:
        """Set list of module names to try to load in forkserver process."""
    def get_inherited_fds(self):
        """Return list of fds inherited from parent process.

        This returns None if the current process was not started by fork
        server.
        """
    def connect_to_new_process(self, fds):
        """Request forkserver to create a child process.

        Returns a pair of fds (status_r, data_w).  The calling process can read
        the child process's pid and (eventually) its returncode from status_r.
        The calling process should write to data_w the pickled preparation and
        process data.
        """
    def ensure_running(self) -> None:
        """Make sure that a fork server is running.

        This can be called from any process.  Note that usually a child
        process will just reuse the forkserver started by its parent, so
        ensure_running() will do nothing.
        """

ensure_running: Incomplete
get_inherited_fds: Incomplete
connect_to_new_process: Incomplete
set_forkserver_preload: Incomplete
