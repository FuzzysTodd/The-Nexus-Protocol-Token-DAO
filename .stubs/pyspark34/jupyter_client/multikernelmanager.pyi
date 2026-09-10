import socket
import typing as t
from .connect import KernelConnectionInfo as KernelConnectionInfo
from .kernelspec import KernelSpecManager as KernelSpecManager, NATIVE_KERNEL_NAME as NATIVE_KERNEL_NAME
from .manager import KernelManager as KernelManager
from .utils import ensure_async as ensure_async, run_sync as run_sync, utcnow as utcnow
from _typeshed import Incomplete
from traitlets.config.configurable import LoggingConfigurable

class DuplicateKernelError(Exception): ...

def kernel_method(f: t.Callable) -> t.Callable:
    """decorator for proxying MKM.method(kernel_id) to individual KMs by ID"""

class MultiKernelManager(LoggingConfigurable):
    """A class for managing multiple kernels."""
    default_kernel_name: Incomplete
    kernel_spec_manager: Incomplete
    kernel_manager_class: Incomplete
    kernel_manager_factory: Incomplete
    shared_context: Incomplete
    context: Incomplete
    connection_dir: Incomplete
    external_connection_dir: Incomplete
    kernel_id_to_connection_file: Incomplete
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...
    def __del__(self) -> None:
        """Handle garbage collection.  Destroy context if applicable."""
    def list_kernel_ids(self) -> list[str]:
        """Return a list of the kernel ids of the active kernels."""
    def __len__(self) -> int:
        """Return the number of running kernels."""
    def __contains__(self, kernel_id: str) -> bool: ...
    def pre_start_kernel(self, kernel_name: str | None, kwargs: t.Any) -> tuple[KernelManager, str, str]: ...
    def update_env(self, *, kernel_id: str, env: t.Dict[str, str]) -> None:
        """
        Allow to update the environment of the given kernel.

        Forward the update env request to the corresponding kernel.

        .. version-added: 8.5
        """
    start_kernel: Incomplete
    shutdown_kernel: Incomplete
    def request_shutdown(self, kernel_id: str, restart: bool | None = False) -> None:
        """Ask a kernel to shut down by its kernel uuid"""
    def finish_shutdown(self, kernel_id: str, waittime: float | None = None, pollinterval: float | None = 0.1) -> None:
        """Wait for a kernel to finish shutting down, and kill it if it doesn't"""
    def cleanup_resources(self, kernel_id: str, restart: bool = False) -> None:
        """Clean up a kernel's resources"""
    def remove_kernel(self, kernel_id: str) -> KernelManager:
        """remove a kernel from our mapping.

        Mainly so that a kernel can be removed if it is already dead,
        without having to call shutdown_kernel.

        The kernel object is returned, or `None` if not found.
        """
    shutdown_all: Incomplete
    def interrupt_kernel(self, kernel_id: str) -> None:
        """Interrupt (SIGINT) the kernel by its uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to interrupt.
        """
    def signal_kernel(self, kernel_id: str, signum: int) -> None:
        """Sends a signal to the kernel by its uuid.

        Note that since only SIGTERM is supported on Windows, this function
        is only useful on Unix systems.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel to signal.
        signum : int
            Signal number to send kernel.
        """
    restart_kernel: Incomplete
    def is_alive(self, kernel_id: str) -> bool:
        """Is the kernel alive.

        This calls KernelManager.is_alive() which calls Popen.poll on the
        actual kernel subprocess.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel.
        """
    def get_kernel(self, kernel_id: str) -> KernelManager:
        """Get the single KernelManager object for a kernel by its uuid.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel.
        """
    def add_restart_callback(self, kernel_id: str, callback: t.Callable, event: str = 'restart') -> None:
        """add a callback for the KernelRestarter"""
    def remove_restart_callback(self, kernel_id: str, callback: t.Callable, event: str = 'restart') -> None:
        """remove a callback for the KernelRestarter"""
    def get_connection_info(self, kernel_id: str) -> dict[str, t.Any]:
        """Return a dictionary of connection data for a kernel.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel.

        Returns
        =======
        connection_dict : dict
            A dict of the information needed to connect to a kernel.
            This includes the ip address and the integer port
            numbers of the different channels (stdin_port, iopub_port,
            shell_port, hb_port).
        """
    def connect_iopub(self, kernel_id: str, identity: bytes | None = None) -> socket.socket:
        """Return a zmq Socket connected to the iopub channel.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel
        identity : bytes (optional)
            The zmq identity of the socket

        Returns
        =======
        stream : zmq Socket or ZMQStream
        """
    def connect_shell(self, kernel_id: str, identity: bytes | None = None) -> socket.socket:
        """Return a zmq Socket connected to the shell channel.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel
        identity : bytes (optional)
            The zmq identity of the socket

        Returns
        =======
        stream : zmq Socket or ZMQStream
        """
    def connect_control(self, kernel_id: str, identity: bytes | None = None) -> socket.socket:
        """Return a zmq Socket connected to the control channel.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel
        identity : bytes (optional)
            The zmq identity of the socket

        Returns
        =======
        stream : zmq Socket or ZMQStream
        """
    def connect_stdin(self, kernel_id: str, identity: bytes | None = None) -> socket.socket:
        """Return a zmq Socket connected to the stdin channel.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel
        identity : bytes (optional)
            The zmq identity of the socket

        Returns
        =======
        stream : zmq Socket or ZMQStream
        """
    def connect_hb(self, kernel_id: str, identity: bytes | None = None) -> socket.socket:
        """Return a zmq Socket connected to the hb channel.

        Parameters
        ==========
        kernel_id : uuid
            The id of the kernel
        identity : bytes (optional)
            The zmq identity of the socket

        Returns
        =======
        stream : zmq Socket or ZMQStream
        """
    def new_kernel_id(self, **kwargs: t.Any) -> str:
        """
        Returns the id to associate with the kernel for this request. Subclasses may override
        this method to substitute other sources of kernel ids.
        :param kwargs:
        :return: string-ized version 4 uuid
        """

class AsyncMultiKernelManager(MultiKernelManager):
    kernel_manager_class: Incomplete
    use_pending_kernels: Incomplete
    context: Incomplete
    start_kernel: t.Callable[..., t.Awaitable]
    restart_kernel: t.Callable[..., t.Awaitable]
    shutdown_kernel: t.Callable[..., t.Awaitable]
    shutdown_all: t.Callable[..., t.Awaitable]
