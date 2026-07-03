from ._disk import rmtree as rmtree
from _typeshed import Incomplete

popen4: Incomplete
MODE: Incomplete

def shelltype():
    """get the name (e.g. ``bash``) of the current command shell

    Args:
        None

    Returns:
        string name of the shell, or None if name can not be determined.
    """
def homedir():
    """get the full path of the user's home directory

    Args:
        None

    Returns:
        string path of the directory, or None if home can not be determined.
    """
def rootdir():
    """get the path corresponding to the root of the current drive

    Args:
        None

    Returns:
        string path of the directory.
    """
def username():
    """get the login name of the current user

    Args:
        None

    Returns:
        string name of the user.
    """
def sep(type: str = ''):
    """get the separator string for the given type of separator

    Args:
        type (str, default=''): one of ``{sep,line,path,ext,alt}``.

    Returns:
        separator string.
    """
def minpath(path, pathsep: Incomplete | None = None):
    """remove duplicate paths from given set of paths

    Args:
        path (str): path string (e.g. '/Users/foo/bin:/bin:/sbin:/usr/bin').
        pathsep (str, default=None): path separator (e.g. ``:``).

    Returns:
        string composed of one or more paths, with duplicates removed.

    Examples:
        >>> minpath('.:/Users/foo/bin:.:/Users/foo/bar/bin:/Users/foo/bin')
        '.:/Users/foo/bin:/Users/foo/bar/bin'
    """
def env(variable, all: bool = True, minimal: bool = False):
    """get dict of environment variables of the form ``{variable:value}``

    Args:
        variable (str): name or partial name for environment variable.
        all (bool, default=True): if False, only return the first match.
        minimal (bool, default=False): if True, remove all duplicate paths.

    Returns:
        dict of strings of environment variables.

    Warning:
        selecting all=False can lead to unexpected matches of *variable*.

    Examples:
        >>> env('*PATH')
        {'PYTHONPATH': '.', 'PATH': '.:/usr/bin:/bin:/usr/sbin:/sbin'}
    """
def whereis(prog, all: bool = False):
    """get path to the given program

    search the standard binary install locations for the given executable.

    Args:
        prog (str): name of an executable to search for (e.g. ``python``).
        all (bool, default=True): if True, return a list of paths found.

    Returns:
        string path of the executable, or list of path strings.
    """
def which(prog, allow_links: bool = True, ignore_errors: bool = True, all: bool = False):
    """get the path of the given program

    search the user's paths for the given executable.

    Args:
        prog (str): name of an executable to search for (e.g. ``python``).
        allow_links (bool, default=True): if False, replace link with fullpath.
        ignore_errors (bool, default=True): if True, ignore search errors.
        all (bool, default=False): if True, get list of paths for executable.

    Returns:
        if all=True, get a list of string paths, else return a string path. 
    """
def find(patterns, root: Incomplete | None = None, recurse: bool = True, type: Incomplete | None = None, verbose: bool = False):
    """get the path to a file or directory

    Args:
        patterns (str): name or partial name of items to search for.
        root (str, default=None): path of top-level directory to search.
        recurse (bool, default=True): if True, recurse downward from *root*.
        type (str, default=None): a search filter.
        verbose (bool, default=False): if True, be verbose about the search.

    Returns:
        a list of string paths.

    Notes:
        on some OS, *recursion* can be specified by recursion depth (*int*),
        and *patterns* can be specified with basic pattern matching. Also,
        multiple patterns can be specified by splitting patterns with a ``;``.
        The *type* can be one of ``{file, dir, link, socket, block, char}``.

    Examples:
        >>> find('pox*', root='..')
        ['/Users/foo/pox/pox', '/Users/foo/pox/scripts/pox_launcher.py']
        >>> 
        >>> find('*shutils*;*init*')
        ['/Users/foo/pox/pox/shutils.py', '/Users/foo/pox/pox/__init__.py']
    """
def walk(root, patterns: str = '*', recurse: bool = True, folders: bool = False, files: bool = True, links: bool = True):
    """walk directory tree and return a list matching the requested pattern

    Args:
        root (str): path of top-level directory to search.
        patterns (str, default='\\*'): (partial) name of items to search for.
        recurse (bool, default=True): if True, recurse downward from *root*.
        folders (bool, default=False): if True, include folders in the results.
        files (bool, default=True): if True, include files in results.
        links (bool, default=True): if True, include links in results.

    Returns:
        a list of string paths.

    Notes:
        patterns can be specified with basic pattern matching. Additionally,
        multiple patterns can be specified by splitting patterns with a ``;``.

    Examples:
        >>> walk('..', patterns='pox*')
        ['/Users/foo/pox/pox', '/Users/foo/pox/scripts/pox_launcher.py']
        >>> 
        >>> walk('.', patterns='*shutils*;*init*')
        ['/Users/foo/pox/pox/shutils.py', '/Users/foo/pox/pox/__init__.py']
    """
def where(name, path, pathsep: Incomplete | None = None):
    """get the full path for the given name string on the given search path.

    Args:
        name (str): name of file, folder, etc to find.
        path (str): path string (e.g. '/Users/foo/bin:/bin:/sbin:/usr/bin').
        pathsep (str, default=None): path separator (e.g. ``:``)

    Returns:
        the full path string.

    Notes:
        if pathsep is not provided, the OS default will be used.
    """
def mkdir(path, root: Incomplete | None = None, mode: Incomplete | None = None):
    """create a new directory in the root directory

    create a directory at *path* and any necessary parents (i.e. ``mkdir -p``).
    Default mode is read/write/execute for 'user' and 'group', and then
    read/execute otherwise.

    Args:
        path (str): string name of the new directory.
        root (str, default=None): path at which to build the new directory.
        mode (str, default=None): octal read/write permission [default: 0o775].

    Returns:
        string absolute path for new directory.
    """
def shellsub(command):
    """parse the given command to be formatted for remote shell invocation

    secure shell (``ssh``) can be used to send and execute commands to remote
    machines (using ``ssh <hostname> <command>``). Additional escape characters
    are needed to enable the command to be correctly formed and executed
    remotely. *shellsub* attemps to parse the given command string correctly
    so that it can be executed remotely with ssh.

    Args:
        command (str): the command to be executed remotely.

    Returns:
        the parsed command string.
    """
getSHELL = shelltype
getHOME = homedir
getROOT = rootdir
getUSER = username
getSEP = sep
stripDups = minpath
