from _typeshed import Incomplete
from zmq.eventloop import zmqstream

__all__ = ['ZMQStream']

class ZMQStream(zmqstream.ZMQStream):
    def __init__(self, socket, io_loop: Incomplete | None = None) -> None: ...
