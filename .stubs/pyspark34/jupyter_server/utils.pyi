from _typeshed import Incomplete
from urllib.parse import urljoin as urljoin
from urllib.request import pathname2url as pathname2url

ApiPath: Incomplete

def url_path_join(*pieces):
    """Join components of url into a relative url

    Use to prevent double slash when joining subpath. This will leave the
    initial and final / in place
    """
def url_is_absolute(url):
    """Determine whether a given URL is absolute"""
def path2url(path):
    """Convert a local file path to a URL"""
def url2path(url):
    """Convert a URL to a local file path"""
def url_escape(path):
    """Escape special characters in a URL path

    Turns '/foo bar/' into '/foo%20bar/'
    """
def url_unescape(path):
    """Unescape special characters in a URL path

    Turns '/foo%20bar/' into '/foo bar/'
    """
def samefile_simple(path, other_path):
    """
    Fill in for os.path.samefile when it is unavailable (Windows+py2).

    Do a case-insensitive string comparison in this case
    plus comparing the full stat result (including times)
    because Windows + py2 doesn't support the stat fields
    needed for identifying if it's the same file (st_ino, st_dev).

    Only to be used if os.path.samefile is not available.

    Parameters
    ----------
    path : str
        representing a path to a file
    other_path : str
        representing a path to another file

    Returns
    -------
    same:   Boolean that is True if both path and other path are the same
    """
def to_os_path(path: ApiPath, root: str = '') -> str:
    """Convert an API path to a filesystem path

    If given, root will be prepended to the path.
    root must be a filesystem path already.
    """
def to_api_path(os_path: str, root: str = '') -> ApiPath:
    """Convert a filesystem path to an API path

    If given, root will be removed from the path.
    root must be a filesystem path already.
    """
def check_version(v, check):
    """check version string v >= check

    If dev/prerelease tags result in TypeError for string-number comparison,
    it is assumed that the dependency is satisfied.
    Users on dev branches are responsible for keeping their own packages up to date.
    """

check_pid: Incomplete

async def run_sync_in_loop(maybe_async):
    """**DEPRECATED**: Use ``ensure_async`` from jupyter_core instead."""
def urlencode_unix_socket_path(socket_path):
    """Encodes a UNIX socket path string from a socket path for the `http+unix` URI form."""
def urldecode_unix_socket_path(socket_path):
    """Decodes a UNIX sock path string from an encoded sock path for the `http+unix` URI form."""
def urlencode_unix_socket(socket_path):
    """Encodes a UNIX socket URL from a socket path for the `http+unix` URI form."""
def unix_socket_in_use(socket_path):
    """Checks whether a UNIX socket path on disk is in use by attempting to connect to it."""
def fetch(urlstring, method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None):
    """
    Send a HTTP, HTTPS, or HTTP+UNIX request
    to a Tornado Web Server. Returns a tornado HTTPResponse.
    """
async def async_fetch(urlstring, method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None, io_loop: Incomplete | None = None):
    """
    Send an asynchronous HTTP, HTTPS, or HTTP+UNIX request
    to a Tornado Web Server. Returns a tornado HTTPResponse.
    """
def is_namespace_package(namespace):
    """Is the provided namespace a Python Namespace Package (PEP420).

    https://www.python.org/dev/peps/pep-0420/#specification

    Returns `None` if module is not importable.

    """
def filefind(filename, path_dirs: Incomplete | None = None):
    """Find a file by looking through a sequence of paths.
    This iterates through a sequence of paths looking for a file and returns
    the full, absolute path of the first occurence of the file.  If no set of
    path dirs is given, the filename is tested as is, after running through
    :func:`expandvars` and :func:`expanduser`.  Thus a simple call::

        filefind('myfile.txt')

    will find the file in the current working dir, but::

        filefind('~/myfile.txt')

    Will find the file in the users home directory.  This function does not
    automatically try any paths, such as the cwd or the user's home directory.

    Parameters
    ----------
    filename : str
        The filename to look for.
    path_dirs : str, None or sequence of str
        The sequence of paths to look for the file in.  If None, the filename
        need to be absolute or be in the cwd.  If a string, the string is
        put into a sequence and the searched.  If a sequence, walk through
        each element and join with ``filename``, calling :func:`expandvars`
        and :func:`expanduser` before testing for existence.

    Returns
    -------
    Raises :exc:`IOError` or returns absolute path to file.
    """
def expand_path(s):
    """Expand $VARS and ~names in a string, like a shell

    :Examples:
       In [2]: os.environ['FOO']='test'
       In [3]: expand_path('variable FOO is $FOO')
       Out[3]: 'variable FOO is test'
    """
def import_item(name):
    '''Import and return ``bar`` given the string ``foo.bar``.
    Calling ``bar = import_item("foo.bar")`` is the functional equivalent of
    executing the code ``from foo import bar``.
    Parameters
    ----------
    name : str
      The fully qualified name of the module/package being imported.
    Returns
    -------
    mod : module object
       The module that was imported.
    '''
