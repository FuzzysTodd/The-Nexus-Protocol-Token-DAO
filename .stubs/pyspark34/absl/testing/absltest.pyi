import enum
import typing
import unittest
from _typeshed import Incomplete
from absl import app as app, flags as flags, logging as logging
from absl.testing import xml_reporter as xml_reporter
from typing import Any, AnyStr, BinaryIO, Callable, ContextManager, MutableMapping, MutableSequence, NoReturn, Sequence, Text, TextIO, Type
from unittest import mock as mock

skip = unittest.skip
skipIf = unittest.skipIf
skipUnless = unittest.skipUnless
SkipTest = unittest.SkipTest
expectedFailure = unittest.expectedFailure
FLAGS: Incomplete

def expectedFailureIf(condition, reason):
    '''Expects the test to fail if the run condition is True.

  Example usage::

      @expectedFailureIf(sys.version.major == 2, "Not yet working in py2")
      def test_foo(self):
        ...

  Args:
    condition: bool, whether to expect failure or not.
    reason: Text, the reason to expect failure.
  Returns:
    Decorator function
  '''

class TempFileCleanup(enum.Enum):
    ALWAYS: str
    SUCCESS: str
    OFF: str

def get_default_test_srcdir() -> Text:
    """Returns default test source dir."""
def get_default_test_tmpdir() -> Text:
    """Returns default test temp dir."""

TEST_SRCDIR: Incomplete
TEST_TMPDIR: Incomplete

class _TempDir:
    """Represents a temporary directory for tests.

  Creation of this class is internal. Using its public methods is OK.

  This class implements the `os.PathLike` interface (specifically,
  `os.PathLike[str]`). This means, in Python 3, it can be directly passed
  to e.g. `os.path.join()`.
  """
    def __init__(self, path: Text) -> None:
        """Module-private: do not instantiate outside module."""
    @property
    def full_path(self) -> Text:
        """Returns the path, as a string, for the directory.

    TIP: Instead of e.g. `os.path.join(temp_dir.full_path)`, you can simply
    do `os.path.join(temp_dir)` because `__fspath__()` is implemented.
    """
    def __fspath__(self) -> Text:
        """See os.PathLike."""
    def create_file(self, file_path: Text | None = None, content: AnyStr | None = None, mode: Text = 'w', encoding: Text = 'utf8', errors: Text = 'strict') -> _TempFile:
        """Create a file in the directory.

    NOTE: If the file already exists, it will be made writable and overwritten.

    Args:
      file_path: Optional file path for the temp file. If not given, a unique
        file name will be generated and used. Slashes are allowed in the name;
        any missing intermediate directories will be created. NOTE: This path
        is the path that will be cleaned up, including any directories in the
        path, e.g., 'foo/bar/baz.txt' will `rm -r foo`
      content: Optional string or bytes to initially write to the file. If not
        specified, then an empty file is created.
      mode: Mode string to use when writing content. Only used if `content` is
        non-empty.
      encoding: Encoding to use when writing string content. Only used if
        `content` is text.
      errors: How to handle text to bytes encoding errors. Only used if
        `content` is text.

    Returns:
      A _TempFile representing the created file.
    """
    def mkdir(self, dir_path: Text | None = None) -> _TempDir:
        """Create a directory in the directory.

    Args:
      dir_path: Optional path to the directory to create. If not given,
        a unique name will be generated and used.

    Returns:
      A _TempDir representing the created directory.
    """

class _TempFile:
    """Represents a tempfile for tests.

  Creation of this class is internal. Using its public methods is OK.

  This class implements the `os.PathLike` interface (specifically,
  `os.PathLike[str]`). This means, in Python 3, it can be directly passed
  to e.g. `os.path.join()`.
  """
    def __init__(self, path: Text) -> None:
        """Private: use _create instead."""
    @property
    def full_path(self) -> Text:
        """Returns the path, as a string, for the file.

    TIP: Instead of e.g. `os.path.join(temp_file.full_path)`, you can simply
    do `os.path.join(temp_file)` because `__fspath__()` is implemented.
    """
    def __fspath__(self) -> Text:
        """See os.PathLike."""
    def read_text(self, encoding: Text = 'utf8', errors: Text = 'strict') -> Text:
        """Return the contents of the file as text."""
    def read_bytes(self) -> bytes:
        """Return the content of the file as bytes."""
    def write_text(self, text: Text, mode: Text = 'w', encoding: Text = 'utf8', errors: Text = 'strict') -> None:
        """Write text to the file.

    Args:
      text: Text to write. In Python 2, it can be bytes, which will be
        decoded using the `encoding` arg (this is as an aid for code that
        is 2 and 3 compatible).
      mode: The mode to open the file for writing.
      encoding: The encoding to use when writing the text to the file.
      errors: The error handling strategy to use when converting text to bytes.
    """
    def write_bytes(self, data: bytes, mode: Text = 'wb') -> None:
        '''Write bytes to the file.

    Args:
      data: bytes to write.
      mode: Mode to open the file for writing. The "b" flag is implicit if
        not already present. It must not have the "t" flag.
    '''
    def open_text(self, mode: Text = 'rt', encoding: Text = 'utf8', errors: Text = 'strict') -> ContextManager[TextIO]:
        '''Return a context manager for opening the file in text mode.

    Args:
      mode: The mode to open the file in. The "t" flag is implicit if not
        already present. It must not have the "b" flag.
      encoding: The encoding to use when opening the file.
      errors: How to handle decoding errors.

    Returns:
      Context manager that yields an open file.

    Raises:
      ValueError: if invalid inputs are provided.
    '''
    def open_bytes(self, mode: Text = 'rb') -> ContextManager[BinaryIO]:
        '''Return a context manager for opening the file in binary mode.

    Args:
      mode: The mode to open the file in. The "b" mode is implicit if not
        already present. It must not have the "t" flag.

    Returns:
      Context manager that yields an open file.

    Raises:
      ValueError: if invalid inputs are provided.
    '''

class _method:
    """A decorator that supports both instance and classmethod invocations.

  Using similar semantics to the @property builtin, this decorator can augment
  an instance method to support conditional logic when invoked on a class
  object. This breaks support for invoking an instance method via the class
  (e.g. Cls.method(self, ...)) but is still situationally useful.
  """
    def __init__(self, finstancemethod: Callable[..., Any]) -> None: ...
    def classmethod(self, fclassmethod: Callable[..., Any]) -> _method: ...
    def __doc__(self) -> str: ...
    def __get__(self, obj: Any | None, type_: Type[Any] | None) -> Callable[..., Any]: ...

class TestCase(unittest.TestCase):
    """Extension of unittest.TestCase providing more power."""
    tempfile_cleanup: TempFileCleanup
    maxDiff: Incomplete
    longMessage: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def setUp(self) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    def create_tempdir(self, name: Text | None = None, cleanup: TempFileCleanup | None = None) -> _TempDir:
        """Create a temporary directory specific to the test.

    NOTE: The directory and its contents will be recursively cleared before
    creation. This ensures that there is no pre-existing state.

    This creates a named directory on disk that is isolated to this test, and
    will be properly cleaned up by the test. This avoids several pitfalls of
    creating temporary directories for test purposes, as well as makes it easier
    to setup directories and verify their contents. For example::

        def test_foo(self):
          out_dir = self.create_tempdir()
          out_log = out_dir.create_file('output.log')
          expected_outputs = [
              os.path.join(out_dir, 'data-0.txt'),
              os.path.join(out_dir, 'data-1.txt'),
          ]
          code_under_test(out_dir)
          self.assertTrue(os.path.exists(expected_paths[0]))
          self.assertTrue(os.path.exists(expected_paths[1]))
          self.assertEqual('foo', out_log.read_text())

    See also: :meth:`create_tempfile` for creating temporary files.

    Args:
      name: Optional name of the directory. If not given, a unique
        name will be generated and used.
      cleanup: Optional cleanup policy on when/if to remove the directory (and
        all its contents) at the end of the test. If None, then uses
        :attr:`tempfile_cleanup`.

    Returns:
      A _TempDir representing the created directory; see _TempDir class docs
      for usage.
    """
    def create_tempfile(self, file_path: Text | None = None, content: AnyStr | None = None, mode: Text = 'w', encoding: Text = 'utf8', errors: Text = 'strict', cleanup: TempFileCleanup | None = None) -> _TempFile:
        """Create a temporary file specific to the test.

    This creates a named file on disk that is isolated to this test, and will
    be properly cleaned up by the test. This avoids several pitfalls of
    creating temporary files for test purposes, as well as makes it easier
    to setup files, their data, read them back, and inspect them when
    a test fails. For example::

        def test_foo(self):
          output = self.create_tempfile()
          code_under_test(output)
          self.assertGreater(os.path.getsize(output), 0)
          self.assertEqual('foo', output.read_text())

    NOTE: This will zero-out the file. This ensures there is no pre-existing
    state.
    NOTE: If the file already exists, it will be made writable and overwritten.

    See also: :meth:`create_tempdir` for creating temporary directories, and
    ``_TempDir.create_file`` for creating files within a temporary directory.

    Args:
      file_path: Optional file path for the temp file. If not given, a unique
        file name will be generated and used. Slashes are allowed in the name;
        any missing intermediate directories will be created. NOTE: This path is
        the path that will be cleaned up, including any directories in the path,
        e.g., ``'foo/bar/baz.txt'`` will ``rm -r foo``.
      content: Optional string or
        bytes to initially write to the file. If not
        specified, then an empty file is created.
      mode: Mode string to use when writing content. Only used if `content` is
        non-empty.
      encoding: Encoding to use when writing string content. Only used if
        `content` is text.
      errors: How to handle text to bytes encoding errors. Only used if
        `content` is text.
      cleanup: Optional cleanup policy on when/if to remove the directory (and
        all its contents) at the end of the test. If None, then uses
        :attr:`tempfile_cleanup`.

    Returns:
      A _TempFile representing the created file; see _TempFile class docs for
      usage.
    """
    def shortDescription(self) -> Text:
        """Formats both the test method name and the first line of its docstring.

    If no docstring is given, only returns the method name.

    This method overrides unittest.TestCase.shortDescription(), which
    only returns the first line of the docstring, obscuring the name
    of the test upon failure.

    Returns:
      desc: A short description of a test method.
    """
    def assertStartsWith(self, actual, expected_start, msg: Incomplete | None = None) -> None:
        """Asserts that actual.startswith(expected_start) is True.

    Args:
      actual: str
      expected_start: str
      msg: Optional message to report on failure.
    """
    def assertNotStartsWith(self, actual, unexpected_start, msg: Incomplete | None = None) -> None:
        """Asserts that actual.startswith(unexpected_start) is False.

    Args:
      actual: str
      unexpected_start: str
      msg: Optional message to report on failure.
    """
    def assertEndsWith(self, actual, expected_end, msg: Incomplete | None = None) -> None:
        """Asserts that actual.endswith(expected_end) is True.

    Args:
      actual: str
      expected_end: str
      msg: Optional message to report on failure.
    """
    def assertNotEndsWith(self, actual, unexpected_end, msg: Incomplete | None = None) -> None:
        """Asserts that actual.endswith(unexpected_end) is False.

    Args:
      actual: str
      unexpected_end: str
      msg: Optional message to report on failure.
    """
    def assertSequenceStartsWith(self, prefix, whole, msg: Incomplete | None = None) -> None:
        """An equality assertion for the beginning of ordered sequences.

    If prefix is an empty sequence, it will raise an error unless whole is also
    an empty sequence.

    If prefix is not a sequence, it will raise an error if the first element of
    whole does not match.

    Args:
      prefix: A sequence expected at the beginning of the whole parameter.
      whole: The sequence in which to look for prefix.
      msg: Optional message to report on failure.
    """
    def assertEmpty(self, container, msg: Incomplete | None = None) -> None:
        """Asserts that an object has zero length.

    Args:
      container: Anything that implements the collections.abc.Sized interface.
      msg: Optional message to report on failure.
    """
    def assertNotEmpty(self, container, msg: Incomplete | None = None) -> None:
        """Asserts that an object has non-zero length.

    Args:
      container: Anything that implements the collections.abc.Sized interface.
      msg: Optional message to report on failure.
    """
    def assertLen(self, container, expected_len, msg: Incomplete | None = None) -> None:
        """Asserts that an object has the expected length.

    Args:
      container: Anything that implements the collections.abc.Sized interface.
      expected_len: The expected length of the container.
      msg: Optional message to report on failure.
    """
    def assertSequenceAlmostEqual(self, expected_seq, actual_seq, places: Incomplete | None = None, msg: Incomplete | None = None, delta: Incomplete | None = None) -> None:
        """An approximate equality assertion for ordered sequences.

    Fail if the two sequences are unequal as determined by their value
    differences rounded to the given number of decimal places (default 7) and
    comparing to zero, or by comparing that the difference between each value
    in the two sequences is more than the given delta.

    Note that decimal places (from zero) are usually not the same as significant
    digits (measured from the most significant digit).

    If the two sequences compare equal then they will automatically compare
    almost equal.

    Args:
      expected_seq: A sequence containing elements we are expecting.
      actual_seq: The sequence that we are testing.
      places: The number of decimal places to compare.
      msg: The message to be printed if the test fails.
      delta: The OK difference between compared values.
    """
    def assertContainsSubset(self, expected_subset, actual_set, msg: Incomplete | None = None) -> None:
        """Checks whether actual iterable is a superset of expected iterable."""
    def assertNoCommonElements(self, expected_seq, actual_seq, msg: Incomplete | None = None) -> None:
        """Checks whether actual iterable and expected iterable are disjoint."""
    def assertItemsEqual(self, expected_seq, actual_seq, msg: Incomplete | None = None) -> None:
        """Deprecated, please use assertCountEqual instead.

    This is equivalent to assertCountEqual.

    Args:
      expected_seq: A sequence containing elements we are expecting.
      actual_seq: The sequence that we are testing.
      msg: The message to be printed if the test fails.
    """
    def assertSameElements(self, expected_seq, actual_seq, msg: Incomplete | None = None) -> None:
        """Asserts that two sequences have the same elements (in any order).

    This method, unlike assertCountEqual, doesn't care about any
    duplicates in the expected and actual sequences::

        # Doesn't raise an AssertionError
        assertSameElements([1, 1, 1, 0, 0, 0], [0, 1])

    If possible, you should use assertCountEqual instead of
    assertSameElements.

    Args:
      expected_seq: A sequence containing elements we are expecting.
      actual_seq: The sequence that we are testing.
      msg: The message to be printed if the test fails.
    """
    def assertMultiLineEqual(self, first, second, msg: Incomplete | None = None, **kwargs) -> None:
        """Asserts that two multi-line strings are equal."""
    def assertBetween(self, value, minv, maxv, msg: Incomplete | None = None) -> None:
        """Asserts that value is between minv and maxv (inclusive)."""
    def assertRegexMatch(self, actual_str, regexes, message: Incomplete | None = None) -> None:
        '''Asserts that at least one regex in regexes matches str.

    If possible you should use `assertRegex`, which is a simpler
    version of this method. `assertRegex` takes a single regular
    expression (a string or re compiled object) instead of a list.

    Notes:

    1. This function uses substring matching, i.e. the matching
       succeeds if *any* substring of the error message matches *any*
       regex in the list.  This is more convenient for the user than
       full-string matching.

    2. If regexes is the empty list, the matching will always fail.

    3. Use regexes=[\'\'] for a regex that will always pass.

    4. \'.\' matches any single character *except* the newline.  To
       match any character, use \'(.|\\n)\'.

    5. \'^\' matches the beginning of each line, not just the beginning
       of the string.  Similarly, \'$\' matches the end of each line.

    6. An exception will be thrown if regexes contains an invalid
       regex.

    Args:
      actual_str:  The string we try to match with the items in regexes.
      regexes:  The regular expressions we want to match against str.
          See "Notes" above for detailed notes on how this is interpreted.
      message:  The message to be printed if the test fails.
    '''
    def assertCommandSucceeds(self, command, regexes=(b'',), env: Incomplete | None = None, close_fds: bool = True, msg: Incomplete | None = None) -> None:
        """Asserts that a shell command succeeds (i.e. exits with code 0).

    Args:
      command: List or string representing the command to run.
      regexes: List of regular expression byte strings that match success.
      env: Dictionary of environment variable settings. If None, no environment
          variables will be set for the child process. This is to make tests
          more hermetic. NOTE: this behavior is different than the standard
          subprocess module.
      close_fds: Whether or not to close all open fd's in the child after
          forking.
      msg: Optional message to report on failure.
    """
    def assertCommandFails(self, command, regexes, env: Incomplete | None = None, close_fds: bool = True, msg: Incomplete | None = None) -> None:
        """Asserts a shell command fails and the error matches a regex in a list.

    Args:
      command: List or string representing the command to run.
      regexes: the list of regular expression strings.
      env: Dictionary of environment variable settings. If None, no environment
          variables will be set for the child process. This is to make tests
          more hermetic. NOTE: this behavior is different than the standard
          subprocess module.
      close_fds: Whether or not to close all open fd's in the child after
          forking.
      msg: Optional message to report on failure.
    """
    class _AssertRaisesContext:
        expected_exception: Incomplete
        test_case: Incomplete
        test_func: Incomplete
        msg: Incomplete
        def __init__(self, expected_exception, test_case, test_func, msg: Incomplete | None = None) -> None: ...
        def __enter__(self): ...
        exception: Incomplete
        def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: types.TracebackType | None): ...
    @typing.overload
    def assertRaisesWithPredicateMatch(self, expected_exception, predicate) -> _AssertRaisesContext: ...
    @typing.overload
    def assertRaisesWithPredicateMatch(self, expected_exception, predicate, callable_obj: Callable[..., Any], *args, **kwargs) -> None: ...
    @typing.overload
    def assertRaisesWithLiteralMatch(self, expected_exception, expected_exception_message) -> _AssertRaisesContext: ...
    @typing.overload
    def assertRaisesWithLiteralMatch(self, expected_exception, expected_exception_message, callable_obj: Callable[..., Any], *args, **kwargs) -> None: ...
    def assertContainsInOrder(self, strings, target, msg: Incomplete | None = None) -> None:
        """Asserts that the strings provided are found in the target in order.

    This may be useful for checking HTML output.

    Args:
      strings: A list of strings, such as [ 'fox', 'dog' ]
      target: A target string in which to look for the strings, such as
          'The quick brown fox jumped over the lazy dog'.
      msg: Optional message to report on failure.
    """
    def assertContainsSubsequence(self, container, subsequence, msg: Incomplete | None = None) -> None:
        '''Asserts that "container" contains "subsequence" as a subsequence.

    Asserts that "container" contains all the elements of "subsequence", in
    order, but possibly with other elements interspersed. For example, [1, 2, 3]
    is a subsequence of [0, 0, 1, 2, 0, 3, 0] but not of [0, 0, 1, 3, 0, 2, 0].

    Args:
      container: the list we\'re testing for subsequence inclusion.
      subsequence: the list we hope will be a subsequence of container.
      msg: Optional message to report on failure.
    '''
    def assertContainsExactSubsequence(self, container, subsequence, msg: Incomplete | None = None) -> None:
        '''Asserts that "container" contains "subsequence" as an exact subsequence.

    Asserts that "container" contains all the elements of "subsequence", in
    order, and without other elements interspersed. For example, [1, 2, 3] is an
    exact subsequence of [0, 0, 1, 2, 3, 0] but not of [0, 0, 1, 2, 0, 3, 0].

    Args:
      container: the list we\'re testing for subsequence inclusion.
      subsequence: the list we hope will be an exact subsequence of container.
      msg: Optional message to report on failure.
    '''
    def assertTotallyOrdered(self, *groups, **kwargs) -> None:
        """Asserts that total ordering has been implemented correctly.

    For example, say you have a class A that compares only on its attribute x.
    Comparators other than ``__lt__`` are omitted for brevity::

        class A(object):
          def __init__(self, x, y):
            self.x = x
            self.y = y

          def __hash__(self):
            return hash(self.x)

          def __lt__(self, other):
            try:
              return self.x < other.x
            except AttributeError:
              return NotImplemented

    assertTotallyOrdered will check that instances can be ordered correctly.
    For example::

        self.assertTotallyOrdered(
            [None],  # None should come before everything else.
            [1],  # Integers sort earlier.
            [A(1, 'a')],
            [A(2, 'b')],  # 2 is after 1.
            [A(3, 'c'), A(3, 'd')],  # The second argument is irrelevant.
            [A(4, 'z')],
            ['foo'])  # Strings sort last.

    Args:
      *groups: A list of groups of elements.  Each group of elements is a list
        of objects that are equal.  The elements in each group must be less
        than the elements in the group after it.  For example, these groups are
        totally ordered: ``[None]``, ``[1]``, ``[2, 2]``, ``[3]``.
      **kwargs: optional msg keyword argument can be passed.
    """
    def assertDictEqual(self, a, b, msg: Incomplete | None = None):
        """Raises AssertionError if a and b are not equal dictionaries.

    Args:
      a: A dict, the expected value.
      b: A dict, the actual value.
      msg: An optional str, the associated message.

    Raises:
      AssertionError: if the dictionaries are not equal.
    """
    def assertUrlEqual(self, a, b, msg: Incomplete | None = None) -> None:
        """Asserts that urls are equal, ignoring ordering of query params."""
    def assertSameStructure(self, a, b, aname: str = 'a', bname: str = 'b', msg: Incomplete | None = None) -> None:
        """Asserts that two values contain the same structural content.

    The two arguments should be data trees consisting of trees of dicts and
    lists. They will be deeply compared by walking into the contents of dicts
    and lists; other items will be compared using the == operator.
    If the two structures differ in content, the failure message will indicate
    the location within the structures where the first difference is found.
    This may be helpful when comparing large structures.

    Mixed Sequence and Set types are supported. Mixed Mapping types are
    supported, but the order of the keys will not be considered in the
    comparison.

    Args:
      a: The first structure to compare.
      b: The second structure to compare.
      aname: Variable name to use for the first structure in assertion messages.
      bname: Variable name to use for the second structure.
      msg: Additional text to include in the failure message.
    """
    def assertJsonEqual(self, first, second, msg: Incomplete | None = None) -> None:
        """Asserts that the JSON objects defined in two strings are equal.

    A summary of the differences will be included in the failure message
    using assertSameStructure.

    Args:
      first: A string containing JSON to decode and compare to second.
      second: A string containing JSON to decode and compare to first.
      msg: Additional text to include in the failure message.
    """
    def fail(self, msg: Incomplete | None = None, user_msg: Incomplete | None = None) -> NoReturn:
        """Fail immediately with the given standard message and user message."""

def get_command_string(command):
    """Returns an escaped string that can be used as a shell command.

  Args:
    command: List or string representing the command to run.
  Returns:
    A string suitable for use as a shell command.
  """
def get_command_stderr(command, env: Incomplete | None = None, close_fds: bool = True):
    """Runs the given shell command and returns a tuple.

  Args:
    command: List or string representing the command to run.
    env: Dictionary of environment variable settings. If None, no environment
        variables will be set for the child process. This is to make tests
        more hermetic. NOTE: this behavior is different than the standard
        subprocess module.
    close_fds: Whether or not to close all open fd's in the child after forking.
        On Windows, this is ignored and close_fds is always False.

  Returns:
    Tuple of (exit status, text printed to stdout and stderr by the command).
  """
def print_python_version() -> None: ...
def main(*args: Text, **kwargs: Any) -> None:
    """Executes a set of Python unit tests.

  Usually this function is called without arguments, so the
  unittest.TestProgram instance will get created with the default settings,
  so it will run all test methods of all TestCase classes in the ``__main__``
  module.

  Args:
    *args: Positional arguments passed through to
        ``unittest.TestProgram.__init__``.
    **kwargs: Keyword arguments passed through to
        ``unittest.TestProgram.__init__``.
  """
def skipThisClass(reason: Text) -> Callable[[_T], _T]:
    '''Skip tests in the decorated TestCase, but not any of its subclasses.

  This decorator indicates that this class should skip all its tests, but not
  any of its subclasses. Useful for if you want to share testMethod or setUp
  implementations between a number of concrete testcase classes.

  Example usage, showing how you can share some common test methods between
  subclasses. In this example, only ``BaseTest`` will be marked as skipped, and
  not RealTest or SecondRealTest::

      @absltest.skipThisClass("Shared functionality")
      class BaseTest(absltest.TestCase):
        def test_simple_functionality(self):
          self.assertEqual(self.system_under_test.method(), 1)

      class RealTest(BaseTest):
        def setUp(self):
          super().setUp()
          self.system_under_test = MakeSystem(argument)

        def test_specific_behavior(self):
          ...

      class SecondRealTest(BaseTest):
        def setUp(self):
          super().setUp()
          self.system_under_test = MakeSystem(other_arguments)

        def test_other_behavior(self):
          ...

  Args:
    reason: The reason we have a skip in place. For instance: \'shared test
      methods\' or \'shared assertion methods\'.

  Returns:
    Decorator function that will cause a class to be skipped.
  '''

class TestLoader(unittest.TestLoader):
    """A test loader which supports common test features.

  Supported features include:
   * Banning untested methods with test-like names: methods attached to this
     testCase with names starting with `Test` are ignored by the test runner,
     and often represent mistakenly-omitted test cases. This loader will raise
     a TypeError when attempting to load a TestCase with such methods.
   * Randomization of test case execution order (optional).
  """
    def __init__(self, *args, **kwds) -> None: ...
    def getTestCaseNames(self, testCaseClass):
        """Validates and returns a (possibly randomized) list of test case names."""

def get_default_xml_output_filename() -> Text | None: ...
def run_tests(argv: MutableSequence[Text], args: Sequence[Any], kwargs: MutableMapping[Text, Any]) -> None:
    """Executes a set of Python unit tests.

  Most users should call absltest.main() instead of run_tests.

  Please note that run_tests should be called from app.run.
  Calling absltest.main() would ensure that.

  Please note that run_tests is allowed to make changes to kwargs.

  Args:
    argv: sys.argv with the command-line flags removed from the front, i.e. the
      argv with which :func:`app.run()<absl.app.run>` has called
      ``__main__.main``. It is passed to
      ``unittest.TestProgram.__init__(argv=)``, which does its own flag parsing.
      It is ignored if kwargs contains an argv entry.
    args: Positional arguments passed through to
      ``unittest.TestProgram.__init__``.
    kwargs: Keyword arguments passed through to
      ``unittest.TestProgram.__init__``.
  """
