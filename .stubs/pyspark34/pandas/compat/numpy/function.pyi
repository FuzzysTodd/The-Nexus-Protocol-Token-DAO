from _typeshed import Incomplete
from numpy import ndarray
from pandas._libs.lib import is_bool as is_bool, is_integer as is_integer
from pandas._typing import Axis as Axis, AxisInt as AxisInt
from pandas.errors import UnsupportedFunctionCall as UnsupportedFunctionCall
from pandas.util._validators import validate_args as validate_args, validate_args_and_kwargs as validate_args_and_kwargs, validate_kwargs as validate_kwargs
from typing import Any, TypeVar, overload

AxisNoneT = TypeVar('AxisNoneT', Axis, None)

class CompatValidator:
    fname: Incomplete
    method: Incomplete
    defaults: Incomplete
    max_fname_arg_count: Incomplete
    def __init__(self, defaults, fname: Incomplete | None = None, method: str | None = None, max_fname_arg_count: Incomplete | None = None) -> None: ...
    def __call__(self, args, kwargs, fname: Incomplete | None = None, max_fname_arg_count: Incomplete | None = None, method: str | None = None) -> None: ...

ARGMINMAX_DEFAULTS: Incomplete
validate_argmin: Incomplete
validate_argmax: Incomplete

def process_skipna(skipna: bool | ndarray | None, args) -> tuple[bool, Any]: ...
def validate_argmin_with_skipna(skipna: bool | ndarray | None, args, kwargs) -> bool:
    """
    If 'Series.argmin' is called via the 'numpy' library, the third parameter
    in its signature is 'out', which takes either an ndarray or 'None', so
    check if the 'skipna' parameter is either an instance of ndarray or is
    None, since 'skipna' itself should be a boolean
    """
def validate_argmax_with_skipna(skipna: bool | ndarray | None, args, kwargs) -> bool:
    """
    If 'Series.argmax' is called via the 'numpy' library, the third parameter
    in its signature is 'out', which takes either an ndarray or 'None', so
    check if the 'skipna' parameter is either an instance of ndarray or is
    None, since 'skipna' itself should be a boolean
    """

ARGSORT_DEFAULTS: dict[str, int | str | None]
validate_argsort: Incomplete
ARGSORT_DEFAULTS_KIND: dict[str, int | None]
validate_argsort_kind: Incomplete

def validate_argsort_with_ascending(ascending: bool | int | None, args, kwargs) -> bool:
    """
    If 'Categorical.argsort' is called via the 'numpy' library, the first
    parameter in its signature is 'axis', which takes either an integer or
    'None', so check if the 'ascending' parameter has either integer type or is
    None, since 'ascending' itself should be a boolean
    """

CLIP_DEFAULTS: dict[str, Any]
validate_clip: Incomplete

@overload
def validate_clip_with_axis(axis: ndarray, args, kwargs) -> None: ...
@overload
def validate_clip_with_axis(axis: AxisNoneT, args, kwargs) -> AxisNoneT: ...

CUM_FUNC_DEFAULTS: dict[str, Any]
validate_cum_func: Incomplete
validate_cumsum: Incomplete

def validate_cum_func_with_skipna(skipna, args, kwargs, name) -> bool:
    """
    If this function is called via the 'numpy' library, the third parameter in
    its signature is 'dtype', which takes either a 'numpy' dtype or 'None', so
    check if the 'skipna' parameter is a boolean or not
    """

ALLANY_DEFAULTS: dict[str, bool | None]
validate_all: Incomplete
validate_any: Incomplete
LOGICAL_FUNC_DEFAULTS: Incomplete
validate_logical_func: Incomplete
MINMAX_DEFAULTS: Incomplete
validate_min: Incomplete
validate_max: Incomplete
RESHAPE_DEFAULTS: dict[str, str]
validate_reshape: Incomplete
REPEAT_DEFAULTS: dict[str, Any]
validate_repeat: Incomplete
ROUND_DEFAULTS: dict[str, Any]
validate_round: Incomplete
SORT_DEFAULTS: dict[str, int | str | None]
validate_sort: Incomplete
STAT_FUNC_DEFAULTS: dict[str, Any | None]
SUM_DEFAULTS: Incomplete
PROD_DEFAULTS: Incomplete
MEDIAN_DEFAULTS: Incomplete
validate_stat_func: Incomplete
validate_sum: Incomplete
validate_prod: Incomplete
validate_mean: Incomplete
validate_median: Incomplete
STAT_DDOF_FUNC_DEFAULTS: dict[str, bool | None]
validate_stat_ddof_func: Incomplete
TAKE_DEFAULTS: dict[str, str | None]
validate_take: Incomplete

def validate_take_with_convert(convert: ndarray | bool | None, args, kwargs) -> bool:
    """
    If this function is called via the 'numpy' library, the third parameter in
    its signature is 'axis', which takes either an ndarray or 'None', so check
    if the 'convert' parameter is either an instance of ndarray or is None
    """

TRANSPOSE_DEFAULTS: Incomplete
validate_transpose: Incomplete

def validate_groupby_func(name, args, kwargs, allowed: Incomplete | None = None) -> None:
    """
    'args' and 'kwargs' should be empty, except for allowed kwargs because all
    of their necessary parameters are explicitly listed in the function
    signature
    """

RESAMPLER_NUMPY_OPS: Incomplete

def validate_resampler_func(method: str, args, kwargs) -> None:
    """
    'args' and 'kwargs' should be empty because all of their necessary
    parameters are explicitly listed in the function signature
    """
def validate_minmax_axis(axis: AxisInt | None, ndim: int = 1) -> None:
    """
    Ensure that the axis argument passed to min, max, argmin, or argmax is zero
    or None, as otherwise it will be incorrectly ignored.

    Parameters
    ----------
    axis : int or None
    ndim : int, default 1

    Raises
    ------
    ValueError
    """
