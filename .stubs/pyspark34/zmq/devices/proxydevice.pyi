from _typeshed import Incomplete
from zmq.devices.basedevice import Device, ProcessDevice, ThreadDevice

__all__ = ['Proxy', 'ThreadProxy', 'ProcessProxy']

class ProxyBase:
    """Base class for overriding methods."""
    mon_type: Incomplete
    def __init__(self, in_type, out_type, mon_type=...) -> None: ...
    def bind_mon(self, addr) -> None:
        """Enqueue ZMQ address for binding on mon_socket.

        See zmq.Socket.bind for details.
        """
    def bind_mon_to_random_port(self, addr, *args, **kwargs):
        """Enqueue a random port on the given interface for binding on
        mon_socket.

        See zmq.Socket.bind_to_random_port for details.

        .. versionadded:: 18.0
        """
    def connect_mon(self, addr) -> None:
        """Enqueue ZMQ address for connecting on mon_socket.

        See zmq.Socket.connect for details.
        """
    def setsockopt_mon(self, opt, value) -> None:
        """Enqueue setsockopt(opt, value) for mon_socket

        See zmq.Socket.setsockopt for details.
        """
    def run_device(self) -> None: ...

class Proxy(ProxyBase, Device):
    """Threadsafe Proxy object.

    See zmq.devices.Device for most of the spec. This subclass adds a
    <method>_mon version of each <method>_{in|out} method, for configuring the
    monitor socket.

    A Proxy is a 3-socket ZMQ Device that functions just like a
    QUEUE, except each message is also sent out on the monitor socket.

    A PUB socket is the most logical choice for the mon_socket, but it is not required.
    """
class ThreadProxy(ProxyBase, ThreadDevice):
    """Proxy in a Thread. See Proxy for more."""
class ProcessProxy(ProxyBase, ProcessDevice):
    """Proxy in a Process. See Proxy for more."""
