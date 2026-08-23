import pathlib
import typing as t
from _typeshed import Incomplete
from jupyter_client.ioloop.manager import AsyncIOLoopKernelManager
from jupyter_client.multikernelmanager import AsyncMultiKernelManager, MultiKernelManager
from jupyter_server import DEFAULT_EVENTS_SCHEMA_PATH as DEFAULT_EVENTS_SCHEMA_PATH
from jupyter_server._tz import isoformat as isoformat, utcnow as utcnow
from jupyter_server.prometheus.metrics import KERNEL_CURRENTLY_RUNNING_TOTAL as KERNEL_CURRENTLY_RUNNING_TOTAL
from jupyter_server.utils import ApiPath as ApiPath, import_item as import_item, to_os_path as to_os_path

class MappingKernelManager(MultiKernelManager):
    """A KernelManager that handles
    - File mapping
    - HTTP error handling
    - Kernel message filtering
    """
    kernel_argv: Incomplete
    root_dir: Incomplete
    cull_idle_timeout: Incomplete
    cull_interval_default: int
    cull_interval: Incomplete
    cull_connected: Incomplete
    cull_busy: Incomplete
    buffer_offline_messages: Incomplete
    kernel_info_timeout: Incomplete
    last_kernel_activity: Incomplete
    pinned_superclass: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize a kernel manager."""
    allowed_message_types: Incomplete
    allow_tracebacks: Incomplete
    traceback_replacement_message: Incomplete
    def cwd_for_path(self, path, **kwargs):
        """Turn API path into absolute OS path."""
    start_kernel: Incomplete
    def ports_changed(self, kernel_id):
        """Used by ZMQChannelsHandler to determine how to coordinate nudge and replays.

        Ports are captured when starting a kernel (via MappingKernelManager).  Ports
        are considered changed (following restarts) if the referenced KernelManager
        is using a set of ports different from those captured at startup.  If changes
        are detected, the captured set is updated and a value of True is returned.

        NOTE: Use is exclusive to ZMQChannelsHandler because this object is a singleton
        instance while ZMQChannelsHandler instances are per WebSocket connection that
        can vary per kernel lifetime.
        """
    def start_buffering(self, kernel_id, session_key, channels) -> None:
        """Start buffering messages for a kernel

        Parameters
        ----------
        kernel_id : str
            The id of the kernel to stop buffering.
        session_key : str
            The session_key, if any, that should get the buffer.
            If the session_key matches the current buffered session_key,
            the buffer will be returned.
        channels : dict({'channel': ZMQStream})
            The zmq channels whose messages should be buffered.
        """
    def get_buffer(self, kernel_id, session_key):
        """Get the buffer for a given kernel

        Parameters
        ----------
        kernel_id : str
            The id of the kernel to stop buffering.
        session_key : str, optional
            The session_key, if any, that should get the buffer.
            If the session_key matches the current buffered session_key,
            the buffer will be returned.
        """
    def stop_buffering(self, kernel_id) -> None:
        """Stop buffering kernel messages

        Parameters
        ----------
        kernel_id : str
            The id of the kernel to stop buffering.
        """
    shutdown_kernel: Incomplete
    restart_kernel: Incomplete
    def notify_connect(self, kernel_id) -> None:
        """Notice a new connection to a kernel"""
    def notify_disconnect(self, kernel_id) -> None:
        """Notice a disconnection from a kernel"""
    def kernel_model(self, kernel_id):
        """Return a JSON-safe dict representing a kernel

        For use in representing kernels in the JSON APIs.
        """
    def list_kernels(self):
        """Returns a list of kernel_id's of kernels running."""
    def start_watching_activity(self, kernel_id) -> None:
        """Start watching IOPub messages on a kernel for activity.

        - update last_activity on every message
        - record execution_state from status messages
        """
    def stop_watching_activity(self, kernel_id) -> None:
        """Stop watching IOPub messages on a kernel for activity."""
    def initialize_culler(self) -> None:
        """Start idle culler if 'cull_idle_timeout' is greater than zero.

        Regardless of that value, set flag that we've been here.
        """
    async def cull_kernels(self) -> None:
        """Handle culling kernels."""
    async def cull_kernel_if_idle(self, kernel_id) -> None:
        """Cull a kernel if it is idle."""

class AsyncMappingKernelManager(MappingKernelManager, AsyncMultiKernelManager):
    """An asynchronous mapping kernel manager."""
    pinned_superclass: Incomplete
    last_kernel_activity: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize an async mapping kernel manager."""

def emit_kernel_action_event(success_msg: str = ''):
    '''Decorate kernel action methods to
    begin emitting jupyter kernel action events.

    Parameters
    ----------
    success_msg: str
        A formattable string thats passed to the message field of
        the emitted event when the action succeeds. You can include
        the kernel_id, kernel_name, or action in the message using
        a formatted string argument,
        e.g. "{kernel_id} succeeded to {action}."

    error_msg: str
        A formattable string thats passed to the message field of
        the emitted event when the action fails. You can include
        the kernel_id, kernel_name, or action in the message using
        a formatted string argument,
        e.g. "{kernel_id} failed to {action}."
    '''

class ServerKernelManager(AsyncIOLoopKernelManager):
    """A server-specific kernel manager."""
    execution_state: Incomplete
    reason: Incomplete
    last_activity: Incomplete
    @property
    def core_event_schema_paths(self) -> t.List[pathlib.Path]: ...
    extra_event_schema_paths: Incomplete
    event_logger: Incomplete
    def emit(self, schema_id, data) -> None:
        """Emit an event from the kernel manager."""
    async def start_kernel(self, *args, **kwargs): ...
    async def shutdown_kernel(self, *args, **kwargs): ...
    async def restart_kernel(self, *args, **kwargs): ...
    async def interrupt_kernel(self, *args, **kwargs): ...
