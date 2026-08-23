import _thread
from _typeshed import Incomplete

__all__ = ['get_hub', 'get_hub_noargs', 'get_hub_if_exists']

class _Threadlocal(_thread._local):
    Hub: Incomplete
    loop: Incomplete
    hub: Incomplete
    def __init__(self) -> None: ...

def get_hub():
    """
    Return the hub for the current thread.

    If a hub does not exist in the current thread, a new one is
    created of the type returned by :func:`get_hub_class`.

    .. deprecated:: 1.3b1
       The ``*args`` and ``**kwargs`` arguments are deprecated. They were
       only used when the hub was created, and so were non-deterministic---to be
       sure they were used, *all* callers had to pass them, or they were order-dependent.
       Use ``set_hub`` instead.

    .. versionchanged:: 1.5a3
       The *args* and *kwargs* arguments are now completely ignored.

    .. versionchanged:: 23.7.0
       The long-deprecated ``args`` and ``kwargs`` parameters are no
       longer accepted.
    """
def get_hub_noargs(): ...
def get_hub_if_exists():
    """
    Return the hub for the current thread.

    Return ``None`` if no hub has been created yet.
    """
