import typing as t
import zmq
import zmq.asyncio
from ._version import protocol_version_info as protocol_version_info
from .channelsabc import HBChannelABC as HBChannelABC
from .session import Session as Session
from _typeshed import Incomplete
from threading import Thread

major_protocol_version: Incomplete

class InvalidPortNumber(Exception):
    """An exception raised for an invalid port number."""

class HBChannel(Thread):
    """The heartbeat channel which monitors the kernel heartbeat.

    Note that the heartbeat channel is paused by default. As long as you start
    this channel, the kernel manager will ensure that it is paused and un-paused
    as appropriate.
    """
    session: Incomplete
    socket: Incomplete
    address: Incomplete
    time_to_dead: float
    daemon: bool
    context: Incomplete
    poller: Incomplete
    def __init__(self, context: zmq.Context | None = None, session: Session | None = None, address: t.Tuple[str, int] | str = '') -> None:
        """Create the heartbeat monitor thread.

        Parameters
        ----------
        context : :class:`zmq.Context`
            The ZMQ context to use.
        session : :class:`session.Session`
            The session to use.
        address : zmq url
            Standard (ip, port) tuple that the kernel is listening on.
        """
    def run(self) -> None:
        """Run the heartbeat thread."""
    def pause(self) -> None:
        """Pause the heartbeat."""
    def unpause(self) -> None:
        """Unpause the heartbeat."""
    def is_beating(self) -> bool:
        """Is the heartbeat running and responsive (and not paused)."""
    def stop(self) -> None:
        """Stop the channel's event loop and join its thread."""
    def close(self) -> None:
        """Close the heartbeat thread."""
    def call_handlers(self, since_last_heartbeat: float) -> None:
        """This method is called in the ioloop thread when a message arrives.

        Subclasses should override this method to handle incoming messages.
        It is important to remember that this method is called in the thread
        so that some logic must be done to ensure that the application level
        handlers are called in the application thread.
        """

class ZMQSocketChannel:
    """A ZMQ socket wrapper"""
    socket: Incomplete
    session: Incomplete
    def __init__(self, socket: zmq.Socket, session: Session, loop: t.Any = None) -> None:
        """Create a channel.

        Parameters
        ----------
        socket : :class:`zmq.Socket`
            The ZMQ socket to use.
        session : :class:`session.Session`
            The session to use.
        loop
            Unused here, for other implementations
        """
    def get_msg(self, timeout: float | None = None) -> t.Dict[str, t.Any]:
        """Gets a message if there is one that is ready."""
    def get_msgs(self) -> t.List[t.Dict[str, t.Any]]:
        """Get all messages that are currently ready."""
    def msg_ready(self) -> bool:
        """Is there a message that has been received?"""
    def close(self) -> None:
        """Close the socket channel."""
    stop = close
    def is_alive(self) -> bool:
        """Test whether the channel is alive."""
    def send(self, msg: t.Dict[str, t.Any]) -> None:
        """Pass a message to the ZMQ socket to send"""
    def start(self) -> None:
        """Start the socket channel."""

class AsyncZMQSocketChannel(ZMQSocketChannel):
    """A ZMQ socket in an async API"""
    socket: zmq.asyncio.Socket
    def __init__(self, socket: zmq.asyncio.Socket, session: Session, loop: t.Any = None) -> None:
        """Create a channel.

        Parameters
        ----------
        socket : :class:`zmq.asyncio.Socket`
            The ZMQ socket to use.
        session : :class:`session.Session`
            The session to use.
        loop
            Unused here, for other implementations
        """
    async def get_msg(self, timeout: float | None = None) -> t.Dict[str, t.Any]:
        """Gets a message if there is one that is ready."""
    async def get_msgs(self) -> t.List[t.Dict[str, t.Any]]:
        """Get all messages that are currently ready."""
    async def msg_ready(self) -> bool:
        """Is there a message that has been received?"""
