from _typeshed import Incomplete

__all__ = ['upcast', 'getdtype', 'getdata', 'isscalarlike', 'isintlike', 'isshape', 'issequence', 'isdense', 'ismatrix', 'get_sum_dtype']

def upcast(*args):
    """Returns the nearest supported sparse dtype for the
    combination of one or more types.

    upcast(t0, t1, ..., tn) -> T  where T is a supported dtype

    Examples
    --------

    >>> upcast('int32')
    <type 'numpy.int32'>
    >>> upcast('bool')
    <type 'numpy.bool_'>
    >>> upcast('int32','float32')
    <type 'numpy.float64'>
    >>> upcast('bool',complex,float)
    <type 'numpy.complex128'>

    """
def getdtype(dtype, a: Incomplete | None = None, default: Incomplete | None = None):
    """Function used to simplify argument processing. If 'dtype' is not
    specified (is None), returns a.dtype; otherwise returns a np.dtype
    object created from the specified dtype argument. If 'dtype' and 'a'
    are both None, construct a data type out of the 'default' parameter.
    Furthermore, 'dtype' must be in 'allowed' set.
    """
def getdata(obj, dtype: Incomplete | None = None, copy: bool = False):
    """
    This is a wrapper of `np.array(obj, dtype=dtype, copy=copy)`
    that will generate a warning if the result is an object array.
    """
def get_sum_dtype(dtype):
    """Mimic numpy's casting for np.sum"""
def isscalarlike(x):
    """Is x either a scalar, an array scalar, or a 0-dim array?"""
def isintlike(x):
    """Is x appropriate as an index into a sparse matrix? Returns True
    if it can be cast safely to a machine int.
    """
def isshape(x, nonneg: bool = False):
    """Is x a valid 2-tuple of dimensions?

    If nonneg, also checks that the dimensions are non-negative.
    """
def issequence(t): ...
def ismatrix(t): ...
def isdense(x): ...
