from _typeshed import Incomplete
from debugpy import common as common
from debugpy.adapter import components as components, launchers as launchers, servers as servers
from debugpy.common import log as log, util as util

class Session(util.Observable):
    """A debug session involving a client, an adapter, a launcher, and a debug server.

    The client and the adapter are always present, and at least one of launcher and debug
    server is present, depending on the scenario.
    """
    lock: Incomplete
    id: Incomplete
    client: Incomplete
    launcher: Incomplete
    server: Incomplete
    no_debug: Incomplete
    pid: Incomplete
    debug_options: Incomplete
    is_finalizing: bool
    def __init__(self) -> None: ...
    def __enter__(self):
        """Lock the session for exclusive access."""
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None:
        """Unlock the session."""
    def register(self) -> None: ...
    def notify_changed(self) -> None: ...
    def wait_for(self, predicate, timeout: Incomplete | None = None):
        """Waits until predicate() becomes true.

        The predicate is invoked with the session locked. If satisfied, the method
        returns immediately. Otherwise, the lock is released (even if it was held
        at entry), and the method blocks waiting for some attribute of either self,
        self.client, self.server, or self.launcher to change. On every change, session
        is re-locked and predicate is re-evaluated, until it is satisfied.

        While the session is unlocked, message handlers for components other than
        the one that is waiting can run, but message handlers for that one are still
        blocked.

        If timeout is not None, the method will unblock and return after that many
        seconds regardless of whether the predicate was satisfied. The method returns
        False if it timed out, and True otherwise.
        """
    def finalize(self, why, terminate_debuggee: Incomplete | None = None) -> None:
        '''Finalizes the debug session.

        If the server is present, sends "disconnect" request with "terminateDebuggee"
        set as specified request to it; waits for it to disconnect, allowing any
        remaining messages from it to be handled; and closes the server channel.

        If the launcher is present, sends "terminate" request to it, regardless of the
        value of terminate; waits for it to disconnect, allowing any remaining messages
        from it to be handled; and closes the launcher channel.

        If the client is present, sends "terminated" event to it.

        If terminate_debuggee=None, it is treated as True if the session has a Launcher
        component, and False otherwise.
        '''

def get(pid): ...
def wait_until_ended() -> None:
    """Blocks until all sessions have ended.

    A session ends when all components that it manages disconnect from it.
    """
