import zmq
from typing import Any, Callable
from zmq import Context

__all__ = ['Device', 'ThreadDevice', 'ProcessDevice']

class Device:
    """A 0MQ Device to be run in the background.

    You do not pass Socket instances to this, but rather Socket types::

        Device(device_type, in_socket_type, out_socket_type)

    For instance::

        dev = Device(zmq.QUEUE, zmq.DEALER, zmq.ROUTER)

    Similar to zmq.device, but socket types instead of sockets themselves are
    passed, and the sockets are created in the work thread, to avoid issues
    with thread safety. As a result, additional bind_{in|out} and
    connect_{in|out} methods and setsockopt_{in|out} allow users to specify
    connections for the sockets.

    Parameters
    ----------
    device_type : int
        The 0MQ Device type
    {in|out}_type : int
        zmq socket types, to be passed later to context.socket(). e.g.
        zmq.PUB, zmq.SUB, zmq.REQ. If out_type is < 0, then in_socket is used
        for both in_socket and out_socket.

    Methods
    -------
    bind_{in_out}(iface)
        passthrough for ``{in|out}_socket.bind(iface)``, to be called in the thread
    connect_{in_out}(iface)
        passthrough for ``{in|out}_socket.connect(iface)``, to be called in the
        thread
    setsockopt_{in_out}(opt,value)
        passthrough for ``{in|out}_socket.setsockopt(opt, value)``, to be called in
        the thread

    Attributes
    ----------
    daemon : bool
        sets whether the thread should be run as a daemon
        Default is true, because if it is false, the thread will not
        exit unless it is killed
    context_factory : callable (class attribute)
        Function for creating the Context. This will be Context.instance
        in ThreadDevices, and Context in ProcessDevices.  The only reason
        it is not instance() in ProcessDevices is that there may be a stale
        Context instance already initialized, and the forked environment
        should *never* try to use it.
    """
    context_factory: Callable[[], zmq.Context]
    daemon: bool
    device_type: int
    in_type: int
    out_type: int
    done: bool
    def __init__(self, device_type: int = ..., in_type: int | None = None, out_type: int | None = None) -> None: ...
    def bind_in(self, addr: str) -> None:
        """Enqueue ZMQ address for binding on in_socket.

        See zmq.Socket.bind for details.
        """
    def bind_in_to_random_port(self, addr: str, *args, **kwargs) -> int:
        """Enqueue a random port on the given interface for binding on
        in_socket.

        See zmq.Socket.bind_to_random_port for details.

        .. versionadded:: 18.0
        """
    def connect_in(self, addr: str) -> None:
        """Enqueue ZMQ address for connecting on in_socket.

        See zmq.Socket.connect for details.
        """
    def setsockopt_in(self, opt: int, value: Any) -> None:
        """Enqueue setsockopt(opt, value) for in_socket

        See zmq.Socket.setsockopt for details.
        """
    def bind_out(self, addr: str) -> None:
        """Enqueue ZMQ address for binding on out_socket.

        See zmq.Socket.bind for details.
        """
    def bind_out_to_random_port(self, addr: str, *args, **kwargs) -> int:
        """Enqueue a random port on the given interface for binding on
        out_socket.

        See zmq.Socket.bind_to_random_port for details.

        .. versionadded:: 18.0
        """
    def connect_out(self, addr: str):
        """Enqueue ZMQ address for connecting on out_socket.

        See zmq.Socket.connect for details.
        """
    def setsockopt_out(self, opt: int, value: Any):
        """Enqueue setsockopt(opt, value) for out_socket

        See zmq.Socket.setsockopt for details.
        """
    def run_device(self) -> None:
        """The runner method.

        Do not call me directly, instead call ``self.start()``, just like a Thread.
        """
    def run(self) -> None:
        """wrap run_device in try/catch ETERM"""
    def start(self) -> None:
        """Start the device. Override me in subclass for other launchers."""
    def join(self, timeout: float | None = None) -> None:
        """wait for me to finish, like Thread.join.

        Reimplemented appropriately by subclasses."""

class BackgroundDevice(Device):
    """Base class for launching Devices in background processes and threads."""
    launcher: Any
    def start(self) -> None: ...
    def join(self, timeout: float | None = None) -> None: ...

class ThreadDevice(BackgroundDevice):
    """A Device that will be run in a background Thread.

    See Device for details.
    """

class ProcessDevice(BackgroundDevice):
    """A Device that will be run in a background Process.

    See Device for details.
    """
    context_factory = Context
