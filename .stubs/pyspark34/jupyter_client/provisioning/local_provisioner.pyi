from ..connect import KernelConnectionInfo as KernelConnectionInfo, LocalPortCache as LocalPortCache
from ..launcher import launch_kernel as launch_kernel
from ..localinterfaces import is_local_ip as is_local_ip, local_ips as local_ips
from .provisioner_base import KernelProvisionerBase as KernelProvisionerBase
from _typeshed import Incomplete
from typing import Any, Dict, List

class LocalProvisioner(KernelProvisionerBase):
    """
    :class:`LocalProvisioner` is a concrete class of ABC :py:class:`KernelProvisionerBase`
    and is the out-of-box default implementation used when no kernel provisioner is
    specified in the kernel specification (``kernel.json``).  It provides functional
    parity to existing applications by launching the kernel locally and using
    :class:`subprocess.Popen` to manage its lifecycle.

    This class is intended to be subclassed for customizing local kernel environments
    and serve as a reference implementation for other custom provisioners.
    """
    process: Incomplete
    pid: Incomplete
    pgid: Incomplete
    ip: Incomplete
    ports_cached: bool
    @property
    def has_process(self) -> bool: ...
    async def poll(self) -> int | None:
        """Poll the provisioner."""
    async def wait(self) -> int | None:
        """Wait for the provisioner process."""
    async def send_signal(self, signum: int) -> None:
        """Sends a signal to the process group of the kernel (this
        usually includes the kernel and any subprocesses spawned by
        the kernel).

        Note that since only SIGTERM is supported on Windows, we will
        check if the desired signal is for interrupt and apply the
        applicable code on Windows in that case.
        """
    async def kill(self, restart: bool = False) -> None:
        """Kill the provisioner and optionally restart."""
    async def terminate(self, restart: bool = False) -> None:
        """Terminate the provisioner and optionally restart."""
    async def cleanup(self, restart: bool = False) -> None:
        """Clean up the resources used by the provisioner and optionally restart."""
    connection_info: Incomplete
    async def pre_launch(self, **kwargs: Any) -> Dict[str, Any]:
        """Perform any steps in preparation for kernel process launch.

        This includes applying additional substitutions to the kernel launch command and env.
        It also includes preparation of launch parameters.

        Returns the updated kwargs.
        """
    async def launch_kernel(self, cmd: List[str], **kwargs: Any) -> KernelConnectionInfo:
        """Launch a kernel with a command."""
    async def get_provisioner_info(self) -> Dict:
        """Captures the base information necessary for persistence relative to this instance."""
    async def load_provisioner_info(self, provisioner_info: Dict) -> None:
        """Loads the base information necessary for persistence relative to this instance."""
