import zmq as _zmq
from _typeshed import Incomplete
from asyncio import SelectorEventLoop
from zmq import _future

__all__ = ['Context', 'Socket', 'Poller', 'ZMQEventLoop', 'install']

class ProactorSelectorThreadWarning(RuntimeWarning):
    """Warning class for notifying about the extra thread spawned by tornado

    We automatically support proactor via tornado's AddThreadSelectorEventLoop"""
class _AsyncIO: ...
class Poller(_AsyncIO, _future._AsyncPoller):
    """Poller returning asyncio.Future for poll results."""
class Socket(_AsyncIO, _future._AsyncSocket):
    """Socket returning asyncio Futures for send/recv/poll methods."""
class Context(_zmq.Context[Socket]):
    """Context for creating asyncio-compatible Sockets"""

class ZMQEventLoop(SelectorEventLoop):
    """DEPRECATED: AsyncIO eventloop using zmq_poll.

    pyzmq sockets should work with any asyncio event loop as of pyzmq 17.
    """
    def __init__(self, selector: Incomplete | None = None) -> None: ...

def install() -> None:
    """DEPRECATED: No longer needed in pyzmq 17"""
