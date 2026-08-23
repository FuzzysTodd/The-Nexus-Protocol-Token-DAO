from ._core import Process as Process
from _typeshed import Incomplete
from collections.abc import Generator

class PsNotAvailable(EnvironmentError): ...

def iter_process_parents(pid, max_depth: int = 10) -> Generator[Incomplete, None, None]:
    """Try to look up the process tree via the output of `ps`."""
