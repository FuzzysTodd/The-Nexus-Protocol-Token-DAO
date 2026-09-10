import numpy as np
from _typeshed import Incomplete
from typing import NamedTuple, TypeVar

IntNumber = int | np.integer
DecimalNumber = float | np.floating | np.integer
SeedType: Incomplete
GeneratorType = TypeVar('GeneratorType', bound=np.random.Generator | np.random.RandomState)

class Generator: ...

def prod(iterable):
    """
    Product of a sequence of numbers.

    Faster than np.prod for short lists like array shapes, and does
    not overflow if using Python integers.
    """
def float_factorial(n: int) -> float:
    """Compute the factorial and return as a float

    Returns infinity when result is too large for a double
    """
def check_random_state(seed):
    """Turn `seed` into a `np.random.RandomState` instance.

    Parameters
    ----------
    seed : {None, int, `numpy.random.Generator`, `numpy.random.RandomState`}, optional
        If `seed` is None (or `np.random`), the `numpy.random.RandomState`
        singleton is used.
        If `seed` is an int, a new ``RandomState`` instance is used,
        seeded with `seed`.
        If `seed` is already a ``Generator`` or ``RandomState`` instance then
        that instance is used.

    Returns
    -------
    seed : {`numpy.random.Generator`, `numpy.random.RandomState`}
        Random number generator.

    """

class FullArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    varkw: Incomplete
    defaults: Incomplete
    kwonlyargs: Incomplete
    kwonlydefaults: Incomplete
    annotations: Incomplete

def getfullargspec_no_self(func):
    """inspect.getfullargspec replacement using inspect.signature.

    If func is a bound method, do not list the 'self' parameter.

    Parameters
    ----------
    func : callable
        A callable to inspect

    Returns
    -------
    fullargspec : FullArgSpec(args, varargs, varkw, defaults, kwonlyargs,
                              kwonlydefaults, annotations)

        NOTE: if the first argument of `func` is self, it is *not*, I repeat
        *not*, included in fullargspec.args.
        This is done for consistency between inspect.getargspec() under
        Python 2.x, and inspect.signature() under Python 3.x.

    """

class _FunctionWrapper:
    """
    Object to wrap user's function, allowing picklability
    """
    f: Incomplete
    args: Incomplete
    def __init__(self, f, args) -> None: ...
    def __call__(self, x): ...

class MapWrapper:
    """
    Parallelisation wrapper for working with map-like callables, such as
    `multiprocessing.Pool.map`.

    Parameters
    ----------
    pool : int or map-like callable
        If `pool` is an integer, then it specifies the number of threads to
        use for parallelization. If ``int(pool) == 1``, then no parallel
        processing is used and the map builtin is used.
        If ``pool == -1``, then the pool will utilize all available CPUs.
        If `pool` is a map-like callable that follows the same
        calling sequence as the built-in map function, then this callable is
        used for parallelization.
    """
    pool: Incomplete
    def __init__(self, pool: int = 1) -> None: ...
    def __enter__(self): ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
    def close(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __call__(self, func, iterable): ...

def rng_integers(gen, low, high: Incomplete | None = None, size: Incomplete | None = None, dtype: str = 'int64', endpoint: bool = False):
    '''
    Return random integers from low (inclusive) to high (exclusive), or if
    endpoint=True, low (inclusive) to high (inclusive). Replaces
    `RandomState.randint` (with endpoint=False) and
    `RandomState.random_integers` (with endpoint=True).

    Return random integers from the "discrete uniform" distribution of the
    specified dtype. If high is None (the default), then results are from
    0 to low.

    Parameters
    ----------
    gen : {None, np.random.RandomState, np.random.Generator}
        Random number generator. If None, then the np.random.RandomState
        singleton is used.
    low : int or array-like of ints
        Lowest (signed) integers to be drawn from the distribution (unless
        high=None, in which case this parameter is 0 and this value is used
        for high).
    high : int or array-like of ints
        If provided, one above the largest (signed) integer to be drawn from
        the distribution (see above for behavior if high=None). If array-like,
        must contain integer values.
    size : array-like of ints, optional
        Output shape. If the given shape is, e.g., (m, n, k), then m * n * k
        samples are drawn. Default is None, in which case a single value is
        returned.
    dtype : {str, dtype}, optional
        Desired dtype of the result. All dtypes are determined by their name,
        i.e., \'int64\', \'int\', etc, so byteorder is not available and a specific
        precision may have different C types depending on the platform.
        The default value is np.int_.
    endpoint : bool, optional
        If True, sample from the interval [low, high] instead of the default
        [low, high) Defaults to False.

    Returns
    -------
    out: int or ndarray of ints
        size-shaped array of random integers from the appropriate distribution,
        or a single such random int if size not provided.
    '''
