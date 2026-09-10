import datetime
import numpy as np
from _typeshed import Incomplete
from pandas._config import get_option as get_option, using_copy_on_write as using_copy_on_write
from pandas._libs import lib as lib, properties as properties
from pandas._libs.hashtable import duplicated as duplicated
from pandas._libs.lib import NoDefault as NoDefault, is_range_indexer as is_range_indexer, no_default as no_default
from pandas._typing import AggFuncType as AggFuncType, AlignJoin as AlignJoin, AnyAll as AnyAll, AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, Axes as Axes, Axis as Axis, AxisInt as AxisInt, ColspaceArgType as ColspaceArgType, CompressionOptions as CompressionOptions, CorrelationMethod as CorrelationMethod, DropKeep as DropKeep, Dtype as Dtype, DtypeObj as DtypeObj, FilePath as FilePath, FillnaOptions as FillnaOptions, FloatFormatType as FloatFormatType, FormattersType as FormattersType, Frequency as Frequency, IgnoreRaise as IgnoreRaise, IndexKeyFunc as IndexKeyFunc, IndexLabel as IndexLabel, Level as Level, MergeHow as MergeHow, NaPosition as NaPosition, PythonFuncType as PythonFuncType, QuantileInterpolation as QuantileInterpolation, ReadBuffer as ReadBuffer, Renamer as Renamer, Scalar as Scalar, SortKind as SortKind, StorageOptions as StorageOptions, Suffixes as Suffixes, TimedeltaConvertibleTypes as TimedeltaConvertibleTypes, TimestampConvertibleTypes as TimestampConvertibleTypes, ValueKeyFunc as ValueKeyFunc, WriteBuffer as WriteBuffer, npt as npt
from pandas.compat import PYPY as PYPY
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.compat.numpy import np_percentile_argname as np_percentile_argname
from pandas.core import algorithms as algorithms, nanops as nanops, ops as ops
from pandas.core.accessor import CachedAccessor as CachedAccessor
from pandas.core.apply import reconstruct_func as reconstruct_func, relabel_result as relabel_result
from pandas.core.array_algos.take import take_2d_multi as take_2d_multi
from pandas.core.arraylike import OpsMixin as OpsMixin
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.arrow import ArrowDtype as ArrowDtype
from pandas.core.arrays.sparse import SparseFrameAccessor as SparseFrameAccessor
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array, sanitize_array as sanitize_array, sanitize_masked_array as sanitize_masked_array
from pandas.core.dtypes.cast import LossySetitemError as LossySetitemError, can_hold_element as can_hold_element, construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, construct_2d_arraylike_from_scalar as construct_2d_arraylike_from_scalar, find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar, invalidate_string_dtypes as invalidate_string_dtypes, maybe_box_native as maybe_box_native, maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import infer_dtype_from_object as infer_dtype_from_object, is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_bool_dtype as is_bool_dtype, is_dataclass as is_dataclass, is_dict_like as is_dict_like, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float as is_float, is_float_dtype as is_float_dtype, is_hashable as is_hashable, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_iterator as is_iterator, is_list_like as is_list_like, is_scalar as is_scalar, is_sequence as is_sequence, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import DataFrameGroupBy as DataFrameGroupBy
from pandas.core.indexers import check_key_length as check_key_length
from pandas.core.indexes.api import DatetimeIndex as DatetimeIndex, Index as Index, PeriodIndex as PeriodIndex, default_index as default_index, ensure_index as ensure_index, ensure_index_from_sequences as ensure_index_from_sequences
from pandas.core.indexes.multi import MultiIndex as MultiIndex, maybe_droplevels as maybe_droplevels
from pandas.core.indexing import check_bool_indexer as check_bool_indexer, check_dict_or_set_indexers as check_dict_or_set_indexers
from pandas.core.interchange.dataframe_protocol import DataFrame as DataFrameXchg
from pandas.core.internals import ArrayManager as ArrayManager, BlockManager as BlockManager, SingleDataManager as SingleDataManager
from pandas.core.internals.construction import arrays_to_mgr as arrays_to_mgr, dataclasses_to_dicts as dataclasses_to_dicts, dict_to_mgr as dict_to_mgr, mgr_to_mgr as mgr_to_mgr, ndarray_to_mgr as ndarray_to_mgr, nested_data_to_arrays as nested_data_to_arrays, rec_array_to_mgr as rec_array_to_mgr, reorder_arrays as reorder_arrays, to_arrays as to_arrays, treat_as_nested as treat_as_nested
from pandas.core.methods import selectn as selectn
from pandas.core.resample import Resampler as Resampler
from pandas.core.reshape.melt import melt as melt
from pandas.core.series import Series as Series
from pandas.core.sorting import get_group_index as get_group_index, lexsort_indexer as lexsort_indexer, nargsort as nargsort
from pandas.errors import ChainedAssignmentError as ChainedAssignmentError, InvalidIndexError as InvalidIndexError
from pandas.io.common import get_handle as get_handle
from pandas.io.formats import console as console, format as fmt
from pandas.io.formats.info import DataFrameInfo as DataFrameInfo, INFO_DOCSTRING as INFO_DOCSTRING, frame_sub_kwargs as frame_sub_kwargs
from pandas.io.formats.style import Styler as Styler
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_ascending as validate_ascending, validate_bool_kwarg as validate_bool_kwarg, validate_percentile as validate_percentile
from typing import Any, Callable, Hashable, Iterable, Literal, Mapping, Sequence, overload

class DataFrame(NDFrame, OpsMixin):
    '''
    Two-dimensional, size-mutable, potentially heterogeneous tabular data.

    Data structure also contains labeled axes (rows and columns).
    Arithmetic operations align on both row and column labels. Can be
    thought of as a dict-like container for Series objects. The primary
    pandas data structure.

    Parameters
    ----------
    data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If
        data is a dict, column order follows insertion-order. If a dict contains Series
        which have an index defined, it is aligned by its index. This alignment also
        occurs if data is a Series or a DataFrame itself. Alignment is done on
        Series/DataFrame inputs.

        If data is a list of dicts, column order follows insertion-order.

    index : Index or array-like
        Index to use for resulting frame. Will default to RangeIndex if
        no indexing information part of input data and no index provided.
    columns : Index or array-like
        Column labels to use for resulting frame when data does not have them,
        defaulting to RangeIndex(0, 1, 2, ..., n). If data contains column labels,
        will perform column selection instead.
    dtype : dtype, default None
        Data type to force. Only a single dtype is allowed. If None, infer.
    copy : bool or None, default None
        Copy data from inputs.
        For dict data, the default of None behaves like ``copy=True``.  For DataFrame
        or 2d ndarray input, the default of None behaves like ``copy=False``.
        If data is a dict containing one or more Series (possibly of different dtypes),
        ``copy=False`` will ensure that these inputs are not copied.

        .. versionchanged:: 1.3.0

    See Also
    --------
    DataFrame.from_records : Constructor from tuples, also record arrays.
    DataFrame.from_dict : From dicts of Series, arrays, or dicts.
    read_csv : Read a comma-separated values (csv) file into DataFrame.
    read_table : Read general delimited file into DataFrame.
    read_clipboard : Read text from clipboard into DataFrame.

    Notes
    -----
    Please reference the :ref:`User Guide <basics.dataframe>` for more information.

    Examples
    --------
    Constructing DataFrame from a dictionary.

    >>> d = {\'col1\': [1, 2], \'col2\': [3, 4]}
    >>> df = pd.DataFrame(data=d)
    >>> df
       col1  col2
    0     1     3
    1     2     4

    Notice that the inferred dtype is int64.

    >>> df.dtypes
    col1    int64
    col2    int64
    dtype: object

    To enforce a single dtype:

    >>> df = pd.DataFrame(data=d, dtype=np.int8)
    >>> df.dtypes
    col1    int8
    col2    int8
    dtype: object

    Constructing DataFrame from a dictionary including Series:

    >>> d = {\'col1\': [0, 1, 2, 3], \'col2\': pd.Series([2, 3], index=[2, 3])}
    >>> pd.DataFrame(data=d, index=[0, 1, 2, 3])
       col1  col2
    0     0   NaN
    1     1   NaN
    2     2   2.0
    3     3   3.0

    Constructing DataFrame from numpy ndarray:

    >>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ...                    columns=[\'a\', \'b\', \'c\'])
    >>> df2
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9

    Constructing DataFrame from a numpy ndarray that has labeled columns:

    >>> data = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)],
    ...                 dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])
    >>> df3 = pd.DataFrame(data, columns=[\'c\', \'a\'])
    ...
    >>> df3
       c  a
    0  3  1
    1  6  4
    2  9  7

    Constructing DataFrame from dataclass:

    >>> from dataclasses import make_dataclass
    >>> Point = make_dataclass("Point", [("x", int), ("y", int)])
    >>> pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
       x  y
    0  0  0
    1  0  3
    2  2  3

    Constructing DataFrame from Series/DataFrame:

    >>> ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
    >>> df = pd.DataFrame(data=ser, index=["a", "c"])
    >>> df
       0
    a  1
    c  3

    >>> df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])
    >>> df2 = pd.DataFrame(data=df1, index=["a", "c"])
    >>> df2
       x
    a  1
    c  3
    '''
    def __init__(self, data: Incomplete | None = None, index: Axes | None = None, columns: Axes | None = None, dtype: Dtype | None = None, copy: bool | None = None) -> None: ...
    def __dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True) -> DataFrameXchg:
        """
        Return the dataframe interchange object implementing the interchange protocol.

        Parameters
        ----------
        nan_as_null : bool, default False
            Whether to tell the DataFrame to overwrite null values in the data
            with ``NaN`` (or ``NaT``).
        allow_copy : bool, default True
            Whether to allow memory copying when exporting. If set to False
            it would cause non-zero-copy exports to fail.

        Returns
        -------
        DataFrame interchange object
            The object which consuming library can use to ingress the dataframe.

        Notes
        -----
        Details on the interchange protocol:
        https://data-apis.org/dataframe-protocol/latest/index.html

        `nan_as_null` currently has no effect; once support for nullable extension
        dtypes is added, this value should be propagated to columns.
        """
    @property
    def axes(self) -> list[Index]:
        """
        Return a list representing the axes of the DataFrame.

        It has the row axis labels and column axis labels as the only members.
        They are returned in that order.

        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.axes
        [RangeIndex(start=0, stop=2, step=1), Index(['col1', 'col2'],
        dtype='object')]
        """
    @property
    def shape(self) -> tuple[int, int]:
        """
        Return a tuple representing the dimensionality of the DataFrame.

        See Also
        --------
        ndarray.shape : Tuple of array dimensions.

        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.shape
        (2, 2)

        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4],
        ...                    'col3': [5, 6]})
        >>> df.shape
        (2, 3)
        """
    @overload
    def to_string(self, buf: None = ..., columns: Sequence[str] | None = ..., col_space: int | list[int] | dict[Hashable, int] | None = ..., header: bool | Sequence[str] = ..., index: bool = ..., na_rep: str = ..., formatters: fmt.FormattersType | None = ..., float_format: fmt.FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool = ..., decimal: str = ..., line_width: int | None = ..., min_rows: int | None = ..., max_colwidth: int | None = ..., encoding: str | None = ...) -> str: ...
    @overload
    def to_string(self, buf: FilePath | WriteBuffer[str], columns: Sequence[str] | None = ..., col_space: int | list[int] | dict[Hashable, int] | None = ..., header: bool | Sequence[str] = ..., index: bool = ..., na_rep: str = ..., formatters: fmt.FormattersType | None = ..., float_format: fmt.FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool = ..., decimal: str = ..., line_width: int | None = ..., min_rows: int | None = ..., max_colwidth: int | None = ..., encoding: str | None = ...) -> None: ...
    @property
    def style(self) -> Styler:
        """
        Returns a Styler object.

        Contains methods for building a styled HTML representation of the DataFrame.

        See Also
        --------
        io.formats.style.Styler : Helps style a DataFrame or Series according to the
            data with HTML and CSS.
        """
    def items(self) -> Iterable[tuple[Hashable, Series]]: ...
    def iterrows(self) -> Iterable[tuple[Hashable, Series]]:
        """
        Iterate over DataFrame rows as (index, Series) pairs.

        Yields
        ------
        index : label or tuple of label
            The index of the row. A tuple for a `MultiIndex`.
        data : Series
            The data of the row as a Series.

        See Also
        --------
        DataFrame.itertuples : Iterate over DataFrame rows as namedtuples of the values.
        DataFrame.items : Iterate over (column name, Series) pairs.

        Notes
        -----
        1. Because ``iterrows`` returns a Series for each row,
           it does **not** preserve dtypes across the rows (dtypes are
           preserved across columns for DataFrames). For example,

           >>> df = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
           >>> row = next(df.iterrows())[1]
           >>> row
           int      1.0
           float    1.5
           Name: 0, dtype: float64
           >>> print(row['int'].dtype)
           float64
           >>> print(df['int'].dtype)
           int64

           To preserve dtypes while iterating over the rows, it is better
           to use :meth:`itertuples` which returns namedtuples of the values
           and which is generally faster than ``iterrows``.

        2. You should **never modify** something you are iterating over.
           This is not guaranteed to work in all cases. Depending on the
           data types, the iterator returns a copy and not a view, and writing
           to it will have no effect.
        """
    def itertuples(self, index: bool = True, name: str | None = 'Pandas') -> Iterable[tuple[Any, ...]]:
        '''
        Iterate over DataFrame rows as namedtuples.

        Parameters
        ----------
        index : bool, default True
            If True, return the index as the first element of the tuple.
        name : str or None, default "Pandas"
            The name of the returned namedtuples or None to return regular
            tuples.

        Returns
        -------
        iterator
            An object to iterate over namedtuples for each row in the
            DataFrame with the first field possibly being the index and
            following fields being the column values.

        See Also
        --------
        DataFrame.iterrows : Iterate over DataFrame rows as (index, Series)
            pairs.
        DataFrame.items : Iterate over (column name, Series) pairs.

        Notes
        -----
        The column names will be renamed to positional names if they are
        invalid Python identifiers, repeated, or start with an underscore.

        Examples
        --------
        >>> df = pd.DataFrame({\'num_legs\': [4, 2], \'num_wings\': [0, 2]},
        ...                   index=[\'dog\', \'hawk\'])
        >>> df
              num_legs  num_wings
        dog          4          0
        hawk         2          2
        >>> for row in df.itertuples():
        ...     print(row)
        ...
        Pandas(Index=\'dog\', num_legs=4, num_wings=0)
        Pandas(Index=\'hawk\', num_legs=2, num_wings=2)

        By setting the `index` parameter to False we can remove the index
        as the first element of the tuple:

        >>> for row in df.itertuples(index=False):
        ...     print(row)
        ...
        Pandas(num_legs=4, num_wings=0)
        Pandas(num_legs=2, num_wings=2)

        With the `name` parameter set we set a custom name for the yielded
        namedtuples:

        >>> for row in df.itertuples(name=\'Animal\'):
        ...     print(row)
        ...
        Animal(Index=\'dog\', num_legs=4, num_wings=0)
        Animal(Index=\'hawk\', num_legs=2, num_wings=2)
        '''
    def __len__(self) -> int:
        """
        Returns length of info axis, but here we use the index.
        """
    @overload
    def dot(self, other: Series) -> Series: ...
    @overload
    def dot(self, other: DataFrame | Index | ArrayLike) -> DataFrame: ...
    @overload
    def __matmul__(self, other: Series) -> Series: ...
    @overload
    def __matmul__(self, other: AnyArrayLike | DataFrame) -> DataFrame | Series: ...
    def __rmatmul__(self, other) -> DataFrame:
        """
        Matrix multiplication using binary `@` operator in Python>=3.5.
        """
    @classmethod
    def from_dict(cls, data: dict, orient: str = 'columns', dtype: Dtype | None = None, columns: Axes | None = None) -> DataFrame:
        '''
        Construct DataFrame from dict of array-like or dicts.

        Creates DataFrame object from dictionary by columns or by index
        allowing dtype specification.

        Parameters
        ----------
        data : dict
            Of the form {field : array-like} or {field : dict}.
        orient : {\'columns\', \'index\', \'tight\'}, default \'columns\'
            The "orientation" of the data. If the keys of the passed dict
            should be the columns of the resulting DataFrame, pass \'columns\'
            (default). Otherwise if the keys should be rows, pass \'index\'.
            If \'tight\', assume a dict with keys [\'index\', \'columns\', \'data\',
            \'index_names\', \'column_names\'].

            .. versionadded:: 1.4.0
               \'tight\' as an allowed value for the ``orient`` argument

        dtype : dtype, default None
            Data type to force after DataFrame construction, otherwise infer.
        columns : list, default None
            Column labels to use when ``orient=\'index\'``. Raises a ValueError
            if used with ``orient=\'columns\'`` or ``orient=\'tight\'``.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.from_records : DataFrame from structured ndarray, sequence
            of tuples or dicts, or DataFrame.
        DataFrame : DataFrame object creation using constructor.
        DataFrame.to_dict : Convert the DataFrame to a dictionary.

        Examples
        --------
        By default the keys of the dict become the DataFrame columns:

        >>> data = {\'col_1\': [3, 2, 1, 0], \'col_2\': [\'a\', \'b\', \'c\', \'d\']}
        >>> pd.DataFrame.from_dict(data)
           col_1 col_2
        0      3     a
        1      2     b
        2      1     c
        3      0     d

        Specify ``orient=\'index\'`` to create the DataFrame using dictionary
        keys as rows:

        >>> data = {\'row_1\': [3, 2, 1, 0], \'row_2\': [\'a\', \'b\', \'c\', \'d\']}
        >>> pd.DataFrame.from_dict(data, orient=\'index\')
               0  1  2  3
        row_1  3  2  1  0
        row_2  a  b  c  d

        When using the \'index\' orientation, the column names can be
        specified manually:

        >>> pd.DataFrame.from_dict(data, orient=\'index\',
        ...                        columns=[\'A\', \'B\', \'C\', \'D\'])
               A  B  C  D
        row_1  3  2  1  0
        row_2  a  b  c  d

        Specify ``orient=\'tight\'`` to create the DataFrame using a \'tight\'
        format:

        >>> data = {\'index\': [(\'a\', \'b\'), (\'a\', \'c\')],
        ...         \'columns\': [(\'x\', 1), (\'y\', 2)],
        ...         \'data\': [[1, 3], [2, 4]],
        ...         \'index_names\': [\'n1\', \'n2\'],
        ...         \'column_names\': [\'z1\', \'z2\']}
        >>> pd.DataFrame.from_dict(data, orient=\'tight\')
        z1     x  y
        z2     1  2
        n1 n2
        a  b   1  3
           c   2  4
        '''
    def to_numpy(self, dtype: npt.DTypeLike | None = None, copy: bool = False, na_value: object = ...) -> np.ndarray:
        '''
        Convert the DataFrame to a NumPy array.

        By default, the dtype of the returned array will be the common NumPy
        dtype of all types in the DataFrame. For example, if the dtypes are
        ``float16`` and ``float32``, the results dtype will be ``float32``.
        This may require copying data and coercing values, which may be
        expensive.

        Parameters
        ----------
        dtype : str or numpy.dtype, optional
            The dtype to pass to :meth:`numpy.asarray`.
        copy : bool, default False
            Whether to ensure that the returned value is not a view on
            another array. Note that ``copy=False`` does not *ensure* that
            ``to_numpy()`` is no-copy. Rather, ``copy=True`` ensure that
            a copy is made, even if not strictly necessary.
        na_value : Any, optional
            The value to use for missing values. The default value depends
            on `dtype` and the dtypes of the DataFrame columns.

            .. versionadded:: 1.1.0

        Returns
        -------
        numpy.ndarray

        See Also
        --------
        Series.to_numpy : Similar method for Series.

        Examples
        --------
        >>> pd.DataFrame({"A": [1, 2], "B": [3, 4]}).to_numpy()
        array([[1, 3],
               [2, 4]])

        With heterogeneous data, the lowest common type will have to
        be used.

        >>> df = pd.DataFrame({"A": [1, 2], "B": [3.0, 4.5]})
        >>> df.to_numpy()
        array([[1. , 3. ],
               [2. , 4.5]])

        For a mix of numeric and non-numeric types, the output array will
        have object dtype.

        >>> df[\'C\'] = pd.date_range(\'2000\', periods=2)
        >>> df.to_numpy()
        array([[1, 3.0, Timestamp(\'2000-01-01 00:00:00\')],
               [2, 4.5, Timestamp(\'2000-01-02 00:00:00\')]], dtype=object)
        '''
    @overload
    def to_dict(self, orient: Literal['dict', 'list', 'series', 'split', 'tight', 'index'] = ..., into: type[dict] = ...) -> dict: ...
    @overload
    def to_dict(self, orient: Literal['records'], into: type[dict] = ...) -> list[dict]: ...
    def to_gbq(self, destination_table: str, project_id: str | None = None, chunksize: int | None = None, reauth: bool = False, if_exists: str = 'fail', auth_local_webserver: bool = True, table_schema: list[dict[str, str]] | None = None, location: str | None = None, progress_bar: bool = True, credentials: Incomplete | None = None) -> None:
        '''
        Write a DataFrame to a Google BigQuery table.

        This function requires the `pandas-gbq package
        <https://pandas-gbq.readthedocs.io>`__.

        See the `How to authenticate with Google BigQuery
        <https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html>`__
        guide for authentication instructions.

        Parameters
        ----------
        destination_table : str
            Name of table to be written, in the form ``dataset.tablename``.
        project_id : str, optional
            Google BigQuery Account project ID. Optional when available from
            the environment.
        chunksize : int, optional
            Number of rows to be inserted in each chunk from the dataframe.
            Set to ``None`` to load the whole dataframe at once.
        reauth : bool, default False
            Force Google BigQuery to re-authenticate the user. This is useful
            if multiple accounts are used.
        if_exists : str, default \'fail\'
            Behavior when the destination table exists. Value can be one of:

            ``\'fail\'``
                If table exists raise pandas_gbq.gbq.TableCreationError.
            ``\'replace\'``
                If table exists, drop it, recreate it, and insert data.
            ``\'append\'``
                If table exists, insert data. Create if does not exist.
        auth_local_webserver : bool, default True
            Use the `local webserver flow`_ instead of the `console flow`_
            when getting user credentials.

            .. _local webserver flow:
                https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_local_server
            .. _console flow:
                https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_console

            *New in version 0.2.0 of pandas-gbq*.

            .. versionchanged:: 1.5.0
               Default value is changed to ``True``. Google has deprecated the
               ``auth_local_webserver = False`` `"out of band" (copy-paste)
               flow
               <https://developers.googleblog.com/2022/02/making-oauth-flows-safer.html?m=1#disallowed-oob>`_.
        table_schema : list of dicts, optional
            List of BigQuery table fields to which according DataFrame
            columns conform to, e.g. ``[{\'name\': \'col1\', \'type\':
            \'STRING\'},...]``. If schema is not provided, it will be
            generated according to dtypes of DataFrame columns. See
            BigQuery API documentation on available names of a field.

            *New in version 0.3.1 of pandas-gbq*.
        location : str, optional
            Location where the load job should run. See the `BigQuery locations
            documentation
            <https://cloud.google.com/bigquery/docs/dataset-locations>`__ for a
            list of available locations. The location must match that of the
            target dataset.

            *New in version 0.5.0 of pandas-gbq*.
        progress_bar : bool, default True
            Use the library `tqdm` to show the progress bar for the upload,
            chunk by chunk.

            *New in version 0.5.0 of pandas-gbq*.
        credentials : google.auth.credentials.Credentials, optional
            Credentials for accessing Google APIs. Use this parameter to
            override default credentials, such as to use Compute Engine
            :class:`google.auth.compute_engine.Credentials` or Service
            Account :class:`google.oauth2.service_account.Credentials`
            directly.

            *New in version 0.8.0 of pandas-gbq*.

        See Also
        --------
        pandas_gbq.to_gbq : This function in the pandas-gbq library.
        read_gbq : Read a DataFrame from Google BigQuery.
        '''
    @classmethod
    def from_records(cls, data, index: Incomplete | None = None, exclude: Incomplete | None = None, columns: Incomplete | None = None, coerce_float: bool = False, nrows: int | None = None) -> DataFrame:
        """
        Convert structured or record ndarray to DataFrame.

        Creates a DataFrame object from a structured ndarray, sequence of
        tuples or dicts, or DataFrame.

        Parameters
        ----------
        data : structured ndarray, sequence of tuples or dicts, or DataFrame
            Structured input data.
        index : str, list of fields, array-like
            Field of array to use as the index, alternately a specific set of
            input labels to use.
        exclude : sequence, default None
            Columns or fields to exclude.
        columns : sequence, default None
            Column names to use. If the passed data do not have names
            associated with them, this argument provides names for the
            columns. Otherwise this argument indicates the order of the columns
            in the result (any names not found in the data will become all-NA
            columns).
        coerce_float : bool, default False
            Attempt to convert values of non-string, non-numeric objects (like
            decimal.Decimal) to floating point, useful for SQL result sets.
        nrows : int, default None
            Number of rows to read if data is an iterator.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.from_dict : DataFrame from dict of array-like or dicts.
        DataFrame : DataFrame object creation using constructor.

        Examples
        --------
        Data can be provided as a structured ndarray:

        >>> data = np.array([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd')],
        ...                 dtype=[('col_1', 'i4'), ('col_2', 'U1')])
        >>> pd.DataFrame.from_records(data)
           col_1 col_2
        0      3     a
        1      2     b
        2      1     c
        3      0     d

        Data can be provided as a list of dicts:

        >>> data = [{'col_1': 3, 'col_2': 'a'},
        ...         {'col_1': 2, 'col_2': 'b'},
        ...         {'col_1': 1, 'col_2': 'c'},
        ...         {'col_1': 0, 'col_2': 'd'}]
        >>> pd.DataFrame.from_records(data)
           col_1 col_2
        0      3     a
        1      2     b
        2      1     c
        3      0     d

        Data can be provided as a list of tuples with corresponding columns:

        >>> data = [(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd')]
        >>> pd.DataFrame.from_records(data, columns=['col_1', 'col_2'])
           col_1 col_2
        0      3     a
        1      2     b
        2      1     c
        3      0     d
        """
    def to_records(self, index: bool = True, column_dtypes: Incomplete | None = None, index_dtypes: Incomplete | None = None) -> np.recarray:
        '''
        Convert DataFrame to a NumPy record array.

        Index will be included as the first field of the record array if
        requested.

        Parameters
        ----------
        index : bool, default True
            Include index in resulting record array, stored in \'index\'
            field or using the index label, if set.
        column_dtypes : str, type, dict, default None
            If a string or type, the data type to store all columns. If
            a dictionary, a mapping of column names and indices (zero-indexed)
            to specific data types.
        index_dtypes : str, type, dict, default None
            If a string or type, the data type to store all index levels. If
            a dictionary, a mapping of index level names and indices
            (zero-indexed) to specific data types.

            This mapping is applied only if `index=True`.

        Returns
        -------
        numpy.recarray
            NumPy ndarray with the DataFrame labels as fields and each row
            of the DataFrame as entries.

        See Also
        --------
        DataFrame.from_records: Convert structured or record ndarray
            to DataFrame.
        numpy.recarray: An ndarray that allows field access using
            attributes, analogous to typed columns in a
            spreadsheet.

        Examples
        --------
        >>> df = pd.DataFrame({\'A\': [1, 2], \'B\': [0.5, 0.75]},
        ...                   index=[\'a\', \'b\'])
        >>> df
           A     B
        a  1  0.50
        b  2  0.75
        >>> df.to_records()
        rec.array([(\'a\', 1, 0.5 ), (\'b\', 2, 0.75)],
                  dtype=[(\'index\', \'O\'), (\'A\', \'<i8\'), (\'B\', \'<f8\')])

        If the DataFrame index has no label then the recarray field name
        is set to \'index\'. If the index has a label then this is used as the
        field name:

        >>> df.index = df.index.rename("I")
        >>> df.to_records()
        rec.array([(\'a\', 1, 0.5 ), (\'b\', 2, 0.75)],
                  dtype=[(\'I\', \'O\'), (\'A\', \'<i8\'), (\'B\', \'<f8\')])

        The index can be excluded from the record array:

        >>> df.to_records(index=False)
        rec.array([(1, 0.5 ), (2, 0.75)],
                  dtype=[(\'A\', \'<i8\'), (\'B\', \'<f8\')])

        Data types can be specified for the columns:

        >>> df.to_records(column_dtypes={"A": "int32"})
        rec.array([(\'a\', 1, 0.5 ), (\'b\', 2, 0.75)],
                  dtype=[(\'I\', \'O\'), (\'A\', \'<i4\'), (\'B\', \'<f8\')])

        As well as for the index:

        >>> df.to_records(index_dtypes="<S2")
        rec.array([(b\'a\', 1, 0.5 ), (b\'b\', 2, 0.75)],
                  dtype=[(\'I\', \'S2\'), (\'A\', \'<i8\'), (\'B\', \'<f8\')])

        >>> index_dtypes = f"<S{df.index.str.len().max()}"
        >>> df.to_records(index_dtypes=index_dtypes)
        rec.array([(b\'a\', 1, 0.5 ), (b\'b\', 2, 0.75)],
                  dtype=[(\'I\', \'S1\'), (\'A\', \'<i8\'), (\'B\', \'<f8\')])
        '''
    def to_stata(self, path: FilePath | WriteBuffer[bytes], *, convert_dates: dict[Hashable, str] | None = None, write_index: bool = True, byteorder: str | None = None, time_stamp: datetime.datetime | None = None, data_label: str | None = None, variable_labels: dict[Hashable, str] | None = None, version: int | None = 114, convert_strl: Sequence[Hashable] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions = None, value_labels: dict[Hashable, dict[float, str]] | None = None) -> None:
        '''
        Export DataFrame object to Stata dta format.

        Writes the DataFrame to a Stata dataset file.
        "dta" files contain a Stata dataset.

        Parameters
        ----------
        path : str, path object, or buffer
            String, path object (implementing ``os.PathLike[str]``), or file-like
            object implementing a binary ``write()`` function.

        convert_dates : dict
            Dictionary mapping columns containing datetime types to stata
            internal format to use when writing the dates. Options are \'tc\',
            \'td\', \'tm\', \'tw\', \'th\', \'tq\', \'ty\'. Column can be either an integer
            or a name. Datetime columns that do not have a conversion type
            specified will be converted to \'tc\'. Raises NotImplementedError if
            a datetime column has timezone information.
        write_index : bool
            Write the index to Stata dataset.
        byteorder : str
            Can be ">", "<", "little", or "big". default is `sys.byteorder`.
        time_stamp : datetime
            A datetime to use as file creation date.  Default is the current
            time.
        data_label : str, optional
            A label for the data set.  Must be 80 characters or smaller.
        variable_labels : dict
            Dictionary containing columns as keys and variable labels as
            values. Each label must be 80 characters or smaller.
        version : {{114, 117, 118, 119, None}}, default 114
            Version to use in the output dta file. Set to None to let pandas
            decide between 118 or 119 formats depending on the number of
            columns in the frame. Version 114 can be read by Stata 10 and
            later. Version 117 can be read by Stata 13 or later. Version 118
            is supported in Stata 14 and later. Version 119 is supported in
            Stata 15 and later. Version 114 limits string variables to 244
            characters or fewer while versions 117 and later allow strings
            with lengths up to 2,000,000 characters. Versions 118 and 119
            support Unicode characters, and version 119 supports more than
            32,767 variables.

            Version 119 should usually only be used when the number of
            variables exceeds the capacity of dta format 118. Exporting
            smaller datasets in format 119 may have unintended consequences,
            and, as of November 2020, Stata SE cannot read version 119 files.

        convert_strl : list, optional
            List of column names to convert to string columns to Stata StrL
            format. Only available if version is 117.  Storing strings in the
            StrL format can produce smaller dta files if strings have more than
            8 characters and values are repeated.
        {compression_options}

            .. versionadded:: 1.1.0

            .. versionchanged:: 1.4.0 Zstandard support.

        {storage_options}

            .. versionadded:: 1.2.0

        value_labels : dict of dicts
            Dictionary containing columns as keys and dictionaries of column value
            to labels as values. Labels for a single variable must be 32,000
            characters or smaller.

            .. versionadded:: 1.4.0

        Raises
        ------
        NotImplementedError
            * If datetimes contain timezone information
            * Column dtype is not representable in Stata
        ValueError
            * Columns listed in convert_dates are neither datetime64[ns]
              or datetime.datetime
            * Column listed in convert_dates is not in DataFrame
            * Categorical label contains more than 32,000 characters

        See Also
        --------
        read_stata : Import Stata data files.
        io.stata.StataWriter : Low-level writer for Stata data files.
        io.stata.StataWriter117 : Low-level writer for version 117 files.

        Examples
        --------
        >>> df = pd.DataFrame({{\'animal\': [\'falcon\', \'parrot\', \'falcon\',
        ...                               \'parrot\'],
        ...                    \'speed\': [350, 18, 361, 15]}})
        >>> df.to_stata(\'animals.dta\')  # doctest: +SKIP
        '''
    def to_feather(self, path: FilePath | WriteBuffer[bytes], **kwargs) -> None:
        """
        Write a DataFrame to the binary Feather format.

        Parameters
        ----------
        path : str, path object, file-like object
            String, path object (implementing ``os.PathLike[str]``), or file-like
            object implementing a binary ``write()`` function. If a string or a path,
            it will be used as Root Directory path when writing a partitioned dataset.
        **kwargs :
            Additional keywords passed to :func:`pyarrow.feather.write_feather`.
            Starting with pyarrow 0.17, this includes the `compression`,
            `compression_level`, `chunksize` and `version` keywords.

            .. versionadded:: 1.1.0

        Notes
        -----
        This function writes the dataframe as a `feather file
        <https://arrow.apache.org/docs/python/feather.html>`_. Requires a default
        index. For saving the DataFrame with your custom index use a method that
        supports custom indices e.g. `to_parquet`.
        """
    def to_markdown(self, buf: FilePath | WriteBuffer[str] | None = None, mode: str = 'wt', index: bool = True, storage_options: StorageOptions = None, **kwargs) -> str | None: ...
    @overload
    def to_parquet(self, path: None = ..., engine: str = ..., compression: str | None = ..., index: bool | None = ..., partition_cols: list[str] | None = ..., storage_options: StorageOptions = ..., **kwargs) -> bytes: ...
    @overload
    def to_parquet(self, path: FilePath | WriteBuffer[bytes], engine: str = ..., compression: str | None = ..., index: bool | None = ..., partition_cols: list[str] | None = ..., storage_options: StorageOptions = ..., **kwargs) -> None: ...
    def to_orc(self, path: FilePath | WriteBuffer[bytes] | None = None, *, engine: Literal['pyarrow'] = 'pyarrow', index: bool | None = None, engine_kwargs: dict[str, Any] | None = None) -> bytes | None:
        """
        Write a DataFrame to the ORC format.

        .. versionadded:: 1.5.0

        Parameters
        ----------
        path : str, file-like object or None, default None
            If a string, it will be used as Root Directory path
            when writing a partitioned dataset. By file-like object,
            we refer to objects with a write() method, such as a file handle
            (e.g. via builtin open function). If path is None,
            a bytes object is returned.
        engine : str, default 'pyarrow'
            ORC library to use. Pyarrow must be >= 7.0.0.
        index : bool, optional
            If ``True``, include the dataframe's index(es) in the file output.
            If ``False``, they will not be written to the file.
            If ``None``, similar to ``infer`` the dataframe's index(es)
            will be saved. However, instead of being saved as values,
            the RangeIndex will be stored as a range in the metadata so it
            doesn't require much space and is faster. Other indexes will
            be included as columns in the file output.
        engine_kwargs : dict[str, Any] or None, default None
            Additional keyword arguments passed to :func:`pyarrow.orc.write_table`.

        Returns
        -------
        bytes if no path argument is provided else None

        Raises
        ------
        NotImplementedError
            Dtype of one or more columns is category, unsigned integers, interval,
            period or sparse.
        ValueError
            engine is not pyarrow.

        See Also
        --------
        read_orc : Read a ORC file.
        DataFrame.to_parquet : Write a parquet file.
        DataFrame.to_csv : Write a csv file.
        DataFrame.to_sql : Write to a sql table.
        DataFrame.to_hdf : Write to hdf.

        Notes
        -----
        * Before using this function you should read the :ref:`user guide about
          ORC <io.orc>` and :ref:`install optional dependencies <install.warn_orc>`.
        * This function requires `pyarrow <https://arrow.apache.org/docs/python/>`_
          library.
        * For supported dtypes please refer to `supported ORC features in Arrow
          <https://arrow.apache.org/docs/cpp/orc.html#data-types>`__.
        * Currently timezones in datetime columns are not preserved when a
          dataframe is converted into ORC files.

        Examples
        --------
        >>> df = pd.DataFrame(data={'col1': [1, 2], 'col2': [4, 3]})
        >>> df.to_orc('df.orc')  # doctest: +SKIP
        >>> pd.read_orc('df.orc')  # doctest: +SKIP
           col1  col2
        0     1     4
        1     2     3

        If you want to get a buffer to the orc content you can write it to io.BytesIO
        >>> import io
        >>> b = io.BytesIO(df.to_orc())  # doctest: +SKIP
        >>> b.seek(0)  # doctest: +SKIP
        0
        >>> content = b.read()  # doctest: +SKIP
        """
    @overload
    def to_html(self, buf: FilePath | WriteBuffer[str], columns: Sequence[Level] | None = ..., col_space: ColspaceArgType | None = ..., header: bool | Sequence[str] = ..., index: bool = ..., na_rep: str = ..., formatters: FormattersType | None = ..., float_format: FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool | str = ..., decimal: str = ..., bold_rows: bool = ..., classes: str | list | tuple | None = ..., escape: bool = ..., notebook: bool = ..., border: int | bool | None = ..., table_id: str | None = ..., render_links: bool = ..., encoding: str | None = ...) -> None: ...
    @overload
    def to_html(self, buf: None = ..., columns: Sequence[Level] | None = ..., col_space: ColspaceArgType | None = ..., header: bool | Sequence[str] = ..., index: bool = ..., na_rep: str = ..., formatters: FormattersType | None = ..., float_format: FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool | str = ..., decimal: str = ..., bold_rows: bool = ..., classes: str | list | tuple | None = ..., escape: bool = ..., notebook: bool = ..., border: int | bool | None = ..., table_id: str | None = ..., render_links: bool = ..., encoding: str | None = ...) -> str: ...
    def to_xml(self, path_or_buffer: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None, index: bool = True, root_name: str | None = 'data', row_name: str | None = 'row', na_rep: str | None = None, attr_cols: list[str] | None = None, elem_cols: list[str] | None = None, namespaces: dict[str | None, str] | None = None, prefix: str | None = None, encoding: str = 'utf-8', xml_declaration: bool | None = True, pretty_print: bool | None = True, parser: str | None = 'lxml', stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions = None) -> str | None:
        '''
        Render a DataFrame to an XML document.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        path_or_buffer : str, path object, file-like object, or None, default None
            String, path object (implementing ``os.PathLike[str]``), or file-like
            object implementing a ``write()`` function. If None, the result is returned
            as a string.
        index : bool, default True
            Whether to include index in XML document.
        root_name : str, default \'data\'
            The name of root element in XML document.
        row_name : str, default \'row\'
            The name of row element in XML document.
        na_rep : str, optional
            Missing data representation.
        attr_cols : list-like, optional
            List of columns to write as attributes in row element.
            Hierarchical columns will be flattened with underscore
            delimiting the different levels.
        elem_cols : list-like, optional
            List of columns to write as children in row element. By default,
            all columns output as children of row element. Hierarchical
            columns will be flattened with underscore delimiting the
            different levels.
        namespaces : dict, optional
            All namespaces to be defined in root element. Keys of dict
            should be prefix names and values of dict corresponding URIs.
            Default namespaces should be given empty string key. For
            example, ::

                namespaces = {{"": "https://example.com"}}

        prefix : str, optional
            Namespace prefix to be used for every element and/or attribute
            in document. This should be one of the keys in ``namespaces``
            dict.
        encoding : str, default \'utf-8\'
            Encoding of the resulting document.
        xml_declaration : bool, default True
            Whether to include the XML declaration at start of document.
        pretty_print : bool, default True
            Whether output should be pretty printed with indentation and
            line breaks.
        parser : {{\'lxml\',\'etree\'}}, default \'lxml\'
            Parser module to use for building of tree. Only \'lxml\' and
            \'etree\' are supported. With \'lxml\', the ability to use XSLT
            stylesheet is supported.
        stylesheet : str, path object or file-like object, optional
            A URL, file-like object, or a raw string containing an XSLT
            script used to transform the raw XML output. Script should use
            layout of elements and attributes from original output. This
            argument requires ``lxml`` to be installed. Only XSLT 1.0
            scripts and not later versions is currently supported.
        {compression_options}

            .. versionchanged:: 1.4.0 Zstandard support.

        {storage_options}

        Returns
        -------
        None or str
            If ``io`` is None, returns the resulting XML format as a
            string. Otherwise returns None.

        See Also
        --------
        to_json : Convert the pandas object to a JSON string.
        to_html : Convert DataFrame to a html.

        Examples
        --------
        >>> df = pd.DataFrame({{\'shape\': [\'square\', \'circle\', \'triangle\'],
        ...                    \'degrees\': [360, 360, 180],
        ...                    \'sides\': [4, np.nan, 3]}})

        >>> df.to_xml()  # doctest: +SKIP
        <?xml version=\'1.0\' encoding=\'utf-8\'?>
        <data>
          <row>
            <index>0</index>
            <shape>square</shape>
            <degrees>360</degrees>
            <sides>4.0</sides>
          </row>
          <row>
            <index>1</index>
            <shape>circle</shape>
            <degrees>360</degrees>
            <sides/>
          </row>
          <row>
            <index>2</index>
            <shape>triangle</shape>
            <degrees>180</degrees>
            <sides>3.0</sides>
          </row>
        </data>

        >>> df.to_xml(attr_cols=[
        ...           \'index\', \'shape\', \'degrees\', \'sides\'
        ...           ])  # doctest: +SKIP
        <?xml version=\'1.0\' encoding=\'utf-8\'?>
        <data>
          <row index="0" shape="square" degrees="360" sides="4.0"/>
          <row index="1" shape="circle" degrees="360"/>
          <row index="2" shape="triangle" degrees="180" sides="3.0"/>
        </data>

        >>> df.to_xml(namespaces={{"doc": "https://example.com"}},
        ...           prefix="doc")  # doctest: +SKIP
        <?xml version=\'1.0\' encoding=\'utf-8\'?>
        <doc:data xmlns:doc="https://example.com">
          <doc:row>
            <doc:index>0</doc:index>
            <doc:shape>square</doc:shape>
            <doc:degrees>360</doc:degrees>
            <doc:sides>4.0</doc:sides>
          </doc:row>
          <doc:row>
            <doc:index>1</doc:index>
            <doc:shape>circle</doc:shape>
            <doc:degrees>360</doc:degrees>
            <doc:sides/>
          </doc:row>
          <doc:row>
            <doc:index>2</doc:index>
            <doc:shape>triangle</doc:shape>
            <doc:degrees>180</doc:degrees>
            <doc:sides>3.0</doc:sides>
          </doc:row>
        </doc:data>
        '''
    def info(self, verbose: bool | None = None, buf: WriteBuffer[str] | None = None, max_cols: int | None = None, memory_usage: bool | str | None = None, show_counts: bool | None = None) -> None: ...
    def memory_usage(self, index: bool = True, deep: bool = False) -> Series:
        """
        Return the memory usage of each column in bytes.

        The memory usage can optionally include the contribution of
        the index and elements of `object` dtype.

        This value is displayed in `DataFrame.info` by default. This can be
        suppressed by setting ``pandas.options.display.memory_usage`` to False.

        Parameters
        ----------
        index : bool, default True
            Specifies whether to include the memory usage of the DataFrame's
            index in returned Series. If ``index=True``, the memory usage of
            the index is the first item in the output.
        deep : bool, default False
            If True, introspect the data deeply by interrogating
            `object` dtypes for system-level memory consumption, and include
            it in the returned values.

        Returns
        -------
        Series
            A Series whose index is the original column names and whose values
            is the memory usage of each column in bytes.

        See Also
        --------
        numpy.ndarray.nbytes : Total bytes consumed by the elements of an
            ndarray.
        Series.memory_usage : Bytes consumed by a Series.
        Categorical : Memory-efficient array for string values with
            many repeated values.
        DataFrame.info : Concise summary of a DataFrame.

        Notes
        -----
        See the :ref:`Frequently Asked Questions <df-memory-usage>` for more
        details.

        Examples
        --------
        >>> dtypes = ['int64', 'float64', 'complex128', 'object', 'bool']
        >>> data = dict([(t, np.ones(shape=5000, dtype=int).astype(t))
        ...              for t in dtypes])
        >>> df = pd.DataFrame(data)
        >>> df.head()
           int64  float64            complex128  object  bool
        0      1      1.0              1.0+0.0j       1  True
        1      1      1.0              1.0+0.0j       1  True
        2      1      1.0              1.0+0.0j       1  True
        3      1      1.0              1.0+0.0j       1  True
        4      1      1.0              1.0+0.0j       1  True

        >>> df.memory_usage()
        Index           128
        int64         40000
        float64       40000
        complex128    80000
        object        40000
        bool           5000
        dtype: int64

        >>> df.memory_usage(index=False)
        int64         40000
        float64       40000
        complex128    80000
        object        40000
        bool           5000
        dtype: int64

        The memory footprint of `object` dtype columns is ignored by default:

        >>> df.memory_usage(deep=True)
        Index            128
        int64          40000
        float64        40000
        complex128     80000
        object        180000
        bool            5000
        dtype: int64

        Use a Categorical for efficient storage of an object-dtype column with
        many repeated values.

        >>> df['object'].astype('category').memory_usage(deep=True)
        5244
        """
    def transpose(self, *args, copy: bool = False) -> DataFrame:
        """
        Transpose index and columns.

        Reflect the DataFrame over its main diagonal by writing rows as columns
        and vice-versa. The property :attr:`.T` is an accessor to the method
        :meth:`transpose`.

        Parameters
        ----------
        *args : tuple, optional
            Accepted for compatibility with NumPy.
        copy : bool, default False
            Whether to copy the data after transposing, even for DataFrames
            with a single dtype.

            Note that a copy is always required for mixed dtype DataFrames,
            or for DataFrames with any extension types.

        Returns
        -------
        DataFrame
            The transposed DataFrame.

        See Also
        --------
        numpy.transpose : Permute the dimensions of a given array.

        Notes
        -----
        Transposing a DataFrame with mixed dtypes will result in a homogeneous
        DataFrame with the `object` dtype. In such a case, a copy of the data
        is always made.

        Examples
        --------
        **Square DataFrame with homogeneous dtype**

        >>> d1 = {'col1': [1, 2], 'col2': [3, 4]}
        >>> df1 = pd.DataFrame(data=d1)
        >>> df1
           col1  col2
        0     1     3
        1     2     4

        >>> df1_transposed = df1.T  # or df1.transpose()
        >>> df1_transposed
              0  1
        col1  1  2
        col2  3  4

        When the dtype is homogeneous in the original DataFrame, we get a
        transposed DataFrame with the same dtype:

        >>> df1.dtypes
        col1    int64
        col2    int64
        dtype: object
        >>> df1_transposed.dtypes
        0    int64
        1    int64
        dtype: object

        **Non-square DataFrame with mixed dtypes**

        >>> d2 = {'name': ['Alice', 'Bob'],
        ...       'score': [9.5, 8],
        ...       'employed': [False, True],
        ...       'kids': [0, 0]}
        >>> df2 = pd.DataFrame(data=d2)
        >>> df2
            name  score  employed  kids
        0  Alice    9.5     False     0
        1    Bob    8.0      True     0

        >>> df2_transposed = df2.T  # or df2.transpose()
        >>> df2_transposed
                      0     1
        name      Alice   Bob
        score       9.5   8.0
        employed  False  True
        kids          0     0

        When the DataFrame has mixed dtypes, we get a transposed DataFrame with
        the `object` dtype:

        >>> df2.dtypes
        name         object
        score       float64
        employed       bool
        kids          int64
        dtype: object
        >>> df2_transposed.dtypes
        0    object
        1    object
        dtype: object
        """
    @property
    def T(self) -> DataFrame:
        """
        The transpose of the DataFrame.

        Returns
        -------
        DataFrame
            The transposed DataFrame.

        See Also
        --------
        DataFrame.transpose : Transpose index and columns.

        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df
           col1  col2
        0     1     3
        1     2     4

        >>> df.T
              0  1
        col1  1  2
        col2  3  4
        """
    def __getitem__(self, key): ...
    def isetitem(self, loc, value) -> None:
        """
        Set the given value in the column with position `loc`.

        This is a positional analogue to ``__setitem__``.

        Parameters
        ----------
        loc : int or sequence of ints
            Index position for the column.
        value : scalar or arraylike
            Value(s) for the column.

        Notes
        -----
        ``frame.isetitem(loc, value)`` is an in-place method as it will
        modify the DataFrame in place (not returning a new object). In contrast to
        ``frame.iloc[:, i] = value`` which will try to update the existing values in
        place, ``frame.isetitem(loc, value)`` will not update the values of the column
        itself in place, it will instead insert a new array.

        In cases where ``frame.columns`` is unique, this is equivalent to
        ``frame[frame.columns[i]] = value``.
        """
    def __setitem__(self, key, value) -> None: ...
    @overload
    def query(self, expr: str, *, inplace: Literal[False] = ..., **kwargs) -> DataFrame: ...
    @overload
    def query(self, expr: str, *, inplace: Literal[True], **kwargs) -> None: ...
    @overload
    def query(self, expr: str, *, inplace: bool = ..., **kwargs) -> DataFrame | None: ...
    @overload
    def eval(self, expr: str, *, inplace: Literal[False] = ..., **kwargs) -> Any: ...
    @overload
    def eval(self, expr: str, *, inplace: Literal[True], **kwargs) -> None: ...
    def select_dtypes(self, include: Incomplete | None = None, exclude: Incomplete | None = None) -> DataFrame:
        """
        Return a subset of the DataFrame's columns based on the column dtypes.

        Parameters
        ----------
        include, exclude : scalar or list-like
            A selection of dtypes or strings to be included/excluded. At least
            one of these parameters must be supplied.

        Returns
        -------
        DataFrame
            The subset of the frame including the dtypes in ``include`` and
            excluding the dtypes in ``exclude``.

        Raises
        ------
        ValueError
            * If both of ``include`` and ``exclude`` are empty
            * If ``include`` and ``exclude`` have overlapping elements
            * If any kind of string dtype is passed in.

        See Also
        --------
        DataFrame.dtypes: Return Series with the data type of each column.

        Notes
        -----
        * To select all *numeric* types, use ``np.number`` or ``'number'``
        * To select strings you must use the ``object`` dtype, but note that
          this will return *all* object dtype columns
        * See the `numpy dtype hierarchy
          <https://numpy.org/doc/stable/reference/arrays.scalars.html>`__
        * To select datetimes, use ``np.datetime64``, ``'datetime'`` or
          ``'datetime64'``
        * To select timedeltas, use ``np.timedelta64``, ``'timedelta'`` or
          ``'timedelta64'``
        * To select Pandas categorical dtypes, use ``'category'``
        * To select Pandas datetimetz dtypes, use ``'datetimetz'`` (new in
          0.20.0) or ``'datetime64[ns, tz]'``

        Examples
        --------
        >>> df = pd.DataFrame({'a': [1, 2] * 3,
        ...                    'b': [True, False] * 3,
        ...                    'c': [1.0, 2.0] * 3})
        >>> df
                a      b  c
        0       1   True  1.0
        1       2  False  2.0
        2       1   True  1.0
        3       2  False  2.0
        4       1   True  1.0
        5       2  False  2.0

        >>> df.select_dtypes(include='bool')
           b
        0  True
        1  False
        2  True
        3  False
        4  True
        5  False

        >>> df.select_dtypes(include=['float64'])
           c
        0  1.0
        1  2.0
        2  1.0
        3  2.0
        4  1.0
        5  2.0

        >>> df.select_dtypes(exclude=['int64'])
               b    c
        0   True  1.0
        1  False  2.0
        2   True  1.0
        3  False  2.0
        4   True  1.0
        5  False  2.0
        """
    def insert(self, loc: int, column: Hashable, value: Scalar | AnyArrayLike, allow_duplicates: bool | lib.NoDefault = ...) -> None:
        '''
        Insert column into DataFrame at specified location.

        Raises a ValueError if `column` is already contained in the DataFrame,
        unless `allow_duplicates` is set to True.

        Parameters
        ----------
        loc : int
            Insertion index. Must verify 0 <= loc <= len(columns).
        column : str, number, or hashable object
            Label of the inserted column.
        value : Scalar, Series, or array-like
        allow_duplicates : bool, optional, default lib.no_default

        See Also
        --------
        Index.insert : Insert new item by index.

        Examples
        --------
        >>> df = pd.DataFrame({\'col1\': [1, 2], \'col2\': [3, 4]})
        >>> df
           col1  col2
        0     1     3
        1     2     4
        >>> df.insert(1, "newcol", [99, 99])
        >>> df
           col1  newcol  col2
        0     1      99     3
        1     2      99     4
        >>> df.insert(0, "col1", [100, 100], allow_duplicates=True)
        >>> df
           col1  col1  newcol  col2
        0   100     1      99     3
        1   100     2      99     4

        Notice that pandas uses index alignment in case of `value` from type `Series`:

        >>> df.insert(0, "col0", pd.Series([5, 6], index=[1, 2]))
        >>> df
           col0  col1  col1  newcol  col2
        0   NaN   100     1      99     3
        1   5.0   100     2      99     4
        '''
    def assign(self, **kwargs) -> DataFrame:
        """
        Assign new columns to a DataFrame.

        Returns a new object with all original columns in addition to new ones.
        Existing columns that are re-assigned will be overwritten.

        Parameters
        ----------
        **kwargs : dict of {str: callable or Series}
            The column names are keywords. If the values are
            callable, they are computed on the DataFrame and
            assigned to the new columns. The callable must not
            change input DataFrame (though pandas doesn't check it).
            If the values are not callable, (e.g. a Series, scalar, or array),
            they are simply assigned.

        Returns
        -------
        DataFrame
            A new DataFrame with the new columns in addition to
            all the existing columns.

        Notes
        -----
        Assigning multiple columns within the same ``assign`` is possible.
        Later items in '\\*\\*kwargs' may refer to newly created or modified
        columns in 'df'; items are computed and assigned into 'df' in order.

        Examples
        --------
        >>> df = pd.DataFrame({'temp_c': [17.0, 25.0]},
        ...                   index=['Portland', 'Berkeley'])
        >>> df
                  temp_c
        Portland    17.0
        Berkeley    25.0

        Where the value is a callable, evaluated on `df`:

        >>> df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
                  temp_c  temp_f
        Portland    17.0    62.6
        Berkeley    25.0    77.0

        Alternatively, the same behavior can be achieved by directly
        referencing an existing Series or sequence:

        >>> df.assign(temp_f=df['temp_c'] * 9 / 5 + 32)
                  temp_c  temp_f
        Portland    17.0    62.6
        Berkeley    25.0    77.0

        You can create multiple columns within the same assign where one
        of the columns depends on another one defined within the same assign:

        >>> df.assign(temp_f=lambda x: x['temp_c'] * 9 / 5 + 32,
        ...           temp_k=lambda x: (x['temp_f'] + 459.67) * 5 / 9)
                  temp_c  temp_f  temp_k
        Portland    17.0    62.6  290.15
        Berkeley    25.0    77.0  298.15
        """
    def align(self, other: DataFrame, join: AlignJoin = 'outer', axis: Axis | None = None, level: Level = None, copy: bool | None = None, fill_value: Incomplete | None = None, method: FillnaOptions | None = None, limit: int | None = None, fill_axis: Axis = 0, broadcast_axis: Axis | None = None) -> DataFrame: ...
    def set_axis(self, labels, *, axis: Axis = 0, copy: bool | None = None) -> DataFrame: ...
    def reindex(self, labels: Incomplete | None = None, *, index: Incomplete | None = None, columns: Incomplete | None = None, axis: Axis | None = None, method: str | None = None, copy: bool | None = None, level: Level | None = None, fill_value: Scalar | None = ..., limit: int | None = None, tolerance: Incomplete | None = None) -> DataFrame: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Level = ..., inplace: Literal[True], errors: IgnoreRaise = ...) -> None: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Level = ..., inplace: Literal[False] = ..., errors: IgnoreRaise = ...) -> DataFrame: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Level = ..., inplace: bool = ..., errors: IgnoreRaise = ...) -> DataFrame | None: ...
    @overload
    def rename(self, mapper: Renamer | None = ..., *, index: Renamer | None = ..., columns: Renamer | None = ..., axis: Axis | None = ..., copy: bool | None = ..., inplace: Literal[True], level: Level = ..., errors: IgnoreRaise = ...) -> None: ...
    @overload
    def rename(self, mapper: Renamer | None = ..., *, index: Renamer | None = ..., columns: Renamer | None = ..., axis: Axis | None = ..., copy: bool | None = ..., inplace: Literal[False] = ..., level: Level = ..., errors: IgnoreRaise = ...) -> DataFrame: ...
    @overload
    def rename(self, mapper: Renamer | None = ..., *, index: Renamer | None = ..., columns: Renamer | None = ..., axis: Axis | None = ..., copy: bool | None = ..., inplace: bool = ..., level: Level = ..., errors: IgnoreRaise = ...) -> DataFrame | None: ...
    @overload
    def fillna(self, value: Hashable | Mapping | Series | DataFrame = ..., *, method: FillnaOptions | None = ..., axis: Axis | None = ..., inplace: Literal[False] = ..., limit: int | None = ..., downcast: dict | None = ...) -> DataFrame: ...
    @overload
    def fillna(self, value: Hashable | Mapping | Series | DataFrame = ..., *, method: FillnaOptions | None = ..., axis: Axis | None = ..., inplace: Literal[True], limit: int | None = ..., downcast: dict | None = ...) -> None: ...
    @overload
    def fillna(self, value: Hashable | Mapping | Series | DataFrame = ..., *, method: FillnaOptions | None = ..., axis: Axis | None = ..., inplace: bool = ..., limit: int | None = ..., downcast: dict | None = ...) -> DataFrame | None: ...
    def pop(self, item: Hashable) -> Series:
        """
        Return item and drop from frame. Raise KeyError if not found.

        Parameters
        ----------
        item : label
            Label of column to be popped.

        Returns
        -------
        Series

        Examples
        --------
        >>> df = pd.DataFrame([('falcon', 'bird', 389.0),
        ...                    ('parrot', 'bird', 24.0),
        ...                    ('lion', 'mammal', 80.5),
        ...                    ('monkey', 'mammal', np.nan)],
        ...                   columns=('name', 'class', 'max_speed'))
        >>> df
             name   class  max_speed
        0  falcon    bird      389.0
        1  parrot    bird       24.0
        2    lion  mammal       80.5
        3  monkey  mammal        NaN

        >>> df.pop('class')
        0      bird
        1      bird
        2    mammal
        3    mammal
        Name: class, dtype: object

        >>> df
             name  max_speed
        0  falcon      389.0
        1  parrot       24.0
        2    lion       80.5
        3  monkey        NaN
        """
    @overload
    def replace(self, to_replace=..., value=..., *, inplace: Literal[False] = ..., limit: int | None = ..., regex: bool = ..., method: Literal['pad', 'ffill', 'bfill'] | lib.NoDefault = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace=..., value=..., *, inplace: Literal[True], limit: int | None = ..., regex: bool = ..., method: Literal['pad', 'ffill', 'bfill'] | lib.NoDefault = ...) -> None: ...
    def shift(self, periods: int = 1, freq: Frequency | None = None, axis: Axis = 0, fill_value: Hashable = ...) -> DataFrame: ...
    @overload
    def set_index(self, keys, *, drop: bool = ..., append: bool = ..., inplace: Literal[False] = ..., verify_integrity: bool = ...) -> DataFrame: ...
    @overload
    def set_index(self, keys, *, drop: bool = ..., append: bool = ..., inplace: Literal[True], verify_integrity: bool = ...) -> None: ...
    @overload
    def reset_index(self, level: IndexLabel = ..., *, drop: bool = ..., inplace: Literal[False] = ..., col_level: Hashable = ..., col_fill: Hashable = ..., allow_duplicates: bool | lib.NoDefault = ..., names: Hashable | Sequence[Hashable] = None) -> DataFrame: ...
    @overload
    def reset_index(self, level: IndexLabel = ..., *, drop: bool = ..., inplace: Literal[True], col_level: Hashable = ..., col_fill: Hashable = ..., allow_duplicates: bool | lib.NoDefault = ..., names: Hashable | Sequence[Hashable] = None) -> None: ...
    @overload
    def reset_index(self, level: IndexLabel = ..., *, drop: bool = ..., inplace: bool = ..., col_level: Hashable = ..., col_fill: Hashable = ..., allow_duplicates: bool | lib.NoDefault = ..., names: Hashable | Sequence[Hashable] = None) -> DataFrame | None: ...
    def isna(self) -> DataFrame: ...
    def isnull(self) -> DataFrame:
        """
        DataFrame.isnull is an alias for DataFrame.isna.
        """
    def notna(self) -> DataFrame: ...
    def notnull(self) -> DataFrame:
        """
        DataFrame.notnull is an alias for DataFrame.notna.
        """
    @overload
    def dropna(self, *, axis: Axis = ..., how: AnyAll | NoDefault = ..., thresh: int | NoDefault = ..., subset: IndexLabel = ..., inplace: Literal[False] = ..., ignore_index: bool = ...) -> DataFrame: ...
    @overload
    def dropna(self, *, axis: Axis = ..., how: AnyAll | NoDefault = ..., thresh: int | NoDefault = ..., subset: IndexLabel = ..., inplace: Literal[True], ignore_index: bool = ...) -> None: ...
    def drop_duplicates(self, subset: Hashable | Sequence[Hashable] | None = None, *, keep: DropKeep = 'first', inplace: bool = False, ignore_index: bool = False) -> DataFrame | None:
        """
        Return DataFrame with duplicate rows removed.

        Considering certain columns is optional. Indexes, including time indexes
        are ignored.

        Parameters
        ----------
        subset : column label or sequence of labels, optional
            Only consider certain columns for identifying duplicates, by
            default use all of the columns.
        keep : {'first', 'last', ``False``}, default 'first'
            Determines which duplicates (if any) to keep.

            - 'first' : Drop duplicates except for the first occurrence.
            - 'last' : Drop duplicates except for the last occurrence.
            - ``False`` : Drop all duplicates.

        inplace : bool, default ``False``
            Whether to modify the DataFrame rather than creating a new one.
        ignore_index : bool, default ``False``
            If ``True``, the resulting axis will be labeled 0, 1, …, n - 1.

        Returns
        -------
        DataFrame or None
            DataFrame with duplicates removed or None if ``inplace=True``.

        See Also
        --------
        DataFrame.value_counts: Count unique combinations of columns.

        Examples
        --------
        Consider dataset containing ramen rating.

        >>> df = pd.DataFrame({
        ...     'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
        ...     'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
        ...     'rating': [4, 4, 3.5, 15, 5]
        ... })
        >>> df
            brand style  rating
        0  Yum Yum   cup     4.0
        1  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        3  Indomie  pack    15.0
        4  Indomie  pack     5.0

        By default, it removes duplicate rows based on all columns.

        >>> df.drop_duplicates()
            brand style  rating
        0  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        3  Indomie  pack    15.0
        4  Indomie  pack     5.0

        To remove duplicates on specific column(s), use ``subset``.

        >>> df.drop_duplicates(subset=['brand'])
            brand style  rating
        0  Yum Yum   cup     4.0
        2  Indomie   cup     3.5

        To remove duplicates and keep last occurrences, use ``keep``.

        >>> df.drop_duplicates(subset=['brand', 'style'], keep='last')
            brand style  rating
        1  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        4  Indomie  pack     5.0
        """
    def duplicated(self, subset: Hashable | Sequence[Hashable] | None = None, keep: DropKeep = 'first') -> Series:
        """
        Return boolean Series denoting duplicate rows.

        Considering certain columns is optional.

        Parameters
        ----------
        subset : column label or sequence of labels, optional
            Only consider certain columns for identifying duplicates, by
            default use all of the columns.
        keep : {'first', 'last', False}, default 'first'
            Determines which duplicates (if any) to mark.

            - ``first`` : Mark duplicates as ``True`` except for the first occurrence.
            - ``last`` : Mark duplicates as ``True`` except for the last occurrence.
            - False : Mark all duplicates as ``True``.

        Returns
        -------
        Series
            Boolean series for each duplicated rows.

        See Also
        --------
        Index.duplicated : Equivalent method on index.
        Series.duplicated : Equivalent method on Series.
        Series.drop_duplicates : Remove duplicate values from Series.
        DataFrame.drop_duplicates : Remove duplicate values from DataFrame.

        Examples
        --------
        Consider dataset containing ramen rating.

        >>> df = pd.DataFrame({
        ...     'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
        ...     'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
        ...     'rating': [4, 4, 3.5, 15, 5]
        ... })
        >>> df
            brand style  rating
        0  Yum Yum   cup     4.0
        1  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        3  Indomie  pack    15.0
        4  Indomie  pack     5.0

        By default, for each set of duplicated values, the first occurrence
        is set on False and all others on True.

        >>> df.duplicated()
        0    False
        1     True
        2    False
        3    False
        4    False
        dtype: bool

        By using 'last', the last occurrence of each set of duplicated values
        is set on False and all others on True.

        >>> df.duplicated(keep='last')
        0     True
        1    False
        2    False
        3    False
        4    False
        dtype: bool

        By setting ``keep`` on False, all duplicates are True.

        >>> df.duplicated(keep=False)
        0     True
        1     True
        2    False
        3    False
        4    False
        dtype: bool

        To find duplicates on specific column(s), use ``subset``.

        >>> df.duplicated(subset=['brand'])
        0    False
        1     True
        2    False
        3     True
        4     True
        dtype: bool
        """
    @overload
    def sort_values(self, by: IndexLabel, *, axis: Axis = ..., ascending=..., inplace: Literal[False] = ..., kind: str = ..., na_position: str = ..., ignore_index: bool = ..., key: ValueKeyFunc = ...) -> DataFrame: ...
    @overload
    def sort_values(self, by: IndexLabel, *, axis: Axis = ..., ascending=..., inplace: Literal[True], kind: str = ..., na_position: str = ..., ignore_index: bool = ..., key: ValueKeyFunc = ...) -> None: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: bool | Sequence[bool] = ..., inplace: Literal[True], kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ...) -> None: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: bool | Sequence[bool] = ..., inplace: Literal[False] = ..., kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ...) -> DataFrame: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: bool | Sequence[bool] = ..., inplace: bool = ..., kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ...) -> DataFrame | None: ...
    def value_counts(self, subset: Sequence[Hashable] | None = None, normalize: bool = False, sort: bool = True, ascending: bool = False, dropna: bool = True) -> Series:
        '''
        Return a Series containing counts of unique rows in the DataFrame.

        .. versionadded:: 1.1.0

        Parameters
        ----------
        subset : label or list of labels, optional
            Columns to use when counting unique combinations.
        normalize : bool, default False
            Return proportions rather than frequencies.
        sort : bool, default True
            Sort by frequencies.
        ascending : bool, default False
            Sort in ascending order.
        dropna : bool, default True
            Don’t include counts of rows that contain NA values.

            .. versionadded:: 1.3.0

        Returns
        -------
        Series

        See Also
        --------
        Series.value_counts: Equivalent method on Series.

        Notes
        -----
        The returned Series will have a MultiIndex with one level per input
        column but an Index (non-multi) for a single label. By default, rows
        that contain any NA values are omitted from the result. By default,
        the resulting Series will be in descending order so that the first
        element is the most frequently-occurring row.

        Examples
        --------
        >>> df = pd.DataFrame({\'num_legs\': [2, 4, 4, 6],
        ...                    \'num_wings\': [2, 0, 0, 0]},
        ...                   index=[\'falcon\', \'dog\', \'cat\', \'ant\'])
        >>> df
                num_legs  num_wings
        falcon         2          2
        dog            4          0
        cat            4          0
        ant            6          0

        >>> df.value_counts()
        num_legs  num_wings
        4         0            2
        2         2            1
        6         0            1
        Name: count, dtype: int64

        >>> df.value_counts(sort=False)
        num_legs  num_wings
        2         2            1
        4         0            2
        6         0            1
        Name: count, dtype: int64

        >>> df.value_counts(ascending=True)
        num_legs  num_wings
        2         2            1
        6         0            1
        4         0            2
        Name: count, dtype: int64

        >>> df.value_counts(normalize=True)
        num_legs  num_wings
        4         0            0.50
        2         2            0.25
        6         0            0.25
        Name: proportion, dtype: float64

        With `dropna` set to `False` we can also count rows with NA values.

        >>> df = pd.DataFrame({\'first_name\': [\'John\', \'Anne\', \'John\', \'Beth\'],
        ...                    \'middle_name\': [\'Smith\', pd.NA, pd.NA, \'Louise\']})
        >>> df
          first_name middle_name
        0       John       Smith
        1       Anne        <NA>
        2       John        <NA>
        3       Beth      Louise

        >>> df.value_counts()
        first_name  middle_name
        Beth        Louise         1
        John        Smith          1
        Name: count, dtype: int64

        >>> df.value_counts(dropna=False)
        first_name  middle_name
        Anne        NaN            1
        Beth        Louise         1
        John        Smith          1
                    NaN            1
        Name: count, dtype: int64

        >>> df.value_counts("first_name")
        first_name
        John    2
        Anne    1
        Beth    1
        Name: count, dtype: int64
        '''
    def nlargest(self, n: int, columns: IndexLabel, keep: str = 'first') -> DataFrame:
        '''
        Return the first `n` rows ordered by `columns` in descending order.

        Return the first `n` rows with the largest values in `columns`, in
        descending order. The columns that are not specified are returned as
        well, but not used for ordering.

        This method is equivalent to
        ``df.sort_values(columns, ascending=False).head(n)``, but more
        performant.

        Parameters
        ----------
        n : int
            Number of rows to return.
        columns : label or list of labels
            Column label(s) to order by.
        keep : {\'first\', \'last\', \'all\'}, default \'first\'
            Where there are duplicate values:

            - ``first`` : prioritize the first occurrence(s)
            - ``last`` : prioritize the last occurrence(s)
            - ``all`` : do not drop any duplicates, even it means
              selecting more than `n` items.

        Returns
        -------
        DataFrame
            The first `n` rows ordered by the given columns in descending
            order.

        See Also
        --------
        DataFrame.nsmallest : Return the first `n` rows ordered by `columns` in
            ascending order.
        DataFrame.sort_values : Sort DataFrame by the values.
        DataFrame.head : Return the first `n` rows without re-ordering.

        Notes
        -----
        This function cannot be used with all column types. For example, when
        specifying columns with `object` or `category` dtypes, ``TypeError`` is
        raised.

        Examples
        --------
        >>> df = pd.DataFrame({\'population\': [59000000, 65000000, 434000,
        ...                                   434000, 434000, 337000, 11300,
        ...                                   11300, 11300],
        ...                    \'GDP\': [1937894, 2583560 , 12011, 4520, 12128,
        ...                            17036, 182, 38, 311],
        ...                    \'alpha-2\': ["IT", "FR", "MT", "MV", "BN",
        ...                                "IS", "NR", "TV", "AI"]},
        ...                   index=["Italy", "France", "Malta",
        ...                          "Maldives", "Brunei", "Iceland",
        ...                          "Nauru", "Tuvalu", "Anguilla"])
        >>> df
                  population      GDP alpha-2
        Italy       59000000  1937894      IT
        France      65000000  2583560      FR
        Malta         434000    12011      MT
        Maldives      434000     4520      MV
        Brunei        434000    12128      BN
        Iceland       337000    17036      IS
        Nauru          11300      182      NR
        Tuvalu         11300       38      TV
        Anguilla       11300      311      AI

        In the following example, we will use ``nlargest`` to select the three
        rows having the largest values in column "population".

        >>> df.nlargest(3, \'population\')
                population      GDP alpha-2
        France    65000000  2583560      FR
        Italy     59000000  1937894      IT
        Malta       434000    12011      MT

        When using ``keep=\'last\'``, ties are resolved in reverse order:

        >>> df.nlargest(3, \'population\', keep=\'last\')
                population      GDP alpha-2
        France    65000000  2583560      FR
        Italy     59000000  1937894      IT
        Brunei      434000    12128      BN

        When using ``keep=\'all\'``, all duplicate items are maintained:

        >>> df.nlargest(3, \'population\', keep=\'all\')
                  population      GDP alpha-2
        France      65000000  2583560      FR
        Italy       59000000  1937894      IT
        Malta         434000    12011      MT
        Maldives      434000     4520      MV
        Brunei        434000    12128      BN

        To order by the largest values in column "population" and then "GDP",
        we can specify multiple columns like in the next example.

        >>> df.nlargest(3, [\'population\', \'GDP\'])
                population      GDP alpha-2
        France    65000000  2583560      FR
        Italy     59000000  1937894      IT
        Brunei      434000    12128      BN
        '''
    def nsmallest(self, n: int, columns: IndexLabel, keep: str = 'first') -> DataFrame:
        '''
        Return the first `n` rows ordered by `columns` in ascending order.

        Return the first `n` rows with the smallest values in `columns`, in
        ascending order. The columns that are not specified are returned as
        well, but not used for ordering.

        This method is equivalent to
        ``df.sort_values(columns, ascending=True).head(n)``, but more
        performant.

        Parameters
        ----------
        n : int
            Number of items to retrieve.
        columns : list or str
            Column name or names to order by.
        keep : {\'first\', \'last\', \'all\'}, default \'first\'
            Where there are duplicate values:

            - ``first`` : take the first occurrence.
            - ``last`` : take the last occurrence.
            - ``all`` : do not drop any duplicates, even it means
              selecting more than `n` items.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.nlargest : Return the first `n` rows ordered by `columns` in
            descending order.
        DataFrame.sort_values : Sort DataFrame by the values.
        DataFrame.head : Return the first `n` rows without re-ordering.

        Examples
        --------
        >>> df = pd.DataFrame({\'population\': [59000000, 65000000, 434000,
        ...                                   434000, 434000, 337000, 337000,
        ...                                   11300, 11300],
        ...                    \'GDP\': [1937894, 2583560 , 12011, 4520, 12128,
        ...                            17036, 182, 38, 311],
        ...                    \'alpha-2\': ["IT", "FR", "MT", "MV", "BN",
        ...                                "IS", "NR", "TV", "AI"]},
        ...                   index=["Italy", "France", "Malta",
        ...                          "Maldives", "Brunei", "Iceland",
        ...                          "Nauru", "Tuvalu", "Anguilla"])
        >>> df
                  population      GDP alpha-2
        Italy       59000000  1937894      IT
        France      65000000  2583560      FR
        Malta         434000    12011      MT
        Maldives      434000     4520      MV
        Brunei        434000    12128      BN
        Iceland       337000    17036      IS
        Nauru         337000      182      NR
        Tuvalu         11300       38      TV
        Anguilla       11300      311      AI

        In the following example, we will use ``nsmallest`` to select the
        three rows having the smallest values in column "population".

        >>> df.nsmallest(3, \'population\')
                  population    GDP alpha-2
        Tuvalu         11300     38      TV
        Anguilla       11300    311      AI
        Iceland       337000  17036      IS

        When using ``keep=\'last\'``, ties are resolved in reverse order:

        >>> df.nsmallest(3, \'population\', keep=\'last\')
                  population  GDP alpha-2
        Anguilla       11300  311      AI
        Tuvalu         11300   38      TV
        Nauru         337000  182      NR

        When using ``keep=\'all\'``, all duplicate items are maintained:

        >>> df.nsmallest(3, \'population\', keep=\'all\')
                  population    GDP alpha-2
        Tuvalu         11300     38      TV
        Anguilla       11300    311      AI
        Iceland       337000  17036      IS
        Nauru         337000    182      NR

        To order by the smallest values in column "population" and then "GDP", we can
        specify multiple columns like in the next example.

        >>> df.nsmallest(3, [\'population\', \'GDP\'])
                  population  GDP alpha-2
        Tuvalu         11300   38      TV
        Anguilla       11300  311      AI
        Nauru         337000  182      NR
        '''
    def swaplevel(self, i: Axis = -2, j: Axis = -1, axis: Axis = 0) -> DataFrame: ...
    def reorder_levels(self, order: Sequence[int | str], axis: Axis = 0) -> DataFrame:
        '''
        Rearrange index levels using input order. May not drop or duplicate levels.

        Parameters
        ----------
        order : list of int or list of str
            List representing new level order. Reference level by number
            (position) or by key (label).
        axis : {0 or \'index\', 1 or \'columns\'}, default 0
            Where to reorder levels.

        Returns
        -------
        DataFrame

        Examples
        --------
        >>> data = {
        ...     "class": ["Mammals", "Mammals", "Reptiles"],
        ...     "diet": ["Omnivore", "Carnivore", "Carnivore"],
        ...     "species": ["Humans", "Dogs", "Snakes"],
        ... }
        >>> df = pd.DataFrame(data, columns=["class", "diet", "species"])
        >>> df = df.set_index(["class", "diet"])
        >>> df
                                          species
        class      diet
        Mammals    Omnivore                Humans
                   Carnivore                 Dogs
        Reptiles   Carnivore               Snakes

        Let\'s reorder the levels of the index:

        >>> df.reorder_levels(["diet", "class"])
                                          species
        diet      class
        Omnivore  Mammals                  Humans
        Carnivore Mammals                    Dogs
                  Reptiles                 Snakes
        '''
    def __divmod__(self, other) -> tuple[DataFrame, DataFrame]: ...
    def __rdivmod__(self, other) -> tuple[DataFrame, DataFrame]: ...
    def compare(self, other: DataFrame, align_axis: Axis = 1, keep_shape: bool = False, keep_equal: bool = False, result_names: Suffixes = ('self', 'other')) -> DataFrame: ...
    def combine(self, other: DataFrame, func: Callable[[Series, Series], Series | Hashable], fill_value: Incomplete | None = None, overwrite: bool = True) -> DataFrame:
        """
        Perform column-wise combine with another DataFrame.

        Combines a DataFrame with `other` DataFrame using `func`
        to element-wise combine columns. The row and column indexes of the
        resulting DataFrame will be the union of the two.

        Parameters
        ----------
        other : DataFrame
            The DataFrame to merge column-wise.
        func : function
            Function that takes two series as inputs and return a Series or a
            scalar. Used to merge the two dataframes column by columns.
        fill_value : scalar value, default None
            The value to fill NaNs with prior to passing any column to the
            merge func.
        overwrite : bool, default True
            If True, columns in `self` that do not exist in `other` will be
            overwritten with NaNs.

        Returns
        -------
        DataFrame
            Combination of the provided DataFrames.

        See Also
        --------
        DataFrame.combine_first : Combine two DataFrame objects and default to
            non-null values in frame calling the method.

        Examples
        --------
        Combine using a simple function that chooses the smaller column.

        >>> df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
        >>> df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
        >>> take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
        >>> df1.combine(df2, take_smaller)
           A  B
        0  0  3
        1  0  3

        Example using a true element-wise combine function.

        >>> df1 = pd.DataFrame({'A': [5, 0], 'B': [2, 4]})
        >>> df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
        >>> df1.combine(df2, np.minimum)
           A  B
        0  1  2
        1  0  3

        Using `fill_value` fills Nones prior to passing the column to the
        merge function.

        >>> df1 = pd.DataFrame({'A': [0, 0], 'B': [None, 4]})
        >>> df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
        >>> df1.combine(df2, take_smaller, fill_value=-5)
           A    B
        0  0 -5.0
        1  0  4.0

        However, if the same element in both dataframes is None, that None
        is preserved

        >>> df1 = pd.DataFrame({'A': [0, 0], 'B': [None, 4]})
        >>> df2 = pd.DataFrame({'A': [1, 1], 'B': [None, 3]})
        >>> df1.combine(df2, take_smaller, fill_value=-5)
            A    B
        0  0 -5.0
        1  0  3.0

        Example that demonstrates the use of `overwrite` and behavior when
        the axis differ between the dataframes.

        >>> df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
        >>> df2 = pd.DataFrame({'B': [3, 3], 'C': [-10, 1], }, index=[1, 2])
        >>> df1.combine(df2, take_smaller)
             A    B     C
        0  NaN  NaN   NaN
        1  NaN  3.0 -10.0
        2  NaN  3.0   1.0

        >>> df1.combine(df2, take_smaller, overwrite=False)
             A    B     C
        0  0.0  NaN   NaN
        1  0.0  3.0 -10.0
        2  NaN  3.0   1.0

        Demonstrating the preference of the passed in dataframe.

        >>> df2 = pd.DataFrame({'B': [3, 3], 'C': [1, 1], }, index=[1, 2])
        >>> df2.combine(df1, take_smaller)
           A    B   C
        0  0.0  NaN NaN
        1  0.0  3.0 NaN
        2  NaN  3.0 NaN

        >>> df2.combine(df1, take_smaller, overwrite=False)
             A    B   C
        0  0.0  NaN NaN
        1  0.0  3.0 1.0
        2  NaN  3.0 1.0
        """
    def combine_first(self, other: DataFrame) -> DataFrame:
        """
        Update null elements with value in the same location in `other`.

        Combine two DataFrame objects by filling null values in one DataFrame
        with non-null values from other DataFrame. The row and column indexes
        of the resulting DataFrame will be the union of the two. The resulting
        dataframe contains the 'first' dataframe values and overrides the
        second one values where both first.loc[index, col] and
        second.loc[index, col] are not missing values, upon calling
        first.combine_first(second).

        Parameters
        ----------
        other : DataFrame
            Provided DataFrame to use to fill null values.

        Returns
        -------
        DataFrame
            The result of combining the provided DataFrame with the other object.

        See Also
        --------
        DataFrame.combine : Perform series-wise operation on two DataFrames
            using a given function.

        Examples
        --------
        >>> df1 = pd.DataFrame({'A': [None, 0], 'B': [None, 4]})
        >>> df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
        >>> df1.combine_first(df2)
             A    B
        0  1.0  3.0
        1  0.0  4.0

        Null values still persist if the location of that null value
        does not exist in `other`

        >>> df1 = pd.DataFrame({'A': [None, 0], 'B': [4, None]})
        >>> df2 = pd.DataFrame({'B': [3, 3], 'C': [1, 1]}, index=[1, 2])
        >>> df1.combine_first(df2)
             A    B    C
        0  NaN  4.0  NaN
        1  0.0  3.0  1.0
        2  NaN  3.0  1.0
        """
    def update(self, other, join: str = 'left', overwrite: bool = True, filter_func: Incomplete | None = None, errors: str = 'ignore') -> None:
        """
        Modify in place using non-NA values from another DataFrame.

        Aligns on indices. There is no return value.

        Parameters
        ----------
        other : DataFrame, or object coercible into a DataFrame
            Should have at least one matching index/column label
            with the original DataFrame. If a Series is passed,
            its name attribute must be set, and that will be
            used as the column name to align with the original DataFrame.
        join : {'left'}, default 'left'
            Only left join is implemented, keeping the index and columns of the
            original object.
        overwrite : bool, default True
            How to handle non-NA values for overlapping keys:

            * True: overwrite original DataFrame's values
              with values from `other`.
            * False: only update values that are NA in
              the original DataFrame.

        filter_func : callable(1d-array) -> bool 1d-array, optional
            Can choose to replace values other than NA. Return True for values
            that should be updated.
        errors : {'raise', 'ignore'}, default 'ignore'
            If 'raise', will raise a ValueError if the DataFrame and `other`
            both contain non-NA data in the same place.

        Returns
        -------
        None
            This method directly changes calling object.

        Raises
        ------
        ValueError
            * When `errors='raise'` and there's overlapping non-NA data.
            * When `errors` is not either `'ignore'` or `'raise'`
        NotImplementedError
            * If `join != 'left'`

        See Also
        --------
        dict.update : Similar method for dictionaries.
        DataFrame.merge : For column(s)-on-column(s) operations.

        Examples
        --------
        >>> df = pd.DataFrame({'A': [1, 2, 3],
        ...                    'B': [400, 500, 600]})
        >>> new_df = pd.DataFrame({'B': [4, 5, 6],
        ...                        'C': [7, 8, 9]})
        >>> df.update(new_df)
        >>> df
           A  B
        0  1  4
        1  2  5
        2  3  6

        The DataFrame's length does not increase as a result of the update,
        only values at matching index/column labels are updated.

        >>> df = pd.DataFrame({'A': ['a', 'b', 'c'],
        ...                    'B': ['x', 'y', 'z']})
        >>> new_df = pd.DataFrame({'B': ['d', 'e', 'f', 'g', 'h', 'i']})
        >>> df.update(new_df)
        >>> df
           A  B
        0  a  d
        1  b  e
        2  c  f

        For Series, its name attribute must be set.

        >>> df = pd.DataFrame({'A': ['a', 'b', 'c'],
        ...                    'B': ['x', 'y', 'z']})
        >>> new_column = pd.Series(['d', 'e'], name='B', index=[0, 2])
        >>> df.update(new_column)
        >>> df
           A  B
        0  a  d
        1  b  y
        2  c  e
        >>> df = pd.DataFrame({'A': ['a', 'b', 'c'],
        ...                    'B': ['x', 'y', 'z']})
        >>> new_df = pd.DataFrame({'B': ['d', 'e']}, index=[1, 2])
        >>> df.update(new_df)
        >>> df
           A  B
        0  a  x
        1  b  d
        2  c  e

        If `other` contains NaNs the corresponding values are not updated
        in the original dataframe.

        >>> df = pd.DataFrame({'A': [1, 2, 3],
        ...                    'B': [400, 500, 600]})
        >>> new_df = pd.DataFrame({'B': [4, np.nan, 6]})
        >>> df.update(new_df)
        >>> df
           A    B
        0  1    4
        1  2  500
        2  3    6
        """
    def groupby(self, by: Incomplete | None = None, axis: Axis = 0, level: IndexLabel | None = None, as_index: bool = True, sort: bool = True, group_keys: bool = True, observed: bool = False, dropna: bool = True) -> DataFrameGroupBy: ...
    def pivot(self, *, columns, index=..., values=...) -> DataFrame: ...
    def pivot_table(self, values: Incomplete | None = None, index: Incomplete | None = None, columns: Incomplete | None = None, aggfunc: AggFuncType = 'mean', fill_value: Incomplete | None = None, margins: bool = False, dropna: bool = True, margins_name: Level = 'All', observed: bool = False, sort: bool = True) -> DataFrame: ...
    def stack(self, level: Level = -1, dropna: bool = True):
        """
        Stack the prescribed level(s) from columns to index.

        Return a reshaped DataFrame or Series having a multi-level
        index with one or more new inner-most levels compared to the current
        DataFrame. The new inner-most levels are created by pivoting the
        columns of the current dataframe:

          - if the columns have a single level, the output is a Series;
          - if the columns have multiple levels, the new index
            level(s) is (are) taken from the prescribed level(s) and
            the output is a DataFrame.

        Parameters
        ----------
        level : int, str, list, default -1
            Level(s) to stack from the column axis onto the index
            axis, defined as one index or label, or a list of indices
            or labels.
        dropna : bool, default True
            Whether to drop rows in the resulting Frame/Series with
            missing values. Stacking a column level onto the index
            axis can create combinations of index and column values
            that are missing from the original dataframe. See Examples
            section.

        Returns
        -------
        DataFrame or Series
            Stacked dataframe or series.

        See Also
        --------
        DataFrame.unstack : Unstack prescribed level(s) from index axis
             onto column axis.
        DataFrame.pivot : Reshape dataframe from long format to wide
             format.
        DataFrame.pivot_table : Create a spreadsheet-style pivot table
             as a DataFrame.

        Notes
        -----
        The function is named by analogy with a collection of books
        being reorganized from being side by side on a horizontal
        position (the columns of the dataframe) to being stacked
        vertically on top of each other (in the index of the
        dataframe).

        Reference :ref:`the user guide <reshaping.stacking>` for more examples.

        Examples
        --------
        **Single level columns**

        >>> df_single_level_cols = pd.DataFrame([[0, 1], [2, 3]],
        ...                                     index=['cat', 'dog'],
        ...                                     columns=['weight', 'height'])

        Stacking a dataframe with a single level column axis returns a Series:

        >>> df_single_level_cols
             weight height
        cat       0      1
        dog       2      3
        >>> df_single_level_cols.stack()
        cat  weight    0
             height    1
        dog  weight    2
             height    3
        dtype: int64

        **Multi level columns: simple case**

        >>> multicol1 = pd.MultiIndex.from_tuples([('weight', 'kg'),
        ...                                        ('weight', 'pounds')])
        >>> df_multi_level_cols1 = pd.DataFrame([[1, 2], [2, 4]],
        ...                                     index=['cat', 'dog'],
        ...                                     columns=multicol1)

        Stacking a dataframe with a multi-level column axis:

        >>> df_multi_level_cols1
             weight
                 kg    pounds
        cat       1        2
        dog       2        4
        >>> df_multi_level_cols1.stack()
                    weight
        cat kg           1
            pounds       2
        dog kg           2
            pounds       4

        **Missing values**

        >>> multicol2 = pd.MultiIndex.from_tuples([('weight', 'kg'),
        ...                                        ('height', 'm')])
        >>> df_multi_level_cols2 = pd.DataFrame([[1.0, 2.0], [3.0, 4.0]],
        ...                                     index=['cat', 'dog'],
        ...                                     columns=multicol2)

        It is common to have missing values when stacking a dataframe
        with multi-level columns, as the stacked dataframe typically
        has more values than the original dataframe. Missing values
        are filled with NaNs:

        >>> df_multi_level_cols2
            weight height
                kg      m
        cat    1.0    2.0
        dog    3.0    4.0
        >>> df_multi_level_cols2.stack()
                height  weight
        cat kg     NaN     1.0
            m      2.0     NaN
        dog kg     NaN     3.0
            m      4.0     NaN

        **Prescribing the level(s) to be stacked**

        The first parameter controls which level or levels are stacked:

        >>> df_multi_level_cols2.stack(0)
                     kg    m
        cat height  NaN  2.0
            weight  1.0  NaN
        dog height  NaN  4.0
            weight  3.0  NaN
        >>> df_multi_level_cols2.stack([0, 1])
        cat  height  m     2.0
             weight  kg    1.0
        dog  height  m     4.0
             weight  kg    3.0
        dtype: float64

        **Dropping missing values**

        >>> df_multi_level_cols3 = pd.DataFrame([[None, 1.0], [2.0, 3.0]],
        ...                                     index=['cat', 'dog'],
        ...                                     columns=multicol2)

        Note that rows where all values are missing are dropped by
        default but this behaviour can be controlled via the dropna
        keyword parameter:

        >>> df_multi_level_cols3
            weight height
                kg      m
        cat    NaN    1.0
        dog    2.0    3.0
        >>> df_multi_level_cols3.stack(dropna=False)
                height  weight
        cat kg     NaN     NaN
            m      1.0     NaN
        dog kg     NaN     2.0
            m      3.0     NaN
        >>> df_multi_level_cols3.stack(dropna=True)
                height  weight
        cat m      1.0     NaN
        dog kg     NaN     2.0
            m      3.0     NaN
        """
    def explode(self, column: IndexLabel, ignore_index: bool = False) -> DataFrame:
        """
        Transform each element of a list-like to a row, replicating index values.

        Parameters
        ----------
        column : IndexLabel
            Column(s) to explode.
            For multiple columns, specify a non-empty list with each element
            be str or tuple, and all specified columns their list-like data
            on same row of the frame must have matching length.

            .. versionadded:: 1.3.0
                Multi-column explode

        ignore_index : bool, default False
            If True, the resulting index will be labeled 0, 1, …, n - 1.

            .. versionadded:: 1.1.0

        Returns
        -------
        DataFrame
            Exploded lists to rows of the subset columns;
            index will be duplicated for these rows.

        Raises
        ------
        ValueError :
            * If columns of the frame are not unique.
            * If specified columns to explode is empty list.
            * If specified columns to explode have not matching count of
              elements rowwise in the frame.

        See Also
        --------
        DataFrame.unstack : Pivot a level of the (necessarily hierarchical)
            index labels.
        DataFrame.melt : Unpivot a DataFrame from wide format to long format.
        Series.explode : Explode a DataFrame from list-like columns to long format.

        Notes
        -----
        This routine will explode list-likes including lists, tuples, sets,
        Series, and np.ndarray. The result dtype of the subset rows will
        be object. Scalars will be returned unchanged, and empty list-likes will
        result in a np.nan for that row. In addition, the ordering of rows in the
        output will be non-deterministic when exploding sets.

        Reference :ref:`the user guide <reshaping.explode>` for more examples.

        Examples
        --------
        >>> df = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
        ...                    'B': 1,
        ...                    'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]})
        >>> df
                   A  B          C
        0  [0, 1, 2]  1  [a, b, c]
        1        foo  1        NaN
        2         []  1         []
        3     [3, 4]  1     [d, e]

        Single-column explode.

        >>> df.explode('A')
             A  B          C
        0    0  1  [a, b, c]
        0    1  1  [a, b, c]
        0    2  1  [a, b, c]
        1  foo  1        NaN
        2  NaN  1         []
        3    3  1     [d, e]
        3    4  1     [d, e]

        Multi-column explode.

        >>> df.explode(list('AC'))
             A  B    C
        0    0  1    a
        0    1  1    b
        0    2  1    c
        1  foo  1  NaN
        2  NaN  1  NaN
        3    3  1    d
        3    4  1    e
        """
    def unstack(self, level: Level = -1, fill_value: Incomplete | None = None):
        """
        Pivot a level of the (necessarily hierarchical) index labels.

        Returns a DataFrame having a new level of column labels whose inner-most level
        consists of the pivoted index labels.

        If the index is not a MultiIndex, the output will be a Series
        (the analogue of stack when the columns are not a MultiIndex).

        Parameters
        ----------
        level : int, str, or list of these, default -1 (last level)
            Level(s) of index to unstack, can pass level name.
        fill_value : int, str or dict
            Replace NaN with this value if the unstack produces missing values.

        Returns
        -------
        Series or DataFrame

        See Also
        --------
        DataFrame.pivot : Pivot a table based on column values.
        DataFrame.stack : Pivot a level of the column labels (inverse operation
            from `unstack`).

        Notes
        -----
        Reference :ref:`the user guide <reshaping.stacking>` for more examples.

        Examples
        --------
        >>> index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),
        ...                                    ('two', 'a'), ('two', 'b')])
        >>> s = pd.Series(np.arange(1.0, 5.0), index=index)
        >>> s
        one  a   1.0
             b   2.0
        two  a   3.0
             b   4.0
        dtype: float64

        >>> s.unstack(level=-1)
             a   b
        one  1.0  2.0
        two  3.0  4.0

        >>> s.unstack(level=0)
           one  two
        a  1.0   3.0
        b  2.0   4.0

        >>> df = s.unstack(level=0)
        >>> df.unstack()
        one  a  1.0
             b  2.0
        two  a  3.0
             b  4.0
        dtype: float64
        """
    def melt(self, id_vars: Incomplete | None = None, value_vars: Incomplete | None = None, var_name: Incomplete | None = None, value_name: Hashable = 'value', col_level: Level = None, ignore_index: bool = True) -> DataFrame: ...
    def diff(self, periods: int = 1, axis: Axis = 0) -> DataFrame: ...
    def aggregate(self, func: Incomplete | None = None, axis: Axis = 0, *args, **kwargs): ...
    agg = aggregate
    @overload
    def any(self, *, axis: Axis = ..., bool_only: bool | None = ..., skipna: bool = ..., level: None = ..., **kwargs) -> Series: ...
    @overload
    def any(self, *, axis: Axis = ..., bool_only: bool | None = ..., skipna: bool = ..., level: Level, **kwargs) -> DataFrame | Series: ...
    def transform(self, func: AggFuncType, axis: Axis = 0, *args, **kwargs) -> DataFrame: ...
    def apply(self, func: AggFuncType, axis: Axis = 0, raw: bool = False, result_type: Literal['expand', 'reduce', 'broadcast'] | None = None, args=(), **kwargs):
        """
        Apply a function along an axis of the DataFrame.

        Objects passed to the function are Series objects whose index is
        either the DataFrame's index (``axis=0``) or the DataFrame's columns
        (``axis=1``). By default (``result_type=None``), the final return type
        is inferred from the return type of the applied function. Otherwise,
        it depends on the `result_type` argument.

        Parameters
        ----------
        func : function
            Function to apply to each column or row.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Axis along which the function is applied:

            * 0 or 'index': apply function to each column.
            * 1 or 'columns': apply function to each row.

        raw : bool, default False
            Determines if row or column is passed as a Series or ndarray object:

            * ``False`` : passes each row or column as a Series to the
              function.
            * ``True`` : the passed function will receive ndarray objects
              instead.
              If you are just applying a NumPy reduction function this will
              achieve much better performance.

        result_type : {'expand', 'reduce', 'broadcast', None}, default None
            These only act when ``axis=1`` (columns):

            * 'expand' : list-like results will be turned into columns.
            * 'reduce' : returns a Series if possible rather than expanding
              list-like results. This is the opposite of 'expand'.
            * 'broadcast' : results will be broadcast to the original shape
              of the DataFrame, the original index and columns will be
              retained.

            The default behaviour (None) depends on the return value of the
            applied function: list-like results will be returned as a Series
            of those. However if the apply function returns a Series these
            are expanded to columns.
        args : tuple
            Positional arguments to pass to `func` in addition to the
            array/series.
        **kwargs
            Additional keyword arguments to pass as keywords arguments to
            `func`.

        Returns
        -------
        Series or DataFrame
            Result of applying ``func`` along the given axis of the
            DataFrame.

        See Also
        --------
        DataFrame.applymap: For elementwise operations.
        DataFrame.aggregate: Only perform aggregating type operations.
        DataFrame.transform: Only perform transforming type operations.

        Notes
        -----
        Functions that mutate the passed object can produce unexpected
        behavior or errors and are not supported. See :ref:`gotchas.udf-mutation`
        for more details.

        Examples
        --------
        >>> df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
        >>> df
           A  B
        0  4  9
        1  4  9
        2  4  9

        Using a numpy universal function (in this case the same as
        ``np.sqrt(df)``):

        >>> df.apply(np.sqrt)
             A    B
        0  2.0  3.0
        1  2.0  3.0
        2  2.0  3.0

        Using a reducing function on either axis

        >>> df.apply(np.sum, axis=0)
        A    12
        B    27
        dtype: int64

        >>> df.apply(np.sum, axis=1)
        0    13
        1    13
        2    13
        dtype: int64

        Returning a list-like will result in a Series

        >>> df.apply(lambda x: [1, 2], axis=1)
        0    [1, 2]
        1    [1, 2]
        2    [1, 2]
        dtype: object

        Passing ``result_type='expand'`` will expand list-like results
        to columns of a Dataframe

        >>> df.apply(lambda x: [1, 2], axis=1, result_type='expand')
           0  1
        0  1  2
        1  1  2
        2  1  2

        Returning a Series inside the function is similar to passing
        ``result_type='expand'``. The resulting column names
        will be the Series index.

        >>> df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)
           foo  bar
        0    1    2
        1    1    2
        2    1    2

        Passing ``result_type='broadcast'`` will ensure the same shape
        result, whether list-like or scalar is returned by the function,
        and broadcast it along the axis. The resulting column names will
        be the originals.

        >>> df.apply(lambda x: [1, 2], axis=1, result_type='broadcast')
           A  B
        0  1  2
        1  1  2
        2  1  2
        """
    def applymap(self, func: PythonFuncType, na_action: str | None = None, **kwargs) -> DataFrame:
        """
        Apply a function to a Dataframe elementwise.

        This method applies a function that accepts and returns a scalar
        to every element of a DataFrame.

        Parameters
        ----------
        func : callable
            Python function, returns a single value from a single value.
        na_action : {None, 'ignore'}, default None
            If ‘ignore’, propagate NaN values, without passing them to func.

            .. versionadded:: 1.2

        **kwargs
            Additional keyword arguments to pass as keywords arguments to
            `func`.

            .. versionadded:: 1.3.0

        Returns
        -------
        DataFrame
            Transformed DataFrame.

        See Also
        --------
        DataFrame.apply : Apply a function along input axis of DataFrame.

        Examples
        --------
        >>> df = pd.DataFrame([[1, 2.12], [3.356, 4.567]])
        >>> df
               0      1
        0  1.000  2.120
        1  3.356  4.567

        >>> df.applymap(lambda x: len(str(x)))
           0  1
        0  3  4
        1  5  5

        Like Series.map, NA values can be ignored:

        >>> df_copy = df.copy()
        >>> df_copy.iloc[0, 0] = pd.NA
        >>> df_copy.applymap(lambda x: len(str(x)), na_action='ignore')
             0  1
        0  NaN  4
        1  5.0  5

        Note that a vectorized version of `func` often exists, which will
        be much faster. You could square each number elementwise.

        >>> df.applymap(lambda x: x**2)
                   0          1
        0   1.000000   4.494400
        1  11.262736  20.857489

        But it's better to avoid applymap in that case.

        >>> df ** 2
                   0          1
        0   1.000000   4.494400
        1  11.262736  20.857489
        """
    def join(self, other: DataFrame | Series | Iterable[DataFrame | Series], on: IndexLabel | None = None, how: MergeHow = 'left', lsuffix: str = '', rsuffix: str = '', sort: bool = False, validate: str | None = None) -> DataFrame:
        '''
        Join columns of another DataFrame.

        Join columns with `other` DataFrame either on index or on a key
        column. Efficiently join multiple DataFrame objects by index at once by
        passing a list.

        Parameters
        ----------
        other : DataFrame, Series, or a list containing any combination of them
            Index should be similar to one of the columns in this one. If a
            Series is passed, its name attribute must be set, and that will be
            used as the column name in the resulting joined DataFrame.
        on : str, list of str, or array-like, optional
            Column or index level name(s) in the caller to join on the index
            in `other`, otherwise joins index-on-index. If multiple
            values given, the `other` DataFrame must have a MultiIndex. Can
            pass an array as the join key if it is not already contained in
            the calling DataFrame. Like an Excel VLOOKUP operation.
        how : {\'left\', \'right\', \'outer\', \'inner\', \'cross\'}, default \'left\'
            How to handle the operation of the two objects.

            * left: use calling frame\'s index (or column if on is specified)
            * right: use `other`\'s index.
            * outer: form union of calling frame\'s index (or column if on is
              specified) with `other`\'s index, and sort it.
              lexicographically.
            * inner: form intersection of calling frame\'s index (or column if
              on is specified) with `other`\'s index, preserving the order
              of the calling\'s one.
            * cross: creates the cartesian product from both frames, preserves the order
              of the left keys.

              .. versionadded:: 1.2.0

        lsuffix : str, default \'\'
            Suffix to use from left frame\'s overlapping columns.
        rsuffix : str, default \'\'
            Suffix to use from right frame\'s overlapping columns.
        sort : bool, default False
            Order result DataFrame lexicographically by the join key. If False,
            the order of the join key depends on the join type (how keyword).
        validate : str, optional
            If specified, checks if join is of specified type.
            * "one_to_one" or "1:1": check if join keys are unique in both left
            and right datasets.
            * "one_to_many" or "1:m": check if join keys are unique in left dataset.
            * "many_to_one" or "m:1": check if join keys are unique in right dataset.
            * "many_to_many" or "m:m": allowed, but does not result in checks.
            .. versionadded:: 1.5.0

        Returns
        -------
        DataFrame
            A dataframe containing columns from both the caller and `other`.

        See Also
        --------
        DataFrame.merge : For column(s)-on-column(s) operations.

        Notes
        -----
        Parameters `on`, `lsuffix`, and `rsuffix` are not supported when
        passing a list of `DataFrame` objects.

        Support for specifying index levels as the `on` parameter was added
        in version 0.23.0.

        Examples
        --------
        >>> df = pd.DataFrame({\'key\': [\'K0\', \'K1\', \'K2\', \'K3\', \'K4\', \'K5\'],
        ...                    \'A\': [\'A0\', \'A1\', \'A2\', \'A3\', \'A4\', \'A5\']})

        >>> df
          key   A
        0  K0  A0
        1  K1  A1
        2  K2  A2
        3  K3  A3
        4  K4  A4
        5  K5  A5

        >>> other = pd.DataFrame({\'key\': [\'K0\', \'K1\', \'K2\'],
        ...                       \'B\': [\'B0\', \'B1\', \'B2\']})

        >>> other
          key   B
        0  K0  B0
        1  K1  B1
        2  K2  B2

        Join DataFrames using their indexes.

        >>> df.join(other, lsuffix=\'_caller\', rsuffix=\'_other\')
          key_caller   A key_other    B
        0         K0  A0        K0   B0
        1         K1  A1        K1   B1
        2         K2  A2        K2   B2
        3         K3  A3       NaN  NaN
        4         K4  A4       NaN  NaN
        5         K5  A5       NaN  NaN

        If we want to join using the key columns, we need to set key to be
        the index in both `df` and `other`. The joined DataFrame will have
        key as its index.

        >>> df.set_index(\'key\').join(other.set_index(\'key\'))
              A    B
        key
        K0   A0   B0
        K1   A1   B1
        K2   A2   B2
        K3   A3  NaN
        K4   A4  NaN
        K5   A5  NaN

        Another option to join using the key columns is to use the `on`
        parameter. DataFrame.join always uses `other`\'s index but we can use
        any column in `df`. This method preserves the original DataFrame\'s
        index in the result.

        >>> df.join(other.set_index(\'key\'), on=\'key\')
          key   A    B
        0  K0  A0   B0
        1  K1  A1   B1
        2  K2  A2   B2
        3  K3  A3  NaN
        4  K4  A4  NaN
        5  K5  A5  NaN

        Using non-unique key values shows how they are matched.

        >>> df = pd.DataFrame({\'key\': [\'K0\', \'K1\', \'K1\', \'K3\', \'K0\', \'K1\'],
        ...                    \'A\': [\'A0\', \'A1\', \'A2\', \'A3\', \'A4\', \'A5\']})

        >>> df
          key   A
        0  K0  A0
        1  K1  A1
        2  K1  A2
        3  K3  A3
        4  K0  A4
        5  K1  A5

        >>> df.join(other.set_index(\'key\'), on=\'key\', validate=\'m:1\')
          key   A    B
        0  K0  A0   B0
        1  K1  A1   B1
        2  K1  A2   B1
        3  K3  A3  NaN
        4  K0  A4   B0
        5  K1  A5   B1
        '''
    def merge(self, right: DataFrame | Series, how: MergeHow = 'inner', on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, sort: bool = False, suffixes: Suffixes = ('_x', '_y'), copy: bool | None = None, indicator: str | bool = False, validate: str | None = None) -> DataFrame: ...
    def round(self, decimals: int | dict[IndexLabel, int] | Series = 0, *args, **kwargs) -> DataFrame:
        """
        Round a DataFrame to a variable number of decimal places.

        Parameters
        ----------
        decimals : int, dict, Series
            Number of decimal places to round each column to. If an int is
            given, round each column to the same number of places.
            Otherwise dict and Series round to variable numbers of places.
            Column names should be in the keys if `decimals` is a
            dict-like, or in the index if `decimals` is a Series. Any
            columns not included in `decimals` will be left as is. Elements
            of `decimals` which are not columns of the input will be
            ignored.
        *args
            Additional keywords have no effect but might be accepted for
            compatibility with numpy.
        **kwargs
            Additional keywords have no effect but might be accepted for
            compatibility with numpy.

        Returns
        -------
        DataFrame
            A DataFrame with the affected columns rounded to the specified
            number of decimal places.

        See Also
        --------
        numpy.around : Round a numpy array to the given number of decimals.
        Series.round : Round a Series to the given number of decimals.

        Examples
        --------
        >>> df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)],
        ...                   columns=['dogs', 'cats'])
        >>> df
            dogs  cats
        0  0.21  0.32
        1  0.01  0.67
        2  0.66  0.03
        3  0.21  0.18

        By providing an integer each column is rounded to the same number
        of decimal places

        >>> df.round(1)
            dogs  cats
        0   0.2   0.3
        1   0.0   0.7
        2   0.7   0.0
        3   0.2   0.2

        With a dict, the number of places for specific columns can be
        specified with the column names as key and the number of decimal
        places as value

        >>> df.round({'dogs': 1, 'cats': 0})
            dogs  cats
        0   0.2   0.0
        1   0.0   1.0
        2   0.7   0.0
        3   0.2   0.0

        Using a Series, the number of places for specific columns can be
        specified with the column names as index and the number of
        decimal places as value

        >>> decimals = pd.Series([0, 1], index=['cats', 'dogs'])
        >>> df.round(decimals)
            dogs  cats
        0   0.2   0.0
        1   0.0   1.0
        2   0.7   0.0
        3   0.2   0.0
        """
    def corr(self, method: CorrelationMethod = 'pearson', min_periods: int = 1, numeric_only: bool = False) -> DataFrame:
        """
        Compute pairwise correlation of columns, excluding NA/null values.

        Parameters
        ----------
        method : {'pearson', 'kendall', 'spearman'} or callable
            Method of correlation:

            * pearson : standard correlation coefficient
            * kendall : Kendall Tau correlation coefficient
            * spearman : Spearman rank correlation
            * callable: callable with input two 1d ndarrays
                and returning a float. Note that the returned matrix from corr
                will have 1 along the diagonals and will be symmetric
                regardless of the callable's behavior.
        min_periods : int, optional
            Minimum number of observations required per pair of columns
            to have a valid result. Currently only available for Pearson
            and Spearman correlation.
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

            .. versionchanged:: 2.0.0
                The default value of ``numeric_only`` is now ``False``.

        Returns
        -------
        DataFrame
            Correlation matrix.

        See Also
        --------
        DataFrame.corrwith : Compute pairwise correlation with another
            DataFrame or Series.
        Series.corr : Compute the correlation between two Series.

        Notes
        -----
        Pearson, Kendall and Spearman correlation are currently computed using pairwise complete observations.

        * `Pearson correlation coefficient <https://en.wikipedia.org/wiki/Pearson_correlation_coefficient>`_
        * `Kendall rank correlation coefficient <https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient>`_
        * `Spearman's rank correlation coefficient <https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient>`_

        Examples
        --------
        >>> def histogram_intersection(a, b):
        ...     v = np.minimum(a, b).sum().round(decimals=1)
        ...     return v
        >>> df = pd.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'])
        >>> df.corr(method=histogram_intersection)
              dogs  cats
        dogs   1.0   0.3
        cats   0.3   1.0

        >>> df = pd.DataFrame([(1, 1), (2, np.nan), (np.nan, 3), (4, 4)],
        ...                   columns=['dogs', 'cats'])
        >>> df.corr(min_periods=3)
              dogs  cats
        dogs   1.0   NaN
        cats   NaN   1.0
        """
    def cov(self, min_periods: int | None = None, ddof: int | None = 1, numeric_only: bool = False) -> DataFrame:
        """
        Compute pairwise covariance of columns, excluding NA/null values.

        Compute the pairwise covariance among the series of a DataFrame.
        The returned data frame is the `covariance matrix
        <https://en.wikipedia.org/wiki/Covariance_matrix>`__ of the columns
        of the DataFrame.

        Both NA and null values are automatically excluded from the
        calculation. (See the note below about bias from missing values.)
        A threshold can be set for the minimum number of
        observations for each value created. Comparisons with observations
        below this threshold will be returned as ``NaN``.

        This method is generally used for the analysis of time series data to
        understand the relationship between different measures
        across time.

        Parameters
        ----------
        min_periods : int, optional
            Minimum number of observations required per pair of columns
            to have a valid result.

        ddof : int, default 1
            Delta degrees of freedom.  The divisor used in calculations
            is ``N - ddof``, where ``N`` represents the number of elements.

            .. versionadded:: 1.1.0

        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

            .. versionchanged:: 2.0.0
                The default value of ``numeric_only`` is now ``False``.

        Returns
        -------
        DataFrame
            The covariance matrix of the series of the DataFrame.

        See Also
        --------
        Series.cov : Compute covariance with another Series.
        core.window.ewm.ExponentialMovingWindow.cov : Exponential weighted sample
            covariance.
        core.window.expanding.Expanding.cov : Expanding sample covariance.
        core.window.rolling.Rolling.cov : Rolling sample covariance.

        Notes
        -----
        Returns the covariance matrix of the DataFrame's time series.
        The covariance is normalized by N-ddof.

        For DataFrames that have Series that are missing data (assuming that
        data is `missing at random
        <https://en.wikipedia.org/wiki/Missing_data#Missing_at_random>`__)
        the returned covariance matrix will be an unbiased estimate
        of the variance and covariance between the member Series.

        However, for many applications this estimate may not be acceptable
        because the estimate covariance matrix is not guaranteed to be positive
        semi-definite. This could lead to estimate correlations having
        absolute values which are greater than one, and/or a non-invertible
        covariance matrix. See `Estimation of covariance matrices
        <https://en.wikipedia.org/w/index.php?title=Estimation_of_covariance_
        matrices>`__ for more details.

        Examples
        --------
        >>> df = pd.DataFrame([(1, 2), (0, 3), (2, 0), (1, 1)],
        ...                   columns=['dogs', 'cats'])
        >>> df.cov()
                  dogs      cats
        dogs  0.666667 -1.000000
        cats -1.000000  1.666667

        >>> np.random.seed(42)
        >>> df = pd.DataFrame(np.random.randn(1000, 5),
        ...                   columns=['a', 'b', 'c', 'd', 'e'])
        >>> df.cov()
                  a         b         c         d         e
        a  0.998438 -0.020161  0.059277 -0.008943  0.014144
        b -0.020161  1.059352 -0.008543 -0.024738  0.009826
        c  0.059277 -0.008543  1.010670 -0.001486 -0.000271
        d -0.008943 -0.024738 -0.001486  0.921297 -0.013692
        e  0.014144  0.009826 -0.000271 -0.013692  0.977795

        **Minimum number of periods**

        This method also supports an optional ``min_periods`` keyword
        that specifies the required minimum number of non-NA observations for
        each column pair in order to have a valid result:

        >>> np.random.seed(42)
        >>> df = pd.DataFrame(np.random.randn(20, 3),
        ...                   columns=['a', 'b', 'c'])
        >>> df.loc[df.index[:5], 'a'] = np.nan
        >>> df.loc[df.index[5:10], 'b'] = np.nan
        >>> df.cov(min_periods=12)
                  a         b         c
        a  0.316741       NaN -0.150812
        b       NaN  1.248003  0.191417
        c -0.150812  0.191417  0.895202
        """
    def corrwith(self, other: DataFrame | Series, axis: Axis = 0, drop: bool = False, method: CorrelationMethod = 'pearson', numeric_only: bool = False) -> Series:
        '''
        Compute pairwise correlation.

        Pairwise correlation is computed between rows or columns of
        DataFrame with rows or columns of Series or DataFrame. DataFrames
        are first aligned along both axes before computing the
        correlations.

        Parameters
        ----------
        other : DataFrame, Series
            Object with which to compute correlations.
        axis : {0 or \'index\', 1 or \'columns\'}, default 0
            The axis to use. 0 or \'index\' to compute row-wise, 1 or \'columns\' for
            column-wise.
        drop : bool, default False
            Drop missing indices from result.
        method : {\'pearson\', \'kendall\', \'spearman\'} or callable
            Method of correlation:

            * pearson : standard correlation coefficient
            * kendall : Kendall Tau correlation coefficient
            * spearman : Spearman rank correlation
            * callable: callable with input two 1d ndarrays
                and returning a float.

        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

            .. versionchanged:: 2.0.0
                The default value of ``numeric_only`` is now ``False``.

        Returns
        -------
        Series
            Pairwise correlations.

        See Also
        --------
        DataFrame.corr : Compute pairwise correlation of columns.

        Examples
        --------
        >>> index = ["a", "b", "c", "d", "e"]
        >>> columns = ["one", "two", "three", "four"]
        >>> df1 = pd.DataFrame(np.arange(20).reshape(5, 4), index=index, columns=columns)
        >>> df2 = pd.DataFrame(np.arange(16).reshape(4, 4), index=index[:4], columns=columns)
        >>> df1.corrwith(df2)
        one      1.0
        two      1.0
        three    1.0
        four     1.0
        dtype: float64

        >>> df2.corrwith(df1, axis=1)
        a    1.0
        b    1.0
        c    1.0
        d    1.0
        e    NaN
        dtype: float64
        '''
    def count(self, axis: Axis = 0, numeric_only: bool = False):
        '''
        Count non-NA cells for each column or row.

        The values `None`, `NaN`, `NaT`, and optionally `numpy.inf` (depending
        on `pandas.options.mode.use_inf_as_na`) are considered NA.

        Parameters
        ----------
        axis : {0 or \'index\', 1 or \'columns\'}, default 0
            If 0 or \'index\' counts are generated for each column.
            If 1 or \'columns\' counts are generated for each row.
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

        Returns
        -------
        Series or DataFrame
            For each column/row the number of non-NA/null entries.
            If `level` is specified returns a `DataFrame`.

        See Also
        --------
        Series.count: Number of non-NA elements in a Series.
        DataFrame.value_counts: Count unique combinations of columns.
        DataFrame.shape: Number of DataFrame rows and columns (including NA
            elements).
        DataFrame.isna: Boolean same-sized DataFrame showing places of NA
            elements.

        Examples
        --------
        Constructing DataFrame from a dictionary:

        >>> df = pd.DataFrame({"Person":
        ...                    ["John", "Myla", "Lewis", "John", "Myla"],
        ...                    "Age": [24., np.nan, 21., 33, 26],
        ...                    "Single": [False, True, True, True, False]})
        >>> df
           Person   Age  Single
        0    John  24.0   False
        1    Myla   NaN    True
        2   Lewis  21.0    True
        3    John  33.0    True
        4    Myla  26.0   False

        Notice the uncounted NA values:

        >>> df.count()
        Person    5
        Age       4
        Single    5
        dtype: int64

        Counts for each **row**:

        >>> df.count(axis=\'columns\')
        0    3
        1    2
        2    3
        3    3
        4    3
        dtype: int64
        '''
    def nunique(self, axis: Axis = 0, dropna: bool = True) -> Series:
        """
        Count number of distinct elements in specified axis.

        Return Series with number of distinct elements. Can ignore NaN
        values.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis to use. 0 or 'index' for row-wise, 1 or 'columns' for
            column-wise.
        dropna : bool, default True
            Don't include NaN in the counts.

        Returns
        -------
        Series

        See Also
        --------
        Series.nunique: Method nunique for Series.
        DataFrame.count: Count non-NA cells for each column or row.

        Examples
        --------
        >>> df = pd.DataFrame({'A': [4, 5, 6], 'B': [4, 1, 1]})
        >>> df.nunique()
        A    3
        B    2
        dtype: int64

        >>> df.nunique(axis=1)
        0    1
        1    2
        2    2
        dtype: int64
        """
    def idxmin(self, axis: Axis = 0, skipna: bool = True, numeric_only: bool = False) -> Series: ...
    def idxmax(self, axis: Axis = 0, skipna: bool = True, numeric_only: bool = False) -> Series: ...
    def mode(self, axis: Axis = 0, numeric_only: bool = False, dropna: bool = True) -> DataFrame:
        """
        Get the mode(s) of each element along the selected axis.

        The mode of a set of values is the value that appears most often.
        It can be multiple values.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis to iterate over while searching for the mode:

            * 0 or 'index' : get mode of each column
            * 1 or 'columns' : get mode of each row.

        numeric_only : bool, default False
            If True, only apply to numeric columns.
        dropna : bool, default True
            Don't consider counts of NaN/NaT.

        Returns
        -------
        DataFrame
            The modes of each column or row.

        See Also
        --------
        Series.mode : Return the highest frequency value in a Series.
        Series.value_counts : Return the counts of values in a Series.

        Examples
        --------
        >>> df = pd.DataFrame([('bird', 2, 2),
        ...                    ('mammal', 4, np.nan),
        ...                    ('arthropod', 8, 0),
        ...                    ('bird', 2, np.nan)],
        ...                   index=('falcon', 'horse', 'spider', 'ostrich'),
        ...                   columns=('species', 'legs', 'wings'))
        >>> df
                   species  legs  wings
        falcon        bird     2    2.0
        horse       mammal     4    NaN
        spider   arthropod     8    0.0
        ostrich       bird     2    NaN

        By default, missing values are not considered, and the mode of wings
        are both 0 and 2. Because the resulting DataFrame has two rows,
        the second row of ``species`` and ``legs`` contains ``NaN``.

        >>> df.mode()
          species  legs  wings
        0    bird   2.0    0.0
        1     NaN   NaN    2.0

        Setting ``dropna=False`` ``NaN`` values are considered and they can be
        the mode (like for wings).

        >>> df.mode(dropna=False)
          species  legs  wings
        0    bird     2    NaN

        Setting ``numeric_only=True``, only the mode of numeric columns is
        computed, and columns of other types are ignored.

        >>> df.mode(numeric_only=True)
           legs  wings
        0   2.0    0.0
        1   NaN    2.0

        To compute the mode over columns and not rows, use the axis parameter:

        >>> df.mode(axis='columns', numeric_only=True)
                   0    1
        falcon   2.0  NaN
        horse    4.0  NaN
        spider   0.0  8.0
        ostrich  2.0  NaN
        """
    @overload
    def quantile(self, q: float = ..., axis: Axis = ..., numeric_only: bool = ..., interpolation: QuantileInterpolation = ...) -> Series: ...
    @overload
    def quantile(self, q: AnyArrayLike | Sequence[float], axis: Axis = ..., numeric_only: bool = ..., interpolation: QuantileInterpolation = ...) -> Series | DataFrame: ...
    @overload
    def quantile(self, q: float | AnyArrayLike | Sequence[float] = ..., axis: Axis = ..., numeric_only: bool = ..., interpolation: QuantileInterpolation = ...) -> Series | DataFrame: ...
    def asfreq(self, freq: Frequency, method: FillnaOptions | None = None, how: str | None = None, normalize: bool = False, fill_value: Hashable = None) -> DataFrame: ...
    def resample(self, rule, axis: Axis = 0, closed: str | None = None, label: str | None = None, convention: str = 'start', kind: str | None = None, on: Level = None, level: Level = None, origin: str | TimestampConvertibleTypes = 'start_day', offset: TimedeltaConvertibleTypes | None = None, group_keys: bool = False) -> Resampler: ...
    def to_timestamp(self, freq: Frequency | None = None, how: str = 'start', axis: Axis = 0, copy: bool | None = None) -> DataFrame:
        """
        Cast to DatetimeIndex of timestamps, at *beginning* of period.

        Parameters
        ----------
        freq : str, default frequency of PeriodIndex
            Desired frequency.
        how : {'s', 'e', 'start', 'end'}
            Convention for converting period to timestamp; start of period
            vs. end.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis to convert (the index by default).
        copy : bool, default True
            If False then underlying input data is not copied.

        Returns
        -------
        DataFrame
            The DataFrame has a DatetimeIndex.

        Examples
        --------
        >>> idx = pd.PeriodIndex(['2023', '2024'], freq='Y')
        >>> d = {'col1': [1, 2], 'col2': [3, 4]}
        >>> df1 = pd.DataFrame(data=d, index=idx)
        >>> df1
              col1   col2
        2023     1      3
        2024\t 2      4

        The resulting timestamps will be at the beginning of the year in this case

        >>> df1 = df1.to_timestamp()
        >>> df1
                    col1   col2
        2023-01-01     1      3
        2024-01-01     2      4
        >>> df1.index
        DatetimeIndex(['2023-01-01', '2024-01-01'], dtype='datetime64[ns]', freq=None)

        Using `freq` which is the offset that the Timestamps will have

        >>> df2 = pd.DataFrame(data=d, index=idx)
        >>> df2 = df2.to_timestamp(freq='M')
        >>> df2
                    col1   col2
        2023-01-31     1      3
        2024-01-31     2      4
        >>> df2.index
        DatetimeIndex(['2023-01-31', '2024-01-31'], dtype='datetime64[ns]', freq=None)
        """
    def to_period(self, freq: Frequency | None = None, axis: Axis = 0, copy: bool | None = None) -> DataFrame:
        '''
        Convert DataFrame from DatetimeIndex to PeriodIndex.

        Convert DataFrame from DatetimeIndex to PeriodIndex with desired
        frequency (inferred from index if not passed).

        Parameters
        ----------
        freq : str, default
            Frequency of the PeriodIndex.
        axis : {0 or \'index\', 1 or \'columns\'}, default 0
            The axis to convert (the index by default).
        copy : bool, default True
            If False then underlying input data is not copied.

        Returns
        -------
        DataFrame
            The DataFrame has a PeriodIndex.

        Examples
        --------
        >>> idx = pd.to_datetime(
        ...     [
        ...         "2001-03-31 00:00:00",
        ...         "2002-05-31 00:00:00",
        ...         "2003-08-31 00:00:00",
        ...     ]
        ... )

        >>> idx
        DatetimeIndex([\'2001-03-31\', \'2002-05-31\', \'2003-08-31\'],
        dtype=\'datetime64[ns]\', freq=None)

        >>> idx.to_period("M")
        PeriodIndex([\'2001-03\', \'2002-05\', \'2003-08\'], dtype=\'period[M]\')

        For the yearly frequency

        >>> idx.to_period("Y")
        PeriodIndex([\'2001\', \'2002\', \'2003\'], dtype=\'period[A-DEC]\')
        '''
    def isin(self, values: Series | DataFrame | Sequence | Mapping) -> DataFrame:
        """
        Whether each element in the DataFrame is contained in values.

        Parameters
        ----------
        values : iterable, Series, DataFrame or dict
            The result will only be true at a location if all the
            labels match. If `values` is a Series, that's the index. If
            `values` is a dict, the keys must be the column names,
            which must match. If `values` is a DataFrame,
            then both the index and column labels must match.

        Returns
        -------
        DataFrame
            DataFrame of booleans showing whether each element in the DataFrame
            is contained in values.

        See Also
        --------
        DataFrame.eq: Equality test for DataFrame.
        Series.isin: Equivalent method on Series.
        Series.str.contains: Test if pattern or regex is contained within a
            string of a Series or Index.

        Examples
        --------
        >>> df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
        ...                   index=['falcon', 'dog'])
        >>> df
                num_legs  num_wings
        falcon         2          2
        dog            4          0

        When ``values`` is a list check whether every value in the DataFrame
        is present in the list (which animals have 0 or 2 legs or wings)

        >>> df.isin([0, 2])
                num_legs  num_wings
        falcon      True       True
        dog        False       True

        To check if ``values`` is *not* in the DataFrame, use the ``~`` operator:

        >>> ~df.isin([0, 2])
                num_legs  num_wings
        falcon     False      False
        dog         True      False

        When ``values`` is a dict, we can pass values to check for each
        column separately:

        >>> df.isin({'num_wings': [0, 3]})
                num_legs  num_wings
        falcon     False      False
        dog        False       True

        When ``values`` is a Series or DataFrame the index and column must
        match. Note that 'falcon' does not match based on the number of legs
        in other.

        >>> other = pd.DataFrame({'num_legs': [8, 3], 'num_wings': [0, 2]},
        ...                      index=['spider', 'falcon'])
        >>> df.isin(other)
                num_legs  num_wings
        falcon     False       True
        dog        False      False
        """
    index: Incomplete
    columns: Incomplete
    plot: Incomplete
    hist: Incomplete
    boxplot: Incomplete
    sparse: Incomplete
    @property
    def values(self) -> np.ndarray:
        """
        Return a Numpy representation of the DataFrame.

        .. warning::

           We recommend using :meth:`DataFrame.to_numpy` instead.

        Only the values in the DataFrame will be returned, the axes labels
        will be removed.

        Returns
        -------
        numpy.ndarray
            The values of the DataFrame.

        See Also
        --------
        DataFrame.to_numpy : Recommended alternative to this method.
        DataFrame.index : Retrieve the index labels.
        DataFrame.columns : Retrieving the column names.

        Notes
        -----
        The dtype will be a lower-common-denominator dtype (implicit
        upcasting); that is to say if the dtypes (even of numeric types)
        are mixed, the one that accommodates all will be chosen. Use this
        with care if you are not dealing with the blocks.

        e.g. If the dtypes are float16 and float32, dtype will be upcast to
        float32.  If dtypes are int32 and uint8, dtype will be upcast to
        int32. By :func:`numpy.find_common_type` convention, mixing int64
        and uint64 will result in a float64 dtype.

        Examples
        --------
        A DataFrame where all columns are the same type (e.g., int64) results
        in an array of the same type.

        >>> df = pd.DataFrame({'age':    [ 3,  29],
        ...                    'height': [94, 170],
        ...                    'weight': [31, 115]})
        >>> df
           age  height  weight
        0    3      94      31
        1   29     170     115
        >>> df.dtypes
        age       int64
        height    int64
        weight    int64
        dtype: object
        >>> df.values
        array([[  3,  94,  31],
               [ 29, 170, 115]])

        A DataFrame with mixed type columns(e.g., str/object, int64, float32)
        results in an ndarray of the broadest type that accommodates these
        mixed types (e.g., object).

        >>> df2 = pd.DataFrame([('parrot',   24.0, 'second'),
        ...                     ('lion',     80.5, 1),
        ...                     ('monkey', np.nan, None)],
        ...                   columns=('name', 'max_speed', 'rank'))
        >>> df2.dtypes
        name          object
        max_speed    float64
        rank          object
        dtype: object
        >>> df2.values
        array([['parrot', 24.0, 'second'],
               ['lion', 80.5, 1],
               ['monkey', nan, None]], dtype=object)
        """
    @overload
    def ffill(self, *, axis: None | Axis = ..., inplace: Literal[False] = ..., limit: None | int = ..., downcast: dict | None = ...) -> DataFrame: ...
    @overload
    def ffill(self, *, axis: None | Axis = ..., inplace: Literal[True], limit: None | int = ..., downcast: dict | None = ...) -> None: ...
    @overload
    def ffill(self, *, axis: None | Axis = ..., inplace: bool = ..., limit: None | int = ..., downcast: dict | None = ...) -> DataFrame | None: ...
    @overload
    def bfill(self, *, axis: None | Axis = ..., inplace: Literal[False] = ..., limit: None | int = ..., downcast=...) -> DataFrame: ...
    @overload
    def bfill(self, *, axis: None | Axis = ..., inplace: Literal[True], limit: None | int = ..., downcast=...) -> None: ...
    @overload
    def bfill(self, *, axis: None | Axis = ..., inplace: bool = ..., limit: None | int = ..., downcast=...) -> DataFrame | None: ...
    def clip(self, lower: float | None = None, upper: float | None = None, *, axis: Axis | None = None, inplace: bool = False, **kwargs) -> DataFrame | None: ...
    def interpolate(self, method: str = 'linear', *, axis: Axis = 0, limit: int | None = None, inplace: bool = False, limit_direction: str | None = None, limit_area: str | None = None, downcast: str | None = None, **kwargs) -> DataFrame | None: ...
    @overload
    def where(self, cond, other=..., *, inplace: Literal[False] = ..., axis: Axis | None = ..., level: Level = ...) -> DataFrame: ...
    @overload
    def where(self, cond, other=..., *, inplace: Literal[True], axis: Axis | None = ..., level: Level = ...) -> None: ...
    @overload
    def where(self, cond, other=..., *, inplace: bool = ..., axis: Axis | None = ..., level: Level = ...) -> DataFrame | None: ...
    @overload
    def mask(self, cond, other=..., *, inplace: Literal[False] = ..., axis: Axis | None = ..., level: Level = ...) -> DataFrame: ...
    @overload
    def mask(self, cond, other=..., *, inplace: Literal[True], axis: Axis | None = ..., level: Level = ...) -> None: ...
    @overload
    def mask(self, cond, other=..., *, inplace: bool = ..., axis: Axis | None = ..., level: Level = ...) -> DataFrame | None: ...
