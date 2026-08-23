from _typeshed import Incomplete
from collections.abc import Generator
from pyspark.serializers import CPickleSerializer as CPickleSerializer, Serializer as Serializer, UTF8Deserializer as UTF8Deserializer, read_int as read_int, write_int as write_int
from pyspark.sql.pandas.types import to_arrow_type as to_arrow_type
from pyspark.sql.types import BinaryType as BinaryType, LongType as LongType, StringType as StringType, StructField as StructField, StructType as StructType

class SpecialLengths:
    END_OF_DATA_SECTION: int
    PYTHON_EXCEPTION_THROWN: int
    TIMING_DATA: int
    END_OF_STREAM: int
    NULL: int
    START_ARROW_STREAM: int

class ArrowCollectSerializer(Serializer):
    """
    Deserialize a stream of batches followed by batch order information. Used in
    PandasConversionMixin._collect_as_arrow() after invoking Dataset.collectAsArrowToPython()
    in the JVM.
    """
    serializer: Incomplete
    def __init__(self) -> None: ...
    def dump_stream(self, iterator, stream): ...
    def load_stream(self, stream) -> Generator[Incomplete, None, None]:
        """
        Load a stream of un-ordered Arrow RecordBatches, where the last iteration yields
        a list of indices that can be used to put the RecordBatches in the correct order.
        """

class ArrowStreamSerializer(Serializer):
    """
    Serializes Arrow record batches as a stream.
    """
    def dump_stream(self, iterator, stream) -> None: ...
    def load_stream(self, stream) -> Generator[Incomplete, None, None]: ...

class ArrowStreamUDFSerializer(ArrowStreamSerializer):
    """
    Same as :class:`ArrowStreamSerializer` but it flattens the struct to Arrow record batch
    for applying each function with the raw record arrow batch. See also `DataFrame.mapInArrow`.
    """
    def load_stream(self, stream) -> Generator[Incomplete, None, None]:
        """
        Flatten the struct into Arrow's record batches.
        """
    def dump_stream(self, iterator, stream):
        """
        Override because Pandas UDFs require a START_ARROW_STREAM before the Arrow stream is sent.
        This should be sent after creating the first record batch so in case of an error, it can
        be sent back to the JVM before the Arrow stream starts.
        """

class ArrowStreamPandasSerializer(ArrowStreamSerializer):
    """
    Serializes Pandas.Series as Arrow data with Arrow streaming format.

    Parameters
    ----------
    timezone : str
        A timezone to respect when handling timestamp values
    safecheck : bool
        If True, conversion from Arrow to Pandas checks for overflow/truncation
    assign_cols_by_name : bool
        If True, then Pandas DataFrames will get columns by name
    """
    def __init__(self, timezone, safecheck, assign_cols_by_name) -> None: ...
    def arrow_to_pandas(self, arrow_column): ...
    def dump_stream(self, iterator, stream) -> None:
        """
        Make ArrowRecordBatches from Pandas Series and serialize. Input is a single series or
        a list of series accompanied by an optional pyarrow type to coerce the data to.
        """
    def load_stream(self, stream) -> Generator[Incomplete, None, None]:
        """
        Deserialize ArrowRecordBatches to an Arrow table and return as a list of pandas.Series.
        """

class ArrowStreamPandasUDFSerializer(ArrowStreamPandasSerializer):
    """
    Serializer used by Python worker to evaluate Pandas UDFs
    """
    def __init__(self, timezone, safecheck, assign_cols_by_name, df_for_struct: bool = False) -> None: ...
    def arrow_to_pandas(self, arrow_column): ...
    def dump_stream(self, iterator, stream):
        """
        Override because Pandas UDFs require a START_ARROW_STREAM before the Arrow stream is sent.
        This should be sent after creating the first record batch so in case of an error, it can
        be sent back to the JVM before the Arrow stream starts.
        """

class CogroupUDFSerializer(ArrowStreamPandasUDFSerializer):
    def load_stream(self, stream) -> Generator[Incomplete, None, None]:
        """
        Deserialize Cogrouped ArrowRecordBatches to a tuple of Arrow tables and yield as two
        lists of pandas.Series.
        """

class ApplyInPandasWithStateSerializer(ArrowStreamPandasUDFSerializer):
    """
    Serializer used by Python worker to evaluate UDF for applyInPandasWithState.

    Parameters
    ----------
    timezone : str
        A timezone to respect when handling timestamp values
    safecheck : bool
        If True, conversion from Arrow to Pandas checks for overflow/truncation
    assign_cols_by_name : bool
        If True, then Pandas DataFrames will get columns by name
    state_object_schema : StructType
        The type of state object represented as Spark SQL type
    arrow_max_records_per_batch : int
        Limit of the number of records that can be written to a single ArrowRecordBatch in memory.
    """
    pickleSer: Incomplete
    utf8_deserializer: Incomplete
    state_object_schema: Incomplete
    result_state_df_type: Incomplete
    result_state_pdf_arrow_type: Incomplete
    arrow_max_records_per_batch: Incomplete
    def __init__(self, timezone, safecheck, assign_cols_by_name, state_object_schema, arrow_max_records_per_batch) -> None: ...
    def load_stream(self, stream) -> Generator[Incomplete, None, Incomplete]:
        """
        Read ArrowRecordBatches from stream, deserialize them to populate a list of pair
        (data chunk, state), and convert the data into a list of pandas.Series.

        Please refer the doc of inner function `gen_data_and_state` for more details how
        this function works in overall.

        In addition, this function further groups the return of `gen_data_and_state` by the state
        instance (same semantic as grouping by grouping key) and produces an iterator of data
        chunks for each group, so that the caller can lazily materialize the data chunk.
        """
    def dump_stream(self, iterator, stream):
        """
        Read through an iterator of (iterator of pandas DataFrame, state), serialize them to Arrow
        RecordBatches, and write batches to stream.
        """
