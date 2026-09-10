from py4j.java_gateway import JavaObject as JavaObject
from pyspark.sql import DataFrame as DataFrame
from pyspark.sql.pandas._typing import DataFrameLike as PandasDataFrameLike
from pyspark.sql.pandas.serializers import ArrowCollectSerializer as ArrowCollectSerializer
from pyspark.sql.types import BooleanType as BooleanType, ByteType as ByteType, DataType as DataType, DayTimeIntervalType as DayTimeIntervalType, DoubleType as DoubleType, FloatType as FloatType, IntegerType as IntegerType, IntegralType as IntegralType, LongType as LongType, MapType as MapType, ShortType as ShortType, StructType as StructType, TimestampNTZType as TimestampNTZType, TimestampType as TimestampType
from pyspark.sql.utils import is_timestamp_ntz_preferred as is_timestamp_ntz_preferred
from pyspark.traceback_utils import SCCallSiteSync as SCCallSiteSync
from typing import overload

class PandasConversionMixin:
    """
    Mix-in for the conversion from Spark to pandas. Currently, only :class:`DataFrame`
    can use this class.
    """
    def toPandas(self) -> PandasDataFrameLike:
        """
        Returns the contents of this :class:`DataFrame` as Pandas ``pandas.DataFrame``.

        This is only available if Pandas is installed and available.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Notes
        -----
        This method should only be used if the resulting Pandas ``pandas.DataFrame`` is
        expected to be small, as all the data is loaded into the driver's memory.

        Usage with ``spark.sql.execution.arrow.pyspark.enabled=True`` is experimental.

        Examples
        --------
        >>> df.toPandas()  # doctest: +SKIP
           age   name
        0    2  Alice
        1    5    Bob
        """

class SparkConversionMixin:
    """
    Min-in for the conversion from pandas to Spark. Currently, only :class:`SparkSession`
    can use this class.
    """
    @overload
    def createDataFrame(self, data: PandasDataFrameLike, samplingRatio: float | None = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: PandasDataFrameLike, schema: StructType | str, verifySchema: bool = ...) -> DataFrame: ...
