from _typeshed import Incomplete

__all__ = ['NoWayToWaitForSocketError', 'wait_for_read', 'wait_for_write']

class NoWayToWaitForSocketError(Exception): ...

def wait_for_read(sock, timeout: Incomplete | None = None):
    """Waits for reading to be available on a given socket.
    Returns True if the socket is readable, or False if the timeout expired.
    """
def wait_for_write(sock, timeout: Incomplete | None = None):
    """Waits for writing to be available on a given socket.
    Returns True if the socket is readable, or False if the timeout expired.
    """
