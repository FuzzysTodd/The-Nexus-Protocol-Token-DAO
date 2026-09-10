import zmq
from .channels import HBChannel as HBChannel
from .client import KernelClient as KernelClient
from .session import Session as Session
from _typeshed import Incomplete
from threading import Thread
from tornado.ioloop import IOLoop
from typing import Any, Dict

class ThreadedZMQSocketChannel:
    """A ZMQ socket invoking a callback in the ioloop"""
    session: Incomplete
    socket: Incomplete
    ioloop: Incomplete
    stream: Incomplete
    def __init__(self, socket: zmq.Socket | None, session: Session | None, loop: IOLoop | None) -> None:
        """Create a channel.

        Parameters
        ----------
        socket : :class:`zmq.Socket`
            The ZMQ socket to use.
        session : :class:`session.Session`
            The session to use.
        loop
            A tornado ioloop to connect the socket to using a ZMQStream
        """
    def is_alive(self) -> bool:
        """Whether the channel is alive."""
    def start(self) -> None:
        """Start the channel."""
    def stop(self) -> None:
        """Stop the channel."""
    def close(self) -> None:
        """Close the channel."""
    def send(self, msg: Dict[str, Any]) -> None:
        """Queue a message to be sent from the IOLoop's thread.

        Parameters
        ----------
        msg : message to send

        This is threadsafe, as it uses IOLoop.add_callback to give the loop's
        thread control of the action.
        """
    def call_handlers(self, msg: Dict[str, Any]) -> None:
        """This method is called in the ioloop thread when a message arrives.

        Subclasses should override this method to handle incoming messages.
        It is important to remember that this method is called in the thread
        so that some logic must be done to ensure that the application level
        handlers are called in the application thread.
        """
    def process_events(self) -> None:
        """Subclasses should override this with a method
        processing any pending GUI events.
        """
    def flush(self, timeout: float = 1.0) -> None:
        """Immediately processes all pending messages on this channel.

        This is only used for the IOPub channel.

        Callers should use this method to ensure that :meth:`call_handlers`
        has been called for all messages that have been received on the
        0MQ SUB socket of this channel.

        This method is thread safe.

        Parameters
        ----------
        timeout : float, optional
            The maximum amount of time to spend flushing, in seconds. The
            default is one second.
        """

class IOLoopThread(Thread):
    """Run a pyzmq ioloop in a thread to send and receive messages"""
    ioloop: Incomplete
    daemon: bool
    def __init__(self) -> None:
        """Initialize an io loop thread."""
    def start(self) -> None:
        """Start the IOLoop thread

        Don't return until self.ioloop is defined,
        which is created in the thread
        """
    def run(self) -> None:
        """Run my loop, ignoring EINTR events in the poller"""
    def stop(self) -> None:
        """Stop the channel's event loop and join its thread.

        This calls :meth:`~threading.Thread.join` and returns when the thread
        terminates. :class:`RuntimeError` will be raised if
        :meth:`~threading.Thread.start` is called again.
        """
    def __del__(self) -> None: ...
    def close(self) -> None:
        """Close the io loop thread."""

class ThreadedKernelClient(KernelClient):
    """A KernelClient that provides thread-safe sockets with async callbacks on message replies."""
    @property
    def ioloop(self) -> IOLoop | None: ...
    ioloop_thread: Incomplete
    def start_channels(self, shell: bool = True, iopub: bool = True, stdin: bool = True, hb: bool = True, control: bool = True) -> None:
        """Start the channels on the client."""
    def stop_channels(self) -> None:
        """Stop the channels on the client."""
    iopub_channel_class: Incomplete
    shell_channel_class: Incomplete
    stdin_channel_class: Incomplete
    hb_channel_class: Incomplete
    control_channel_class: Incomplete
    def is_alive(self) -> bool:
        """Is the kernel process still running?"""
