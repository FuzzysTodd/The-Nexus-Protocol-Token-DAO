from _typeshed import Incomplete
from pandas.core.arrays.numeric import NumericArray as NumericArray, NumericDtype as NumericDtype
from pandas.core.dtypes.base import register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.common import is_integer_dtype as is_integer_dtype

class IntegerDtype(NumericDtype):
    """
    An ExtensionDtype to hold a single size & kind of integer dtype.

    These specific implementations are subclasses of the non-public
    IntegerDtype. For example, we have Int8Dtype to represent signed int 8s.

    The attributes name & type are set when these subclasses are created.
    """
    @classmethod
    def construct_array_type(cls) -> type[IntegerArray]:
        """
        Return the array type associated with this dtype.

        Returns
        -------
        type
        """

class IntegerArray(NumericArray):
    """
    Array of integer (optional missing) values.

    Uses :attr:`pandas.NA` as the missing value.

    .. warning::

       IntegerArray is currently experimental, and its API or internal
       implementation may change without warning.

    We represent an IntegerArray with 2 numpy arrays:

    - data: contains a numpy integer array of the appropriate dtype
    - mask: a boolean array holding a mask on the data, True is missing

    To construct an IntegerArray from generic array-like input, use
    :func:`pandas.array` with one of the integer dtypes (see examples).

    See :ref:`integer_na` for more.

    Parameters
    ----------
    values : numpy.ndarray
        A 1-d integer-dtype array.
    mask : numpy.ndarray
        A 1-d boolean-dtype array indicating missing values.
    copy : bool, default False
        Whether to copy the `values` and `mask`.

    Attributes
    ----------
    None

    Methods
    -------
    None

    Returns
    -------
    IntegerArray

    Examples
    --------
    Create an IntegerArray with :func:`pandas.array`.

    >>> int_array = pd.array([1, None, 3], dtype=pd.Int32Dtype())
    >>> int_array
    <IntegerArray>
    [1, <NA>, 3]
    Length: 3, dtype: Int32

    String aliases for the dtypes are also available. They are capitalized.

    >>> pd.array([1, None, 3], dtype='Int32')
    <IntegerArray>
    [1, <NA>, 3]
    Length: 3, dtype: Int32

    >>> pd.array([1, None, 3], dtype='UInt16')
    <IntegerArray>
    [1, <NA>, 3]
    Length: 3, dtype: UInt16
    """

class Int8Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class Int16Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class Int32Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class Int64Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class UInt8Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class UInt16Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class UInt32Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class UInt64Dtype(IntegerDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

INT_STR_TO_DTYPE: dict[str, IntegerDtype]
