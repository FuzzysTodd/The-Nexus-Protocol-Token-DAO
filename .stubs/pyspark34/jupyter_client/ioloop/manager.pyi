import typing as t
from ..manager import AsyncKernelManager as AsyncKernelManager, KernelManager as KernelManager
from .restarter import AsyncIOLoopKernelRestarter as AsyncIOLoopKernelRestarter, IOLoopKernelRestarter as IOLoopKernelRestarter
from _typeshed import Incomplete

def as_zmqstream(f: t.Any) -> t.Callable:
    """Convert a socket to a zmq stream."""

class IOLoopKernelManager(KernelManager):
    """An io loop kernel manager."""
    loop: Incomplete
    restarter_class: Incomplete
    def start_restarter(self) -> None:
        """Start the restarter."""
    def stop_restarter(self) -> None:
        """Stop the restarter."""
    connect_shell: Incomplete
    connect_control: Incomplete
    connect_iopub: Incomplete
    connect_stdin: Incomplete
    connect_hb: Incomplete

class AsyncIOLoopKernelManager(AsyncKernelManager):
    """An async ioloop kernel manager."""
    loop: Incomplete
    restarter_class: Incomplete
    def start_restarter(self) -> None:
        """Start the restarter."""
    def stop_restarter(self) -> None:
        """Stop the restarter."""
    connect_shell: Incomplete
    connect_control: Incomplete
    connect_iopub: Incomplete
    connect_stdin: Incomplete
    connect_hb: Incomplete
