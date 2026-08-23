import xml.dom.minidom
from _typeshed import Incomplete
from unittest import TextTestResult, TextTestRunner

class XMLDocument(xml.dom.minidom.Document):
    def createCDATAOrText(self, data): ...

class _TestInfo:
    """This class is used to keep useful information about the execution of a
    test method.
    """
    SUCCESS: Incomplete
    FAILURE: Incomplete
    ERROR: Incomplete
    test_result: Incomplete
    test_method: Incomplete
    outcome: Incomplete
    err: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    def __init__(self, test_result, test_method, outcome=..., err: Incomplete | None = None) -> None:
        """Create a new instance of _TestInfo."""
    def get_elapsed_time(self):
        """Return the time that shows how long the test method took to
        execute.
        """
    def get_description(self):
        """Return a text representation of the test method."""
    def get_error_info(self):
        """Return a text representation of an exception thrown by a test
        method.
        """

class _XMLTestResult(TextTestResult):
    """A test result class that can express test results in a XML report.

    Used by XMLTestRunner.
    """
    successes: Incomplete
    callback: Incomplete
    elapsed_times: Incomplete
    output_patched: bool
    def __init__(self, stream=..., descriptions: int = 1, verbosity: int = 1, elapsed_times: bool = True) -> None:
        """Create a new instance of _XMLTestResult."""
    start_time: Incomplete
    def startTest(self, test) -> None:
        """Called before execute each test method."""
    stop_time: Incomplete
    def stopTest(self, test) -> None:
        """Called after execute each test method."""
    def addSuccess(self, test) -> None:
        """Called when a test executes successfully."""
    def addFailure(self, test, err) -> None:
        """Called when a test method fails."""
    def addError(self, test, err) -> None:
        """Called when a test method raises an error."""
    def printErrorList(self, flavour, errors) -> None:
        """Write some information about the FAIL or ERROR to the stream."""
    def generate_reports(self, test_runner) -> None:
        """Generates the XML reports to a given XMLTestRunner object."""

class XMLTestRunner(TextTestRunner):
    """A test runner class that outputs the results in JUnit like XML files.
    """
    output: Incomplete
    elapsed_times: Incomplete
    def __init__(self, output: str = '.', stream: Incomplete | None = None, descriptions: bool = True, verbose: bool = False, elapsed_times: bool = True) -> None:
        """Create a new instance of XMLTestRunner."""
    def run(self, test):
        """Run the given test case or test suite."""
