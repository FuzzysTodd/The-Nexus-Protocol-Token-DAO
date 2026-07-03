from _typeshed import Incomplete
from jupyter_client.kernelspec import KernelSpecManager
from traitlets.config import Application
from typing import Any

pjoin: Incomplete
KERNEL_NAME: Incomplete
RESOURCES: Incomplete

def make_ipkernel_cmd(mod: str = 'ipykernel_launcher', executable: str | None = None, extra_arguments: list[str] | None = None) -> list[str]:
    """Build Popen command list for launching an IPython kernel.

    Parameters
    ----------
    mod : str, optional (default 'ipykernel')
        A string of an IPython module whose __main__ starts an IPython kernel
    executable : str, optional (default sys.executable)
        The Python executable to use for the kernel process.
    extra_arguments : list, optional
        A list of extra arguments to pass when executing the launch code.

    Returns
    -------
    A Popen command list
    """
def get_kernel_dict(extra_arguments: list[str] | None = None) -> dict[str, Any]:
    """Construct dict for kernel.json"""
def write_kernel_spec(path: str | None = None, overrides: dict[str, Any] | None = None, extra_arguments: list[str] | None = None) -> str:
    """Write a kernel spec directory to `path`

    If `path` is not specified, a temporary directory is created.
    If `overrides` is given, the kernelspec JSON is updated before writing.

    The path to the kernelspec is always returned.
    """
def install(kernel_spec_manager: KernelSpecManager | None = None, user: bool = False, kernel_name: str = ..., display_name: str | None = None, prefix: str | None = None, profile: str | None = None, env: dict[str, str] | None = None) -> str:
    """Install the IPython kernelspec for Jupyter

    Parameters
    ----------
    kernel_spec_manager : KernelSpecManager [optional]
        A KernelSpecManager to use for installation.
        If none provided, a default instance will be created.
    user : bool [default: False]
        Whether to do a user-only install, or system-wide.
    kernel_name : str, optional
        Specify a name for the kernelspec.
        This is needed for having multiple IPython kernels for different environments.
    display_name : str, optional
        Specify the display name for the kernelspec
    profile : str, optional
        Specify a custom profile to be loaded by the kernel.
    prefix : str, optional
        Specify an install prefix for the kernelspec.
        This is needed to install into a non-default location, such as a conda/virtual-env.
    env : dict, optional
        A dictionary of extra environment variables for the kernel.
        These will be added to the current environment variables before the
        kernel is started

    Returns
    -------
    The path where the kernelspec was installed.
    """

class InstallIPythonKernelSpecApp(Application):
    """Dummy app wrapping argparse"""
    name: Incomplete
    argv: Incomplete
    def initialize(self, argv: list[str] | None = None) -> None:
        """Initialize the app."""
    def start(self) -> None:
        """Start the app."""
