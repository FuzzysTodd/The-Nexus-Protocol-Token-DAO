import numpy as np
from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from pandas._config import get_option as get_option
from pandas._libs import NaT as NaT, lib as lib
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._typing import ArrayLike as ArrayLike, AstypeArg as AstypeArg, AxisInt as AxisInt, Dtype as Dtype, NpDtype as NpDtype, Ordered as Ordered, Shape as Shape, SortKind as SortKind, npt as npt, type_t as type_t
from pandas.core import algorithms as algorithms, arraylike as arraylike, ops as ops
from pandas.core.accessor import PandasDelegate as PandasDelegate, delegate_names as delegate_names
from pandas.core.algorithms import factorize as factorize, take_nd as take_nd
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray, ravel_compat as ravel_compat
from pandas.core.base import ExtensionArray as ExtensionArray, NoNewAttributesMixin as NoNewAttributesMixin, PandasObject as PandasObject
from pandas.core.construction import extract_array as extract_array, sanitize_array as sanitize_array
from pandas.core.dtypes.cast import coerce_indexer_dtype as coerce_indexer_dtype, find_common_type as find_common_type
from pandas.core.dtypes.common import ensure_int64 as ensure_int64, ensure_platform_int as ensure_platform_int, is_any_real_numeric_dtype as is_any_real_numeric_dtype, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_dict_like as is_dict_like, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_hashable as is_hashable, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_scalar as is_scalar, is_timedelta64_dtype as is_timedelta64_dtype, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.sorting import nargsort as nargsort
from pandas.core.strings.object_array import ObjectStringArrayMixin as ObjectStringArrayMixin
from pandas.io.formats import console as console
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Iterator, Literal, TypeVar, overload

CategoricalT = TypeVar('CategoricalT', bound='Categorical')

def contains(cat, key, container) -> bool:
    """
    Helper for membership check for ``key`` in ``cat``.

    This is a helper method for :method:`__contains__`
    and :class:`CategoricalIndex.__contains__`.

    Returns True if ``key`` is in ``cat.categories`` and the
    location of ``key`` in ``categories`` is in ``container``.

    Parameters
    ----------
    cat : :class:`Categorical`or :class:`categoricalIndex`
    key : a hashable object
        The key to check membership for.
    container : Container (e.g. list-like or mapping)
        The container to check for membership in.

    Returns
    -------
    is_in : bool
        True if ``key`` is in ``self.categories`` and location of
        ``key`` in ``categories`` is in ``container``, else False.

    Notes
    -----
    This method does not check for NaN values. Do that separately
    before calling this method.
    """

class Categorical(NDArrayBackedExtensionArray, PandasObject, ObjectStringArrayMixin):
    """
    Represent a categorical variable in classic R / S-plus fashion.

    `Categoricals` can only take on a limited, and usually fixed, number
    of possible values (`categories`). In contrast to statistical categorical
    variables, a `Categorical` might have an order, but numerical operations
    (additions, divisions, ...) are not possible.

    All values of the `Categorical` are either in `categories` or `np.nan`.
    Assigning values outside of `categories` will raise a `ValueError`. Order
    is defined by the order of the `categories`, not lexical order of the
    values.

    Parameters
    ----------
    values : list-like
        The values of the categorical. If categories are given, values not in
        categories will be replaced with NaN.
    categories : Index-like (unique), optional
        The unique categories for this categorical. If not given, the
        categories are assumed to be the unique values of `values` (sorted, if
        possible, otherwise in the order in which they appear).
    ordered : bool, default False
        Whether or not this categorical is treated as a ordered categorical.
        If True, the resulting categorical will be ordered.
        An ordered categorical respects, when sorted, the order of its
        `categories` attribute (which in turn is the `categories` argument, if
        provided).
    dtype : CategoricalDtype
        An instance of ``CategoricalDtype`` to use for this categorical.

    Attributes
    ----------
    categories : Index
        The categories of this categorical
    codes : ndarray
        The codes (integer positions, which point to the categories) of this
        categorical, read only.
    ordered : bool
        Whether or not this Categorical is ordered.
    dtype : CategoricalDtype
        The instance of ``CategoricalDtype`` storing the ``categories``
        and ``ordered``.

    Methods
    -------
    from_codes
    __array__

    Raises
    ------
    ValueError
        If the categories do not validate.
    TypeError
        If an explicit ``ordered=True`` is given but no `categories` and the
        `values` are not sortable.

    See Also
    --------
    CategoricalDtype : Type for categorical data.
    CategoricalIndex : An Index with an underlying ``Categorical``.

    Notes
    -----
    See the `user guide
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html>`__
    for more.

    Examples
    --------
    >>> pd.Categorical([1, 2, 3, 1, 2, 3])
    [1, 2, 3, 1, 2, 3]
    Categories (3, int64): [1, 2, 3]

    >>> pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
    ['a', 'b', 'c', 'a', 'b', 'c']
    Categories (3, object): ['a', 'b', 'c']

    Missing values are not included as a category.

    >>> c = pd.Categorical([1, 2, 3, 1, 2, 3, np.nan])
    >>> c
    [1, 2, 3, 1, 2, 3, NaN]
    Categories (3, int64): [1, 2, 3]

    However, their presence is indicated in the `codes` attribute
    by code `-1`.

    >>> c.codes
    array([ 0,  1,  2,  0,  1,  2, -1], dtype=int8)

    Ordered `Categoricals` can be sorted according to the custom order
    of the categories and can have a min and max value.

    >>> c = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'], ordered=True,
    ...                    categories=['c', 'b', 'a'])
    >>> c
    ['a', 'b', 'c', 'a', 'b', 'c']
    Categories (3, object): ['c' < 'b' < 'a']
    >>> c.min()
    'c'
    """
    __array_priority__: int
    def __init__(self, values, categories: Incomplete | None = None, ordered: Incomplete | None = None, dtype: Dtype | None = None, fastpath: bool = False, copy: bool = True) -> None: ...
    @property
    def dtype(self) -> CategoricalDtype:
        """
        The :class:`~pandas.api.types.CategoricalDtype` for this instance.
        """
    @overload
    def astype(self, dtype: npt.DTypeLike, copy: bool = ...) -> np.ndarray: ...
    @overload
    def astype(self, dtype: ExtensionDtype, copy: bool = ...) -> ExtensionArray: ...
    @overload
    def astype(self, dtype: AstypeArg, copy: bool = ...) -> ArrayLike: ...
    def to_list(self):
        """
        Alias for tolist.
        """
    @classmethod
    def from_codes(cls, codes, categories: Incomplete | None = None, ordered: Incomplete | None = None, dtype: Dtype | None = None) -> Categorical:
        '''
        Make a Categorical type from codes and categories or dtype.

        This constructor is useful if you already have codes and
        categories/dtype and so do not need the (computation intensive)
        factorization step, which is usually done on the constructor.

        If your data does not follow this convention, please use the normal
        constructor.

        Parameters
        ----------
        codes : array-like of int
            An integer array, where each integer points to a category in
            categories or dtype.categories, or else is -1 for NaN.
        categories : index-like, optional
            The categories for the categorical. Items need to be unique.
            If the categories are not given here, then they must be provided
            in `dtype`.
        ordered : bool, optional
            Whether or not this categorical is treated as an ordered
            categorical. If not given here or in `dtype`, the resulting
            categorical will be unordered.
        dtype : CategoricalDtype or "category", optional
            If :class:`CategoricalDtype`, cannot be used together with
            `categories` or `ordered`.

        Returns
        -------
        Categorical

        Examples
        --------
        >>> dtype = pd.CategoricalDtype([\'a\', \'b\'], ordered=True)
        >>> pd.Categorical.from_codes(codes=[0, 1, 0, 1], dtype=dtype)
        [\'a\', \'b\', \'a\', \'b\']
        Categories (2, object): [\'a\' < \'b\']
        '''
    @property
    def categories(self) -> Index:
        """
        The categories of this categorical.

        Setting assigns new values to each category (effectively a rename of
        each individual category).

        The assigned value has to be a list-like object. All items must be
        unique and the number of items in the new categories must be the same
        as the number of items in the old categories.

        Raises
        ------
        ValueError
            If the new categories do not validate as categories or if the
            number of new categories is unequal the number of old categories

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.
        """
    @property
    def ordered(self) -> Ordered:
        """
        Whether the categories have an ordered relationship.
        """
    @property
    def codes(self) -> np.ndarray:
        """
        The category codes of this categorical.

        Codes are an array of integers which are the positions of the actual
        values in the categories array.

        There is no setter, use the other categorical methods and the normal item
        setter to change values in the categorical.

        Returns
        -------
        ndarray[int]
            A non-writable view of the `codes` array.
        """
    def set_ordered(self, value: bool) -> Categorical:
        """
        Set the ordered attribute to the boolean value.

        Parameters
        ----------
        value : bool
           Set whether this categorical is ordered (True) or not (False).
        """
    def as_ordered(self) -> Categorical:
        """
        Set the Categorical to be ordered.

        Returns
        -------
        Categorical
            Ordered Categorical.
        """
    def as_unordered(self) -> Categorical:
        """
        Set the Categorical to be unordered.

        Returns
        -------
        Categorical
            Unordered Categorical.
        """
    def set_categories(self, new_categories, ordered: Incomplete | None = None, rename: bool = False):
        """
        Set the categories to the specified new_categories.

        `new_categories` can include new categories (which will result in
        unused categories) or remove old categories (which results in values
        set to NaN). If `rename==True`, the categories will simple be renamed
        (less or more items than in old categories will result in values set to
        NaN or in unused categories respectively).

        This method can be used to perform more than one action of adding,
        removing, and reordering simultaneously and is therefore faster than
        performing the individual steps via the more specialised methods.

        On the other hand this methods does not do checks (e.g., whether the
        old categories are included in the new categories on a reorder), which
        can result in surprising changes, for example when using special string
        dtypes, which does not considers a S1 string equal to a single char
        python string.

        Parameters
        ----------
        new_categories : Index-like
           The categories in new order.
        ordered : bool, default False
           Whether or not the categorical is treated as a ordered categorical.
           If not given, do not change the ordered information.
        rename : bool, default False
           Whether or not the new_categories should be considered as a rename
           of the old categories or as reordered categories.

        Returns
        -------
        Categorical with reordered categories.

        Raises
        ------
        ValueError
            If new_categories does not validate as categories

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        remove_unused_categories : Remove categories which are not used.
        """
    def rename_categories(self, new_categories) -> Categorical:
        """
        Rename categories.

        Parameters
        ----------
        new_categories : list-like, dict-like or callable

            New categories which will replace old categories.

            * list-like: all items must be unique and the number of items in
              the new categories must match the existing number of categories.

            * dict-like: specifies a mapping from
              old categories to new. Categories not contained in the mapping
              are passed through and extra categories in the mapping are
              ignored.

            * callable : a callable that is called on all items in the old
              categories and whose return values comprise the new categories.

        Returns
        -------
        Categorical
            Categorical with renamed categories.

        Raises
        ------
        ValueError
            If new categories are list-like and do not have the same number of
            items than the current categories or do not validate as categories

        See Also
        --------
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.

        Examples
        --------
        >>> c = pd.Categorical(['a', 'a', 'b'])
        >>> c.rename_categories([0, 1])
        [0, 0, 1]
        Categories (2, int64): [0, 1]

        For dict-like ``new_categories``, extra keys are ignored and
        categories not in the dictionary are passed through

        >>> c.rename_categories({'a': 'A', 'c': 'C'})
        ['A', 'A', 'b']
        Categories (2, object): ['A', 'b']

        You may also provide a callable to create the new categories

        >>> c.rename_categories(lambda x: x.upper())
        ['A', 'A', 'B']
        Categories (2, object): ['A', 'B']
        """
    def reorder_categories(self, new_categories, ordered: Incomplete | None = None):
        """
        Reorder categories as specified in new_categories.

        `new_categories` need to include all old categories and no new category
        items.

        Parameters
        ----------
        new_categories : Index-like
           The categories in new order.
        ordered : bool, optional
           Whether or not the categorical is treated as a ordered categorical.
           If not given, do not change the ordered information.

        Returns
        -------
        Categorical
            Categorical with reordered categories.

        Raises
        ------
        ValueError
            If the new categories do not contain all old category items or any
            new ones

        See Also
        --------
        rename_categories : Rename categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.
        """
    def add_categories(self, new_categories) -> Categorical:
        """
        Add new categories.

        `new_categories` will be included at the last/highest place in the
        categories and will be unused directly after this call.

        Parameters
        ----------
        new_categories : category or list-like of category
           The new categories to be included.

        Returns
        -------
        Categorical
            Categorical with new categories added.

        Raises
        ------
        ValueError
            If the new categories include old categories or do not validate as
            categories

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        remove_categories : Remove the specified categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.

        Examples
        --------
        >>> c = pd.Categorical(['c', 'b', 'c'])
        >>> c
        ['c', 'b', 'c']
        Categories (2, object): ['b', 'c']

        >>> c.add_categories(['d', 'a'])
        ['c', 'b', 'c']
        Categories (4, object): ['b', 'c', 'd', 'a']
        """
    def remove_categories(self, removals):
        """
        Remove the specified categories.

        `removals` must be included in the old categories. Values which were in
        the removed categories will be set to NaN

        Parameters
        ----------
        removals : category or list of categories
           The categories which should be removed.

        Returns
        -------
        Categorical
            Categorical with removed categories.

        Raises
        ------
        ValueError
            If the removals are not contained in the categories

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.

        Examples
        --------
        >>> c = pd.Categorical(['a', 'c', 'b', 'c', 'd'])
        >>> c
        ['a', 'c', 'b', 'c', 'd']
        Categories (4, object): ['a', 'b', 'c', 'd']

        >>> c.remove_categories(['d', 'a'])
        [NaN, 'c', 'b', 'c', NaN]
        Categories (2, object): ['b', 'c']
        """
    def remove_unused_categories(self) -> Categorical:
        """
        Remove categories which are not used.

        Returns
        -------
        Categorical
            Categorical with unused categories dropped.

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        set_categories : Set the categories to the specified ones.

        Examples
        --------
        >>> c = pd.Categorical(['a', 'c', 'b', 'c', 'd'])
        >>> c
        ['a', 'c', 'b', 'c', 'd']
        Categories (4, object): ['a', 'b', 'c', 'd']

        >>> c[2] = 'a'
        >>> c[4] = 'c'
        >>> c
        ['a', 'c', 'a', 'c', 'c']
        Categories (4, object): ['a', 'b', 'c', 'd']

        >>> c.remove_unused_categories()
        ['a', 'c', 'a', 'c', 'c']
        Categories (2, object): ['a', 'c']
        """
    def map(self, mapper):
        """
        Map categories using an input mapping or function.

        Maps the categories to new categories. If the mapping correspondence is
        one-to-one the result is a :class:`~pandas.Categorical` which has the
        same order property as the original, otherwise a :class:`~pandas.Index`
        is returned. NaN values are unaffected.

        If a `dict` or :class:`~pandas.Series` is used any unmapped category is
        mapped to `NaN`. Note that if this happens an :class:`~pandas.Index`
        will be returned.

        Parameters
        ----------
        mapper : function, dict, or Series
            Mapping correspondence.

        Returns
        -------
        pandas.Categorical or pandas.Index
            Mapped categorical.

        See Also
        --------
        CategoricalIndex.map : Apply a mapping correspondence on a
            :class:`~pandas.CategoricalIndex`.
        Index.map : Apply a mapping correspondence on an
            :class:`~pandas.Index`.
        Series.map : Apply a mapping correspondence on a
            :class:`~pandas.Series`.
        Series.apply : Apply more complex functions on a
            :class:`~pandas.Series`.

        Examples
        --------
        >>> cat = pd.Categorical(['a', 'b', 'c'])
        >>> cat
        ['a', 'b', 'c']
        Categories (3, object): ['a', 'b', 'c']
        >>> cat.map(lambda x: x.upper())
        ['A', 'B', 'C']
        Categories (3, object): ['A', 'B', 'C']
        >>> cat.map({'a': 'first', 'b': 'second', 'c': 'third'})
        ['first', 'second', 'third']
        Categories (3, object): ['first', 'second', 'third']

        If the mapping is one-to-one the ordering of the categories is
        preserved:

        >>> cat = pd.Categorical(['a', 'b', 'c'], ordered=True)
        >>> cat
        ['a', 'b', 'c']
        Categories (3, object): ['a' < 'b' < 'c']
        >>> cat.map({'a': 3, 'b': 2, 'c': 1})
        [3, 2, 1]
        Categories (3, int64): [3 < 2 < 1]

        If the mapping is not one-to-one an :class:`~pandas.Index` is returned:

        >>> cat.map({'a': 'first', 'b': 'second', 'c': 'first'})
        Index(['first', 'second', 'first'], dtype='object')

        If a `dict` is used, all unmapped categories are mapped to `NaN` and
        the result is an :class:`~pandas.Index`:

        >>> cat.map({'a': 'first', 'b': 'second'})
        Index(['first', 'second', nan], dtype='object')
        """
    __eq__: Incomplete
    __ne__: Incomplete
    __lt__: Incomplete
    __gt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    def __array__(self, dtype: NpDtype | None = None) -> np.ndarray:
        """
        The numpy array interface.

        Returns
        -------
        numpy.array
            A numpy array of either the specified dtype or,
            if dtype==None (default), the same dtype as
            categorical.categories.dtype.
        """
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs): ...
    @property
    def nbytes(self) -> int: ...
    def memory_usage(self, deep: bool = False) -> int:
        """
        Memory usage of my values

        Parameters
        ----------
        deep : bool
            Introspect the data deeply, interrogate
            `object` dtypes for system-level memory consumption

        Returns
        -------
        bytes used

        Notes
        -----
        Memory usage does not include memory consumed by elements that
        are not components of the array if deep=False

        See Also
        --------
        numpy.ndarray.nbytes
        """
    def isna(self) -> np.ndarray:
        """
        Detect missing values

        Missing values (-1 in .codes) are detected.

        Returns
        -------
        np.ndarray[bool] of whether my values are null

        See Also
        --------
        isna : Top-level isna.
        isnull : Alias of isna.
        Categorical.notna : Boolean inverse of Categorical.isna.

        """
    isnull = isna
    def notna(self) -> np.ndarray:
        """
        Inverse of isna

        Both missing values (-1 in .codes) and NA as a category are detected as
        null.

        Returns
        -------
        np.ndarray[bool] of whether my values are not null

        See Also
        --------
        notna : Top-level notna.
        notnull : Alias of notna.
        Categorical.isna : Boolean inverse of Categorical.notna.

        """
    notnull = notna
    def value_counts(self, dropna: bool = True) -> Series:
        """
        Return a Series containing counts of each category.

        Every category will have an entry, even those with a count of 0.

        Parameters
        ----------
        dropna : bool, default True
            Don't include counts of NaN.

        Returns
        -------
        counts : Series

        See Also
        --------
        Series.value_counts
        """
    def check_for_ordered(self, op) -> None:
        """assert that we are ordered"""
    def argsort(self, *, ascending: bool = True, kind: SortKind = 'quicksort', **kwargs):
        """
        Return the indices that would sort the Categorical.

        Missing values are sorted at the end.

        Parameters
        ----------
        ascending : bool, default True
            Whether the indices should result in an ascending
            or descending sort.
        kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
            Sorting algorithm.
        **kwargs:
            passed through to :func:`numpy.argsort`.

        Returns
        -------
        np.ndarray[np.intp]

        See Also
        --------
        numpy.ndarray.argsort

        Notes
        -----
        While an ordering is applied to the category values, arg-sorting
        in this context refers more to organizing and grouping together
        based on matching category values. Thus, this function can be
        called on an unordered Categorical instance unlike the functions
        'Categorical.min' and 'Categorical.max'.

        Examples
        --------
        >>> pd.Categorical(['b', 'b', 'a', 'c']).argsort()
        array([2, 0, 1, 3])

        >>> cat = pd.Categorical(['b', 'b', 'a', 'c'],
        ...                      categories=['c', 'b', 'a'],
        ...                      ordered=True)
        >>> cat.argsort()
        array([3, 0, 1, 2])

        Missing values are placed at the end

        >>> cat = pd.Categorical([2, None, 1])
        >>> cat.argsort()
        array([2, 0, 1])
        """
    @overload
    def sort_values(self, *, inplace: Literal[False] = ..., ascending: bool = ..., na_position: str = ...) -> Categorical: ...
    @overload
    def sort_values(self, *, inplace: Literal[True], ascending: bool = ..., na_position: str = ...) -> None: ...
    def __iter__(self) -> Iterator:
        """
        Returns an Iterator over the values of this Categorical.
        """
    def __contains__(self, key) -> bool:
        """
        Returns True if `key` is in this Categorical.
        """
    def min(self, *, skipna: bool = True, **kwargs):
        """
        The minimum value of the object.

        Only ordered `Categoricals` have a minimum!

        Raises
        ------
        TypeError
            If the `Categorical` is not `ordered`.

        Returns
        -------
        min : the minimum of this `Categorical`, NA value if empty
        """
    def max(self, *, skipna: bool = True, **kwargs):
        """
        The maximum value of the object.

        Only ordered `Categoricals` have a maximum!

        Raises
        ------
        TypeError
            If the `Categorical` is not `ordered`.

        Returns
        -------
        max : the maximum of this `Categorical`, NA if array is empty
        """
    def unique(self):
        '''
        Return the ``Categorical`` which ``categories`` and ``codes`` are
        unique.

        .. versionchanged:: 1.3.0

            Previously, unused categories were dropped from the new categories.

        Returns
        -------
        Categorical

        See Also
        --------
        pandas.unique
        CategoricalIndex.unique
        Series.unique : Return unique values of Series object.

        Examples
        --------
        >>> pd.Categorical(list("baabc")).unique()
        [\'b\', \'a\', \'c\']
        Categories (3, object): [\'a\', \'b\', \'c\']
        >>> pd.Categorical(list("baab"), categories=list("abc"), ordered=True).unique()
        [\'b\', \'a\']
        Categories (3, object): [\'a\' < \'b\' < \'c\']
        '''
    def equals(self, other: object) -> bool:
        """
        Returns True if categorical arrays are equal.

        Parameters
        ----------
        other : `Categorical`

        Returns
        -------
        bool
        """
    def describe(self) -> DataFrame:
        """
        Describes this Categorical

        Returns
        -------
        description: `DataFrame`
            A dataframe with frequency and counts by category.
        """
    def isin(self, values) -> npt.NDArray[np.bool_]:
        """
        Check whether `values` are contained in Categorical.

        Return a boolean NumPy Array showing whether each element in
        the Categorical matches an element in the passed sequence of
        `values` exactly.

        Parameters
        ----------
        values : set or list-like
            The sequence of values to test. Passing in a single string will
            raise a ``TypeError``. Instead, turn a single string into a
            list of one element.

        Returns
        -------
        np.ndarray[bool]

        Raises
        ------
        TypeError
          * If `values` is not a set or list-like

        See Also
        --------
        pandas.Series.isin : Equivalent method on Series.

        Examples
        --------
        >>> s = pd.Categorical(['lama', 'cow', 'lama', 'beetle', 'lama',
        ...                'hippo'])
        >>> s.isin(['cow', 'lama'])
        array([ True,  True,  True, False,  True, False])

        Passing a single string as ``s.isin('lama')`` will raise an error. Use
        a list of one element instead:

        >>> s.isin(['lama'])
        array([ True, False,  True, False,  True, False])
        """

class CategoricalAccessor(PandasDelegate, PandasObject, NoNewAttributesMixin):
    '''
    Accessor object for categorical properties of the Series values.

    Parameters
    ----------
    data : Series or CategoricalIndex

    Examples
    --------
    >>> s = pd.Series(list("abbccc")).astype("category")
    >>> s
    0    a
    1    b
    2    b
    3    c
    4    c
    5    c
    dtype: category
    Categories (3, object): [\'a\', \'b\', \'c\']

    >>> s.cat.categories
    Index([\'a\', \'b\', \'c\'], dtype=\'object\')

    >>> s.cat.rename_categories(list("cba"))
    0    c
    1    b
    2    b
    3    a
    4    a
    5    a
    dtype: category
    Categories (3, object): [\'c\', \'b\', \'a\']

    >>> s.cat.reorder_categories(list("cba"))
    0    a
    1    b
    2    b
    3    c
    4    c
    5    c
    dtype: category
    Categories (3, object): [\'c\', \'b\', \'a\']

    >>> s.cat.add_categories(["d", "e"])
    0    a
    1    b
    2    b
    3    c
    4    c
    5    c
    dtype: category
    Categories (5, object): [\'a\', \'b\', \'c\', \'d\', \'e\']

    >>> s.cat.remove_categories(["a", "c"])
    0    NaN
    1      b
    2      b
    3    NaN
    4    NaN
    5    NaN
    dtype: category
    Categories (1, object): [\'b\']

    >>> s1 = s.cat.add_categories(["d", "e"])
    >>> s1.cat.remove_unused_categories()
    0    a
    1    b
    2    b
    3    c
    4    c
    5    c
    dtype: category
    Categories (3, object): [\'a\', \'b\', \'c\']

    >>> s.cat.set_categories(list("abcde"))
    0    a
    1    b
    2    b
    3    c
    4    c
    5    c
    dtype: category
    Categories (5, object): [\'a\', \'b\', \'c\', \'d\', \'e\']

    >>> s.cat.as_ordered()
    0    a
    1    b
    2    b
    3    c
    4    c
    5    c
    dtype: category
    Categories (3, object): [\'a\' < \'b\' < \'c\']

    >>> s.cat.as_unordered()
    0    a
    1    b
    2    b
    3    c
    4    c
    5    c
    dtype: category
    Categories (3, object): [\'a\', \'b\', \'c\']
    '''
    def __init__(self, data) -> None: ...
    @property
    def codes(self) -> Series:
        """
        Return Series of codes as well as the index.
        """

def recode_for_categories(codes: np.ndarray, old_categories, new_categories, copy: bool = True) -> np.ndarray:
    """
    Convert a set of codes for to a new set of categories

    Parameters
    ----------
    codes : np.ndarray
    old_categories, new_categories : Index
    copy: bool, default True
        Whether to copy if the codes are unchanged.

    Returns
    -------
    new_codes : np.ndarray[np.int64]

    Examples
    --------
    >>> old_cat = pd.Index(['b', 'a', 'c'])
    >>> new_cat = pd.Index(['a', 'b'])
    >>> codes = np.array([0, 1, 1, 2])
    >>> recode_for_categories(codes, old_cat, new_cat)
    array([ 1,  0,  0, -1], dtype=int8)
    """
def factorize_from_iterable(values) -> tuple[np.ndarray, Index]:
    """
    Factorize an input `values` into `categories` and `codes`. Preserves
    categorical dtype in `categories`.

    Parameters
    ----------
    values : list-like

    Returns
    -------
    codes : ndarray
    categories : Index
        If `values` has a categorical dtype, then `categories` is
        a CategoricalIndex keeping the categories and order of `values`.
    """
def factorize_from_iterables(iterables) -> tuple[list[np.ndarray], list[Index]]:
    """
    A higher-level wrapper over `factorize_from_iterable`.

    Parameters
    ----------
    iterables : list-like of list-likes

    Returns
    -------
    codes : list of ndarrays
    categories : list of Indexes

    Notes
    -----
    See `factorize_from_iterable` for more info.
    """
