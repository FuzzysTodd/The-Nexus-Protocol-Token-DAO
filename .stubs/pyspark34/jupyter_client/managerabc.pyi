import abc
from typing import Any

class KernelManagerABC(metaclass=abc.ABCMeta):
    """KernelManager ABC.

    The docstrings for this class can be found in the base implementation:

    `jupyter_client.manager.KernelManager`
    """
    @property
    @abc.abstractmethod
    def kernel(self) -> Any: ...
    @abc.abstractmethod
    def start_kernel(self, **kw: Any) -> None:
        """Start the kernel."""
    @abc.abstractmethod
    def shutdown_kernel(self, now: bool = False, restart: bool = False) -> None:
        """Shut down the kernel."""
    @abc.abstractmethod
    def restart_kernel(self, now: bool = False, **kw: Any) -> None:
        """Restart the kernel."""
    @property
    @abc.abstractmethod
    def has_kernel(self) -> bool: ...
    @abc.abstractmethod
    def interrupt_kernel(self) -> None:
        """Interrupt the kernel."""
    @abc.abstractmethod
    def signal_kernel(self, signum: int) -> None:
        """Send a signal to the kernel."""
    @abc.abstractmethod
    def is_alive(self) -> bool:
        """Test whether the kernel is alive."""
