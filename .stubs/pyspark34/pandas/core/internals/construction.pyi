import numpy as np
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, Manager as Manager, npt as npt
from pandas.core import algorithms as algorithms
from pandas.core.arrays import BooleanArray as BooleanArray, ExtensionArray as ExtensionArray, FloatingArray as FloatingArray, IntegerArray as IntegerArray
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array, range_to_ndarray as range_to_ndarray, sanitize_array as sanitize_array
from pandas.core.dtypes.astype import astype_is_view as astype_is_view
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, dict_compat as dict_compat, maybe_cast_to_datetime as maybe_cast_to_datetime, maybe_convert_platform as maybe_convert_platform, maybe_infer_to_datetimelike as maybe_infer_to_datetimelike
from pandas.core.dtypes.common import is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_bool_dtype as is_bool_dtype, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_named_tuple as is_named_tuple, is_object_dtype as is_object_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.indexes.api import DatetimeIndex as DatetimeIndex, Index as Index, TimedeltaIndex as TimedeltaIndex, default_index as default_index, ensure_index as ensure_index, get_objs_combined_axis as get_objs_combined_axis, union_indexes as union_indexes
from pandas.core.internals.array_manager import ArrayManager as ArrayManager, SingleArrayManager as SingleArrayManager
from pandas.core.internals.blocks import BlockPlacement as BlockPlacement, ensure_block_shape as ensure_block_shape, new_block_2d as new_block_2d
from pandas.core.internals.managers import BlockManager as BlockManager, SingleBlockManager as SingleBlockManager, create_block_manager_from_blocks as create_block_manager_from_blocks, create_block_manager_from_column_arrays as create_block_manager_from_column_arrays
from typing import Sequence

def arrays_to_mgr(arrays, columns: Index, index, *, dtype: DtypeObj | None = None, verify_integrity: bool = True, typ: str | None = None, consolidate: bool = True) -> Manager:
    """
    Segregate Series based on type and coerce into matrices.

    Needs to handle a lot of exceptional cases.
    """
def rec_array_to_mgr(data: np.recarray | np.ndarray, index, columns, dtype: DtypeObj | None, copy: bool, typ: str) -> Manager:
    """
    Extract from a masked rec array and create the manager.
    """
def mgr_to_mgr(mgr, typ: str, copy: bool = True):
    """
    Convert to specific type of Manager. Does not copy if the type is already
    correct. Does not guarantee a copy otherwise. `copy` keyword only controls
    whether conversion from Block->ArrayManager copies the 1D arrays.
    """
def ndarray_to_mgr(values, index, columns, dtype: DtypeObj | None, copy: bool, typ: str) -> Manager: ...
def dict_to_mgr(data: dict, index, columns, *, dtype: DtypeObj | None = None, typ: str = 'block', copy: bool = True) -> Manager:
    """
    Segregate Series based on type and coerce into matrices.
    Needs to handle a lot of exceptional cases.

    Used in DataFrame.__init__
    """
def nested_data_to_arrays(data: Sequence, columns: Index | None, index: Index | None, dtype: DtypeObj | None) -> tuple[list[ArrayLike], Index, Index]:
    """
    Convert a single sequence of arrays to multiple arrays.
    """
def treat_as_nested(data) -> bool:
    """
    Check if we should use nested_data_to_arrays.
    """
def reorder_arrays(arrays: list[ArrayLike], arr_columns: Index, columns: Index | None, length: int) -> tuple[list[ArrayLike], Index]:
    """
    Pre-emptively (cheaply) reindex arrays with new columns.
    """
def dataclasses_to_dicts(data):
    """
    Converts a list of dataclass instances to a list of dictionaries.

    Parameters
    ----------
    data : List[Type[dataclass]]

    Returns
    --------
    list_dict : List[dict]

    Examples
    --------
    >>> from dataclasses import dataclass
    >>> @dataclass
    ... class Point:
    ...     x: int
    ...     y: int

    >>> dataclasses_to_dicts([Point(1, 2), Point(2, 3)])
    [{'x': 1, 'y': 2}, {'x': 2, 'y': 3}]

    """
def to_arrays(data, columns: Index | None, dtype: DtypeObj | None = None) -> tuple[list[ArrayLike], Index]:
    """
    Return list of arrays, columns.

    Returns
    -------
    list[ArrayLike]
        These will become columns in a DataFrame.
    Index
        This will become frame.columns.

    Notes
    -----
    Ensures that len(result_arrays) == len(result_index).
    """
def convert_object_array(content: list[npt.NDArray[np.object_]], dtype: DtypeObj | None, dtype_backend: str = 'numpy', coerce_float: bool = False) -> list[ArrayLike]:
    """
    Internal function to convert object array.

    Parameters
    ----------
    content: List[np.ndarray]
    dtype: np.dtype or ExtensionDtype
    dtype_backend: Controls if nullable/pyarrow dtypes are returned.
    coerce_float: Cast floats that are integers to int.

    Returns
    -------
    List[ArrayLike]
    """
