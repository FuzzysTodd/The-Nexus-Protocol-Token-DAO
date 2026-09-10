from _typeshed import Incomplete
from azure.datalake.store.core import AzureDLFile
from fsspec import AbstractFileSystem

logger: Incomplete

class AzureDatalakeFileSystem(AbstractFileSystem):
    '''
    Access Azure Datalake Gen1 as if it were a file system.

    This exposes a filesystem-like API on top of Azure Datalake Storage

    Parameters
    -----------
    tenant_id:  string
        Azure tenant, also known as the subscription id
    client_id: string
        The username or serivceprincipal id
    client_secret: string
        The access key
    store_name: string (optional)
        The name of the datalake account being accessed.  Should be inferred from the urlpath
        if using with Dask read_xxx and to_xxx methods.

    Examples
    --------

    >>> adl = AzureDatalakeFileSystem(tenant_id="xxxx", client_id="xxxx",
    ...                               client_secret="xxxx")
    >>> adl.ls(\'\')

    Sharded Parquet & CSV files can be read as

    >>> storage_options = dict(tennant_id=TENNANT_ID, client_id=CLIENT_ID,
    ...                        client_secret=CLIENT_SECRET)  # doctest: +SKIP
    >>> ddf = dd.read_parquet(\'adl://store_name/folder/filename.parquet\',
    ...                       storage_options=storage_options)  # doctest: +SKIP

    >>> ddf = dd.read_csv(\'adl://store_name/folder/*.csv\'
    ...                   storage_options=storage_options)  # doctest: +SKIP


    Sharded Parquet and CSV files can be written as

    >>> ddf.to_parquet("adl://store_name/folder/filename.parquet",
    ...                storage_options=storage_options)  # doctest: +SKIP

    >>> ddf.to_csv(\'adl://store_name/folder/*.csv\'
    ...            storage_options=storage_options)  # doctest: +SKIP
    '''
    protocol: str
    tenant_id: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    store_name: Incomplete
    def __init__(self, tenant_id, client_id, client_secret, store_name) -> None: ...
    azure_fs: Incomplete
    def do_connect(self) -> None:
        """Establish connection object."""
    def ls(self, path, detail: bool = False, invalidate_cache: bool = True, **kwargs): ...
    def info(self, path, invalidate_cache: bool = True, expected_error_code: int = 404, **kwargs): ...
    def glob(self, path, details: bool = False, invalidate_cache: bool = True, **kwargs):
        """For a template path, return matching files"""
    def isdir(self, path, **kwargs):
        """Is this entry directory-like?"""
    def isfile(self, path, **kwargs):
        """Is this entry file-like?"""
    def read_block(self, fn, offset, length, delimiter: Incomplete | None = None, **kwargs): ...
    def ukey(self, path): ...
    def size(self, path): ...
    def rmdir(self, path) -> None:
        """Remove a directory, if empty"""
    def rm_file(self, path) -> None:
        """Delete a file"""

class AzureDatalakeFile(AzureDLFile):
    fs: Incomplete
    path: Incomplete
    mode: Incomplete
    def __init__(self, fs, path, mode: str = 'rb', autocommit: bool = True, block_size=..., cache_type: str = 'bytes', cache_options: Incomplete | None = None, *, delimiter: Incomplete | None = None, **kwargs) -> None: ...
    loc: Incomplete
    def seek(self, loc: int, whence: int = 0, **kwargs):
        """Set current file location

        Parameters
        ----------
        loc: int
            byte location

        whence: {0, 1, 2}
            from start of file, current location or end of file, resp.
        """
