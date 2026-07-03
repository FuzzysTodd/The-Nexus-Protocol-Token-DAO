import numpy as np
import pandas as pd
import pandas.util.testing as testing
from _typeshed import Incomplete
from pandas._testing import makeDataFrame as make_dataframe
from pandas.core.common import is_numeric_dtype as is_numeric_dtype
from pandas.tseries import frequencies as frequencies
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly, deprecate_kwarg as deprecate_kwarg

__all__ = ['assert_frame_equal', 'assert_index_equal', 'assert_series_equal', 'data_klasses', 'frequencies', 'is_numeric_dtype', 'testing', 'cache_readonly', 'deprecate_kwarg', 'Appender', 'Substitution', 'is_int_index', 'is_float_index', 'make_dataframe', 'to_numpy', 'PD_LT_1_0_0', 'get_cached_func', 'get_cached_doc', 'call_cached_func', 'PD_LT_1_4', 'PD_LT_2']

PD_LT_1_0_0: Incomplete
PD_LT_1_4: Incomplete
PD_LT_2: Incomplete
data_klasses: Incomplete
assert_frame_equal: Incomplete
assert_index_equal: Incomplete
assert_series_equal: Incomplete

def is_int_index(index: pd.Index) -> bool:
    """
    Check if an index is integral

    Parameters
    ----------
    index : pd.Index
        Any numeric index

    Returns
    -------
    bool
        True if is an index with a standard integral type
    """
def is_float_index(index: pd.Index) -> bool:
    """
    Check if an index is floating

    Parameters
    ----------
    index : pd.Index
        Any numeric index

    Returns
    -------
    bool
        True if an index with a standard numpy floating dtype
    """
def to_numpy(po: pd.DataFrame) -> np.ndarray:
    """
    Workaround legacy pandas lacking to_numpy

    Parameters
    ----------
    po : Pandas obkect

    Returns
    -------
    ndarray
        A numpy array
    """
def get_cached_func(cached_prop): ...
def call_cached_func(cached_prop, *args, **kwargs): ...
def get_cached_doc(cached_prop) -> str | None: ...
