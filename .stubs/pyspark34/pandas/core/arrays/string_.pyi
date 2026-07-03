import numpy as np
import pyarrow
from _typeshed import Incomplete
from pandas import Series as Series
from pandas._config import get_option as get_option
from pandas._libs import lib as lib, missing as libmissing
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._typing import AxisInt as AxisInt, Dtype as Dtype, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, Scalar as Scalar, npt as npt, type_t as type_t
from pandas.compat import pa_version_under7p0 as pa_version_under7p0
from pandas.core import ops as ops
from pandas.core.array_algos import masked_reductions as masked_reductions
from pandas.core.arrays import ExtensionArray as ExtensionArray, FloatingArray as FloatingArray, IntegerArray as IntegerArray
from pandas.core.arrays.floating import FloatingDtype as FloatingDtype
from pandas.core.arrays.integer import IntegerDtype as IntegerDtype
from pandas.core.arrays.numpy_ import PandasArray as PandasArray
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype, StorageExtensionDtype as StorageExtensionDtype, register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.common import is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_dtype_equal as is_dtype_equal, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.indexers import check_array_indexer as check_array_indexer
from pandas.core.missing import isna as isna
from pandas.util._decorators import doc as doc
from typing import Literal

class StringDtype(StorageExtensionDtype):
    '''
    Extension dtype for string data.

    .. warning::

       StringDtype is considered experimental. The implementation and
       parts of the API may change without warning.

    Parameters
    ----------
    storage : {"python", "pyarrow"}, optional
        If not given, the value of ``pd.options.mode.string_storage``.

    Attributes
    ----------
    None

    Methods
    -------
    None

    Examples
    --------
    >>> pd.StringDtype()
    string[python]

    >>> pd.StringDtype(storage="pyarrow")
    string[pyarrow]
    '''
    name: str
    @property
    def na_value(self) -> libmissing.NAType: ...
    storage: Incomplete
    def __init__(self, storage: Incomplete | None = None) -> None: ...
    @property
    def type(self) -> type[str]: ...
    @classmethod
    def construct_from_string(cls, string):
        """
        Construct a StringDtype from a string.

        Parameters
        ----------
        string : str
            The type of the name. The storage type will be taking from `string`.
            Valid options and their storage types are

            ========================== ==============================================
            string                     result storage
            ========================== ==============================================
            ``'string'``               pd.options.mode.string_storage, default python
            ``'string[python]'``       python
            ``'string[pyarrow]'``      pyarrow
            ========================== ==============================================

        Returns
        -------
        StringDtype

        Raise
        -----
        TypeError
            If the string is not a valid option.
        """
    def construct_array_type(self) -> type_t[BaseStringArray]:
        """
        Return the array type associated with this dtype.

        Returns
        -------
        type
        """
    def __from_arrow__(self, array: pyarrow.Array | pyarrow.ChunkedArray) -> BaseStringArray:
        """
        Construct StringArray from pyarrow Array/ChunkedArray.
        """

class BaseStringArray(ExtensionArray):
    """
    Mixin class for StringArray, ArrowStringArray.
    """
    def tolist(self): ...

class StringArray(BaseStringArray, PandasArray):
    '''
    Extension array for string data.

    .. warning::

       StringArray is considered experimental. The implementation and
       parts of the API may change without warning.

    Parameters
    ----------
    values : array-like
        The array of data.

        .. warning::

           Currently, this expects an object-dtype ndarray
           where the elements are Python strings
           or nan-likes (``None``, ``np.nan``, ``NA``).
           This may change without warning in the future. Use
           :meth:`pandas.array` with ``dtype="string"`` for a stable way of
           creating a `StringArray` from any sequence.

        .. versionchanged:: 1.5.0

           StringArray now accepts array-likes containing
           nan-likes(``None``, ``np.nan``) for the ``values`` parameter
           in addition to strings and :attr:`pandas.NA`

    copy : bool, default False
        Whether to copy the array of data.

    Attributes
    ----------
    None

    Methods
    -------
    None

    See Also
    --------
    :func:`pandas.array`
        The recommended function for creating a StringArray.
    Series.str
        The string methods are available on Series backed by
        a StringArray.

    Notes
    -----
    StringArray returns a BooleanArray for comparison methods.

    Examples
    --------
    >>> pd.array([\'This is\', \'some text\', None, \'data.\'], dtype="string")
    <StringArray>
    [\'This is\', \'some text\', <NA>, \'data.\']
    Length: 4, dtype: string

    Unlike arrays instantiated with ``dtype="object"``, ``StringArray``
    will convert the values to strings.

    >>> pd.array([\'1\', 1], dtype="object")
    <PandasArray>
    [\'1\', 1]
    Length: 2, dtype: object
    >>> pd.array([\'1\', 1], dtype="string")
    <StringArray>
    [\'1\', \'1\']
    Length: 2, dtype: string

    However, instantiating StringArrays directly with non-strings will raise an error.

    For comparison methods, `StringArray` returns a :class:`pandas.BooleanArray`:

    >>> pd.array(["a", None, "c"], dtype="string") == "a"
    <BooleanArray>
    [True, <NA>, False]
    Length: 3, dtype: boolean
    '''
    def __init__(self, values, copy: bool = False) -> None: ...
    def __arrow_array__(self, type: Incomplete | None = None):
        """
        Convert myself into a pyarrow Array.
        """
    def __setitem__(self, key, value) -> None: ...
    def astype(self, dtype, copy: bool = True): ...
    def min(self, axis: Incomplete | None = None, skipna: bool = True, **kwargs) -> Scalar: ...
    def max(self, axis: Incomplete | None = None, skipna: bool = True, **kwargs) -> Scalar: ...
    def value_counts(self, dropna: bool = True) -> Series: ...
    def memory_usage(self, deep: bool = False) -> int: ...
    def searchsorted(self, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right'] = 'left', sorter: NumpySorter = None) -> npt.NDArray[np.intp] | np.intp: ...
