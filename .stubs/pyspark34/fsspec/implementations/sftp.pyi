from .. import AbstractFileSystem as AbstractFileSystem
from ..utils import infer_storage_options as infer_storage_options
from _typeshed import Incomplete

logger: Incomplete

class SFTPFileSystem(AbstractFileSystem):
    """Files over SFTP/SSH

    Peer-to-peer filesystem over SSH using paramiko.

    Note: if using this with the ``open`` or ``open_files``, with full URLs,
    there is no way to tell if a path is relative, so all paths are assumed
    to be absolute.
    """
    protocol: Incomplete
    temppath: Incomplete
    host: Incomplete
    ssh_kwargs: Incomplete
    def __init__(self, host, **ssh_kwargs) -> None:
        """

        Parameters
        ----------
        host: str
            Hostname or IP as a string
        temppath: str
            Location on the server to put files, when within a transaction
        ssh_kwargs: dict
            Parameters passed on to connection. See details in
            https://docs.paramiko.org/en/3.3/api/client.html#paramiko.client.SSHClient.connect
            May include port, username, password...
        """
    def mkdir(self, path, create_parents: bool = False, mode: int = 511) -> None: ...
    def makedirs(self, path, exist_ok: bool = False, mode: int = 511) -> None: ...
    def rmdir(self, path) -> None: ...
    def info(self, path): ...
    def ls(self, path, detail: bool = False): ...
    def put(self, lpath, rpath, callback: Incomplete | None = None, **kwargs) -> None: ...
    def get_file(self, rpath, lpath, **kwargs) -> None: ...
    def mv(self, old, new) -> None: ...

def commit_a_file(self) -> None: ...
def discard_a_file(self) -> None: ...
