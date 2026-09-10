import numpy as np
from pandas._libs import NaT as NaT, Timedelta as Timedelta, Timestamp as Timestamp, lib as lib
from pandas._libs.tslibs import BaseOffset as BaseOffset, get_supported_reso as get_supported_reso, get_unit_from_dtype as get_unit_from_dtype, is_supported_unit as is_supported_unit, is_unitless as is_unitless, npy_unit_to_abbrev as npy_unit_to_abbrev
from pandas._typing import ArrayLike as ArrayLike, Shape as Shape
from pandas.core.computation import expressions as expressions
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike as construct_1d_object_array_from_listlike, find_common_type as find_common_type
from pandas.core.dtypes.common import ensure_object as ensure_object, is_bool_dtype as is_bool_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_v_string_like as is_numeric_v_string_like, is_object_dtype as is_object_dtype, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCExtensionArray as ABCExtensionArray, ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.ops import missing as missing, roperator as roperator
from pandas.core.ops.dispatch import should_extension_dispatch as should_extension_dispatch
from pandas.core.ops.invalid import invalid_comparison as invalid_comparison
from typing import Any

def comp_method_OBJECT_ARRAY(op, x, y): ...
def arithmetic_op(left: ArrayLike, right: Any, op):
    '''
    Evaluate an arithmetic operation `+`, `-`, `*`, `/`, `//`, `%`, `**`, ...

    Note: the caller is responsible for ensuring that numpy warnings are
    suppressed (with np.errstate(all="ignore")) if needed.

    Parameters
    ----------
    left : np.ndarray or ExtensionArray
    right : object
        Cannot be a DataFrame or Index.  Series is *not* excluded.
    op : {operator.add, operator.sub, ...}
        Or one of the reversed variants from roperator.

    Returns
    -------
    ndarray or ExtensionArray
        Or a 2-tuple of these in the case of divmod or rdivmod.
    '''
def comparison_op(left: ArrayLike, right: Any, op) -> ArrayLike:
    '''
    Evaluate a comparison operation `=`, `!=`, `>=`, `>`, `<=`, or `<`.

    Note: the caller is responsible for ensuring that numpy warnings are
    suppressed (with np.errstate(all="ignore")) if needed.

    Parameters
    ----------
    left : np.ndarray or ExtensionArray
    right : object
        Cannot be a DataFrame, Series, or Index.
    op : {operator.eq, operator.ne, operator.gt, operator.ge, operator.lt, operator.le}

    Returns
    -------
    ndarray or ExtensionArray
    '''
def na_logical_op(x: np.ndarray, y, op): ...
def logical_op(left: ArrayLike, right: Any, op) -> ArrayLike:
    """
    Evaluate a logical operation `|`, `&`, or `^`.

    Parameters
    ----------
    left : np.ndarray or ExtensionArray
    right : object
        Cannot be a DataFrame, Series, or Index.
    op : {operator.and_, operator.or_, operator.xor}
        Or one of the reversed variants from roperator.

    Returns
    -------
    ndarray or ExtensionArray
    """
def get_array_op(op):
    """
    Return a binary array operation corresponding to the given operator op.

    Parameters
    ----------
    op : function
        Binary operator from operator or roperator module.

    Returns
    -------
    functools.partial
    """
def maybe_prepare_scalar_for_op(obj, shape: Shape):
    """
    Cast non-pandas objects to pandas types to unify behavior of arithmetic
    and comparison operations.

    Parameters
    ----------
    obj: object
    shape : tuple[int]

    Returns
    -------
    out : object

    Notes
    -----
    Be careful to call this *after* determining the `name` attribute to be
    attached to the result of the arithmetic operation.
    """
