import io
from _typeshed import Incomplete
from fsspec.spec import AbstractFileSystem as AbstractFileSystem
from fsspec.utils import get_package_version_without_import as get_package_version_without_import, infer_storage_options as infer_storage_options, mirror_from as mirror_from, tokenize as tokenize
from functools import cached_property as cached_property

def wrap_exceptions(func): ...

PYARROW_VERSION: Incomplete

class ArrowFSWrapper(AbstractFileSystem):
    """FSSpec-compatible wrapper of pyarrow.fs.FileSystem.

    Parameters
    ----------
    fs : pyarrow.fs.FileSystem

    """
    root_marker: str
    fs: Incomplete
    def __init__(self, fs, **kwargs) -> None: ...
    @property
    def protocol(self): ...
    @cached_property
    def fsid(self): ...
    def ls(self, path, detail: bool = False, **kwargs): ...
    def info(self, path, **kwargs): ...
    def exists(self, path): ...
    def cp_file(self, path1, path2, **kwargs) -> None: ...
    def mv(self, path1, path2, **kwargs) -> None: ...
    mv_file = mv
    def rm_file(self, path) -> None: ...
    def rm(self, path, recursive: bool = False, maxdepth: Incomplete | None = None) -> None: ...
    def mkdir(self, path, create_parents: bool = True, **kwargs) -> None: ...
    def makedirs(self, path, exist_ok: bool = False) -> None: ...
    def rmdir(self, path) -> None: ...
    def modified(self, path): ...
    def cat_file(self, path, start: Incomplete | None = None, end: Incomplete | None = None, **kwargs): ...
    def get_file(self, rpath, lpath, **kwargs) -> None: ...

class ArrowFile(io.IOBase):
    path: Incomplete
    mode: Incomplete
    fs: Incomplete
    stream: Incomplete
    blocksize: Incomplete
    kwargs: Incomplete
    def __init__(self, fs, stream, path, mode, block_size: Incomplete | None = None, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

class HadoopFileSystem(ArrowFSWrapper):
    """A wrapper on top of the pyarrow.fs.HadoopFileSystem
    to connect it's interface with fsspec"""
    protocol: str
    def __init__(self, host: str = 'default', port: int = 0, user: Incomplete | None = None, kerb_ticket: Incomplete | None = None, extra_conf: Incomplete | None = None, **kwargs) -> None:
        '''

        Parameters
        ----------
        host: str
            Hostname, IP or "default" to try to read from Hadoop config
        port: int
            Port to connect on, or default from Hadoop config if 0
        user: str or None
            If given, connect as this username
        kerb_ticket: str or None
            If given, use this ticket for authentication
        extra_conf: None or dict
            Passed on to HadoopFileSystem
        '''
