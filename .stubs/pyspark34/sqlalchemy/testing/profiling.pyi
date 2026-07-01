from . import config as config
from ..util import has_compiled_ext as has_compiled_ext
from .util import gc_collect as gc_collect
from _typeshed import Incomplete
from collections.abc import Generator

class ProfileStatsFile:
    """Store per-platform/fn profiling results in a file.

    There was no json module available when this was written, but now
    the file format which is very deterministically line oriented is kind of
    handy in any case for diffs and merges.

    """
    force_write: Incomplete
    write: Incomplete
    fname: Incomplete
    short_fname: Incomplete
    data: Incomplete
    dump: Incomplete
    sort: Incomplete
    def __init__(self, filename, sort: str = 'cumulative', dump: Incomplete | None = None) -> None: ...
    @property
    def platform_key(self): ...
    def has_stats(self): ...
    def result(self, callcount): ...
    def reset_count(self) -> None: ...
    def replace(self, callcount) -> None: ...

def function_call_count(variance: float = 0.05, times: int = 1, warmup: int = 0):
    """Assert a target for a test case's function call count.

    The main purpose of this assertion is to detect changes in
    callcounts for various functions - the actual number is not as important.
    Callcounts are stored in a file keyed to Python version and OS platform
    information.  This file is generated automatically for new tests,
    and versioned so that unexpected changes in callcounts will be detected.

    """
def count_functions(variance: float = 0.05) -> Generator[None, None, None]: ...
