import collections
import unittest
from .loader import TestLoader as TestLoader
from _typeshed import Incomplete
from collections.abc import Generator
from numba.core import config as config
from unittest import loader as loader, runner, suite as suite

def make_tag_decorator(known_tags):
    """
    Create a decorator allowing tests to be tagged with the *known_tags*.
    """
def cuda_sensitive_mtime(x):
    """
    Return a key for sorting tests bases on mtime and test name. For CUDA
    tests, interleaving tests from different classes is dangerous as the CUDA
    context might get reset unexpectedly between methods of a class, so for
    CUDA tests the key prioritises the test module and class ahead of the
    mtime.
    """
def parse_slice(useslice):
    '''Parses the argument string "useslice" as a shard index and number and
    returns a function that filters on those arguments. i.e. input
    useslice="1:3" leads to output something like `lambda x: zlib.crc32(x) % 3
    == 1`.
    '''

class TestLister:
    """Simply list available tests rather than running them."""
    useslice: Incomplete
    def __init__(self, useslice) -> None: ...
    def run(self, test): ...

class SerialSuite(unittest.TestSuite):
    """A simple marker to make sure tests in this suite are run serially.

    Note: As the suite is going through internals of unittest,
          it may get unpacked and stuffed into a plain TestSuite.
          We need to set an attribute on the TestCase objects to
          remember they should not be run in parallel.
    """
    def addTest(self, test) -> None: ...

class BasicTestRunner(runner.TextTestRunner):
    useslice: Incomplete
    def __init__(self, useslice, **kwargs) -> None: ...
    def run(self, test): ...

class NumbaTestProgram(unittest.main):
    """
    A TestProgram subclass adding the following options:
    * a -R option to enable reference leak detection
    * a --profile option to enable profiling of the test run
    * a -m option for parallel execution
    * a -l option to (only) list tests

    Currently the options are only added in 3.4+.
    """
    refleak: bool
    profile: bool
    multiprocess: bool
    useslice: Incomplete
    list: bool
    tags: Incomplete
    exclude_tags: Incomplete
    random_select: Incomplete
    random_seed: int
    nomultiproc: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    testNames: Incomplete
    test: Incomplete
    buffer: bool
    def parseArgs(self, argv) -> None: ...
    testRunner: Incomplete
    def runTests(self) -> None: ...

class ReferenceLeakError(RuntimeError): ...

class IntPool(collections.defaultdict):
    def __missing__(self, key): ...

class RefleakTestResult(runner.TextTestResult):
    warmup: int
    repetitions: int
    def addSuccess(self, test): ...

class RefleakTestRunner(runner.TextTestRunner):
    resultclass = RefleakTestResult

class ParallelTestResult(runner.TextTestResult):
    """
    A TestResult able to inject results from other results.
    """
    def add_results(self, result) -> None:
        """
        Add the results from the other *result* to this result.
        """

class _MinimalResult:
    """
    A minimal, picklable TestResult-alike object.
    """
    def fixup_case(self, case) -> None:
        """
        Remove any unpicklable attributes from TestCase instance *case*.
        """
    test_id: Incomplete
    def __init__(self, original_result, test_id: Incomplete | None = None) -> None: ...

class _FakeStringIO:
    """
    A trivial picklable StringIO-alike for Python 2.
    """
    def __init__(self, value) -> None: ...
    def getvalue(self): ...

class _MinimalRunner:
    """
    A minimal picklable object able to instantiate a runner in a
    child process and run a test case with it.
    """
    runner_cls: Incomplete
    runner_args: Incomplete
    def __init__(self, runner_cls, runner_args) -> None: ...
    def __call__(self, test): ...
    def cleanup_object(self, test) -> Generator[Incomplete, None, None]:
        """
        A context manager which cleans up unwanted attributes on a test case
        (or any other object).
        """

class ParallelTestRunner(runner.TextTestRunner):
    """
    A test runner which delegates the actual running to a pool of child
    processes.
    """
    resultclass = ParallelTestResult
    timeout: Incomplete
    runner_cls: Incomplete
    nprocs: Incomplete
    useslice: Incomplete
    runner_args: Incomplete
    def __init__(self, runner_cls, nprocs, useslice, **kwargs) -> None: ...
    def run(self, test): ...
