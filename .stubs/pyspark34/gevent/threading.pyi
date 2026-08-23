import threading as __threading__
from _typeshed import Incomplete
from gevent._util import LazyOnClass as LazyOnClass
from gevent.hub import getcurrent as getcurrent
from gevent.local import local as local
from gevent.lock import RLock as RLock

__implements__: Incomplete
local = local
start_new_thread: Incomplete
allocate_lock: Incomplete
getcurrent = getcurrent
Lock: Incomplete
RLock = RLock

class _DummyThread(_DummyThread_):
    def __init__(self) -> None: ...

def main_native_thread(): ...

class Thread(__threading__.Thread): ...
class Timer(Thread, __threading__.Timer): ...

get_ident: Incomplete
