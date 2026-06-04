import pandas as pd
from _typeshed import Incomplete
from pandas.api.types import CategoricalDtype as CategoricalDtype
from pyspark._globals import _NoValueType
from pyspark.pandas._typing import Label as Label
from pyspark.pandas.data_type_ops.base import DataTypeOps as DataTypeOps
from pyspark.pandas.series import Series as Series
from pyspark.pandas.spark.utils import as_nullable_spark_type as as_nullable_spark_type, force_decimal_precision_scale as force_decimal_precision_scale
from pyspark.pandas.typedef import Dtype as Dtype, as_spark_type as as_spark_type, extension_dtypes as extension_dtypes, infer_pd_series_spark_type as infer_pd_series_spark_type, spark_type_to_pandas_dtype as spark_type_to_pandas_dtype
from pyspark.pandas.utils import column_labels_level as column_labels_level, default_session as default_session, is_name_like_tuple as is_name_like_tuple, is_testing as is_testing, lazy_property as lazy_property, name_like_string as name_like_string, scol_for as scol_for, spark_column_equals as spark_column_equals
from pyspark.sql import Column as Column, DataFrame as SparkDataFrame, Window as Window
from pyspark.sql.types import BooleanType as BooleanType, DataType as DataType, LongType as LongType, StringType as StringType, StructField as StructField, StructType as StructType
from pyspark.sql.utils import is_timestamp_ntz_preferred as is_timestamp_ntz_preferred
from typing import Any, Dict, List, Sequence, Tuple

SPARK_INDEX_NAME_FORMAT: Incomplete
SPARK_DEFAULT_INDEX_NAME: Incomplete
SPARK_INDEX_NAME_PATTERN: Incomplete
NATURAL_ORDER_COLUMN_NAME: str
HIDDEN_COLUMNS: Incomplete
DEFAULT_SERIES_NAME: int
SPARK_DEFAULT_SERIES_NAME: Incomplete

class InternalField:
    """
    The internal field to store the dtype as well as the Spark's StructField optionally.

    Parameters
    ----------
    dtype : numpy.dtype or pandas' ExtensionDtype
        The dtype for the field
    struct_field : StructField, optional
        The `StructField` for the field. If None, InternalFrame will properly set.
    """
    def __init__(self, dtype: Dtype, struct_field: StructField | None = None) -> None: ...
    @staticmethod
    def from_struct_field(struct_field: StructField, *, use_extension_dtypes: bool = False) -> InternalField:
        """
        Returns a new InternalField object created from the given StructField.

        The dtype will be inferred from the data type of the given StructField.

        Parameters
        ----------
        struct_field : StructField
            The StructField used to create a new InternalField object.
        use_extension_dtypes : bool
            If True, try to use the extension dtypes.

        Returns
        -------
        InternalField
        """
    @property
    def dtype(self) -> Dtype:
        """Return the dtype for the field."""
    @property
    def struct_field(self) -> StructField | None:
        """Return the StructField for the field."""
    @property
    def name(self) -> str:
        """Return the field name if the StructField exists."""
    @property
    def spark_type(self) -> DataType:
        """Return the spark data type for the field if the StructField exists."""
    @property
    def nullable(self) -> bool:
        """Return the nullability for the field if the StructField exists."""
    @property
    def metadata(self) -> Dict[str, Any]:
        """Return the metadata for the field if the StructField exists."""
    @property
    def is_extension_dtype(self) -> bool:
        """Return whether the dtype for the field is an extension type or not."""
    def normalize_spark_type(self) -> InternalField:
        """Return a new InternalField object with normalized Spark data type."""
    def copy(self, *, name: str | _NoValueType = ..., dtype: Dtype | _NoValueType = ..., spark_type: DataType | _NoValueType = ..., nullable: bool | _NoValueType = ..., metadata: Dict[str, Any] | None | _NoValueType = ...) -> InternalField:
        """Copy the InternalField object."""
    def __eq__(self, other: Any) -> bool: ...

class InternalFrame:
    '''
    The internal immutable DataFrame which manages Spark DataFrame and column names and index
    information.

    .. note:: this is an internal class. It is not supposed to be exposed to users and users
        should not directly access to it.

    The internal immutable DataFrame represents the index information for a DataFrame it belongs to.
    For instance, if we have a pandas-on-Spark DataFrame as below, pandas DataFrame does not
    store the index as columns.

    >>> psdf = ps.DataFrame({
    ...     \'A\': [1, 2, 3, 4],
    ...     \'B\': [5, 6, 7, 8],
    ...     \'C\': [9, 10, 11, 12],
    ...     \'D\': [13, 14, 15, 16],
    ...     \'E\': [17, 18, 19, 20]}, columns = [\'A\', \'B\', \'C\', \'D\', \'E\'])
    >>> psdf  # doctest: +NORMALIZE_WHITESPACE
       A  B   C   D   E
    0  1  5   9  13  17
    1  2  6  10  14  18
    2  3  7  11  15  19
    3  4  8  12  16  20

    However, all columns including index column are also stored in Spark DataFrame internally
    as below.

    >>> psdf._internal.to_internal_spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE
    +-----------------+---+---+---+---+---+
    |__index_level_0__|  A|  B|  C|  D|  E|
    +-----------------+---+---+---+---+---+
    |                0|  1|  5|  9| 13| 17|
    |                1|  2|  6| 10| 14| 18|
    |                2|  3|  7| 11| 15| 19|
    |                3|  4|  8| 12| 16| 20|
    +-----------------+---+---+---+---+---+

    To fill this gap, the current metadata is used by mapping Spark\'s internal column
    to pandas-on-Spark\'s index. See the method below:

    * `spark_frame` represents the internal Spark DataFrame

    * `data_spark_column_names` represents non-indexing Spark column names

    * `data_spark_columns` represents non-indexing Spark columns

    * `data_fields` represents non-indexing InternalFields

    * `index_spark_column_names` represents internal index Spark column names

    * `index_spark_columns` represents internal index Spark columns

    * `index_fields` represents index InternalFields

    * `spark_column_names` represents all columns

    * `index_names` represents the external index name as a label

    * `to_internal_spark_frame` represents Spark DataFrame derived by the metadata. Includes index.

    * `to_pandas_frame` represents pandas DataFrame derived by the metadata

    >>> internal = psdf._internal
    >>> internal.spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    +-----------------+---+---+---+---+---+-----------------+
    |__index_level_0__|  A|  B|  C|  D|  E|__natural_order__|
    +-----------------+---+---+---+---+---+-----------------+
    |                0|  1|  5|  9| 13| 17|              ...|
    |                1|  2|  6| 10| 14| 18|              ...|
    |                2|  3|  7| 11| 15| 19|              ...|
    |                3|  4|  8| 12| 16| 20|              ...|
    +-----------------+---+---+---+---+---+-----------------+
    >>> internal.data_spark_column_names
    [\'A\', \'B\', \'C\', \'D\', \'E\']
    >>> internal.index_spark_column_names
    [\'__index_level_0__\']
    >>> internal.spark_column_names
    [\'__index_level_0__\', \'A\', \'B\', \'C\', \'D\', \'E\']
    >>> internal.index_names
    [None]
    >>> internal.data_fields    # doctest: +NORMALIZE_WHITESPACE
    [InternalField(dtype=int64, struct_field=StructField(\'A\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'B\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'C\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'D\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'E\', LongType(), False))]
    >>> internal.index_fields
    [InternalField(dtype=int64, struct_field=StructField(\'__index_level_0__\', LongType(), False))]
    >>> internal.to_internal_spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE
    +-----------------+---+---+---+---+---+
    |__index_level_0__|  A|  B|  C|  D|  E|
    +-----------------+---+---+---+---+---+
    |                0|  1|  5|  9| 13| 17|
    |                1|  2|  6| 10| 14| 18|
    |                2|  3|  7| 11| 15| 19|
    |                3|  4|  8| 12| 16| 20|
    +-----------------+---+---+---+---+---+
    >>> internal.to_pandas_frame
       A  B   C   D   E
    0  1  5   9  13  17
    1  2  6  10  14  18
    2  3  7  11  15  19
    3  4  8  12  16  20

    In case that index is set to one of the existing columns as below:

    >>> psdf1 = psdf.set_index("A")
    >>> psdf1  # doctest: +NORMALIZE_WHITESPACE
       B   C   D   E
    A
    1  5   9  13  17
    2  6  10  14  18
    3  7  11  15  19
    4  8  12  16  20

    >>> psdf1._internal.to_internal_spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE
    +---+---+---+---+---+
    |  A|  B|  C|  D|  E|
    +---+---+---+---+---+
    |  1|  5|  9| 13| 17|
    |  2|  6| 10| 14| 18|
    |  3|  7| 11| 15| 19|
    |  4|  8| 12| 16| 20|
    +---+---+---+---+---+

    >>> internal = psdf1._internal
    >>> internal.spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    +-----------------+---+---+---+---+---+-----------------+
    |__index_level_0__|  A|  B|  C|  D|  E|__natural_order__|
    +-----------------+---+---+---+---+---+-----------------+
    |                0|  1|  5|  9| 13| 17|              ...|
    |                1|  2|  6| 10| 14| 18|              ...|
    |                2|  3|  7| 11| 15| 19|              ...|
    |                3|  4|  8| 12| 16| 20|              ...|
    +-----------------+---+---+---+---+---+-----------------+
    >>> internal.data_spark_column_names
    [\'B\', \'C\', \'D\', \'E\']
    >>> internal.index_spark_column_names
    [\'A\']
    >>> internal.spark_column_names
    [\'A\', \'B\', \'C\', \'D\', \'E\']
    >>> internal.index_names
    [(\'A\',)]
    >>> internal.data_fields  # doctest: +NORMALIZE_WHITESPACE
    [InternalField(dtype=int64, struct_field=StructField(\'B\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'C\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'D\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'E\', LongType(), False))]
    >>> internal.index_fields
    [InternalField(dtype=int64, struct_field=StructField(\'A\', LongType(), False))]
    >>> internal.to_internal_spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE
    +---+---+---+---+---+
    |  A|  B|  C|  D|  E|
    +---+---+---+---+---+
    |  1|  5|  9| 13| 17|
    |  2|  6| 10| 14| 18|
    |  3|  7| 11| 15| 19|
    |  4|  8| 12| 16| 20|
    +---+---+---+---+---+
    >>> internal.to_pandas_frame  # doctest: +NORMALIZE_WHITESPACE
       B   C   D   E
    A
    1  5   9  13  17
    2  6  10  14  18
    3  7  11  15  19
    4  8  12  16  20

    In case that index becomes a multi index as below:

    >>> psdf2 = psdf.set_index("A", append=True)
    >>> psdf2  # doctest: +NORMALIZE_WHITESPACE
         B   C   D   E
      A
    0 1  5   9  13  17
    1 2  6  10  14  18
    2 3  7  11  15  19
    3 4  8  12  16  20

    >>> psdf2._internal.to_internal_spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE
    +-----------------+---+---+---+---+---+
    |__index_level_0__|  A|  B|  C|  D|  E|
    +-----------------+---+---+---+---+---+
    |                0|  1|  5|  9| 13| 17|
    |                1|  2|  6| 10| 14| 18|
    |                2|  3|  7| 11| 15| 19|
    |                3|  4|  8| 12| 16| 20|
    +-----------------+---+---+---+---+---+

    >>> internal = psdf2._internal
    >>> internal.spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    +-----------------+---+---+---+---+---+-----------------+
    |__index_level_0__|  A|  B|  C|  D|  E|__natural_order__|
    +-----------------+---+---+---+---+---+-----------------+
    |                0|  1|  5|  9| 13| 17|              ...|
    |                1|  2|  6| 10| 14| 18|              ...|
    |                2|  3|  7| 11| 15| 19|              ...|
    |                3|  4|  8| 12| 16| 20|              ...|
    +-----------------+---+---+---+---+---+-----------------+
    >>> internal.data_spark_column_names
    [\'B\', \'C\', \'D\', \'E\']
    >>> internal.index_spark_column_names
    [\'__index_level_0__\', \'A\']
    >>> internal.spark_column_names
    [\'__index_level_0__\', \'A\', \'B\', \'C\', \'D\', \'E\']
    >>> internal.index_names
    [None, (\'A\',)]
    >>> internal.data_fields  # doctest: +NORMALIZE_WHITESPACE
    [InternalField(dtype=int64, struct_field=StructField(\'B\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'C\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'D\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'E\', LongType(), False))]
    >>> internal.index_fields  # doctest: +NORMALIZE_WHITESPACE
    [InternalField(dtype=int64, struct_field=StructField(\'__index_level_0__\', LongType(), False)),
     InternalField(dtype=int64, struct_field=StructField(\'A\', LongType(), False))]
    >>> internal.to_internal_spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE
    +-----------------+---+---+---+---+---+
    |__index_level_0__|  A|  B|  C|  D|  E|
    +-----------------+---+---+---+---+---+
    |                0|  1|  5|  9| 13| 17|
    |                1|  2|  6| 10| 14| 18|
    |                2|  3|  7| 11| 15| 19|
    |                3|  4|  8| 12| 16| 20|
    +-----------------+---+---+---+---+---+
    >>> internal.to_pandas_frame  # doctest: +NORMALIZE_WHITESPACE
         B   C   D   E
      A
    0 1  5   9  13  17
    1 2  6  10  14  18
    2 3  7  11  15  19
    3 4  8  12  16  20

    For multi-level columns, it also holds column_labels

    >>> columns = pd.MultiIndex.from_tuples([(\'X\', \'A\'), (\'X\', \'B\'),
    ...                                      (\'Y\', \'C\'), (\'Y\', \'D\')])
    >>> psdf3 = ps.DataFrame([
    ...     [1, 2, 3, 4],
    ...     [5, 6, 7, 8],
    ...     [9, 10, 11, 12],
    ...     [13, 14, 15, 16],
    ...     [17, 18, 19, 20]], columns = columns)
    >>> psdf3  # doctest: +NORMALIZE_WHITESPACE
        X       Y
        A   B   C   D
    0   1   2   3   4
    1   5   6   7   8
    2   9  10  11  12
    3  13  14  15  16
    4  17  18  19  20

    >>> internal = psdf3._internal
    >>> internal.spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    +-----------------+------+------+------+------+-----------------+
    |__index_level_0__|(X, A)|(X, B)|(Y, C)|(Y, D)|__natural_order__|
    +-----------------+------+------+------+------+-----------------+
    |                0|     1|     2|     3|     4|              ...|
    |                1|     5|     6|     7|     8|              ...|
    |                2|     9|    10|    11|    12|              ...|
    |                3|    13|    14|    15|    16|              ...|
    |                4|    17|    18|    19|    20|              ...|
    +-----------------+------+------+------+------+-----------------+
    >>> internal.data_spark_column_names
    [\'(X, A)\', \'(X, B)\', \'(Y, C)\', \'(Y, D)\']
    >>> internal.column_labels
    [(\'X\', \'A\'), (\'X\', \'B\'), (\'Y\', \'C\'), (\'Y\', \'D\')]

    For Series, it also holds scol to represent the column.

    >>> psseries = psdf1.B
    >>> psseries
    A
    1    5
    2    6
    3    7
    4    8
    Name: B, dtype: int64

    >>> internal = psseries._internal
    >>> internal.spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    +-----------------+---+---+---+---+---+-----------------+
    |__index_level_0__|  A|  B|  C|  D|  E|__natural_order__|
    +-----------------+---+---+---+---+---+-----------------+
    |                0|  1|  5|  9| 13| 17|              ...|
    |                1|  2|  6| 10| 14| 18|              ...|
    |                2|  3|  7| 11| 15| 19|              ...|
    |                3|  4|  8| 12| 16| 20|              ...|
    +-----------------+---+---+---+---+---+-----------------+
    >>> internal.data_spark_column_names
    [\'B\']
    >>> internal.index_spark_column_names
    [\'A\']
    >>> internal.spark_column_names
    [\'A\', \'B\']
    >>> internal.index_names
    [(\'A\',)]
    >>> internal.data_fields
    [InternalField(dtype=int64, struct_field=StructField(\'B\', LongType(), False))]
    >>> internal.index_fields
    [InternalField(dtype=int64, struct_field=StructField(\'A\', LongType(), False))]
    >>> internal.to_internal_spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE
    +---+---+
    |  A|  B|
    +---+---+
    |  1|  5|
    |  2|  6|
    |  3|  7|
    |  4|  8|
    +---+---+
    >>> internal.to_pandas_frame  # doctest: +NORMALIZE_WHITESPACE
       B
    A
    1  5
    2  6
    3  7
    4  8
    '''
    def __init__(self, spark_frame: SparkDataFrame, index_spark_columns: List[Column] | None, index_names: List[Label | None] | None = None, index_fields: List[InternalField] | None = None, column_labels: List[Label] | None = None, data_spark_columns: List[Column] | None = None, data_fields: List[InternalField] | None = None, column_label_names: List[Label | None] | None = None) -> None:
        '''
        Create a new internal immutable DataFrame to manage Spark DataFrame, column fields and
        index fields and names.

        :param spark_frame: Spark DataFrame to be managed.
        :param index_spark_columns: list of Spark Column
                                    Spark Columns for the index.
        :param index_names: list of tuples
                            the index names.
        :param index_fields: list of InternalField
                             the InternalFields for the index columns
        :param column_labels: list of tuples with the same length
                              The multi-level values in the tuples.
        :param data_spark_columns: list of Spark Column
                                   Spark Columns to appear as columns. If this is None, calculated
                                   from spark_frame.
        :param data_fields: list of InternalField
                            the InternalFields for the data columns
        :param column_label_names: Names for each of the column index levels.

        See the examples below to refer what each parameter means.

        >>> column_labels = pd.MultiIndex.from_tuples(
        ...     [(\'a\', \'x\'), (\'a\', \'y\'), (\'b\', \'z\')], names=["column_labels_a", "column_labels_b"])
        >>> row_index = pd.MultiIndex.from_tuples(
        ...     [(\'foo\', \'bar\'), (\'foo\', \'bar\'), (\'zoo\', \'bar\')],
        ...     names=["row_index_a", "row_index_b"])
        >>> psdf = ps.DataFrame(
        ...     [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=row_index, columns=column_labels)
        >>> psdf.set_index((\'a\', \'x\'), append=True, inplace=True)
        >>> psdf  # doctest: +NORMALIZE_WHITESPACE
        column_labels_a                  a  b
        column_labels_b                  y  z
        row_index_a row_index_b (a, x)
        foo         bar         1       2  3
                                4       5  6
        zoo         bar         7       8  9

        >>> internal = psdf._internal

        >>> internal.spark_frame.show()  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        +-----------------+-----------------+------+------+------+...
        |__index_level_0__|__index_level_1__|(a, x)|(a, y)|(b, z)|...
        +-----------------+-----------------+------+------+------+...
        |              foo|              bar|     1|     2|     3|...
        |              foo|              bar|     4|     5|     6|...
        |              zoo|              bar|     7|     8|     9|...
        +-----------------+-----------------+------+------+------+...

        >>> internal.index_spark_columns  # doctest: +SKIP
        [Column<\'__index_level_0__\'>, Column<\'__index_level_1__\'>, Column<\'(a, x)\'>]

        >>> internal.index_names
        [(\'row_index_a\',), (\'row_index_b\',), (\'a\', \'x\')]

        >>> internal.index_fields  # doctest: +NORMALIZE_WHITESPACE
        [InternalField(dtype=object,
            struct_field=StructField(\'__index_level_0__\', StringType(), False)),
         InternalField(dtype=object,
            struct_field=StructField(\'__index_level_1__\', StringType(), False)),
         InternalField(dtype=int64,
            struct_field=StructField(\'(a, x)\', LongType(), False))]

        >>> internal.column_labels
        [(\'a\', \'y\'), (\'b\', \'z\')]

        >>> internal.data_spark_columns  # doctest: +SKIP
        [Column<\'(a, y)\'>, Column<\'(b, z)\'>]

        >>> internal.data_fields  # doctest: +NORMALIZE_WHITESPACE
        [InternalField(dtype=int64, struct_field=StructField(\'(a, y)\', LongType(), False)),
         InternalField(dtype=int64, struct_field=StructField(\'(b, z)\', LongType(), False))]

        >>> internal.column_label_names
        [(\'column_labels_a\',), (\'column_labels_b\',)]
        '''
    @staticmethod
    def attach_default_index(sdf: SparkDataFrame, default_index_type: str | None = None) -> SparkDataFrame:
        """
        This method attaches a default index to Spark DataFrame. Spark does not have the index
        notion so corresponding column should be generated.
        There are several types of default index can be configured by `compute.default_index_type`.

        >>> spark_frame = ps.range(10).to_spark()
        >>> spark_frame
        DataFrame[id: bigint]

        It adds the default index column '__index_level_0__'.

        >>> spark_frame = InternalFrame.attach_default_index(spark_frame)
        >>> spark_frame
        DataFrame[__index_level_0__: bigint, id: bigint]

        It throws an exception if the given column name already exists.

        >>> InternalFrame.attach_default_index(spark_frame)
        ... # doctest: +ELLIPSIS
        Traceback (most recent call last):
          ...
        AssertionError: '__index_level_0__' already exists...
        """
    @staticmethod
    def attach_sequence_column(sdf: SparkDataFrame, column_name: str) -> SparkDataFrame: ...
    @staticmethod
    def attach_distributed_column(sdf: SparkDataFrame, column_name: str) -> SparkDataFrame: ...
    @staticmethod
    def attach_distributed_sequence_column(sdf: SparkDataFrame, column_name: str) -> SparkDataFrame:
        '''
        This method attaches a Spark column that has a sequence in a distributed manner.
        This is equivalent to the column assigned when default index type \'distributed-sequence\'.

        >>> sdf = ps.DataFrame([\'a\', \'b\', \'c\']).to_spark()
        >>> sdf = InternalFrame.attach_distributed_sequence_column(sdf, column_name="sequence")
        >>> sdf.show()  # doctest: +NORMALIZE_WHITESPACE
        +--------+---+
        |sequence|  0|
        +--------+---+
        |       0|  a|
        |       1|  b|
        |       2|  c|
        +--------+---+
        '''
    def spark_column_for(self, label: Label) -> Column:
        """Return Spark Column for the given column label."""
    def spark_column_name_for(self, label_or_scol: Label | Column) -> str:
        """Return the actual Spark column name for the given column label."""
    def spark_type_for(self, label_or_scol: Label | Column) -> DataType:
        """Return DataType for the given column label."""
    def spark_column_nullable_for(self, label_or_scol: Label | Column) -> bool:
        """Return nullability for the given column label."""
    def field_for(self, label: Label) -> InternalField:
        """Return InternalField for the given column label."""
    @property
    def spark_frame(self) -> SparkDataFrame:
        """Return the managed Spark DataFrame."""
    def data_spark_column_names(self) -> List[str]:
        """Return the managed column field names."""
    @property
    def data_spark_columns(self) -> List[Column]:
        """Return Spark Columns for the managed data columns."""
    @property
    def index_spark_column_names(self) -> List[str]:
        """Return the managed index field names."""
    @property
    def index_spark_columns(self) -> List[Column]:
        """Return Spark Columns for the managed index columns."""
    def spark_column_names(self) -> List[str]:
        """Return all the field names including index field names."""
    def spark_columns(self) -> List[Column]:
        """Return Spark Columns for the managed columns including index columns."""
    @property
    def index_names(self) -> List[Label | None]:
        """Return the managed index names."""
    def index_level(self) -> int:
        """Return the level of the index."""
    @property
    def column_labels(self) -> List[Label]:
        """Return the managed column index."""
    def column_labels_level(self) -> int:
        """Return the level of the column index."""
    @property
    def column_label_names(self) -> List[Label | None]:
        """Return names of the index levels."""
    @property
    def index_fields(self) -> List[InternalField]:
        """Return InternalFields for the managed index columns."""
    @property
    def data_fields(self) -> List[InternalField]:
        """Return InternalFields for the managed columns."""
    def to_internal_spark_frame(self) -> SparkDataFrame:
        """
        Return as Spark DataFrame. This contains index columns as well
        and should be only used for internal purposes.
        """
    def to_pandas_frame(self) -> pd.DataFrame:
        """Return as pandas DataFrame."""
    def arguments_for_restore_index(self) -> Dict:
        """Create arguments for `restore_index`."""
    @staticmethod
    def restore_index(pdf: pd.DataFrame, *, index_columns: List[str], index_names: List[Label], data_columns: List[str], column_labels: List[Label], column_label_names: List[Label], fields: List[InternalField] = None) -> pd.DataFrame:
        '''
        Restore pandas DataFrame indices using the metadata.

        :param pdf: the pandas DataFrame to be processed.
        :param index_columns: the original column names for index columns.
        :param index_names: the index names after restored.
        :param data_columns: the original column names for data columns.
        :param column_labels: the column labels after restored.
        :param column_label_names: the column label names after restored.
        :param fields: the fields after restored.
        :return: the restored pandas DataFrame

        >>> from numpy import dtype
        >>> pdf = pd.DataFrame({"index": [10, 20, 30], "a": [\'a\', \'b\', \'c\'], "b": [0, 2, 1]})
        >>> InternalFrame.restore_index(
        ...     pdf,
        ...     index_columns=["index"],
        ...     index_names=[("idx",)],
        ...     data_columns=["a", "b", "index"],
        ...     column_labels=[("x",), ("y",), ("z",)],
        ...     column_label_names=[("lv1",)],
        ...     fields=[
        ...         InternalField(
        ...             dtype=dtype(\'int64\'),
        ...             struct_field=StructField(name=\'index\', dataType=LongType(), nullable=False),
        ...         ),
        ...         InternalField(
        ...             dtype=dtype(\'object\'),
        ...             struct_field=StructField(name=\'a\', dataType=StringType(), nullable=False),
        ...         ),
        ...         InternalField(
        ...             dtype=CategoricalDtype(categories=["i", "j", "k"]),
        ...             struct_field=StructField(name=\'b\', dataType=LongType(), nullable=False),
        ...         ),
        ...     ],
        ... )  # doctest: +NORMALIZE_WHITESPACE
        lv1  x  y   z
        idx
        10   a  i  10
        20   b  k  20
        30   c  j  30
        '''
    def resolved_copy(self) -> InternalFrame:
        """Copy the immutable InternalFrame with the updates resolved."""
    def with_new_sdf(self, spark_frame: SparkDataFrame, *, index_fields: List[InternalField] | None = None, data_columns: List[str] | None = None, data_fields: List[InternalField] | None = None) -> InternalFrame:
        """Copy the immutable InternalFrame with the updates by the specified Spark DataFrame.

        :param spark_frame: the new Spark DataFrame
        :param index_fields: the new InternalFields for the index columns.
                             If None, the original dtyeps are used.
        :param data_columns: the new column names. If None, the original one is used.
        :param data_fields: the new InternalFields for the data columns.
                            If None, the original dtyeps are used.
        :return: the copied InternalFrame.
        """
    def with_new_columns(self, scols_or_pssers: Sequence[Column | Series], *, column_labels: List[Label] | None = None, data_fields: List[InternalField] | None = None, column_label_names: List[Label | None] | None | _NoValueType = ..., keep_order: bool = True) -> InternalFrame:
        """
        Copy the immutable InternalFrame with the updates by the specified Spark Columns or Series.

        :param scols_or_pssers: the new Spark Columns or Series.
        :param column_labels: the new column index.
            If None, the column_labels of the corresponding `scols_or_pssers` is used if it is
            Series; otherwise the original one is used.
        :param data_fields: the new InternalFields for the data columns.
            If None, the dtypes of the corresponding `scols_or_pssers` is used if it is Series;
            otherwise the dtypes will be inferred from the corresponding `scols_or_pssers`.
        :param column_label_names: the new names of the column index levels.
        :return: the copied InternalFrame.
        """
    def with_filter(self, pred: Column | Series) -> InternalFrame:
        """
        Copy the immutable InternalFrame with the updates by the predicate.

        :param pred: the predicate to filter.
        :return: the copied InternalFrame.
        """
    def with_new_spark_column(self, column_label: Label, scol: Column, *, field: InternalField | None = None, keep_order: bool = True) -> InternalFrame:
        """
        Copy the immutable InternalFrame with the updates by the specified Spark Column.

        :param column_label: the column label to be updated.
        :param scol: the new Spark Column
        :param field: the new InternalField for the data column.
            If not specified, the InternalField will be inferred from the spark Column.
        :return: the copied InternalFrame.
        """
    def select_column(self, column_label: Label) -> InternalFrame:
        """
        Copy the immutable InternalFrame with the specified column.

        :param column_label: the column label to use.
        :return: the copied InternalFrame.
        """
    def copy(self, *, spark_frame: SparkDataFrame | _NoValueType = ..., index_spark_columns: List[Column] | _NoValueType = ..., index_names: List[Label | None] | None | _NoValueType = ..., index_fields: List[InternalField] | None | _NoValueType = ..., column_labels: List[Label] | None | _NoValueType = ..., data_spark_columns: List[Column] | None | _NoValueType = ..., data_fields: List[InternalField] | None | _NoValueType = ..., column_label_names: List[Label | None] | None | _NoValueType = ...) -> InternalFrame:
        """
        Copy the immutable InternalFrame.

        :param spark_frame: the new Spark DataFrame. If not specified, the original one is used.
        :param index_spark_columns: the list of Spark Column.
                                    If not specified, the original ones are used.
        :param index_names: the index names. If not specified, the original ones are used.
        :param index_fields: the new InternalFields for the index columns.
                             If not specified, the original metadata are used.
        :param column_labels: the new column labels. If not specified, the original ones are used.
        :param data_spark_columns: the new Spark Columns.
                                   If not specified, the original ones are used.
        :param data_fields: the new InternalFields for the data columns.
                            If not specified, the original metadata are used.
        :param column_label_names: the new names of the column index levels.
                                   If not specified, the original ones are used.
        :return: the copied immutable InternalFrame.
        """
    @staticmethod
    def from_pandas(pdf: pd.DataFrame) -> InternalFrame:
        """Create an immutable DataFrame from pandas DataFrame.

        :param pdf: :class:`pd.DataFrame`
        :return: the created immutable DataFrame
        """
    @staticmethod
    def prepare_pandas_frame(pdf: pd.DataFrame, *, retain_index: bool = True, prefer_timestamp_ntz: bool = False) -> Tuple[pd.DataFrame, List[str], List[InternalField], List[str], List[InternalField]]:
        '''
        Prepare pandas DataFrame for creating Spark DataFrame.

        :param pdf: the pandas DataFrame to be prepared.
        :param retain_index: whether the indices should be retained.
        :return: the tuple of
            - the prepared pandas dataFrame
            - index column names for Spark DataFrame
            - the InternalFields for the index columns of the given pandas DataFrame
            - data column names for Spark DataFrame
            - the InternalFields for the data columns of the given pandas DataFrame

        >>> pdf = pd.DataFrame(
        ...    {("x", "a"): [\'a\', \'b\', \'c\'],
        ...     ("y", "b"): pd.Categorical(["i", "k", "j"], categories=["i", "j", "k"])},
        ...    index=[10, 20, 30])
        >>> prepared, index_columns, index_fields, data_columns, data_fields = (
        ...     InternalFrame.prepare_pandas_frame(pdf)
        ... )
        >>> prepared
           __index_level_0__ (x, a)  (y, b)
        0                 10      a       0
        1                 20      b       2
        2                 30      c       1
        >>> index_columns
        [\'__index_level_0__\']
        >>> index_fields  # doctest: +NORMALIZE_WHITESPACE
        [InternalField(dtype=int64, struct_field=StructField(\'__index_level_0__\',
                                                            LongType(), False))]
        >>> data_columns
        [\'(x, a)\', \'(y, b)\']
        >>> data_fields  # doctest: +NORMALIZE_WHITESPACE
        [InternalField(dtype=object, struct_field=StructField(\'(x, a)\', StringType(), False)),
         InternalField(dtype=category, struct_field=StructField(\'(y, b)\', ByteType(), False))]

        >>> import datetime
        >>> pdf = pd.DataFrame({
        ...     "dt": [datetime.datetime(1970, 1, 1)], "dt_obj": [datetime.datetime(1970, 1, 1)]
        ... })
        >>> pdf.dt_obj = pdf.dt_obj.astype("object")
        >>> _, _, _, _, data_fields = (
        ...     InternalFrame.prepare_pandas_frame(pdf, prefer_timestamp_ntz=True)
        ... )
        >>> data_fields  # doctest: +NORMALIZE_WHITESPACE
        [InternalField(dtype=datetime64[ns],
            struct_field=StructField(\'dt\', TimestampNTZType(), False)),
         InternalField(dtype=object,
            struct_field=StructField(\'dt_obj\', TimestampNTZType(), False))]

        >>> pdf = pd.DataFrame({
        ...     "td": [datetime.timedelta(0)], "td_obj": [datetime.timedelta(0)]
        ... })
        >>> pdf.td_obj = pdf.td_obj.astype("object")
        >>> _, _, _, _, data_fields = (
        ...     InternalFrame.prepare_pandas_frame(pdf)
        ... )
        >>> data_fields  # doctest: +NORMALIZE_WHITESPACE
        [InternalField(dtype=timedelta64[ns],
            struct_field=StructField(\'td\', DayTimeIntervalType(0, 3), False)),
         InternalField(dtype=object,
            struct_field=StructField(\'td_obj\', DayTimeIntervalType(0, 3), False))]
        '''
