import threading
from _typeshed import Incomplete

def sleep(seconds: float) -> None:
    """
    Sleep strategy that delays execution for a given number of seconds.

    This is the default strategy, and may be mocked out for unit testing.
    """

class sleep_using_event:
    """Sleep strategy that waits on an event to be set."""
    event: Incomplete
    def __init__(self, event: threading.Event) -> None: ...
    def __call__(self, timeout: float | None) -> None: ...
