from _typeshed import Incomplete
from debugpy import launcher as launcher
from debugpy.common import log as log

class CaptureOutput:
    '''Captures output from the specified file descriptor, and tees it into another
    file descriptor while generating DAP "output" events for it.
    '''
    instances: Incomplete
    category: Incomplete
    def __init__(self, whose, category, fd, stream) -> None: ...
    def __del__(self) -> None: ...

def wait_for_remaining_output() -> None:
    """Waits for all remaining output to be captured and propagated."""
