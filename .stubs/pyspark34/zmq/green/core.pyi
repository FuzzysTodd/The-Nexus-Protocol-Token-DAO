from _typeshed import Incomplete
from typing import Tuple
from zmq import Context as _original_Context, Socket as _original_Socket

TIMEOS: Tuple

class _Socket(_original_Socket):
    """Green version of :class:`zmq.Socket`

    The following methods are overridden:

        * send
        * recv

    To ensure that the ``zmq.NOBLOCK`` flag is set and that sending or receiving
    is deferred to the hub if a ``zmq.EAGAIN`` (retry) error is raised.

    The `__state_changed` method is triggered when the zmq.FD for the socket is
    marked as readable and triggers the necessary read and write events (which
    are waited for in the recv and send methods).

    Some double underscore prefixes are used to minimize pollution of
    :class:`zmq.Socket`'s namespace.
    """
    def __init__(self, *a, **kw) -> None: ...
    def __del__(self) -> None: ...
    def close(self, linger: Incomplete | None = None) -> None: ...
    def send(self, data, flags: int = 0, copy: bool = True, track: bool = False, **kwargs):
        """send, which will only block current greenlet

        state_changed always fires exactly once (success or fail) at the
        end of this method.
        """
    def recv(self, flags: int = 0, copy: bool = True, track: bool = False):
        """recv, which will only block current greenlet

        state_changed always fires exactly once (success or fail) at the
        end of this method.
        """
    def send_multipart(self, *args, **kwargs):
        """wrap send_multipart to prevent state_changed on each partial send"""
    def recv_multipart(self, *args, **kwargs):
        """wrap recv_multipart to prevent state_changed on each partial recv"""
    def get(self, opt):
        """trigger state_changed on getsockopt(EVENTS)"""
    def set(self, opt, val):
        """set socket option"""

class _Context(_original_Context[_Socket]):
    """Replacement for :class:`zmq.Context`

    Ensures that the greened Socket above is used in calls to `socket`.
    """
