import numpy as np
from pandas import MultiIndex as MultiIndex
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, npt as npt
from pandas.compat import np_version_under1p21 as np_version_under1p21
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.dtypes.cast import infer_dtype_from as infer_dtype_from
from pandas.core.dtypes.common import is_list_like as is_list_like
from typing import Any

def putmask_inplace(values: ArrayLike, mask: npt.NDArray[np.bool_], value: Any) -> None:
    """
    ExtensionArray-compatible implementation of np.putmask.  The main
    difference is we do not handle repeating or truncating like numpy.

    Parameters
    ----------
    values: np.ndarray or ExtensionArray
    mask : np.ndarray[bool]
        We assume extract_bool_array has already been called.
    value : Any
    """
def putmask_without_repeat(values: np.ndarray, mask: npt.NDArray[np.bool_], new: Any) -> None:
    """
    np.putmask will truncate or repeat if `new` is a listlike with
    len(new) != len(values).  We require an exact match.

    Parameters
    ----------
    values : np.ndarray
    mask : np.ndarray[bool]
    new : Any
    """
def validate_putmask(values: ArrayLike | MultiIndex, mask: np.ndarray) -> tuple[npt.NDArray[np.bool_], bool]:
    """
    Validate mask and check if this putmask operation is a no-op.
    """
def extract_bool_array(mask: ArrayLike) -> npt.NDArray[np.bool_]:
    """
    If we have a SparseArray or BooleanArray, convert it to ndarray[bool].
    """
def setitem_datetimelike_compat(values: np.ndarray, num_set: int, other):
    """
    Parameters
    ----------
    values : np.ndarray
    num_set : int
        For putmask, this is mask.sum()
    other : Any
    """
