from .. import AbstractFileSystem as AbstractFileSystem
from ..utils import infer_storage_options as infer_storage_options
from _typeshed import Incomplete

class SMBFileSystem(AbstractFileSystem):
    """Allow reading and writing to Windows and Samba network shares.

    When using `fsspec.open()` for getting a file-like object the URI
    should be specified as this format:
    ``smb://workgroup;user:password@server:port/share/folder/file.csv``.

    Example::

        >>> import fsspec
        >>> with fsspec.open(
        ...     'smb://myuser:mypassword@myserver.com/' 'share/folder/file.csv'
        ... ) as smbfile:
        ...     df = pd.read_csv(smbfile, sep='|', header=None)

    Note that you need to pass in a valid hostname or IP address for the host
    component of the URL. Do not use the Windows/NetBIOS machine name for the
    host component.

    The first component of the path in the URL points to the name of the shared
    folder. Subsequent path components will point to the directory/folder/file.

    The URL components ``workgroup`` , ``user``, ``password`` and ``port`` may be
    optional.

    .. note::

        For working this source require `smbprotocol`_ to be installed, e.g.::

            $ pip install smbprotocol
            # or
            # pip install smbprotocol[kerberos]

    .. _smbprotocol: https://github.com/jborean93/smbprotocol#requirements

    Note: if using this with the ``open`` or ``open_files``, with full URLs,
    there is no way to tell if a path is relative, so all paths are assumed
    to be absolute.
    """
    protocol: str
    host: Incomplete
    port: Incomplete
    username: Incomplete
    password: Incomplete
    timeout: Incomplete
    encrypt: Incomplete
    temppath: Incomplete
    share_access: Incomplete
    def __init__(self, host, port: Incomplete | None = None, username: Incomplete | None = None, password: Incomplete | None = None, timeout: int = 60, encrypt: Incomplete | None = None, share_access: Incomplete | None = None, **kwargs) -> None:
        """
        You can use _get_kwargs_from_urls to get some kwargs from
        a reasonable SMB url.

        Authentication will be anonymous or integrated if username/password are not
        given.

        Parameters
        ----------
        host: str
            The remote server name/ip to connect to
        port: int or None
            Port to connect with. Usually 445, sometimes 139.
        username: str or None
            Username to connect with. Required if Kerberos auth is not being used.
        password: str or None
            User's password on the server, if using username
        timeout: int
            Connection timeout in seconds
        encrypt: bool
            Whether to force encryption or not, once this has been set to True
            the session cannot be changed back to False.
        share_access: str or None
            Specifies the default access applied to file open operations
            performed with this file system object.
            This affects whether other processes can concurrently open a handle
            to the same file.

            - None (the default): exclusively locks the file until closed.
            - 'r': Allow other handles to be opened with read access.
            - 'w': Allow other handles to be opened with write access.
            - 'd': Allow other handles to be opened with delete access.
        """
    def mkdir(self, path, create_parents: bool = True, **kwargs) -> None: ...
    def makedirs(self, path, exist_ok: bool = False) -> None: ...
    def rmdir(self, path) -> None: ...
    def info(self, path, **kwargs): ...
    def created(self, path):
        """Return the created timestamp of a file as a datetime.datetime"""
    def modified(self, path):
        """Return the modified timestamp of a file as a datetime.datetime"""
    def ls(self, path, detail: bool = True, **kwargs): ...
    def copy(self, path1, path2, **kwargs) -> None:
        """Copy within two locations in the same filesystem"""
    def mv(self, path1, path2, recursive: Incomplete | None = None, maxdepth: Incomplete | None = None, **kwargs) -> None: ...

class SMBFileOpener:
    """writes to remote temporary file, move on commit"""
    path: Incomplete
    temp: Incomplete
    mode: Incomplete
    block_size: Incomplete
    kwargs: Incomplete
    smbfile: Incomplete
    port: Incomplete
    def __init__(self, path, temp, mode, port: int = 445, block_size: int = -1, **kwargs) -> None: ...
    def commit(self) -> None:
        """Move temp file to definitive on success."""
    def discard(self) -> None:
        """Remove the temp file on failure."""
    def __fspath__(self): ...
    def __iter__(self): ...
    def __getattr__(self, item): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
