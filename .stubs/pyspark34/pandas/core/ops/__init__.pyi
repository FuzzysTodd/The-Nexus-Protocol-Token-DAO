from pandas import DataFrame, Series
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op as maybe_dispatch_ufunc_to_dunder_op
from pandas._typing import Level
from pandas.core.ops.array_ops import arithmetic_op as arithmetic_op, comp_method_OBJECT_ARRAY as comp_method_OBJECT_ARRAY, comparison_op as comparison_op, logical_op as logical_op
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.ops.invalid import invalid_comparison as invalid_comparison
from pandas.core.ops.mask_ops import kleene_and as kleene_and, kleene_or as kleene_or, kleene_xor as kleene_xor
from pandas.core.ops.methods import add_flex_arithmetic_methods as add_flex_arithmetic_methods
from pandas.core.roperator import radd as radd, rand_ as rand_, rdiv as rdiv, rdivmod as rdivmod, rfloordiv as rfloordiv, rmod as rmod, rmul as rmul, ror_ as ror_, rpow as rpow, rsub as rsub, rtruediv as rtruediv, rxor as rxor

__all__ = ['add_flex_arithmetic_methods', 'align_method_FRAME', 'align_method_SERIES', 'ARITHMETIC_BINOPS', 'arithmetic_op', 'COMPARISON_BINOPS', 'comparison_op', 'comp_method_OBJECT_ARRAY', 'fill_binop', 'flex_arith_method_FRAME', 'flex_comp_method_FRAME', 'flex_method_SERIES', 'frame_arith_method_with_reindex', 'invalid_comparison', 'kleene_and', 'kleene_or', 'kleene_xor', 'logical_op', 'maybe_dispatch_ufunc_to_dunder_op', 'radd', 'rand_', 'rdiv', 'rdivmod', 'rfloordiv', 'rmod', 'rmul', 'ror_', 'rpow', 'rsub', 'rtruediv', 'rxor', 'should_reindex_frame_op', 'unpack_zerodim_and_defer']

ARITHMETIC_BINOPS: set[str]
COMPARISON_BINOPS: set[str]

def fill_binop(left, right, fill_value):
    """
    If a non-None fill_value is given, replace null entries in left and right
    with this value, but only in positions where _one_ of left/right is null,
    not both.

    Parameters
    ----------
    left : array-like
    right : array-like
    fill_value : object

    Returns
    -------
    left : array-like
    right : array-like

    Notes
    -----
    Makes copies if fill_value is not None and NAs are present.
    """
def align_method_SERIES(left: Series, right, align_asobject: bool = False):
    """align lhs and rhs Series"""
def flex_method_SERIES(op): ...
def align_method_FRAME(left, right, axis, flex: bool | None = False, level: Level = None):
    """
    Convert rhs to meet lhs dims if input is list, tuple or np.ndarray.

    Parameters
    ----------
    left : DataFrame
    right : Any
    axis : int, str, or None
    flex : bool or None, default False
        Whether this is a flex op, in which case we reindex.
        None indicates not to check for alignment.
    level : int or level name, default None

    Returns
    -------
    left : DataFrame
    right : Any
    """
def should_reindex_frame_op(left: DataFrame, right, op, axis: int, fill_value, level) -> bool:
    """
    Check if this is an operation between DataFrames that will need to reindex.
    """
def frame_arith_method_with_reindex(left: DataFrame, right: DataFrame, op) -> DataFrame:
    """
    For DataFrame-with-DataFrame operations that require reindexing,
    operate only on shared columns, then reindex.

    Parameters
    ----------
    left : DataFrame
    right : DataFrame
    op : binary operator

    Returns
    -------
    DataFrame
    """
def flex_arith_method_FRAME(op): ...
def flex_comp_method_FRAME(op): ...
