from .utils import close_container_client as close_container_client, close_credential as close_credential, close_service_client as close_service_client, filter_blobs as filter_blobs, get_blob_metadata as get_blob_metadata, match_blob_version as match_blob_version
from _typeshed import Incomplete
from datetime import datetime
from fsspec.asyn import AsyncFileSystem
from fsspec.spec import AbstractBufferedFile
from typing import Tuple

logger: Incomplete
FORWARDED_BLOB_PROPERTIES: Incomplete
VERSIONED_BLOB_PROPERTIES: Incomplete

def make_callback(key, callback): ...
def get_running_loop(): ...

class AzureBlobFileSystem(AsyncFileSystem):
    '''
    Access Azure Datalake Gen2 and Azure Storage if it were a file system using Multiprotocol Access

    Parameters
    ----------
    account_name: str
        The storage account name. This is used to authenticate requests
        signed with an account key and to construct the storage endpoint. It
        is required unless a connection string is given, or if a custom
        domain is used with anonymous authentication.
    account_key: str
        The storage account key. This is used for shared key authentication.
        If any of account key, sas token or client_id is specified, anonymous access
        will be used.
    sas_token: str
        A shared access signature token to use to authenticate requests
        instead of the account key. If account key and sas token are both
        specified, account key will be used to sign. If any of account key, sas token
        or client_id are specified, anonymous access will be used.
    request_session: Session
        The session object to use for http requests.
    connection_string: str
        If specified, this will override all other parameters besides
        request session. See
        http://azure.microsoft.com/en-us/documentation/articles/storage-configure-connection-string/
        for the connection string format.
    credential: TokenCredential or SAS token
        The credentials with which to authenticate.  Optional if the account URL already has a SAS token.
        Can include an instance of TokenCredential class from azure.identity
    blocksize: int
        The block size to use for download/upload operations. Defaults to the value of
        ``BlockBlobService.MAX_BLOCK_SIZE``
    client_id: str
        Client ID to use when authenticating using an AD Service Principal client/secret.
    client_secret: str
        Client secret to use when authenticating using an AD Service Principal client/secret.
    tenant_id: str
        Tenant ID to use when authenticating using an AD Service Principal client/secret.
    default_fill_cache: bool = True
        Whether to use cache filling with opoen by default
    default_cache_type: string (\'bytes\')
        If given, the default cache_type value used for "open()".  Set to none if no caching
        is desired.  Docs in fsspec
    version_aware : bool (False)
        Whether to support blob versioning.  If enable this will require the
        user to have the necessary permissions for dealing with versioned blobs.

    Pass on to fsspec:

    skip_instance_cache:  to control reuse of instances
    use_listings_cache, listings_expiry_time, max_paths: to control reuse of directory listings

    Examples
    --------

    Authentication with an account_key

    >>> abfs = AzureBlobFileSystem(account_name="XXXX", account_key="XXXX")
    >>> abfs.ls(\'\')

    Authentication with an Azure ServicePrincipal

    >>> abfs = AzureBlobFileSystem(account_name="XXXX", tenant_id=TENANT_ID,
    ...                            client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    >>> abfs.ls(\'\')

    Authentication with DefaultAzureCredential

    >>> abfs = AzureBlobFileSystem(account_name="XXXX", anon=False)
    >>> abfs.ls(\'\')

    Read files as

    >>> ddf = dd.read_csv(\'abfs://container_name/folder/*.csv\', storage_options={
    ...     \'account_name\': ACCOUNT_NAME, \'tenant_id\': TENANT_ID, \'client_id\': CLIENT_ID,
    ...     \'client_secret\': CLIENT_SECRET})
    ... })

    Sharded Parquet & csv files can be read as:

    >>> ddf = dd.read_csv(\'abfs://container_name/folder/*.csv\', storage_options={
    ...                   \'account_name\': ACCOUNT_NAME, \'account_key\': ACCOUNT_KEY})
    >>> ddf = dd.read_parquet(\'abfs://container_name/folder.parquet\', storage_options={
    ...                       \'account_name\': ACCOUNT_NAME, \'account_key\': ACCOUNT_KEY,})
    '''
    protocol: str
    account_name: Incomplete
    account_key: Incomplete
    connection_string: Incomplete
    sas_token: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    tenant_id: Incomplete
    anon: Incomplete
    location_mode: Incomplete
    credential: Incomplete
    request_session: Incomplete
    blocksize: Incomplete
    default_fill_cache: Incomplete
    default_cache_type: Incomplete
    version_aware: Incomplete
    sync_credential: Incomplete
    def __init__(self, account_name: str = None, account_key: str = None, connection_string: str = None, credential: str = None, sas_token: str = None, request_session: Incomplete | None = None, socket_timeout=..., blocksize: int = ..., client_id: str = None, client_secret: str = None, tenant_id: str = None, anon: bool = True, location_mode: str = 'primary', loop: Incomplete | None = None, asynchronous: bool = False, default_fill_cache: bool = True, default_cache_type: str = 'bytes', version_aware: bool = False, **kwargs) -> None: ...
    service_client: Incomplete
    account_url: Incomplete
    def do_connect(self) -> None:
        """Connect to the BlobServiceClient, using user-specified connection details.
        Tries credentials first, then connection string and finally account key

        Raises
        ------
        ValueError if none of the connection details are available
        """
    def split_path(self, path, delimiter: str = '/', return_container: bool = False, **kwargs) -> Tuple[str, str, str | None]:
        '''
        Normalize ABFS path string into bucket and key.

        Parameters
        ----------
        path : string
            Input path, like `abfs://my_container/path/to/file`

        delimiter: string
            Delimiter used to split the path

        return_container: bool

        Examples
        --------
        >>> split_path("abfs://my_container/path/to/file")
        [\'my_container\', \'path/to/file\']

        >>> split_path("abfs://my_container/path/to/versioned_file?versionid=some_version_id")
        [\'my_container\', \'path/to/versioned_file\', \'some_version_id\']
        '''
    def modified(self, path: str) -> datetime: ...
    def created(self, path: str) -> datetime: ...
    def glob(self, path, **kwargs): ...
    def find(self, path, withdirs: bool = False, prefix: str = '', **kwargs): ...
    mkdir: Incomplete
    def makedir(self, path, exist_ok: bool = False) -> None:
        """
        Create directory entry at path

        Parameters
        ----------
        path: str
            The path to create

        delimiter: str
            Delimiter to use when splitting the path

        exist_ok: bool
            If False (default), raise an error if the directory already exists.
        """
    rm: Incomplete
    def rmdir(self, path: str, delimiter: str = '/', **kwargs): ...
    def size(self, path): ...
    def isfile(self, path): ...
    def isdir(self, path): ...
    def exists(self, path): ...
    pipe_file: Incomplete
    def cat(self, path, recursive: bool = False, on_error: str = 'raise', **kwargs):
        '''Fetch (potentially multiple) paths\' contents
        Returns a dict of {path: contents} if there are multiple paths
        or the path has been otherwise expanded
        on_error : "raise", "omit", "return"
            If raise, an underlying exception will be raised (converted to KeyError
            if the type is in self.missing_exceptions); if omit, keys with exception
            will simply not be included in the output; if "return", all keys are
            included in the output, but the value will be bytes or an exception
            instance.
        '''
    def url(self, path, expires: int = 3600, **kwargs): ...
    def expand_path(self, path, recursive: bool = False, maxdepth: Incomplete | None = None, skip_noexist: bool = True): ...
    put_file: Incomplete
    cp_file: Incomplete
    def upload(self, lpath, rpath, recursive: bool = False, **kwargs):
        """Alias of :ref:`FilesystemSpec.put`."""
    def download(self, rpath, lpath, recursive: bool = False, **kwargs):
        """Alias of :ref:`FilesystemSpec.get`."""
    get_file: Incomplete
    def getxattr(self, path, attr): ...
    setxattrs: Incomplete
    def invalidate_cache(self, path: Incomplete | None = None) -> None: ...

class AzureBlobFile(AbstractBufferedFile):
    """File-like operations on Azure Blobs"""
    DEFAULT_BLOCK_SIZE: Incomplete
    fs: Incomplete
    path: Incomplete
    mode: Incomplete
    container_name: Incomplete
    blob: Incomplete
    block_size: Incomplete
    version_id: Incomplete
    loop: Incomplete
    container_client: Incomplete
    blocksize: Incomplete
    loc: int
    autocommit: Incomplete
    end: Incomplete
    start: Incomplete
    closed: bool
    metadata: Incomplete
    kwargs: Incomplete
    details: Incomplete
    size: Incomplete
    cache: Incomplete
    buffer: Incomplete
    offset: Incomplete
    forced: bool
    location: Incomplete
    def __init__(self, fs: AzureBlobFileSystem, path: str, mode: str = 'rb', block_size: str = 'default', autocommit: bool = True, cache_type: str = 'bytes', cache_options: dict = {}, metadata: Incomplete | None = None, version_id: str | None = None, **kwargs) -> None:
        '''
        Represents a file on AzureBlobStorage that implements buffered reading and writing

        Parameters
        ----------
        fs: AzureBlobFileSystem
            An instance of the filesystem

        path: str
            The location of the file on the filesystem

        mode: str
            What mode to open the file in. Defaults to "rb"

        block_size: int, str
            Buffer size for reading and writing. The string "default" will use the class
            default

        autocommit: bool
            Whether or not to write to the destination directly

        cache_type: str
            One of "readahead", "none", "mmap", "bytes", defaults to "readahead"
            Caching policy in read mode. See the definitions in ``core``.

        cache_options : dict
            Additional options passed to the constructor for the cache specified
            by `cache_type`.

        version_id : str
            Optional version to read the file at.  If not specified this will
            default to the current version of the object.  This is only used for
            reading.

        kwargs: dict
            Passed to AbstractBufferedFile
        '''
    def close(self) -> None:
        """Close file and azure client."""
    def connect_client(self) -> None:
        """Connect to the Asynchronous BlobServiceClient, using user-specified connection details.
        Tries credentials first, then connection string and finally account key

        Raises
        ------
        ValueError if none of the connection details are available
        """
    def __del__(self) -> None: ...
