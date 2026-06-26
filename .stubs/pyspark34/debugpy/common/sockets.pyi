from _typeshed import Incomplete
from debugpy.common import log as log
from debugpy.common.util import hide_thread_from_debugger as hide_thread_from_debugger

def create_server(host, port: int = 0, backlog=..., timeout: Incomplete | None = None):
    """Return a local server socket listening on the given port."""
def create_client():
    """Return a client socket that may be connected to a remote address."""
def shut_down(sock, how=...) -> None:
    """Shut down the given socket."""
def close_socket(sock) -> None:
    """Shutdown and close the socket."""
def serve(name, handler, host, port: int = 0, backlog=..., timeout: Incomplete | None = None):
    """Accepts TCP connections on the specified host and port, and invokes the
    provided handler function for every new connection.

    Returns the created server socket.
    """
