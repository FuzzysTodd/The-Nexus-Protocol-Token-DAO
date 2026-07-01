import typing as t
from . import __version__ as __version__
from .kernelspec import KernelSpecManager as KernelSpecManager
from .provisioning.factory import KernelProvisionerFactory as KernelProvisionerFactory
from _typeshed import Incomplete
from jupyter_core.application import JupyterApp
from traitlets.config.application import Application

class ListKernelSpecs(JupyterApp):
    """An app to list kernel specs."""
    version = __version__
    description: str
    kernel_spec_manager: Incomplete
    json_output: Incomplete
    flags: Incomplete
    def start(self) -> dict[str, t.Any] | None:
        """Start the application."""

class InstallKernelSpec(JupyterApp):
    """An app to install a kernel spec."""
    version = __version__
    description: str
    examples: str
    usage: str
    kernel_spec_manager: Incomplete
    sourcedir: Incomplete
    kernel_name: Incomplete
    user: Incomplete
    prefix: Incomplete
    replace: Incomplete
    aliases: Incomplete
    flags: Incomplete
    def parse_command_line(self, argv: None | list[str]) -> None:
        """Parse the command line args."""
    def start(self) -> None:
        """Start the application."""

class RemoveKernelSpec(JupyterApp):
    """An app to remove a kernel spec."""
    version = __version__
    description: str
    examples: str
    force: Incomplete
    spec_names: Incomplete
    kernel_spec_manager: Incomplete
    flags: Incomplete
    def parse_command_line(self, argv: list[str] | None) -> None:
        """Parse the command line args."""
    def start(self) -> None:
        """Start the application."""

class InstallNativeKernelSpec(JupyterApp):
    """An app to install the native kernel spec."""
    version = __version__
    description: str
    kernel_spec_manager: Incomplete
    user: Incomplete
    flags: Incomplete
    def start(self) -> None:
        """Start the application."""

class ListProvisioners(JupyterApp):
    """An app to list provisioners."""
    version = __version__
    description: str
    def start(self) -> None:
        """Start the application."""

class KernelSpecApp(Application):
    """An app to manage kernel specs."""
    version = __version__
    name: str
    description: str
    subcommands: Incomplete
    aliases: Incomplete
    flags: Incomplete
    def start(self) -> None:
        """Start the application."""
