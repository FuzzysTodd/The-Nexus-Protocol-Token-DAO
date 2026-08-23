import numpy as np
from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op as maybe_dispatch_ufunc_to_dunder_op
from pandas.core import roperator as roperator
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.generic import ABCNDFrame as ABCNDFrame
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from typing import Any

REDUCTION_ALIASES: Incomplete

class OpsMixin:
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __and__(self, other): ...
    def __rand__(self, other): ...
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __xor__(self, other): ...
    def __rxor__(self, other): ...
    def __add__(self, other):
        """
        Get Addition of DataFrame and other, column-wise.

        Equivalent to ``DataFrame.add(other)``.

        Parameters
        ----------
        other : scalar, sequence, Series, dict or DataFrame
            Object to be added to the DataFrame.

        Returns
        -------
        DataFrame
            The result of adding ``other`` to DataFrame.

        See Also
        --------
        DataFrame.add : Add a DataFrame and another object, with option for index-
            or column-oriented addition.

        Examples
        --------
        >>> df = pd.DataFrame({'height': [1.5, 2.6], 'weight': [500, 800]},
        ...                   index=['elk', 'moose'])
        >>> df
               height  weight
        elk       1.5     500
        moose     2.6     800

        Adding a scalar affects all rows and columns.

        >>> df[['height', 'weight']] + 1.5
               height  weight
        elk       3.0   501.5
        moose     4.1   801.5

        Each element of a list is added to a column of the DataFrame, in order.

        >>> df[['height', 'weight']] + [0.5, 1.5]
               height  weight
        elk       2.0   501.5
        moose     3.1   801.5

        Keys of a dictionary are aligned to the DataFrame, based on column names;
        each value in the dictionary is added to the corresponding column.

        >>> df[['height', 'weight']] + {'height': 0.5, 'weight': 1.5}
               height  weight
        elk       2.0   501.5
        moose     3.1   801.5

        When `other` is a :class:`Series`, the index of `other` is aligned with the
        columns of the DataFrame.

        >>> s1 = pd.Series([0.5, 1.5], index=['weight', 'height'])
        >>> df[['height', 'weight']] + s1
               height  weight
        elk       3.0   500.5
        moose     4.1   800.5

        Even when the index of `other` is the same as the index of the DataFrame,
        the :class:`Series` will not be reoriented. If index-wise alignment is desired,
        :meth:`DataFrame.add` should be used with `axis='index'`.

        >>> s2 = pd.Series([0.5, 1.5], index=['elk', 'moose'])
        >>> df[['height', 'weight']] + s2
               elk  height  moose  weight
        elk    NaN     NaN    NaN     NaN
        moose  NaN     NaN    NaN     NaN

        >>> df[['height', 'weight']].add(s2, axis='index')
               height  weight
        elk       2.0   500.5
        moose     4.1   801.5

        When `other` is a :class:`DataFrame`, both columns names and the
        index are aligned.

        >>> other = pd.DataFrame({'height': [0.2, 0.4, 0.6]},
        ...                      index=['elk', 'moose', 'deer'])
        >>> df[['height', 'weight']] + other
               height  weight
        deer      NaN     NaN
        elk       1.7     NaN
        moose     3.0     NaN
        """
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __pow__(self, other): ...
    def __rpow__(self, other): ...

def array_ufunc(self, ufunc: np.ufunc, method: str, *inputs: Any, **kwargs: Any):
    """
    Compatibility with numpy ufuncs.

    See also
    --------
    numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__
    """
def dispatch_ufunc_with_out(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
    """
    If we have an `out` keyword, then call the ufunc without `out` and then
    set the result into the given `out`.
    """
def default_array_ufunc(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
    """
    Fallback to the behavior we would get if we did not define __array_ufunc__.

    Notes
    -----
    We are assuming that `self` is among `inputs`.
    """
def dispatch_reduction_ufunc(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
    """
    Dispatch ufunc reductions to self's reduction methods.
    """
