import websocket
from .._tz import UTC as UTC, utcnow as utcnow
from ..services.kernels.kernelmanager import AsyncMappingKernelManager as AsyncMappingKernelManager, ServerKernelManager as ServerKernelManager, emit_kernel_action_event as emit_kernel_action_event
from ..services.sessions.sessionmanager import SessionManager as SessionManager
from ..utils import url_path_join as url_path_join
from .gateway_client import GatewayClient as GatewayClient, gateway_request as gateway_request
from _typeshed import Incomplete
from jupyter_client.asynchronous.client import AsyncKernelClient
from jupyter_client.kernelspec import KernelSpecManager
from logging import Logger
from queue import Queue
from typing import Any

class GatewayMappingKernelManager(AsyncMappingKernelManager):
    """Kernel manager that supports remote kernels hosted by Jupyter Kernel or Enterprise Gateway."""
    kernels_url: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize a gateway mapping kernel manager."""
    def remove_kernel(self, kernel_id):
        """Complete override since we want to be more tolerant of missing keys"""
    async def start_kernel(self, *, kernel_id: Incomplete | None = None, path: Incomplete | None = None, **kwargs):
        """Start a kernel for a session and return its kernel_id.

        Parameters
        ----------
        kernel_id : uuid
            The uuid to associate the new kernel with. If this
            is not None, this kernel will be persistent whenever it is
            requested.
        path : API path
            The API path (unicode, '/' delimited) for the cwd.
            Will be transformed to an OS path relative to root_dir.
        """
    async def kernel_model(self, kernel_id):
        """Return a dictionary of kernel information described in the
        JSON standard model.

        Parameters
        ----------
        kernel_id : uuid
            The uuid of the kernel.
        """
    async def list_kernels(self, **kwargs):
        """Get a list of running kernels from the Gateway server.

        We'll use this opportunity to refresh the models in each of
        the kernels we're managing.
        """
    async def shutdown_kernel(self, kernel_id, now: bool = False, restart: bool = False) -> None:
        """Shutdown a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to shutdown.
        now : bool
            Shutdown the kernel immediately (True) or gracefully (False)
        restart : bool
            The purpose of this shutdown is to restart the kernel (True)
        """
    async def restart_kernel(self, kernel_id, now: bool = False, **kwargs) -> None:
        """Restart a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to restart.
        """
    async def interrupt_kernel(self, kernel_id, **kwargs) -> None:
        """Interrupt a kernel by its kernel uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to interrupt.
        """
    async def shutdown_all(self, now: bool = False) -> None:
        """Shutdown all kernels."""
    async def cull_kernels(self) -> None:
        """Override cull_kernels, so we can be sure their state is current."""

class GatewayKernelSpecManager(KernelSpecManager):
    """A gateway kernel spec manager."""
    base_endpoint: Incomplete
    base_resource_endpoint: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize a gateway kernel spec manager."""
    async def get_all_specs(self):
        """Get all of the kernel specs for the gateway."""
    async def list_kernel_specs(self):
        """Get a list of kernel specs."""
    async def get_kernel_spec(self, kernel_name, **kwargs):
        """Get kernel spec for kernel_name.

        Parameters
        ----------
        kernel_name : str
            The name of the kernel.
        """
    async def get_kernel_spec_resource(self, kernel_name, path):
        """Get kernel spec for kernel_name.

        Parameters
        ----------
        kernel_name : str
            The name of the kernel.
        path : str
            The name of the desired resource
        """

class GatewaySessionManager(SessionManager):
    """A gateway session manager."""
    kernel_manager: Incomplete
    async def kernel_culled(self, kernel_id: str) -> bool:
        """Checks if the kernel is still considered alive and returns true if it's not found."""

class GatewayKernelManager(ServerKernelManager):
    """Manages a single kernel remotely via a Gateway Server."""
    kernel_id: str | None
    kernel: Incomplete
    kernels_url: Incomplete
    kernel_url: Incomplete
    execution_state: str
    last_activity: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize the gateway kernel manager."""
    @property
    def has_kernel(self):
        """Has a kernel been started that we are managing."""
    client_class: Incomplete
    client_factory: Incomplete
    def client(self, **kwargs):
        """Create a client configured to connect to our kernel"""
    async def refresh_model(self, model: Incomplete | None = None):
        """Refresh the kernel model.

        Parameters
        ----------
        model : dict
            The model from which to refresh the kernel.  If None, the kernel
            model is fetched from the Gateway server.
        """
    async def start_kernel(self, **kwargs) -> None:
        """Starts a kernel via HTTP in an asynchronous manner.

        Parameters
        ----------
        `**kwargs` : optional
             keyword arguments that are passed down to build the kernel_cmd
             and launching the kernel (e.g. Popen kwargs).
        """
    async def shutdown_kernel(self, now: bool = False, restart: bool = False) -> None:
        """Attempts to stop the kernel process cleanly via HTTP."""
    async def restart_kernel(self, **kw) -> None:
        """Restarts a kernel via HTTP."""
    async def interrupt_kernel(self) -> None:
        """Interrupts the kernel via an HTTP request."""
    async def is_alive(self):
        """Is the kernel process still running?"""
    def cleanup_resources(self, restart: bool = False) -> None:
        """Clean up resources when the kernel is shut down"""

class ChannelQueue(Queue):
    """A queue for a named channel."""
    channel_name: str | None
    response_router_finished: bool
    channel_socket: Incomplete
    log: Incomplete
    def __init__(self, channel_name: str, channel_socket: websocket.WebSocket, log: Logger) -> None:
        """Initialize a channel queue."""
    async def get_msg(self, *args: Any, **kwargs: Any) -> dict:
        """Get a message from the queue."""
    def send(self, msg: dict) -> None:
        """Send a message to the queue."""
    @staticmethod
    def serialize_datetime(dt):
        """Serialize a datetime object."""
    def start(self) -> None:
        """Start the queue."""
    def stop(self) -> None:
        """Stop the queue."""
    def is_alive(self) -> bool:
        """Whether the queue is alive."""

class HBChannelQueue(ChannelQueue):
    """A queue for the hearbeat channel."""
    def is_beating(self) -> bool:
        """Whether the channel is beating."""

class GatewayKernelClient(AsyncKernelClient):
    """Communicates with a single kernel indirectly via a websocket to a gateway server.

    There are five channels associated with each kernel:

    * shell: for request/reply calls to the kernel.
    * iopub: for the kernel to publish results to frontends.
    * hb: for monitoring the kernel's heartbeat.
    * stdin: for frontends to reply to raw_input calls in the kernel.
    * control: for kernel management calls to the kernel.

    The messages that can be sent on these channels are exposed as methods of the
    client (KernelClient.execute, complete, history, etc.). These methods only
    send the message, they don't wait for a reply. To get results, use e.g.
    :meth:`get_shell_msg` to fetch messages from the shell channel.
    """
    allow_stdin: bool
    kernel_id: Incomplete
    channel_socket: Incomplete
    response_router: Incomplete
    def __init__(self, kernel_id, **kwargs) -> None:
        """Initialize a gateway kernel client."""
    async def start_channels(self, shell: bool = True, iopub: bool = True, stdin: bool = True, hb: bool = True, control: bool = True) -> None:
        """Starts the channels for this kernel.

        For this class, we establish a websocket connection to the destination
        and set up the channel-based queues on which applicable messages will
        be posted.
        """
    def stop_channels(self) -> None:
        """Stops all the running channels for this kernel.

        For this class, we close the websocket connection and destroy the
        channel-based queues.
        """
    @property
    def shell_channel(self):
        """Get the shell channel object for this kernel."""
    @property
    def iopub_channel(self):
        """Get the iopub channel object for this kernel."""
    @property
    def stdin_channel(self):
        """Get the stdin channel object for this kernel."""
    @property
    def hb_channel(self):
        """Get the hb channel object for this kernel."""
    @property
    def control_channel(self):
        """Get the control channel object for this kernel."""
