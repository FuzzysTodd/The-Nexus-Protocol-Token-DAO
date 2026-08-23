from . import assertions as assertions
from .. import exc as exc
from ..exc import SATestSuiteWarning as SATestSuiteWarning

def warn_test_suite(message) -> None: ...
def setup_filters() -> None:
    """hook for setting up warnings filters.

    SQLAlchemy-specific classes must only be here and not in pytest config,
    as we need to delay importing SQLAlchemy until conftest.py has been
    processed.

    NOTE: filters on subclasses of DeprecationWarning or
    PendingDeprecationWarning have no effect if added here, since pytest
    will add at each test the following filters
    ``always::PendingDeprecationWarning`` and ``always::DeprecationWarning``
    that will take precedence over any added here.

    """
def assert_warnings(fn, warning_msgs, regex: bool = False):
    """Assert that each of the given warnings are emitted by fn.

    Deprecated.  Please use assertions.expect_warnings().

    """
