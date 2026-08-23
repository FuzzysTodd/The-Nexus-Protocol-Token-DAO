from _typeshed import Incomplete

__all__ = ['local']

class _wrefdict(dict):
    """A dict that can be weak referenced"""

class _greenlet_deleted:
    """
    A weakref callback for when the greenlet
    is deleted.

    If the greenlet is a `gevent.greenlet.Greenlet` and
    supplies ``rawlink``, that will be used instead of a
    weakref.
    """
    idt: Incomplete
    wrdicts: Incomplete
    def __init__(self, idt, wrdicts) -> None: ...
    def __call__(self, _unused) -> None: ...

class _local_deleted:
    key: Incomplete
    wrthread: Incomplete
    greenlet_deleted: Incomplete
    def __init__(self, key, wrthread, greenlet_deleted) -> None: ...
    def __call__(self, _unused) -> None: ...

class _localimpl:
    """A class managing thread-local dicts"""
    key: Incomplete
    dicts: Incomplete
    localargs: Incomplete
    localkwargs: Incomplete
    localtypeid: Incomplete
    def __init__(self, args, kwargs, local_type, id_local) -> None: ...

class _localimpl_dict_entry:
    """
    The object that goes in the ``dicts`` of ``_localimpl``
    object for each thread.
    """
    wrgreenlet: Incomplete
    localdict: Incomplete
    def __init__(self, wrgreenlet, localdict) -> None: ...

class local:
    """
    An object whose attributes are greenlet-local.
    """
    def __cinit__(self, *args, **kw) -> None: ...
    def __getattribute__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...
    def __copy__(self): ...
