from .constants import INPROCESS_KEY as INPROCESS_KEY
from _typeshed import Incomplete
from jupyter_client.manager import KernelManager

class InProcessKernelManager(KernelManager):
    """A manager for an in-process kernel.

    This class implements the interface of
    `jupyter_client.kernelmanagerabc.KernelManagerABC` and allows
    (asynchronous) frontends to be used seamlessly with an in-process kernel.

    See `jupyter_client.kernelmanager.KernelManager` for docstrings.
    """
    kernel: Incomplete
    client_class: Incomplete
    def start_kernel(self, **kwds) -> None:
        """Start the kernel."""
    def shutdown_kernel(self) -> None:
        """Shutdown the kernel."""
    def restart_kernel(self, now: bool = False, **kwds) -> None:
        """Restart the kernel."""
    @property
    def has_kernel(self): ...
    def interrupt_kernel(self) -> None:
        """Interrupt the kernel."""
    def signal_kernel(self, signum) -> None:
        """Send a signal to the kernel."""
    def is_alive(self):
        """Test if the kernel is alive."""
    def client(self, **kwargs):
        """Get a client for the kernel."""
