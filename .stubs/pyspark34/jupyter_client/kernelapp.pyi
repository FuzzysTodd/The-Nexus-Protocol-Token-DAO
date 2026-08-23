import typing as t
from . import __version__ as __version__
from .kernelspec import KernelSpecManager as KernelSpecManager, NATIVE_KERNEL_NAME as NATIVE_KERNEL_NAME
from .manager import KernelManager as KernelManager
from _typeshed import Incomplete
from jupyter_core.application import JupyterApp

class KernelApp(JupyterApp):
    """Launch a kernel by name in a local subprocess."""
    version = __version__
    description: str
    classes: Incomplete
    aliases: Incomplete
    flags: Incomplete
    kernel_name: Incomplete
    km: Incomplete
    loop: Incomplete
    def initialize(self, argv: str | t.Sequence[str] | None = None) -> None:
        """Initialize the application."""
    def setup_signals(self) -> None:
        """Shutdown on SIGTERM or SIGINT (Ctrl-C)"""
    def shutdown(self, signo: int) -> None:
        """Shut down the application."""
    def log_connection_info(self) -> None:
        """Log the connection info for the kernel."""
    def start(self) -> None:
        """Start the application."""

main: Incomplete
