from .main import NumbaTestProgram as NumbaTestProgram, SerialSuite as SerialSuite, make_tag_decorator as make_tag_decorator
from _typeshed import Incomplete
from numba.core import config as config

def load_testsuite(loader, dir):
    """Find tests in 'dir'."""
def run_tests(argv: Incomplete | None = None, defaultTest: Incomplete | None = None, topleveldir: Incomplete | None = None, xmloutput: Incomplete | None = None, verbosity: int = 1, nomultiproc: bool = False):
    """
    args
    ----
    - xmloutput [str or None]
        Path of XML output directory (optional)
    - verbosity [int]
        Verbosity level of tests output

    Returns the TestResult object after running the test *suite*.
    """
