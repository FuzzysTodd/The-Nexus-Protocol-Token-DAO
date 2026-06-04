from _typeshed import Incomplete
from zmq.devices.proxydevice import ProcessProxy, Proxy, ThreadProxy

__all__ = ['ProxySteerable', 'ThreadProxySteerable', 'ProcessProxySteerable']

class ProxySteerableBase:
    """Base class for overriding methods."""
    ctrl_type: Incomplete
    def __init__(self, in_type, out_type, mon_type=..., ctrl_type: Incomplete | None = None) -> None: ...
    def bind_ctrl(self, addr) -> None:
        """Enqueue ZMQ address for binding on ctrl_socket.

        See zmq.Socket.bind for details.
        """
    def bind_ctrl_to_random_port(self, addr, *args, **kwargs):
        """Enqueue a random port on the given interface for binding on
        ctrl_socket.

        See zmq.Socket.bind_to_random_port for details.
        """
    def connect_ctrl(self, addr) -> None:
        """Enqueue ZMQ address for connecting on ctrl_socket.

        See zmq.Socket.connect for details.
        """
    def setsockopt_ctrl(self, opt, value) -> None:
        """Enqueue setsockopt(opt, value) for ctrl_socket

        See zmq.Socket.setsockopt for details.
        """
    def run_device(self) -> None: ...

class ProxySteerable(ProxySteerableBase, Proxy):
    """Class for running a steerable proxy in the background.

    See zmq.devices.Proxy for most of the spec.  If the control socket is not
    NULL, the proxy supports control flow, provided by the socket.

    If PAUSE is received on this socket, the proxy suspends its activities. If
    RESUME is received, it goes on. If TERMINATE is received, it terminates
    smoothly.  If the control socket is NULL, the proxy behave exactly as if
    zmq.devices.Proxy had been used.

    This subclass adds a <method>_ctrl version of each <method>_{in|out}
    method, for configuring the control socket.

    .. versionadded:: libzmq-4.1
    .. versionadded:: 18.0
    """
class ThreadProxySteerable(ProxySteerableBase, ThreadProxy):
    """ProxySteerable in a Thread. See ProxySteerable for details."""
class ProcessProxySteerable(ProxySteerableBase, ProcessProxy):
    """ProxySteerable in a Process. See ProxySteerable for details."""
