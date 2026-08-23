from .minitornado.ioloop import PeriodicCallback as PeriodicCallback, PollIOLoop as PollIOLoop
from .minitornado.log import gen_log as gen_log
from _typeshed import Incomplete
from typing import Tuple
from zmq import ETERM as ETERM, POLLERR as POLLERR, POLLIN as POLLIN, POLLOUT as POLLOUT, Poller as Poller, ZMQError as ZMQError

tornado_version: Tuple

class DelayedCallback(PeriodicCallback):
    """Schedules the given callback to be called once.

    The callback is called once, after callback_time milliseconds.

    `start` must be called after the DelayedCallback is created.

    The timeout is calculated from when `start` is called.
    """
    def __init__(self, callback, callback_time, io_loop: Incomplete | None = None) -> None: ...
    def start(self) -> None:
        """Starts the timer."""

class ZMQPoller:
    """A poller that can be used in the tornado IOLoop.

    This simply wraps a regular zmq.Poller, scaling the timeout
    by 1000, so that it is in seconds rather than milliseconds.
    """
    def __init__(self) -> None: ...
    def register(self, fd, events): ...
    def modify(self, fd, events): ...
    def unregister(self, fd): ...
    def poll(self, timeout):
        """poll in seconds rather than milliseconds.

        Event masks will be IOLoop.READ/WRITE/ERROR
        """
    def close(self) -> None: ...

class ZMQIOLoop(PollIOLoop):
    """ZMQ subclass of tornado's IOLoop

    Minor modifications, so that .current/.instance return self
    """
    def initialize(self, impl: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def instance(cls, *args, **kwargs):
        """Returns a global `IOLoop` instance.

        Most applications have a single, global `IOLoop` running on the
        main thread.  Use this method to get this instance from
        another thread.  To get the current thread's `IOLoop`, use `current()`.
        """
    @classmethod
    def current(cls, *args, **kwargs):
        """Returns the current thread’s IOLoop."""
    def start(self) -> None: ...
IOLoop = ZMQIOLoop

def install() -> None:
    """set the tornado IOLoop instance with the pyzmq IOLoop.

    After calling this function, tornado's IOLoop.instance() and pyzmq's
    IOLoop.instance() will return the same object.

    An assertion error will be raised if tornado's IOLoop has been initialized
    prior to calling this function.
    """
