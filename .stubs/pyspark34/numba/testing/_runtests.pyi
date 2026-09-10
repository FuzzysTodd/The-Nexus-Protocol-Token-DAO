from _typeshed import Incomplete

def main(*argv, **kwds):
    """keyword arguments are accepted for backward compatibility only.
    See `numba.testing.run_tests()` documentation for details."""

class _FailedFirstRunner:
    """
    Test Runner to handle the failed-first (--failed-first) option.
    """
    cache_filename: str
    last_failed: Incomplete
    def __init__(self, last_failed: bool = False) -> None: ...
    def main(self, argv, kwds): ...
    def save_failed_tests(self, result, all_tests) -> None: ...
    def find_last_failed(self, argv): ...
