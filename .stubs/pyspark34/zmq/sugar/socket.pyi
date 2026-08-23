import zmq
from .attrsettr import AttributeSetter
from _typeshed import Incomplete
from typing import Any, Dict, Generic, List, Sequence, TypeVar, overload
from zmq._typing import Literal
from zmq.backend import Socket as SocketBase

__all__ = ['Socket']

T = TypeVar('T', bound='Socket')

class _SocketContext(Generic[T]):
    """Context Manager for socket bind/unbind"""
    socket: T
    kind: str
    addr: str
    def __init__(self, socket: T, kind: str, addr: str) -> None: ...
    def __enter__(self) -> T: ...
    def __exit__(self, *args) -> None: ...
ST = TypeVar('ST')

class Socket(SocketBase, AttributeSetter, Generic[ST]):
    """The ZMQ socket object

    To create a Socket, first create a Context::

        ctx = zmq.Context.instance()

    then call ``ctx.socket(socket_type)``::

        s = ctx.socket(zmq.ROUTER)

    .. versionadded:: 25

        Sockets can now be shadowed by passing another Socket.
        This helps in creating an async copy of a sync socket or vice versa::

            s = zmq.Socket(async_socket)

        Which previously had to be::

            s = zmq.Socket.shadow(async_socket.underlying)
    """
    @overload
    def __init__(self, ctx_or_socket: zmq.Context, socket_type: int, *, copy_threshold: int | None = None) -> None: ...
    @overload
    def __init__(self, *, shadow: Socket | int, copy_threshold: int | None = None) -> None: ...
    @overload
    def __init__(self, ctx_or_socket: Socket) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> T:
        """Sockets are context managers

        .. versionadded:: 14.4
        """
    def __exit__(self, *args, **kwargs) -> None: ...
    def __copy__(self, memo: Incomplete | None = None) -> T:
        """Copying a Socket creates a shadow copy"""
    __deepcopy__ = __copy__
    @classmethod
    def shadow(cls, address: int | zmq.Socket) -> T:
        """Shadow an existing libzmq socket

        address is a zmq.Socket or an integer (or FFI pointer)
        representing the address of the libzmq socket.

        .. versionadded:: 14.1

        .. versionadded:: 25
            Support for shadowing `zmq.Socket` objects,
            instead of just integer addresses.
        """
    def close(self, linger: Incomplete | None = None) -> None:
        """
        Close the socket.

        If linger is specified, LINGER sockopt will be set prior to closing.

        Note: closing a zmq Socket may not close the underlying sockets
        if there are undelivered messages.
        Only after all messages are delivered or discarded by reaching the socket's LINGER timeout
        (default: forever)
        will the underlying sockets be closed.

        This can be called to close the socket by hand. If this is not
        called, the socket will automatically be closed when it is
        garbage collected,
        in which case you may see a ResourceWarning about the unclosed socket.
        """
    def bind(self, addr: str) -> _SocketContext[T]:
        """s.bind(addr)

        Bind the socket to an address.

        This causes the socket to listen on a network port. Sockets on the
        other side of this connection will use ``Socket.connect(addr)`` to
        connect to this socket.

        Returns a context manager which will call unbind on exit.

        .. versionadded:: 20.0
            Can be used as a context manager.

        Parameters
        ----------
        addr : str
            The address string. This has the form 'protocol://interface:port',
            for example 'tcp://127.0.0.1:5555'. Protocols supported include
            tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is
            encoded to utf-8 first.

        """
    def connect(self, addr: str) -> _SocketContext[T]:
        """s.connect(addr)

        Connect to a remote 0MQ socket.

        Returns a context manager which will call disconnect on exit.

        .. versionadded:: 20.0
            Can be used as a context manager.

        Parameters
        ----------
        addr : str
            The address string. This has the form 'protocol://interface:port',
            for example 'tcp://127.0.0.1:5555'. Protocols supported are
            tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
            encoded to utf-8 first.

        """
    @property
    def socket_type(self) -> int: ...
    def __dir__(self): ...
    setsockopt: Incomplete
    getsockopt: Incomplete
    def __setattr__(self, key, value) -> None:
        """Override to allow setting zmq.[UN]SUBSCRIBE even though we have a subscribe method"""
    def fileno(self) -> int:
        """Return edge-triggered file descriptor for this socket.

        This is a read-only edge-triggered file descriptor for both read and write events on this socket.
        It is important that all available events be consumed when an event is detected,
        otherwise the read event will not trigger again.

        .. versionadded:: 17.0
        """
    def subscribe(self, topic: str | bytes) -> None:
        """Subscribe to a topic

        Only for SUB sockets.

        .. versionadded:: 15.3
        """
    def unsubscribe(self, topic: str | bytes) -> None:
        """Unsubscribe from a topic

        Only for SUB sockets.

        .. versionadded:: 15.3
        """
    def set_string(self, option: int, optval: str, encoding: str = 'utf-8') -> None:
        """Set socket options with a unicode object.

        This is simply a wrapper for setsockopt to protect from encoding ambiguity.

        See the 0MQ documentation for details on specific options.

        Parameters
        ----------
        option : int
            The name of the option to set. Can be any of: SUBSCRIBE,
            UNSUBSCRIBE, IDENTITY
        optval : str
            The value of the option to set.
        encoding : str
            The encoding to be used, default is utf8
        """
    setsockopt_unicode = set_string
    setsockopt_string = set_string
    def get_string(self, option: int, encoding: str = 'utf-8') -> str:
        """Get the value of a socket option.

        See the 0MQ documentation for details on specific options.

        Parameters
        ----------
        option : int
            The option to retrieve.

        Returns
        -------
        optval : str
            The value of the option as a unicode string.
        """
    getsockopt_unicode = get_string
    getsockopt_string = get_string
    def bind_to_random_port(self, addr: str, min_port: int = 49152, max_port: int = 65536, max_tries: int = 100) -> int:
        """Bind this socket to a random port in a range.

        If the port range is unspecified, the system will choose the port.

        Parameters
        ----------
        addr : str
            The address string without the port to pass to ``Socket.bind()``.
        min_port : int, optional
            The minimum port in the range of ports to try (inclusive).
        max_port : int, optional
            The maximum port in the range of ports to try (exclusive).
        max_tries : int, optional
            The maximum number of bind attempts to make.

        Returns
        -------
        port : int
            The port the socket was bound to.

        Raises
        ------
        ZMQBindError
            if `max_tries` reached before successful bind
        """
    def get_hwm(self) -> int:
        """Get the High Water Mark.

        On libzmq ≥ 3, this gets SNDHWM if available, otherwise RCVHWM
        """
    sndhwm: Incomplete
    rcvhwm: Incomplete
    def set_hwm(self, value: int) -> None:
        """Set the High Water Mark.

        On libzmq ≥ 3, this sets both SNDHWM and RCVHWM


        .. warning::

            New values only take effect for subsequent socket
            bind/connects.
        """
    hwm: Incomplete
    @overload
    def send(self, data: Any, flags: int = ..., copy: bool = ..., *, track: Literal[True], routing_id: int | None = ..., group: str | None = ...) -> zmq.MessageTracker: ...
    @overload
    def send(self, data: Any, flags: int = ..., copy: bool = ..., *, track: Literal[False], routing_id: int | None = ..., group: str | None = ...) -> None: ...
    @overload
    def send(self, data: Any, flags: int = ..., *, copy: bool = ..., routing_id: int | None = ..., group: str | None = ...) -> None: ...
    @overload
    def send(self, data: Any, flags: int = ..., copy: bool = ..., track: bool = ..., routing_id: int | None = ..., group: str | None = ...) -> zmq.MessageTracker | None: ...
    def send_multipart(self, msg_parts: Sequence, flags: int = 0, copy: bool = True, track: bool = False, **kwargs):
        """Send a sequence of buffers as a multipart message.

        The zmq.SNDMORE flag is added to all msg parts before the last.

        Parameters
        ----------
        msg_parts : iterable
            A sequence of objects to send as a multipart message. Each element
            can be any sendable object (Frame, bytes, buffer-providers)
        flags : int, optional
            Any valid flags for :func:`Socket.send`.
            SNDMORE is added automatically for frames before the last.
        copy : bool, optional
            Should the frame(s) be sent in a copying or non-copying manner.
            If copy=False, frames smaller than self.copy_threshold bytes
            will be copied anyway.
        track : bool, optional
            Should the frame(s) be tracked for notification that ZMQ has
            finished with it (ignored if copy=True).

        Returns
        -------
        None : if copy or not track
        MessageTracker : if track and not copy
            a MessageTracker object, whose `pending` property will
            be True until the last send is completed.
        """
    @overload
    def recv_multipart(self, flags: int = ..., *, copy: Literal[True], track: bool = ...) -> List[bytes]: ...
    @overload
    def recv_multipart(self, flags: int = ..., *, copy: Literal[False], track: bool = ...) -> List[zmq.Frame]: ...
    @overload
    def recv_multipart(self, flags: int = ..., *, track: bool = ...) -> List[bytes]: ...
    @overload
    def recv_multipart(self, flags: int = 0, copy: bool = True, track: bool = False) -> List[zmq.Frame] | List[bytes]: ...
    def send_serialized(self, msg, serialize, flags: int = 0, copy: bool = True, **kwargs):
        """Send a message with a custom serialization function.

        .. versionadded:: 17

        Parameters
        ----------
        msg : The message to be sent. Can be any object serializable by `serialize`.
        serialize : callable
            The serialization function to use.
            serialize(msg) should return an iterable of sendable message frames
            (e.g. bytes objects), which will be passed to send_multipart.
        flags : int, optional
            Any valid flags for :func:`Socket.send`.
        copy : bool, optional
            Whether to copy the frames.

        """
    def recv_serialized(self, deserialize, flags: int = 0, copy: bool = True):
        """Receive a message with a custom deserialization function.

        .. versionadded:: 17

        Parameters
        ----------
        deserialize : callable
            The deserialization function to use.
            deserialize will be called with one argument: the list of frames
            returned by recv_multipart() and can return any object.
        flags : int, optional
            Any valid flags for :func:`Socket.recv`.
        copy : bool, optional
            Whether to recv bytes or Frame objects.

        Returns
        -------
        obj : object
            The object returned by the deserialization function.

        Raises
        ------
        ZMQError
            for any of the reasons :func:`~Socket.recv` might fail
        """
    def send_string(self, u: str, flags: int = 0, copy: bool = True, encoding: str = 'utf-8', **kwargs) -> zmq.Frame | None:
        """Send a Python unicode string as a message with an encoding.

        0MQ communicates with raw bytes, so you must encode/decode
        text (str) around 0MQ.

        Parameters
        ----------
        u : str
            The unicode string to send.
        flags : int, optional
            Any valid flags for :func:`Socket.send`.
        encoding : str [default: 'utf-8']
            The encoding to be used
        """
    send_unicode = send_string
    def recv_string(self, flags: int = 0, encoding: str = 'utf-8') -> str:
        """Receive a unicode string, as sent by send_string.

        Parameters
        ----------
        flags : int
            Any valid flags for :func:`Socket.recv`.
        encoding : str [default: 'utf-8']
            The encoding to be used

        Returns
        -------
        s : str
            The Python unicode string that arrives as encoded bytes.

        Raises
        ------
        ZMQError
            for any of the reasons :func:`~Socket.recv` might fail
        """
    recv_unicode = recv_string
    def send_pyobj(self, obj: Any, flags: int = 0, protocol: int = ..., **kwargs) -> zmq.Frame | None:
        """Send a Python object as a message using pickle to serialize.

        Parameters
        ----------
        obj : Python object
            The Python object to send.
        flags : int
            Any valid flags for :func:`Socket.send`.
        protocol : int
            The pickle protocol number to use. The default is pickle.DEFAULT_PROTOCOL
            where defined, and pickle.HIGHEST_PROTOCOL elsewhere.
        """
    def recv_pyobj(self, flags: int = 0) -> Any:
        """Receive a Python object as a message using pickle to serialize.

        Parameters
        ----------
        flags : int
            Any valid flags for :func:`Socket.recv`.

        Returns
        -------
        obj : Python object
            The Python object that arrives as a message.

        Raises
        ------
        ZMQError
            for any of the reasons :func:`~Socket.recv` might fail
        """
    def send_json(self, obj: Any, flags: int = 0, **kwargs) -> None:
        """Send a Python object as a message using json to serialize.

        Keyword arguments are passed on to json.dumps

        Parameters
        ----------
        obj : Python object
            The Python object to send
        flags : int
            Any valid flags for :func:`Socket.send`
        """
    def recv_json(self, flags: int = 0, **kwargs) -> List | str | int | float | Dict:
        """Receive a Python object as a message using json to serialize.

        Keyword arguments are passed on to json.loads

        Parameters
        ----------
        flags : int
            Any valid flags for :func:`Socket.recv`.

        Returns
        -------
        obj : Python object
            The Python object that arrives as a message.

        Raises
        ------
        ZMQError
            for any of the reasons :func:`~Socket.recv` might fail
        """
    def poll(self, timeout: Incomplete | None = None, flags=...) -> int:
        """Poll the socket for events.
        See :class:`Poller` to wait for multiple sockets at once.

        Parameters
        ----------
        timeout : int [default: None]
            The timeout (in milliseconds) to wait for an event. If unspecified
            (or specified None), will wait forever for an event.
        flags : int [default: POLLIN]
            POLLIN, POLLOUT, or POLLIN|POLLOUT. The event flags to poll for.

        Returns
        -------
        event_mask : int
            The poll event mask (POLLIN, POLLOUT),
            0 if the timeout was reached without an event.
        """
    def get_monitor_socket(self, events: int | None = None, addr: str | None = None) -> T:
        """Return a connected PAIR socket ready to receive the event notifications.

        .. versionadded:: libzmq-4.0
        .. versionadded:: 14.0

        Parameters
        ----------
        events : int [default: ZMQ_EVENT_ALL]
            The bitmask defining which events are wanted.
        addr :  string [default: None]
            The optional endpoint for the monitoring sockets.

        Returns
        -------
        socket :  (PAIR)
            The socket is already connected and ready to receive messages.
        """
    def disable_monitor(self) -> None:
        """Shutdown the PAIR socket (created using get_monitor_socket)
        that is serving socket events.

        .. versionadded:: 14.4
        """
