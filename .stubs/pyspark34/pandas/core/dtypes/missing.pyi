import numpy as np
from _typeshed import Incomplete
from pandas._config import get_option as get_option
from pandas._libs import lib as lib
from pandas._libs.tslibs import NaT as NaT, iNaT as iNaT
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, NDFrame as NDFrame, NDFrameT as NDFrameT, Scalar as Scalar, npt as npt
from pandas.core.dtypes.common import DT64NS_DTYPE as DT64NS_DTYPE, TD64NS_DTYPE as TD64NS_DTYPE, ensure_object as ensure_object, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_complex_dtype as is_complex_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_or_object_np_dtype as is_string_or_object_np_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype, IntervalDtype as IntervalDtype, PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCExtensionArray as ABCExtensionArray, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_list_like as is_list_like
from pandas.core.indexes.base import Index as Index
from typing import overload

isposinf_scalar: Incomplete
isneginf_scalar: Incomplete
nan_checker: Incomplete
INF_AS_NA: bool

@overload
def isna(obj: Scalar) -> bool: ...
@overload
def isna(obj: ArrayLike | Index | list) -> npt.NDArray[np.bool_]: ...
@overload
def isna(obj: NDFrameT) -> NDFrameT: ...
@overload
def isna(obj: NDFrameT | ArrayLike | Index | list) -> NDFrameT | npt.NDArray[np.bool_]: ...
@overload
def isna(obj: object) -> bool | npt.NDArray[np.bool_] | NDFrame: ...
isnull = isna

@overload
def notna(obj: Scalar) -> bool: ...
@overload
def notna(obj: ArrayLike | Index | list) -> npt.NDArray[np.bool_]: ...
@overload
def notna(obj: NDFrameT) -> NDFrameT: ...
@overload
def notna(obj: NDFrameT | ArrayLike | Index | list) -> NDFrameT | npt.NDArray[np.bool_]: ...
@overload
def notna(obj: object) -> bool | npt.NDArray[np.bool_] | NDFrame: ...
notnull = notna

def isna_compat(arr, fill_value=...) -> bool:
    """
    Parameters
    ----------
    arr: a numpy array
    fill_value: fill value, default to np.nan

    Returns
    -------
    True if we can fill using this fill_value
    """
def array_equivalent(left, right, strict_nan: bool = False, dtype_equal: bool = False) -> bool:
    """
    True if two arrays, left and right, have equal non-NaN elements, and NaNs
    in corresponding locations.  False otherwise. It is assumed that left and
    right are NumPy arrays of the same dtype. The behavior of this function
    (particularly with respect to NaNs) is not defined if the dtypes are
    different.

    Parameters
    ----------
    left, right : ndarrays
    strict_nan : bool, default False
        If True, consider NaN and None to be different.
    dtype_equal : bool, default False
        Whether `left` and `right` are known to have the same dtype
        according to `is_dtype_equal`. Some methods like `BlockManager.equals`.
        require that the dtypes match. Setting this to ``True`` can improve
        performance, but will give different results for arrays that are
        equal but different dtypes.

    Returns
    -------
    b : bool
        Returns True if the arrays are equivalent.

    Examples
    --------
    >>> array_equivalent(
    ...     np.array([1, 2, np.nan]),
    ...     np.array([1, 2, np.nan]))
    True
    >>> array_equivalent(
    ...     np.array([1, np.nan, 2]),
    ...     np.array([1, 2, np.nan]))
    False
    """
def array_equals(left: ArrayLike, right: ArrayLike) -> bool:
    """
    ExtensionArray-compatible implementation of array_equivalent.
    """
def infer_fill_value(val):
    """
    infer the fill value for the nan/NaT from the provided
    scalar/ndarray/list-like if we are a NaT, return the correct dtyped
    element to provide proper block construction
    """
def maybe_fill(arr: np.ndarray) -> np.ndarray:
    """
    Fill numpy.ndarray with NaN, unless we have a integer or boolean dtype.
    """
def na_value_for_dtype(dtype: DtypeObj, compat: bool = True):
    """
    Return a dtype compat na value

    Parameters
    ----------
    dtype : string / dtype
    compat : bool, default True

    Returns
    -------
    np.dtype or a pandas dtype

    Examples
    --------
    >>> na_value_for_dtype(np.dtype('int64'))
    0
    >>> na_value_for_dtype(np.dtype('int64'), compat=False)
    nan
    >>> na_value_for_dtype(np.dtype('float64'))
    nan
    >>> na_value_for_dtype(np.dtype('bool'))
    False
    >>> na_value_for_dtype(np.dtype('datetime64[ns]'))
    numpy.datetime64('NaT')
    """
def remove_na_arraylike(arr):
    """
    Return array-like containing only true/non-NaN values, possibly empty.
    """
def is_valid_na_for_dtype(obj, dtype: DtypeObj) -> bool:
    """
    isna check that excludes incompatible dtypes

    Parameters
    ----------
    obj : object
    dtype : np.datetime64, np.timedelta64, DatetimeTZDtype, or PeriodDtype

    Returns
    -------
    bool
    """
def isna_all(arr: ArrayLike) -> bool:
    """
    Optimized equivalent to isna(arr).all()
    """
