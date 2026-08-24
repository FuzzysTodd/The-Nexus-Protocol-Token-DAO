import typing as t
from . import kernelspec as kernelspec
from .asynchronous import AsyncKernelClient as AsyncKernelClient
from .blocking import BlockingKernelClient as BlockingKernelClient
from .client import KernelClient as KernelClient
from .connect import ConnectionFileMixin as ConnectionFileMixin
from .managerabc import KernelManagerABC as KernelManagerABC
from .provisioning import KernelProvisionerBase as KernelProvisionerBase
from _typeshed import Incomplete
from asyncio.futures import Future
from concurrent.futures import Future as CFuture
from enum import Enum
from traitlets import Bool, DottedObjectName, Float, Instance, Type, Unicode

class _ShutdownStatus(Enum):
    """

    This is so far used only for testing in order to track the internal state of
    the shutdown logic, and verifying which path is taken for which
    missbehavior.

    """
    Unset: Incomplete
    ShutdownRequest: str
    SigtermRequest: str
    SigkillRequest: str
F = t.TypeVar('F', bound=t.Callable[..., t.Any])

def in_pending_state(method: F) -> F:
    """Sets the kernel to a pending state by
    creating a fresh Future for the KernelManager's `ready`
    attribute. Once the method is finished, set the Future's results.
    """

class KernelManager(ConnectionFileMixin):
    """Manages a single kernel in a subprocess on this host.

    This version starts kernels with Popen.
    """
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize a kernel manager."""
    context: Instance
    client_class: DottedObjectName
    client_factory: Type
    kernel_id: str | Unicode
    provisioner: KernelProvisionerBase | None
    kernel_spec_manager: Instance
    shutdown_wait_time: Float
    kernel_name: str | Unicode
    @property
    def kernel_spec(self) -> kernelspec.KernelSpec | None: ...
    cache_ports: Bool
    @property
    def ready(self) -> CFuture | Future:
        """A future that resolves when the kernel process has started for the first time"""
    @property
    def ipykernel(self) -> bool: ...
    autorestart: Bool
    shutting_down: bool
    def __del__(self) -> None: ...
    def start_restarter(self) -> None:
        """Start the kernel restarter."""
    def stop_restarter(self) -> None:
        """Stop the kernel restarter."""
    def add_restart_callback(self, callback: t.Callable, event: str = 'restart') -> None:
        """Register a callback to be called when a kernel is restarted"""
    def remove_restart_callback(self, callback: t.Callable, event: str = 'restart') -> None:
        """Unregister a callback to be called when a kernel is restarted"""
    def client(self, **kwargs: t.Any) -> BlockingKernelClient:
        """Create a client configured to connect to our kernel"""
    def update_env(self, *, env: t.Dict[str, str]) -> None:
        """
        Allow to update the environment of a kernel manager.

        This will take effect only after kernel restart when the new env is
        passed to the new kernel.

        This is useful as some of the information of the current kernel reflect
        the state of the session that started it, and those session information
        (like the attach file path, or name), are mutable.

        .. version-added: 8.5
        """
    def format_kernel_cmd(self, extra_arguments: t.List[str] | None = None) -> t.List[str]:
        """Replace templated args (e.g. {connection_file})"""
    pre_start_kernel: Incomplete
    post_start_kernel: Incomplete
    start_kernel: Incomplete
    request_shutdown: Incomplete
    finish_shutdown: Incomplete
    cleanup_resources: Incomplete
    shutdown_kernel: Incomplete
    restart_kernel: Incomplete
    @property
    def owns_kernel(self) -> bool: ...
    @property
    def has_kernel(self) -> bool:
        """Has a kernel process been started that we are actively managing."""
    interrupt_kernel: Incomplete
    signal_kernel: Incomplete
    is_alive: Incomplete

class AsyncKernelManager(KernelManager):
    """An async kernel manager."""
    client_class: DottedObjectName
    client_factory: Type
    context: Instance
    def client(self, **kwargs: t.Any) -> AsyncKernelClient:
        """Get a client for the manager."""
    start_kernel: t.Callable[..., t.Awaitable]
    pre_start_kernel: t.Callable[..., t.Awaitable]
    post_start_kernel: t.Callable[..., t.Awaitable]
    request_shutdown: t.Callable[..., t.Awaitable]
    finish_shutdown: t.Callable[..., t.Awaitable]
    cleanup_resources: t.Callable[..., t.Awaitable]
    shutdown_kernel: t.Callable[..., t.Awaitable]
    restart_kernel: t.Callable[..., t.Awaitable]
    interrupt_kernel: t.Callable[..., t.Awaitable]
    signal_kernel: t.Callable[..., t.Awaitable]
    is_alive: t.Callable[..., t.Awaitable]

def start_new_kernel(startup_timeout: float = 60, kernel_name: str = 'python', **kwargs: t.Any) -> t.Tuple[KernelManager, BlockingKernelClient]:
    """Start a new kernel, and return its Manager and Client"""
async def start_new_async_kernel(startup_timeout: float = 60, kernel_name: str = 'python', **kwargs: t.Any) -> t.Tuple[AsyncKernelManager, AsyncKernelClient]:
    """Start a new kernel, and return its Manager and Client"""
def run_kernel(**kwargs: t.Any) -> t.Iterator[KernelClient]:
    """Context manager to create a kernel in a subprocess.

    The kernel is shut down when the context exits.

    Returns
    -------
    kernel_client: connected KernelClient instance
    """
