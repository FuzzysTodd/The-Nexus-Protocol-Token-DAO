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
        """Register name of resource with resource tracker."""
    def unregister(self, name, rtype) -> None:
        """Unregister name of resource with resource tracker."""

ensure_running: Incomplete
register: Incomplete
unregister: Incomplete
