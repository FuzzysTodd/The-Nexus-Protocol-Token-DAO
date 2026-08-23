from _typeshed import Incomplete
from traitlets import HasTraits

class DummySocket(HasTraits):
    """A dummy socket implementing (part of) the zmq.Socket interface."""
    queue: Incomplete
    message_sent: Incomplete
    context: Incomplete
    def recv_multipart(self, flags: int = 0, copy: bool = True, track: bool = False):
        """Recv a multipart message."""
    def send_multipart(self, msg_parts, flags: int = 0, copy: bool = True, track: bool = False) -> None:
        """Send a multipart message."""
    def flush(self, timeout: float = 1.0) -> None:
        """no-op to comply with stream API"""
