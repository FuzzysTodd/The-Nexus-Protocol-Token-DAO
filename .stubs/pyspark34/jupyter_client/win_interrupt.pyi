from typing import Any

def create_interrupt_event() -> Any:
    """Create an interrupt event handle.

    The parent process should call this to create the
    interrupt event that is passed to the child process. It should store
    this handle and use it with ``send_interrupt`` to interrupt the child
    process.
    """
def send_interrupt(interrupt_handle: Any) -> None:
    """Sends an interrupt event using the specified handle."""
