from _typeshed import Incomplete
from threading import Thread

CONTROL_THREAD_NAME: str

class ControlThread(Thread):
    """A thread for a control channel."""
    io_loop: Incomplete
    pydev_do_not_trace: bool
    is_pydev_daemon_thread: bool
    def __init__(self, **kwargs) -> None:
        """Initialize the thread."""
    name: Incomplete
    def run(self) -> None:
        """Run the thread."""
    def stop(self) -> None:
        """Stop the thread.

        This method is threadsafe.
        """
