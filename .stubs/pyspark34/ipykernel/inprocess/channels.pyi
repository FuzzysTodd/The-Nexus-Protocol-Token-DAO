from _typeshed import Incomplete
from typing import List

class InProcessChannel:
    """Base class for in-process channels."""
    proxy_methods: List[object]
    client: Incomplete
    def __init__(self, client: Incomplete | None = None) -> None:
        """Initialize the channel."""
    def is_alive(self):
        """Test if the channel is alive."""
    def start(self) -> None:
        """Start the channel."""
    def stop(self) -> None:
        """Stop the channel."""
    def call_handlers(self, msg) -> None:
        """This method is called in the main thread when a message arrives.

        Subclasses should override this method to handle incoming messages.
        """
    def flush(self, timeout: float = 1.0) -> None:
        """Flush the channel."""
    def call_handlers_later(self, *args, **kwds) -> None:
        """Call the message handlers later.

        The default implementation just calls the handlers immediately, but this
        method exists so that GUI toolkits can defer calling the handlers until
        after the event loop has run, as expected by GUI frontends.
        """
    def process_events(self) -> None:
        """Process any pending GUI events.

        This method will be never be called from a frontend without an event
        loop (e.g., a terminal frontend).
        """

class InProcessHBChannel:
    """A dummy heartbeat channel interface for in-process kernels.

    Normally we use the heartbeat to check that the kernel process is alive.
    When the kernel is in-process, that doesn't make sense, but clients still
    expect this interface.
    """
    time_to_dead: float
    client: Incomplete
    def __init__(self, client: Incomplete | None = None) -> None:
        """Initialize the channel."""
    def is_alive(self):
        """Test if the channel is alive."""
    def start(self) -> None:
        """Start the channel."""
    def stop(self) -> None:
        """Stop the channel."""
    def pause(self) -> None:
        """Pause the channel."""
    def unpause(self) -> None:
        """Unpause the channel."""
    def is_beating(self):
        """Test if the channel is beating."""
