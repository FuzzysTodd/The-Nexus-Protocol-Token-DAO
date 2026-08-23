from _typeshed import Incomplete
from io import TextIOBase

MASTER: int
CHILD: int
PIPE_BUFFER_SIZE: int

class IOPubThread:
    """An object for sending IOPub messages in a background thread

    Prevents a blocking main thread from delaying output from threads.

    IOPubThread(pub_socket).background_socket is a Socket-API-providing object
    whose IO is always run in a thread.
    """
    socket: Incomplete
    background_socket: Incomplete
    io_loop: Incomplete
    thread: Incomplete
    def __init__(self, socket, pipe: bool = False) -> None:
        """Create IOPub thread

        Parameters
        ----------
        socket : zmq.PUB Socket
            the socket on which messages will be sent.
        pipe : bool
            Whether this process should listen for IOPub messages
            piped from subprocesses.
        """
    def start(self) -> None:
        """Start the IOPub thread"""
    def stop(self) -> None:
        """Stop the IOPub thread"""
    def close(self) -> None:
        """Close the IOPub thread."""
    @property
    def closed(self): ...
    def schedule(self, f) -> None:
        """Schedule a function to be called in our IO thread.

        If the thread is not running, call immediately.
        """
    def send_multipart(self, *args, **kwargs):
        """send_multipart schedules actual zmq send in my thread.

        If my thread isn't running (e.g. forked process), send immediately.
        """

class BackgroundSocket:
    """Wrapper around IOPub thread that provides zmq send[_multipart]"""
    io_thread: Incomplete
    def __init__(self, io_thread) -> None:
        """Initialize the socket."""
    def __getattr__(self, attr):
        """Wrap socket attr access for backward-compatibility"""
    def __setattr__(self, attr, value) -> None:
        """Set an attribute on the socket."""
    def send(self, msg, *args, **kwargs):
        """Send a message to the socket."""
    def send_multipart(self, *args, **kwargs):
        """Schedule send in IO thread"""

class OutStream(TextIOBase):
    """A file like object that publishes the stream to a 0MQ PUB socket.

    Output is handed off to an IO Thread
    """
    flush_timeout: int
    flush_interval: float
    topic: Incomplete
    encoding: str
    def fileno(self):
        """
        Things like subprocess will peak and write to the fileno() of stderr/stdout.
        """
    session: Incomplete
    pub_thread: Incomplete
    name: Incomplete
    parent_header: Incomplete
    echo: Incomplete
    def __init__(self, session, pub_thread, name, pipe: Incomplete | None = None, echo: Incomplete | None = None, *, watchfd: bool = True, isatty: bool = False) -> None:
        """
        Parameters
        ----------
        session : object
            the session object
        pub_thread : threading.Thread
            the publication thread
        name : str {'stderr', 'stdout'}
            the name of the standard stream to replace
        pipe : object
            the pip object
        echo : bool
            whether to echo output
        watchfd : bool (default, True)
            Watch the file descriptor corresponding to the replaced stream.
            This is useful if you know some underlying code will write directly
            the file descriptor by its number. It will spawn a watching thread,
            that will swap the give file descriptor for a pipe, read from the
            pipe, and insert this into the current Stream.
        isatty : bool (default, False)
            Indication of whether this stream has terminal capabilities (e.g. can handle colors)

        """
    def isatty(self):
        """Return a bool indicating whether this is an 'interactive' stream.

        Returns:
            Boolean
        """
    def set_parent(self, parent) -> None:
        """Set the parent header."""
    def close(self) -> None:
        """Close the stream."""
    @property
    def closed(self): ...
    def flush(self) -> None:
        """trigger actual zmq send

        send will happen in the background thread
        """
    def write(self, string: str) -> int | None:
        """Write to current stream after encoding if necessary

        Returns
        -------
        len : int
            number of items from input parameter written to stream.

        """
    def writelines(self, sequence) -> None:
        """Write lines to the stream."""
    def writable(self):
        """Test whether the stream is writable."""
    def register_hook(self, hook) -> None:
        """
        Registers a hook with the thread-local storage.

        Parameters
        ----------
        hook : Any callable object

        Returns
        -------
        Either a publishable message, or `None`.
        The hook callable must return a message from
        the __call__ method if they still require the
        `session.send` method to be called after transformation.
        Returning `None` will halt that execution path, and
        session.send will not be called.
        """
    def unregister_hook(self, hook):
        """
        Un-registers a hook with the thread-local storage.

        Parameters
        ----------
        hook : Any callable object which has previously been
            registered as a hook.

        Returns
        -------
        bool - `True` if the hook was removed, `False` if it wasn't
            found.
        """
