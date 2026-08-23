import doctest as pdoctest
from _typeshed import Incomplete
from collections.abc import Generator
from doctest import DocTestFinder, DocTestRunner
from sympy.core.cache import clear_cache as clear_cache
from sympy.external import import_module as import_module
from sympy.external.gmpy import GROUND_TYPES as GROUND_TYPES, HAS_GMPY as HAS_GMPY
from typing import NamedTuple

IS_WINDOWS: Incomplete
ON_CI: Incomplete
SPLIT_DENSITY: Incomplete
SPLIT_DENSITY_SLOW: Incomplete

class Skipped(Exception): ...
class TimeOutError(Exception): ...
class DependencyError(Exception): ...

def convert_to_native_paths(lst):
    """
    Converts a list of '/' separated paths into a list of
    native (os.sep separated) paths and converts to lowercase
    if the system is case insensitive.
    """
def get_sympy_dir():
    """
    Returns the root SymPy directory and set the global value
    indicating whether the system is case sensitive or not.
    """
def setup_pprint(): ...
def raise_on_deprecated() -> Generator[None, None, None]:
    """Context manager to make DeprecationWarning raise an error

    This is to catch SymPyDeprecationWarning from library code while running
    tests and doctests. It is important to use this context manager around
    each individual test/doctest in case some tests modify the warning
    filters.
    """
def run_in_subprocess_with_hash_randomization(function, function_args=(), function_kwargs: Incomplete | None = None, command=..., module: str = 'sympy.testing.runtests', force: bool = False):
    '''
    Run a function in a Python subprocess with hash randomization enabled.

    If hash randomization is not supported by the version of Python given, it
    returns False.  Otherwise, it returns the exit value of the command.  The
    function is passed to sys.exit(), so the return value of the function will
    be the return value.

    The environment variable PYTHONHASHSEED is used to seed Python\'s hash
    randomization.  If it is set, this function will return False, because
    starting a new subprocess is unnecessary in that case.  If it is not set,
    one is set at random, and the tests are run.  Note that if this
    environment variable is set when Python starts, hash randomization is
    automatically enabled.  To force a subprocess to be created even if
    PYTHONHASHSEED is set, pass ``force=True``.  This flag will not force a
    subprocess in Python versions that do not support hash randomization (see
    below), because those versions of Python do not support the ``-R`` flag.

    ``function`` should be a string name of a function that is importable from
    the module ``module``, like "_test".  The default for ``module`` is
    "sympy.testing.runtests".  ``function_args`` and ``function_kwargs``
    should be a repr-able tuple and dict, respectively.  The default Python
    command is sys.executable, which is the currently running Python command.

    This function is necessary because the seed for hash randomization must be
    set by the environment variable before Python starts.  Hence, in order to
    use a predetermined seed for tests, we must start Python in a separate
    subprocess.

    Hash randomization was added in the minor Python versions 2.6.8, 2.7.3,
    3.1.5, and 3.2.3, and is enabled by default in all Python versions after
    and including 3.3.0.

    Examples
    ========

    >>> from sympy.testing.runtests import (
    ... run_in_subprocess_with_hash_randomization)
    >>> # run the core tests in verbose mode
    >>> run_in_subprocess_with_hash_randomization("_test",
    ... function_args=("core",),
    ... function_kwargs={\'verbose\': True}) # doctest: +SKIP
    # Will return 0 if sys.executable supports hash randomization and tests
    # pass, 1 if they fail, and False if it does not support hash
    # randomization.

    '''
def run_all_tests(test_args=(), test_kwargs: Incomplete | None = None, doctest_args=(), doctest_kwargs: Incomplete | None = None, examples_args=(), examples_kwargs: Incomplete | None = None) -> None:
    '''
    Run all tests.

    Right now, this runs the regular tests (bin/test), the doctests
    (bin/doctest), and the examples (examples/all.py).

    This is what ``setup.py test`` uses.

    You can pass arguments and keyword arguments to the test functions that
    support them (for now, test,  doctest, and the examples). See the
    docstrings of those functions for a description of the available options.

    For example, to run the solvers tests with colors turned off:

    >>> from sympy.testing.runtests import run_all_tests
    >>> run_all_tests(test_args=("solvers",),
    ... test_kwargs={"colors:False"}) # doctest: +SKIP

    '''
def test(*paths, subprocess: bool = True, rerun: int = 0, **kwargs):
    '''
    Run tests in the specified test_*.py files.

    Tests in a particular test_*.py file are run if any of the given strings
    in ``paths`` matches a part of the test file\'s path. If ``paths=[]``,
    tests in all test_*.py files are run.

    Notes:

    - If sort=False, tests are run in random order (not default).
    - Paths can be entered in native system format or in unix,
      forward-slash format.
    - Files that are on the blacklist can be tested by providing
      their path; they are only excluded if no paths are given.

    **Explanation of test results**

    ======  ===============================================================
    Output  Meaning
    ======  ===============================================================
    .       passed
    F       failed
    X       XPassed (expected to fail but passed)
    f       XFAILed (expected to fail and indeed failed)
    s       skipped
    w       slow
    T       timeout (e.g., when ``--timeout`` is used)
    K       KeyboardInterrupt (when running the slow tests with ``--slow``,
            you can interrupt one of them without killing the test runner)
    ======  ===============================================================


    Colors have no additional meaning and are used just to facilitate
    interpreting the output.

    Examples
    ========

    >>> import sympy

    Run all tests:

    >>> sympy.test()    # doctest: +SKIP

    Run one file:

    >>> sympy.test("sympy/core/tests/test_basic.py")    # doctest: +SKIP
    >>> sympy.test("_basic")    # doctest: +SKIP

    Run all tests in sympy/functions/ and some particular file:

    >>> sympy.test("sympy/core/tests/test_basic.py",
    ...        "sympy/functions")    # doctest: +SKIP

    Run all tests in sympy/core and sympy/utilities:

    >>> sympy.test("/core", "/util")    # doctest: +SKIP

    Run specific test from a file:

    >>> sympy.test("sympy/core/tests/test_basic.py",
    ...        kw="test_equality")    # doctest: +SKIP

    Run specific test from any file:

    >>> sympy.test(kw="subs")    # doctest: +SKIP

    Run the tests with verbose mode on:

    >>> sympy.test(verbose=True)    # doctest: +SKIP

    Do not sort the test output:

    >>> sympy.test(sort=False)    # doctest: +SKIP

    Turn on post-mortem pdb:

    >>> sympy.test(pdb=True)    # doctest: +SKIP

    Turn off colors:

    >>> sympy.test(colors=False)    # doctest: +SKIP

    Force colors, even when the output is not to a terminal (this is useful,
    e.g., if you are piping to ``less -r`` and you still want colors)

    >>> sympy.test(force_colors=False)    # doctest: +SKIP

    The traceback verboseness can be set to "short" or "no" (default is
    "short")

    >>> sympy.test(tb=\'no\')    # doctest: +SKIP

    The ``split`` option can be passed to split the test run into parts. The
    split currently only splits the test files, though this may change in the
    future. ``split`` should be a string of the form \'a/b\', which will run
    part ``a`` of ``b``. For instance, to run the first half of the test suite:

    >>> sympy.test(split=\'1/2\')  # doctest: +SKIP

    The ``time_balance`` option can be passed in conjunction with ``split``.
    If ``time_balance=True`` (the default for ``sympy.test``), SymPy will attempt
    to split the tests such that each split takes equal time.  This heuristic
    for balancing is based on pre-recorded test data.

    >>> sympy.test(split=\'1/2\', time_balance=True)  # doctest: +SKIP

    You can disable running the tests in a separate subprocess using
    ``subprocess=False``.  This is done to support seeding hash randomization,
    which is enabled by default in the Python versions where it is supported.
    If subprocess=False, hash randomization is enabled/disabled according to
    whether it has been enabled or not in the calling Python process.
    However, even if it is enabled, the seed cannot be printed unless it is
    called from a new Python process.

    Hash randomization was added in the minor Python versions 2.6.8, 2.7.3,
    3.1.5, and 3.2.3, and is enabled by default in all Python versions after
    and including 3.3.0.

    If hash randomization is not supported ``subprocess=False`` is used
    automatically.

    >>> sympy.test(subprocess=False)     # doctest: +SKIP

    To set the hash randomization seed, set the environment variable
    ``PYTHONHASHSEED`` before running the tests.  This can be done from within
    Python using

    >>> import os
    >>> os.environ[\'PYTHONHASHSEED\'] = \'42\' # doctest: +SKIP

    Or from the command line using

    $ PYTHONHASHSEED=42 ./bin/test

    If the seed is not set, a random seed will be chosen.

    Note that to reproduce the same hash values, you must use both the same seed
    as well as the same architecture (32-bit vs. 64-bit).

    '''
def doctest(*paths, subprocess: bool = True, rerun: int = 0, **kwargs):
    '''
    Runs doctests in all \\*.py files in the SymPy directory which match
    any of the given strings in ``paths`` or all tests if paths=[].

    Notes:

    - Paths can be entered in native system format or in unix,
      forward-slash format.
    - Files that are on the blacklist can be tested by providing
      their path; they are only excluded if no paths are given.

    Examples
    ========

    >>> import sympy

    Run all tests:

    >>> sympy.doctest() # doctest: +SKIP

    Run one file:

    >>> sympy.doctest("sympy/core/basic.py") # doctest: +SKIP
    >>> sympy.doctest("polynomial.rst") # doctest: +SKIP

    Run all tests in sympy/functions/ and some particular file:

    >>> sympy.doctest("/functions", "basic.py") # doctest: +SKIP

    Run any file having polynomial in its name, doc/src/modules/polynomial.rst,
    sympy/functions/special/polynomials.py, and sympy/polys/polynomial.py:

    >>> sympy.doctest("polynomial") # doctest: +SKIP

    The ``split`` option can be passed to split the test run into parts. The
    split currently only splits the test files, though this may change in the
    future. ``split`` should be a string of the form \'a/b\', which will run
    part ``a`` of ``b``. Note that the regular doctests and the Sphinx
    doctests are split independently. For instance, to run the first half of
    the test suite:

    >>> sympy.doctest(split=\'1/2\')  # doctest: +SKIP

    The ``subprocess`` and ``verbose`` options are the same as with the function
    ``test()`` (see the docstring of that function for more information) except
    that ``verbose`` may also be set equal to ``2`` in order to print
    individual doctest lines, as they are being tested.
    '''

sp: Incomplete

def split_list(l, split, density: Incomplete | None = None):
    """
    Splits a list into part a of b

    split should be a string of the form 'a/b'. For instance, '1/3' would give
    the split one of three.

    If the length of the list is not divisible by the number of splits, the
    last split will have more items.

    `density` may be specified as a list.  If specified,
    tests will be balanced so that each split has as equal-as-possible
    amount of mass according to `density`.

    >>> from sympy.testing.runtests import split_list
    >>> a = list(range(10))
    >>> split_list(a, '1/3')
    [0, 1, 2]
    >>> split_list(a, '2/3')
    [3, 4, 5]
    >>> split_list(a, '3/3')
    [6, 7, 8, 9]
    """

class SymPyTestResults(NamedTuple):
    failed: Incomplete
    attempted: Incomplete

def sympytestfile(filename, module_relative: bool = True, name: Incomplete | None = None, package: Incomplete | None = None, globs: Incomplete | None = None, verbose: Incomplete | None = None, report: bool = True, optionflags: int = 0, extraglobs: Incomplete | None = None, raise_on_error: bool = False, parser=..., encoding: Incomplete | None = None):
    '''
    Test examples in the given file.  Return (#failures, #tests).

    Optional keyword arg ``module_relative`` specifies how filenames
    should be interpreted:

    - If ``module_relative`` is True (the default), then ``filename``
      specifies a module-relative path.  By default, this path is
      relative to the calling module\'s directory; but if the
      ``package`` argument is specified, then it is relative to that
      package.  To ensure os-independence, ``filename`` should use
      "/" characters to separate path segments, and should not
      be an absolute path (i.e., it may not begin with "/").

    - If ``module_relative`` is False, then ``filename`` specifies an
      os-specific path.  The path may be absolute or relative (to
      the current working directory).

    Optional keyword arg ``name`` gives the name of the test; by default
    use the file\'s basename.

    Optional keyword argument ``package`` is a Python package or the
    name of a Python package whose directory should be used as the
    base directory for a module relative filename.  If no package is
    specified, then the calling module\'s directory is used as the base
    directory for module relative filenames.  It is an error to
    specify ``package`` if ``module_relative`` is False.

    Optional keyword arg ``globs`` gives a dict to be used as the globals
    when executing examples; by default, use {}.  A copy of this dict
    is actually used for each docstring, so that each docstring\'s
    examples start with a clean slate.

    Optional keyword arg ``extraglobs`` gives a dictionary that should be
    merged into the globals that are used to execute examples.  By
    default, no extra globals are used.

    Optional keyword arg ``verbose`` prints lots of stuff if true, prints
    only failures if false; by default, it\'s true iff "-v" is in sys.argv.

    Optional keyword arg ``report`` prints a summary at the end when true,
    else prints nothing at the end.  In verbose mode, the summary is
    detailed, else very brief (in fact, empty if all tests passed).

    Optional keyword arg ``optionflags`` or\'s together module constants,
    and defaults to 0.  Possible values (see the docs for details):

    - DONT_ACCEPT_TRUE_FOR_1
    - DONT_ACCEPT_BLANKLINE
    - NORMALIZE_WHITESPACE
    - ELLIPSIS
    - SKIP
    - IGNORE_EXCEPTION_DETAIL
    - REPORT_UDIFF
    - REPORT_CDIFF
    - REPORT_NDIFF
    - REPORT_ONLY_FIRST_FAILURE

    Optional keyword arg ``raise_on_error`` raises an exception on the
    first unexpected exception or failure. This allows failures to be
    post-mortem debugged.

    Optional keyword arg ``parser`` specifies a DocTestParser (or
    subclass) that should be used to extract tests from the files.

    Optional keyword arg ``encoding`` specifies an encoding that should
    be used to convert the file to unicode.

    Advanced tomfoolery:  testmod runs methods of a local instance of
    class doctest.Tester, then merges the results into (or creates)
    global Tester instance doctest.master.  Methods of doctest.master
    can be called directly too, if you want to do something unusual.
    Passing report=0 to testmod is especially useful then, to delay
    displaying a summary.  Invoke doctest.master.summarize(verbose)
    when you\'re done fiddling.
    '''

class SymPyTests:
    def __init__(self, reporter, kw: str = '', post_mortem: bool = False, seed: Incomplete | None = None, fast_threshold: Incomplete | None = None, slow_threshold: Incomplete | None = None) -> None: ...
    def test(self, sort: bool = False, timeout: bool = False, slow: bool = False, enhance_asserts: bool = False, fail_on_timeout: bool = False):
        """
        Runs the tests returning True if all tests pass, otherwise False.

        If sort=False run tests in random order.
        """
    def test_file(self, filename, sort: bool = True, timeout: bool = False, slow: bool = False, enhance_asserts: bool = False, fail_on_timeout: bool = False): ...
    def matches(self, x):
        '''
        Does the keyword expression self._kw match "x"? Returns True/False.

        Always returns True if self._kw is "".
        '''
    def get_test_files(self, dir, pat: str = 'test_*.py'):
        """
        Returns the list of test_*.py (default) files at or below directory
        ``dir`` relative to the SymPy home directory.
        """

class SymPyDocTests:
    def __init__(self, reporter, normal) -> None: ...
    def test(self):
        """
        Runs the tests and returns True if all tests pass, otherwise False.
        """
    def test_file(self, filename): ...
    def get_test_files(self, dir, pat: str = '*.py', init_only: bool = True):
        """
        Returns the list of \\*.py files (default) from which docstrings
        will be tested which are at or below directory ``dir``. By default,
        only those that have an __init__.py in their parent directory
        and do not start with ``test_`` will be included.
        """

class SymPyDocTestFinder(DocTestFinder):
    """
    A class used to extract the DocTests that are relevant to a given
    object, from its docstring and the docstrings of its contained
    objects.  Doctests can currently be extracted from the following
    object types: modules, functions, classes, methods, staticmethods,
    classmethods, and properties.

    Modified from doctest's version to look harder for code that
    appears comes from a different module. For example, the @vectorize
    decorator makes it look like functions come from multidimensional.py
    even though their code exists elsewhere.
    """

class SymPyDocTestRunner(DocTestRunner):
    """
    A class used to run DocTest test cases, and accumulate statistics.
    The ``run`` method is used to process a single DocTest case.  It
    returns a tuple ``(f, t)``, where ``t`` is the number of test cases
    tried, and ``f`` is the number of test cases that failed.

    Modified from the doctest version to not reset the sys.displayhook (see
    issue 5140).

    See the docstring of the original DocTestRunner for more information.
    """
    test: Incomplete
    debugger: Incomplete
    save_linecache_getlines: Incomplete
    def run(self, test, compileflags: Incomplete | None = None, out: Incomplete | None = None, clear_globs: bool = True):
        """
        Run the examples in ``test``, and display the results using the
        writer function ``out``.

        The examples are run in the namespace ``test.globs``.  If
        ``clear_globs`` is true (the default), then this namespace will
        be cleared after the test runs, to help with garbage
        collection.  If you would like to examine the namespace after
        the test completes, then use ``clear_globs=False``.

        ``compileflags`` gives the set of flags that should be used by
        the Python compiler when running the examples.  If not
        specified, then it will default to the set of future-import
        flags that apply to ``globs``.

        The output of each example is checked using
        ``SymPyDocTestRunner.check_output``, and the results are
        formatted by the ``SymPyDocTestRunner.report_*`` methods.
        """

monkeypatched_methods: Incomplete
oldname: Incomplete
newname: Incomplete

class SymPyOutputChecker(pdoctest.OutputChecker):
    """
    Compared to the OutputChecker from the stdlib our OutputChecker class
    supports numerical comparison of floats occurring in the output of the
    doctest examples
    """
    num_got_rgx: Incomplete
    num_want_rgx: Incomplete
    def __init__(self) -> None: ...
    def check_output(self, want, got, optionflags):
        """
        Return True iff the actual output from an example (`got`)
        matches the expected output (`want`).  These strings are
        always considered to match if they are identical; but
        depending on what option flags the test runner is using,
        several non-exact match types are also possible.  See the
        documentation for `TestRunner` for more information about
        option flags.
        """

class Reporter:
    """
    Parent class for all reporters.
    """

class PyTestReporter(Reporter):
    """
    Py.test like reporter. Should produce output identical to py.test.
    """
    slow_test_functions: Incomplete
    fast_test_functions: Incomplete
    def __init__(self, verbose: bool = False, tb: str = 'short', colors: bool = True, force_colors: bool = False, split: Incomplete | None = None) -> None: ...
    def root_dir(self, dir) -> None: ...
    @property
    def terminal_width(self): ...
    def write(self, text, color: str = '', align: str = 'left', width: Incomplete | None = None, force_colors: bool = False) -> None:
        '''
        Prints a text on the screen.

        It uses sys.stdout.write(), so no readline library is necessary.

        Parameters
        ==========

        color : choose from the colors below, "" means default color
        align : "left"/"right", "left" is a normal print, "right" is aligned on
                the right-hand side of the screen, filled with spaces if
                necessary
        width : the screen width

        '''
    def write_center(self, text, delim: str = '=') -> None: ...
    def write_exception(self, e, val, tb) -> None: ...
    def start(self, seed: Incomplete | None = None, msg: str = 'test process starts') -> None: ...
    def finish(self): ...
    def entering_filename(self, filename, n) -> None: ...
    def leaving_filename(self) -> None: ...
    def entering_test(self, f) -> None: ...
    def test_xfail(self) -> None: ...
    def test_xpass(self, v) -> None: ...
    def test_fail(self, exc_info) -> None: ...
    def doctest_fail(self, name, error_msg) -> None: ...
    def test_pass(self, char: str = '.') -> None: ...
    def test_skip(self, v: Incomplete | None = None) -> None: ...
    def test_exception(self, exc_info) -> None: ...
    def import_error(self, filename, exc_info) -> None: ...
