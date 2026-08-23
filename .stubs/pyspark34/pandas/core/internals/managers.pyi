import numpy as np
from _typeshed import Incomplete
from pandas._config import using_copy_on_write as using_copy_on_write
from pandas._libs import internals as libinternals, lib as lib
from pandas._libs.internals import BlockPlacement as BlockPlacement, BlockValuesRefs as BlockValuesRefs
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, QuantileInterpolation as QuantileInterpolation, Shape as Shape, npt as npt, type_t as type_t
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.arrays.sparse import SparseDtype as SparseDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.cast import infer_dtype_from_scalar as infer_dtype_from_scalar
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_dtype_equal as is_dtype_equal, is_list_like as is_list_like
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import array_equals as array_equals, isna as isna
from pandas.core.indexers import maybe_convert_indices as maybe_convert_indices
from pandas.core.indexes.api import Index as Index, ensure_index as ensure_index
from pandas.core.internals.base import DataManager as DataManager, SingleDataManager as SingleDataManager, interleaved_dtype as interleaved_dtype
from pandas.core.internals.blocks import Block as Block, NumpyBlock as NumpyBlock, ensure_block_shape as ensure_block_shape, extend_blocks as extend_blocks, get_block_type as get_block_type, new_block as new_block, new_block_2d as new_block_2d
from pandas.core.internals.ops import blockwise_all as blockwise_all, operate_blockwise as operate_blockwise
from pandas.errors import PerformanceWarning as PerformanceWarning
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, Callable, Hashable, Literal, Sequence, TypeVar

T = TypeVar('T', bound='BaseBlockManager')

class BaseBlockManager(DataManager):
    """
    Core internal data structure to implement DataFrame, Series, etc.

    Manage a bunch of labeled 2D mixed-type ndarrays. Essentially it's a
    lightweight blocked set of labeled data to be manipulated by the DataFrame
    public API class

    Attributes
    ----------
    shape
    ndim
    axes
    values
    items

    Methods
    -------
    set_axis(axis, new_labels)
    copy(deep=True)

    get_dtypes

    apply(func, axes, block_filter_fn)

    get_bool_data
    get_numeric_data

    get_slice(slice_like, axis)
    get(label)
    iget(loc)

    take(indexer, axis)
    reindex_axis(new_labels, axis)
    reindex_indexer(new_labels, indexer, axis)

    delete(label)
    insert(loc, label, value)
    set(label, value)

    Parameters
    ----------
    blocks: Sequence of Block
    axes: Sequence of Index
    verify_integrity: bool, default True

    Notes
    -----
    This is *not* a public API class
    """
    blocks: tuple[Block, ...]
    axes: list[Index]
    @property
    def ndim(self) -> int: ...
    def __init__(self, blocks, axes, verify_integrity: bool = True) -> None: ...
    @classmethod
    def from_blocks(cls, blocks: list[Block], axes: list[Index]) -> T: ...
    @property
    def blknos(self) -> npt.NDArray[np.intp]:
        """
        Suppose we want to find the array corresponding to our i'th column.

        blknos[i] identifies the block from self.blocks that contains this column.

        blklocs[i] identifies the column of interest within
        self.blocks[self.blknos[i]]
        """
    @property
    def blklocs(self) -> npt.NDArray[np.intp]:
        """
        See blknos.__doc__
        """
    def make_empty(self, axes: Incomplete | None = None) -> T:
        """return an empty BlockManager with the items axis of len 0"""
    def __nonzero__(self) -> bool: ...
    __bool__ = __nonzero__
    def set_axis(self, axis: AxisInt, new_labels: Index) -> None: ...
    @property
    def is_single_block(self) -> bool: ...
    @property
    def items(self) -> Index: ...
    def add_references(self, mgr: BaseBlockManager) -> None:
        """
        Adds the references from one manager to another. We assume that both
        managers have the same block structure.
        """
    def references_same_values(self, mgr: BaseBlockManager, blkno: int) -> bool:
        """
        Checks if two blocks from two different block managers reference the
        same underlying values.
        """
    def get_dtypes(self): ...
    @property
    def arrays(self) -> list[ArrayLike]:
        """
        Quick access to the backing arrays of the Blocks.

        Only for compatibility with ArrayManager for testing convenience.
        Not to be used in actual code, and return value is not the same as the
        ArrayManager method (list of 1D arrays vs iterator of 2D ndarrays / 1D EAs).

        Warning! The returned arrays don't handle Copy-on-Write, so this should
        be used with caution (only in read-mode).
        """
    def apply(self, f, align_keys: list[str] | None = None, **kwargs) -> T:
        """
        Iterate over the blocks, collect and create a new BlockManager.

        Parameters
        ----------
        f : str or callable
            Name of the Block method to apply.
        align_keys: List[str] or None, default None
        **kwargs
            Keywords to pass to `f`

        Returns
        -------
        BlockManager
        """
    def where(self, other, cond, align: bool) -> T: ...
    def round(self, decimals: int, using_cow: bool = False) -> T: ...
    def setitem(self, indexer, value) -> T:
        """
        Set values with indexer.

        For SingleBlockManager, this backs s[indexer] = value
        """
    def putmask(self, mask, new, align: bool = True): ...
    def diff(self, n: int, axis: AxisInt) -> T: ...
    def interpolate(self, inplace: bool, **kwargs) -> T: ...
    def shift(self, periods: int, axis: AxisInt, fill_value) -> T: ...
    def fillna(self, value, limit, inplace: bool, downcast) -> T: ...
    def astype(self, dtype, copy: bool | None = False, errors: str = 'raise') -> T: ...
    def convert(self, copy: bool | None) -> T: ...
    def replace(self, to_replace, value, inplace: bool) -> T: ...
    def replace_regex(self, **kwargs): ...
    def replace_list(self, src_list: list[Any], dest_list: list[Any], inplace: bool = False, regex: bool = False) -> T:
        """do a list replace"""
    def to_native_types(self, **kwargs) -> T:
        """
        Convert values to native types (strings / python objects) that are used
        in formatting (repr / csv).
        """
    @property
    def is_numeric_mixed_type(self) -> bool: ...
    @property
    def any_extension_types(self) -> bool:
        """Whether any of the blocks in this manager are extension blocks"""
    @property
    def is_view(self) -> bool:
        """return a boolean if we are a single block and are a view"""
    def get_bool_data(self, copy: bool = False) -> T:
        """
        Select blocks that are bool-dtype and columns from object-dtype blocks
        that are all-bool.

        Parameters
        ----------
        copy : bool, default False
            Whether to copy the blocks
        """
    def get_numeric_data(self, copy: bool = False) -> T:
        """
        Parameters
        ----------
        copy : bool, default False
            Whether to copy the blocks
        """
    @property
    def nblocks(self) -> int: ...
    def copy(self, deep: bool | None | Literal['all'] = True) -> T:
        """
        Make deep or shallow copy of BlockManager

        Parameters
        ----------
        deep : bool, string or None, default True
            If False or None, return a shallow copy (do not copy data)
            If 'all', copy data and a deep copy of the index

        Returns
        -------
        BlockManager
        """
    def consolidate(self) -> T:
        """
        Join together blocks having same dtype

        Returns
        -------
        y : BlockManager
        """
    def reindex_indexer(self, new_axis: Index, indexer: npt.NDArray[np.intp] | None, axis: AxisInt, fill_value: Incomplete | None = None, allow_dups: bool = False, copy: bool | None = True, only_slice: bool = False, *, use_na_proxy: bool = False) -> T:
        """
        Parameters
        ----------
        new_axis : Index
        indexer : ndarray[intp] or None
        axis : int
        fill_value : object, default None
        allow_dups : bool, default False
        copy : bool or None, default True
            If None, regard as False to get shallow copy.
        only_slice : bool, default False
            Whether to take views, not copies, along columns.
        use_na_proxy : bool, default False
            Whether to use a np.void ndarray for newly introduced columns.

        pandas-indexer with -1's only.
        """
    def take(self, indexer, axis: AxisInt = 1, verify: bool = True, convert_indices: bool = True) -> T:
        """
        Take items along any axis.

        indexer : np.ndarray or slice
        axis : int, default 1
        verify : bool, default True
            Check that all entries are between 0 and len(self) - 1, inclusive.
            Pass verify=False if this check has been done by the caller.
        convert_indices : bool, default True
            Whether to attempt to convert indices to positive values.

        Returns
        -------
        BlockManager
        """

class BlockManager(libinternals.BlockManager, BaseBlockManager):
    """
    BaseBlockManager that holds 2D blocks.
    """
    ndim: int
    def __init__(self, blocks: Sequence[Block], axes: Sequence[Index], verify_integrity: bool = True) -> None: ...
    @classmethod
    def from_blocks(cls, blocks: list[Block], axes: list[Index]) -> BlockManager:
        """
        Constructor for BlockManager and SingleBlockManager with same signature.
        """
    def fast_xs(self, loc: int) -> SingleBlockManager:
        """
        Return the array corresponding to `frame.iloc[loc]`.

        Parameters
        ----------
        loc : int

        Returns
        -------
        np.ndarray or ExtensionArray
        """
    def iget(self, i: int, track_ref: bool = True) -> SingleBlockManager:
        """
        Return the data as a SingleBlockManager.
        """
    def iget_values(self, i: int) -> ArrayLike:
        """
        Return the data for column i as the values (ndarray or ExtensionArray).

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution.
        """
    @property
    def column_arrays(self) -> list[np.ndarray]:
        """
        Used in the JSON C code to access column arrays.
        This optimizes compared to using `iget_values` by converting each

        Warning! This doesn't handle Copy-on-Write, so should be used with
        caution (current use case of consuming this in the JSON code is fine).
        """
    blocks: Incomplete
    def iset(self, loc: int | slice | np.ndarray, value: ArrayLike, inplace: bool = False):
        """
        Set new item in-place. Does not consolidate. Adds new Block if not
        contained in the current set of items
        """
    def column_setitem(self, loc: int, idx: int | slice | np.ndarray, value, inplace_only: bool = False) -> None:
        '''
        Set values ("setitem") into a single column (not setting the full column).

        This is a method on the BlockManager level, to avoid creating an
        intermediate Series at the DataFrame level (`s = df[loc]; s[idx] = value`)
        '''
    def insert(self, loc: int, item: Hashable, value: ArrayLike) -> None:
        """
        Insert item at selected position.

        Parameters
        ----------
        loc : int
        item : hashable
        value : np.ndarray or ExtensionArray
        """
    def idelete(self, indexer) -> BlockManager:
        """
        Delete selected locations, returning a new BlockManager.
        """
    def grouped_reduce(self, func: Callable) -> T:
        """
        Apply grouped reduction function blockwise, returning a new BlockManager.

        Parameters
        ----------
        func : grouped reduction function

        Returns
        -------
        BlockManager
        """
    def reduce(self, func: Callable) -> T:
        """
        Apply reduction function blockwise, returning a single-row BlockManager.

        Parameters
        ----------
        func : reduction function

        Returns
        -------
        BlockManager
        """
    def operate_blockwise(self, other: BlockManager, array_op) -> BlockManager:
        """
        Apply array_op blockwise with another (aligned) BlockManager.
        """
    def quantile(self, *, qs: Index, axis: AxisInt = 0, interpolation: QuantileInterpolation = 'linear') -> T:
        """
        Iterate over blocks applying quantile reduction.
        This routine is intended for reduction type operations and
        will do inference on the generated blocks.

        Parameters
        ----------
        axis: reduction axis, default 0
        consolidate: bool, default True. Join together blocks having same
            dtype
        interpolation : type of interpolation, default 'linear'
        qs : list of the quantiles to be computed

        Returns
        -------
        BlockManager
        """
    def unstack(self, unstacker, fill_value) -> BlockManager:
        """
        Return a BlockManager with all blocks unstacked.

        Parameters
        ----------
        unstacker : reshape._Unstacker
        fill_value : Any
            fill_value for newly introduced missing values.

        Returns
        -------
        unstacked : BlockManager
        """
    def to_dict(self, copy: bool = True):
        """
        Return a dict of str(dtype) -> BlockManager

        Parameters
        ----------
        copy : bool, default True

        Returns
        -------
        values : a dict of dtype -> BlockManager
        """
    def as_array(self, dtype: np.dtype | None = None, copy: bool = False, na_value: object = ...) -> np.ndarray:
        """
        Convert the blockmanager data into an numpy array.

        Parameters
        ----------
        dtype : np.dtype or None, default None
            Data type of the return array.
        copy : bool, default False
            If True then guarantee that a copy is returned. A value of
            False does not guarantee that the underlying data is not
            copied.
        na_value : object, default lib.no_default
            Value to be used as the missing value sentinel.

        Returns
        -------
        arr : ndarray
        """
    def is_consolidated(self) -> bool:
        """
        Return True if more than one block with the same dtype
        """

class SingleBlockManager(BaseBlockManager, SingleDataManager):
    """manage a single block with"""
    @property
    def ndim(self) -> Literal[1]: ...
    is_single_block: bool
    axes: Incomplete
    blocks: Incomplete
    def __init__(self, block: Block, axis: Index, verify_integrity: bool = False) -> None: ...
    @classmethod
    def from_blocks(cls, blocks: list[Block], axes: list[Index]) -> SingleBlockManager:
        """
        Constructor for BlockManager and SingleBlockManager with same signature.
        """
    @classmethod
    def from_array(cls, array: ArrayLike, index: Index, refs: BlockValuesRefs | None = None) -> SingleBlockManager:
        """
        Constructor for if we have an array that is not yet a Block.
        """
    def to_2d_mgr(self, columns: Index) -> BlockManager:
        """
        Manager analogue of Series.to_frame
        """
    def getitem_mgr(self, indexer: slice | np.ndarray) -> SingleBlockManager: ...
    def get_slice(self, slobj: slice, axis: AxisInt = 0) -> SingleBlockManager: ...
    @property
    def index(self) -> Index: ...
    @property
    def dtype(self) -> DtypeObj: ...
    def get_dtypes(self) -> np.ndarray: ...
    def external_values(self):
        """The array that Series.values returns"""
    def internal_values(self):
        """The array that Series._values returns"""
    def array_values(self):
        """The array that Series.array returns"""
    def get_numeric_data(self, copy: bool = False): ...
    def setitem_inplace(self, indexer, value) -> None:
        """
        Set values with indexer.

        For Single[Block/Array]Manager, this backs s[indexer] = value

        This is an inplace version of `setitem()`, mutating the manager/values
        in place, not returning a new Manager (and Block), and thus never changing
        the dtype.
        """
    def idelete(self, indexer) -> SingleBlockManager:
        """
        Delete single location from SingleBlockManager.

        Ensures that self.blocks doesn't become empty.
        """
    def fast_xs(self, loc) -> None:
        """
        fast path for getting a cross-section
        return a view of the data
        """
    def set_values(self, values: ArrayLike) -> None:
        """
        Set the values of the single block in place.

        Use at your own risk! This does not check if the passed values are
        valid for the current Block/SingleBlockManager (length, dtype, etc).
        """

def create_block_manager_from_blocks(blocks: list[Block], axes: list[Index], consolidate: bool = True, verify_integrity: bool = True) -> BlockManager: ...
def create_block_manager_from_column_arrays(arrays: list[ArrayLike], axes: list[Index], consolidate: bool, refs: list) -> BlockManager: ...
def raise_construction_error(tot_items: int, block_shape: Shape, axes: list[Index], e: ValueError | None = None):
    """raise a helpful message about our construction"""
