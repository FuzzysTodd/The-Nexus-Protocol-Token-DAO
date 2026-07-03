from . import shutils as shutils
from ._disk import disk_used as disk_used, kbytes as kbytes
from _typeshed import Incomplete

def pattern(list=[], separator: str = ';'):
    """generate a filter pattern from list of strings

    Args:
        list (list(str), default=[]): a list of filter elements.
        separator (str, default=';'): the separator string.

    Returns:
        a string composed of filter elements joined by the separator.
    """
def expandvars(string, ref: Incomplete | None = None, secondref={}):
    """expand shell variables in string

    Expand shell variables of form ``$var`` and ``${var}``. Unknown variables
    are left unchanged. If a reference dictionary (*ref*) is provided,
    restrict lookups to *ref*. A second reference dictionary (*secondref*)
    can also be provided for failover searches. If *ref* is not provided,
    lookup variables are defined by the user's environment variables.

    Args:
        string (str): a string with shell variables.
        ref (dict(str), default=None): a dict of lookup variables.
        secondref (dict(str), default={}): a failover reference dict.

    Returns:
        string with the selected shell variables substituted.

    Examples:
        >>> expandvars('found:: $PYTHONPATH')
        'found:: .:/Users/foo/lib/python3.4/site-packages'
        >>> 
        >>> expandvars('found:: $PYTHONPATH', ref={})
        'found:: $PYTHONPATH'
    """
def getvars(path, ref: Incomplete | None = None, sep: Incomplete | None = None):
    """get a dictionary of all variables defined in path

    Extract shell variables of form ``$var`` and ``${var}``. Unknown variables
    will raise an exception. If a reference dictionary (*ref*) is provided,
    first try the lookup in *ref*.  Failover from *ref* will lookup variables
    defined in the user's environment variables.  Use *sep* to override the
    path separator (``os.sep``).

    Args:
        path (str): a path string with shell variables.
        ref (dict(str), default=None): a dict of lookup variables.
        sep (str, default=None): the path separator string.

    Returns:
        dict of shell variables found in the given path string.

    Examples:
        >>> getvars('$HOME/stuff')
        {'HOME': '/Users/foo'}
    """
def convert(files, platform: Incomplete | None = None, pathsep: Incomplete | None = None, verbose: bool = True):
    """convert text files to given platform type

    Ensure given files use the appropriate ``os.linesep`` and other formatting.

    Args:
        files (list(str)): a list of filenames.
        platform (str, default=None): platform name as in ``os.name``.
        pathsep (str, default=None): the path separator string.
        verbose (bool, default=True): if True, print debug statements..

    Returns:
        0 if converted, otherwise return 1.
    """
def replace(file, sub={}, outfile: Incomplete | None = None) -> None:
    """make text substitutions given by *sub* in the given file

    Args:
        file (str): path to original file.
        sub (dict(str), default={}: dict of string replacements ``{old:new}``.
        outfile (str, default=None): if given, don't overwrite original file.

    Returns:
        None

    Notes:
        ``replace`` uses regular expressions, thus a pattern may be used as
        *old* text. ``replace`` can fail if order of substitution is important.
    """
def index_slice(sequence, start, stop, step: int = 1, sequential: bool = False, inclusive: bool = False):
    """get the slice for a given sequence

    Slice indicies are determined by the positions of *start* and *stop*.
    If *start* is not found in the sequence, slice from the beginning. If
    *stop* is not found in the sequence, slice to the end.

    Args:
        sequence (list): an ordered sequence of elements.
        start (int): index for start of the slice.
        stop (int): index for stop position in the sequence.
        step (int, default=1): indices until next member of the slice.
        sequential (bool, default=False): if True, *start* must preceed *stop*.
        inclusive (bool, default=False): if True, include *stop* in the slice.

    Returns:
        slice corresponding to given *start*, *stop*, and *step*.
    """
def index_join(sequence, start, stop, step: int = 1, sequential: bool = True, inclusive: bool = True):
    """slice a list of strings, then join the remaining strings

    If *start* is not found in the sequence, slice from the beginning. If
    *stop* is not found in the sequence, slice to the end.

    Args:
        sequence (list): an ordered sequence of elements.
        start (int): index for start of the slice.
        stop (int): index for stop position in the sequence.
        step (int, default=1): indices until next member of the slice.
        sequential (bool, default=True): if True, *start* must preceed *stop*.
        inclusive (bool, default=True): if True, include *stop* in the slice.

    Returns:
        string produced by slicing the given sequence and joining the elements.
    """
def findpackage(package, root: Incomplete | None = None, all: bool = False, verbose: bool = True, recurse: bool = True):
    """retrieve the path(s) for a package

    Args:
        package (str): name of the package to search for.
        root (str, default=None): path string of top-level directory to search.
        all (bool, defualt=False): if True, return everywhere package is found.
        verbose (bool, default=True): if True, print messages about the search.
        recurse (bool, default=True): if True, recurse down the root directory.

    Returns:
        string path (or list of paths) where package is found.

    Notes:
        On some OS, recursion can be specified by recursion depth (an integer).
        ``findpackage`` will do standard pattern matching for package names,
        attempting to match the head directory of the distribution.
    """
def select(iterable, counter: str = '', minimum: bool = False, reverse: bool = False, all: bool = True):
    """find items in iterable with the max (or min) count of the given counter.

    Find the items in an iterable that have the maximum number of *counter*
    (e.g. counter='3' counts occurances of '3'). Use ``minimum=True`` to
    search for the minimum number of occurances of the *counter*.

    Args:
        iterable (list): an iterable of iterables (e.g. lists, strings, etc).
        counter (str, default=''): the item to count.
        minimum (bool, default=False): if True, find min count (else, max).
        reverse (bool, default=False): if True, reverse order of the results.
        all (bool, default=True): if False, only return the first result.

    Returns:
        list of items in the iterable with the min (or max) count.

    Examples:
        >>> z = ['zero','one','two','three','4','five','six','seven','8','9/81']
        >>> select(z, counter='e')
        ['three', 'seven']
        >>> select(z, counter='e', minimum=True)
        ['two', '4', 'six', '8', '9/81']
        >>> 
        >>> y = [[1,2,3],[4,5,6],[1,3,5]]
        >>> select(y, counter=3)
        [[1, 2, 3], [1, 3, 5]]
        >>> select(y, counter=3, minumim=True, all=False)
        [4, 5, 6]
    """
def selectdict(dict, counter: str = '', minimum: bool = False, all: bool = True):
    """return a dict of items with the max (or min) count of the given counter.

    Get the items from a dict that have the maximum number of the *counter*
    (e.g. counter='3' counts occurances of '3') in the values. Use
    ``minimum=True`` to search for minimum number of occurances of *counter*.

    Args:
        dict (dict): dict with iterables as values (e.g. lists, strings, etc).
        counter (str, default=''): the item to count.
        minimum (bool, default=False): if True, find min count (else, max).
        all (bool, default=True): if False, only return the first result.

    Returns:
        dict of items composed of the entries with the min (or max) count.

    Examples:
        >>> z = ['zero','one','two','three','4','five','six','seven','8','9/81']
        >>> z = dict(enumerate(z))
        >>> selectdict(z, counter='e')
        {3: 'three', 7: 'seven'}
        >>> selectdict(z, counter='e', minimum=True)
        {8: '8', 9: '9/81', 2: 'two', 4: '4', 6: 'six'}
        >>> 
        >>> y = {1: [1,2,3], 2: [4,5,6], 3: [1,3,5]}
        >>> selectdict(y, counter=3)
        {1: [1, 2, 3], 3: [1, 3, 5]}
        >>> selectdict(y, counter=3, minumim=True)
        {2: [4, 5, 6]}
    """
def remote(path, host: Incomplete | None = None, user: Incomplete | None = None, loopback: bool = False):
    """build string for a remote connection of the form ``[[user@]host:]path``

    Args:
        path (str): path string for location of target on (remote) filesystem.
        host (str, default=None): string name/ip address of (remote) host.
        user (str, default=None): user name on (remote) host.
        loopback (bool, default=False): if True, ensure *host* is used.

    Returns:
        a remote connection string.

    Notes:
        if loopback=True and host=None, then host will be set to localhost.
    """
def parse_remote(path, loopback: bool = False, login_flag: bool = False):
    """parse remote connection string of the form ``[[user@]host:]path``

    Args:
        path (str): remote connection string.
        loopback (bool, default=False): if True, ensure *host* is used.
        login_flag (bool, default=False): if True, prepend user with ``-l``.

    Returns:
        a tuple of the form ``(user, host, path)``.

    Notes:
        if loopback=True and host=None, then host will be set to localhost.
    """
def which_python(version: bool = False, lazy: bool = False, fullpath: bool = True, ignore_errors: bool = True):
    """get the command to launch the selected version of python

    ``which_python`` composes a command string that can be used to launch
    the desired python executable. The user's path is searched for the
    executable, unless ``lazy=True`` and thus only a lazy-evaluating command
    (e.g. ``which python``) is produced.

    Args:
        version (bool, default=False): if True, include the version of python.
        lazy (bool, default=False): if True, build a lazy-evaluating command.
        fullpath (bool, default=True): if True, provide the full path.
        ignore_errors (bool, default=True): if True, ignore path search errors.

    Returns:
        string of the implicit or explicit location of the python executable.

    Notes:
        if version is given as an int or float, include the version number
        in the command string.

        if the executable is not found, an error will be thrown unless
        ``ignore_error=True``.
    """
def wait_for(path, sleep: int = 1, tries: int = 150, ignore_errors: bool = False) -> None:
    """block execution by waiting for a file to appear at the given path
        
    Args:
        path (str): the path string to watch for the file.
        sleep (float, default=1): the time between checking results.
        tries (int, default=150): the number of times to try.
        ignore_errors (bool, default=False): if True, ignore timeout error.

    Returns:
        None

    Notes:
        if the file is not found after the given number of tries, an error
        will be thrown unless ``ignore_error=True``.

        using ``subproc = Popen(...)`` and ``subproc.wait()`` is usually
        a better approach. However, when a handle to the subprocess is
        unavailable, waiting for a file to appear at a given path is a
        decent last resort.
    """
makefilter = pattern
getVars = getvars
replaceText = replace
getLines = index_join
makeTarget = remote
parseTarget = parse_remote
prunelist = select
prunedict = selectdict
