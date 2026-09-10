import zipfile
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from gzip import GzipFile

__all__ = ['path', 'PathPointer', 'FileSystemPathPointer', 'BufferedGzipFile', 'GzipFileSystemPathPointer', 'GzipFileSystemPathPointer', 'find', 'retrieve', 'FORMATS', 'AUTO_FORMATS', 'load', 'show_cfg', 'clear_cache', 'LazyLoader', 'OpenOnDemandZipFile', 'GzipFileSystemPathPointer', 'SeekableUnicodeStreamReader']

path: Incomplete

class PathPointer(metaclass=ABCMeta):
    """
    An abstract base class for 'path pointers,' used by NLTK's data
    package to identify specific paths.  Two subclasses exist:
    ``FileSystemPathPointer`` identifies a file that can be accessed
    directly via a given absolute path.  ``ZipFilePathPointer``
    identifies a file contained within a zipfile, that can be accessed
    by reading that zipfile.
    """
    @abstractmethod
    def open(self, encoding: Incomplete | None = None):
        """
        Return a seekable read-only stream that can be used to read
        the contents of the file identified by this path pointer.

        :raise IOError: If the path specified by this pointer does
            not contain a readable file.
        """
    @abstractmethod
    def file_size(self):
        """
        Return the size of the file pointed to by this path pointer,
        in bytes.

        :raise IOError: If the path specified by this pointer does
            not contain a readable file.
        """
    @abstractmethod
    def join(self, fileid):
        """
        Return a new path pointer formed by starting at the path
        identified by this pointer, and then following the relative
        path given by ``fileid``.  The path components of ``fileid``
        should be separated by forward slashes, regardless of
        the underlying file system's path separator character.
        """

class FileSystemPathPointer(PathPointer, str):
    """
    A path pointer that identifies a file which can be accessed
    directly via a given absolute path.
    """
    def __init__(self, _path) -> None:
        """
        Create a new path pointer for the given absolute path.

        :raise IOError: If the given path does not exist.
        """
    @property
    def path(self):
        """The absolute path identified by this path pointer."""
    def open(self, encoding: Incomplete | None = None): ...
    def file_size(self): ...
    def join(self, fileid): ...

class BufferedGzipFile(GzipFile):
    """A ``GzipFile`` subclass for compatibility with older nltk releases.

    Use ``GzipFile`` directly as it also buffers in all supported
    Python versions.
    """
    def __init__(self, filename: Incomplete | None = None, mode: Incomplete | None = None, compresslevel: int = 9, fileobj: Incomplete | None = None, **kwargs) -> None:
        """Return a buffered gzip file object."""
    def write(self, data) -> None: ...

class GzipFileSystemPathPointer(FileSystemPathPointer):
    """
    A subclass of ``FileSystemPathPointer`` that identifies a gzip-compressed
    file located at a given absolute path.  ``GzipFileSystemPathPointer`` is
    appropriate for loading large gzip-compressed pickle objects efficiently.
    """
    def open(self, encoding: Incomplete | None = None): ...

class ZipFilePathPointer(PathPointer):
    """
    A path pointer that identifies a file contained within a zipfile,
    which can be accessed by reading that zipfile.
    """
    def __init__(self, zipfile, entry: str = '') -> None:
        """
        Create a new path pointer pointing at the specified entry
        in the given zipfile.

        :raise IOError: If the given zipfile does not exist, or if it
        does not contain the specified entry.
        """
    @property
    def zipfile(self):
        """
        The zipfile.ZipFile object used to access the zip file
        containing the entry identified by this path pointer.
        """
    @property
    def entry(self):
        """
        The name of the file within zipfile that this path
        pointer points to.
        """
    def open(self, encoding: Incomplete | None = None): ...
    def file_size(self): ...
    def join(self, fileid): ...

def find(resource_name, paths: Incomplete | None = None):
    """
    Find the given resource by searching through the directories and
    zip files in paths, where a None or empty string specifies an absolute path.
    Returns a corresponding path name.  If the given resource is not
    found, raise a ``LookupError``, whose message gives a pointer to
    the installation instructions for the NLTK downloader.

    Zip File Handling:

      - If ``resource_name`` contains a component with a ``.zip``
        extension, then it is assumed to be a zipfile; and the
        remaining path components are used to look inside the zipfile.

      - If any element of ``nltk.data.path`` has a ``.zip`` extension,
        then it is assumed to be a zipfile.

      - If a given resource name that does not contain any zipfile
        component is not found initially, then ``find()`` will make a
        second attempt to find that resource, by replacing each
        component *p* in the path with *p.zip/p*.  For example, this
        allows ``find()`` to map the resource name
        ``corpora/chat80/cities.pl`` to a zip file path pointer to
        ``corpora/chat80.zip/chat80/cities.pl``.

      - When using ``find()`` to locate a directory contained in a
        zipfile, the resource name must end with the forward slash
        character.  Otherwise, ``find()`` will not locate the
        directory.

    :type resource_name: str or unicode
    :param resource_name: The name of the resource to search for.
        Resource names are posix-style relative path names, such as
        ``corpora/brown``.  Directory names will be
        automatically converted to a platform-appropriate path separator.
    :rtype: str
    """
def retrieve(resource_url, filename: Incomplete | None = None, verbose: bool = True) -> None:
    '''
    Copy the given resource to a local file.  If no filename is
    specified, then use the URL\'s filename.  If there is already a
    file named ``filename``, then raise a ``ValueError``.

    :type resource_url: str
    :param resource_url: A URL specifying where the resource should be
        loaded from.  The default protocol is "nltk:", which searches
        for the file in the the NLTK data package.
    '''

FORMATS: Incomplete
AUTO_FORMATS: Incomplete

def load(resource_url, format: str = 'auto', cache: bool = True, verbose: bool = False, logic_parser: Incomplete | None = None, fstruct_reader: Incomplete | None = None, encoding: Incomplete | None = None):
    '''
    Load a given resource from the NLTK data package.  The following
    resource formats are currently supported:

      - ``pickle``
      - ``json``
      - ``yaml``
      - ``cfg`` (context free grammars)
      - ``pcfg`` (probabilistic CFGs)
      - ``fcfg`` (feature-based CFGs)
      - ``fol`` (formulas of First Order Logic)
      - ``logic`` (Logical formulas to be parsed by the given logic_parser)
      - ``val`` (valuation of First Order Logic model)
      - ``text`` (the file contents as a unicode string)
      - ``raw`` (the raw file contents as a byte string)

    If no format is specified, ``load()`` will attempt to determine a
    format based on the resource name\'s file extension.  If that
    fails, ``load()`` will raise a ``ValueError`` exception.

    For all text formats (everything except ``pickle``, ``json``, ``yaml`` and ``raw``),
    it tries to decode the raw contents using UTF-8, and if that doesn\'t
    work, it tries with ISO-8859-1 (Latin-1), unless the ``encoding``
    is specified.

    :type resource_url: str
    :param resource_url: A URL specifying where the resource should be
        loaded from.  The default protocol is "nltk:", which searches
        for the file in the the NLTK data package.
    :type cache: bool
    :param cache: If true, add this resource to a cache.  If load()
        finds a resource in its cache, then it will return it from the
        cache rather than loading it.
    :type verbose: bool
    :param verbose: If true, print a message when loading a resource.
        Messages are not displayed when a resource is retrieved from
        the cache.
    :type logic_parser: LogicParser
    :param logic_parser: The parser that will be used to parse logical
        expressions.
    :type fstruct_reader: FeatStructReader
    :param fstruct_reader: The parser that will be used to parse the
        feature structure of an fcfg.
    :type encoding: str
    :param encoding: the encoding of the input; only used for text formats.
    '''
def show_cfg(resource_url, escape: str = '##') -> None:
    '''
    Write out a grammar file, ignoring escaped and empty lines.

    :type resource_url: str
    :param resource_url: A URL specifying where the resource should be
        loaded from.  The default protocol is "nltk:", which searches
        for the file in the the NLTK data package.
    :type escape: str
    :param escape: Prepended string that signals lines to be ignored
    '''
def clear_cache() -> None:
    """
    Remove all objects from the resource cache.
    :see: load()
    """

class LazyLoader:
    def __init__(self, _path) -> None: ...
    def __getattr__(self, attr): ...

class OpenOnDemandZipFile(zipfile.ZipFile):
    """
    A subclass of ``zipfile.ZipFile`` that closes its file pointer
    whenever it is not using it; and re-opens it when it needs to read
    data from the zipfile.  This is useful for reducing the number of
    open file handles when many zip files are being accessed at once.
    ``OpenOnDemandZipFile`` must be constructed from a filename, not a
    file-like object (to allow re-opening).  ``OpenOnDemandZipFile`` is
    read-only (i.e. ``write()`` and ``writestr()`` are disabled.
    """
    def __init__(self, filename) -> None: ...
    fp: Incomplete
    def read(self, name): ...
    def write(self, *args, **kwargs) -> None:
        """:raise NotImplementedError: OpenOnDemandZipfile is read-only"""
    def writestr(self, *args, **kwargs) -> None:
        """:raise NotImplementedError: OpenOnDemandZipfile is read-only"""

class SeekableUnicodeStreamReader:
    """
    A stream reader that automatically encodes the source byte stream
    into unicode (like ``codecs.StreamReader``); but still supports the
    ``seek()`` and ``tell()`` operations correctly.  This is in contrast
    to ``codecs.StreamReader``, which provide *broken* ``seek()`` and
    ``tell()`` methods.

    This class was motivated by ``StreamBackedCorpusView``, which
    makes extensive use of ``seek()`` and ``tell()``, and needs to be
    able to handle unicode-encoded files.

    Note: this class requires stateless decoders.  To my knowledge,
    this shouldn't cause a problem with any of python's builtin
    unicode encodings.
    """
    DEBUG: bool
    stream: Incomplete
    encoding: Incomplete
    errors: Incomplete
    decode: Incomplete
    bytebuffer: bytes
    linebuffer: Incomplete
    def __init__(self, stream, encoding, errors: str = 'strict') -> None: ...
    def read(self, size: Incomplete | None = None):
        """
        Read up to ``size`` bytes, decode them using this reader's
        encoding, and return the resulting unicode string.

        :param size: The maximum number of bytes to read.  If not
            specified, then read as many bytes as possible.
        :type size: int
        :rtype: unicode
        """
    def discard_line(self) -> None: ...
    def readline(self, size: Incomplete | None = None):
        """
        Read a line of text, decode it using this reader's encoding,
        and return the resulting unicode string.

        :param size: The maximum number of bytes to read.  If no
            newline is encountered before ``size`` bytes have been read,
            then the returned value may not be a complete line of text.
        :type size: int
        """
    def readlines(self, sizehint: Incomplete | None = None, keepends: bool = True):
        """
        Read this file's contents, decode them using this reader's
        encoding, and return it as a list of unicode lines.

        :rtype: list(unicode)
        :param sizehint: Ignored.
        :param keepends: If false, then strip newlines.
        """
    def next(self):
        """Return the next decoded line from the underlying stream."""
    def __next__(self): ...
    def __iter__(self):
        """Return self"""
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def xreadlines(self):
        """Return self"""
    @property
    def closed(self):
        """True if the underlying stream is closed."""
    @property
    def name(self):
        """The name of the underlying stream."""
    @property
    def mode(self):
        """The mode of the underlying stream."""
    def close(self) -> None:
        """
        Close the underlying stream.
        """
    def seek(self, offset, whence: int = 0) -> None:
        """
        Move the stream to a new file position.  If the reader is
        maintaining any buffers, then they will be cleared.

        :param offset: A byte count offset.
        :param whence: If 0, then the offset is from the start of the file
            (offset should be positive), if 1, then the offset is from the
            current position (offset may be positive or negative); and if 2,
            then the offset is from the end of the file (offset should
            typically be negative).
        """
    def char_seek_forward(self, offset) -> None:
        """
        Move the read pointer forward by ``offset`` characters.
        """
    def tell(self):
        """
        Return the current file position on the underlying byte
        stream.  If this reader is maintaining any buffers, then the
        returned file position will be the position of the beginning
        of those buffers.
        """
