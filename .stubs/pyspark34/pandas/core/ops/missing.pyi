import numpy as np
from pandas.core.dtypes.common import is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_scalar as is_scalar
from pandas.core.ops import roperator as roperator

def mask_zero_div_zero(x, y, result: np.ndarray) -> np.ndarray:
    """
    Set results of  0 // 0 to np.nan, regardless of the dtypes
    of the numerator or the denominator.

    Parameters
    ----------
    x : ndarray
    y : ndarray
    result : ndarray

    Returns
    -------
    ndarray
        The filled result.

    Examples
    --------
    >>> x = np.array([1, 0, -1], dtype=np.int64)
    >>> x
    array([ 1,  0, -1])
    >>> y = 0       # int 0; numpy behavior is different with float
    >>> result = x // y
    >>> result      # raw numpy result does not fill division by zero
    array([0, 0, 0])
    >>> mask_zero_div_zero(x, y, result)
    array([ inf,  nan, -inf])
    """
def dispatch_fill_zeros(op, left, right, result):
    """
    Call _fill_zeros with the appropriate fill value depending on the operation,
    with special logic for divmod and rdivmod.

    Parameters
    ----------
    op : function (operator.add, operator.div, ...)
    left : object (np.ndarray for non-reversed ops)
    right : object (np.ndarray for reversed ops)
    result : ndarray

    Returns
    -------
    result : np.ndarray

    Notes
    -----
    For divmod and rdivmod, the `result` parameter and returned `result`
    is a 2-tuple of ndarray objects.
    """
