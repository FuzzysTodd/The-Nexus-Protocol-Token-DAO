import pyarrow as pa
import pyspark.sql.connect.proto as pb2
from _typeshed import Incomplete
from pyspark.sql.connect.utils import check_dependencies as check_dependencies
from pyspark.sql.types import ArrayType as ArrayType, BinaryType as BinaryType, BooleanType as BooleanType, ByteType as ByteType, CharType as CharType, DataType as DataType, DateType as DateType, DayTimeIntervalType as DayTimeIntervalType, DecimalType as DecimalType, DoubleType as DoubleType, FloatType as FloatType, IntegerType as IntegerType, LongType as LongType, MapType as MapType, NullType as NullType, ShortType as ShortType, StringType as StringType, StructField as StructField, StructType as StructType, TimestampNTZType as TimestampNTZType, TimestampType as TimestampType, UserDefinedType as UserDefinedType, VarcharType as VarcharType
from typing import Any, Dict

JVM_BYTE_MIN: int
JVM_BYTE_MAX: int
JVM_SHORT_MIN: int
JVM_SHORT_MAX: int
JVM_INT_MIN: int
JVM_INT_MAX: int
JVM_LONG_MIN: int
JVM_LONG_MAX: int

class UnparsedDataType(DataType):
    '''
    Unparsed data type.

    The data type string will be parsed later.

    Parameters
    ----------
    data_type_string : str
        The data type string format equals :class:`DataType.simpleString`,
        except that the top level struct type can omit the ``struct<>``.
        This also supports a schema in a DDL-formatted string and case-insensitive strings.

    Examples
    --------
    >>> from pyspark.sql.connect.types import UnparsedDataType

    >>> UnparsedDataType("int ")
    UnparsedDataType(\'int \')
    >>> UnparsedDataType("INT ")
    UnparsedDataType(\'INT \')
    >>> UnparsedDataType("a: byte, b: decimal(  16 , 8   ) ")
    UnparsedDataType(\'a: byte, b: decimal(  16 , 8   ) \')
    >>> UnparsedDataType("a DOUBLE, b STRING")
    UnparsedDataType(\'a DOUBLE, b STRING\')
    >>> UnparsedDataType("a DOUBLE, b CHAR( 50 )")
    UnparsedDataType(\'a DOUBLE, b CHAR( 50 )\')
    >>> UnparsedDataType("a DOUBLE, b VARCHAR( 50 )")
    UnparsedDataType(\'a DOUBLE, b VARCHAR( 50 )\')
    >>> UnparsedDataType("a: array< short>")
    UnparsedDataType(\'a: array< short>\')
    >>> UnparsedDataType(" map<string , string > ")
    UnparsedDataType(\' map<string , string > \')
    '''
    data_type_string: Incomplete
    def __init__(self, data_type_string: str) -> None: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> Dict[str, Any]: ...
    def needConversion(self) -> bool: ...
    def toInternal(self, obj: Any) -> Any: ...
    def fromInternal(self, obj: Any) -> Any: ...

def pyspark_types_to_proto_types(data_type: DataType) -> pb2.DataType: ...
def proto_schema_to_pyspark_data_type(schema: pb2.DataType) -> DataType: ...
def to_arrow_type(dt: DataType) -> pa.DataType:
    """
    Convert Spark data type to pyarrow type.

    This function refers to 'pyspark.sql.pandas.types.to_arrow_type' but relax the restriction,
    e.g. it supports nested StructType.
    """
def to_arrow_schema(schema: StructType) -> pa.Schema:
    """Convert a schema from Spark to Arrow"""
def from_arrow_type(at: pa.DataType, prefer_timestamp_ntz: bool = False) -> DataType:
    """Convert pyarrow type to Spark data type.

    This function refers to 'pyspark.sql.pandas.types.from_arrow_type' but relax the restriction,
    e.g. it supports nested StructType, Array of TimestampType. However, Arrow DictionaryType is
    not allowed.
    """
def from_arrow_schema(arrow_schema: pa.Schema) -> StructType:
    """Convert schema from Arrow to Spark."""
