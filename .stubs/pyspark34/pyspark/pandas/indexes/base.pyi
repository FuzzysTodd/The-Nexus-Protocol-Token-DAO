import numpy as np
import pandas as pd
from _typeshed import Incomplete
from pyspark.pandas._typing import Dtype as Dtype, Label as Label, Name as Name, Scalar as Scalar
from pyspark.pandas.base import IndexOpsMixin as IndexOpsMixin
from pyspark.pandas.config import get_option as get_option, option_context as option_context
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.internal import DEFAULT_SERIES_NAME as DEFAULT_SERIES_NAME, InternalField as InternalField, InternalFrame as InternalFrame, SPARK_DEFAULT_INDEX_NAME as SPARK_DEFAULT_INDEX_NAME, SPARK_INDEX_NAME_FORMAT as SPARK_INDEX_NAME_FORMAT
from pyspark.pandas.missing.indexes import MissingPandasLikeIndex as MissingPandasLikeIndex
from pyspark.pandas.series import Series as Series, first_series as first_series
from pyspark.pandas.spark.accessors import SparkIndexMethods as SparkIndexMethods, SparkIndexOpsMethods as SparkIndexOpsMethods
from pyspark.pandas.utils import ERROR_MESSAGE_CANNOT_COMBINE as ERROR_MESSAGE_CANNOT_COMBINE, is_name_like_tuple as is_name_like_tuple, is_name_like_value as is_name_like_value, log_advice as log_advice, name_like_string as name_like_string, same_anchor as same_anchor, scol_for as scol_for, validate_bool_kwarg as validate_bool_kwarg, validate_index_loc as validate_index_loc, verify_temp_column_name as verify_temp_column_name
from pyspark.sql import Column as Column
from pyspark.sql.types import DayTimeIntervalType as DayTimeIntervalType, FractionalType as FractionalType, IntegralType as IntegralType, TimestampNTZType as TimestampNTZType, TimestampType as TimestampType
from typing import Any, Callable, Iterator, List, Tuple

class Index(IndexOpsMixin):
    """
    pandas-on-Spark Index that corresponds to pandas Index logically. This might hold Spark Column
    internally.

    Parameters
    ----------
    data : array-like (1-dimensional)
    dtype : dtype, default None
        If dtype is None, we find the dtype that best fits the data.
        If an actual dtype is provided, we coerce to that dtype if it's safe.
        Otherwise, an error will be raised.
    copy : bool
        Make a copy of input ndarray.
    name : object
        Name to be stored in the index.
    tupleize_cols : bool (default: True)
        When True, attempt to create a MultiIndex if possible.

    See Also
    --------
    MultiIndex : A multi-level, or hierarchical, Index.
    DatetimeIndex : Index of datetime64 data.
    Int64Index : A special case of :class:`Index` with purely integer labels.
    Float64Index : A special case of :class:`Index` with purely float labels.

    Examples
    --------
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[1, 2, 3]).index
    Int64Index([1, 2, 3], dtype='int64')

    >>> ps.DataFrame({'a': [1, 2, 3]}, index=list('abc')).index
    Index(['a', 'b', 'c'], dtype='object')

    >>> ps.Index([1, 2, 3])
    Int64Index([1, 2, 3], dtype='int64')

    >>> ps.Index(list('abc'))
    Index(['a', 'b', 'c'], dtype='object')

    From a Series:

    >>> s = ps.Series([1, 2, 3], index=[10, 20, 30])
    >>> ps.Index(s)
    Int64Index([1, 2, 3], dtype='int64')

    From an Index:

    >>> idx = ps.Index([1, 2, 3])
    >>> ps.Index(idx)
    Int64Index([1, 2, 3], dtype='int64')
    """
    def __new__(cls, data: Any | None = None, dtype: str | Dtype | None = None, copy: bool = False, name: Name | None = None, tupleize_cols: bool = True, **kwargs: Any) -> Index: ...
    spark: SparkIndexOpsMethods
    @property
    def size(self) -> int:
        """
        Return an int representing the number of elements in this object.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'],
        ...                   index=list('abcd'))
        >>> df.index.size
        4

        >>> df.set_index('dogs', append=True).index.size
        4
        """
    @property
    def shape(self) -> tuple:
        """
        Return a tuple of the shape of the underlying data.

        Examples
        --------
        >>> idx = ps.Index(['a', 'b', 'c'])
        >>> idx
        Index(['a', 'b', 'c'], dtype='object')
        >>> idx.shape
        (3,)

        >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> midx  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y'),
                    ('c', 'z')],
                   )
        >>> midx.shape
        (3,)
        """
    def identical(self, other: Index) -> bool:
        """
        Similar to equals, but check that other comparable attributes are
        also equal.

        Returns
        -------
        bool
            If two Index objects have equal elements and same type True,
            otherwise False.

        Examples
        --------

        >>> from pyspark.pandas.config import option_context
        >>> idx = ps.Index(['a', 'b', 'c'])
        >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])

        For Index

        >>> idx.identical(idx)
        True
        >>> with option_context('compute.ops_on_diff_frames', True):
        ...     idx.identical(ps.Index(['a', 'b', 'c']))
        True
        >>> with option_context('compute.ops_on_diff_frames', True):
        ...     idx.identical(ps.Index(['b', 'b', 'a']))
        False
        >>> idx.identical(midx)
        False

        For MultiIndex

        >>> midx.identical(midx)
        True
        >>> with option_context('compute.ops_on_diff_frames', True):
        ...     midx.identical(ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')]))
        True
        >>> with option_context('compute.ops_on_diff_frames', True):
        ...     midx.identical(ps.MultiIndex.from_tuples([('c', 'z'), ('b', 'y'), ('a', 'x')]))
        False
        >>> midx.identical(idx)
        False
        """
    def equals(self, other: Index) -> bool:
        '''
        Determine if two Index objects contain the same elements.

        Returns
        -------
        bool
            True if "other" is an Index and it has the same elements as calling
            index; False otherwise.

        Examples
        --------

        >>> from pyspark.pandas.config import option_context
        >>> idx = ps.Index([\'a\', \'b\', \'c\'])
        >>> idx.name = "name"
        >>> midx = ps.MultiIndex.from_tuples([(\'a\', \'x\'), (\'b\', \'y\'), (\'c\', \'z\')])
        >>> midx.names = ("nameA", "nameB")

        For Index

        >>> idx.equals(idx)
        True
        >>> with option_context(\'compute.ops_on_diff_frames\', True):
        ...     idx.equals(ps.Index([\'a\', \'b\', \'c\']))
        True
        >>> with option_context(\'compute.ops_on_diff_frames\', True):
        ...     idx.equals(ps.Index([\'b\', \'b\', \'a\']))
        False
        >>> idx.equals(midx)
        False

        For MultiIndex

        >>> midx.equals(midx)
        True
        >>> with option_context(\'compute.ops_on_diff_frames\', True):
        ...     midx.equals(ps.MultiIndex.from_tuples([(\'a\', \'x\'), (\'b\', \'y\'), (\'c\', \'z\')]))
        True
        >>> with option_context(\'compute.ops_on_diff_frames\', True):
        ...     midx.equals(ps.MultiIndex.from_tuples([(\'c\', \'z\'), (\'b\', \'y\'), (\'a\', \'x\')]))
        False
        >>> midx.equals(idx)
        False
        '''
    def transpose(self) -> Index:
        """
        Return the transpose, For index, It will be index itself.

        Examples
        --------
        >>> idx = ps.Index(['a', 'b', 'c'])
        >>> idx
        Index(['a', 'b', 'c'], dtype='object')

        >>> idx.transpose()
        Index(['a', 'b', 'c'], dtype='object')

        For MultiIndex

        >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> midx  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y'),
                    ('c', 'z')],
                   )

        >>> midx.transpose()  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y'),
                    ('c', 'z')],
                   )
        """
    T: Incomplete
    def to_pandas(self) -> pd.Index:
        """
        Return a pandas Index.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver's memory.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'],
        ...                   index=list('abcd'))
        >>> df['dogs'].index.to_pandas()
        Index(['a', 'b', 'c', 'd'], dtype='object')
        """
    def to_numpy(self, dtype: str | Dtype | None = None, copy: bool = False) -> np.ndarray:
        """
        A NumPy ndarray representing the values in this Index or MultiIndex.

        .. note:: This method should only be used if the resulting NumPy ndarray is expected
            to be small, as all the data is loaded into the driver's memory.

        Parameters
        ----------
        dtype : str or numpy.dtype, optional
            The dtype to pass to :meth:`numpy.asarray`
        copy : bool, default False
            Whether to ensure that the returned value is not a view on
            another array. Note that ``copy=False`` does not *ensure* that
            ``to_numpy()`` is no-copy. Rather, ``copy=True`` ensures that
            a copy is made, even if not strictly necessary.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        >>> ps.Series([1, 2, 3, 4]).index.to_numpy()
        array([0, 1, 2, 3])
        >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index.to_numpy()
        array([(1, 4), (2, 5), (3, 6)], dtype=object)
        """
    def map(self, mapper: dict | Callable[[Any], Any] | pd.Series, na_action: str | None = None) -> Index:
        '''
        Map values using input correspondence (a dict, Series, or function).

        Parameters
        ----------
        mapper : function, dict, or pd.Series
            Mapping correspondence.
        na_action : {None, \'ignore\'}
            If ‘ignore’, propagate NA values, without passing them to the mapping correspondence.

        Returns
        -------
        applied : Index, inferred
            The output of the mapping function applied to the index.

        Examples
        --------
        >>> psidx = ps.Index([1, 2, 3])

        >>> psidx.map({1: "one", 2: "two", 3: "three"})
        Index([\'one\', \'two\', \'three\'], dtype=\'object\')

        >>> psidx.map(lambda id: "{id} + 1".format(id=id))
        Index([\'1 + 1\', \'2 + 1\', \'3 + 1\'], dtype=\'object\')

        >>> pser = pd.Series(["one", "two", "three"], index=[1, 2, 3])
        >>> psidx.map(pser)
        Index([\'one\', \'two\', \'three\'], dtype=\'object\')
        '''
    @property
    def values(self) -> np.ndarray:
        """
        Return an array representing the data in the Index.

        .. warning:: We recommend using `Index.to_numpy()` instead.

        .. note:: This method should only be used if the resulting NumPy ndarray is expected
            to be small, as all the data is loaded into the driver's memory.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        >>> ps.Series([1, 2, 3, 4]).index.values
        array([0, 1, 2, 3])
        >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index.values
        array([(1, 4), (2, 5), (3, 6)], dtype=object)
        """
    @property
    def asi8(self) -> np.ndarray:
        """
        Integer representation of the values.

        .. warning:: We recommend using `Index.to_numpy()` instead.

        .. note:: This method should only be used if the resulting NumPy ndarray is expected
            to be small, as all the data is loaded into the driver's memory.

        .. deprecated:: 3.4.0

        Returns
        -------
        numpy.ndarray
            An ndarray with int64 dtype.

        Examples
        --------
        >>> ps.Index([1, 2, 3]).asi8
        array([1, 2, 3])

        Returns None for non-int64 dtype

        >>> ps.Index(['a', 'b', 'c']).asi8 is None
        True
        """
    @property
    def has_duplicates(self) -> bool:
        '''
        If index has duplicates, return True, otherwise False.

        Examples
        --------
        >>> idx = ps.Index([1, 5, 7, 7])
        >>> idx.has_duplicates
        True

        >>> idx = ps.Index([1, 5, 7])
        >>> idx.has_duplicates
        False

        >>> idx = ps.Index(["Watermelon", "Orange", "Apple",
        ...                 "Watermelon"])
        >>> idx.has_duplicates
        True

        >>> idx = ps.Index(["Orange", "Apple",
        ...                 "Watermelon"])
        >>> idx.has_duplicates
        False
        '''
    @property
    def is_unique(self) -> bool:
        '''
        Return if the index has unique values.

        Examples
        --------
        >>> idx = ps.Index([1, 5, 7, 7])
        >>> idx.is_unique
        False

        >>> idx = ps.Index([1, 5, 7])
        >>> idx.is_unique
        True

        >>> idx = ps.Index(["Watermelon", "Orange", "Apple",
        ...                 "Watermelon"])
        >>> idx.is_unique
        False

        >>> idx = ps.Index(["Orange", "Apple",
        ...                 "Watermelon"])
        >>> idx.is_unique
        True
        '''
    @property
    def name(self) -> Name:
        """Return name of the Index."""
    @name.setter
    def name(self, name: Name) -> None: ...
    @property
    def names(self) -> List[Name]:
        """Return names of the Index."""
    @names.setter
    def names(self, names: List[Name]) -> None: ...
    @property
    def nlevels(self) -> int:
        '''
        Number of levels in Index & MultiIndex.

        Examples
        --------
        >>> psdf = ps.DataFrame({"a": [1, 2, 3]}, index=pd.Index([\'a\', \'b\', \'c\'], name="idx"))
        >>> psdf.index.nlevels
        1

        >>> psdf = ps.DataFrame({\'a\': [1, 2, 3]}, index=[list(\'abc\'), list(\'def\')])
        >>> psdf.index.nlevels
        2
        '''
    def rename(self, name: Name | List[Name], inplace: bool = False) -> Index | None:
        '''
        Alter Index or MultiIndex name.
        Able to set new names without level. Defaults to returning a new index.

        Parameters
        ----------
        name : label or list of labels
            Name(s) to set.
        inplace : boolean, default False
            Modifies the object directly, instead of creating a new Index or MultiIndex.

        Returns
        -------
        Index or MultiIndex
            The same type as the caller or None if inplace is True.

        Examples
        --------
        >>> df = ps.DataFrame({\'a\': [\'A\', \'C\'], \'b\': [\'A\', \'B\']}, columns=[\'a\', \'b\'])
        >>> df.index.rename("c")
        Int64Index([0, 1], dtype=\'int64\', name=\'c\')

        >>> df.set_index("a", inplace=True)
        >>> df.index.rename("d")
        Index([\'A\', \'C\'], dtype=\'object\', name=\'d\')

        You can also change the index name in place.

        >>> df.index.rename("e", inplace=True)
        >>> df.index
        Index([\'A\', \'C\'], dtype=\'object\', name=\'e\')

        >>> df  # doctest: +NORMALIZE_WHITESPACE
           b
        e
        A  A
        C  B

        Support for MultiIndex

        >>> psidx = ps.MultiIndex.from_tuples([(\'a\', \'x\'), (\'b\', \'y\')])
        >>> psidx.names = [\'hello\', \'pandas-on-Spark\']
        >>> psidx  # doctest: +SKIP
        MultiIndex([(\'a\', \'x\'),
                    (\'b\', \'y\')],
                   names=[\'hello\', \'pandas-on-Spark\'])

        >>> psidx.rename([\'aloha\', \'databricks\'])  # doctest: +SKIP
        MultiIndex([(\'a\', \'x\'),
                    (\'b\', \'y\')],
                   names=[\'aloha\', \'databricks\'])
        '''
    def fillna(self, value: Scalar) -> Index:
        """
        Fill NA/NaN values with the specified value.

        Parameters
        ----------
        value : scalar
            Scalar value to use to fill holes (example: 0). This value cannot be a list-likes.

        Returns
        -------
        Index :
            filled with value

        Examples
        --------
        >>> idx = ps.Index([1, 2, None])
        >>> idx
        Float64Index([1.0, 2.0, nan], dtype='float64')

        >>> idx.fillna(0)
        Float64Index([1.0, 2.0, 0.0], dtype='float64')
        """
    def drop_duplicates(self, keep: bool | str = 'first') -> Index:
        """
        Return Index with duplicate values removed.

        Parameters
        ----------
        keep : {'first', 'last', ``False``}, default 'first'
            Method to handle dropping duplicates:
            - 'first' : Drop duplicates except for the first occurrence.
            - 'last' : Drop duplicates except for the last occurrence.
            - ``False`` : Drop all duplicates.

        Returns
        -------
        deduplicated : Index

        See Also
        --------
        Series.drop_duplicates : Equivalent method on Series.
        DataFrame.drop_duplicates : Equivalent method on DataFrame.

        Examples
        --------
        Generate an Index with duplicate values.

        >>> idx = ps.Index(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo'])

        >>> idx.drop_duplicates().sort_values()
        Index(['beetle', 'cow', 'hippo', 'lama'], dtype='object')
        """
    def to_series(self, name: Name | None = None) -> Series:
        """
        Create a Series with both index and values equal to the index keys
        useful with map for returning an indexer based on an index.

        Parameters
        ----------
        name : string, optional
            name of resulting Series. If None, defaults to name of original
            index

        Returns
        -------
        Series : dtype will be based on the type of the Index values.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'],
        ...                   index=list('abcd'))
        >>> df['dogs'].index.to_series()
        a    a
        b    b
        c    c
        d    d
        dtype: object
        """
    def to_frame(self, index: bool = True, name: Name | None = None) -> DataFrame:
        """
        Create a DataFrame with a column containing the Index.

        Parameters
        ----------
        index : boolean, default True
            Set the index of the returned DataFrame as the original Index.
        name : object, default None
            The passed name should substitute for the index name (if it has
            one).

        Returns
        -------
        DataFrame
            DataFrame containing the original Index data.

        See Also
        --------
        Index.to_series : Convert an Index to a Series.
        Series.to_frame : Convert Series to DataFrame.

        Examples
        --------
        >>> idx = ps.Index(['Ant', 'Bear', 'Cow'], name='animal')
        >>> idx.to_frame()  # doctest: +NORMALIZE_WHITESPACE
               animal
        animal
        Ant       Ant
        Bear     Bear
        Cow       Cow

        By default, the original Index is reused. To enforce a new Index:

        >>> idx.to_frame(index=False)
          animal
        0    Ant
        1   Bear
        2    Cow

        To override the name of the resulting column, specify `name`:

        >>> idx.to_frame(name='zoo')  # doctest: +NORMALIZE_WHITESPACE
                 zoo
        animal
        Ant      Ant
        Bear    Bear
        Cow      Cow
        """
    def is_boolean(self) -> bool:
        """
        Return if the current index type is a boolean type.

        Examples
        --------
        >>> ps.DataFrame({'a': [1]}, index=[True]).index.is_boolean()
        True
        """
    def is_categorical(self) -> bool:
        """
        Return if the current index type is a categorical type.

        Examples
        --------
        >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_categorical()
        False
        """
    def is_floating(self) -> bool:
        """
        Return if the current index type is a floating type.

        Examples
        --------
        >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_floating()
        False
        """
    def is_integer(self) -> bool:
        """
        Return if the current index type is an integer type.

        Examples
        --------
        >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_integer()
        True
        """
    def is_interval(self) -> bool:
        """
        Return if the current index type is an interval type.

        Examples
        --------
        >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_interval()
        False
        """
    def is_numeric(self) -> bool:
        """
        Return if the current index type is a numeric type.

        Examples
        --------
        >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_numeric()
        True
        """
    def is_object(self) -> bool:
        '''
        Return if the current index type is an object type.

        Examples
        --------
        >>> ps.DataFrame({\'a\': [1]}, index=["a"]).index.is_object()
        True
        '''
    def is_type_compatible(self, kind: str) -> bool:
        """
        Whether the index type is compatible with the provided type.

        .. deprecated:: 3.4.0

        Examples
        --------
        >>> psidx = ps.Index([1, 2, 3])
        >>> psidx.is_type_compatible('integer')
        True

        >>> psidx = ps.Index([1.0, 2.0, 3.0])
        >>> psidx.is_type_compatible('integer')
        False
        >>> psidx.is_type_compatible('floating')
        True
        """
    def dropna(self, how: str = 'any') -> Index:
        '''
        Return Index or MultiIndex without NA/NaN values

        Parameters
        ----------
        how : {\'any\', \'all\'}, default \'any\'
            If the Index is a MultiIndex, drop the value when any or all levels
            are NaN.

        Returns
        -------
        Index or MultiIndex

        Examples
        --------

        >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
        ...                   index=[\'cobra\', \'viper\', None],
        ...                   columns=[\'max_speed\', \'shield\'])
        >>> df  # doctest: +SKIP
               max_speed  shield
        cobra          1       2
        viper          4       5
        None           7       8

        >>> df.index.dropna()
        Index([\'cobra\', \'viper\'], dtype=\'object\')

        Also support for MultiIndex


        >>> tuples = [(np.nan, 1.0), (2.0, 2.0), (np.nan, np.nan), (3.0, np.nan)]
        >>> midx = ps.MultiIndex.from_tuples(tuples)
        >>> midx  # doctest: +SKIP
        MultiIndex([(nan, 1.0),
                    (2.0, 2.0),
                    (nan, nan),
                    (3.0, nan)],
                   )

        >>> midx.dropna()  # doctest: +SKIP
        MultiIndex([(2.0, 2.0)],
                   )

        >>> midx.dropna(how="all")  # doctest: +SKIP
        MultiIndex([(nan, 1.0),
                    (2.0, 2.0),
                    (3.0, nan)],
                   )
        '''
    def unique(self, level: int | Name | None = None) -> Index:
        '''
        Return unique values in the index.

        Be aware the order of unique values might be different than pandas.Index.unique

        Parameters
        ----------
        level : int or str, optional, default is None

        Returns
        -------
        Index without duplicates

        See Also
        --------
        Series.unique
        groupby.SeriesGroupBy.unique

        Examples
        --------
        >>> ps.DataFrame({\'a\': [\'a\', \'b\', \'c\']}, index=[1, 1, 3]).index.unique().sort_values()
        Int64Index([1, 3], dtype=\'int64\')

        >>> ps.DataFrame({\'a\': [\'a\', \'b\', \'c\']}, index=[\'d\', \'e\', \'e\']).index.unique().sort_values()
        Index([\'d\', \'e\'], dtype=\'object\')

        MultiIndex

        >>> ps.MultiIndex.from_tuples([("A", "X"), ("A", "Y"), ("A", "X")]).unique()
        ... # doctest: +SKIP
        MultiIndex([(\'A\', \'X\'),
                    (\'A\', \'Y\')],
                   )
        '''
    def drop(self, labels: List[Any]) -> Index:
        """
        Make new Index with passed list of labels deleted.

        Parameters
        ----------
        labels : array-like

        Returns
        -------
        dropped : Index

        Examples
        --------
        >>> index = ps.Index([1, 2, 3])
        >>> index
        Int64Index([1, 2, 3], dtype='int64')

        >>> index.drop([1])
        Int64Index([2, 3], dtype='int64')
        """
    def get_level_values(self, level: int | Name) -> Index:
        """
        Return Index if a valid level is given.

        Examples
        --------
        >>> psidx = ps.Index(['a', 'b', 'c'], name='ks')
        >>> psidx.get_level_values(0)
        Index(['a', 'b', 'c'], dtype='object', name='ks')

        >>> psidx.get_level_values('ks')
        Index(['a', 'b', 'c'], dtype='object', name='ks')
        """
    def copy(self, name: Name | None = None, deep: bool | None = None) -> Index:
        """
        Make a copy of this object. name sets those attributes on the new object.

        Parameters
        ----------
        name : string, optional
            to set name of index
        deep : None
            this parameter is not supported but just dummy parameter to match pandas.

        Examples
        --------
        >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
        ...                   index=['cobra', 'viper', 'sidewinder'],
        ...                   columns=['max_speed', 'shield'])
        >>> df
                    max_speed  shield
        cobra               1       2
        viper               4       5
        sidewinder          7       8
        >>> df.index
        Index(['cobra', 'viper', 'sidewinder'], dtype='object')

        Copy index

        >>> df.index.copy()
        Index(['cobra', 'viper', 'sidewinder'], dtype='object')

        Copy index with name

        >>> df.index.copy(name='snake')
        Index(['cobra', 'viper', 'sidewinder'], dtype='object', name='snake')
        """
    def droplevel(self, level: int | Name | List[int | Name]) -> Index:
        '''
        Return index with requested level(s) removed.
        If resulting index has only 1 level left, the result will be
        of Index type, not MultiIndex.

        Parameters
        ----------
        level : int, str, tuple, or list-like, default 0
            If a string is given, must be the name of a level
            If list-like, elements must be names or indexes of levels.

        Returns
        -------
        Index or MultiIndex

        Examples
        --------
        >>> midx = ps.DataFrame({\'a\': [\'a\', \'b\']}, index=[[\'a\', \'x\'], [\'b\', \'y\'], [1, 2]]).index
        >>> midx  # doctest: +SKIP
        MultiIndex([(\'a\', \'b\', 1),
                    (\'x\', \'y\', 2)],
                   )
        >>> midx.droplevel([0, 1])  # doctest: +SKIP
        Int64Index([1, 2], dtype=\'int64\')
        >>> midx.droplevel(0)  # doctest: +SKIP
        MultiIndex([(\'b\', 1),
                    (\'y\', 2)],
                   )
        >>> midx.names = [("a", "b"), "b", "c"]
        >>> midx.droplevel([(\'a\', \'b\')])  # doctest: +SKIP
        MultiIndex([(\'b\', 1),
                    (\'y\', 2)],
                   names=[\'b\', \'c\'])
        '''
    def symmetric_difference(self, other: Index, result_name: Name | None = None, sort: bool | None = None) -> Index:
        """
        Compute the symmetric difference of two Index objects.

        Parameters
        ----------
        other : Index or array-like
        result_name : str
        sort : True or None, default None
            Whether to sort the resulting index.
            * True : Attempt to sort the result.
            * None : Do not sort the result.

        Returns
        -------
        symmetric_difference : Index

        Notes
        -----
        ``symmetric_difference`` contains elements that appear in either
        ``idx1`` or ``idx2`` but not both. Equivalent to the Index created by
        ``idx1.difference(idx2) | idx2.difference(idx1)`` with duplicates
        dropped.

        Examples
        --------
        >>> s1 = ps.Series([1, 2, 3, 4], index=[1, 2, 3, 4])
        >>> s2 = ps.Series([1, 2, 3, 4], index=[2, 3, 4, 5])

        >>> s1.index.symmetric_difference(s2.index)  # doctest: +SKIP
        Int64Index([5, 1], dtype='int64')

        You can set name of result Index.

        >>> s1.index.symmetric_difference(s2.index, result_name='pandas-on-Spark')  # doctest: +SKIP
        Int64Index([5, 1], dtype='int64', name='pandas-on-Spark')

        You can set sort to `True`, if you want to sort the resulting index.

        >>> s1.index.symmetric_difference(s2.index, sort=True)
        Int64Index([1, 5], dtype='int64')

        You can also use the ``^`` operator:

        >>> s1.index ^ s2.index  # doctest: +SKIP
        Int64Index([5, 1], dtype='int64')
        """
    def sort_values(self, return_indexer: bool = False, ascending: bool = True) -> Index | Tuple['Index', 'Index']:
        """
        Return a sorted copy of the index, and optionally return the indices that
        sorted the index itself.

        .. note:: This method is not supported for pandas when index has NaN value.
                  pandas raises unexpected TypeError, but we support treating NaN
                  as the smallest value.
                  This method returns indexer as a pandas-on-Spark index while
                  pandas returns it as a list. That's because indexer in pandas-on-Spark
                  may not fit in memory.

        Parameters
        ----------
        return_indexer : bool, default False
            Should the indices that would sort the index be returned.
        ascending : bool, default True
            Should the index values be sorted in an ascending order.

        Returns
        -------
        sorted_index : ps.Index or ps.MultiIndex
            Sorted copy of the index.
        indexer : ps.Index
            The indices that the index itself was sorted by.

        See Also
        --------
        Series.sort_values : Sort values of a Series.
        DataFrame.sort_values : Sort values in a DataFrame.

        Examples
        --------
        >>> idx = ps.Index([10, 100, 1, 1000])
        >>> idx
        Int64Index([10, 100, 1, 1000], dtype='int64')

        Sort values in ascending order (default behavior).

        >>> idx.sort_values()
        Int64Index([1, 10, 100, 1000], dtype='int64')

        Sort values in descending order.

        >>> idx.sort_values(ascending=False)
        Int64Index([1000, 100, 10, 1], dtype='int64')

        Sort values in descending order, and also get the indices idx was sorted by.

        >>> idx.sort_values(ascending=False, return_indexer=True)
        (Int64Index([1000, 100, 10, 1], dtype='int64'), Int64Index([3, 1, 0, 2], dtype='int64'))

        Support for MultiIndex.

        >>> psidx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('c', 'y', 2), ('b', 'z', 3)])
        >>> psidx  # doctest: +SKIP
        MultiIndex([('a', 'x', 1),
                    ('c', 'y', 2),
                    ('b', 'z', 3)],
                   )

        >>> psidx.sort_values()  # doctest: +SKIP
        MultiIndex([('a', 'x', 1),
                    ('b', 'z', 3),
                    ('c', 'y', 2)],
                   )

        >>> psidx.sort_values(ascending=False)  # doctest: +SKIP
        MultiIndex([('c', 'y', 2),
                    ('b', 'z', 3),
                    ('a', 'x', 1)],
                   )

        >>> psidx.sort_values(ascending=False, return_indexer=True)  # doctest: +SKIP
        (MultiIndex([('c', 'y', 2),
                    ('b', 'z', 3),
                    ('a', 'x', 1)],
                   ), Int64Index([1, 2, 0], dtype='int64'))
        """
    def sort(self, *args, **kwargs) -> None:
        """
        Use sort_values instead.
        """
    def min(self) -> Scalar | Tuple[Scalar, ...]:
        """
        Return the minimum value of the Index.

        Returns
        -------
        scalar
            Minimum value.

        See Also
        --------
        Index.max : Return the maximum value of the object.
        Series.min : Return the minimum value in a Series.
        DataFrame.min : Return the minimum values in a DataFrame.

        Examples
        --------
        >>> idx = ps.Index([3, 2, 1])
        >>> idx.min()
        1

        >>> idx = ps.Index(['c', 'b', 'a'])
        >>> idx.min()
        'a'

        For a MultiIndex, the maximum is determined lexicographically.

        >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
        >>> idx.min()
        ('a', 'x', 1)
        """
    def max(self) -> Scalar | Tuple[Scalar, ...]:
        """
        Return the maximum value of the Index.

        Returns
        -------
        scalar
            Maximum value.

        See Also
        --------
        Index.min : Return the minimum value in an Index.
        Series.max : Return the maximum value in a Series.
        DataFrame.max : Return the maximum values in a DataFrame.

        Examples
        --------
        >>> idx = ps.Index([3, 2, 1])
        >>> idx.max()
        3

        >>> idx = ps.Index(['c', 'b', 'a'])
        >>> idx.max()
        'c'

        For a MultiIndex, the maximum is determined lexicographically.

        >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
        >>> idx.max()
        ('b', 'y', 2)
        """
    def delete(self, loc: int | List[int]) -> Index:
        """
        Make new Index with passed location(-s) deleted.

        .. note:: this API can be pretty expensive since it is based on
             a global sequence internally.

        Returns
        -------
        new_index : Index

        Examples
        --------
        >>> psidx = ps.Index([10, 10, 9, 8, 4, 2, 4, 4, 2, 2, 10, 10])
        >>> psidx
        Int64Index([10, 10, 9, 8, 4, 2, 4, 4, 2, 2, 10, 10], dtype='int64')

        >>> psidx.delete(0).sort_values()
        Int64Index([2, 2, 2, 4, 4, 4, 8, 9, 10, 10, 10], dtype='int64')

        >>> psidx.delete([0, 1, 2, 3, 10, 11]).sort_values()
        Int64Index([2, 2, 2, 4, 4, 4], dtype='int64')

        MultiIndex

        >>> psidx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)])
        >>> psidx  # doctest: +SKIP
        MultiIndex([('a', 'x', 1),
                    ('b', 'y', 2),
                    ('c', 'z', 3)],
                   )

        >>> psidx.delete([0, 2]).sort_values()  # doctest: +SKIP
        MultiIndex([('b', 'y', 2)],
                   )
        """
    def append(self, other: Index) -> Index:
        """
        Append a collection of Index options together.

        Parameters
        ----------
        other : Index

        Returns
        -------
        appended : Index

        Examples
        --------
        >>> psidx = ps.Index([10, 5, 0, 5, 10, 5, 0, 10])
        >>> psidx
        Int64Index([10, 5, 0, 5, 10, 5, 0, 10], dtype='int64')

        >>> psidx.append(psidx)
        Int64Index([10, 5, 0, 5, 10, 5, 0, 10, 10, 5, 0, 5, 10, 5, 0, 10], dtype='int64')

        Support for MiltiIndex

        >>> psidx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y')])
        >>> psidx  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y')],
                   )

        >>> psidx.append(psidx)  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y'),
                    ('a', 'x'),
                    ('b', 'y')],
                   )
        """
    def argmax(self) -> int:
        """
        Return a maximum argument indexer.

        Parameters
        ----------
        skipna : bool, default True

        Returns
        -------
        maximum argument indexer

        Examples
        --------
        >>> psidx = ps.Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3])
        >>> psidx
        Int64Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3], dtype='int64')

        >>> psidx.argmax()
        4
        """
    def argmin(self) -> int:
        """
        Return a minimum argument indexer.

        Parameters
        ----------
        skipna : bool, default True

        Returns
        -------
        minimum argument indexer

        Examples
        --------
        >>> psidx = ps.Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3])
        >>> psidx
        Int64Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3], dtype='int64')

        >>> psidx.argmin()
        7
        """
    def set_names(self, names: Name | List[Name], level: int | Name | List[int | Name] | None = None, inplace: bool = False) -> Index | None:
        """
        Set Index or MultiIndex name.
        Able to set new names partially and by level.

        Parameters
        ----------
        names : label or list of label
            Name(s) to set.
        level : int, label or list of int or label, optional
            If the index is a MultiIndex, level(s) to set (None for all
            levels). Otherwise level must be None.
        inplace : bool, default False
            Modifies the object directly, instead of creating a new Index or
            MultiIndex.

        Returns
        -------
        Index
            The same type as the caller or None if inplace is True.

        See Also
        --------
        Index.rename : Able to set new names without level.

        Examples
        --------
        >>> idx = ps.Index([1, 2, 3, 4])
        >>> idx
        Int64Index([1, 2, 3, 4], dtype='int64')

        >>> idx.set_names('quarter')
        Int64Index([1, 2, 3, 4], dtype='int64', name='quarter')

        For MultiIndex

        >>> idx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y')])
        >>> idx  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y')],
                   )

        >>> idx.set_names(['kind', 'year'], inplace=True)
        >>> idx  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y')],
                   names=['kind', 'year'])

        >>> idx.set_names('species', level=0)  # doctest: +SKIP
        MultiIndex([('a', 'x'),
                    ('b', 'y')],
                   names=['species', 'year'])
        """
    def difference(self, other: Index, sort: bool | None = None) -> Index:
        """
        Return a new Index with elements from the index that are not in
        `other`.

        This is the set difference of two Index objects.

        Parameters
        ----------
        other : Index or array-like
        sort : True or None, default None
            Whether to sort the resulting index.
            * True : Attempt to sort the result.
            * None : Do not sort the result.

        Returns
        -------
        difference : Index

        Examples
        --------

        >>> idx1 = ps.Index([2, 1, 3, 4])
        >>> idx2 = ps.Index([3, 4, 5, 6])
        >>> idx1.difference(idx2, sort=True)
        Int64Index([1, 2], dtype='int64')

        MultiIndex

        >>> midx1 = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)])
        >>> midx2 = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'z', 2), ('k', 'z', 3)])
        >>> midx1.difference(midx2)  # doctest: +SKIP
        MultiIndex([('b', 'y', 2),
                    ('c', 'z', 3)],
                   )
        """
    @property
    def is_all_dates(self) -> bool:
        """
        Return if all data types of the index are datetime.
        remember that since pandas-on-Spark does not support multiple data types in an index,
        so it returns True if any type of data is datetime.

        .. deprecated:: 3.4.0

        Examples
        --------
        >>> from datetime import datetime

        >>> idx = ps.Index([datetime(2019, 1, 1, 0, 0, 0), datetime(2019, 2, 3, 0, 0, 0)])
        >>> idx
        DatetimeIndex(['2019-01-01', '2019-02-03'], dtype='datetime64[ns]', freq=None)

        >>> idx.is_all_dates
        True

        >>> idx = ps.Index([datetime(2019, 1, 1, 0, 0, 0), None])
        >>> idx
        DatetimeIndex(['2019-01-01', 'NaT'], dtype='datetime64[ns]', freq=None)

        >>> idx.is_all_dates
        True

        >>> idx = ps.Index([0, 1, 2])
        >>> idx
        Int64Index([0, 1, 2], dtype='int64')

        >>> idx.is_all_dates
        False
        """
    def repeat(self, repeats: int) -> Index:
        """
        Repeat elements of a Index/MultiIndex.

        Returns a new Index/MultiIndex where each element of the current Index/MultiIndex
        is repeated consecutively a given number of times.

        Parameters
        ----------
        repeats : int
            The number of repetitions for each element. This should be a
            non-negative integer. Repeating 0 times will return an empty
            Index.

        Returns
        -------
        repeated_index : Index/MultiIndex
            Newly created Index/MultiIndex with repeated elements.

        See Also
        --------
        Series.repeat : Equivalent function for Series.

        Examples
        --------
        >>> idx = ps.Index(['a', 'b', 'c'])
        >>> idx
        Index(['a', 'b', 'c'], dtype='object')
        >>> idx.repeat(2)
        Index(['a', 'b', 'c', 'a', 'b', 'c'], dtype='object')

        For MultiIndex,

        >>> midx = ps.MultiIndex.from_tuples([('x', 'a'), ('x', 'b'), ('y', 'c')])
        >>> midx  # doctest: +SKIP
        MultiIndex([('x', 'a'),
                    ('x', 'b'),
                    ('y', 'c')],
                   )
        >>> midx.repeat(2)  # doctest: +SKIP
        MultiIndex([('x', 'a'),
                    ('x', 'b'),
                    ('y', 'c'),
                    ('x', 'a'),
                    ('x', 'b'),
                    ('y', 'c')],
                   )
        >>> midx.repeat(0)  # doctest: +SKIP
        MultiIndex([], )
        """
    def asof(self, label: Any) -> Scalar:
        """
        Return the label from the index, or, if not present, the previous one.

        Assuming that the index is sorted, return the passed index label if it
        is in the index, or return the previous index label if the passed one
        is not in the index.

        .. note:: This API is dependent on :meth:`Index.is_monotonic_increasing`
            which can be expensive.

        Parameters
        ----------
        label : object
            The label up to which the method returns the latest index label.

        Returns
        -------
        object
            The passed label if it is in the index. The previous label if the
            passed label is not in the sorted index or `NaN` if there is no
            such label.

        Examples
        --------
        `Index.asof` returns the latest index label up to the passed label.

        >>> idx = ps.Index(['2013-12-31', '2014-01-02', '2014-01-03'])
        >>> idx.asof('2014-01-01')
        '2013-12-31'

        If the label is in the index, the method returns the passed label.

        >>> idx.asof('2014-01-02')
        '2014-01-02'

        If all of the labels in the index are later than the passed label,
        NaN is returned.

        >>> idx.asof('1999-01-02')
        nan
        """
    def union(self, other: DataFrame | Series | Index | List, sort: bool | None = None) -> Index:
        '''
        Form the union of two Index objects.

        Parameters
        ----------
        other : Index or array-like
        sort : bool or None, default None
            Whether to sort the resulting Index.

        Returns
        -------
        union : Index

        Examples
        --------

        Index

        >>> idx1 = ps.Index([1, 2, 3, 4])
        >>> idx2 = ps.Index([3, 4, 5, 6])
        >>> idx1.union(idx2).sort_values()
        Int64Index([1, 2, 3, 4, 5, 6], dtype=\'int64\')

        MultiIndex

        >>> midx1 = ps.MultiIndex.from_tuples([("x", "a"), ("x", "b"), ("x", "c"), ("x", "d")])
        >>> midx2 = ps.MultiIndex.from_tuples([("x", "c"), ("x", "d"), ("x", "e"), ("x", "f")])
        >>> midx1.union(midx2).sort_values()  # doctest: +SKIP
        MultiIndex([(\'x\', \'a\'),
                    (\'x\', \'b\'),
                    (\'x\', \'c\'),
                    (\'x\', \'d\'),
                    (\'x\', \'e\'),
                    (\'x\', \'f\')],
                   )
        '''
    def holds_integer(self) -> bool:
        '''
        Whether the type is an integer type.
        Always return False for MultiIndex.

        Notes
        -----
        When Index contains null values the result can be different with pandas
        since pandas-on-Spark cast integer to float when Index contains null values.

        >>> ps.Index([1, 2, 3, None])
        Float64Index([1.0, 2.0, 3.0, nan], dtype=\'float64\')

        Examples
        --------
        >>> psidx = ps.Index([1, 2, 3, 4])
        >>> psidx.holds_integer()
        True

        Returns False for string type.

        >>> psidx = ps.Index(["A", "B", "C", "D"])
        >>> psidx.holds_integer()
        False

        Returns False for float type.

        >>> psidx = ps.Index([1.1, 2.2, 3.3, 4.4])
        >>> psidx.holds_integer()
        False
        '''
    def intersection(self, other: DataFrame | Series | Index | List) -> Index:
        """
        Form the intersection of two Index objects.

        This returns a new Index with elements common to the index and `other`.

        Parameters
        ----------
        other : Index or array-like

        Returns
        -------
        intersection : Index

        Examples
        --------
        >>> idx1 = ps.Index([1, 2, 3, 4])
        >>> idx2 = ps.Index([3, 4, 5, 6])
        >>> idx1.intersection(idx2).sort_values()
        Int64Index([3, 4], dtype='int64')
        """
    def item(self) -> Scalar | Tuple[Scalar, ...]:
        """
        Return the first element of the underlying data as a python scalar.

        Returns
        -------
        scalar
            The first element of Index.

        Raises
        ------
        ValueError
            If the data is not length-1.

        Examples
        --------
        >>> psidx = ps.Index([10])
        >>> psidx.item()
        10
        """
    def insert(self, loc: int, item: Any) -> Index:
        """
        Make new Index inserting new item at location.

        Follows Python list.append semantics for negative values.

        .. versionchanged:: 3.4.0
           Raise IndexError when loc is out of bounds to follow Pandas 1.4+ behavior

        Parameters
        ----------
        loc : int
        item : object

        Returns
        -------
        new_index : Index

        Examples
        --------
        >>> psidx = ps.Index([1, 2, 3, 4, 5])
        >>> psidx.insert(3, 100)
        Int64Index([1, 2, 3, 100, 4, 5], dtype='int64')

        For negative values

        >>> psidx = ps.Index([1, 2, 3, 4, 5])
        >>> psidx.insert(-3, 100)
        Int64Index([1, 2, 100, 3, 4, 5], dtype='int64')
        """
    def view(self) -> Index:
        """
        this is defined as a copy with the same identity
        """
    def to_list(self) -> List:
        """
        Return a list of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)

        .. note:: This method should only be used if the resulting list is expected
            to be small, as all the data is loaded into the driver's memory.

        Examples
        --------
        Index

        >>> idx = ps.Index([1, 2, 3, 4, 5])
        >>> idx.to_list()
        [1, 2, 3, 4, 5]

        MultiIndex

        >>> tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
        >>> midx = ps.MultiIndex.from_tuples(tuples)
        >>> midx.to_list()
        [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
        """
    tolist = to_list
    @property
    def inferred_type(self) -> str:
        """
        Return a string of the type inferred from the values.

        Examples
        --------
        >>> from datetime import datetime
        >>> ps.Index([1, 2, 3]).inferred_type
        'integer'

        >>> ps.Index([1.0, 2.0, 3.0]).inferred_type
        'floating'

        >>> ps.Index(['a', 'b', 'c']).inferred_type
        'string'

        >>> ps.Index([True, False, True, False]).inferred_type
        'boolean'
        """
    def __getattr__(self, item: str) -> Any: ...
    def __iter__(self) -> Iterator: ...
    def __and__(self, other: Index) -> Index: ...
    def __or__(self, other: Index) -> Index: ...
    def __xor__(self, other: Index) -> Index: ...
    def __rxor__(self, other: Any) -> Index: ...
    def __bool__(self) -> bool: ...
