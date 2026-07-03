import numpy as np
from _typeshed import Incomplete
from pandas import CategoricalIndex as CategoricalIndex, DataFrame as DataFrame, Series as Series
from pandas._config import get_option as get_option
from pandas._libs import index as libindex, lib as lib
from pandas._libs.hashtable import duplicated as duplicated
from pandas._typing import AnyAll as AnyAll, AnyArrayLike as AnyArrayLike, Axis as Axis, DropKeep as DropKeep, DtypeObj as DtypeObj, F as F, IgnoreRaise as IgnoreRaise, IndexLabel as IndexLabel, Scalar as Scalar, Shape as Shape, npt as npt
from pandas.core.array_algos.putmask import validate_putmask as validate_putmask
from pandas.core.arrays import Categorical as Categorical
from pandas.core.arrays.categorical import factorize_from_iterables as factorize_from_iterables
from pandas.core.dtypes.cast import coerce_indexer_dtype as coerce_indexer_dtype
from pandas.core.dtypes.common import ensure_int64 as ensure_int64, ensure_platform_int as ensure_platform_int, is_categorical_dtype as is_categorical_dtype, is_extension_array_dtype as is_extension_array_dtype, is_hashable as is_hashable, is_integer as is_integer, is_iterator as is_iterator, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_scalar as is_scalar, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCDatetimeIndex as ABCDatetimeIndex, ABCTimedeltaIndex as ABCTimedeltaIndex
from pandas.core.dtypes.missing import array_equivalent as array_equivalent, isna as isna
from pandas.core.indexes.base import Index as Index, ensure_index as ensure_index, get_unanimous_names as get_unanimous_names
from pandas.core.indexes.frozen import FrozenList as FrozenList
from pandas.core.ops.invalid import make_invalid_op as make_invalid_op
from pandas.core.sorting import get_group_index as get_group_index, indexer_from_factorized as indexer_from_factorized, lexsort_indexer as lexsort_indexer
from pandas.errors import InvalidIndexError as InvalidIndexError, PerformanceWarning as PerformanceWarning, UnsortedIndexError as UnsortedIndexError
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.util._decorators import Appender as Appender, cache_readonly as cache_readonly, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Any, Callable, Hashable, Iterable, Literal, Sequence

class MultiIndexUIntEngine(libindex.BaseMultiIndexCodesEngine, libindex.UInt64Engine):
    """
    This class manages a MultiIndex by mapping label combinations to positive
    integers.
    """
class MultiIndexPyIntEngine(libindex.BaseMultiIndexCodesEngine, libindex.ObjectEngine):
    """
    This class manages those (extreme) cases in which the number of possible
    label combinations overflows the 64 bits integers, and uses an ObjectEngine
    containing Python integers.
    """

def names_compat(meth: F) -> F:
    """
    A decorator to allow either `name` or `names` keyword but not both.

    This makes it easier to share code with base class.
    """

class MultiIndex(Index):
    """
    A multi-level, or hierarchical, index object for pandas objects.

    Parameters
    ----------
    levels : sequence of arrays
        The unique labels for each level.
    codes : sequence of arrays
        Integers for each level designating which label at each location.
    sortorder : optional int
        Level of sortedness (must be lexicographically sorted by that
        level).
    names : optional sequence of objects
        Names for each of the index levels. (name is accepted for compat).
    copy : bool, default False
        Copy the meta-data.
    verify_integrity : bool, default True
        Check that the levels/codes are consistent and valid.

    Attributes
    ----------
    names
    levels
    codes
    nlevels
    levshape
    dtypes

    Methods
    -------
    from_arrays
    from_tuples
    from_product
    from_frame
    set_levels
    set_codes
    to_frame
    to_flat_index
    sortlevel
    droplevel
    swaplevel
    reorder_levels
    remove_unused_levels
    get_level_values
    get_indexer
    get_loc
    get_locs
    get_loc_level
    drop

    See Also
    --------
    MultiIndex.from_arrays  : Convert list of arrays to MultiIndex.
    MultiIndex.from_product : Create a MultiIndex from the cartesian product
                              of iterables.
    MultiIndex.from_tuples  : Convert list of tuples to a MultiIndex.
    MultiIndex.from_frame   : Make a MultiIndex from a DataFrame.
    Index : The base pandas Index type.

    Notes
    -----
    See the `user guide
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html>`__
    for more.

    Examples
    --------
    A new ``MultiIndex`` is typically constructed using one of the helper
    methods :meth:`MultiIndex.from_arrays`, :meth:`MultiIndex.from_product`
    and :meth:`MultiIndex.from_tuples`. For example (using ``.from_arrays``):

    >>> arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
    >>> pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
    MultiIndex([(1,  'red'),
                (1, 'blue'),
                (2,  'red'),
                (2, 'blue')],
               names=['number', 'color'])

    See further examples for how to construct a MultiIndex in the doc strings
    of the mentioned helper methods.
    """
    sortorder: int | None
    def __new__(cls, levels: Incomplete | None = None, codes: Incomplete | None = None, sortorder: Incomplete | None = None, names: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False, name: Incomplete | None = None, verify_integrity: bool = True) -> MultiIndex: ...
    @classmethod
    def from_arrays(cls, arrays, sortorder: Incomplete | None = None, names: Sequence[Hashable] | Hashable | lib.NoDefault = ...) -> MultiIndex:
        """
        Convert arrays to MultiIndex.

        Parameters
        ----------
        arrays : list / sequence of array-likes
            Each array-like gives one level's value for each data point.
            len(arrays) is the number of levels.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that
            level).
        names : list / sequence of str, optional
            Names for the levels in the index.

        Returns
        -------
        MultiIndex

        See Also
        --------
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex.
        MultiIndex.from_product : Make a MultiIndex from cartesian product
                                  of iterables.
        MultiIndex.from_frame : Make a MultiIndex from a DataFrame.

        Examples
        --------
        >>> arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
        >>> pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
        MultiIndex([(1,  'red'),
                    (1, 'blue'),
                    (2,  'red'),
                    (2, 'blue')],
                   names=['number', 'color'])
        """
    @classmethod
    def from_tuples(cls, tuples: Iterable[tuple[Hashable, ...]], sortorder: int | None = None, names: Sequence[Hashable] | Hashable = None) -> MultiIndex:
        """
        Convert list of tuples to MultiIndex.

        Parameters
        ----------
        tuples : list / sequence of tuple-likes
            Each tuple is the index of one row/column.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that
            level).
        names : list / sequence of str, optional
            Names for the levels in the index.

        Returns
        -------
        MultiIndex

        See Also
        --------
        MultiIndex.from_arrays : Convert list of arrays to MultiIndex.
        MultiIndex.from_product : Make a MultiIndex from cartesian product
                                  of iterables.
        MultiIndex.from_frame : Make a MultiIndex from a DataFrame.

        Examples
        --------
        >>> tuples = [(1, 'red'), (1, 'blue'),
        ...           (2, 'red'), (2, 'blue')]
        >>> pd.MultiIndex.from_tuples(tuples, names=('number', 'color'))
        MultiIndex([(1,  'red'),
                    (1, 'blue'),
                    (2,  'red'),
                    (2, 'blue')],
                   names=['number', 'color'])
        """
    @classmethod
    def from_product(cls, iterables: Sequence[Iterable[Hashable]], sortorder: int | None = None, names: Sequence[Hashable] | Hashable | lib.NoDefault = ...) -> MultiIndex:
        """
        Make a MultiIndex from the cartesian product of multiple iterables.

        Parameters
        ----------
        iterables : list / sequence of iterables
            Each iterable has unique labels for each level of the index.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that
            level).
        names : list / sequence of str, optional
            Names for the levels in the index.
            If not explicitly provided, names will be inferred from the
            elements of iterables if an element has a name attribute.

        Returns
        -------
        MultiIndex

        See Also
        --------
        MultiIndex.from_arrays : Convert list of arrays to MultiIndex.
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex.
        MultiIndex.from_frame : Make a MultiIndex from a DataFrame.

        Examples
        --------
        >>> numbers = [0, 1, 2]
        >>> colors = ['green', 'purple']
        >>> pd.MultiIndex.from_product([numbers, colors],
        ...                            names=['number', 'color'])
        MultiIndex([(0,  'green'),
                    (0, 'purple'),
                    (1,  'green'),
                    (1, 'purple'),
                    (2,  'green'),
                    (2, 'purple')],
                   names=['number', 'color'])
        """
    @classmethod
    def from_frame(cls, df: DataFrame, sortorder: Incomplete | None = None, names: Incomplete | None = None) -> MultiIndex:
        """
        Make a MultiIndex from a DataFrame.

        Parameters
        ----------
        df : DataFrame
            DataFrame to be converted to MultiIndex.
        sortorder : int, optional
            Level of sortedness (must be lexicographically sorted by that
            level).
        names : list-like, optional
            If no names are provided, use the column names, or tuple of column
            names if the columns is a MultiIndex. If a sequence, overwrite
            names with the given sequence.

        Returns
        -------
        MultiIndex
            The MultiIndex representation of the given DataFrame.

        See Also
        --------
        MultiIndex.from_arrays : Convert list of arrays to MultiIndex.
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex.
        MultiIndex.from_product : Make a MultiIndex from cartesian product
                                  of iterables.

        Examples
        --------
        >>> df = pd.DataFrame([['HI', 'Temp'], ['HI', 'Precip'],
        ...                    ['NJ', 'Temp'], ['NJ', 'Precip']],
        ...                   columns=['a', 'b'])
        >>> df
              a       b
        0    HI    Temp
        1    HI  Precip
        2    NJ    Temp
        3    NJ  Precip

        >>> pd.MultiIndex.from_frame(df)
        MultiIndex([('HI',   'Temp'),
                    ('HI', 'Precip'),
                    ('NJ',   'Temp'),
                    ('NJ', 'Precip')],
                   names=['a', 'b'])

        Using explicit names, instead of the column names

        >>> pd.MultiIndex.from_frame(df, names=['state', 'observation'])
        MultiIndex([('HI',   'Temp'),
                    ('HI', 'Precip'),
                    ('NJ',   'Temp'),
                    ('NJ', 'Precip')],
                   names=['state', 'observation'])
        """
    @property
    def values(self) -> np.ndarray: ...
    @property
    def array(self) -> None:
        """
        Raises a ValueError for `MultiIndex` because there's no single
        array backing a MultiIndex.

        Raises
        ------
        ValueError
        """
    def dtypes(self) -> Series:
        """
        Return the dtypes as a Series for the underlying MultiIndex.
        """
    def __len__(self) -> int: ...
    @property
    def size(self) -> int:
        """
        Return the number of elements in the underlying data.
        """
    def levels(self) -> FrozenList: ...
    def set_levels(self, levels, *, level: Incomplete | None = None, verify_integrity: bool = True) -> MultiIndex:
        '''
        Set new levels on MultiIndex. Defaults to returning new index.

        Parameters
        ----------
        levels : sequence or list of sequence
            New level(s) to apply.
        level : int, level name, or sequence of int/level names (default None)
            Level(s) to set (None for all levels).
        verify_integrity : bool, default True
            If True, checks that levels and codes are compatible.

        Returns
        -------
        MultiIndex

        Examples
        --------
        >>> idx = pd.MultiIndex.from_tuples(
        ...     [
        ...         (1, "one"),
        ...         (1, "two"),
        ...         (2, "one"),
        ...         (2, "two"),
        ...         (3, "one"),
        ...         (3, "two")
        ...     ],
        ...     names=["foo", "bar"]
        ... )
        >>> idx
        MultiIndex([(1, \'one\'),
            (1, \'two\'),
            (2, \'one\'),
            (2, \'two\'),
            (3, \'one\'),
            (3, \'two\')],
           names=[\'foo\', \'bar\'])

        >>> idx.set_levels([[\'a\', \'b\', \'c\'], [1, 2]])
        MultiIndex([(\'a\', 1),
                    (\'a\', 2),
                    (\'b\', 1),
                    (\'b\', 2),
                    (\'c\', 1),
                    (\'c\', 2)],
                   names=[\'foo\', \'bar\'])
        >>> idx.set_levels([\'a\', \'b\', \'c\'], level=0)
        MultiIndex([(\'a\', \'one\'),
                    (\'a\', \'two\'),
                    (\'b\', \'one\'),
                    (\'b\', \'two\'),
                    (\'c\', \'one\'),
                    (\'c\', \'two\')],
                   names=[\'foo\', \'bar\'])
        >>> idx.set_levels([\'a\', \'b\'], level=\'bar\')
        MultiIndex([(1, \'a\'),
                    (1, \'b\'),
                    (2, \'a\'),
                    (2, \'b\'),
                    (3, \'a\'),
                    (3, \'b\')],
                   names=[\'foo\', \'bar\'])

        If any of the levels passed to ``set_levels()`` exceeds the
        existing length, all of the values from that argument will
        be stored in the MultiIndex levels, though the values will
        be truncated in the MultiIndex output.

        >>> idx.set_levels([[\'a\', \'b\', \'c\'], [1, 2, 3, 4]], level=[0, 1])
        MultiIndex([(\'a\', 1),
            (\'a\', 2),
            (\'b\', 1),
            (\'b\', 2),
            (\'c\', 1),
            (\'c\', 2)],
           names=[\'foo\', \'bar\'])
        >>> idx.set_levels([[\'a\', \'b\', \'c\'], [1, 2, 3, 4]], level=[0, 1]).levels
        FrozenList([[\'a\', \'b\', \'c\'], [1, 2, 3, 4]])
        '''
    @property
    def nlevels(self) -> int:
        """
        Integer number of levels in this MultiIndex.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([['a'], ['b'], ['c']])
        >>> mi
        MultiIndex([('a', 'b', 'c')],
                   )
        >>> mi.nlevels
        3
        """
    @property
    def levshape(self) -> Shape:
        """
        A tuple with the length of each level.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([['a'], ['b'], ['c']])
        >>> mi
        MultiIndex([('a', 'b', 'c')],
                   )
        >>> mi.levshape
        (1, 1, 1)
        """
    @property
    def codes(self): ...
    def set_codes(self, codes, *, level: Incomplete | None = None, verify_integrity: bool = True):
        '''
        Set new codes on MultiIndex. Defaults to returning new index.

        Parameters
        ----------
        codes : sequence or list of sequence
            New codes to apply.
        level : int, level name, or sequence of int/level names (default None)
            Level(s) to set (None for all levels).
        verify_integrity : bool, default True
            If True, checks that levels and codes are compatible.

        Returns
        -------
        new index (of same type and class...etc) or None
            The same type as the caller or None if ``inplace=True``.

        Examples
        --------
        >>> idx = pd.MultiIndex.from_tuples(
        ...     [(1, "one"), (1, "two"), (2, "one"), (2, "two")], names=["foo", "bar"]
        ... )
        >>> idx
        MultiIndex([(1, \'one\'),
            (1, \'two\'),
            (2, \'one\'),
            (2, \'two\')],
           names=[\'foo\', \'bar\'])

        >>> idx.set_codes([[1, 0, 1, 0], [0, 0, 1, 1]])
        MultiIndex([(2, \'one\'),
                    (1, \'one\'),
                    (2, \'two\'),
                    (1, \'two\')],
                   names=[\'foo\', \'bar\'])
        >>> idx.set_codes([1, 0, 1, 0], level=0)
        MultiIndex([(2, \'one\'),
                    (1, \'two\'),
                    (2, \'one\'),
                    (1, \'two\')],
                   names=[\'foo\', \'bar\'])
        >>> idx.set_codes([0, 0, 1, 1], level=\'bar\')
        MultiIndex([(1, \'one\'),
                    (1, \'one\'),
                    (2, \'two\'),
                    (2, \'two\')],
                   names=[\'foo\', \'bar\'])
        >>> idx.set_codes([[1, 0, 1, 0], [0, 0, 1, 1]], level=[0, 1])
        MultiIndex([(2, \'one\'),
                    (1, \'one\'),
                    (2, \'two\'),
                    (1, \'two\')],
                   names=[\'foo\', \'bar\'])
        '''
    def copy(self, names: Incomplete | None = None, deep: bool = False, name: Incomplete | None = None):
        """
        Make a copy of this object.

        Names, dtype, levels and codes can be passed and will be set on new copy.

        Parameters
        ----------
        names : sequence, optional
        deep : bool, default False
        name : Label
            Kept for compatibility with 1-dimensional Index. Should not be used.

        Returns
        -------
        MultiIndex

        Notes
        -----
        In most cases, there should be no functional difference from using
        ``deep``, but if ``deep`` is passed it will attempt to deepcopy.
        This could be potentially expensive on large MultiIndex objects.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([['a'], ['b'], ['c']])
        >>> mi
        MultiIndex([('a', 'b', 'c')],
                   )
        >>> mi.copy()
        MultiIndex([('a', 'b', 'c')],
                   )
        """
    def __array__(self, dtype: Incomplete | None = None) -> np.ndarray:
        """the array interface, return my values"""
    def view(self, cls: Incomplete | None = None):
        """this is defined as a copy with the same identity"""
    def __contains__(self, key: Any) -> bool: ...
    def dtype(self) -> np.dtype: ...
    def memory_usage(self, deep: bool = False) -> int: ...
    def nbytes(self) -> int:
        """return the number of bytes in the underlying data"""
    def format(self, name: bool | None = None, formatter: Callable | None = None, na_rep: str | None = None, names: bool = False, space: int = 2, sparsify: Incomplete | None = None, adjoin: bool = True) -> list: ...
    names: Incomplete
    def inferred_type(self) -> str: ...
    def is_monotonic_increasing(self) -> bool:
        """
        Return a boolean if the values are equal or increasing.
        """
    def is_monotonic_decreasing(self) -> bool:
        """
        Return a boolean if the values are equal or decreasing.
        """
    def duplicated(self, keep: DropKeep = 'first') -> npt.NDArray[np.bool_]: ...
    def fillna(self, value: Incomplete | None = None, downcast: Incomplete | None = None) -> None:
        """
        fillna is not implemented for MultiIndex
        """
    def dropna(self, how: AnyAll = 'any') -> MultiIndex: ...
    def get_level_values(self, level):
        """
        Return vector of label values for requested level.

        Length of returned vector is equal to the length of the index.

        Parameters
        ----------
        level : int or str
            ``level`` is either the integer position of the level in the
            MultiIndex, or the name of the level.

        Returns
        -------
        Index
            Values is a level of this MultiIndex converted to
            a single :class:`Index` (or subclass thereof).

        Notes
        -----
        If the level contains missing values, the result may be casted to
        ``float`` with missing values specified as ``NaN``. This is because
        the level is converted to a regular ``Index``.

        Examples
        --------
        Create a MultiIndex:

        >>> mi = pd.MultiIndex.from_arrays((list('abc'), list('def')))
        >>> mi.names = ['level_1', 'level_2']

        Get level values by supplying level as either integer or name:

        >>> mi.get_level_values(0)
        Index(['a', 'b', 'c'], dtype='object', name='level_1')
        >>> mi.get_level_values('level_2')
        Index(['d', 'e', 'f'], dtype='object', name='level_2')

        If a level contains missing values, the return type of the level
        may be cast to ``float``.

        >>> pd.MultiIndex.from_arrays([[1, None, 2], [3, 4, 5]]).dtypes
        level_0    int64
        level_1    int64
        dtype: object
        >>> pd.MultiIndex.from_arrays([[1, None, 2], [3, 4, 5]]).get_level_values(0)
        Index([1.0, nan, 2.0], dtype='float64')
        """
    def unique(self, level: Incomplete | None = None): ...
    def to_frame(self, index: bool = True, name=..., allow_duplicates: bool = False) -> DataFrame:
        """
        Create a DataFrame with the levels of the MultiIndex as columns.

        Column ordering is determined by the DataFrame constructor with data as
        a dict.

        Parameters
        ----------
        index : bool, default True
            Set the index of the returned DataFrame as the original MultiIndex.

        name : list / sequence of str, optional
            The passed names should substitute index level names.

        allow_duplicates : bool, optional default False
            Allow duplicate column labels to be created.

            .. versionadded:: 1.5.0

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame : Two-dimensional, size-mutable, potentially heterogeneous
            tabular data.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([['a', 'b'], ['c', 'd']])
        >>> mi
        MultiIndex([('a', 'c'),
                    ('b', 'd')],
                   )

        >>> df = mi.to_frame()
        >>> df
             0  1
        a c  a  c
        b d  b  d

        >>> df = mi.to_frame(index=False)
        >>> df
           0  1
        0  a  c
        1  b  d

        >>> df = mi.to_frame(name=['x', 'y'])
        >>> df
             x  y
        a c  a  c
        b d  b  d
        """
    def to_flat_index(self) -> Index:
        """
        Convert a MultiIndex to an Index of Tuples containing the level values.

        Returns
        -------
        pd.Index
            Index with the MultiIndex data represented in Tuples.

        See Also
        --------
        MultiIndex.from_tuples : Convert flat index back to MultiIndex.

        Notes
        -----
        This method will simply return the caller if called by anything other
        than a MultiIndex.

        Examples
        --------
        >>> index = pd.MultiIndex.from_product(
        ...     [['foo', 'bar'], ['baz', 'qux']],
        ...     names=['a', 'b'])
        >>> index.to_flat_index()
        Index([('foo', 'baz'), ('foo', 'qux'),
               ('bar', 'baz'), ('bar', 'qux')],
              dtype='object')
        """
    def remove_unused_levels(self) -> MultiIndex:
        """
        Create new MultiIndex from current that removes unused levels.

        Unused level(s) means levels that are not expressed in the
        labels. The resulting MultiIndex will have the same outward
        appearance, meaning the same .values and ordering. It will
        also be .equals() to the original.

        Returns
        -------
        MultiIndex

        Examples
        --------
        >>> mi = pd.MultiIndex.from_product([range(2), list('ab')])
        >>> mi
        MultiIndex([(0, 'a'),
                    (0, 'b'),
                    (1, 'a'),
                    (1, 'b')],
                   )

        >>> mi[2:]
        MultiIndex([(1, 'a'),
                    (1, 'b')],
                   )

        The 0 from the first level is not represented
        and can be removed

        >>> mi2 = mi[2:].remove_unused_levels()
        >>> mi2.levels
        FrozenList([[1], ['a', 'b']])
        """
    def __reduce__(self):
        """Necessary for making this object picklable"""
    def __getitem__(self, key): ...
    def take(self, indices, axis: Axis = 0, allow_fill: bool = True, fill_value: Incomplete | None = None, **kwargs) -> MultiIndex: ...
    def append(self, other):
        """
        Append a collection of Index options together.

        Parameters
        ----------
        other : Index or list/tuple of indices

        Returns
        -------
        Index
            The combined index.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([['a'], ['b']])
        >>> mi
        MultiIndex([('a', 'b')],
                   )
        >>> mi.append(mi)
        MultiIndex([('a', 'b'), ('a', 'b')],
                   )
        """
    def argsort(self, *args, **kwargs) -> npt.NDArray[np.intp]: ...
    def repeat(self, repeats: int, axis: Incomplete | None = None) -> MultiIndex: ...
    def drop(self, codes, level: Index | np.ndarray | Iterable[Hashable] | None = None, errors: IgnoreRaise = 'raise') -> MultiIndex:
        """
        Make new MultiIndex with passed list of codes deleted.

        Parameters
        ----------
        codes : array-like
            Must be a list of tuples when level is not specified.
        level : int or level name, default None
        errors : str, default 'raise'

        Returns
        -------
        MultiIndex
        """
    def swaplevel(self, i: int = -2, j: int = -1) -> MultiIndex:
        """
        Swap level i with level j.

        Calling this method does not change the ordering of the values.

        Parameters
        ----------
        i : int, str, default -2
            First level of index to be swapped. Can pass level name as string.
            Type of parameters can be mixed.
        j : int, str, default -1
            Second level of index to be swapped. Can pass level name as string.
            Type of parameters can be mixed.

        Returns
        -------
        MultiIndex
            A new MultiIndex.

        See Also
        --------
        Series.swaplevel : Swap levels i and j in a MultiIndex.
        DataFrame.swaplevel : Swap levels i and j in a MultiIndex on a
            particular axis.

        Examples
        --------
        >>> mi = pd.MultiIndex(levels=[['a', 'b'], ['bb', 'aa']],
        ...                    codes=[[0, 0, 1, 1], [0, 1, 0, 1]])
        >>> mi
        MultiIndex([('a', 'bb'),
                    ('a', 'aa'),
                    ('b', 'bb'),
                    ('b', 'aa')],
                   )
        >>> mi.swaplevel(0, 1)
        MultiIndex([('bb', 'a'),
                    ('aa', 'a'),
                    ('bb', 'b'),
                    ('aa', 'b')],
                   )
        """
    def reorder_levels(self, order) -> MultiIndex:
        """
        Rearrange levels using input order. May not drop or duplicate levels.

        Parameters
        ----------
        order : list of int or list of str
            List representing new level order. Reference level by number
            (position) or by key (label).

        Returns
        -------
        MultiIndex

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([[1, 2], [3, 4]], names=['x', 'y'])
        >>> mi
        MultiIndex([(1, 3),
                    (2, 4)],
                   names=['x', 'y'])

        >>> mi.reorder_levels(order=[1, 0])
        MultiIndex([(3, 1),
                    (4, 2)],
                   names=['y', 'x'])

        >>> mi.reorder_levels(order=['y', 'x'])
        MultiIndex([(3, 1),
                    (4, 2)],
                   names=['y', 'x'])
        """
    def sortlevel(self, level: IndexLabel = 0, ascending: bool | list[bool] = True, sort_remaining: bool = True) -> tuple[MultiIndex, npt.NDArray[np.intp]]:
        """
        Sort MultiIndex at the requested level.

        The result will respect the original ordering of the associated
        factor at that level.

        Parameters
        ----------
        level : list-like, int or str, default 0
            If a string is given, must be a name of the level.
            If list-like must be names or ints of levels.
        ascending : bool, default True
            False to sort in descending order.
            Can also be a list to specify a directed ordering.
        sort_remaining : sort by the remaining levels after level

        Returns
        -------
        sorted_index : pd.MultiIndex
            Resulting index.
        indexer : np.ndarray[np.intp]
            Indices of output values in original index.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([[0, 0], [2, 1]])
        >>> mi
        MultiIndex([(0, 2),
                    (0, 1)],
                   )

        >>> mi.sortlevel()
        (MultiIndex([(0, 1),
                    (0, 2)],
                   ), array([1, 0]))

        >>> mi.sortlevel(sort_remaining=False)
        (MultiIndex([(0, 2),
                    (0, 1)],
                   ), array([0, 1]))

        >>> mi.sortlevel(1)
        (MultiIndex([(0, 1),
                    (0, 2)],
                   ), array([1, 0]))

        >>> mi.sortlevel(1, ascending=False)
        (MultiIndex([(0, 2),
                    (0, 1)],
                   ), array([0, 1]))
        """
    def get_slice_bound(self, label: Hashable | Sequence[Hashable], side: Literal['left', 'right']) -> int:
        '''
        For an ordered MultiIndex, compute slice bound
        that corresponds to given label.

        Returns leftmost (one-past-the-rightmost if `side==\'right\') position
        of given label.

        Parameters
        ----------
        label : object or tuple of objects
        side : {\'left\', \'right\'}

        Returns
        -------
        int
            Index of label.

        Notes
        -----
        This method only works if level 0 index of the MultiIndex is lexsorted.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list(\'abbc\'), list(\'gefd\')])

        Get the locations from the leftmost \'b\' in the first level
        until the end of the multiindex:

        >>> mi.get_slice_bound(\'b\', side="left")
        1

        Like above, but if you get the locations from the rightmost
        \'b\' in the first level and \'f\' in the second level:

        >>> mi.get_slice_bound((\'b\',\'f\'), side="right")
        3

        See Also
        --------
        MultiIndex.get_loc : Get location for a label or a tuple of labels.
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.
        '''
    def slice_locs(self, start: Incomplete | None = None, end: Incomplete | None = None, step: Incomplete | None = None) -> tuple[int, int]:
        """
        For an ordered MultiIndex, compute the slice locations for input
        labels.

        The input labels can be tuples representing partial levels, e.g. for a
        MultiIndex with 3 levels, you can pass a single value (corresponding to
        the first level), or a 1-, 2-, or 3-tuple.

        Parameters
        ----------
        start : label or tuple, default None
            If None, defaults to the beginning
        end : label or tuple
            If None, defaults to the end
        step : int or None
            Slice step

        Returns
        -------
        (start, end) : (int, int)

        Notes
        -----
        This method only works if the MultiIndex is properly lexsorted. So,
        if only the first 2 levels of a 3-level MultiIndex are lexsorted,
        you can only pass two levels to ``.slice_locs``.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abbd'), list('deff')],
        ...                                names=['A', 'B'])

        Get the slice locations from the beginning of 'b' in the first level
        until the end of the multiindex:

        >>> mi.slice_locs(start='b')
        (1, 4)

        Like above, but stop at the end of 'b' in the first level and 'f' in
        the second level:

        >>> mi.slice_locs(start='b', end=('b', 'f'))
        (1, 3)

        See Also
        --------
        MultiIndex.get_loc : Get location for a label or a tuple of labels.
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.
        """
    def get_loc(self, key):
        """
        Get location for a label or a tuple of labels.

        The location is returned as an integer/slice or boolean
        mask.

        Parameters
        ----------
        key : label or tuple of labels (one for each level)

        Returns
        -------
        int, slice object or boolean mask
            If the key is past the lexsort depth, the return may be a
            boolean mask array, otherwise it is always a slice or int.

        See Also
        --------
        Index.get_loc : The get_loc method for (single-level) index.
        MultiIndex.slice_locs : Get slice location given start label(s) and
                                end label(s).
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.

        Notes
        -----
        The key cannot be a slice, list of same-level labels, a boolean mask,
        or a sequence of such. If you want to use those, use
        :meth:`MultiIndex.get_locs` instead.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')])

        >>> mi.get_loc('b')
        slice(1, 3, None)

        >>> mi.get_loc(('b', 'e'))
        1
        """
    def get_loc_level(self, key, level: IndexLabel = 0, drop_level: bool = True):
        """
        Get location and sliced index for requested label(s)/level(s).

        Parameters
        ----------
        key : label or sequence of labels
        level : int/level name or list thereof, optional
        drop_level : bool, default True
            If ``False``, the resulting index will not drop any level.

        Returns
        -------
        tuple
            A 2-tuple where the elements :

            Element 0: int, slice object or boolean array.

            Element 1: The resulting sliced multiindex/index. If the key
            contains all levels, this will be ``None``.

        See Also
        --------
        MultiIndex.get_loc  : Get location for a label or a tuple of labels.
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')],
        ...                                names=['A', 'B'])

        >>> mi.get_loc_level('b')
        (slice(1, 3, None), Index(['e', 'f'], dtype='object', name='B'))

        >>> mi.get_loc_level('e', level='B')
        (array([False,  True, False]), Index(['b'], dtype='object', name='A'))

        >>> mi.get_loc_level(['b', 'e'])
        (1, None)
        """
    def get_locs(self, seq):
        """
        Get location for a sequence of labels.

        Parameters
        ----------
        seq : label, slice, list, mask or a sequence of such
           You should use one of the above for each level.
           If a level should not be used, set it to ``slice(None)``.

        Returns
        -------
        numpy.ndarray
            NumPy array of integers suitable for passing to iloc.

        See Also
        --------
        MultiIndex.get_loc : Get location for a label or a tuple of labels.
        MultiIndex.slice_locs : Get slice location given start label(s) and
                                end label(s).

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')])

        >>> mi.get_locs('b')  # doctest: +SKIP
        array([1, 2], dtype=int64)

        >>> mi.get_locs([slice(None), ['e', 'f']])  # doctest: +SKIP
        array([1, 2], dtype=int64)

        >>> mi.get_locs([[True, False, True], slice('e', 'f')])  # doctest: +SKIP
        array([2], dtype=int64)
        """
    def truncate(self, before: Incomplete | None = None, after: Incomplete | None = None) -> MultiIndex:
        """
        Slice index between two labels / tuples, return new MultiIndex.

        Parameters
        ----------
        before : label or tuple, can be partial. Default None
            None defaults to start.
        after : label or tuple, can be partial. Default None
            None defaults to end.

        Returns
        -------
        MultiIndex
            The truncated MultiIndex.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([['a', 'b', 'c'], ['x', 'y', 'z']])
        >>> mi
        MultiIndex([('a', 'x'), ('b', 'y'), ('c', 'z')],
                   )
        >>> mi.truncate(before='a', after='b')
        MultiIndex([('a', 'x'), ('b', 'y')],
                   )
        """
    def equals(self, other: object) -> bool:
        """
        Determines if two MultiIndex objects have the same labeling information
        (the levels themselves do not necessarily have to be the same)

        See Also
        --------
        equal_levels
        """
    def equal_levels(self, other: MultiIndex) -> bool:
        """
        Return True if the levels of both MultiIndex objects are the same

        """
    def astype(self, dtype, copy: bool = True): ...
    def putmask(self, mask, value: MultiIndex) -> MultiIndex:
        """
        Return a new MultiIndex of the values set with the mask.

        Parameters
        ----------
        mask : array like
        value : MultiIndex
            Must either be the same length as self or length one

        Returns
        -------
        MultiIndex
        """
    def insert(self, loc: int, item) -> MultiIndex:
        """
        Make new MultiIndex inserting new item at location

        Parameters
        ----------
        loc : int
        item : tuple
            Must be same length as number of levels in the MultiIndex

        Returns
        -------
        new_index : Index
        """
    def delete(self, loc) -> MultiIndex:
        """
        Make new index with passed location deleted

        Returns
        -------
        new_index : MultiIndex
        """
    def isin(self, values, level: Incomplete | None = None) -> npt.NDArray[np.bool_]: ...
    rename: Incomplete
    __add__: Incomplete
    __radd__: Incomplete
    __iadd__: Incomplete
    __sub__: Incomplete
    __rsub__: Incomplete
    __isub__: Incomplete
    __pow__: Incomplete
    __rpow__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    __floordiv__: Incomplete
    __rfloordiv__: Incomplete
    __truediv__: Incomplete
    __rtruediv__: Incomplete
    __mod__: Incomplete
    __rmod__: Incomplete
    __divmod__: Incomplete
    __rdivmod__: Incomplete
    __neg__: Incomplete
    __pos__: Incomplete
    __abs__: Incomplete
    __invert__: Incomplete

def sparsify_labels(label_list, start: int = 0, sentinel: object = ''): ...
def maybe_droplevels(index: Index, key) -> Index:
    """
    Attempt to drop level or levels from the given index.

    Parameters
    ----------
    index: Index
    key : scalar or tuple

    Returns
    -------
    Index
    """
