from _typeshed import Incomplete

__all__ = ['AbstractLinkable']

class _FakeNotifier:
    pending: bool
    def __init__(self) -> None: ...

class AbstractLinkable:
    hub: Incomplete
    def __init__(self, hub: Incomplete | None = None) -> None: ...
    def linkcount(self): ...
    def ready(self) -> None: ...
    def rawlink(self, callback) -> None:
        """
        Register a callback to call when this object is ready.

        *callback* will be called in the :class:`Hub
        <gevent.hub.Hub>`, so it must not use blocking gevent API.
        *callback* will be passed one argument: this instance.
        """
    def unlink(self, callback) -> None:
        """Remove the callback set by :meth:`rawlink`"""
