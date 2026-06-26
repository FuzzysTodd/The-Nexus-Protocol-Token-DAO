import contextlib
import unittest
from _typeshed import Incomplete
from numpy.testing import assert_almost_equal as assert_almost_equal, assert_approx_equal as assert_approx_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal, assert_array_less as assert_array_less

__all__ = ['assert_raises', 'assert_raises_regexp', 'assert_array_equal', 'assert_almost_equal', 'assert_array_almost_equal', 'assert_array_less', 'assert_approx_equal', 'assert_allclose', 'assert_run_python_script', 'SkipTest']

assert_raises: Incomplete
SkipTest = unittest.case.SkipTest
assert_raises_regexp = assert_raises_regex

class _IgnoreWarnings:
    """Improved and simplified Python warnings context manager and decorator.

    This class allows the user to ignore the warnings raised by a function.
    Copied from Python 2.7.5 and modified as required.

    Parameters
    ----------
    category : tuple of warning class, default=Warning
        The category to filter. By default, all the categories will be muted.

    """
    log: Incomplete
    category: Incomplete
    def __init__(self, category) -> None: ...
    def __call__(self, fn):
        """Decorator to catch and hide warnings without visual nesting."""
    def __enter__(self) -> None: ...
    def __exit__(self, *exc_info) -> None: ...

def assert_allclose(actual, desired, rtol: Incomplete | None = None, atol: float = 0.0, equal_nan: bool = True, err_msg: str = '', verbose: bool = True) -> None:
    """dtype-aware variant of numpy.testing.assert_allclose

    This variant introspects the least precise floating point dtype
    in the input argument and automatically sets the relative tolerance
    parameter to 1e-4 float32 and use 1e-7 otherwise (typically float64
    in scikit-learn).

    `atol` is always left to 0. by default. It should be adjusted manually
    to an assertion-specific value in case there are null values expected
    in `desired`.

    The aggregate tolerance is `atol + rtol * abs(desired)`.

    Parameters
    ----------
    actual : array_like
        Array obtained.
    desired : array_like
        Array desired.
    rtol : float, optional, default=None
        Relative tolerance.
        If None, it is set based on the provided arrays' dtypes.
    atol : float, optional, default=0.
        Absolute tolerance.
    equal_nan : bool, optional, default=True
        If True, NaNs will compare equal.
    err_msg : str, optional, default=''
        The error message to be printed in case of failure.
    verbose : bool, optional, default=True
        If True, the conflicting values are appended to the error message.

    Raises
    ------
    AssertionError
        If actual and desired are not equal up to specified precision.

    See Also
    --------
    numpy.testing.assert_allclose

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.utils._testing import assert_allclose
    >>> x = [1e-5, 1e-3, 1e-1]
    >>> y = np.arccos(np.cos(x))
    >>> assert_allclose(x, y, rtol=1e-5, atol=0)
    >>> a = np.full(shape=10, fill_value=1e-5, dtype=np.float32)
    >>> assert_allclose(a, 1e-5)
    """

class TempMemmap:
    """
    Parameters
    ----------
    data
    mmap_mode : str, default='r'
    """
    mmap_mode: Incomplete
    data: Incomplete
    def __init__(self, data, mmap_mode: str = 'r') -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def assert_run_python_script(source_code, timeout: int = 60) -> None:
    """Utility to check assertions in an independent Python subprocess.

    The script provided in the source code should return 0 and not print
    anything on stderr or stdout.

    This is a port from cloudpickle https://github.com/cloudpipe/cloudpickle

    Parameters
    ----------
    source_code : str
        The Python source code to execute.
    timeout : int, default=60
        Time in seconds before timeout.
    """

class _Raises(contextlib.AbstractContextManager):
    expected_exc_types: Incomplete
    matches: Incomplete
    may_pass: Incomplete
    err_msg: Incomplete
    raised_and_matched: bool
    def __init__(self, expected_exc_type, match, may_pass, err_msg) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, _: types.TracebackType | None): ...

class MinimalClassifier:
    """Minimal classifier implementation with inheriting from BaseEstimator.

    This estimator should be tested with:

    * `check_estimator` in `test_estimator_checks.py`;
    * within a `Pipeline` in `test_pipeline.py`;
    * within a `SearchCV` in `test_search.py`.
    """
    param: Incomplete
    def __init__(self, param: Incomplete | None = None) -> None: ...
    def get_params(self, deep: bool = True): ...
    def set_params(self, **params): ...
    def fit(self, X, y): ...
    def predict_proba(self, X): ...
    def predict(self, X): ...
    def score(self, X, y): ...

class MinimalRegressor:
    """Minimal regressor implementation with inheriting from BaseEstimator.

    This estimator should be tested with:

    * `check_estimator` in `test_estimator_checks.py`;
    * within a `Pipeline` in `test_pipeline.py`;
    * within a `SearchCV` in `test_search.py`.
    """
    param: Incomplete
    def __init__(self, param: Incomplete | None = None) -> None: ...
    def get_params(self, deep: bool = True): ...
    def set_params(self, **params): ...
    is_fitted_: bool
    def fit(self, X, y): ...
    def predict(self, X): ...
    def score(self, X, y): ...

class MinimalTransformer:
    """Minimal transformer implementation with inheriting from
    BaseEstimator.

    This estimator should be tested with:

    * `check_estimator` in `test_estimator_checks.py`;
    * within a `Pipeline` in `test_pipeline.py`;
    * within a `SearchCV` in `test_search.py`.
    """
    param: Incomplete
    def __init__(self, param: Incomplete | None = None) -> None: ...
    def get_params(self, deep: bool = True): ...
    def set_params(self, **params): ...
    is_fitted_: bool
    def fit(self, X, y: Incomplete | None = None): ...
    def transform(self, X, y: Incomplete | None = None): ...
    def fit_transform(self, X, y: Incomplete | None = None): ...
