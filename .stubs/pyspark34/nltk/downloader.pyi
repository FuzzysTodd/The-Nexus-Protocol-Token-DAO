import threading
from _typeshed import Incomplete
from collections.abc import Generator
from nltk.draw.table import Table as Table
from nltk.draw.util import ShowText as ShowText

TKINTER: bool
TclError = ValueError

class Package:
    """
    A directory entry for a downloadable package.  These entries are
    extracted from the XML index file that is downloaded by
    ``Downloader``.  Each package consists of a single file; but if
    that file is a zip file, then it can be automatically decompressed
    when the package is installed.
    """
    id: Incomplete
    name: Incomplete
    subdir: Incomplete
    url: Incomplete
    size: Incomplete
    unzipped_size: Incomplete
    checksum: Incomplete
    svn_revision: Incomplete
    copyright: Incomplete
    contact: Incomplete
    license: Incomplete
    author: Incomplete
    filename: Incomplete
    unzip: Incomplete
    def __init__(self, id, url, name: Incomplete | None = None, subdir: str = '', size: Incomplete | None = None, unzipped_size: Incomplete | None = None, checksum: Incomplete | None = None, svn_revision: Incomplete | None = None, copyright: str = 'Unknown', contact: str = 'Unknown', license: str = 'Unknown', author: str = 'Unknown', unzip: bool = True, **kw) -> None: ...
    @staticmethod
    def fromxml(xml): ...
    def __lt__(self, other): ...

class Collection:
    """
    A directory entry for a collection of downloadable packages.
    These entries are extracted from the XML index file that is
    downloaded by ``Downloader``.
    """
    id: Incomplete
    name: Incomplete
    children: Incomplete
    packages: Incomplete
    def __init__(self, id, children, name: Incomplete | None = None, **kw) -> None: ...
    @staticmethod
    def fromxml(xml): ...
    def __lt__(self, other): ...

class DownloaderMessage:
    """A status message object, used by ``incr_download`` to
    communicate its progress."""

class StartCollectionMessage(DownloaderMessage):
    """Data server has started working on a collection of packages."""
    collection: Incomplete
    def __init__(self, collection) -> None: ...

class FinishCollectionMessage(DownloaderMessage):
    """Data server has finished working on a collection of packages."""
    collection: Incomplete
    def __init__(self, collection) -> None: ...

class StartPackageMessage(DownloaderMessage):
    """Data server has started working on a package."""
    package: Incomplete
    def __init__(self, package) -> None: ...

class FinishPackageMessage(DownloaderMessage):
    """Data server has finished working on a package."""
    package: Incomplete
    def __init__(self, package) -> None: ...

class StartDownloadMessage(DownloaderMessage):
    """Data server has started downloading a package."""
    package: Incomplete
    def __init__(self, package) -> None: ...

class FinishDownloadMessage(DownloaderMessage):
    """Data server has finished downloading a package."""
    package: Incomplete
    def __init__(self, package) -> None: ...

class StartUnzipMessage(DownloaderMessage):
    """Data server has started unzipping a package."""
    package: Incomplete
    def __init__(self, package) -> None: ...

class FinishUnzipMessage(DownloaderMessage):
    """Data server has finished unzipping a package."""
    package: Incomplete
    def __init__(self, package) -> None: ...

class UpToDateMessage(DownloaderMessage):
    """The package download file is already up-to-date"""
    package: Incomplete
    def __init__(self, package) -> None: ...

class StaleMessage(DownloaderMessage):
    """The package download file is out-of-date or corrupt"""
    package: Incomplete
    def __init__(self, package) -> None: ...

class ErrorMessage(DownloaderMessage):
    """Data server encountered an error"""
    package: Incomplete
    message: Incomplete
    def __init__(self, package, message) -> None: ...

class ProgressMessage(DownloaderMessage):
    """Indicates how much progress the data server has made"""
    progress: Incomplete
    def __init__(self, progress) -> None: ...

class SelectDownloadDirMessage(DownloaderMessage):
    """Indicates what download directory the data server is using"""
    download_dir: Incomplete
    def __init__(self, download_dir) -> None: ...

class Downloader:
    """
    A class used to access the NLTK data server, which can be used to
    download corpora and other data packages.
    """
    INDEX_TIMEOUT: Incomplete
    DEFAULT_URL: str
    INSTALLED: str
    NOT_INSTALLED: str
    STALE: str
    PARTIAL: str
    def __init__(self, server_index_url: Incomplete | None = None, download_dir: Incomplete | None = None) -> None: ...
    def list(self, download_dir: Incomplete | None = None, show_packages: bool = True, show_collections: bool = True, header: bool = True, more_prompt: bool = False, skip_installed: bool = False) -> None: ...
    def packages(self): ...
    def corpora(self): ...
    def models(self): ...
    def collections(self): ...
    def incr_download(self, info_or_id, download_dir: Incomplete | None = None, force: bool = False) -> Generator[Incomplete, Incomplete, None]: ...
    def download(self, info_or_id: Incomplete | None = None, download_dir: Incomplete | None = None, quiet: bool = False, force: bool = False, prefix: str = '[nltk_data] ', halt_on_error: bool = True, raise_on_error: bool = False, print_error_to=...): ...
    def is_stale(self, info_or_id, download_dir: Incomplete | None = None): ...
    def is_installed(self, info_or_id, download_dir: Incomplete | None = None): ...
    def clear_status_cache(self, id: Incomplete | None = None) -> None: ...
    def status(self, info_or_id, download_dir: Incomplete | None = None):
        """
        Return a constant describing the status of the given package
        or collection.  Status can be one of ``INSTALLED``,
        ``NOT_INSTALLED``, ``STALE``, or ``PARTIAL``.
        """
    def update(self, quiet: bool = False, prefix: str = '[nltk_data] ') -> None:
        """
        Re-download any packages whose status is STALE.
        """
    def index(self):
        """
        Return the XML index describing the packages available from
        the data server.  If necessary, this index will be downloaded
        from the data server.
        """
    def info(self, id):
        """Return the ``Package`` or ``Collection`` record for the
        given item."""
    def xmlinfo(self, id):
        """Return the XML info record for the given item"""
    url: Incomplete
    def default_download_dir(self):
        """
        Return the directory to which packages will be downloaded by
        default.  This value can be overridden using the constructor,
        or on a case-by-case basis using the ``download_dir`` argument when
        calling ``download()``.

        On Windows, the default download directory is
        ``PYTHONHOME/lib/nltk``, where *PYTHONHOME* is the
        directory containing Python, e.g. ``C:\\Python25``.

        On all other platforms, the default directory is the first of
        the following which exists or which can be created with write
        permission: ``/usr/share/nltk_data``, ``/usr/local/share/nltk_data``,
        ``/usr/lib/nltk_data``, ``/usr/local/lib/nltk_data``, ``~/nltk_data``.
        """
    download_dir: Incomplete

class DownloaderShell:
    def __init__(self, dataserver) -> None: ...
    def run(self) -> None: ...

class DownloaderGUI:
    """
    Graphical interface for downloading packages from the NLTK data
    server.
    """
    COLUMNS: Incomplete
    COLUMN_WEIGHTS: Incomplete
    COLUMN_WIDTHS: Incomplete
    DEFAULT_COLUMN_WIDTH: int
    INITIAL_COLUMNS: Incomplete
    def __init__(self, dataserver, use_threads: bool = True) -> None: ...
    def destroy(self, *e) -> None: ...
    def mainloop(self, *args, **kwargs) -> None: ...
    HELP: Incomplete
    def help(self, *e) -> None: ...
    def about(self, *e) -> None: ...
    class _DownloadThread(threading.Thread):
        data_server: Incomplete
        items: Incomplete
        lock: Incomplete
        message_queue: Incomplete
        abort: Incomplete
        def __init__(self, data_server, items, lock, message_queue, abort) -> None: ...
        def run(self) -> None: ...

def md5_hexdigest(file):
    """
    Calculate and return the MD5 checksum for a given file.
    ``file`` may either be a filename or an open stream.
    """
def unzip(filename, root, verbose: bool = True) -> None:
    """
    Extract the contents of the zip file ``filename`` into the
    directory ``root``.
    """
def build_index(root, base_url):
    """
    Create a new data.xml index file, by combining the xml description
    files for various packages and collections.  ``root`` should be the
    path to a directory containing the package xml and zip files; and
    the collection xml files.  The ``root`` directory is expected to
    have the following subdirectories::

      root/
        packages/ .................. subdirectory for packages
          corpora/ ................. zip & xml files for corpora
          grammars/ ................ zip & xml files for grammars
          taggers/ ................. zip & xml files for taggers
          tokenizers/ .............. zip & xml files for tokenizers
          etc.
        collections/ ............... xml files for collections

    For each package, there should be two files: ``package.zip``
    (where *package* is the package name)
    which contains the package itself as a compressed zip file; and
    ``package.xml``, which is an xml description of the package.  The
    zipfile ``package.zip`` should expand to a single subdirectory
    named ``package/``.  The base filename ``package`` must match
    the identifier given in the package's xml file.

    For each collection, there should be a single file ``collection.zip``
    describing the collection, where *collection* is the name of the collection.

    All identifiers (for both packages and collections) must be unique.
    """

download: Incomplete

def download_shell() -> None: ...
def download_gui() -> None: ...
def update() -> None: ...
