import io
from .config import apply_config as apply_config, conf as conf
from .dircache import DirCache as DirCache
from .transaction import Transaction as Transaction
from .utils import isfilelike as isfilelike, other_paths as other_paths, read_block as read_block, stringify_path as stringify_path, tokenize as tokenize
from _typeshed import Incomplete
from collections.abc import Generator
from typing import ClassVar

logger: Incomplete

def make_instance(cls, args, kwargs): ...

class _Cached(type):
    """
    Metaclass for caching file system instances.

    Notes
    -----
    Instances are cached according to

    * The values of the class attributes listed in `_extra_tokenize_attributes`
    * The arguments passed to ``__init__``.

    This creates an additional reference to the filesystem, which prevents the
    filesystem from being garbage collected when all *user* references go away.
    A call to the :meth:`AbstractFileSystem.clear_instance_cache` must *also*
    be made for a filesystem instance to be garbage collected.
    """
    def __init__(cls, *args, **kwargs) -> None: ...
    def __call__(cls, *args, **kwargs): ...

class AbstractFileSystem(metaclass=_Cached):
    """
    An abstract super-class for pythonic file-systems

    Implementations are expected to be compatible with or, better, subclass
    from here.
    """
    cachable: bool
    blocksize: Incomplete
    sep: str
    protocol: ClassVar[str | tuple[str, ...]]
    async_impl: bool
    mirror_sync_methods: bool
    root_marker: str
    dircache: Incomplete
    def __init__(self, *args, **storage_options) -> None:
        """Create and configure file-system instance

        Instances may be cachable, so if similar enough arguments are seen
        a new instance is not required. The token attribute exists to allow
        implementations to cache instances if they wish.

        A reasonable default should be provided if there are no arguments.

        Subclasses should call this method.

        Parameters
        ----------
        use_listings_cache, listings_expiry_time, max_paths:
            passed to ``DirCache``, if the implementation supports
            directory listing caching. Pass use_listings_cache=False
            to disable such caching.
        skip_instance_cache: bool
            If this is a cachable implementation, pass True here to force
            creating a new instance even if a matching instance exists, and prevent
            storing this instance.
        asynchronous: bool
        loop: asyncio-compatible IOLoop or None
        """
    @property
    def fsid(self) -> None:
        """Persistent filesystem id that can be used to compare filesystems
        across sessions.
        """
    def __dask_tokenize__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __reduce__(self): ...
    def unstrip_protocol(self, name: str) -> str:
        """Format FS-specific path to generic, including protocol"""
    @classmethod
    def current(cls):
        """Return the most recently instantiated FileSystem

        If no instance has been created, then create one with defaults
        """
    @property
    def transaction(self):
        """A context within which files are committed together upon exit

        Requires the file class to implement `.commit()` and `.discard()`
        for the normal and exception cases.
        """
    def start_transaction(self):
        """Begin write transaction for deferring files, non-context version"""
    def end_transaction(self) -> None:
        """Finish write transaction, non-context version"""
    def invalidate_cache(self, path: Incomplete | None = None) -> None:
        """
        Discard any cached directory information

        Parameters
        ----------
        path: string or None
            If None, clear all listings cached else listings at or under given
            path.
        """
    def mkdir(self, path, create_parents: bool = True, **kwargs) -> None:
        """
        Create directory entry at path

        For systems that don't have true directories, may create an for
        this instance only and not touch the real filesystem

        Parameters
        ----------
        path: str
            location
        create_parents: bool
            if True, this is equivalent to ``makedirs``
        kwargs:
            may be permissions, etc.
        """
    def makedirs(self, path, exist_ok: bool = False) -> None:
        """Recursively make directories

        Creates directory at path and any intervening required directories.
        Raises exception if, for instance, the path already exists but is a
        file.

        Parameters
        ----------
        path: str
            leaf directory name
        exist_ok: bool (False)
            If False, will error if the target already exists
        """
    def rmdir(self, path) -> None:
        """Remove a directory, if empty"""
    def ls(self, path, detail: bool = True, **kwargs) -> None:
        '''List objects at path.

        This should include subdirectories and files at that location. The
        difference between a file and a directory must be clear when details
        are requested.

        The specific keys, or perhaps a FileInfo class, or similar, is TBD,
        but must be consistent across implementations.
        Must include:

        - full path to the entry (without protocol)
        - size of the entry, in bytes. If the value cannot be determined, will
          be ``None``.
        - type of entry, "file", "directory" or other

        Additional information
        may be present, appropriate to the file-system, e.g., generation,
        checksum, etc.

        May use refresh=True|False to allow use of self._ls_from_cache to
        check for a saved listing and avoid calling the backend. This would be
        common where listing may be expensive.

        Parameters
        ----------
        path: str
        detail: bool
            if True, gives a list of dictionaries, where each is the same as
            the result of ``info(path)``. If False, gives a list of paths
            (str).
        kwargs: may have additional backend-specific options, such as version
            information

        Returns
        -------
        List of strings if detail is False, or list of directory information
        dicts if detail is True.
        '''
    def walk(self, path, maxdepth: Incomplete | None = None, topdown: bool = True, on_error: str = 'omit', **kwargs) -> Generator[Incomplete, Incomplete, Incomplete]:
        '''Return all files belows path

        List all files, recursing into subdirectories; output is iterator-style,
        like ``os.walk()``. For a simple list of files, ``find()`` is available.

        When topdown is True, the caller can modify the dirnames list in-place (perhaps
        using del or slice assignment), and walk() will
        only recurse into the subdirectories whose names remain in dirnames;
        this can be used to prune the search, impose a specific order of visiting,
        or even to inform walk() about directories the caller creates or renames before
        it resumes walk() again.
        Modifying dirnames when topdown is False has no effect. (see os.walk)

        Note that the "files" outputted will include anything that is not
        a directory, such as links.

        Parameters
        ----------
        path: str
            Root to recurse into
        maxdepth: int
            Maximum recursion depth. None means limitless, but not recommended
            on link-based file-systems.
        topdown: bool (True)
            Whether to walk the directory tree from the top downwards or from
            the bottom upwards.
        on_error: "omit", "raise", a collable
            if omit (default), path with exception will simply be empty;
            If raise, an underlying exception will be raised;
            if callable, it will be called with a single OSError instance as argument
        kwargs: passed to ``ls``
        '''
    def find(self, path, maxdepth: Incomplete | None = None, withdirs: bool = False, detail: bool = False, **kwargs):
        """List all files below path.

        Like posix ``find`` command without conditions

        Parameters
        ----------
        path : str
        maxdepth: int or None
            If not None, the maximum number of levels to descend
        withdirs: bool
            Whether to include directory paths in the output. This is True
            when used by glob, but users usually only want files.
        kwargs are passed to ``ls``.
        """
    def du(self, path, total: bool = True, maxdepth: Incomplete | None = None, withdirs: bool = False, **kwargs):
        """Space used by files and optionally directories within a path

        Directory size does not include the size of its contents.

        Parameters
        ----------
        path: str
        total: bool
            Whether to sum all the file sizes
        maxdepth: int or None
            Maximum number of directory levels to descend, None for unlimited.
        withdirs: bool
            Whether to include directory paths in the output.
        kwargs: passed to ``find``

        Returns
        -------
        Dict of {path: size} if total=False, or int otherwise, where numbers
        refer to bytes used.
        """
    def glob(self, path, maxdepth: Incomplete | None = None, **kwargs):
        '''
        Find files by glob-matching.

        If the path ends with \'/\', only folders are returned.

        We support ``"**"``,
        ``"?"`` and ``"[..]"``. We do not support ^ for pattern negation.

        The `maxdepth` option is applied on the first `**` found in the path.

        Search path names that contain embedded characters special to this
        implementation of glob may not produce expected results;
        e.g., ``foo/bar/*starredfilename*``.

        kwargs are passed to ``ls``.
        '''
    def exists(self, path, **kwargs):
        """Is there a file at the given path"""
    def lexists(self, path, **kwargs):
        """If there is a file at the given path (including
        broken links)"""
    def info(self, path, **kwargs):
        """Give details of entry at path

        Returns a single dictionary, with exactly the same information as ``ls``
        would with ``detail=True``.

        The default implementation should calls ls and could be overridden by a
        shortcut. kwargs are passed on to ```ls()``.

        Some file systems might not be able to measure the file's size, in
        which case, the returned dict will include ``'size': None``.

        Returns
        -------
        dict with keys: name (full path in the FS), size (in bytes), type (file,
        directory, or something else) and other FS-specific keys.
        """
    def checksum(self, path):
        """Unique value for current version of file

        If the checksum is the same from one moment to another, the contents
        are guaranteed to be the same. If the checksum changes, the contents
        *might* have changed.

        This should normally be overridden; default will probably capture
        creation/modification timestamp (which would be good) or maybe
        access timestamp (which would be bad)
        """
    def size(self, path):
        """Size in bytes of file"""
    def sizes(self, paths):
        """Size in bytes of each file in a list of paths"""
    def isdir(self, path):
        """Is this entry directory-like?"""
    def isfile(self, path):
        """Is this entry file-like?"""
    def read_text(self, path, encoding: Incomplete | None = None, errors: Incomplete | None = None, newline: Incomplete | None = None, **kwargs):
        """Get the contents of the file as a string.

        Parameters
        ----------
        path: str
            URL of file on this filesystems
        encoding, errors, newline: same as `open`.
        """
    def write_text(self, path, value, encoding: Incomplete | None = None, errors: Incomplete | None = None, newline: Incomplete | None = None, **kwargs):
        """Write the text to the given file.

        An existing file will be overwritten.

        Parameters
        ----------
        path: str
            URL of file on this filesystems
        value: str
            Text to write.
        encoding, errors, newline: same as `open`.
        """
    def cat_file(self, path, start: Incomplete | None = None, end: Incomplete | None = None, **kwargs):
        """Get the content of a file

        Parameters
        ----------
        path: URL of file on this filesystems
        start, end: int
            Bytes limits of the read. If negative, backwards from end,
            like usual python slices. Either can be None for start or
            end of file, respectively
        kwargs: passed to ``open()``.
        """
    def pipe_file(self, path, value, **kwargs) -> None:
        """Set the bytes of given file"""
    def pipe(self, path, value: Incomplete | None = None, **kwargs) -> None:
        """Put value into path

        (counterpart to ``cat``)

        Parameters
        ----------
        path: string or dict(str, bytes)
            If a string, a single remote location to put ``value`` bytes; if a dict,
            a mapping of {path: bytesvalue}.
        value: bytes, optional
            If using a single path, these are the bytes to put there. Ignored if
            ``path`` is a dict
        """
    def cat_ranges(self, paths, starts, ends, max_gap: Incomplete | None = None, on_error: str = 'return', **kwargs): ...
    def cat(self, path, recursive: bool = False, on_error: str = 'raise', **kwargs):
        '''Fetch (potentially multiple) paths\' contents

        Parameters
        ----------
        recursive: bool
            If True, assume the path(s) are directories, and get all the
            contained files
        on_error : "raise", "omit", "return"
            If raise, an underlying exception will be raised (converted to KeyError
            if the type is in self.missing_exceptions); if omit, keys with exception
            will simply not be included in the output; if "return", all keys are
            included in the output, but the value will be bytes or an exception
            instance.
        kwargs: passed to cat_file

        Returns
        -------
        dict of {path: contents} if there are multiple paths
        or the path has been otherwise expanded
        '''
    def get_file(self, rpath, lpath, callback=..., outfile: Incomplete | None = None, **kwargs) -> None:
        """Copy single remote file to local"""
    def get(self, rpath, lpath, recursive: bool = False, callback=..., maxdepth: Incomplete | None = None, **kwargs) -> None:
        '''Copy file(s) to local.

        Copies a specific file or tree of files (if recursive=True). If lpath
        ends with a "/", it will be assumed to be a directory, and target files
        will go within. Can submit a list of paths, which may be glob-patterns
        and will be expanded.

        Calls get_file for each source.
        '''
    def put_file(self, lpath, rpath, callback=..., **kwargs) -> None:
        """Copy single file to remote"""
    def put(self, lpath, rpath, recursive: bool = False, callback=..., maxdepth: Incomplete | None = None, **kwargs) -> None:
        '''Copy file(s) from local.

        Copies a specific file or tree of files (if recursive=True). If rpath
        ends with a "/", it will be assumed to be a directory, and target files
        will go within.

        Calls put_file for each source.
        '''
    def head(self, path, size: int = 1024):
        """Get the first ``size`` bytes from file"""
    def tail(self, path, size: int = 1024):
        """Get the last ``size`` bytes from file"""
    def cp_file(self, path1, path2, **kwargs) -> None: ...
    def copy(self, path1, path2, recursive: bool = False, maxdepth: Incomplete | None = None, on_error: Incomplete | None = None, **kwargs) -> None:
        '''Copy within two locations in the filesystem

        on_error : "raise", "ignore"
            If raise, any not-found exceptions will be raised; if ignore any
            not-found exceptions will cause the path to be skipped; defaults to
            raise unless recursive is true, where the default is ignore
        '''
    def expand_path(self, path, recursive: bool = False, maxdepth: Incomplete | None = None, **kwargs):
        """Turn one or more globs or directories into a list of all matching paths
        to files or directories.

        kwargs are passed to ``glob`` or ``find``, which may in turn call ``ls``
        """
    def mv(self, path1, path2, recursive: bool = False, maxdepth: Incomplete | None = None, **kwargs) -> None:
        """Move file(s) from one location to another"""
    def rm_file(self, path) -> None:
        """Delete a file"""
    def rm(self, path, recursive: bool = False, maxdepth: Incomplete | None = None) -> None:
        """Delete files.

        Parameters
        ----------
        path: str or list of str
            File(s) to delete.
        recursive: bool
            If file(s) are directories, recursively delete contents and then
            also remove the directory
        maxdepth: int or None
            Depth to pass to walk for finding files to delete, if recursive.
            If None, there will be no limit and infinite recursion may be
            possible.
        """
    def open(self, path, mode: str = 'rb', block_size: Incomplete | None = None, cache_options: Incomplete | None = None, compression: Incomplete | None = None, **kwargs):
        '''
        Return a file-like object from the filesystem

        The resultant instance must function correctly in a context ``with``
        block.

        Parameters
        ----------
        path: str
            Target file
        mode: str like \'rb\', \'w\'
            See builtin ``open()``
        block_size: int
            Some indication of buffering - this is a value in bytes
        cache_options : dict, optional
            Extra arguments to pass through to the cache.
        compression: string or None
            If given, open file using compression codec. Can either be a compression
            name (a key in ``fsspec.compression.compr``) or "infer" to guess the
            compression from the filename suffix.
        encoding, errors, newline: passed on to TextIOWrapper for text mode
        '''
    def touch(self, path, truncate: bool = True, **kwargs) -> None:
        """Create empty file, or update timestamp

        Parameters
        ----------
        path: str
            file location
        truncate: bool
            If True, always set file size to 0; if False, update timestamp and
            leave file unchanged, if backend allows this
        """
    def ukey(self, path):
        """Hash of file properties, to tell if it has changed"""
    def read_block(self, fn, offset, length, delimiter: Incomplete | None = None):
        """Read a block of bytes from

        Starting at ``offset`` of the file, read ``length`` bytes.  If
        ``delimiter`` is set then we ensure that the read starts and stops at
        delimiter boundaries that follow the locations ``offset`` and ``offset
        + length``.  If ``offset`` is zero then we start at zero.  The
        bytestring returned WILL include the end delimiter string.

        If offset+length is beyond the eof, reads to eof.

        Parameters
        ----------
        fn: string
            Path to filename
        offset: int
            Byte offset to start read
        length: int
            Number of bytes to read. If None, read to end.
        delimiter: bytes (optional)
            Ensure reading starts and stops at delimiter bytestring

        Examples
        --------
        >>> fs.read_block('data/file.csv', 0, 13)  # doctest: +SKIP
        b'Alice, 100\\nBo'
        >>> fs.read_block('data/file.csv', 0, 13, delimiter=b'\\n')  # doctest: +SKIP
        b'Alice, 100\\nBob, 200\\n'

        Use ``length=None`` to read to the end of the file.
        >>> fs.read_block('data/file.csv', 0, None, delimiter=b'\\n')  # doctest: +SKIP
        b'Alice, 100\\nBob, 200\\nCharlie, 300'

        See Also
        --------
        :func:`fsspec.utils.read_block`
        """
    def to_json(self):
        """
        JSON representation of this filesystem instance

        Returns
        -------
        str: JSON structure with keys cls (the python location of this class),
            protocol (text name of this class's protocol, first one in case of
            multiple), args (positional args, usually empty), and all other
            kwargs as their own keys.
        """
    @staticmethod
    def from_json(blob):
        """
        Recreate a filesystem instance from JSON representation

        See ``.to_json()`` for the expected structure of the input

        Parameters
        ----------
        blob: str

        Returns
        -------
        file system instance, not necessarily of this particular class.
        """
    def get_mapper(self, root: str = '', check: bool = False, create: bool = False, missing_exceptions: Incomplete | None = None):
        """Create key/value store based on this file-system

        Makes a MutableMapping interface to the FS at the given root path.
        See ``fsspec.mapping.FSMap`` for further details.
        """
    @classmethod
    def clear_instance_cache(cls) -> None:
        """
        Clear the cache of filesystem instances.

        Notes
        -----
        Unless overridden by setting the ``cachable`` class attribute to False,
        the filesystem class stores a reference to newly created instances. This
        prevents Python's normal rules around garbage collection from working,
        since the instances refcount will not drop to zero until
        ``clear_instance_cache`` is called.
        """
    def created(self, path) -> None:
        """Return the created timestamp of a file as a datetime.datetime"""
    def modified(self, path) -> None:
        """Return the modified timestamp of a file as a datetime.datetime"""
    def read_bytes(self, path, start: Incomplete | None = None, end: Incomplete | None = None, **kwargs):
        """Alias of `AbstractFileSystem.cat_file`."""
    def write_bytes(self, path, value, **kwargs) -> None:
        """Alias of `AbstractFileSystem.pipe_file`."""
    def makedir(self, path, create_parents: bool = True, **kwargs):
        """Alias of `AbstractFileSystem.mkdir`."""
    def mkdirs(self, path, exist_ok: bool = False):
        """Alias of `AbstractFileSystem.makedirs`."""
    def listdir(self, path, detail: bool = True, **kwargs):
        """Alias of `AbstractFileSystem.ls`."""
    def cp(self, path1, path2, **kwargs):
        """Alias of `AbstractFileSystem.copy`."""
    def move(self, path1, path2, **kwargs):
        """Alias of `AbstractFileSystem.mv`."""
    def stat(self, path, **kwargs):
        """Alias of `AbstractFileSystem.info`."""
    def disk_usage(self, path, total: bool = True, maxdepth: Incomplete | None = None, **kwargs):
        """Alias of `AbstractFileSystem.du`."""
    def rename(self, path1, path2, **kwargs):
        """Alias of `AbstractFileSystem.mv`."""
    def delete(self, path, recursive: bool = False, maxdepth: Incomplete | None = None):
        """Alias of `AbstractFileSystem.rm`."""
    def upload(self, lpath, rpath, recursive: bool = False, **kwargs):
        """Alias of `AbstractFileSystem.put`."""
    def download(self, rpath, lpath, recursive: bool = False, **kwargs):
        """Alias of `AbstractFileSystem.get`."""
    def sign(self, path, expiration: int = 100, **kwargs) -> None:
        """Create a signed URL representing the given path

        Some implementations allow temporary URLs to be generated, as a
        way of delegating credentials.

        Parameters
        ----------
        path : str
             The path on the filesystem
        expiration : int
            Number of seconds to enable the URL for (if supported)

        Returns
        -------
        URL : str
            The signed URL

        Raises
        ------
        NotImplementedError : if method is not implemented for a filesystem
        """

class AbstractBufferedFile(io.IOBase):
    """Convenient class to derive from to provide buffering

    In the case that the backend does not provide a pythonic file-like object
    already, this class contains much of the logic to build one. The only
    methods that need to be overridden are ``_upload_chunk``,
    ``_initiate_upload`` and ``_fetch_range``.
    """
    DEFAULT_BLOCK_SIZE: Incomplete
    path: Incomplete
    fs: Incomplete
    mode: Incomplete
    blocksize: Incomplete
    loc: int
    autocommit: Incomplete
    end: Incomplete
    start: Incomplete
    kwargs: Incomplete
    size: Incomplete
    cache: Incomplete
    buffer: Incomplete
    offset: Incomplete
    forced: bool
    location: Incomplete
    def __init__(self, fs, path, mode: str = 'rb', block_size: str = 'default', autocommit: bool = True, cache_type: str = 'readahead', cache_options: Incomplete | None = None, size: Incomplete | None = None, **kwargs) -> None:
        '''
        Template for files with buffered reading and writing

        Parameters
        ----------
        fs: instance of FileSystem
        path: str
            location in file-system
        mode: str
            Normal file modes. Currently only \'wb\', \'ab\' or \'rb\'. Some file
            systems may be read-only, and some may not support append.
        block_size: int
            Buffer size for reading or writing, \'default\' for class default
        autocommit: bool
            Whether to write to final destination; may only impact what
            happens when file is being closed.
        cache_type: {"readahead", "none", "mmap", "bytes"}, default "readahead"
            Caching policy in read mode. See the definitions in ``core``.
        cache_options : dict
            Additional options passed to the constructor for the cache specified
            by `cache_type`.
        size: int
            If given and in read mode, suppressed having to look up the file size
        kwargs:
            Gets stored as self.kwargs
        '''
    @property
    def details(self): ...
    @details.setter
    def details(self, value) -> None: ...
    @property
    def full_name(self): ...
    @property
    def closed(self): ...
    @closed.setter
    def closed(self, c) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other):
        """Files are equal if they have the same checksum, only in read mode"""
    def commit(self) -> None:
        """Move from temp to final destination"""
    def discard(self) -> None:
        """Throw away temporary file"""
    def info(self):
        """File information about this path"""
    def tell(self):
        """Current file location"""
    def seek(self, loc, whence: int = 0):
        """Set current file location

        Parameters
        ----------
        loc: int
            byte location
        whence: {0, 1, 2}
            from start of file, current location or end of file, resp.
        """
    def write(self, data):
        """
        Write data to buffer.

        Buffer only sent on flush() or if buffer is greater than
        or equal to blocksize.

        Parameters
        ----------
        data: bytes
            Set of bytes to be written.
        """
    def flush(self, force: bool = False) -> None:
        """
        Write buffered data to backend store.

        Writes the current buffer, if it is larger than the block-size, or if
        the file is being closed.

        Parameters
        ----------
        force: bool
            When closing, write the last block even if it is smaller than
            blocks are allowed to be. Disallows further writing to this file.
        """
    def read(self, length: int = -1):
        """
        Return data from cache, or fetch pieces as necessary

        Parameters
        ----------
        length: int (-1)
            Number of bytes to read; if <0, all remaining bytes.
        """
    def readinto(self, b):
        """mirrors builtin file's readinto method

        https://docs.python.org/3/library/io.html#io.RawIOBase.readinto
        """
    def readuntil(self, char: bytes = b'\n', blocks: Incomplete | None = None):
        """Return data between current position and first occurrence of char

        char is included in the output, except if the end of the tile is
        encountered first.

        Parameters
        ----------
        char: bytes
            Thing to find
        blocks: None or int
            How much to read in each go. Defaults to file blocksize - which may
            mean a new read on every call.
        """
    def readline(self):
        """Read until first occurrence of newline character

        Note that, because of character encoding, this is not necessarily a
        true line ending.
        """
    def __next__(self): ...
    def __iter__(self): ...
    def readlines(self):
        """Return all data, split by the newline character"""
    def readinto1(self, b): ...
    def close(self) -> None:
        """Close file

        Finalizes writes, discards cache
        """
    def readable(self):
        """Whether opened for reading"""
    def seekable(self):
        """Whether is seekable (only in read mode)"""
    def writable(self):
        """Whether opened for writing"""
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
