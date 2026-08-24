import pandas as pd
import pyspark.pandas as ps
from pyspark.pandas.internal import InternalField as InternalField
from pyspark.sql.types import StructField as StructField
from typing import Any, Callable, List

class CategoricalAccessor:
    '''
    Accessor object for categorical properties of the Series values.

    Examples
    --------
    >>> s = ps.Series(list("abbccc"), dtype="category")
    >>> s  # doctest: +SKIP
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

    >>> s.cat.codes
    0    0
    1    1
    2    1
    3    2
    4    2
    5    2
    dtype: int8
    '''
    def __init__(self, series: ps.Series) -> None: ...
    @property
    def categories(self) -> pd.Index:
        '''
        The categories of this categorical.

        Examples
        --------
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
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
        '''
    @categories.setter
    def categories(self, categories: pd.Index | List) -> None: ...
    @property
    def ordered(self) -> bool:
        '''
        Whether the categories have an ordered relationship.

        Examples
        --------
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']

        >>> s.cat.ordered
        False
        '''
    @property
    def codes(self) -> ps.Series:
        '''
        Return Series of codes as well as the index.

        Examples
        --------
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']

        >>> s.cat.codes
        0    0
        1    1
        2    1
        3    2
        4    2
        5    2
        dtype: int8
        '''
    def add_categories(self, new_categories: pd.Index | Any | List) -> ps.Series | None:
        '''
        Add new categories.

        `new_categories` will be included at the last/highest place in the
        categories and will be unused directly after this call.

        Parameters
        ----------
        new_categories : category or list-like of category
           The new categories to be included.

        Returns
        -------
        Series or None
            Categorical with new categories added or None if ``inplace=True``.

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
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']

        >>> s.cat.add_categories(\'x\')  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (4, object): [\'a\', \'b\', \'c\', \'x\']
        '''
    def as_ordered(self, inplace: bool = False) -> ps.Series | None:
        '''
        Set the Categorical to be ordered.

        Parameters
        ----------
        inplace : bool, default False
           Whether or not to set the ordered attribute in-place or return
           a copy of this categorical with ordered set to True.

            .. deprecated:: 3.4.0

        Returns
        -------
        Series or None
            Ordered Categorical or None if ``inplace=True``.

        Examples
        --------
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']

        >>> s.cat.as_ordered()  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\' < \'b\' < \'c\']
        '''
    def as_unordered(self, inplace: bool = False) -> ps.Series | None:
        '''
        Set the Categorical to be unordered.

        Parameters
        ----------
        inplace : bool, default False
           Whether or not to set the ordered attribute in-place or return
           a copy of this categorical with ordered set to False.

            .. deprecated:: 3.4.0

        Returns
        -------
        Series or None
            Unordered Categorical or None if ``inplace=True``.

        Examples
        --------
        >>> s = ps.Series(list("abbccc"), dtype="category").cat.as_ordered()
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\' < \'b\' < \'c\']

        >>> s.cat.as_unordered()  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']
        '''
    def remove_categories(self, removals: pd.Index | Any | List) -> ps.Series | None:
        '''
        Remove the specified categories.

        `removals` must be included in the old categories. Values which were in
        the removed categories will be set to NaN

        Parameters
        ----------
        removals : category or list of categories
           The categories which should be removed.

        Returns
        -------
        Series or None
            Categorical with removed categories or None if ``inplace=True``.

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
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']

        >>> s.cat.remove_categories(\'b\')  # doctest: +SKIP
        0      a
        1    NaN
        2    NaN
        3      c
        4      c
        5      c
        dtype: category
        Categories (2, object): [\'a\', \'c\']
        '''
    def remove_unused_categories(self) -> ps.Series | None:
        '''
        Remove categories which are not used.

        Returns
        -------
        cat : Series or None
            Categorical with unused categories dropped or None if ``inplace=True``.

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        set_categories : Set the categories to the specified ones.

        Examples
        --------
        >>> s = ps.Series(pd.Categorical(list("abbccc"), categories=[\'a\', \'b\', \'c\', \'d\']))
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (4, object): [\'a\', \'b\', \'c\', \'d\']

        >>> s.cat.remove_unused_categories()  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']
        '''
    def rename_categories(self, new_categories: list | dict | Callable) -> ps.Series | None:
        '''
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
        cat : Series or None
            Categorical with removed categories or None if ``inplace=True``.

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
        >>> s = ps.Series(["a", "a", "b"], dtype="category")
        >>> s.cat.rename_categories([0, 1])  # doctest: +SKIP
        0    0
        1    0
        2    1
        dtype: category
        Categories (2, int64): [0, 1]

        For dict-like ``new_categories``, extra keys are ignored and
        categories not in the dictionary are passed through

        >>> s.cat.rename_categories({\'a\': \'A\', \'c\': \'C\'})  # doctest: +SKIP
        0    A
        1    A
        2    b
        dtype: category
        Categories (2, object): [\'A\', \'b\']

        You may also provide a callable to create the new categories

        >>> s.cat.rename_categories(lambda x: x.upper())  # doctest: +SKIP
        0    A
        1    A
        2    B
        dtype: category
        Categories (2, object): [\'A\', \'B\']
        '''
    def reorder_categories(self, new_categories: pd.Index | List, ordered: bool | None = None) -> ps.Series | None:
        '''
        Reorder categories as specified in new_categories.

        `new_categories` needs to include all old categories and no new category
        items.

        Parameters
        ----------
        new_categories : Index-like
           The categories in new order.
        ordered : bool, optional
           Whether or not the categorical is treated as an ordered categorical.
           If not given, do not change the ordered information.

        Returns
        -------
        cat : Series or None
            Categorical with removed categories or None if ``inplace=True``.

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

        Examples
        --------
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']

        >>> s.cat.reorder_categories([\'c\', \'b\', \'a\'], ordered=True)  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'c\' < \'b\' < \'a\']
        '''
    def set_categories(self, new_categories: pd.Index | List, ordered: bool | None = None, rename: bool = False) -> ps.Series | None:
        '''
        Set the categories to the specified new_categories.

        `new_categories` can include new categories (which will result in
        unused categories) or remove old categories (which results in values
        set to NaN). If `rename==True`, the categories will simply be renamed
        (less or more items than in old categories will result in values set to
        NaN or in unused categories respectively).

        This method can be used to perform more than one action of adding,
        removing, and reordering simultaneously and is therefore faster than
        performing the individual steps via the more specialised methods.

        On the other hand this methods does not do checks (e.g., whether the
        old categories are included in the new categories on a reorder), which
        can result in surprising changes, for example when using special string
        dtypes, which does not consider a S1 string equal to a single char
        python string.

        Parameters
        ----------
        new_categories : Index-like
           The categories in new order.
        ordered : bool, default False
           Whether or not the categorical is treated as an ordered categorical.
           If not given, do not change the ordered information.
        rename : bool, default False
           Whether or not the new_categories should be considered as a rename
           of the old categories or as reordered categories.

        Returns
        -------
        Series with reordered categories or None if inplace.

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

        Examples
        --------
        >>> s = ps.Series(list("abbccc"), dtype="category")
        >>> s  # doctest: +SKIP
        0    a
        1    b
        2    b
        3    c
        4    c
        5    c
        dtype: category
        Categories (3, object): [\'a\', \'b\', \'c\']

        >>> s.cat.set_categories([\'b\', \'c\'])  # doctest: +SKIP
        0    NaN
        1      b
        2      b
        3      c
        4      c
        5      c
        dtype: category
        Categories (2, object): [\'b\', \'c\']

        >>> s.cat.set_categories([1, 2, 3], rename=True)  # doctest: +SKIP
        0    1
        1    2
        2    2
        3    3
        4    3
        5    3
        dtype: category
        Categories (3, int64): [1, 2, 3]

        >>> s.cat.set_categories([1, 2, 3], rename=True, ordered=True)  # doctest: +SKIP
        0    1
        1    2
        2    2
        3    3
        4    3
        5    3
        dtype: category
        Categories (3, int64): [1 < 2 < 3]
        '''
