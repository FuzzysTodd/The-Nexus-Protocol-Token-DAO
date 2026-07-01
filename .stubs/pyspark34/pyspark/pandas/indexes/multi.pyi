import pandas as pd
from _typeshed import Incomplete
from pyspark.pandas._typing import Label as Label, Name as Name, Scalar as Scalar
from pyspark.pandas.exceptions import PandasNotImplementedError as PandasNotImplementedError
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.indexes.base import Index as Index
from pyspark.pandas.internal import InternalField as InternalField, InternalFrame as InternalFrame, NATURAL_ORDER_COLUMN_NAME as NATURAL_ORDER_COLUMN_NAME, SPARK_INDEX_NAME_FORMAT as SPARK_INDEX_NAME_FORMAT
from pyspark.pandas.missing.indexes import MissingPandasLikeMultiIndex as MissingPandasLikeMultiIndex
from pyspark.pandas.series import Series as Series, first_series as first_series
from pyspark.pandas.utils import compare_disallow_null as compare_disallow_null, is_name_like_tuple as is_name_like_tuple, name_like_string as name_like_string, scol_for as scol_for, validate_index_loc as validate_index_loc, verify_temp_column_name as verify_temp_column_name
from pyspark.sql import Column as Column, Window as Window
from pyspark.sql.types import DataType as DataType
from typing import Any, Callable, Iterator, List, Tuple

class MultiIndex(Index):
    """
    pandas-on-Spark MultiIndex that corresponds to pandas MultiIndex logically. This might hold
    Spark Column internally.

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

    See Also
    --------
    MultiIndex.from_arrays  : Convert list of arrays to MultiIndex.
    MultiIndex.from_product : Create a MultiIndex from the cartesian product
                              of iterables.
    MultiIndex.from_tuples  : Convert list of tuples to a MultiIndex.
    MultiIndex.from_frame   : Make a MultiIndex from a DataFrame.
    Index : A single-level Index.

    Examples
    --------
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index  # doctest: +SKIP
    MultiIndex([(1, 4),
                (2, 5),
                (3, 6)],
               )

    >>> ps.DataFrame({'a': [1, 2, 3]}, index=[list('abc'), list('def')]).index  # doctest: +SKIP
    MultiIndex([('a', 'd'),
                ('b', 'e'),
                ('c', 'f')],
               )
    """
    def __new__(cls, levels: Incomplete | None = None, codes: Incomplete | None = None, sortorder: Incomplete | None = None, names: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False, name: Incomplete | None = None, verify_integrity: bool = True): ...
    def __abs__(self) -> MultiIndex: ...
    def any(self, *args, **kwargs) -> None: ...
    def all(self, *args, **kwargs) -> None: ...
    @staticmethod
    def from_tuples(tuples: List[Tuple], sortorder: int | None = None, names: List[Name] | None = None) -> MultiIndex:
        """
        Convert list of tuples to MultiIndex.

        Parameters
        ----------
        tuples : list / sequence of tuple-likes
            Each tuple is the index of one row/column.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that level).
        names : list / sequence of str, optional
            Names for the levels in the index.

        Returns
        -------
        index : MultiIndex

        Examples
        --------

        >>> tuples = [(1, 'red'), (1, 'blue'),
        ...           (2, 'red'), (2, 'blue')]
        >>> ps.MultiIndex.from_tuples(tuples, names=('number', 'color'))  # doctest: +SKIP
        MultiIndex([(1,  'red'),
                    (1, 'blue'),
                    (2,  'red'),
                    (2, 'blue')],
                   names=['number', 'color'])
        """
    @staticmethod
    def from_arrays(arrays: List[List], sortorder: int | None = None, names: List[Name] | None = None) -> MultiIndex:
        """
        Convert arrays to MultiIndex.

        Parameters
        ----------
        arrays: list / sequence of array-likes
            Each array-like gives one level’s value for each data point. len(arrays)
            is the number of levels.
        sortorder: int or None
            Level of sortedness (must be lexicographically sorted by that level).
        names: list / sequence of str, optional
            Names for the levels in the index.

        Returns
        -------
        index: MultiIndex

        Examples
        --------

        >>> arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
        >>> ps.MultiIndex.from_arrays(arrays, names=('number', 'color'))  # doctest: +SKIP
        MultiIndex([(1,  'red'),
                    (1, 'blue'),
                    (2,  'red'),
                    (2, 'blue')],
                   names=['number', 'color'])
        """
    @staticmethod
    def from_product(iterables: List[List], sortorder: int | None = None, names: List[Name] | None = None) -> MultiIndex:
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

        Returns
        -------
        index : MultiIndex

        See Also
        --------
        MultiIndex.from_arrays : Convert list of arrays to MultiIndex.
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex.

        Examples
        --------
        >>> numbers = [0, 1, 2]
        >>> colors = ['green', 'purple']
        >>> ps.MultiIndex.from_product([numbers, colors],
        ...                            names=['number', 'color'])  # doctest: +SKIP
        MultiIndex([(0,  'green'),
                    (0, 'purple'),
                    (1,  'green'),
                    (1, 'purple'),
                    (2,  'green'),
                    (2, 'purple')],
                   names=['number', 'color'])
        """
    @staticmethod
    def from_frame(df: DataFrame, names: List[Name] | None = None) -> MultiIndex:
        """
        Make a MultiIndex from a DataFrame.

        Parameters
        ----------
        df : DataFrame
            DataFrame to be converted to MultiIndex.
        names : list-like, optional
            If no names are provided, use the column names, or tuple of column
            names if the column is a MultiIndex. If a sequence, overwrite
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
        >>> df = ps.DataFrame([['HI', 'Temp'], ['HI', 'Precip'],
        ...                    ['NJ', 'Temp'], ['NJ', 'Precip']],
        ...                   columns=['a', 'b'])
        >>> df  # doctest: +SKIP
              a       b
        0    HI    Temp
        1    HI  Precip
        2    NJ    Temp
        3    NJ  Precip

        >>> ps.MultiIndex.from_frame(df)  # doctest: +SKIP
        MultiIndex([('HI',   'Temp'),
                    ('HI', 'Precip'),
                    ('NJ',   'Temp'),
                    ('NJ', 'Precip')],
                   names=['a', 'b'])

        Using explicit names, instead of the column names

        >>> ps.MultiIndex.from_frame(df, names=['state', 'observation'])  # doctest: +SKIP
        MultiIndex([('HI',   'Temp'),
                    ('HI', 'Precip'),
                    ('NJ',   'Temp'),
                    ('NJ', 'Precip')],
                   names=['state', 'observation'])
        """
    @property
    def name(self) -> Name: ...
    @name.setter
    def name(self, name: Name) -> None: ...
    @property
    def dtypes(self) -> pd.Series:
        '''Return the dtypes as a Series for the underlying MultiIndex.

        .. versionadded:: 3.3.0

        Returns
        -------
        pd.Series
            The data type of each level.

        Examples
        --------
        >>> psmidx = ps.MultiIndex.from_arrays(
        ...     [[0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
        ...     names=("zero", "one"),
        ... )
        >>> psmidx.dtypes
        zero    int64
        one     int64
        dtype: object
        '''
    def swaplevel(self, i: int = -2, j: int = -1) -> MultiIndex:
        """
        Swap level i with level j.
        Calling this method does not change the ordering of the values.

        Parameters
        ----------
        i : int, str, default -2
            First level of index to be swapped. Can pass level name as string.
            Parameter types can be mixed.
        j : int, str, default -1
            Second level of index to be swapped. Can pass level name as string.
            Parameter types can be mixed.

        Returns
        -------
        MultiIndex
            A new MultiIndex.

        Examples
        --------
        >>> midx = ps.MultiIndex.from_arrays([['a', 'b'], [1, 2]], names = ['word', 'number'])
        >>> midx  # doctest: +SKIP
        MultiIndex([('a', 1),
                    ('b', 2)],
                   names=['word', 'number'])

        >>> midx.swaplevel(0, 1)  # doctest: +SKIP
        MultiIndex([(1, 'a'),
                    (2, 'b')],
                   names=['number', 'word'])

        >>> midx.swaplevel('number', 'word')  # doctest: +SKIP
        MultiIndex([(1, 'a'),
                    (2, 'b')],
                   names=['number', 'word'])
        """
    @property
    def levshape(self) -> Tuple[int, ...]:
        """
        A tuple with the length of each level.

        Examples
        --------
        >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> midx  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y'),
                    ('c', 'z')],
                   )

        >>> midx.levshape
        (3, 3)
        """
    def to_frame(self, index: bool = True, name: List[Name] | None = None) -> DataFrame:
        """
        Create a DataFrame with the levels of the MultiIndex as columns.
        Column ordering is determined by the DataFrame constructor with data as
        a dict.

        Parameters
        ----------
        index : boolean, default True
            Set the index of the returned DataFrame as the original MultiIndex.
        name : list / sequence of strings, optional
            The passed names should substitute index level names.

        Returns
        -------
        DataFrame : a DataFrame containing the original MultiIndex data.

        See Also
        --------
        DataFrame

        Examples
        --------
        >>> tuples = [(1, 'red'), (1, 'blue'),
        ...           (2, 'red'), (2, 'blue')]
        >>> idx = ps.MultiIndex.from_tuples(tuples, names=('number', 'color'))
        >>> idx  # doctest: +SKIP
        MultiIndex([(1,  'red'),
                    (1, 'blue'),
                    (2,  'red'),
                    (2, 'blue')],
                   names=['number', 'color'])
        >>> idx.to_frame()  # doctest: +NORMALIZE_WHITESPACE
                      number color
        number color
        1      red         1   red
               blue        1  blue
        2      red         2   red
               blue        2  blue

        By default, the original Index is reused. To enforce a new Index:

        >>> idx.to_frame(index=False)
           number color
        0       1   red
        1       1  blue
        2       2   red
        3       2  blue

        To override the name of the resulting column, specify `name`:

        >>> idx.to_frame(name=['n', 'c'])  # doctest: +NORMALIZE_WHITESPACE
                      n     c
        number color
        1      red    1   red
               blue   1  blue
        2      red    2   red
               blue   2  blue
        """
    def to_pandas(self) -> pd.MultiIndex:
        """
        Return a pandas MultiIndex.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver's memory.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'],
        ...                   index=[list('abcd'), list('efgh')])
        >>> df['dogs'].index.to_pandas()  # doctest: +SKIP
        MultiIndex([('a', 'e'),
                    ('b', 'f'),
                    ('c', 'g'),
                    ('d', 'h')],
                   )
        """
    def nunique(self, dropna: bool = True, approx: bool = False, rsd: float = 0.05) -> int: ...
    def copy(self, deep: bool | None = None) -> MultiIndex:
        """
        Make a copy of this object.

        Parameters
        ----------
        deep : None
            this parameter is not supported but just dummy parameter to match pandas.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'],
        ...                   index=[list('abcd'), list('efgh')])
        >>> df['dogs'].index  # doctest: +SKIP
        MultiIndex([('a', 'e'),
                    ('b', 'f'),
                    ('c', 'g'),
                    ('d', 'h')],
                   )

        Copy index

        >>> df.index.copy()  # doctest: +SKIP
        MultiIndex([('a', 'e'),
                    ('b', 'f'),
                    ('c', 'g'),
                    ('d', 'h')],
                   )
        """
    def symmetric_difference(self, other: Index, result_name: List[Name] | None = None, sort: bool | None = None) -> MultiIndex:
        """
        Compute the symmetric difference of two MultiIndex objects.

        Parameters
        ----------
        other : Index or array-like
        result_name : list
        sort : True or None, default None
            Whether to sort the resulting index.
            * True : Attempt to sort the result.
            * None : Do not sort the result.

        Returns
        -------
        symmetric_difference : MultiIndex

        Notes
        -----
        ``symmetric_difference`` contains elements that appear in either
        ``idx1`` or ``idx2`` but not both. Equivalent to the Index created by
        ``idx1.difference(idx2) | idx2.difference(idx1)`` with duplicates
        dropped.

        Examples
        --------
        >>> midx1 = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                        ['speed', 'weight', 'length']],
        ...                       [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                        [0, 0, 0, 0, 1, 2, 0, 1, 2]])
        >>> midx2 = pd.MultiIndex([['pandas-on-Spark', 'cow', 'falcon'],
        ...                        ['speed', 'weight', 'length']],
        ...                       [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                        [0, 0, 0, 0, 1, 2, 0, 1, 2]])
        >>> s1 = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
        ...                index=midx1)
        >>> s2 = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
        ...              index=midx2)

        >>> s1.index.symmetric_difference(s2.index)  # doctest: +SKIP
        MultiIndex([('pandas-on-Spark', 'speed'),
                    (  'lama', 'speed')],
                   )

        You can set names of the result Index.

        >>> s1.index.symmetric_difference(s2.index, result_name=['a', 'b'])  # doctest: +SKIP
        MultiIndex([('pandas-on-Spark', 'speed'),
                    (  'lama', 'speed')],
                   names=['a', 'b'])

        You can set sort to `True`, if you want to sort the resulting index.

        >>> s1.index.symmetric_difference(s2.index, sort=True)  # doctest: +SKIP
        MultiIndex([('pandas-on-Spark', 'speed'),
                    (  'lama', 'speed')],
                   )

        You can also use the ``^`` operator:

        >>> s1.index ^ s2.index  # doctest: +SKIP
        MultiIndex([('pandas-on-Spark', 'speed'),
                    (  'lama', 'speed')],
                   )
        """
    def drop(self, codes: List[Any], level: int | Name | None = None) -> MultiIndex:
        """
        Make new MultiIndex with passed list of labels deleted

        Parameters
        ----------
        codes : array-like
            Must be a list of tuples
        level : int or level name, default None

        Returns
        -------
        dropped : MultiIndex

        Examples
        --------
        >>> index = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> index # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y'),
                    ('c', 'z')],
                   )

        >>> index.drop(['a']) # doctest: +SKIP
        MultiIndex([('b', 'y'),
                    ('c', 'z')],
                   )

        >>> index.drop(['x', 'y'], level=1) # doctest: +SKIP
        MultiIndex([('c', 'z')],
                   )
        """
    def drop_duplicates(self, keep: bool | str = 'first') -> MultiIndex:
        '''
        Return MultiIndex with duplicate values removed.

        Parameters
        ----------
        keep : {\'first\', \'last\', ``False``}, default \'first\'
            Method to handle dropping duplicates:
            - \'first\' : Drop duplicates except for the first occurrence.
            - \'last\' : Drop duplicates except for the last occurrence.
            - ``False`` : Drop all duplicates.

        Returns
        -------
        deduplicated : MultiIndex

        See Also
        --------
        Series.drop_duplicates : Equivalent method on Series.
        DataFrame.drop_duplicates : Equivalent method on DataFrame.

        Examples
        --------
        Generate a MultiIndex with duplicate values.

        >>> arrays = [[1, 2, 3, 1, 2], ["red", "blue", "black", "red", "blue"]]
        >>> midx = ps.MultiIndex.from_arrays(arrays, names=("number", "color"))
        >>> midx
        MultiIndex([(1,   \'red\'),
                    (2,  \'blue\'),
                    (3, \'black\'),
                    (1,   \'red\'),
                    (2,  \'blue\')],
                   names=[\'number\', \'color\'])

        >>> midx.drop_duplicates()
        MultiIndex([(1,   \'red\'),
                    (2,  \'blue\'),
                    (3, \'black\')],
                   names=[\'number\', \'color\'])

        >>> midx.drop_duplicates(keep=\'first\')
        MultiIndex([(1,   \'red\'),
                    (2,  \'blue\'),
                    (3, \'black\')],
                   names=[\'number\', \'color\'])

        >>> midx.drop_duplicates(keep=\'last\')
        MultiIndex([(3, \'black\'),
                    (1,   \'red\'),
                    (2,  \'blue\')],
                   names=[\'number\', \'color\'])

        >>> midx.drop_duplicates(keep=False)
        MultiIndex([(3, \'black\')],
                   names=[\'number\', \'color\'])
        '''
    def argmax(self) -> None: ...
    def argmin(self) -> None: ...
    def asof(self, label: Any) -> None: ...
    @property
    def is_all_dates(self) -> bool:
        """
        is_all_dates always returns False for MultiIndex

        Examples
        --------
        >>> from datetime import datetime

        >>> idx = ps.MultiIndex.from_tuples(
        ...     [(datetime(2019, 1, 1, 0, 0, 0), datetime(2019, 1, 1, 0, 0, 0)),
        ...      (datetime(2019, 1, 1, 0, 0, 0), datetime(2019, 1, 1, 0, 0, 0))])
        >>> idx  # doctest: +SKIP
        MultiIndex([('2019-01-01', '2019-01-01'),
                    ('2019-01-01', '2019-01-01')],
                   )

        >>> idx.is_all_dates
        False
        """
    def __getattr__(self, item: str) -> Any: ...
    def get_level_values(self, level: int | Name) -> Index:
        """
        Return vector of label values for requested level,
        equal to the length of the index.

        Parameters
        ----------
        level : int or str
            ``level`` is either the integer position of the level in the
            MultiIndex, or the name of the level.

        Returns
        -------
        values : Index
            Values is a level of this MultiIndex converted to
            a single :class:`Index` (or subclass thereof).

        Examples
        --------

        Create a MultiIndex:

        >>> mi = ps.MultiIndex.from_tuples([('x', 'a'), ('x', 'b'), ('y', 'a')])
        >>> mi.names = ['level_1', 'level_2']

        Get level values by supplying level as either integer or name:

        >>> mi.get_level_values(0)
        Index(['x', 'x', 'y'], dtype='object', name='level_1')

        >>> mi.get_level_values('level_2')
        Index(['a', 'b', 'a'], dtype='object', name='level_2')
        """
    def insert(self, loc: int, item: Any) -> Index:
        '''
        Make new MultiIndex inserting new item at location.

        Follows Python list.append semantics for negative values.

        .. versionchanged:: 3.4.0
           Raise IndexError when loc is out of bounds to follow Pandas 1.4+ behavior

        Parameters
        ----------
        loc : int
        item : object

        Returns
        -------
        new_index : MultiIndex

        Examples
        --------
        >>> psmidx = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "z")])
        >>> psmidx.insert(3, ("h", "j"))  # doctest: +SKIP
        MultiIndex([(\'a\', \'x\'),
                    (\'b\', \'y\'),
                    (\'c\', \'z\'),
                    (\'h\', \'j\')],
                   )

        For negative values

        >>> psmidx.insert(-2, ("h", "j"))  # doctest: +SKIP
        MultiIndex([(\'a\', \'x\'),
                    (\'h\', \'j\'),
                    (\'b\', \'y\'),
                    (\'c\', \'z\')],
                   )
        '''
    def item(self) -> Tuple[Scalar, ...]:
        """
        Return the first element of the underlying data as a python tuple.

        Returns
        -------
        tuple
            The first element of MultiIndex.

        Raises
        ------
        ValueError
            If the data is not length-1.

        Examples
        --------
        >>> psmidx = ps.MultiIndex.from_tuples([('a', 'x')])
        >>> psmidx.item()
        ('a', 'x')
        """
    def intersection(self, other: DataFrame | Series | Index | List) -> MultiIndex:
        '''
        Form the intersection of two Index objects.

        This returns a new Index with elements common to the index and `other`.

        Parameters
        ----------
        other : Index or array-like

        Returns
        -------
        intersection : MultiIndex

        Examples
        --------
        >>> midx1 = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "z")])
        >>> midx2 = ps.MultiIndex.from_tuples([("c", "z"), ("d", "w")])
        >>> midx1.intersection(midx2).sort_values()  # doctest: +SKIP
        MultiIndex([(\'c\', \'z\')],
                   )
        '''
    def equal_levels(self, other: MultiIndex) -> bool:
        '''
        Return True if the levels of both MultiIndex objects are the same

        .. versionadded:: 3.3.0

        Examples
        --------
        >>> psmidx1 = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "z")])
        >>> psmidx2 = ps.MultiIndex.from_tuples([("b", "y"), ("a", "x"), ("c", "z")])
        >>> psmidx1.equal_levels(psmidx2)
        True

        >>> psmidx2 = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "j")])
        >>> psmidx1.equal_levels(psmidx2)
        False
        '''
    @property
    def hasnans(self) -> bool: ...
    @property
    def inferred_type(self) -> str:
        """
        Return a string of the type inferred from the values.
        """
    @property
    def asi8(self) -> None:
        """
        Integer representation of the values.
        """
    def factorize(self, sort: bool = True, na_sentinel: int | None = -1) -> Tuple['MultiIndex', pd.Index]: ...
    def __iter__(self) -> Iterator: ...
    def map(self, mapper: dict | Callable[[Any], Any] | pd.Series = None, na_action: str | None = None) -> Index: ...
