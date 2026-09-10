import numpy as np
from _typeshed import Incomplete
from pandas._config import using_copy_on_write as using_copy_on_write
from pandas._libs import internals as libinternals, lib as lib, writers as writers
from pandas._libs.internals import BlockPlacement as BlockPlacement, BlockValuesRefs as BlockValuesRefs
from pandas._libs.missing import NA as NA
from pandas._libs.tslibs import IncompatibleFrequency as IncompatibleFrequency
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, F as F, FillnaOptions as FillnaOptions, IgnoreRaise as IgnoreRaise, QuantileInterpolation as QuantileInterpolation, Shape as Shape, npt as npt
from pandas.core import missing as missing
from pandas.core.api import Index as Index
from pandas.core.array_algos.putmask import extract_bool_array as extract_bool_array, putmask_inplace as putmask_inplace, putmask_without_repeat as putmask_without_repeat, setitem_datetimelike_compat as setitem_datetimelike_compat, validate_putmask as validate_putmask
from pandas.core.array_algos.quantile import quantile_compat as quantile_compat
from pandas.core.array_algos.replace import compare_or_regex_search as compare_or_regex_search, replace_regex as replace_regex, should_use_regex as should_use_regex
from pandas.core.array_algos.transforms import shift as shift
from pandas.core.arrays import Categorical as Categorical, DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, IntervalArray as IntervalArray, PandasArray as PandasArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.arrays.sparse import SparseDtype as SparseDtype
from pandas.core.base import PandasObject as PandasObject
from pandas.core.computation import expressions as expressions
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.astype import astype_array_safe as astype_array_safe, astype_is_view as astype_is_view
from pandas.core.dtypes.cast import LossySetitemError as LossySetitemError, can_hold_element as can_hold_element, find_result_type as find_result_type, maybe_downcast_to_dtype as maybe_downcast_to_dtype, np_can_hold_element as np_can_hold_element
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_1d_only_ea_obj as is_1d_only_ea_obj, is_dtype_equal as is_dtype_equal, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_sparse as is_sparse, is_string_dtype as is_string_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype, PandasDtype as PandasDtype, PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCPandasArray as ABCPandasArray, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexers import check_setitem_lengths as check_setitem_lengths
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, Callable, Iterable, Sequence

def maybe_split(meth: F) -> F:
    """
    If we have a multi-column block, split and operate block-wise.  Otherwise
    use the original method.
    """

class Block(PandasObject):
    """
    Canonical n-dimensional unit of homogeneous dtype contained in a pandas
    data structure

    Index-ignorant; let the container take care of that
    """
    values: np.ndarray | ExtensionArray
    ndim: int
    refs: BlockValuesRefs
    __init__: Callable
    is_numeric: bool
    is_object: bool
    is_extension: bool
    @property
    def is_bool(self) -> bool:
        """
        We can be bool if a) we are bool dtype or b) object dtype with bool objects.
        """
    def external_values(self): ...
    def fill_value(self): ...
    @property
    def mgr_locs(self) -> BlockPlacement: ...
    @mgr_locs.setter
    def mgr_locs(self, new_mgr_locs: BlockPlacement) -> None: ...
    def make_block(self, values, placement: Incomplete | None = None, refs: BlockValuesRefs | None = None) -> Block:
        """
        Create a new block, with type inference propagate any values that are
        not specified
        """
    def make_block_same_class(self, values, placement: BlockPlacement | None = None, refs: BlockValuesRefs | None = None) -> Block:
        """Wrap given values in a block of same type as self."""
    def __len__(self) -> int: ...
    def getitem_block(self, slicer: slice | npt.NDArray[np.intp]) -> Block:
        """
        Perform __getitem__-like, return result as block.

        Only supports slices that preserve dimensionality.
        """
    def getitem_block_columns(self, slicer: slice, new_mgr_locs: BlockPlacement) -> Block:
        """
        Perform __getitem__-like, return result as block.

        Only supports slices that preserve dimensionality.
        """
    def should_store(self, value: ArrayLike) -> bool:
        """
        Should we set self.values[indexer] = value inplace or do we need to cast?

        Parameters
        ----------
        value : np.ndarray or ExtensionArray

        Returns
        -------
        bool
        """
    def apply(self, func, **kwargs) -> list[Block]:
        """
        apply the function to my values; return a block if we are not
        one
        """
    def reduce(self, func) -> list[Block]: ...
    def split_and_operate(self, func, *args, **kwargs) -> list[Block]:
        """
        Split the block and apply func column-by-column.

        Parameters
        ----------
        func : Block method
        *args
        **kwargs

        Returns
        -------
        List[Block]
        """
    def coerce_to_target_dtype(self, other) -> Block:
        """
        coerce the current block to a dtype compat for other
        we will return a block, possibly object, and not raise

        we can also safely try to coerce to the same dtype
        and will receive the same block
        """
    def convert(self, *, copy: bool = True, using_cow: bool = False) -> list[Block]:
        """
        attempt to coerce any object types to better types return a copy
        of the block (if copy = True) by definition we are not an ObjectBlock
        here!
        """
    def dtype(self) -> DtypeObj: ...
    def astype(self, dtype: DtypeObj, copy: bool = False, errors: IgnoreRaise = 'raise', using_cow: bool = False) -> Block:
        """
        Coerce to the new dtype.

        Parameters
        ----------
        dtype : np.dtype or ExtensionDtype
        copy : bool, default False
            copy if indicated
        errors : str, {'raise', 'ignore'}, default 'raise'
            - ``raise`` : allow exceptions to be raised
            - ``ignore`` : suppress exceptions. On error return original object
        using_cow: bool, default False
            Signaling if copy on write copy logic is used.

        Returns
        -------
        Block
        """
    def to_native_types(self, na_rep: str = 'nan', quoting: Incomplete | None = None, **kwargs) -> Block:
        """convert to our native types format"""
    def copy(self, deep: bool = True) -> Block:
        """copy constructor"""
    def replace(self, to_replace, value, inplace: bool = False, mask: npt.NDArray[np.bool_] | None = None, using_cow: bool = False) -> list[Block]:
        """
        replace the to_replace value with value, possible to create new
        blocks here this is just a call to putmask.
        """
    def replace_list(self, src_list: Iterable[Any], dest_list: Sequence[Any], inplace: bool = False, regex: bool = False, using_cow: bool = False) -> list[Block]:
        """
        See BlockManager.replace_list docstring.
        """
    @property
    def shape(self) -> Shape: ...
    def iget(self, i: int | tuple[int, int] | tuple[slice, int]) -> np.ndarray: ...
    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        """
        Modify block values in-place with new item value.

        If copy=True, first copy the underlying values in place before modifying
        (for Copy-on-Write).

        Notes
        -----
        `set_inplace` never creates a new array or new Block, whereas `setitem`
        _may_ create a new array and always creates a new Block.

        Caller is responsible for checking values.dtype == self.dtype.
        """
    def take_nd(self, indexer: npt.NDArray[np.intp], axis: AxisInt, new_mgr_locs: BlockPlacement | None = None, fill_value=...) -> Block:
        """
        Take values according to indexer and return them as a block.
        """
    def setitem(self, indexer, value, using_cow: bool = False) -> Block:
        """
        Attempt self.values[indexer] = value, possibly creating a new array.

        Parameters
        ----------
        indexer : tuple, list-like, array-like, slice, int
            The subset of self.values to set
        value : object
            The value being set
        using_cow: bool, default False
            Signaling if CoW is used.

        Returns
        -------
        Block

        Notes
        -----
        `indexer` is a direct slice/positional indexer. `value` must
        be a compatible shape.
        """
    def putmask(self, mask, new, using_cow: bool = False) -> list[Block]:
        """
        putmask the data to the block; it is possible that we may create a
        new dtype of block

        Return the resulting block(s).

        Parameters
        ----------
        mask : np.ndarray[bool], SparseArray[bool], or BooleanArray
        new : a ndarray/object
        using_cow: bool, default False

        Returns
        -------
        List[Block]
        """
    def where(self, other, cond, _downcast: str | bool = 'infer', using_cow: bool = False) -> list[Block]:
        '''
        evaluate the block; return result block(s) from the result

        Parameters
        ----------
        other : a ndarray/object
        cond : np.ndarray[bool], SparseArray[bool], or BooleanArray
        _downcast : str or None, default "infer"
            Private because we only specify it when calling from fillna.

        Returns
        -------
        List[Block]
        '''
    def fillna(self, value, limit: int | None = None, inplace: bool = False, downcast: Incomplete | None = None, using_cow: bool = False) -> list[Block]:
        """
        fillna on the block with the value. If we fail, then convert to
        ObjectBlock and try again
        """
    def interpolate(self, *, method: FillnaOptions = 'pad', axis: AxisInt = 0, index: Index | None = None, inplace: bool = False, limit: int | None = None, limit_direction: str = 'forward', limit_area: str | None = None, fill_value: Any | None = None, downcast: str | None = None, using_cow: bool = False, **kwargs) -> list[Block]: ...
    def diff(self, n: int, axis: AxisInt = 1) -> list[Block]:
        """return block for the diff of the values"""
    def shift(self, periods: int, axis: AxisInt = 0, fill_value: Any = None) -> list[Block]:
        """shift the block by periods, possibly upcast"""
    def quantile(self, qs: Index, interpolation: QuantileInterpolation = 'linear', axis: AxisInt = 0) -> Block:
        """
        compute the quantiles of the

        Parameters
        ----------
        qs : Index
            The quantiles to be computed in float64.
        interpolation : str, default 'linear'
            Type of interpolation.
        axis : int, default 0
            Axis to compute.

        Returns
        -------
        Block
        """
    def round(self, decimals: int, using_cow: bool = False) -> Block:
        """
        Rounds the values.
        If the block is not of an integer or float dtype, nothing happens.
        This is consistent with DataFrame.round behavivor.
        (Note: Series.round would raise)

        Parameters
        ----------
        decimals: int,
            Number of decimal places to round to.
            Caller is responsible for validating this
        using_cow: bool,
            Whether Copy on Write is enabled right now
        """
    def delete(self, loc) -> list[Block]:
        """Deletes the locs from the block.

        We split the block to avoid copying the underlying data. We create new
        blocks for every connected segment of the initial block that is not deleted.
        The new blocks point to the initial array.
        """
    @property
    def is_view(self) -> bool:
        """return a boolean if I am possibly a view"""
    @property
    def array_values(self) -> ExtensionArray:
        """
        The array that Series.array returns. Always an ExtensionArray.
        """
    def get_values(self, dtype: DtypeObj | None = None) -> np.ndarray:
        """
        return an internal format, currently just the ndarray
        this is often overridden to handle to_dense like operations
        """
    def values_for_json(self) -> np.ndarray: ...

class EABackedBlock(Block):
    """
    Mixin for Block subclasses backed by ExtensionArray.
    """
    values: ExtensionArray
    def setitem(self, indexer, value, using_cow: bool = False):
        """
        Attempt self.values[indexer] = value, possibly creating a new array.

        This differs from Block.setitem by not allowing setitem to change
        the dtype of the Block.

        Parameters
        ----------
        indexer : tuple, list-like, array-like, slice, int
            The subset of self.values to set
        value : object
            The value being set
        using_cow: bool, default False
            Signaling if CoW is used.

        Returns
        -------
        Block

        Notes
        -----
        `indexer` is a direct slice/positional indexer. `value` must
        be a compatible shape.
        """
    def where(self, other, cond, _downcast: str | bool = 'infer', using_cow: bool = False) -> list[Block]: ...
    def putmask(self, mask, new, using_cow: bool = False) -> list[Block]:
        """
        See Block.putmask.__doc__
        """
    def delete(self, loc) -> list[Block]: ...
    def array_values(self) -> ExtensionArray: ...
    def get_values(self, dtype: DtypeObj | None = None) -> np.ndarray:
        """
        return object dtype as boxed values, such as Timestamps/Timedelta
        """
    def values_for_json(self) -> np.ndarray: ...
    def interpolate(self, *, method: FillnaOptions = 'pad', axis: int = 0, inplace: bool = False, limit: int | None = None, fill_value: Incomplete | None = None, using_cow: bool = False, **kwargs): ...

class ExtensionBlock(libinternals.Block, EABackedBlock):
    """
    Block for holding extension types.

    Notes
    -----
    This holds all 3rd-party extension array types. It's also the immediate
    parent class for our internal extension types' blocks.

    ExtensionArrays are limited to 1-D.
    """
    is_extension: bool
    values: ExtensionArray
    def fillna(self, value, limit: int | None = None, inplace: bool = False, downcast: Incomplete | None = None, using_cow: bool = False) -> list[Block]: ...
    def shape(self) -> Shape: ...
    def iget(self, i: int | tuple[int, int] | tuple[slice, int]): ...
    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None: ...
    @property
    def is_view(self) -> bool:
        """Extension arrays are never treated as views."""
    def is_numeric(self): ...
    def getitem_block_index(self, slicer: slice) -> ExtensionBlock:
        """
        Perform __getitem__-like specialized to slicing along index.
        """
    def diff(self, n: int, axis: AxisInt = 1) -> list[Block]: ...
    def shift(self, periods: int, axis: AxisInt = 0, fill_value: Any = None) -> list[Block]:
        """
        Shift the block by `periods`.

        Dispatches to underlying ExtensionArray and re-boxes in an
        ExtensionBlock.
        """

class NumpyBlock(libinternals.NumpyBlock, Block):
    values: np.ndarray
    @property
    def is_view(self) -> bool:
        """return a boolean if I am possibly a view"""
    @property
    def array_values(self) -> ExtensionArray: ...
    def get_values(self, dtype: DtypeObj | None = None) -> np.ndarray: ...
    def values_for_json(self) -> np.ndarray: ...

class NumericBlock(NumpyBlock):
    is_numeric: bool

class NDArrayBackedExtensionBlock(libinternals.NDArrayBackedBlock, EABackedBlock):
    """
    Block backed by an NDArrayBackedExtensionArray
    """
    values: NDArrayBackedExtensionArray
    def is_extension(self) -> bool: ...
    @property
    def is_view(self) -> bool:
        """return a boolean if I am possibly a view"""
    def diff(self, n: int, axis: AxisInt = 0) -> list[Block]:
        """
        1st discrete difference.

        Parameters
        ----------
        n : int
            Number of periods to diff.
        axis : int, default 0
            Axis to diff upon.

        Returns
        -------
        A list with a new Block.

        Notes
        -----
        The arguments here are mimicking shift so they are called correctly
        by apply.
        """
    def shift(self, periods: int, axis: AxisInt = 0, fill_value: Any = None) -> list[Block]: ...

class DatetimeLikeBlock(NDArrayBackedExtensionBlock):
    """Block for datetime64[ns], timedelta64[ns]."""
    is_numeric: bool
    values: DatetimeArray | TimedeltaArray
    def values_for_json(self) -> np.ndarray: ...
    def interpolate(self, *, method: FillnaOptions = 'pad', index: Index | None = None, axis: int = 0, inplace: bool = False, limit: int | None = None, fill_value: Incomplete | None = None, using_cow: bool = False, **kwargs): ...

class DatetimeTZBlock(DatetimeLikeBlock):
    """implement a datetime64 block with a tz attribute"""
    values: DatetimeArray
    is_extension: bool
    values_for_json: Incomplete

class ObjectBlock(NumpyBlock):
    is_object: bool
    def convert(self, *, copy: bool = True, using_cow: bool = False) -> list[Block]:
        """
        attempt to cast any object types to better types return a copy of
        the block (if copy = True) by definition we ARE an ObjectBlock!!!!!
        """

def maybe_coerce_values(values: ArrayLike) -> ArrayLike:
    """
    Input validation for values passed to __init__. Ensure that
    any datetime64/timedelta64 dtypes are in nanoseconds.  Ensure
    that we do not have string dtypes.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray

    Returns
    -------
    values : np.ndarray or ExtensionArray
    """
def get_block_type(dtype: DtypeObj):
    """
    Find the appropriate Block subclass to use for the given values and dtype.

    Parameters
    ----------
    dtype : numpy or pandas dtype

    Returns
    -------
    cls : class, subclass of Block
    """
def new_block_2d(values: ArrayLike, placement: BlockPlacement, refs: BlockValuesRefs | None = None): ...
def new_block(values, placement, *, ndim: int, refs: BlockValuesRefs | None = None) -> Block: ...
def check_ndim(values, placement: BlockPlacement, ndim: int) -> None:
    """
    ndim inference and validation.

    Validates that values.ndim and ndim are consistent.
    Validates that len(values) and len(placement) are consistent.

    Parameters
    ----------
    values : array-like
    placement : BlockPlacement
    ndim : int

    Raises
    ------
    ValueError : the number of dimensions do not match
    """
def extract_pandas_array(values: np.ndarray | ExtensionArray, dtype: DtypeObj | None, ndim: int) -> tuple[np.ndarray | ExtensionArray, DtypeObj | None]:
    """
    Ensure that we don't allow PandasArray / PandasDtype in internals.
    """
def extend_blocks(result, blocks: Incomplete | None = None) -> list[Block]:
    """return a new extended blocks, given the result"""
def ensure_block_shape(values: ArrayLike, ndim: int = 1) -> ArrayLike:
    """
    Reshape if possible to have values.ndim == ndim.
    """
def to_native_types(values: ArrayLike, *, na_rep: str = 'nan', quoting: Incomplete | None = None, float_format: Incomplete | None = None, decimal: str = '.', **kwargs) -> np.ndarray:
    """convert to our native types format"""
def external_values(values: ArrayLike) -> ArrayLike:
    """
    The array that Series.values returns (public attribute).

    This has some historical constraints, and is overridden in block
    subclasses to return the correct array (e.g. period returns
    object ndarray and datetimetz a datetime64[ns] ndarray instead of
    proper extension array).
    """
