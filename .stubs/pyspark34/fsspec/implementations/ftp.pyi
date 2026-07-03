from ..spec import AbstractBufferedFile as AbstractBufferedFile, AbstractFileSystem as AbstractFileSystem
from ..utils import infer_storage_options as infer_storage_options, isfilelike as isfilelike
from _typeshed import Incomplete
from typing import Any

class FTPFileSystem(AbstractFileSystem):
    """A filesystem over classic FTP"""
    root_marker: str
    cachable: bool
    protocol: str
    host: Incomplete
    port: Incomplete
    tempdir: Incomplete
    cred: Incomplete
    timeout: Incomplete
    encoding: Incomplete
    blocksize: Incomplete
    def __init__(self, host, port: int = 21, username: Incomplete | None = None, password: Incomplete | None = None, acct: Incomplete | None = None, block_size: Incomplete | None = None, tempdir: Incomplete | None = None, timeout: int = 30, encoding: str = 'utf-8', **kwargs) -> None:
        '''
        You can use _get_kwargs_from_urls to get some kwargs from
        a reasonable FTP url.

        Authentication will be anonymous if username/password are not
        given.

        Parameters
        ----------
        host: str
            The remote server name/ip to connect to
        port: int
            Port to connect with
        username: str or None
            If authenticating, the user\'s identifier
        password: str of None
            User\'s password on the server, if using
        acct: str or None
            Some servers also need an "account" string for auth
        block_size: int or None
            If given, the read-ahead or write buffer size.
        tempdir: str
            Directory on remote to put temporary files when in a transaction
        timeout: int
            Timeout of the ftp connection in seconds
        encoding: str
            Encoding to use for directories and filenames in FTP connection
        '''
    def ls(self, path, detail: bool = True, **kwargs): ...
    def info(self, path, **kwargs): ...
    def get_file(self, rpath, lpath, **kwargs) -> None: ...
    def cat_file(self, path, start: Incomplete | None = None, end: Incomplete | None = None, **kwargs): ...
    def rm(self, path, recursive: bool = False, maxdepth: Incomplete | None = None) -> None: ...
    def mkdir(self, path: str, create_parents: bool = True, **kwargs: Any) -> None: ...
    def makedirs(self, path: str, exist_ok: bool = False) -> None: ...
    def rmdir(self, path) -> None: ...
    def mv(self, path1, path2, **kwargs) -> None: ...
    def __del__(self) -> None: ...
    def invalidate_cache(self, path: Incomplete | None = None) -> None: ...

class TransferDone(Exception):
    """Internal exception to break out of transfer"""

class FTPFile(AbstractBufferedFile):
    """Interact with a remote FTP file with read/write buffering"""
    target: Incomplete
    path: Incomplete
    def __init__(self, fs, path, mode: str = 'rb', block_size: str = 'default', autocommit: bool = True, cache_type: str = 'readahead', cache_options: Incomplete | None = None, **kwargs) -> None: ...
    def commit(self) -> None: ...
    def discard(self) -> None: ...
