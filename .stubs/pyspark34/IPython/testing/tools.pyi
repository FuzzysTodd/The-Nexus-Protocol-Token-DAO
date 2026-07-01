import unittest
from . import skipdoctest as skipdoctest
from IPython.utils import py3compat as py3compat
from IPython.utils.io import Tee as Tee, temp_pyfile as temp_pyfile
from IPython.utils.process import get_output_error_code as get_output_error_code
from IPython.utils.text import list_strings as list_strings
from _typeshed import Incomplete
from collections.abc import Generator
from io import StringIO

doctest_deco: Incomplete

def full_path(startPath, files):
    """Make full paths for all the listed files, based on startPath.

    Only the base part of startPath is kept, since this routine is typically
    used with a script's ``__file__`` variable as startPath. The base of startPath
    is then prepended to all the listed files, forming the output list.

    Parameters
    ----------
    startPath : string
      Initial path to use as the base for the results.  This path is split
      using os.path.split() and only its first component is kept.

    files : string or list
      One or more files.

    Examples
    --------

    >>> full_path('/foo/bar.py',['a.txt','b.txt'])
    ['/foo/a.txt', '/foo/b.txt']

    >>> full_path('/foo',['a.txt','b.txt'])
    ['/a.txt', '/b.txt']

    If a single file is given, the output is still a list::

        >>> full_path('/foo','a.txt')
        ['/a.txt']
    """
def parse_test_output(txt):
    """Parse the output of a test run and return errors, failures.

    Parameters
    ----------
    txt : str
      Text output of a test run, assumed to contain a line of one of the
      following forms::

        'FAILED (errors=1)'
        'FAILED (failures=1)'
        'FAILED (errors=1, failures=1)'

    Returns
    -------
    nerr, nfail
      number of errors and failures.
    """
def default_argv():
    """Return a valid default argv for creating testing instances of ipython"""
def default_config():
    """Return a config object with good defaults for testing."""
def get_ipython_cmd(as_string: bool = False):
    """
    Return appropriate IPython command line name. By default, this will return
    a list that can be used with subprocess.Popen, for example, but passing
    `as_string=True` allows for returning the IPython command as a string.

    Parameters
    ----------
    as_string: bool
        Flag to allow to return the command as a string.
    """
def ipexec(fname, options: Incomplete | None = None, commands=()):
    """Utility to call 'ipython filename'.

    Starts IPython with a minimal and safe configuration to make startup as fast
    as possible.

    Note that this starts IPython in a subprocess!

    Parameters
    ----------
    fname : str, Path
      Name of file to be executed (should have .py or .ipy extension).

    options : optional, list
      Extra command-line flags to be passed to IPython.

    commands : optional, list
      Commands to send in on stdin

    Returns
    -------
    ``(stdout, stderr)`` of ipython subprocess.
    """
def ipexec_validate(fname, expected_out, expected_err: str = '', options: Incomplete | None = None, commands=()) -> None:
    """Utility to call 'ipython filename' and validate output/error.

    This function raises an AssertionError if the validation fails.

    Note that this starts IPython in a subprocess!

    Parameters
    ----------
    fname : str, Path
      Name of the file to be executed (should have .py or .ipy extension).

    expected_out : str
      Expected stdout of the process.

    expected_err : optional, str
      Expected stderr of the process.

    options : optional, list
      Extra command-line flags to be passed to IPython.

    Returns
    -------
    None
    """

class TempFileMixin(unittest.TestCase):
    """Utility class to create temporary Python/IPython files.

    Meant as a mixin class for test cases."""
    tmps: Incomplete
    fname: Incomplete
    def mktmp(self, src, ext: str = '.py') -> None:
        """Make a valid python temp file."""
    def tearDown(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

pair_fail_msg: str

def check_pairs(func, pairs) -> None:
    """Utility function for the common case of checking a function with a
    sequence of input/output pairs.

    Parameters
    ----------
    func : callable
      The function to be tested. Should accept a single argument.
    pairs : iterable
      A list of (input, expected_output) tuples.

    Returns
    -------
    None. Raises an AssertionError if any output does not match the expected
    value.
    """
MyStringIO = StringIO
notprinted_msg: str

class AssertPrints:
    '''Context manager for testing that code prints certain text.

    Examples
    --------
    >>> with AssertPrints("abc", suppress=False):
    ...     print("abcd")
    ...     print("def")
    ...
    abcd
    def
    '''
    s: Incomplete
    channel: Incomplete
    suppress: Incomplete
    def __init__(self, s, channel: str = 'stdout', suppress: bool = True) -> None: ...
    orig_stream: Incomplete
    buffer: Incomplete
    tee: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, etype: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None): ...

printed_msg: str

class AssertNotPrints(AssertPrints):
    """Context manager for checking that certain output *isn't* produced.

    Counterpart of AssertPrints"""
    def __exit__(self, etype: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None): ...

def mute_warn() -> Generator[None, None, None]: ...
def make_tempfile(name) -> Generator[None, None, None]:
    """Create an empty, named, temporary file for the duration of the context."""
def fake_input(inputs):
    """Temporarily replace the input() function to return the given values

    Use as a context manager:

    with fake_input(['result1', 'result2']):
        ...

    Values are returned in order. If input() is called again after the last value
    was used, EOFError is raised.
    """
def help_output_test(subcommand: str = ''):
    """test that `ipython [subcommand] -h` works"""
def help_all_output_test(subcommand: str = ''):
    """test that `ipython [subcommand] --help-all` works"""
