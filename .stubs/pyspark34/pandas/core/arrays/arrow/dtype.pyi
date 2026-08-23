import numpy as np
import pyarrow as pa
from _typeshed import Incomplete
from pandas._libs.tslibs import Timedelta as Timedelta, Timestamp as Timestamp
from pandas._typing import DtypeObj as DtypeObj, TYPE_CHECKING as TYPE_CHECKING, type_t as type_t
from pandas.compat import pa_version_under7p0 as pa_version_under7p0
from pandas.core.arrays.arrow import ArrowExtensionArray as ArrowExtensionArray
from pandas.core.dtypes.base import StorageExtensionDtype as StorageExtensionDtype, register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.dtypes import CategoricalDtypeType as CategoricalDtypeType
from pandas.util._decorators import cache_readonly as cache_readonly

class ArrowDtype(StorageExtensionDtype):
    '''
    An ExtensionDtype for PyArrow data types.

    .. warning::

       ArrowDtype is considered experimental. The implementation and
       parts of the API may change without warning.

    While most ``dtype`` arguments can accept the "string"
    constructor, e.g. ``"int64[pyarrow]"``, ArrowDtype is useful
    if the data type contains parameters like ``pyarrow.timestamp``.

    Parameters
    ----------
    pyarrow_dtype : pa.DataType
        An instance of a `pyarrow.DataType <https://arrow.apache.org/docs/python/api/datatypes.html#factory-functions>`__.

    Attributes
    ----------
    pyarrow_dtype

    Methods
    -------
    None

    Returns
    -------
    ArrowDtype

    Examples
    --------
    >>> import pyarrow as pa
    >>> pd.ArrowDtype(pa.int64())
    int64[pyarrow]

    Types with parameters must be constructed with ArrowDtype.

    >>> pd.ArrowDtype(pa.timestamp("s", tz="America/New_York"))
    timestamp[s, tz=America/New_York][pyarrow]
    >>> pd.ArrowDtype(pa.list_(pa.int64()))
    list<item: int64>[pyarrow]
    '''
    pyarrow_dtype: Incomplete
    def __init__(self, pyarrow_dtype: pa.DataType) -> None: ...
    @property
    def type(self):
        """
        Returns associated scalar type.
        """
    @property
    def name(self) -> str:
        """
        A string identifying the data type.
        """
    def numpy_dtype(self) -> np.dtype:
        """Return an instance of the related numpy dtype"""
    def kind(self) -> str: ...
    def itemsize(self) -> int:
        """Return the number of bytes in this dtype"""
    @classmethod
    def construct_array_type(cls) -> type_t[ArrowExtensionArray]:
        """
        Return the array type associated with this dtype.

        Returns
        -------
        type
        """
    @classmethod
    def construct_from_string(cls, string: str) -> ArrowDtype:
        '''
        Construct this type from a string.

        Parameters
        ----------
        string : str
            string should follow the format f"{pyarrow_type}[pyarrow]"
            e.g. int64[pyarrow]
        '''
    def __from_arrow__(self, array: pa.Array | pa.ChunkedArray):
        """
        Construct IntegerArray/FloatingArray from pyarrow Array/ChunkedArray.
        """
