import zmq
from _typeshed import Incomplete
from tornado.ioloop import IOLoop
from typing import Any, Callable, List, Sequence, overload
from zmq import POLLIN as POLLIN, POLLOUT as POLLOUT
from zmq._typing import Literal as Literal
from zmq.utils import jsonapi as jsonapi

class ZMQStream:
    """A utility class to register callbacks when a zmq socket sends and receives

    For use with tornado IOLoop.

    There are three main methods

    Methods:

    * **on_recv(callback, copy=True):**
        register a callback to be run every time the socket has something to receive
    * **on_send(callback):**
        register a callback to be run every time you call send
    * **send_multipart(self, msg, flags=0, copy=False, callback=None):**
        perform a send that will trigger the callback
        if callback is passed, on_send is also called.

        There are also send_multipart(), send_json(), send_pyobj()

    Three other methods for deactivating the callbacks:

    * **stop_on_recv():**
        turn off the recv callback
    * **stop_on_send():**
        turn off the send callback

    which simply call ``on_<evt>(None)``.

    The entire socket interface, excluding direct recv methods, is also
    provided, primarily through direct-linking the methods.
    e.g.

    >>> stream.bind is stream.socket.bind
    True


    .. versionadded:: 25

        send/recv callbacks can be coroutines.

    .. versionchanged:: 25

        ZMQStreams only support base zmq.Socket classes (this has always been true, but not enforced).
        If ZMQStreams are created with e.g. async Socket subclasses,
        a RuntimeWarning will be shown,
        and the socket cast back to the default zmq.Socket
        before connecting events.

        Previously, using async sockets (or any zmq.Socket subclass) would result in undefined behavior for the
        arguments passed to callback functions.
        Now, the callback functions reliably get the return value of the base `zmq.Socket` send/recv_multipart methods
        (the list of message frames).
    """
    socket: zmq.Socket
    io_loop: IOLoop
    poller: zmq.Poller
    bind: Incomplete
    bind_to_random_port: Incomplete
    connect: Incomplete
    setsockopt: Incomplete
    getsockopt: Incomplete
    setsockopt_string: Incomplete
    getsockopt_string: Incomplete
    setsockopt_unicode: Incomplete
    getsockopt_unicode: Incomplete
    def __init__(self, socket: zmq.Socket, io_loop: IOLoop | None = None) -> None: ...
    def stop_on_recv(self):
        """Disable callback and automatic receiving."""
    def stop_on_send(self):
        """Disable callback on sending."""
    def stop_on_err(self) -> None:
        """DEPRECATED, does nothing"""
    def on_err(self, callback: Callable):
        """DEPRECATED, does nothing"""
    @overload
    def on_recv(self, callback: Callable[[List[bytes]], Any]) -> None: ...
    @overload
    def on_recv(self, callback: Callable[[List[bytes]], Any], copy: Literal[True]) -> None: ...
    @overload
    def on_recv(self, callback: Callable[[List[zmq.Frame]], Any], copy: Literal[False]) -> None: ...
    @overload
    def on_recv(self, callback: Callable[[List[zmq.Frame]], Any] | Callable[[List[bytes]], Any], copy: bool = ...): ...
    @overload
    def on_recv_stream(self, callback: Callable[[ZMQStream, List[bytes]], Any]) -> None: ...
    @overload
    def on_recv_stream(self, callback: Callable[[ZMQStream, List[bytes]], Any], copy: Literal[True]) -> None: ...
    @overload
    def on_recv_stream(self, callback: Callable[[ZMQStream, List[zmq.Frame]], Any], copy: Literal[False]) -> None: ...
    @overload
    def on_recv_stream(self, callback: Callable[[ZMQStream, List[zmq.Frame]], Any] | Callable[[ZMQStream, List[bytes]], Any], copy: bool = ...): ...
    def on_send(self, callback: Callable[[Sequence[Any], zmq.MessageTracker | None], Any]):
        """Register a callback to be called on each send

        There will be two arguments::

            callback(msg, status)

        * `msg` will be the list of sendable objects that was just sent
        * `status` will be the return result of socket.send_multipart(msg) -
          MessageTracker or None.

        Non-copying sends return a MessageTracker object whose
        `done` attribute will be True when the send is complete.
        This allows users to track when an object is safe to write to
        again.

        The second argument will always be None if copy=True
        on the send.

        Use on_send_stream(callback) to register a callback that will be passed
        this ZMQStream as the first argument, in addition to the other two.

        on_send(None) disables recv event polling.

        Parameters
        ----------

        callback : callable
            callback must take exactly two arguments, which will be
            the message being sent (always a list),
            and the return result of socket.send_multipart(msg) -
            MessageTracker or None.

            if callback is None, send callbacks are disabled.
        """
    def on_send_stream(self, callback: Callable[[ZMQStream, Sequence[Any], zmq.MessageTracker | None], Any]):
        """Same as on_send, but callback will get this stream as first argument

        Callback will be passed three arguments::

            callback(stream, msg, status)

        Useful when a single callback should be used with multiple streams.
        """
    def send(self, msg, flags: int = 0, copy: bool = True, track: bool = False, callback: Incomplete | None = None, **kwargs):
        """Send a message, optionally also register a new callback for sends.
        See zmq.socket.send for details.
        """
    def send_multipart(self, msg: Sequence[Any], flags: int = 0, copy: bool = True, track: bool = False, callback: Callable | None = None, **kwargs: Any) -> None:
        """Send a multipart message, optionally also register a new callback for sends.
        See zmq.socket.send_multipart for details.
        """
    def send_string(self, u: str, flags: int = 0, encoding: str = 'utf-8', callback: Callable | None = None, **kwargs: Any):
        """Send a unicode message with an encoding.
        See zmq.socket.send_unicode for details.
        """
    send_unicode = send_string
    def send_json(self, obj: Any, flags: int = 0, callback: Callable | None = None, **kwargs: Any):
        """Send json-serialized version of an object.
        See zmq.socket.send_json for details.
        """
    def send_pyobj(self, obj: Any, flags: int = 0, protocol: int = -1, callback: Callable | None = None, **kwargs: Any):
        """Send a Python object as a message using pickle to serialize.

        See zmq.socket.send_json for details.
        """
    def flush(self, flag: int = ..., limit: int | None = None):
        """Flush pending messages.

        This method safely handles all pending incoming and/or outgoing messages,
        bypassing the inner loop, passing them to the registered callbacks.

        A limit can be specified, to prevent blocking under high load.

        flush will return the first time ANY of these conditions are met:
            * No more events matching the flag are pending.
            * the total number of events handled reaches the limit.

        Note that if ``flag|POLLIN != 0``, recv events will be flushed even if no callback
        is registered, unlike normal IOLoop operation. This allows flush to be
        used to remove *and ignore* incoming messages.

        Parameters
        ----------
        flag : int, default=POLLIN|POLLOUT
                0MQ poll flags.
                If flag|POLLIN,  recv events will be flushed.
                If flag|POLLOUT, send events will be flushed.
                Both flags can be set at once, which is the default.
        limit : None or int, optional
                The maximum number of messages to send or receive.
                Both send and recv count against this limit.

        Returns
        -------
        int : count of events handled (both send and recv)
        """
    def set_close_callback(self, callback: Callable | None):
        """Call the given callback when the stream is closed."""
    def close(self, linger: int | None = None) -> None:
        """Close this stream."""
    def receiving(self) -> bool:
        """Returns True if we are currently receiving from the stream."""
    def sending(self) -> bool:
        """Returns True if we are currently sending to the stream."""
    def closed(self) -> bool: ...
