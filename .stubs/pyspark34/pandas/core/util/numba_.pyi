from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.errors import NumbaUtilError as NumbaUtilError
from typing import Callable

GLOBAL_USE_NUMBA: bool

def maybe_use_numba(engine: str | None) -> bool:
    """Signal whether to use numba routines."""
def set_use_numba(enable: bool = False) -> None: ...
def get_jit_arguments(engine_kwargs: dict[str, bool] | None = None, kwargs: dict | None = None) -> dict[str, bool]:
    """
    Return arguments to pass to numba.JIT, falling back on pandas default JIT settings.

    Parameters
    ----------
    engine_kwargs : dict, default None
        user passed keyword arguments for numba.JIT
    kwargs : dict, default None
        user passed keyword arguments to pass into the JITed function

    Returns
    -------
    dict[str, bool]
        nopython, nogil, parallel

    Raises
    ------
    NumbaUtilError
    """
def jit_user_function(func: Callable, nopython: bool, nogil: bool, parallel: bool) -> Callable:
    """
    JIT the user's function given the configurable arguments.

    Parameters
    ----------
    func : function
        user defined function
    nopython : bool
        nopython parameter for numba.JIT
    nogil : bool
        nogil parameter for numba.JIT
    parallel : bool
        parallel parameter for numba.JIT

    Returns
    -------
    function
        Numba JITed function
    """
