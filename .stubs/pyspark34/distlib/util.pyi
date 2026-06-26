from . import DistlibException as DistlibException
from .compat import BaseConfigurator as BaseConfigurator, CertificateError as CertificateError, Container as Container, HTTPHandler as HTTPHandler, HTTPSHandler as BaseHTTPSHandler, StringIO as StringIO, URLError as URLError, ZipFile as ZipFile, cache_from_source as cache_from_source, configparser as configparser, fsdecode as fsdecode, httplib as httplib, match_hostname as match_hostname, raw_input as raw_input, shutil as shutil, splittype as splittype, string_types as string_types, text_type as text_type, unquote as unquote, urljoin as urljoin, urlopen as urlopen, urlparse as urlparse, valid_ident as valid_ident, xmlrpclib as xmlrpclib
from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete
IDENTIFIER: Incomplete
VERSION_IDENTIFIER: Incomplete
COMPARE_OP: Incomplete
MARKER_OP: Incomplete
OR: Incomplete
AND: Incomplete
NON_SPACE: Incomplete
STRING_CHUNK: Incomplete

def parse_marker(marker_string):
    '''
    Parse a marker string and return a dictionary containing a marker expression.

    The dictionary will contain keys "op", "lhs" and "rhs" for non-terminals in
    the expression grammar, or strings. A string contained in quotes is to be
    interpreted as a literal string, and a string not contained in quotes is a
    variable (such as os_name).
    '''
def parse_requirement(req):
    """
    Parse a requirement passed in as a string. Return a Container
    whose attributes contain the various parts of the requirement.
    """
def get_resources_dests(resources_root, rules):
    """Find destinations for resources files"""
def in_venv(): ...
def get_executable(): ...
def proceed(prompt, allowed_chars, error_prompt: Incomplete | None = None, default: Incomplete | None = None): ...
def extract_by_key(d, keys): ...
def read_exports(stream): ...
def write_exports(exports, stream) -> None: ...
def tempdir() -> Generator[Incomplete, None, None]: ...
def chdir(d) -> Generator[None, None, None]: ...
def socket_timeout(seconds: int = 15) -> Generator[None, None, None]: ...

class cached_property:
    func: Incomplete
    def __init__(self, func) -> None: ...
    def __get__(self, obj, cls: Incomplete | None = None): ...

def convert_path(pathname):
    """Return 'pathname' as a name that will work on the native filesystem.

    The path is split on '/' and put back together again using the current
    directory separator.  Needed because filenames in the setup script are
    always supplied in Unix style, and have to be converted to the local
    convention before we can actually use them in the filesystem.  Raises
    ValueError on non-Unix-ish systems if 'pathname' either starts or
    ends with a slash.
    """

class FileOperator:
    dry_run: Incomplete
    ensured: Incomplete
    def __init__(self, dry_run: bool = False) -> None: ...
    def record_as_written(self, path) -> None: ...
    def newer(self, source, target):
        '''Tell if the target is newer than the source.

        Returns true if \'source\' exists and is more recently modified than
        \'target\', or if \'source\' exists and \'target\' doesn\'t.

        Returns false if both exist and \'target\' is the same age or younger
        than \'source\'. Raise PackagingFileError if \'source\' does not exist.

        Note that this test is not very accurate: files created in the same
        second will have the same "age".
        '''
    def copy_file(self, infile, outfile, check: bool = True) -> None:
        """Copy a file respecting dry-run and force flags.
        """
    def copy_stream(self, instream, outfile, encoding: Incomplete | None = None) -> None: ...
    def write_binary_file(self, path, data) -> None: ...
    def write_text_file(self, path, data, encoding) -> None: ...
    def set_mode(self, bits, mask, files) -> None: ...
    set_executable_mode: Incomplete
    def ensure_dir(self, path) -> None: ...
    def byte_compile(self, path, optimize: bool = False, force: bool = False, prefix: Incomplete | None = None, hashed_invalidation: bool = False): ...
    def ensure_removed(self, path) -> None: ...
    def is_writable(self, path): ...
    def commit(self):
        """
        Commit recorded changes, turn off recording, return
        changes.
        """
    def rollback(self) -> None: ...

def resolve(module_name, dotted_path): ...

class ExportEntry:
    name: Incomplete
    prefix: Incomplete
    suffix: Incomplete
    flags: Incomplete
    def __init__(self, name, prefix, suffix, flags) -> None: ...
    def value(self): ...
    def __eq__(self, other): ...
    __hash__: Incomplete

ENTRY_RE: Incomplete

def get_export_entry(specification): ...
def get_cache_base(suffix: Incomplete | None = None):
    """
    Return the default base location for distlib caches. If the directory does
    not exist, it is created. Use the suffix provided for the base directory,
    and default to '.distlib' if it isn't provided.

    On Windows, if LOCALAPPDATA is defined in the environment, then it is
    assumed to be a directory, and will be the parent directory of the result.
    On POSIX, and on Windows if LOCALAPPDATA is not defined, the user's home
    directory - using os.expanduser('~') - will be the parent directory of
    the result.

    The result is just the directory '.distlib' in the parent directory as
    determined above, or with the name specified with ``suffix``.
    """
def path_to_cache_dir(path):
    """
    Convert an absolute path to a directory name for use in a cache.

    The algorithm used is:

    #. On Windows, any ``':'`` in the drive is replaced with ``'---'``.
    #. Any occurrence of ``os.sep`` is replaced with ``'--'``.
    #. ``'.cache'`` is appended.
    """
def ensure_slash(s): ...
def parse_credentials(netloc): ...
def get_process_umask(): ...
def is_string_sequence(seq): ...

PROJECT_NAME_AND_VERSION: Incomplete
PYTHON_VERSION: Incomplete

def split_filename(filename, project_name: Incomplete | None = None):
    """
    Extract name, version, python version from a filename (no extension)

    Return name, version, pyver or None
    """

NAME_VERSION_RE: Incomplete

def parse_name_and_version(p):
    """
    A utility method used to get name and version from a string.

    From e.g. a Provides-Dist value.

    :param p: A value in a form 'foo (1.0)'
    :return: The name and version as a tuple.
    """
def get_extras(requested, available): ...
def get_project_data(name): ...
def get_package_data(name, version): ...

class Cache:
    """
    A class implementing a cache for resources that need to live in the file system
    e.g. shared libraries. This class was moved from resources to here because it
    could be used by other modules, e.g. the wheel module.
    """
    base: Incomplete
    def __init__(self, base) -> None:
        """
        Initialise an instance.

        :param base: The base directory where the cache should be located.
        """
    def prefix_to_dir(self, prefix):
        """
        Converts a resource prefix to a directory name in the cache.
        """
    def clear(self):
        """
        Clear the cache.
        """

class EventMixin:
    """
    A very simple publish/subscribe system.
    """
    def __init__(self) -> None: ...
    def add(self, event, subscriber, append: bool = True) -> None:
        """
        Add a subscriber for an event.

        :param event: The name of an event.
        :param subscriber: The subscriber to be added (and called when the
                           event is published).
        :param append: Whether to append or prepend the subscriber to an
                       existing subscriber list for the event.
        """
    def remove(self, event, subscriber) -> None:
        """
        Remove a subscriber for an event.

        :param event: The name of an event.
        :param subscriber: The subscriber to be removed.
        """
    def get_subscribers(self, event):
        """
        Return an iterator for the subscribers for an event.
        :param event: The event to return subscribers for.
        """
    def publish(self, event, *args, **kwargs):
        """
        Publish a event and return a list of values returned by its
        subscribers.

        :param event: The event to publish.
        :param args: The positional arguments to pass to the event's
                     subscribers.
        :param kwargs: The keyword arguments to pass to the event's
                       subscribers.
        """

class Sequencer:
    def __init__(self) -> None: ...
    def add_node(self, node) -> None: ...
    def remove_node(self, node, edges: bool = False) -> None: ...
    def add(self, pred, succ) -> None: ...
    def remove(self, pred, succ) -> None: ...
    def is_step(self, step): ...
    def get_steps(self, final): ...
    @property
    def strong_connections(self): ...
    @property
    def dot(self): ...

ARCHIVE_EXTENSIONS: Incomplete

def unarchive(archive_filename, dest_dir, format: Incomplete | None = None, check: bool = True): ...
def zip_dir(directory):
    """zip a directory tree into a BytesIO object"""

UNITS: Incomplete

class Progress:
    unknown: str
    min: Incomplete
    max: Incomplete
    started: Incomplete
    elapsed: int
    done: bool
    def __init__(self, minval: int = 0, maxval: int = 100) -> None: ...
    cur: Incomplete
    def update(self, curval) -> None: ...
    def increment(self, incr) -> None: ...
    def start(self): ...
    def stop(self) -> None: ...
    @property
    def maximum(self): ...
    @property
    def percentage(self): ...
    def format_duration(self, duration): ...
    @property
    def ETA(self): ...
    @property
    def speed(self): ...

RICH_GLOB: Incomplete

def iglob(path_glob):
    """Extended globbing function that supports ** and {opt1,opt2,opt3}."""

class HTTPSConnection(httplib.HTTPSConnection):
    ca_certs: Incomplete
    check_domain: bool
    sock: Incomplete
    def connect(self) -> None: ...

class HTTPSHandler(BaseHTTPSHandler):
    ca_certs: Incomplete
    check_domain: Incomplete
    def __init__(self, ca_certs, check_domain: bool = True) -> None: ...
    def https_open(self, req): ...

class HTTPSOnlyHandler(HTTPSHandler, HTTPHandler):
    def http_open(self, req) -> None: ...

class Transport(xmlrpclib.Transport):
    timeout: Incomplete
    def __init__(self, timeout, use_datetime: int = 0) -> None: ...
    def make_connection(self, host): ...

class SafeTransport(xmlrpclib.SafeTransport):
    timeout: Incomplete
    def __init__(self, timeout, use_datetime: int = 0) -> None: ...
    def make_connection(self, host): ...

class ServerProxy(xmlrpclib.ServerProxy):
    timeout: Incomplete
    transport: Incomplete
    def __init__(self, uri, **kwargs) -> None: ...

class CSVBase:
    defaults: Incomplete
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...

class CSVReader(CSVBase):
    stream: Incomplete
    reader: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __iter__(self): ...
    def next(self): ...
    __next__ = next

class CSVWriter(CSVBase):
    stream: Incomplete
    writer: Incomplete
    def __init__(self, fn, **kwargs) -> None: ...
    def writerow(self, row) -> None: ...

class Configurator(BaseConfigurator):
    value_converters: Incomplete
    base: Incomplete
    def __init__(self, config, base: Incomplete | None = None) -> None: ...
    def configure_custom(self, config): ...
    def __getitem__(self, key): ...
    def inc_convert(self, value):
        """Default converter for the inc:// protocol."""

class SubprocessMixin:
    """
    Mixin for running subprocesses and capturing their output
    """
    verbose: Incomplete
    progress: Incomplete
    def __init__(self, verbose: bool = False, progress: Incomplete | None = None) -> None: ...
    def reader(self, stream, context) -> None:
        """
        Read lines from a subprocess' output stream and either pass to a progress
        callable (if specified) or write progress information to sys.stderr.
        """
    def run_command(self, cmd, **kwargs): ...

def normalize_name(name):
    """Normalize a python package name a la PEP 503"""

class PyPIRCFile:
    DEFAULT_REPOSITORY: str
    DEFAULT_REALM: str
    filename: Incomplete
    url: Incomplete
    def __init__(self, fn: Incomplete | None = None, url: Incomplete | None = None) -> None: ...
    def read(self): ...
    def update(self, username, password) -> None: ...

def get_host_platform():
    """Return a string that identifies the current platform.  This is used mainly to
    distinguish platform-specific build directories and platform-specific built
    distributions.  Typically includes the OS name and version and the
    architecture (as supplied by 'os.uname()'), although the exact information
    included depends on the OS; eg. on Linux, the kernel version isn't
    particularly important.

    Examples of returned values:
       linux-i586
       linux-alpha (?)
       solaris-2.6-sun4u

    Windows will return one of:
       win-amd64 (64bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
       win32 (all others - specifically, sys.platform is returned)

    For other non-POSIX platforms, currently just returns 'sys.platform'.

    """
def get_platform(): ...
