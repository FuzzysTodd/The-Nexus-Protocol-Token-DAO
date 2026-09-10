import numpy as np
from pandas._typing import NumpyIndexT as NumpyIndexT
from pandas.core.dtypes.common import is_list_like as is_list_like

def cartesian_product(X) -> list[np.ndarray]:
    """
    Numpy version of itertools.product.
    Sometimes faster (for large inputs)...

    Parameters
    ----------
    X : list-like of list-likes

    Returns
    -------
    product : list of ndarrays

    Examples
    --------
    >>> cartesian_product([list('ABC'), [1, 2]])
    [array(['A', 'A', 'B', 'B', 'C', 'C'], dtype='<U1'), array([1, 2, 1, 2, 1, 2])]

    See Also
    --------
    itertools.product : Cartesian product of input iterables.  Equivalent to
        nested for-loops.
    """
def tile_compat(arr: NumpyIndexT, num: int) -> NumpyIndexT:
    """
    Index compat for np.tile.

    Notes
    -----
    Does not support multi-dimensional `num`.
    """
