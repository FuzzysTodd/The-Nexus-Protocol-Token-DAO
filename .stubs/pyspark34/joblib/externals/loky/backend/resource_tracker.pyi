from _typeshed import Incomplete

__all__ = ['ensure_running', 'register', 'unregister']

class ResourceTracker:
    def __init__(self) -> None: ...
    def getfd(self): ...
    def ensure_running(self) -> None:
        """Make sure that resource tracker process is running.

        This can be run from any process.  Usually a child process will use
        the resource created by its parent."""
    def register(self, name, rtype) -> None:
        """Register a named resource, and increment its refcount."""
    def unregister(self, name, rtype) -> None:
        """Unregister a named resource with resource tracker."""
    def maybe_unlink(self, name, rtype) -> None:
        """Decrement the refcount of a resource, and delete it if it hits 0"""

ensure_running: Incomplete
register: Incomplete
unregister: Incomplete
