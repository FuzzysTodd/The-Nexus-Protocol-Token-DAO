import logging
import psutil
import typing as t
from ._version import kernel_protocol_version as kernel_protocol_version
from .control import CONTROL_THREAD_NAME as CONTROL_THREAD_NAME
from _typeshed import Incomplete
from ipykernel.jsonutil import json_clean as json_clean
from traitlets.config.configurable import SingletonConfigurable

class Kernel(SingletonConfigurable):
    """The base kernel class."""
    eventloop: Incomplete
    processes: t.Dict[str, psutil.Process]
    session: Incomplete
    profile_dir: Incomplete
    shell_stream: Incomplete
    shell_streams: Incomplete
    implementation: str
    implementation_version: str
    banner: str
    control_stream: Incomplete
    debug_shell_socket: Incomplete
    control_thread: Incomplete
    iopub_socket: Incomplete
    iopub_thread: Incomplete
    stdin_socket: Incomplete
    log: logging.Logger
    int_id: Incomplete
    ident: Incomplete
    language_info: t.Dict[str, object]
    help_links: Incomplete
    debug_just_my_code: Incomplete
    stop_on_error_timeout: Incomplete
    aborted: Incomplete
    execution_count: int
    msg_types: Incomplete
    control_msg_types: Incomplete
    shell_handlers: Incomplete
    control_handlers: Incomplete
    control_queue: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize the kernel."""
    def dispatch_control(self, msg) -> None: ...
    async def poll_control_queue(self) -> None: ...
    async def process_control(self, msg) -> None:
        """dispatch control requests"""
    def should_handle(self, stream, msg, idents):
        """Check whether a shell-channel message should be handled

        Allows subclasses to prevent handling of certain messages (e.g. aborted requests).
        """
    async def dispatch_shell(self, msg) -> None:
        """dispatch shell requests"""
    saved_sigint_handler: Incomplete
    def pre_handler_hook(self) -> None:
        """Hook to execute before calling message handler"""
    def post_handler_hook(self) -> None:
        """Hook to execute after calling message handler"""
    def enter_eventloop(self) -> None:
        """enter eventloop"""
    async def do_one_iteration(self) -> None:
        """Process a single shell message

        Any pending control messages will be flushed as well

        .. versionchanged:: 5
            This is now a coroutine
        """
    async def process_one(self, wait: bool = True) -> None:
        """Process one request

        Returns None if no message was handled.
        """
    async def dispatch_queue(self) -> None:
        """Coroutine to preserve order of message handling

        Ensures that only one message is processing at a time,
        even when the handler is async
        """
    def schedule_dispatch(self, dispatch, *args) -> None:
        """schedule a message for dispatch"""
    io_loop: Incomplete
    msg_queue: Incomplete
    def start(self) -> None:
        """register dispatchers for streams"""
    def record_ports(self, ports) -> None:
        """Record the ports that this kernel is using.

        The creator of the Kernel instance must call this methods if they
        want the :meth:`connect_request` method to return the port numbers.
        """
    def set_parent(self, ident, parent, channel: str = 'shell') -> None:
        """Set the current parent request

        Side effects (IOPub messages) and replies are associated with
        the request that caused them via the parent_header.

        The parent identity is used to route input_request messages
        on the stdin channel.
        """
    def get_parent(self, channel: Incomplete | None = None):
        """Get the parent request associated with a channel.

        .. versionadded:: 6

        Parameters
        ----------
        channel : str
            the name of the channel ('shell' or 'control')

        Returns
        -------
        message : dict
            the parent message for the most recent request on the channel.
        """
    def send_response(self, stream, msg_or_type, content: Incomplete | None = None, ident: Incomplete | None = None, buffers: Incomplete | None = None, track: bool = False, header: Incomplete | None = None, metadata: Incomplete | None = None, channel: Incomplete | None = None):
        """Send a response to the message we're currently processing.

        This accepts all the parameters of :meth:`jupyter_client.session.Session.send`
        except ``parent``.

        This relies on :meth:`set_parent` having been called for the current
        message.
        """
    def init_metadata(self, parent):
        """Initialize metadata.

        Run at the beginning of execution requests.
        """
    def finish_metadata(self, parent, metadata, reply_content):
        """Finish populating metadata.

        Run after completing an execution request.
        """
    async def execute_request(self, stream, ident, parent) -> None:
        """handle an execute_request"""
    def do_execute(self, code, silent, store_history: bool = True, user_expressions: Incomplete | None = None, allow_stdin: bool = False, *, cell_id: Incomplete | None = None) -> None:
        """Execute user code. Must be overridden by subclasses."""
    async def complete_request(self, stream, ident, parent) -> None:
        """Handle a completion request."""
    def do_complete(self, code, cursor_pos):
        """Override in subclasses to find completions."""
    async def inspect_request(self, stream, ident, parent) -> None:
        """Handle an inspect request."""
    def do_inspect(self, code, cursor_pos, detail_level: int = 0, omit_sections=()):
        """Override in subclasses to allow introspection."""
    async def history_request(self, stream, ident, parent) -> None:
        """Handle a history request."""
    def do_history(self, hist_access_type, output, raw, session: Incomplete | None = None, start: Incomplete | None = None, stop: Incomplete | None = None, n: Incomplete | None = None, pattern: Incomplete | None = None, unique: bool = False):
        """Override in subclasses to access history."""
    async def connect_request(self, stream, ident, parent) -> None:
        """Handle a connect request."""
    @property
    def kernel_info(self): ...
    async def kernel_info_request(self, stream, ident, parent) -> None:
        """Handle a kernel info request."""
    async def comm_info_request(self, stream, ident, parent) -> None:
        """Handle a comm info request."""
    async def interrupt_request(self, stream, ident, parent) -> None:
        """Handle an interrupt request."""
    async def shutdown_request(self, stream, ident, parent) -> None:
        """Handle a shutdown request."""
    def do_shutdown(self, restart):
        """Override in subclasses to do things when the frontend shuts down the
        kernel.
        """
    async def is_complete_request(self, stream, ident, parent) -> None:
        """Handle an is_complete request."""
    def do_is_complete(self, code):
        """Override in subclasses to find completions."""
    async def debug_request(self, stream, ident, parent) -> None:
        """Handle a debug request."""
    def get_process_metric_value(self, process, name, attribute: Incomplete | None = None):
        """Get the process metric value."""
    async def usage_request(self, stream, ident, parent) -> None:
        """Handle a usage request."""
    async def do_debug_request(self, msg) -> None: ...
    async def apply_request(self, stream, ident, parent) -> None:
        """Handle an apply request."""
    def do_apply(self, content, bufs, msg_id, reply_metadata) -> None:
        """DEPRECATED"""
    async def abort_request(self, stream, ident, parent) -> None:
        """abort a specific msg by id"""
    async def clear_request(self, stream, idents, parent) -> None:
        """Clear our namespace."""
    def do_clear(self) -> None:
        """DEPRECATED since 4.0.3"""
    def getpass(self, prompt: str = '', stream: Incomplete | None = None):
        """Forward getpass to frontends

        Raises
        ------
        StdinNotImplementedError if active frontend doesn't support stdin.
        """
    def raw_input(self, prompt: str = ''):
        """Forward raw_input to frontends

        Raises
        ------
        StdinNotImplementedError if active frontend doesn't support stdin.
        """
