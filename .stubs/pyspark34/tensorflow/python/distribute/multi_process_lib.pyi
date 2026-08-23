import multiprocessing
from _typeshed import Incomplete
from tensorflow.python.eager import test as test

def is_oss():
    """Returns whether the test is run under OSS."""

class _AbslProcess:
    """A process that runs using absl.app.run."""
    run: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AbslForkServerProcess(_AbslProcess, multiprocessing.context.ForkServerProcess):
    """An absl-compatible Forkserver process.

    Note: Forkserver is not available in windows.
    """

class AbslForkServerContext(multiprocessing.context.ForkServerContext):
    Process = AbslForkServerProcess
Process = multiprocessing.Process

class Process:
    """A process that skips test (until windows is supported)."""
    def __init__(self, *args, **kwargs) -> None: ...

def test_main() -> None:
    """Main function to be called within `__main__` of a test file."""
def initialized():
    """Returns whether the module is initialized."""
