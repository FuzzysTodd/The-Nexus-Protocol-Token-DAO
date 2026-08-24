import io
from .. import config as config
from ..filesystems import COMPRESSION_FILESYSTEMS as COMPRESSION_FILESYSTEMS
from ..utils.file_utils import get_authentication_headers_for_url as get_authentication_headers_for_url, get_datasets_user_agent as get_datasets_user_agent, http_head as http_head, is_local_path as is_local_path, is_relative_path as is_relative_path, url_or_path_join as url_or_path_join
from ..utils.logging import get_logger as get_logger
from ..utils.py_utils import map_nested as map_nested
from .download_config import DownloadConfig as DownloadConfig
from _typeshed import Incomplete
from typing import Callable, Iterable, List, Tuple

logger: Incomplete
BASE_KNOWN_EXTENSIONS: Incomplete
COMPRESSION_EXTENSION_TO_PROTOCOL: Incomplete
SINGLE_FILE_COMPRESSION_PROTOCOLS: Incomplete
SINGLE_SLASH_AFTER_PROTOCOL_PATTERN: Incomplete
MAGIC_NUMBER_TO_COMPRESSION_PROTOCOL: Incomplete
MAGIC_NUMBER_TO_UNSUPPORTED_COMPRESSION_PROTOCOL: Incomplete
MAGIC_NUMBER_MAX_LENGTH: Incomplete

class NonStreamableDatasetError(Exception): ...

def xjoin(a, *p):
    '''
    This function extends os.path.join to support the "::" hop separator. It supports both paths and urls.

    A shorthand, particularly useful where you have multiple hops, is to “chain” the URLs with the special separator "::".
    This is used to access files inside a zip file over http for example.

    Let\'s say you have a zip file at https://host.com/archive.zip, and you want to access the file inside the zip file at /folder1/file.txt.
    Then you can just chain the url this way:

        zip://folder1/file.txt::https://host.com/archive.zip

    The xjoin function allows you to apply the join on the first path of the chain.

    Example::

        >>> xjoin("zip://folder1::https://host.com/archive.zip", "file.txt")
        zip://folder1/file.txt::https://host.com/archive.zip
    '''
def xdirname(a):
    '''
    This function extends os.path.dirname to support the "::" hop separator. It supports both paths and urls.

    A shorthand, particularly useful where you have multiple hops, is to “chain” the URLs with the special separator "::".
    This is used to access files inside a zip file over http for example.

    Let\'s say you have a zip file at https://host.com/archive.zip, and you want to access the file inside the zip file at /folder1/file.txt.
    Then you can just chain the url this way:

        zip://folder1/file.txt::https://host.com/archive.zip

    The xdirname function allows you to apply the dirname on the first path of the chain.

    Example::

        >>> xdirname("zip://folder1/file.txt::https://host.com/archive.zip")
        zip://folder1::https://host.com/archive.zip
    '''
def xexists(urlpath: str, download_config: DownloadConfig | None = None):
    """Extend `os.path.exists` function to support both local and remote files.

    Args:
        urlpath (`str`): URL path.
        download_config : mainly use token or storage_options to support different platforms and auth types.

    Returns:
        `bool`
    """
def xbasename(a):
    '''
    This function extends os.path.basename to support the "::" hop separator. It supports both paths and urls.

    A shorthand, particularly useful where you have multiple hops, is to “chain” the URLs with the special separator "::".
    This is used to access files inside a zip file over http for example.

    Let\'s say you have a zip file at https://host.com/archive.zip, and you want to access the file inside the zip file at /folder1/file.txt.
    Then you can just chain the url this way:

        zip://folder1/file.txt::https://host.com/archive.zip

    The xbasename function allows you to apply the basename on the first path of the chain.

    Example::

        >>> xbasename("zip://folder1/file.txt::https://host.com/archive.zip")
        file.txt
    '''
def xsplit(a):
    '''
    This function extends os.path.split to support the "::" hop separator. It supports both paths and urls.

    A shorthand, particularly useful where you have multiple hops, is to “chain” the URLs with the special separator "::".
    This is used to access files inside a zip file over http for example.

    Let\'s say you have a zip file at https://host.com/archive.zip, and you want to access the file inside the zip file at /folder1/file.txt.
    Then you can just chain the url this way:

        zip://folder1/file.txt::https://host.com/archive.zip

    The xsplit function allows you to apply the xsplit on the first path of the chain.

    Example::

        >>> xsplit("zip://folder1/file.txt::https://host.com/archive.zip")
        (\'zip://folder1::https://host.com/archive.zip\', \'file.txt\')
    '''
def xsplitext(a):
    '''
    This function extends os.path.splitext to support the "::" hop separator. It supports both paths and urls.

    A shorthand, particularly useful where you have multiple hops, is to “chain” the URLs with the special separator "::".
    This is used to access files inside a zip file over http for example.

    Let\'s say you have a zip file at https://host.com/archive.zip, and you want to access the file inside the zip file at /folder1/file.txt.
    Then you can just chain the url this way:

        zip://folder1/file.txt::https://host.com/archive.zip

    The xsplitext function allows you to apply the splitext on the first path of the chain.

    Example::

        >>> xsplitext("zip://folder1/file.txt::https://host.com/archive.zip")
        (\'zip://folder1/file::https://host.com/archive.zip\', \'.txt\')
    '''
def xisfile(path, download_config: DownloadConfig | None = None) -> bool:
    """Extend `os.path.isfile` function to support remote files.

    Args:
        path (`str`): URL path.
        download_config : mainly use token or storage_options to support different platforms and auth types.

    Returns:
        `bool`
    """
def xgetsize(path, download_config: DownloadConfig | None = None) -> int:
    """Extend `os.path.getsize` function to support remote files.

    Args:
        path (`str`): URL path.
        download_config : mainly use token or storage_options to support different platforms and auth types.

    Returns:
        `int`: optional
    """
def xisdir(path, download_config: DownloadConfig | None = None) -> bool:
    """Extend `os.path.isdir` function to support remote files.

    Args:
        path (`str`): URL path.
        download_config : mainly use token or storage_options to support different platforms and auth types.

    Returns:
        `bool`
    """
def xrelpath(path, start: Incomplete | None = None):
    """Extend `os.path.relpath` function to support remote files.

    Args:
        path (`str`): URL path.
        start (`str`): Start URL directory path.

    Returns:
        `str`
    """
def xopen(file: str, mode: str = 'r', *args, download_config: DownloadConfig | None = None, **kwargs):
    '''Extend `open` function to support remote files using `fsspec`.

    It also has a retry mechanism in case connection fails.
    The `args` and `kwargs` are passed to `fsspec.open`, except `token` which is used for queries to private repos on huggingface.co

    Args:
        file (`str`): Path name of the file to be opened.
        mode (`str`, *optional*, default "r"): Mode in which the file is opened.
        *args: Arguments to be passed to `fsspec.open`.
        download_config : mainly use token or storage_options to support different platforms and auth types.
        **kwargs: Keyword arguments to be passed to `fsspec.open`.

    Returns:
        file object
    '''
def xlistdir(path: str, download_config: DownloadConfig | None = None) -> List[str]:
    """Extend `os.listdir` function to support remote files.

    Args:
        path (`str`): URL path.
        download_config : mainly use token or storage_options to support different platforms and auth types.

    Returns:
        `list` of `str`
    """
def xglob(urlpath, *, recursive: bool = False, download_config: DownloadConfig | None = None):
    '''Extend `glob.glob` function to support remote files.

    Args:
        urlpath (`str`): URL path with shell-style wildcard patterns.
        recursive (`bool`, default `False`): Whether to match the "**" pattern recursively to zero or more
            directories or subdirectories.
        download_config : mainly use token or storage_options to support different platforms and auth types.

    Returns:
        `list` of `str`
    '''
def xwalk(urlpath, download_config: DownloadConfig | None = None, **kwargs):
    """Extend `os.walk` function to support remote files.

    Args:
        urlpath (`str`): URL root path.
        download_config : mainly use token or storage_options to support different platforms and auth types.
        **kwargs: Additional keyword arguments forwarded to the underlying filesystem.


    Yields:
        `tuple`: 3-tuple (dirpath, dirnames, filenames).
    """

class xPath(Incomplete):
    """Extension of `pathlib.Path` to support both local paths and remote URLs."""
    def exists(self, download_config: DownloadConfig | None = None):
        """Extend `pathlib.Path.exists` method to support both local and remote files.

        Args:
            download_config : mainly use token or storage_options to support different platforms and auth types.

        Returns:
            `bool`
        """
    def glob(self, pattern, download_config: DownloadConfig | None = None):
        """Glob function for argument of type :obj:`~pathlib.Path` that supports both local paths end remote URLs.

        Args:
            pattern (`str`): Pattern that resulting paths must match.
            download_config : mainly use token or storage_options to support different platforms and auth types.

        Yields:
            [`xPath`]
        """
    def rglob(self, pattern, **kwargs):
        """Rglob function for argument of type :obj:`~pathlib.Path` that supports both local paths end remote URLs.

        Args:
            pattern (`str`): Pattern that resulting paths must match.

        Yields:
            [`xPath`]
        """
    @property
    def parent(self) -> xPath:
        """Name function for argument of type :obj:`~pathlib.Path` that supports both local paths end remote URLs.

        Returns:
            [`xPath`]
        """
    @property
    def name(self) -> str:
        """Name function for argument of type :obj:`~pathlib.Path` that supports both local paths end remote URLs.

        Returns:
            `str`
        """
    @property
    def stem(self) -> str:
        """Stem function for argument of type :obj:`~pathlib.Path` that supports both local paths end remote URLs.

        Returns:
            `str`
        """
    @property
    def suffix(self) -> str:
        """Suffix function for argument of type :obj:`~pathlib.Path` that supports both local paths end remote URLs.

        Returns:
            `str`
        """
    def open(self, *args, **kwargs):
        """Extend :func:`xopen` to support argument of type :obj:`~pathlib.Path`.

        Args:
            **args: Arguments passed to :func:`fsspec.open`.
            **kwargs: Keyword arguments passed to :func:`fsspec.open`.

        Returns:
            `io.FileIO`: File-like object.
        """
    def joinpath(self, *p: Tuple[str, ...]) -> xPath:
        """Extend :func:`xjoin` to support argument of type :obj:`~pathlib.Path`.

        Args:
            *p (`tuple` of `str`): Other path components.

        Returns:
            [`xPath`]
        """
    def __truediv__(self, p: str) -> xPath: ...
    def with_suffix(self, suffix): ...

def xgzip_open(filepath_or_buffer, *args, download_config: DownloadConfig | None = None, **kwargs): ...
def xnumpy_load(filepath_or_buffer, *args, download_config: DownloadConfig | None = None, **kwargs): ...
def xpandas_read_csv(filepath_or_buffer, download_config: DownloadConfig | None = None, **kwargs): ...
def xpandas_read_excel(filepath_or_buffer, download_config: DownloadConfig | None = None, **kwargs): ...
def xsio_loadmat(filepath_or_buffer, download_config: DownloadConfig | None = None, **kwargs): ...
def xet_parse(source, parser: Incomplete | None = None, download_config: DownloadConfig | None = None):
    """Extend `xml.etree.ElementTree.parse` function to support remote files.

    Args:
        source: File path or file object.
        parser (`XMLParser`, *optional*, default `XMLParser`): Parser instance.
        download_config : mainly use token or storage_options to support different platforms and auth types.

    Returns:
        `xml.etree.ElementTree.Element`: Root element of the given source document.
    """
def xxml_dom_minidom_parse(filename_or_file, download_config: DownloadConfig | None = None, **kwargs):
    """Extend `xml.dom.minidom.parse` function to support remote files.

    Args:
        filename_or_file (`str` or file): File path or file object.
        download_config : mainly use token or storage_options to support different platforms and auth types.
        **kwargs (optional): Additional keyword arguments passed to `xml.dom.minidom.parse`.

    Returns:
        :obj:`xml.dom.minidom.Document`: Parsed document.
    """

class _IterableFromGenerator(Iterable):
    """Utility class to create an iterable from a generator function, in order to reset the generator when needed."""
    generator: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, generator: Callable, *args, **kwargs) -> None: ...
    def __iter__(self): ...

class ArchiveIterable(_IterableFromGenerator):
    """An iterable of (path, fileobj) from a TAR archive, used by `iter_archive`"""
    @classmethod
    def from_buf(cls, fileobj) -> ArchiveIterable: ...
    @classmethod
    def from_urlpath(cls, urlpath_or_buf, download_config: DownloadConfig | None = None) -> ArchiveIterable: ...

class FilesIterable(_IterableFromGenerator):
    """An iterable of paths from a list of directories or files"""
    @classmethod
    def from_urlpaths(cls, urlpaths, download_config: DownloadConfig | None = None) -> FilesIterable: ...

class StreamingDownloadManager:
    '''
    Download manager that uses the "::" separator to navigate through (possibly remote) compressed archives.
    Contrary to the regular `DownloadManager`, the `download` and `extract` methods don\'t actually download nor extract
    data, but they rather return the path or url that could be opened using the `xopen` function which extends the
    built-in `open` function to stream data from remote files.
    '''
    is_streaming: bool
    download_config: Incomplete
    def __init__(self, dataset_name: str | None = None, data_dir: str | None = None, download_config: DownloadConfig | None = None, base_path: str | None = None) -> None: ...
    @property
    def manual_dir(self): ...
    def download(self, url_or_urls):
        """Normalize URL(s) of files to stream data from.
        This is the lazy version of `DownloadManager.download` for streaming.

        Args:
            url_or_urls (`str` or `list` or `dict`):
                URL(s) of files to stream data from. Each url is a `str`.

        Returns:
            url(s): (`str` or `list` or `dict`), URL(s) to stream data from matching the given input url_or_urls.

        Example:

        ```py
        >>> downloaded_files = dl_manager.download('https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz')
        ```
        """
    def extract(self, url_or_urls):
        """Add extraction protocol for given url(s) for streaming.

        This is the lazy version of `DownloadManager.extract` for streaming.

        Args:
            url_or_urls (`str` or `list` or `dict`):
                URL(s) of files to stream data from. Each url is a `str`.

        Returns:
            url(s): (`str` or `list` or `dict`), URL(s) to stream data from matching the given input `url_or_urls`.

        Example:

        ```py
        >>> downloaded_files = dl_manager.download('https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz')
        >>> extracted_files = dl_manager.extract(downloaded_files)
        ```
        """
    def download_and_extract(self, url_or_urls):
        """Prepare given `url_or_urls` for streaming (add extraction protocol).

        This is the lazy version of `DownloadManager.download_and_extract` for streaming.

        Is equivalent to:

        ```
        urls = dl_manager.extract(dl_manager.download(url_or_urls))
        ```

        Args:
            url_or_urls (`str` or `list` or `dict`):
                URL(s) to stream from data from. Each url is a `str`.

        Returns:
            url(s): (`str` or `list` or `dict`), URL(s) to stream data from matching the given input `url_or_urls`.
        """
    def iter_archive(self, urlpath_or_buf: str | io.BufferedReader) -> Iterable[Tuple]:
        """Iterate over files within an archive.

        Args:
            urlpath_or_buf (`str` or `io.BufferedReader`):
                Archive path or archive binary file object.

        Yields:
            `tuple[str, io.BufferedReader]`:
                2-tuple (path_within_archive, file_object).
                File object is opened in binary mode.

        Example:

        ```py
        >>> archive = dl_manager.download('https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz')
        >>> files = dl_manager.iter_archive(archive)
        ```
        """
    def iter_files(self, urlpaths: str | List[str]) -> Iterable[str]:
        """Iterate over files.

        Args:
            urlpaths (`str` or `list` of `str`):
                Root paths.

        Yields:
            str: File URL path.

        Example:

        ```py
        >>> files = dl_manager.download_and_extract('https://huggingface.co/datasets/beans/resolve/main/data/train.zip')
        >>> files = dl_manager.iter_files(files)
        ```
        """
