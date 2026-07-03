from _typeshed import Incomplete
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, Shape as Shape
from pandas.core.base import PandasObject as PandasObject
from pandas.core.dtypes.cast import find_common_type as find_common_type, np_can_hold_element as np_can_hold_element
from pandas.core.indexes.api import Index as Index, default_index as default_index
from pandas.errors import AbstractMethodError as AbstractMethodError
from typing import Literal, TypeVar

T = TypeVar('T', bound='DataManager')

class DataManager(PandasObject):
    axes: list[Index]
    @property
    def items(self) -> Index: ...
    def __len__(self) -> int: ...
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self) -> Shape: ...
    def reindex_indexer(self, new_axis, indexer, axis: AxisInt, fill_value: Incomplete | None = None, allow_dups: bool = False, copy: bool = True, only_slice: bool = False) -> T: ...
    def reindex_axis(self, new_index: Index, axis: AxisInt, fill_value: Incomplete | None = None, only_slice: bool = False) -> T:
        """
        Conform data manager to new index.
        """
    def equals(self, other: object) -> bool:
        """
        Implementation for DataFrame.equals
        """
    def apply(self, f, align_keys: list[str] | None = None, **kwargs) -> T: ...
    def isna(self, func) -> T: ...
    def is_consolidated(self) -> bool: ...
    def consolidate(self) -> T: ...

class SingleDataManager(DataManager):
    @property
    def ndim(self) -> Literal[1]: ...
    @property
    def array(self) -> ArrayLike:
        """
        Quick access to the backing array of the Block or SingleArrayManager.
        """
    def setitem_inplace(self, indexer, value) -> None:
        """
        Set values with indexer.

        For Single[Block/Array]Manager, this backs s[indexer] = value

        This is an inplace version of `setitem()`, mutating the manager/values
        in place, not returning a new Manager (and Block), and thus never changing
        the dtype.
        """
    def grouped_reduce(self, func): ...
    @classmethod
    def from_array(cls, arr: ArrayLike, index: Index): ...

def interleaved_dtype(dtypes: list[DtypeObj]) -> DtypeObj | None:
    """
    Find the common dtype for `blocks`.

    Parameters
    ----------
    blocks : List[DtypeObj]

    Returns
    -------
    dtype : np.dtype, ExtensionDtype, or None
        None is returned when `blocks` is empty.
    """
