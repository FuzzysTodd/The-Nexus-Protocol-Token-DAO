import unittest
from _typeshed import Incomplete
from absl.testing import _pretty_print_reporter

class _TestCaseResult:
    '''Private helper for _TextAndXMLTestResult that represents a test result.

  Attributes:
    test: A TestCase instance of an individual test method.
    name: The name of the individual test method.
    full_class_name: The full name of the test class.
    run_time: The duration (in seconds) it took to run the test.
    start_time: Epoch relative timestamp of when test started (in seconds)
    errors: A list of error 4-tuples. Error tuple entries are
        1) a string identifier of either "failure" or "error"
        2) an exception_type
        3) an exception_message
        4) a string version of a sys.exc_info()-style tuple of values
           (\'error\', err[0], err[1], self._exc_info_to_string(err))
           If the length of errors is 0, then the test is either passed or
           skipped.
    skip_reason: A string explaining why the test was skipped.
  '''
    run_time: int
    start_time: int
    skip_reason: Incomplete
    errors: Incomplete
    test: Incomplete
    name: Incomplete
    full_class_name: Incomplete
    def __init__(self, test) -> None: ...
    def set_run_time(self, time_in_secs) -> None: ...
    def set_start_time(self, time_in_secs) -> None: ...
    def print_xml_summary(self, stream) -> None:
        """Prints an XML Summary of a TestCase.

    Status and result are populated as per JUnit XML test result reporter.
    A test that has been skipped will always have a skip reason,
    as every skip method in Python's unittest requires the reason arg to be
    passed.

    Args:
      stream: output stream to write test report XML to
    """

class _TestSuiteResult:
    """Private helper for _TextAndXMLTestResult."""
    suites: Incomplete
    failure_counts: Incomplete
    error_counts: Incomplete
    overall_start_time: int
    overall_end_time: int
    def __init__(self) -> None: ...
    def add_test_case_result(self, test_case_result) -> None: ...
    def print_xml_summary(self, stream): ...
    def set_end_time(self, timestamp_in_secs) -> None:
        """Sets the start timestamp of this test suite.

    Args:
      timestamp_in_secs: timestamp in seconds since epoch
    """
    def set_start_time(self, timestamp_in_secs) -> None:
        """Sets the end timestamp of this test suite.

    Args:
      timestamp_in_secs: timestamp in seconds since epoch
    """

class _TextAndXMLTestResult(_pretty_print_reporter.TextTestResult):
    """Private TestResult class that produces both formatted text results and XML.

  Used by TextAndXMLTestRunner.
  """
    xml_stream: Incomplete
    pending_test_case_results: Incomplete
    suite: Incomplete
    time_getter: Incomplete
    def __init__(self, xml_stream, stream, descriptions, verbosity, time_getter=..., testsuites_properties: Incomplete | None = None) -> None: ...
    start_time: Incomplete
    def startTest(self, test) -> None: ...
    def stopTest(self, test) -> None: ...
    def startTestRun(self) -> None: ...
    def stopTestRun(self) -> None: ...
    def add_pending_test_case_result(self, test, error_summary: Incomplete | None = None, skip_reason: Incomplete | None = None) -> None:
        '''Adds result information to a test case result which may still be running.

    If a result entry for the test already exists, add_pending_test_case_result
    will add error summary tuples and/or overwrite skip_reason for the result.
    If it does not yet exist, a result entry will be created.
    Note that a test result is considered to have been run and passed
    only if there are no errors or skip_reason.

    Args:
      test: A test method as defined by unittest
      error_summary: A 4-tuple with the following entries:
          1) a string identifier of either "failure" or "error"
          2) an exception_type
          3) an exception_message
          4) a string version of a sys.exc_info()-style tuple of values
             (\'error\', err[0], err[1], self._exc_info_to_string(err))
             If the length of errors is 0, then the test is either passed or
             skipped.
      skip_reason: a string explaining why the test was skipped
    '''
    def delete_pending_test_case_result(self, test) -> None: ...
    def get_pending_test_case_result(self, test): ...
    def addSuccess(self, test) -> None: ...
    def addError(self, test, err) -> None: ...
    def addFailure(self, test, err) -> None: ...
    def addSkip(self, test, reason) -> None: ...
    def addExpectedFailure(self, test, err) -> None: ...
    def addUnexpectedSuccess(self, test) -> None: ...
    def addSubTest(self, test, subtest, err) -> None: ...
    def printErrors(self) -> None: ...

class TextAndXMLTestRunner(unittest.TextTestRunner):
    """A test runner that produces both formatted text results and XML.

  It prints out the names of tests as they are run, errors as they
  occur, and a summary of the results at the end of the test run.
  """
    def __init__(self, xml_stream: Incomplete | None = None, *args, **kwargs) -> None:
        """Initialize a TextAndXMLTestRunner.

    Args:
      xml_stream: file-like or None; XML-formatted test results are output
          via this object's write() method.  If None (the default), the
          new instance behaves as described in the set_default_xml_stream method
          documentation below.
      *args: passed unmodified to unittest.TextTestRunner.__init__.
      **kwargs: passed unmodified to unittest.TextTestRunner.__init__.
    """
    @classmethod
    def set_default_xml_stream(cls, xml_stream) -> None:
        """Sets the default XML stream for the class.

    Args:
      xml_stream: file-like or None; used for instances when xml_stream is None
          or not passed to their constructors.  If None is passed, instances
          created with xml_stream=None will act as ordinary TextTestRunner
          instances; this is the default state before any calls to this method
          have been made.
    """
    @classmethod
    def set_testsuites_property(cls, key, value) -> None: ...
