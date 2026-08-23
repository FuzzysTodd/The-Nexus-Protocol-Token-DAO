from _typeshed import Incomplete
from collections.abc import Generator

LOGGER: Incomplete

def file_hash(*args, **kwargs):
    '''
    WARNING: Importing this function from pooch.utils is DEPRECATED.
    Please import from the top-level namespace (`from pooch import file_hash`)
    instead, which is fully backwards compatible with pooch >= 0.1.

    Examples
    --------

    >>> fname = "test-file-for-hash.txt"
    >>> with open(fname, "w") as f:
    ...     __ = f.write("content of the file")
    >>> print(file_hash(fname))
    0fc74468e6a9a829f103d069aeb2bb4f8646bad58bf146bb0e3379b759ec4a00
    >>> import os
    >>> os.remove(fname)

    '''
def get_logger():
    """
    Get the default event logger.

    The logger records events like downloading files, unzipping archives, etc.
    Use the method :meth:`logging.Logger.setLevel` of this object to adjust the
    verbosity level from Pooch.

    Returns
    -------
    logger : :class:`logging.Logger`
        The logger object for Pooch
    """
def os_cache(project):
    """
    Default cache location based on the operating system.

    The folder locations are defined by the ``platformdirs``  package
    using the ``user_cache_dir`` function.
    Usually, the locations will be following (see the
    `platformdirs documentation <https://platformdirs.readthedocs.io>`__):

    * Mac: ``~/Library/Caches/<AppName>``
    * Unix: ``~/.cache/<AppName>`` or the value of the ``XDG_CACHE_HOME``
      environment variable, if defined.
    * Windows: ``C:\\Users\\<user>\\AppData\\Local\\<AppAuthor>\\<AppName>\\Cache``

    Parameters
    ----------
    project : str
        The project name.

    Returns
    -------
    cache_path : :class:`pathlib.Path`
        The default location for the data cache. User directories (``'~'``) are
        not expanded.

    """
def check_version(version, fallback: str = 'master'):
    '''
    Check if a version is PEP440 compliant and there are no unreleased changes.

    For example, ``version = "0.1"`` will be returned as is but ``version =
    "0.1+10.8dl8dh9"`` will return the fallback. This is the convention used by
    `versioneer <https://github.com/warner/python-versioneer>`__ to mark that
    this version is 10 commits ahead of the last release.

    Parameters
    ----------
    version : str
        A version string.
    fallback : str
        What to return if the version string has unreleased changes.

    Returns
    -------
    version : str
        If *version* is PEP440 compliant and there are unreleased changes, then
        return *version*. Otherwise, return *fallback*.

    Raises
    ------
    InvalidVersion
        If *version* is not PEP440 compliant.

    Examples
    --------

    >>> check_version("0.1")
    \'0.1\'
    >>> check_version("0.1a10")
    \'0.1a10\'
    >>> check_version("0.1+111.9hdg36")
    \'master\'
    >>> check_version("0.1+111.9hdg36", fallback="dev")
    \'dev\'

    '''
def parse_url(url):
    '''
    Parse a URL into 3 components:

    <protocol>://<netloc>/<path>

    Example URLs:

    * http://127.0.0.1:8080/test.nc
    * ftp://127.0.0.1:8080/test.nc
    * doi:10.6084/m9.figshare.923450.v1/test.nc

    The DOI is a special case. The protocol will be "doi", the netloc will be
    the DOI, and the path is what comes after the last "/".
    The only exception are Zenodo dois: the protocol will be "doi", the netloc
    will be composed by the "prefix/suffix" and the path is what comes after
    the second "/". This allows to support special cases of Zenodo dois where
    the path contains forward slashes "/", created by the GitHub-Zenodo
    integration service.

    Parameters
    ----------
    url : str
        The URL.

    Returns
    -------
    parsed_url : dict
        Three components of a URL (e.g.,
        ``{\'protocol\':\'http\', \'netloc\':\'127.0.0.1:8080\',\'path\': \'/test.nc\'}``).

    '''
def cache_location(path, env: Incomplete | None = None, version: Incomplete | None = None):
    """
    Location of the cache given a base path and optional configuration.

    Checks for the environment variable to overwrite the path of the local
    cache. Optionally add *version* to the path if given.

    Parameters
    ----------
    path : str, PathLike, list or tuple
        The path to the local data storage folder. If this is a list or tuple,
        we'll join the parts with the appropriate separator. Use
        :func:`pooch.os_cache` for a sensible default.
    version : str or None
        The version string for your project. Will be appended to given path if
        not None.
    env : str or None
        An environment variable that can be used to overwrite *path*. This
        allows users to control where they want the data to be stored. We'll
        append *version* to the end of this value as well.

    Returns
    -------
    local_path : PathLike
        The path to the local directory.

    """
def make_local_storage(path, env: Incomplete | None = None) -> None:
    """
    Create the local cache directory and make sure it's writable.

    Parameters
    ----------
    path : str or PathLike
        The path to the local data storage folder.
    env : str or None
        An environment variable that can be used to overwrite *path*. Only used
        in the error message in case the folder is not writable.
    """
def temporary_file(path: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """
    Create a closed and named temporary file and make sure it's cleaned up.

    Using :class:`tempfile.NamedTemporaryFile` will fail on Windows if trying
    to open the file a second time (when passing its name to Pooch function,
    for example). This context manager creates the file, closes it, yields the
    file path, and makes sure it's deleted in the end.

    Parameters
    ----------
    path : str or PathLike
        The directory in which the temporary file will be created.

    Yields
    ------
    fname : str
        The path to the temporary file.

    """
def unique_file_name(url):
    '''
    Create a unique file name based on the given URL.

    The file name will be unique to the URL by prepending the name with the MD5
    hash (hex digest) of the URL. The name will also include the last portion
    of the URL.

    The format will be: ``{md5}-{filename}.{ext}``

    The file name will be cropped so that the entire name (including the hash)
    is less than 255 characters long (the limit on most file systems).

    Parameters
    ----------
    url : str
        The URL with a file name at the end.

    Returns
    -------
    fname : str
        The file name, unique to this URL.

    Examples
    --------

    >>> print(unique_file_name("https://www.some-server.org/2020/data.txt"))
    02ddee027ce5ebb3d7059fb23d210604-data.txt
    >>> print(unique_file_name("https://www.some-server.org/2019/data.txt"))
    9780092867b497fca6fc87d8308f1025-data.txt
    >>> print(unique_file_name("https://www.some-server.org/2020/data.txt.gz"))
    181a9d52e908219c2076f55145d6a344-data.txt.gz

    '''
