import numpy as np
from _typeshed import Incomplete
from pandas import Index as Index
from pandas._libs import NaT as NaT, algos as algos, lib as lib
from pandas._typing import ArrayLike as ArrayLike, Axis as Axis, AxisInt as AxisInt, F as F, npt as npt
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.cast import infer_dtype_from as infer_dtype_from
from pandas.core.dtypes.common import is_array_like as is_array_like, is_numeric_v_string_like as is_numeric_v_string_like, is_object_dtype as is_object_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna, na_value_for_dtype as na_value_for_dtype
from typing import Any

def check_value_size(value, mask: npt.NDArray[np.bool_], length: int):
    """
    Validate the size of the values passed to ExtensionArray.fillna.
    """
def mask_missing(arr: ArrayLike, values_to_mask) -> npt.NDArray[np.bool_]:
    """
    Return a masking array of same size/shape as arr
    with entries equaling any member of values_to_mask set to True

    Parameters
    ----------
    arr : ArrayLike
    values_to_mask: list, tuple, or scalar

    Returns
    -------
    np.ndarray[bool]
    """
def clean_fill_method(method: str | None, allow_nearest: bool = False): ...

NP_METHODS: Incomplete
SP_METHODS: Incomplete

def clean_interp_method(method: str, index: Index, **kwargs) -> str: ...
def find_valid_index(values, *, how: str, is_valid: npt.NDArray[np.bool_]) -> int | None:
    """
    Retrieves the index of the first valid value.

    Parameters
    ----------
    values : ndarray or ExtensionArray
    how : {'first', 'last'}
        Use this parameter to change between the first or last valid index.
    is_valid: np.ndarray
        Mask to find na_values.

    Returns
    -------
    int or None
    """
def interpolate_array_2d(data: np.ndarray, method: str = 'pad', axis: AxisInt = 0, index: Index | None = None, limit: int | None = None, limit_direction: str = 'forward', limit_area: str | None = None, fill_value: Any | None = None, coerce: bool = False, downcast: str | None = None, **kwargs) -> None:
    """
    Wrapper to dispatch to either interpolate_2d or _interpolate_2d_with_fill.

    Notes
    -----
    Alters 'data' in-place.
    """
def interpolate_2d(values: np.ndarray, method: str = 'pad', axis: Axis = 0, limit: int | None = None, limit_area: str | None = None) -> None:
    '''
    Perform an actual interpolation of values, values will be make 2-d if
    needed fills inplace, returns the result.

    Parameters
    ----------
    values: np.ndarray
        Input array.
    method: str, default "pad"
        Interpolation method. Could be "bfill" or "pad"
    axis: 0 or 1
        Interpolation axis
    limit: int, optional
        Index limit on interpolation.
    limit_area: str, optional
        Limit area for interpolation. Can be "inside" or "outside"

    Notes
    -----
    Modifies values in-place.
    '''
def get_fill_func(method, ndim: int = 1): ...
def clean_reindex_fill_method(method) -> str | None: ...
