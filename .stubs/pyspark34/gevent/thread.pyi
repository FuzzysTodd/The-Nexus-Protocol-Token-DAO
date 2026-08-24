from _typeshed import Incomplete
from gevent._compat import PYPY as PYPY
from gevent._hub_local import get_hub_if_exists as get_hub_if_exists
from gevent._util import copy_globals as copy_globals
from gevent.exceptions import LoopExit as LoopExit
from gevent.greenlet import Greenlet as Greenlet
from gevent.hub import GreenletExit as GreenletExit, getcurrent as getcurrent, sleep as sleep
from gevent.lock import BoundedSemaphore as BoundedSemaphore

__implements__: Incomplete
__imports__: Incomplete
__target__: str
error: Incomplete

def get_ident(gr: Incomplete | None = None): ...
def start_new_thread(function, args=(), kwargs: Incomplete | None = None): ...

class LockType(BoundedSemaphore):
    def acquire(self, blocking: bool = True, timeout: int = -1): ...
allocate_lock = LockType

def exit() -> None: ...
def stack_size(size: Incomplete | None = None): ...
