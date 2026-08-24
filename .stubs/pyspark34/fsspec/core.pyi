import io
from .caching import BaseCache as BaseCache, BlockCache as BlockCache, BytesCache as BytesCache, MMapCache as MMapCache, ReadAheadCache as ReadAheadCache, caches as caches
from .compression import compr as compr
from .registry import filesystem as filesystem, get_filesystem_class as get_filesystem_class
from .utils import build_name_function as build_name_function, infer_compression as infer_compression, stringify_path as stringify_path
from _typeshed import Incomplete

logger: Incomplete

class OpenFile:
    """
    File-like object to be used in a context

    Can layer (buffered) text-mode and compression over any file-system, which
    are typically binary-only.

    These instances are safe to serialize, as the low-level file object
    is not created until invoked using ``with``.

    Parameters
    ----------
    fs: FileSystem
        The file system to use for opening the file. Should be a subclass or duck-type
        with ``fsspec.spec.AbstractFileSystem``
    path: str
        Location to open
    mode: str like 'rb', optional
        Mode of the opened file
    compression: str or None, optional
        Compression to apply
    encoding: str or None, optional
        The encoding to use if opened in text mode.
    errors: str or None, optional
        How to handle encoding errors if opened in text mode.
    newline: None or str
        Passed to TextIOWrapper in text mode, how to handle line endings.
    autoopen: bool
        If True, calls open() immediately. Mostly used by pickle
    pos: int
        If given and autoopen is True, seek to this location immediately
    """
    fs: Incomplete
    path: Incomplete
    mode: Incomplete
    compression: Incomplete
    encoding: Incomplete
    errors: Incomplete
    newline: Incomplete
    fobjects: Incomplete
    def __init__(self, fs, path, mode: str = 'rb', compression: Incomplete | None = None, encoding: Incomplete | None = None, errors: Incomplete | None = None, newline: Incomplete | None = None) -> None: ...
    def __reduce__(self): ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    @property
    def full_name(self): ...
    def open(self):
        """Materialise this as a real open file without context

        The OpenFile object should be explicitly closed to avoid enclosed file
        instances persisting. You must, therefore, keep a reference to the OpenFile
        during the life of the file-like it generates.
        """
    def close(self) -> None:
        """Close all encapsulated file objects"""

class OpenFiles(list):
    """List of OpenFile instances

    Can be used in a single context, which opens and closes all of the
    contained files. Normal list access to get the elements works as
    normal.

    A special case is made for caching filesystems - the files will
    be down/uploaded together at the start or end of the context, and
    this may happen concurrently, if the target filesystem supports it.
    """
    mode: Incomplete
    fs: Incomplete
    files: Incomplete
    def __init__(self, *args, mode: str = 'rb', fs: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def __getitem__(self, item): ...

def open_files(urlpath, mode: str = 'rb', compression: Incomplete | None = None, encoding: str = 'utf8', errors: Incomplete | None = None, name_function: Incomplete | None = None, num: int = 1, protocol: Incomplete | None = None, newline: Incomplete | None = None, auto_mkdir: bool = True, expand: bool = True, **kwargs):
    '''Given a path or paths, return a list of ``OpenFile`` objects.

    For writing, a str path must contain the "*" character, which will be filled
    in by increasing numbers, e.g., "part*" ->  "part1", "part2" if num=2.

    For either reading or writing, can instead provide explicit list of paths.

    Parameters
    ----------
    urlpath: string or list
        Absolute or relative filepath(s). Prefix with a protocol like ``s3://``
        to read from alternative filesystems. To read from multiple files you
        can pass a globstring or a list of paths, with the caveat that they
        must all have the same protocol.
    mode: \'rb\', \'wt\', etc.
    compression: string or None
        If given, open file using compression codec. Can either be a compression
        name (a key in ``fsspec.compression.compr``) or "infer" to guess the
        compression from the filename suffix.
    encoding: str
        For text mode only
    errors: None or str
        Passed to TextIOWrapper in text mode
    name_function: function or None
        if opening a set of files for writing, those files do not yet exist,
        so we need to generate their names by formatting the urlpath for
        each sequence number
    num: int [1]
        if writing mode, number of files we expect to create (passed to
        name+function)
    protocol: str or None
        If given, overrides the protocol found in the URL.
    newline: bytes or None
        Used for line terminator in text mode. If None, uses system default;
        if blank, uses no translation.
    auto_mkdir: bool (True)
        If in write mode, this will ensure the target directory exists before
        writing, by calling ``fs.mkdirs(exist_ok=True)``.
    expand: bool
    **kwargs: dict
        Extra options that make sense to a particular storage connection, e.g.
        host, port, username, password, etc.

    Examples
    --------
    >>> files = open_files(\'2015-*-*.csv\')  # doctest: +SKIP
    >>> files = open_files(
    ...     \'s3://bucket/2015-*-*.csv.gz\', compression=\'gzip\'
    ... )  # doctest: +SKIP

    Returns
    -------
    An ``OpenFiles`` instance, which is a list of ``OpenFile`` objects that can
    be used as a single context

    Notes
    -----
    For a full list of the available protocols and the implementations that
    they map across to see the latest online documentation:

    - For implementations built into ``fsspec`` see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations
    - For implementations in separate packages see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#other-known-implementations
    '''
def url_to_fs(url, **kwargs):
    """
    Turn fully-qualified and potentially chained URL into filesystem instance

    Parameters
    ----------
    url : str
        The fsspec-compatible URL
    **kwargs: dict
        Extra options that make sense to a particular storage connection, e.g.
        host, port, username, password, etc.

    Returns
    -------
    filesystem : FileSystem
        The new filesystem discovered from ``url`` and created with
        ``**kwargs``.
    urlpath : str
        The file-systems-specific URL for ``url``.
    """
def open(urlpath, mode: str = 'rb', compression: Incomplete | None = None, encoding: str = 'utf8', errors: Incomplete | None = None, protocol: Incomplete | None = None, newline: Incomplete | None = None, **kwargs):
    '''Given a path or paths, return one ``OpenFile`` object.

    Parameters
    ----------
    urlpath: string or list
        Absolute or relative filepath. Prefix with a protocol like ``s3://``
        to read from alternative filesystems. Should not include glob
        character(s).
    mode: \'rb\', \'wt\', etc.
    compression: string or None
        If given, open file using compression codec. Can either be a compression
        name (a key in ``fsspec.compression.compr``) or "infer" to guess the
        compression from the filename suffix.
    encoding: str
        For text mode only
    errors: None or str
        Passed to TextIOWrapper in text mode
    protocol: str or None
        If given, overrides the protocol found in the URL.
    newline: bytes or None
        Used for line terminator in text mode. If None, uses system default;
        if blank, uses no translation.
    **kwargs: dict
        Extra options that make sense to a particular storage connection, e.g.
        host, port, username, password, etc.

    Examples
    --------
    >>> openfile = open(\'2015-01-01.csv\')  # doctest: +SKIP
    >>> openfile = open(
    ...     \'s3://bucket/2015-01-01.csv.gz\', compression=\'gzip\'
    ... )  # doctest: +SKIP
    >>> with openfile as f:
    ...     df = pd.read_csv(f)  # doctest: +SKIP
    ...

    Returns
    -------
    ``OpenFile`` object.

    Notes
    -----
    For a full list of the available protocols and the implementations that
    they map across to see the latest online documentation:

    - For implementations built into ``fsspec`` see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations
    - For implementations in separate packages see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#other-known-implementations
    '''
def open_local(url, mode: str = 'rb', **storage_options):
    """Open file(s) which can be resolved to local

    For files which either are local, or get downloaded upon open
    (e.g., by file caching)

    Parameters
    ----------
    url: str or list(str)
    mode: str
        Must be read mode
    storage_options:
        passed on to FS for or used by open_files (e.g., compression)
    """
def get_compression(urlpath, compression): ...
def split_protocol(urlpath):
    """Return protocol, path pair"""
def strip_protocol(urlpath):
    """Return only path part of full URL, according to appropriate backend"""
def expand_paths_if_needed(paths, mode, num, fs, name_function):
    """Expand paths if they have a ``*`` in them (write mode) or any of ``*?[]``
    in them (read mode).

    :param paths: list of paths
    mode: str
        Mode in which to open files.
    num: int
        If opening in writing mode, number of files we expect to create.
    fs: filesystem object
    name_function: callable
        If opening in writing mode, this callable is used to generate path
        names. Names are generated for each partition by
        ``urlpath.replace('*', name_function(partition_index))``.
    :return: list of paths
    """
def get_fs_token_paths(urlpath, mode: str = 'rb', num: int = 1, name_function: Incomplete | None = None, storage_options: Incomplete | None = None, protocol: Incomplete | None = None, expand: bool = True):
    """Filesystem, deterministic token, and paths from a urlpath and options.

    Parameters
    ----------
    urlpath: string or iterable
        Absolute or relative filepath, URL (may include protocols like
        ``s3://``), or globstring pointing to data.
    mode: str, optional
        Mode in which to open files.
    num: int, optional
        If opening in writing mode, number of files we expect to create.
    name_function: callable, optional
        If opening in writing mode, this callable is used to generate path
        names. Names are generated for each partition by
        ``urlpath.replace('*', name_function(partition_index))``.
    storage_options: dict, optional
        Additional keywords to pass to the filesystem class.
    protocol: str or None
        To override the protocol specifier in the URL
    expand: bool
        Expand string paths for writing, assuming the path is a directory
    """

class PickleableTextIOWrapper(io.TextIOWrapper):
    """TextIOWrapper cannot be pickled. This solves it.

    Requires that ``buffer`` be pickleable, which all instances of
    AbstractBufferedFile are.
    """
    args: Incomplete
    def __init__(self, buffer, encoding: Incomplete | None = None, errors: Incomplete | None = None, newline: Incomplete | None = None, line_buffering: bool = False, write_through: bool = False) -> None: ...
    def __reduce__(self): ...
