import zmq
from _typeshed import Incomplete
from jupyter_client import BlockingKernelClient
from traitlets import Unicode
from traitlets.config import LoggingConfigurable, SingletonConfigurable
from typing import Any, Dict

__all__ = ['write_connection_file', 'find_connection_file', 'tunnel_to_kernel', 'KernelConnectionInfo', 'LocalPortCache']

KernelConnectionInfo = Dict[str, int | str | bytes]

def write_connection_file(fname: str | None = None, shell_port: int = 0, iopub_port: int = 0, stdin_port: int = 0, hb_port: int = 0, control_port: int = 0, ip: str = '', key: bytes = b'', transport: str = 'tcp', signature_scheme: str = 'hmac-sha256', kernel_name: str = '', **kwargs: Any) -> tuple[str, KernelConnectionInfo]:
    """Generates a JSON config file, including the selection of random ports.

    Parameters
    ----------

    fname : unicode
        The path to the file to write

    shell_port : int, optional
        The port to use for ROUTER (shell) channel.

    iopub_port : int, optional
        The port to use for the SUB channel.

    stdin_port : int, optional
        The port to use for the ROUTER (raw input) channel.

    control_port : int, optional
        The port to use for the ROUTER (control) channel.

    hb_port : int, optional
        The port to use for the heartbeat REP channel.

    ip  : str, optional
        The ip address the kernel will bind to.

    key : str, optional
        The Session key used for message authentication.

    signature_scheme : str, optional
        The scheme used for message authentication.
        This has the form 'digest-hash', where 'digest'
        is the scheme used for digests, and 'hash' is the name of the hash function
        used by the digest scheme.
        Currently, 'hmac' is the only supported digest scheme,
        and 'sha256' is the default hash function.

    kernel_name : str, optional
        The name of the kernel currently connected to.
    """
def find_connection_file(filename: str = 'kernel-*.json', path: str | list[str] | None = None, profile: str | None = None) -> str:
    """find a connection file, and return its absolute path.

    The current working directory and optional search path
    will be searched for the file if it is not given by absolute path.

    If the argument does not match an existing file, it will be interpreted as a
    fileglob, and the matching file in the profile's security dir with
    the latest access time will be used.

    Parameters
    ----------
    filename : str
        The connection file or fileglob to search for.
    path : str or list of strs[optional]
        Paths in which to search for connection files.

    Returns
    -------
    str : The absolute path of the connection file.
    """
def tunnel_to_kernel(connection_info: str | KernelConnectionInfo, sshserver: str, sshkey: str | None = None) -> tuple[Any, ...]:
    """tunnel connections to a kernel via ssh

    This will open five SSH tunnels from localhost on this machine to the
    ports associated with the kernel.  They can be either direct
    localhost-localhost tunnels, or if an intermediate server is necessary,
    the kernel must be listening on a public IP.

    Parameters
    ----------
    connection_info : dict or str (path)
        Either a connection dict, or the path to a JSON connection file
    sshserver : str
        The ssh sever to use to tunnel to the kernel. Can be a full
        `user@server:port` string. ssh config aliases are respected.
    sshkey : str [optional]
        Path to file containing ssh key to use for authentication.
        Only necessary if your ssh config does not already associate
        a keyfile with the host.

    Returns
    -------

    (shell, iopub, stdin, hb, control) : ints
        The five ports on localhost that have been forwarded to the kernel.
    """

class ConnectionFileMixin(LoggingConfigurable):
    """Mixin for configurable classes that work with connection files"""
    data_dir: str | Unicode
    connection_file: Incomplete
    transport: Incomplete
    kernel_name: str | Unicode
    context: Incomplete
    ip: Incomplete
    hb_port: Incomplete
    shell_port: Incomplete
    iopub_port: Incomplete
    stdin_port: Incomplete
    control_port: Incomplete
    @property
    def ports(self) -> list[int]: ...
    session: Incomplete
    def get_connection_info(self, session: bool = False) -> KernelConnectionInfo:
        """Return the connection info as a dict

        Parameters
        ----------
        session : bool [default: False]
            If True, return our session object will be included in the connection info.
            If False (default), the configuration parameters of our session object will be included,
            rather than the session object itself.

        Returns
        -------
        connect_info : dict
            dictionary of connection information.
        """
    blocking_class: Incomplete
    def blocking_client(self) -> BlockingKernelClient:
        """Make a blocking client connected to my kernel"""
    def cleanup_connection_file(self) -> None:
        """Cleanup connection file *if we wrote it*

        Will not raise if the connection file was already removed somehow.
        """
    def cleanup_ipc_files(self) -> None:
        """Cleanup ipc files if we wrote them."""
    def cleanup_random_ports(self) -> None:
        """Forgets randomly assigned port numbers and cleans up the connection file.

        Does nothing if no port numbers have been randomly assigned.
        In particular, does nothing unless the transport is tcp.
        """
    def write_connection_file(self, **kwargs: Any) -> None:
        """Write connection info to JSON dict in self.connection_file."""
    def load_connection_file(self, connection_file: str | None = None) -> None:
        """Load connection info from JSON dict in self.connection_file.

        Parameters
        ----------
        connection_file: unicode, optional
            Path to connection file to load.
            If unspecified, use self.connection_file
        """
    def load_connection_info(self, info: KernelConnectionInfo) -> None:
        """Load connection info from a dict containing connection info.

        Typically this data comes from a connection file
        and is called by load_connection_file.

        Parameters
        ----------
        info: dict
            Dictionary containing connection_info.
            See the connection_file spec for details.
        """
    def connect_iopub(self, identity: bytes | None = None) -> zmq.sugar.socket.Socket:
        """return zmq Socket connected to the IOPub channel"""
    def connect_shell(self, identity: bytes | None = None) -> zmq.sugar.socket.Socket:
        """return zmq Socket connected to the Shell channel"""
    def connect_stdin(self, identity: bytes | None = None) -> zmq.sugar.socket.Socket:
        """return zmq Socket connected to the StdIn channel"""
    def connect_hb(self, identity: bytes | None = None) -> zmq.sugar.socket.Socket:
        """return zmq Socket connected to the Heartbeat channel"""
    def connect_control(self, identity: bytes | None = None) -> zmq.sugar.socket.Socket:
        """return zmq Socket connected to the Control channel"""

class LocalPortCache(SingletonConfigurable):
    """
    Used to keep track of local ports in order to prevent race conditions that
    can occur between port acquisition and usage by the kernel.  All locally-
    provisioned kernels should use this mechanism to limit the possibility of
    race conditions.  Note that this does not preclude other applications from
    acquiring a cached but unused port, thereby re-introducing the issue this
    class is attempting to resolve (minimize).
    See: https://github.com/jupyter/jupyter_client/issues/487
    """
    currently_used_ports: Incomplete
    def __init__(self, **kwargs: Any) -> None: ...
    def find_available_port(self, ip: str) -> int: ...
    def return_port(self, port: int) -> None: ...
