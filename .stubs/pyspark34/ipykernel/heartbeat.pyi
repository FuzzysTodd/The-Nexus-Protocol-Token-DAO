from _typeshed import Incomplete
from threading import Thread

class Heartbeat(Thread):
    """A simple ping-pong style heartbeat that runs in a thread."""
    context: Incomplete
    original_port: Incomplete
    addr: Incomplete
    daemon: bool
    pydev_do_not_trace: bool
    is_pydev_daemon_thread: bool
    name: str
    def __init__(self, context, addr: Incomplete | None = None) -> None:
        """Initialize the heartbeat thread."""
    port: Incomplete
    def pick_port(self):
        """Pick a port for the heartbeat."""
    socket: Incomplete
    def run(self) -> None:
        """Run the heartbeat thread."""
