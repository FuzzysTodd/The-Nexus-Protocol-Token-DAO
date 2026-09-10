from _typeshed import Incomplete

def preexec_fn() -> None: ...
PtyProcessUnicode = object
preexec_fn: Incomplete
ENV_PREFIX: str
DEFAULT_TERM_TYPE: str

class PtyWithClients:
    clients: Incomplete
    read_buffer: Incomplete
    ptyproc: Incomplete
    def __init__(self, argv, env: Incomplete | None = None, cwd: Incomplete | None = None) -> None: ...
    def resize_to_smallest(self) -> None:
        """Set the terminal size to that of the smallest client dimensions.

        A terminal not using the full space available is much nicer than a
        terminal trying to use more than the available space, so we keep it
        sized to the smallest client.
        """
    def kill(self, sig=...) -> None:
        """Send a signal to the process in the pty"""
    def killpg(self, sig=...):
        """Send a signal to the process group of the process in the pty"""
    async def terminate(self, force: bool = False):
        '''This forces a child process to terminate. It starts nicely with
        SIGHUP and SIGINT. If "force" is True then moves onto SIGKILL. This
        returns True if the child was terminated. This returns False if the
        child could not be terminated.'''

class TermManagerBase:
    """Base class for a terminal manager."""
    shell_command: Incomplete
    server_url: Incomplete
    term_settings: Incomplete
    extra_env: Incomplete
    log: Incomplete
    ptys_by_fd: Incomplete
    blocking_io_executor: Incomplete
    def __init__(self, shell_command, server_url: str = '', term_settings: Incomplete | None = None, extra_env: Incomplete | None = None, ioloop: Incomplete | None = None, blocking_io_executor: Incomplete | None = None) -> None: ...
    def make_term_env(self, height: int = 25, width: int = 80, winheight: int = 0, winwidth: int = 0, **kwargs):
        """Build the environment variables for the process in the terminal."""
    def new_terminal(self, **kwargs):
        """Make a new terminal, return a :class:`PtyWithClients` instance."""
    def start_reading(self, ptywclients) -> None:
        """Connect a terminal to the tornado event loop to read data from it."""
    def on_eof(self, ptywclients) -> None:
        """Called when the pty has closed."""
    def pty_read(self, fd, events: Incomplete | None = None) -> None:
        """Called by the event loop when there is pty data ready to read."""
    def pre_pty_read_hook(self, ptywclients) -> None:
        """Hook before pty read, subclass can patch something into ptywclients when pty_read"""
    def get_terminal(self, url_component: Incomplete | None = None) -> None:
        """Override in a subclass to give a terminal to a new websocket connection

        The :class:`TermSocket` handler works with zero or one URL components
        (capturing groups in the URL spec regex). If it receives one, it is
        passed as the ``url_component`` parameter; otherwise, this is None.
        """
    def client_disconnected(self, websocket) -> None:
        """Override this to e.g. kill terminals on client disconnection."""
    async def shutdown(self) -> None: ...
    async def kill_all(self) -> None: ...

class SingleTermManager(TermManagerBase):
    """All connections to the websocket share a common terminal."""
    terminal: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def get_terminal(self, url_component: Incomplete | None = None): ...
    async def kill_all(self) -> None: ...

class MaxTerminalsReached(Exception):
    max_terminals: Incomplete
    def __init__(self, max_terminals) -> None: ...

class UniqueTermManager(TermManagerBase):
    """Give each websocket a unique terminal to use."""
    max_terminals: Incomplete
    def __init__(self, max_terminals: Incomplete | None = None, **kwargs) -> None: ...
    def get_terminal(self, url_component: Incomplete | None = None): ...
    def client_disconnected(self, websocket) -> None:
        """Send terminal SIGHUP when client disconnects."""

class NamedTermManager(TermManagerBase):
    """Share terminals between websockets connected to the same endpoint."""
    max_terminals: Incomplete
    terminals: Incomplete
    def __init__(self, max_terminals: Incomplete | None = None, **kwargs) -> None: ...
    def get_terminal(self, term_name): ...
    name_template: str
    def new_named_terminal(self, **kwargs): ...
    def kill(self, name, sig=...) -> None: ...
    async def terminate(self, name, force: bool = False) -> None: ...
    def on_eof(self, ptywclients) -> None: ...
    async def kill_all(self) -> None: ...
