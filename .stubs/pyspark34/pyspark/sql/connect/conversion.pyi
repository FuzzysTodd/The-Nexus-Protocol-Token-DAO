import pyarrow as pa
from pyspark.sql.connect.types import to_arrow_schema as to_arrow_schema
from pyspark.sql.connect.utils import check_dependencies as check_dependencies
from pyspark.sql.types import ArrayType as ArrayType, BinaryType as BinaryType, DataType as DataType, DecimalType as DecimalType, MapType as MapType, NullType as NullType, Row as Row, StringType as StringType, StructType as StructType, TimestampNTZType as TimestampNTZType, TimestampType as TimestampType, UserDefinedType as UserDefinedType
from typing import Any, List, Sequence

class LocalDataToArrowConversion:
    """
    Conversion from local data (except pandas DataFrame and numpy ndarray) to Arrow.
    Currently, only :class:`SparkSession` in Spark Connect can use this class.
    """
    @staticmethod
    def convert(data: Sequence[Any], schema: StructType) -> pa.Table: ...

class ArrowTableToRowsConversion:
    """
    Conversion from Arrow Table to Rows.
    Currently, only :class:`DataFrame` in Spark Connect can use this class.
    """
    @staticmethod
    def convert(table: pa.Table, schema: StructType) -> List[Row]: ...
