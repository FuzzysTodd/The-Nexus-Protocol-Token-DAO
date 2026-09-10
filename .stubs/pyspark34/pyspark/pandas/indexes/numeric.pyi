from pyspark.pandas._typing import Dtype as Dtype, Name as Name
from pyspark.pandas.indexes.base import Index as Index
from pyspark.pandas.series import Series as Series
from typing import Any

class NumericIndex(Index):
    """
    Provide numeric type operations.
    This is an abstract class.
    """
class IntegerIndex(NumericIndex):
    """
    This is an abstract class for Int64Index.
    """

class Int64Index(IntegerIndex):
    """
    Immutable sequence used for indexing and alignment. The basic object
    storing axis labels for all pandas objects. Int64Index is a special case
    of `Index` with purely integer labels.

    .. deprecated:: 3.4.0

    Parameters
    ----------
    data : array-like (1-dimensional)
    dtype : NumPy dtype (default: int64)
    copy : bool
        Make a copy of input ndarray.
    name : object
        Name to be stored in the index.

    See Also
    --------
    Index : The base pandas-on-Spark Index type.
    Float64Index : A special case of :class:`Index` with purely float labels.

    Notes
    -----
    An Index instance can **only** contain hashable objects.

    Examples
    --------
    >>> ps.Int64Index([1, 2, 3])
    Int64Index([1, 2, 3], dtype='int64')

    From a Series:

    >>> s = ps.Series([1, 2, 3], index=[10, 20, 30])
    >>> ps.Int64Index(s)
    Int64Index([1, 2, 3], dtype='int64')

    From an Index:

    >>> idx = ps.Index([1, 2, 3])
    >>> ps.Int64Index(idx)
    Int64Index([1, 2, 3], dtype='int64')
    """
    def __new__(cls, data: Any | None = None, dtype: str | Dtype | None = None, copy: bool = False, name: Name | None = None) -> Int64Index: ...

class Float64Index(NumericIndex):
    """
    Immutable sequence used for indexing and alignment. The basic object
    storing axis labels for all pandas objects. Float64Index is a special case
    of `Index` with purely float labels.

    .. deprecated:: 3.4.0

    Parameters
    ----------
    data : array-like (1-dimensional)
    dtype : NumPy dtype (default: float64)
    copy : bool
        Make a copy of input ndarray.
    name : object
        Name to be stored in the index.

    See Also
    --------
    Index : The base pandas-on-Spark Index type.
    Int64Index : A special case of :class:`Index` with purely integer labels.

    Notes
    -----
    An Index instance can **only** contain hashable objects.

    Examples
    --------
    >>> ps.Float64Index([1.0, 2.0, 3.0])
    Float64Index([1.0, 2.0, 3.0], dtype='float64')

    From a Series:

    >>> s = ps.Series([1, 2, 3], index=[10, 20, 30])
    >>> ps.Float64Index(s)
    Float64Index([1.0, 2.0, 3.0], dtype='float64')

    From an Index:

    >>> idx = ps.Index([1, 2, 3])
    >>> ps.Float64Index(idx)
    Float64Index([1.0, 2.0, 3.0], dtype='float64')
    """
    def __new__(cls, data: Any | None = None, dtype: str | Dtype | None = None, copy: bool = False, name: Name | None = None) -> Float64Index: ...
