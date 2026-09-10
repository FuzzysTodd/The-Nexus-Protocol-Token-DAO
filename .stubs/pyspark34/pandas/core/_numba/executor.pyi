from pandas._typing import Scalar as Scalar
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from typing import Callable

def generate_shared_aggregator(func: Callable[..., Scalar], nopython: bool, nogil: bool, parallel: bool):
    """
    Generate a Numba function that loops over the columns 2D object and applies
    a 1D numba kernel over each column.

    Parameters
    ----------
    func : function
        aggregation function to be applied to each column
    nopython : bool
        nopython to be passed into numba.jit
    nogil : bool
        nogil to be passed into numba.jit
    parallel : bool
        parallel to be passed into numba.jit

    Returns
    -------
    Numba function
    """
