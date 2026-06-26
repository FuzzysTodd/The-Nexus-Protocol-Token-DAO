import selectors2 as __selectors__
from _typeshed import Incomplete
from gevent import sleep as sleep
from gevent._compat import iteritems as iteritems, itervalues as itervalues
from gevent._util import Lazy as Lazy, copy_globals as copy_globals
from gevent.event import Event as Event

__target__: str
__implements__: Incomplete
__extra__: Incomplete
__imports__: Incomplete
EVENT_READ: Incomplete
EVENT_WRITE: Incomplete
SelectorKey = __selectors__.SelectorKey

class GeventSelector(_BaseSelectorImpl):
    """
    A selector implementation using gevent primitives.

    This is a type of :class:`selectors.BaseSelector`, so the documentation
    for that class applies here.

    .. caution::
       As the base class indicates, it is critically important to
       unregister file objects before closing them. (Or close the selector
       they are registered with before closing them.) Failure to do so
       may crash the process or have other unintended results.
    """
    def __init__(self, hub: Incomplete | None = None) -> None: ...
    def hub(self): ...
    def register(self, fileobj, events, data: Incomplete | None = None): ...
    def unregister(self, fileobj): ...
    def select(self, timeout: Incomplete | None = None):
        """
        Poll for I/O.

        Note that, like the built-in selectors, this will block
        indefinitely if no timeout is given and no files have been
        registered.
        """
    def close(self) -> None: ...
DefaultSelector = GeventSelector
