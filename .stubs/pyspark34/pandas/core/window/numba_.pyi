import numpy as np
from pandas._typing import Scalar as Scalar
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.util.numba_ import jit_user_function as jit_user_function
from typing import Callable

def generate_numba_apply_func(func: Callable[..., Scalar], nopython: bool, nogil: bool, parallel: bool):
    """
    Generate a numba jitted apply function specified by values from engine_kwargs.

    1. jit the user's function
    2. Return a rolling apply function with the jitted function inline

    Configurations specified in engine_kwargs apply to both the user's
    function _AND_ the rolling apply function.

    Parameters
    ----------
    func : function
        function to be applied to each window and will be JITed
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
def generate_numba_ewm_func(nopython: bool, nogil: bool, parallel: bool, com: float, adjust: bool, ignore_na: bool, deltas: tuple, normalize: bool):
    """
    Generate a numba jitted ewm mean or sum function specified by values
    from engine_kwargs.

    Parameters
    ----------
    nopython : bool
        nopython to be passed into numba.jit
    nogil : bool
        nogil to be passed into numba.jit
    parallel : bool
        parallel to be passed into numba.jit
    com : float
    adjust : bool
    ignore_na : bool
    deltas : tuple
    normalize : bool

    Returns
    -------
    Numba function
    """
def generate_numba_table_func(func: Callable[..., np.ndarray], nopython: bool, nogil: bool, parallel: bool):
    """
    Generate a numba jitted function to apply window calculations table-wise.

    Func will be passed a M window size x N number of columns array, and
    must return a 1 x N number of columns array. Func is intended to operate
    row-wise, but the result will be transposed for axis=1.

    1. jit the user's function
    2. Return a rolling apply function with the jitted function inline

    Parameters
    ----------
    func : function
        function to be applied to each window and will be JITed
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
def generate_manual_numpy_nan_agg_with_axis(nan_func): ...
def generate_numba_ewm_table_func(nopython: bool, nogil: bool, parallel: bool, com: float, adjust: bool, ignore_na: bool, deltas: tuple, normalize: bool):
    """
    Generate a numba jitted ewm mean or sum function applied table wise specified
    by values from engine_kwargs.

    Parameters
    ----------
    nopython : bool
        nopython to be passed into numba.jit
    nogil : bool
        nogil to be passed into numba.jit
    parallel : bool
        parallel to be passed into numba.jit
    com : float
    adjust : bool
    ignore_na : bool
    deltas : tuple
    normalize: bool

    Returns
    -------
    Numba function
    """
