from ..restarter import KernelRestarter as KernelRestarter
from _typeshed import Incomplete

class IOLoopKernelRestarter(KernelRestarter):
    """Monitor and autorestart a kernel."""
    loop: Incomplete
    def start(self) -> None:
        """Start the polling of the kernel."""
    def stop(self) -> None:
        """Stop the kernel polling."""

class AsyncIOLoopKernelRestarter(IOLoopKernelRestarter):
    """An async io loop kernel restarter."""
    async def poll(self) -> None:
        """Poll the kernel."""
