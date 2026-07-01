from _typeshed import Incomplete
from debugpy import adapter as adapter
from debugpy.adapter import components as components
from debugpy.common import json as json, log as log, messaging as messaging, sockets as sockets

access_token: Incomplete
listener: Incomplete

class Connection:
    """A debug server that is connected to the adapter.

    Servers that are not participating in a debug session are managed directly by the
    corresponding Connection instance.

    Servers that are participating in a debug session are managed by that sessions's
    Server component instance, but Connection object remains, and takes over again
    once the session ends.
    """
    disconnected: bool
    process_replaced: bool
    server: Server | None
    pid: int | None
    ppid: int | None
    channel: messaging.JsonMessageChannel
    def __init__(self, sock) -> None: ...
    def authenticate(self) -> None: ...
    def request(self, request) -> None: ...
    def event(self, event) -> None: ...
    def terminated_event(self, event) -> None: ...
    def disconnect(self) -> None: ...
    def attach_to_session(self, session) -> None:
        """Attaches this server to the specified Session as a Server component.

        Raises ValueError if the server already belongs to some session.
        """

class Server(components.Component):
    """Handles the debug server side of a debug session."""
    message_handler: Incomplete
    connection: Connection
    class Capabilities(components.Capabilities):
        PROPERTIES: Incomplete
    def __init__(self, session, connection) -> None: ...
    @property
    def pid(self):
        """Process ID of the debuggee process, as reported by the server."""
    @property
    def ppid(self):
        """Parent process ID of the debuggee process, as reported by the server."""
    capabilities: Incomplete
    def initialize(self, request) -> None: ...
    def request(self, request) -> None: ...
    def event(self, event) -> None: ...
    def initialized_event(self, event) -> None: ...
    def process_event(self, event) -> None: ...
    def continued_event(self, event) -> None: ...
    def exited_event(self, event: messaging.Event): ...
    def terminated_event(self, event) -> None: ...
    is_connected: bool
    def detach_from_session(self) -> None: ...
    def disconnect(self): ...

def serve(host: str = '127.0.0.1', port: int = 0): ...
def is_serving(): ...
def stop_serving() -> None: ...
def connections(): ...
def wait_for_connection(session, predicate, timeout: Incomplete | None = None):
    """Waits until there is a server matching the specified predicate connected to
    this adapter, and returns the corresponding Connection.

    If there is more than one server connection already available, returns the oldest
    one.
    """
def wait_until_disconnected() -> None:
    """Blocks until all debug servers disconnect from the adapter.

    If there are no server connections, waits until at least one is established first,
    before waiting for it to disconnect.
    """
def dont_wait_for_first_connection() -> None:
    """Unblocks any pending wait_until_disconnected() call that is waiting on the
    first server to connect.
    """
def inject(pid, debugpy_args, on_output) -> None: ...
