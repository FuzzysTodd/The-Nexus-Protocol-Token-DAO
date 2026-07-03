import typing as t
from . import KernelManager as KernelManager, connect as connect, find_connection_file as find_connection_file, tunnel_to_kernel as tunnel_to_kernel
from .blocking import BlockingKernelClient as BlockingKernelClient
from .connect import KernelConnectionInfo as KernelConnectionInfo
from .kernelspec import NoSuchKernel as NoSuchKernel
from .localinterfaces import localhost as localhost
from .restarter import KernelRestarter as KernelRestarter
from .session import Session as Session
from _typeshed import Incomplete
from traitlets import Unicode

ConnectionFileMixin = connect.ConnectionFileMixin
flags: dict
app_flags: dict
aliases: dict
app_aliases: dict
classes: t.List[t.Type[t.Any]]

class JupyterConsoleApp(ConnectionFileMixin):
    """The base Jupyter console application."""
    name: str | Unicode
    description: str | Unicode
    classes = classes
    flags: Incomplete
    aliases: Incomplete
    kernel_manager_class: Incomplete
    kernel_client_class = BlockingKernelClient
    kernel_argv: Incomplete
    sshserver: Incomplete
    sshkey: Incomplete
    existing: Incomplete
    kernel_name: Incomplete
    confirm_exit: Incomplete
    def build_kernel_argv(self, argv: object = None) -> None:
        """build argv to be passed to kernel subprocess

        Override in subclasses if any args should be passed to the kernel
        """
    connection_file: Incomplete
    def init_connection_file(self) -> None:
        """find the connection file, and load the info if found.

        The current working directory and the current profile's security
        directory will be searched for the file if it is not given by
        absolute path.

        When attempting to connect to an existing kernel and the `--existing`
        argument does not match an existing file, it will be interpreted as a
        fileglob, and the matching file in the current profile's security dir
        with the latest access time will be used.

        After this method is called, self.connection_file contains the *full path*
        to the connection file, never just its name.
        """
    ip: Incomplete
    def init_ssh(self) -> None:
        """set up ssh tunnels, if needed."""
    kernel_manager: Incomplete
    shell_port: Incomplete
    iopub_port: Incomplete
    stdin_port: Incomplete
    hb_port: Incomplete
    control_port: Incomplete
    def init_kernel_manager(self) -> None:
        """Initialize the kernel manager."""
    kernel_client: Incomplete
    def init_kernel_client(self) -> None:
        """Initialize the kernel client."""
    def initialize(self, argv: object = None) -> None:
        """
        Classes which mix this class in should call:
               JupyterConsoleApp.initialize(self,argv)
        """

class IPythonConsoleApp(JupyterConsoleApp):
    """An app to manage an ipython console."""
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize the app."""
