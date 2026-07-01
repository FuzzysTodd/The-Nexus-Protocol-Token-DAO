import numpy as np
from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._typing import Dtype as Dtype, Scalar as Scalar, npt as npt
from pandas.compat import pa_version_under7p0 as pa_version_under7p0
from pandas.core.arrays.arrow import ArrowExtensionArray as ArrowExtensionArray
from pandas.core.arrays.arrow._arrow_utils import fallback_performancewarning as fallback_performancewarning
from pandas.core.arrays.boolean import BooleanDtype as BooleanDtype
from pandas.core.arrays.integer import Int64Dtype as Int64Dtype
from pandas.core.arrays.numeric import NumericDtype as NumericDtype
from pandas.core.arrays.string_ import BaseStringArray as BaseStringArray, StringDtype as StringDtype
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_dtype_equal as is_dtype_equal, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.strings.object_array import ObjectStringArrayMixin as ObjectStringArrayMixin

ArrowStringScalarOrNAT: Incomplete

class ArrowStringArray(ObjectStringArrayMixin, ArrowExtensionArray, BaseStringArray):
    '''
    Extension array for string data in a ``pyarrow.ChunkedArray``.

    .. versionadded:: 1.2.0

    .. warning::

       ArrowStringArray is considered experimental. The implementation and
       parts of the API may change without warning.

    Parameters
    ----------
    values : pyarrow.Array or pyarrow.ChunkedArray
        The array of data.

    Attributes
    ----------
    None

    Methods
    -------
    None

    See Also
    --------
    :func:`pandas.array`
        The recommended function for creating a ArrowStringArray.
    Series.str
        The string methods are available on Series backed by
        a ArrowStringArray.

    Notes
    -----
    ArrowStringArray returns a BooleanArray for comparison methods.

    Examples
    --------
    >>> pd.array([\'This is\', \'some text\', None, \'data.\'], dtype="string[pyarrow]")
    <ArrowStringArray>
    [\'This is\', \'some text\', <NA>, \'data.\']
    Length: 4, dtype: string
    '''
    def __init__(self, values) -> None: ...
    def __len__(self) -> int:
        """
        Length of this array.

        Returns
        -------
        length : int
        """
    @property
    def dtype(self) -> StringDtype:
        """
        An instance of 'string[pyarrow]'.
        """
    def insert(self, loc: int, item) -> ArrowStringArray: ...
    def isin(self, values) -> npt.NDArray[np.bool_]: ...
    def astype(self, dtype, copy: bool = True): ...
