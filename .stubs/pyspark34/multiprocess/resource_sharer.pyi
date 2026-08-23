from _typeshed import Incomplete

__all__ = ['stop', 'DupFd']

class DupFd:
    """Wrapper for fd which can be used at any time."""
    def __init__(self, fd) -> None: ...
    def detach(self):
        """Get the fd.  This should only be called once."""

class _ResourceSharer:
    """Manager for resources using background thread."""
    def __init__(self) -> None: ...
    def register(self, send, close):
        """Register resource, returning an identifier."""
    @staticmethod
    def get_connection(ident):
        """Return connection from which to receive identified resource."""
    def stop(self, timeout: Incomplete | None = None) -> None:
        """Stop the background thread and clear registered resources."""

stop: Incomplete
