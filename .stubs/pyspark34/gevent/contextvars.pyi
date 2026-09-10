from _typeshed import Incomplete
from collections import Mapping
from gevent.local import local

__all__ = ['ContextVar', 'Context', 'copy_context', 'Token']

__implements__ = __stdlib_expected__

class _ContextState(local):
    context: Incomplete
    def __init__(self) -> None: ...

class _ContextData:
    """
    A copy-on-write immutable mapping from ContextVar
    keys to arbitrary values. Setting values requires a
    copy, making it O(n), not O(1).
    """
    def __init__(self) -> None: ...
    def __getitem__(self, key): ...
    def __contains__(self, key) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def set(self, key, value): ...
    def delete(self, key): ...

class ContextVar:
    """
    Implementation of :class:`contextvars.ContextVar`.
    """
    def __init__(self, name, default=...) -> None: ...
    __init_subclass__: Incomplete
    @classmethod
    def __class_getitem__(cls, _): ...
    @property
    def name(self): ...
    def get(self, default=...): ...
    def set(self, value): ...
    def reset(self, token) -> None: ...

class Token:
    """
    Opaque implementation of :class:`contextvars.Token`.
    """
    MISSING: Incomplete
    def __init__(self, context, var, old_value) -> None: ...
    __init_subclass__: Incomplete
    @property
    def var(self):
        """
        A read-only attribute pointing to the variable that created the token
        """
    @property
    def old_value(self):
        """
        A read-only attribute set to the value the variable had before
        the ``set()`` call, or to :attr:`MISSING` if the variable wasn't set
        before.
        """

class Context(Mapping):
    """
    Implementation of :class:`contextvars.Context`
    """
    def __init__(self) -> None:
        """
        Creates an empty context.
        """
    __init_subclass__: Incomplete
    def run(self, function, *args, **kwargs): ...
    def copy(self):
        """
        Return a shallow copy.
        """
    def __getitem__(self, key): ...
    def __contains__(self, key) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

def copy_context():
    """
    Return a shallow copy of the current context.
    """
