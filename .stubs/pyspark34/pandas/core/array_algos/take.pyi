import numpy as np
from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, npt as npt
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike
from pandas.core.dtypes.cast import maybe_promote as maybe_promote
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_1d_only_ea_obj as is_1d_only_ea_obj
from pandas.core.dtypes.missing import na_value_for_dtype as na_value_for_dtype
from typing import overload

@overload
def take_nd(arr: np.ndarray, indexer, axis: AxisInt = ..., fill_value=..., allow_fill: bool = ...) -> np.ndarray: ...
@overload
def take_nd(arr: ExtensionArray, indexer, axis: AxisInt = ..., fill_value=..., allow_fill: bool = ...) -> ArrayLike: ...
def take_1d(arr: ArrayLike, indexer: npt.NDArray[np.intp], fill_value: Incomplete | None = None, allow_fill: bool = True, mask: npt.NDArray[np.bool_] | None = None) -> ArrayLike:
    """
    Specialized version for 1D arrays. Differences compared to `take_nd`:

    - Assumes input array has already been converted to numpy array / EA
    - Assumes indexer is already guaranteed to be intp dtype ndarray
    - Only works for 1D arrays

    To ensure the lowest possible overhead.

    Note: similarly to `take_nd`, this function assumes that the indexer is
    a valid(ated) indexer with no out of bound indices.

    Parameters
    ----------
    arr : np.ndarray or ExtensionArray
        Input array.
    indexer : ndarray
        1-D array of indices to take (validated indices, intp dtype).
    fill_value : any, default np.nan
        Fill value to replace -1 values with
    allow_fill : bool, default True
        If False, indexer is assumed to contain no -1 values so no filling
        will be done.  This short-circuits computation of a mask. Result is
        undefined if allow_fill == False and -1 is present in indexer.
    mask : np.ndarray, optional, default None
        If `allow_fill` is True, and the mask (where indexer == -1) is already
        known, it can be passed to avoid recomputation.
    """
def take_2d_multi(arr: np.ndarray, indexer: tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]], fill_value=...) -> np.ndarray:
    """
    Specialized Cython take which sets NaN values in one pass.
    """
