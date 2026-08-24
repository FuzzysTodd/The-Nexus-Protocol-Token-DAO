from ..caching import AllBytes as AllBytes
from _typeshed import Incomplete
from fsspec.asyn import AbstractAsyncStreamedFile as AbstractAsyncStreamedFile, AsyncFileSystem as AsyncFileSystem, sync as sync, sync_wrapper as sync_wrapper
from fsspec.exceptions import FSTimeoutError as FSTimeoutError
from fsspec.spec import AbstractBufferedFile as AbstractBufferedFile
from fsspec.utils import DEFAULT_BLOCK_SIZE as DEFAULT_BLOCK_SIZE, isfilelike as isfilelike, nullcontext as nullcontext, tokenize as tokenize

ex: Incomplete
ex2: Incomplete
logger: Incomplete

async def get_client(**kwargs): ...

class HTTPFileSystem(AsyncFileSystem):
    '''
    Simple File-System for fetching data via HTTP(S)

    ``ls()`` is implemented by loading the parent page and doing a regex
    match on the result. If simple_link=True, anything of the form
    "http(s)://server.com/stuff?thing=other"; otherwise only links within
    HTML href tags will be used.
    '''
    sep: str
    block_size: Incomplete
    simple_links: Incomplete
    same_schema: Incomplete
    cache_type: Incomplete
    cache_options: Incomplete
    client_kwargs: Incomplete
    get_client: Incomplete
    encoded: Incomplete
    kwargs: Incomplete
    use_listings_cache: Incomplete
    def __init__(self, simple_links: bool = True, block_size: Incomplete | None = None, same_scheme: bool = True, size_policy: Incomplete | None = None, cache_type: str = 'bytes', cache_options: Incomplete | None = None, asynchronous: bool = False, loop: Incomplete | None = None, client_kwargs: Incomplete | None = None, get_client=..., encoded: bool = False, **storage_options) -> None:
        """
        NB: if this is called async, you must await set_client

        Parameters
        ----------
        block_size: int
            Blocks to read bytes; if 0, will default to raw requests file-like
            objects instead of HTTPFile instances
        simple_links: bool
            If True, will consider both HTML <a> tags and anything that looks
            like a URL; if False, will consider only the former.
        same_scheme: True
            When doing ls/glob, if this is True, only consider paths that have
            http/https matching the input URLs.
        size_policy: this argument is deprecated
        client_kwargs: dict
            Passed to aiohttp.ClientSession, see
            https://docs.aiohttp.org/en/stable/client_reference.html
            For example, ``{'auth': aiohttp.BasicAuth('user', 'pass')}``
        get_client: Callable[..., aiohttp.ClientSession]
            A callable which takes keyword arguments and constructs
            an aiohttp.ClientSession. It's state will be managed by
            the HTTPFileSystem class.
        storage_options: key-value
            Any other parameters passed on to requests
        cache_type, cache_options: defaults used in open
        """
    @property
    def fsid(self): ...
    def encode_url(self, url): ...
    @staticmethod
    def close_session(loop, session) -> None: ...
    async def set_session(self): ...
    ls: Incomplete
    async def open_async(self, path, mode: str = 'rb', size: Incomplete | None = None, **kwargs): ...
    def ukey(self, url):
        """Unique identifier; assume HTTP files are static, unchanging"""

class HTTPFile(AbstractBufferedFile):
    """
    A file-like object pointing to a remove HTTP(S) resource

    Supports only reading, with read-ahead of a predermined block-size.

    In the case that the server does not supply the filesize, only reading of
    the complete file in one go is supported.

    Parameters
    ----------
    url: str
        Full URL of the remote resource, including the protocol
    session: requests.Session or None
        All calls will be made within this session, to avoid restarting
        connections where the server allows this
    block_size: int or None
        The amount of read-ahead to do, in bytes. Default is 5MB, or the value
        configured for the FileSystem creating this file
    size: None or int
        If given, this is the size of the file in bytes, and we don't attempt
        to call the server to find the value.
    kwargs: all other key-values are passed to requests calls.
    """
    asynchronous: Incomplete
    url: Incomplete
    session: Incomplete
    details: Incomplete
    loop: Incomplete
    def __init__(self, fs, url, session: Incomplete | None = None, block_size: Incomplete | None = None, mode: str = 'rb', cache_type: str = 'bytes', cache_options: Incomplete | None = None, size: Incomplete | None = None, loop: Incomplete | None = None, asynchronous: bool = False, **kwargs) -> None: ...
    def read(self, length: int = -1):
        """Read bytes from file

        Parameters
        ----------
        length: int
            Read up to this many bytes. If negative, read all content to end of
            file. If the server has not supplied the filesize, attempting to
            read only part of the data will raise a ValueError.
        """
    cache: Incomplete
    size: Incomplete
    async def async_fetch_all(self) -> None:
        """Read whole file in one shot, without caching

        This is only called when position is still at zero,
        and read() is called without a byte-count.
        """
    async def async_fetch_range(self, start, end):
        """Download a block of data

        The expectation is that the server returns only the requested bytes,
        with HTTP code 206. If this is not the case, we first check the headers,
        and then stream the output - if the data size is bigger than we
        requested, an exception is raised.
        """
    def __reduce__(self): ...

def reopen(fs, url, mode, blocksize, cache_type, size: Incomplete | None = None): ...

magic_check: Incomplete

def has_magic(s): ...

class HTTPStreamFile(AbstractBufferedFile):
    asynchronous: Incomplete
    url: Incomplete
    loop: Incomplete
    session: Incomplete
    details: Incomplete
    r: Incomplete
    def __init__(self, fs, url, mode: str = 'rb', loop: Incomplete | None = None, session: Incomplete | None = None, **kwargs) -> None: ...
    def seek(self, loc, whence: int = 0) -> None: ...
    read: Incomplete
    def close(self) -> None: ...
    def __reduce__(self): ...

class AsyncStreamFile(AbstractAsyncStreamedFile):
    url: Incomplete
    session: Incomplete
    r: Incomplete
    details: Incomplete
    kwargs: Incomplete
    size: Incomplete
    def __init__(self, fs, url, mode: str = 'rb', loop: Incomplete | None = None, session: Incomplete | None = None, size: Incomplete | None = None, **kwargs) -> None: ...
    async def read(self, num: int = -1): ...
    async def close(self) -> None: ...

async def get_range(session, url, start, end, file: Incomplete | None = None, **kwargs): ...

file_size: Incomplete
