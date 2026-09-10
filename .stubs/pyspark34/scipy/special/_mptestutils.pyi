from _typeshed import Incomplete
from scipy.special._testutils import assert_func_equal as assert_func_equal

class Arg:
    """Generate a set of numbers on the real axis, concentrating on
    'interesting' regions and covering all orders of magnitude.

    """
    def __init__(self, a=..., b=..., inclusive_a: bool = True, inclusive_b: bool = True) -> None: ...
    def values(self, n):
        """Return an array containing n numbers."""

class FixedArg:
    def __init__(self, values) -> None: ...
    def values(self, n): ...

class ComplexArg:
    real: Incomplete
    imag: Incomplete
    def __init__(self, a=..., b=...) -> None: ...
    def values(self, n): ...

class IntArg:
    a: Incomplete
    b: Incomplete
    def __init__(self, a: int = -1000, b: int = 1000) -> None: ...
    def values(self, n): ...

def get_args(argspec, n): ...

class MpmathData:
    scipy_func: Incomplete
    mpmath_func: Incomplete
    arg_spec: Incomplete
    dps: Incomplete
    prec: Incomplete
    n: Incomplete
    rtol: Incomplete
    atol: Incomplete
    ignore_inf_sign: Incomplete
    nan_ok: Incomplete
    is_complex: Incomplete
    distinguish_nan_and_inf: Incomplete
    name: Incomplete
    param_filter: Incomplete
    def __init__(self, scipy_func, mpmath_func, arg_spec, name: Incomplete | None = None, dps: Incomplete | None = None, prec: Incomplete | None = None, n: Incomplete | None = None, rtol: float = 1e-07, atol: float = 1e-300, ignore_inf_sign: bool = False, distinguish_nan_and_inf: bool = True, nan_ok: bool = True, param_filter: Incomplete | None = None) -> None: ...
    def check(self): ...

def assert_mpmath_equal(*a, **kw) -> None: ...
def nonfunctional_tooslow(func): ...
def mpf2float(x):
    '''
    Convert an mpf to the nearest floating point number. Just using
    float directly doesn\'t work because of results like this:

    with mp.workdps(50):
        float(mpf("0.99999999999999999")) = 0.9999999999999999

    '''
def mpc2complex(x): ...
def trace_args(func): ...

POSIX: Incomplete

class TimeoutError(Exception): ...

def time_limited(timeout: float = 0.5, return_val=..., use_sigalrm: bool = True):
    """
    Decorator for setting a timeout for pure-Python functions.

    If the function does not return within `timeout` seconds, the
    value `return_val` is returned instead.

    On POSIX this uses SIGALRM by default. On non-POSIX, settrace is
    used. Do not use this with threads: the SIGALRM implementation
    does probably not work well. The settrace implementation only
    traces the current thread.

    The settrace implementation slows down execution speed. Slowdown
    by a factor around 10 is probably typical.
    """
def exception_to_nan(func):
    """Decorate function to return nan if it raises an exception"""
def inf_to_nan(func):
    """Decorate function to return nan if it returns inf"""
def mp_assert_allclose(res, std, atol: int = 0, rtol: float = 1e-17) -> None:
    """
    Compare lists of mpmath.mpf's or mpmath.mpc's directly so that it
    can be done to higher precision than double.
    """
