import numpy as np
from _typeshed import Incomplete
from pandas import Series as Series
from pandas._libs import lib as lib
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, Dtype as Dtype, F as F, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, PositionalIndexer2D as PositionalIndexer2D, PositionalIndexerTuple as PositionalIndexerTuple, ScalarIndexer as ScalarIndexer, SequenceIndexer as SequenceIndexer, Shape as Shape, TakeIndexer as TakeIndexer, npt as npt, type_t as type_t
from pandas.core import missing as missing
from pandas.core.algorithms import take as take, unique as unique, value_counts as value_counts
from pandas.core.array_algos.quantile import quantile_with_mask as quantile_with_mask
from pandas.core.array_algos.transforms import shift as shift
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.common import is_dtype_equal as is_dtype_equal, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype, PeriodDtype as PeriodDtype
from pandas.core.dtypes.missing import array_equivalent as array_equivalent
from pandas.core.indexers import check_array_indexer as check_array_indexer
from pandas.core.sorting import nargminmax as nargminmax
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.util._decorators import doc as doc
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg, validate_fillna_kwargs as validate_fillna_kwargs, validate_insert_loc as validate_insert_loc
from typing import Any, Literal, TypeVar, overload

NDArrayBackedExtensionArrayT = TypeVar('NDArrayBackedExtensionArrayT', bound='NDArrayBackedExtensionArray')

def ravel_compat(meth: F) -> F:
    """
    Decorator to ravel a 2D array before passing it to a cython operation,
    then reshape the result to our own shape.
    """

class NDArrayBackedExtensionArray(NDArrayBacked, ExtensionArray):
    """
    ExtensionArray that is backed by a single NumPy ndarray.
    """
    def view(self, dtype: Dtype | None = None) -> ArrayLike: ...
    def take(self, indices: TakeIndexer, *, allow_fill: bool = False, fill_value: Any = None, axis: AxisInt = 0) -> NDArrayBackedExtensionArrayT: ...
    def equals(self, other) -> bool: ...
    def argmin(self, axis: AxisInt = 0, skipna: bool = True): ...
    def argmax(self, axis: AxisInt = 0, skipna: bool = True): ...
    def unique(self) -> NDArrayBackedExtensionArrayT: ...
    def searchsorted(self, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right'] = 'left', sorter: NumpySorter = None) -> npt.NDArray[np.intp] | np.intp: ...
    def shift(self, periods: int = 1, fill_value: Incomplete | None = None, axis: AxisInt = 0): ...
    def __setitem__(self, key, value) -> None: ...
    @overload
    def __getitem__(self, key: ScalarIndexer) -> Any: ...
    @overload
    def __getitem__(self, key: SequenceIndexer | PositionalIndexerTuple) -> NDArrayBackedExtensionArrayT: ...
    def fillna(self, value: Incomplete | None = None, method: Incomplete | None = None, limit: Incomplete | None = None) -> NDArrayBackedExtensionArrayT: ...
    def insert(self, loc: int, item) -> NDArrayBackedExtensionArrayT:
        """
        Make new ExtensionArray inserting new item at location. Follows
        Python list.append semantics for negative values.

        Parameters
        ----------
        loc : int
        item : object

        Returns
        -------
        type(self)
        """
    def value_counts(self, dropna: bool = True) -> Series:
        """
        Return a Series containing counts of unique values.

        Parameters
        ----------
        dropna : bool, default True
            Don't include counts of NA values.

        Returns
        -------
        Series
        """
