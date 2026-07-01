import numpy as np
from pandas._libs import lib as lib
from pandas._typing import AxisInt as AxisInt
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.generic import NDFrame as NDFrame

def preprocess_weights(obj: NDFrame, weights, axis: AxisInt) -> np.ndarray:
    """
    Process and validate the `weights` argument to `NDFrame.sample` and
    `.GroupBy.sample`.

    Returns `weights` as an ndarray[np.float64], validated except for normalizing
    weights (because that must be done groupwise in groupby sampling).
    """
def process_sampling_size(n: int | None, frac: float | None, replace: bool) -> int | None:
    """
    Process and validate the `n` and `frac` arguments to `NDFrame.sample` and
    `.GroupBy.sample`.

    Returns None if `frac` should be used (variable sampling sizes), otherwise returns
    the constant sampling size.
    """
def sample(obj_len: int, size: int, replace: bool, weights: np.ndarray | None, random_state: np.random.RandomState | np.random.Generator) -> np.ndarray:
    """
    Randomly sample `size` indices in `np.arange(obj_len)`

    Parameters
    ----------
    obj_len : int
        The length of the indices being considered
    size : int
        The number of values to choose
    replace : bool
        Allow or disallow sampling of the same row more than once.
    weights : np.ndarray[np.float64] or None
        If None, equal probability weighting, otherwise weights according
        to the vector normalized
    random_state: np.random.RandomState or np.random.Generator
        State used for the random sampling

    Returns
    -------
    np.ndarray[np.intp]
    """
