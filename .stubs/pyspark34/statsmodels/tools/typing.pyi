from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike, DTypeLike as DTypeLike, NDArray as NDArray
from pandas import DataFrame, Series
from typing import Sequence

__all__ = ['ArrayLike', 'DTypeLike', 'Float64Array', 'ArrayLike1D', 'ArrayLike2D', 'NDArray', 'NumericArray']

NumericArray: Incomplete
Float64Array: Incomplete
ArrayLike1D = Sequence[float | int] | NumericArray | Series
ArrayLike2D = Sequence[Sequence[float | int]] | NumericArray | DataFrame
