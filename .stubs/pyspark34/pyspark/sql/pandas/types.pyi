import pyarrow as pa
from pyspark.sql.types import ArrayType as ArrayType, BinaryType as BinaryType, BooleanType as BooleanType, ByteType as ByteType, DataType as DataType, DateType as DateType, DayTimeIntervalType as DayTimeIntervalType, DecimalType as DecimalType, DoubleType as DoubleType, FloatType as FloatType, IntegerType as IntegerType, LongType as LongType, MapType as MapType, NullType as NullType, ShortType as ShortType, StringType as StringType, StructField as StructField, StructType as StructType, TimestampNTZType as TimestampNTZType, TimestampType as TimestampType, cast as cast

def to_arrow_type(dt: DataType) -> pa.DataType:
    """Convert Spark data type to pyarrow type"""
def to_arrow_schema(schema: StructType) -> pa.Schema:
    """Convert a schema from Spark to Arrow"""
def from_arrow_type(at: pa.DataType, prefer_timestamp_ntz: bool = False) -> DataType:
    """Convert pyarrow type to Spark data type."""
def from_arrow_schema(arrow_schema: pa.Schema) -> StructType:
    """Convert schema from Arrow to Spark."""
