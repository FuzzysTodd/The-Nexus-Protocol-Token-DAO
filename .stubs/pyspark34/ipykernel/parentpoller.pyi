from _typeshed import Incomplete
from threading import Thread

class ParentPollerUnix(Thread):
    """A Unix-specific daemon thread that terminates the program immediately
    when the parent process no longer exists.
    """
    daemon: bool
    def __init__(self) -> None:
        """Initialize the poller."""
    def run(self) -> None:
        """Run the poller."""

class ParentPollerWindows(Thread):
    """A Windows-specific daemon thread that listens for a special event that
    signals an interrupt and, optionally, terminates the program immediately
    when the parent process no longer exists.
    """
    daemon: bool
    interrupt_handle: Incomplete
    parent_handle: Incomplete
    def __init__(self, interrupt_handle: Incomplete | None = None, parent_handle: Incomplete | None = None) -> None:
        """Create the poller. At least one of the optional parameters must be
        provided.

        Parameters
        ----------
        interrupt_handle : HANDLE (int), optional
            If provided, the program will generate a Ctrl+C event when this
            handle is signaled.
        parent_handle : HANDLE (int), optional
            If provided, the program will terminate immediately when this
            handle is signaled.
        """
    def run(self) -> None:
        """Run the poll loop. This method never returns."""
