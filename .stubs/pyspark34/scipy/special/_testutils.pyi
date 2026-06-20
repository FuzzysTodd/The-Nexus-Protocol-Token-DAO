from _typeshed import Incomplete

__all__ = ['with_special_errors', 'assert_func_equal', 'FuncData']

class MissingModule:
    name: Incomplete
    def __init__(self, name) -> None: ...

def with_special_errors(func):
    """
    Enable special function errors (such as underflow, overflow,
    loss of precision, etc.)
    """
def assert_func_equal(func, results, points, rtol: Incomplete | None = None, atol: Incomplete | None = None, param_filter: Incomplete | None = None, knownfailure: Incomplete | None = None, vectorized: bool = True, dtype: Incomplete | None = None, nan_ok: bool = False, ignore_inf_sign: bool = False, distinguish_nan_and_inf: bool = True) -> None: ...

class FuncData:
    """
    Data set for checking a special function.

    Parameters
    ----------
    func : function
        Function to test
    data : numpy array
        columnar data to use for testing
    param_columns : int or tuple of ints
        Columns indices in which the parameters to `func` lie.
        Can be imaginary integers to indicate that the parameter
        should be cast to complex.
    result_columns : int or tuple of ints, optional
        Column indices for expected results from `func`.
    result_func : callable, optional
        Function to call to obtain results.
    rtol : float, optional
        Required relative tolerance. Default is 5*eps.
    atol : float, optional
        Required absolute tolerance. Default is 5*tiny.
    param_filter : function, or tuple of functions/Nones, optional
        Filter functions to exclude some parameter ranges.
        If omitted, no filtering is done.
    knownfailure : str, optional
        Known failure error message to raise when the test is run.
        If omitted, no exception is raised.
    nan_ok : bool, optional
        If nan is always an accepted result.
    vectorized : bool, optional
        Whether all functions passed in are vectorized.
    ignore_inf_sign : bool, optional
        Whether to ignore signs of infinities.
        (Doesn't matter for complex-valued functions.)
    distinguish_nan_and_inf : bool, optional
        If True, treat numbers which contain nans or infs as
        equal. Sets ignore_inf_sign to be True.

    """
    func: Incomplete
    data: Incomplete
    dataname: Incomplete
    param_columns: Incomplete
    result_columns: Incomplete
    result_func: Incomplete
    rtol: Incomplete
    atol: Incomplete
    param_filter: Incomplete
    knownfailure: Incomplete
    nan_ok: Incomplete
    vectorized: Incomplete
    ignore_inf_sign: Incomplete
    distinguish_nan_and_inf: Incomplete
    def __init__(self, func, data, param_columns, result_columns: Incomplete | None = None, result_func: Incomplete | None = None, rtol: Incomplete | None = None, atol: Incomplete | None = None, param_filter: Incomplete | None = None, knownfailure: Incomplete | None = None, dataname: Incomplete | None = None, nan_ok: bool = False, vectorized: bool = True, ignore_inf_sign: bool = False, distinguish_nan_and_inf: bool = True) -> None: ...
    def get_tolerances(self, dtype): ...
    def check(self, data: Incomplete | None = None, dtype: Incomplete | None = None, dtypes: Incomplete | None = None):
        """Check the special function against the data."""
