from _typeshed import Incomplete
from pandas.core.arrays.numeric import NumericArray as NumericArray, NumericDtype as NumericDtype
from pandas.core.dtypes.base import register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.common import is_float_dtype as is_float_dtype

class FloatingDtype(NumericDtype):
    """
    An ExtensionDtype to hold a single size of floating dtype.

    These specific implementations are subclasses of the non-public
    FloatingDtype. For example we have Float32Dtype to represent float32.

    The attributes name & type are set when these subclasses are created.
    """
    @classmethod
    def construct_array_type(cls) -> type[FloatingArray]:
        """
        Return the array type associated with this dtype.

        Returns
        -------
        type
        """

class FloatingArray(NumericArray):
    '''
    Array of floating (optional missing) values.

    .. versionadded:: 1.2.0

    .. warning::

       FloatingArray is currently experimental, and its API or internal
       implementation may change without warning. Especially the behaviour
       regarding NaN (distinct from NA missing values) is subject to change.

    We represent a FloatingArray with 2 numpy arrays:

    - data: contains a numpy float array of the appropriate dtype
    - mask: a boolean array holding a mask on the data, True is missing

    To construct an FloatingArray from generic array-like input, use
    :func:`pandas.array` with one of the float dtypes (see examples).

    See :ref:`integer_na` for more.

    Parameters
    ----------
    values : numpy.ndarray
        A 1-d float-dtype array.
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
    FloatingArray

    Examples
    --------
    Create an FloatingArray with :func:`pandas.array`:

    >>> pd.array([0.1, None, 0.3], dtype=pd.Float32Dtype())
    <FloatingArray>
    [0.1, <NA>, 0.3]
    Length: 3, dtype: Float32

    String aliases for the dtypes are also available. They are capitalized.

    >>> pd.array([0.1, None, 0.3], dtype="Float32")
    <FloatingArray>
    [0.1, <NA>, 0.3]
    Length: 3, dtype: Float32
    '''

class Float32Dtype(FloatingDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

class Float64Dtype(FloatingDtype):
    type: Incomplete
    name: str
    __doc__: Incomplete

FLOAT_STR_TO_DTYPE: Incomplete
