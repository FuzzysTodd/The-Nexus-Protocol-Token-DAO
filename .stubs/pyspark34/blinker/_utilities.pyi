import typing as t
from _typeshed import Incomplete
from blinker._saferef import BoundMethodWeakref as BoundMethodWeakref
from functools import partial as partial
from weakref import ref

IdentityType: Incomplete

class _symbol:
    def __init__(self, name) -> None:
        """Construct a new named symbol."""
    def __reduce__(self): ...

class symbol:
    """A constant symbol.

    >>> symbol('foo') is symbol('foo')
    True
    >>> symbol('foo')
    foo

    A slight refinement of the MAGICCOOKIE=object() pattern.  The primary
    advantage of symbol() is its repr().  They are also singletons.

    Repeated calls of symbol('name') will all return the same instance.

    """
    symbols: Incomplete
    def __new__(cls, name): ...

def hashable_identity(obj: object) -> IdentityType: ...

WeakTypes: Incomplete

class annotatable_weakref(ref):
    """A weakref.ref that supports custom instance attributes."""
    receiver_id: IdentityType | None
    sender_id: IdentityType | None

def reference(object, callback: Incomplete | None = None, **annotations) -> annotatable_weakref:
    """Return an annotated weak ref."""
def callable_reference(object, callback: Incomplete | None = None):
    """Return an annotated weak ref, supporting bound instance methods."""

class lazy_property:
    """A @property that is only evaluated once."""
    __doc__: Incomplete
    def __init__(self, deferred) -> None: ...
    def __get__(self, obj, cls): ...

def is_coroutine_function(func: t.Any) -> bool: ...
