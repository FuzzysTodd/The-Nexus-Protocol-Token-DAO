from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Series as Series
from pandas._config import using_copy_on_write as using_copy_on_write
from pandas._typing import Axis as Axis, AxisInt as AxisInt, HashableT as HashableT
from pandas.core.arrays.categorical import factorize_from_iterable as factorize_from_iterable, factorize_from_iterables as factorize_from_iterables
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_bool as is_bool
from pandas.core.dtypes.missing import isna as isna
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, all_indexes_same as all_indexes_same, default_index as default_index, ensure_index as ensure_index, get_objs_combined_axis as get_objs_combined_axis, get_unanimous_names as get_unanimous_names
from pandas.core.internals import concatenate_managers as concatenate_managers
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Iterable, Literal, Mapping, overload

@overload
def concat(objs: Iterable[DataFrame] | Mapping[HashableT, DataFrame], *, axis: Literal[0, 'index'] = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame: ...
@overload
def concat(objs: Iterable[Series] | Mapping[HashableT, Series], *, axis: Literal[0, 'index'] = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> Series: ...
@overload
def concat(objs: Iterable[NDFrame] | Mapping[HashableT, NDFrame], *, axis: Literal[0, 'index'] = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame | Series: ...
@overload
def concat(objs: Iterable[NDFrame] | Mapping[HashableT, NDFrame], *, axis: Literal[1, 'columns'], join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame: ...
@overload
def concat(objs: Iterable[NDFrame] | Mapping[HashableT, NDFrame], *, axis: Axis = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame | Series: ...

class _Concatenator:
    """
    Orchestrates a concatenation operation for BlockManagers
    """
    intersect: bool
    objs: Incomplete
    bm_axis: Incomplete
    axis: Incomplete
    keys: Incomplete
    names: Incomplete
    levels: Incomplete
    sort: Incomplete
    ignore_index: Incomplete
    verify_integrity: Incomplete
    copy: Incomplete
    new_axes: Incomplete
    def __init__(self, objs: Iterable[NDFrame] | Mapping[HashableT, NDFrame], axis: Axis = 0, join: str = 'outer', keys: Incomplete | None = None, levels: Incomplete | None = None, names: Incomplete | None = None, ignore_index: bool = False, verify_integrity: bool = False, copy: bool = True, sort: bool = False) -> None: ...
    def get_result(self): ...
