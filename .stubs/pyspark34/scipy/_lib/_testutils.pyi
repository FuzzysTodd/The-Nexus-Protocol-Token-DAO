from _typeshed import Incomplete

__all__ = ['PytestTester', 'check_free_memory', '_TestPythranFunc']

class FPUModeChangeWarning(RuntimeWarning):
    """Warning about FPU mode change"""

class PytestTester:
    """
    Pytest test runner entry point.
    """
    module_name: Incomplete
    def __init__(self, module_name) -> None: ...
    def __call__(self, label: str = 'fast', verbose: int = 1, extra_argv: Incomplete | None = None, doctests: bool = False, coverage: bool = False, tests: Incomplete | None = None, parallel: Incomplete | None = None): ...

class _TestPythranFunc:
    """
    These are situations that can be tested in our pythran tests:
    - A function with multiple array arguments and then
      other positional and keyword arguments.
    - A function with array-like keywords (e.g. `def somefunc(x0, x1=None)`.
    Note: list/tuple input is not yet tested!

    `self.arguments`: A dictionary which key is the index of the argument,
                      value is tuple(array value, all supported dtypes)
    `self.partialfunc`: A function used to freeze some non-array argument
                        that of no interests in the original function
    """
    ALL_INTEGER: Incomplete
    ALL_FLOAT: Incomplete
    ALL_COMPLEX: Incomplete
    arguments: Incomplete
    partialfunc: Incomplete
    expected: Incomplete
    def setup_method(self) -> None: ...
    def get_optional_args(self, func): ...
    def get_max_dtype_list_length(self): ...
    def get_dtype(self, dtype_list, dtype_idx): ...
    def test_all_dtypes(self) -> None: ...
    def test_views(self) -> None: ...
    def test_strided(self) -> None: ...

def check_free_memory(free_mb) -> None:
    """
    Check *free_mb* of memory is available, otherwise do pytest.skip
    """
