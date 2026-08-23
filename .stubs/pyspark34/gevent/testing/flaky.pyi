import unittest
from . import sysinfo as sysinfo

class FlakyAssertionError(AssertionError):
    """Re-raised so that we know it's a known-flaky test."""
class FlakyTest(unittest.SkipTest):
    """
    A unittest exception that causes the test to be skipped when raised.

    Use this carefully, it is a code smell and indicates an undebugged problem.
    """
class FlakyTestRaceCondition(FlakyTest):
    """
    Use this when the flaky test is definitely caused by a race condition.
    """
class FlakyTestTimeout(FlakyTest):
    """
    Use this when the flaky test is definitely caused by an
    unexpected timeout.
    """
class FlakyTestCrashes(FlakyTest):
    """
    Use this when the test sometimes crashes.
    """

def reraiseFlakyTestRaceCondition() -> None: ...
reraiseFlakyTestTimeout = reraiseFlakyTestRaceCondition
reraiseFlakyTestRaceConditionLibuv = reraiseFlakyTestRaceCondition
reraiseFlakyTestTimeoutLibuv = reraiseFlakyTestRaceCondition
reraiseFlakyTestRaceConditionLibuv = reraiseFlakyTestRaceCondition
reraiseFlakyTestTimeoutLibuv = reraiseFlakyTestTimeout

def reraises_flaky_timeout(exc_kind=..., _func=...): ...
def reraises_flaky_race_condition(exc_kind=...): ...
