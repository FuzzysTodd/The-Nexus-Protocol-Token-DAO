from _typeshed import Incomplete
from pandas import Index as Index
from pandas._libs import NaT as NaT
from pandas._libs.missing import NA as NA
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, Manager as Manager, Shape as Shape
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray
from pandas.core.arrays.sparse import SparseDtype as SparseDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike
from pandas.core.dtypes.astype import astype_array as astype_array
from pandas.core.dtypes.cast import ensure_dtype_can_hold_na as ensure_dtype_can_hold_na, find_common_type as find_common_type, np_find_common_type as np_find_common_type
from pandas.core.dtypes.common import is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_dtype_equal as is_dtype_equal, is_scalar as is_scalar, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna, isna_all as isna_all
from pandas.core.internals.array_manager import ArrayManager as ArrayManager, NullArrayProxy as NullArrayProxy
from pandas.core.internals.blocks import Block as Block, ensure_block_shape as ensure_block_shape, new_block_2d as new_block_2d
from pandas.core.internals.managers import BlockManager as BlockManager
from pandas.util._decorators import cache_readonly as cache_readonly

def concat_arrays(to_concat: list) -> ArrayLike:
    """
    Alternative for concat_compat but specialized for use in the ArrayManager.

    Differences: only deals with 1D arrays (no axis keyword), assumes
    ensure_wrapped_if_datetimelike and does not skip empty arrays to determine
    the dtype.
    In addition ensures that all NullArrayProxies get replaced with actual
    arrays.

    Parameters
    ----------
    to_concat : list of arrays

    Returns
    -------
    np.ndarray or ExtensionArray
    """
def concatenate_managers(mgrs_indexers, axes: list[Index], concat_axis: AxisInt, copy: bool) -> Manager:
    """
    Concatenate block managers into one.

    Parameters
    ----------
    mgrs_indexers : list of (BlockManager, {axis: indexer,...}) tuples
    axes : list of Index
    concat_axis : int
    copy : bool

    Returns
    -------
    BlockManager
    """

class JoinUnit:
    block: Incomplete
    indexers: Incomplete
    shape: Incomplete
    def __init__(self, block: Block, shape: Shape, indexers: Incomplete | None = None) -> None: ...
    def needs_filling(self) -> bool: ...
    def dtype(self) -> DtypeObj: ...
    def is_na(self) -> bool: ...
    def get_reindexed_values(self, empty_dtype: DtypeObj, upcasted_na) -> ArrayLike: ...
