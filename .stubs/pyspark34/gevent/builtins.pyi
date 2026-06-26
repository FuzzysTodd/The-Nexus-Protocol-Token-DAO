from _typeshed import Incomplete
from gevent._compat import imp_acquire_lock as imp_acquire_lock, imp_release_lock as imp_release_lock
from gevent._util import copy_globals as copy_globals
from gevent.lock import RLock as RLock

__target__: str

def __import__(*args, **kwargs):
    """
    __import__(name, globals=None, locals=None, fromlist=(), level=0) -> object

    Normally python protects imports against concurrency by doing some locking
    at the C level (at least, it does that in CPython).  This function just
    wraps the normal __import__ functionality in a recursive lock, ensuring that
    we're protected against greenlet import concurrency as well.
    """

__implements__: Incomplete
__import__: Incomplete
__imports__: Incomplete
