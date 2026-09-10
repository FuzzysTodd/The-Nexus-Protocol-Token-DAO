import datetime
import numpy as np
from _typeshed import Incomplete
from py4j.java_gateway import GatewayClient, JavaObject
from typing import Any, Dict, Iterator, List, Tuple, TypeVar, overload

__all__ = ['DataType', 'NullType', 'CharType', 'StringType', 'VarcharType', 'BinaryType', 'BooleanType', 'DateType', 'TimestampType', 'TimestampNTZType', 'DecimalType', 'DoubleType', 'FloatType', 'ByteType', 'IntegerType', 'LongType', 'DayTimeIntervalType', 'Row', 'ShortType', 'ArrayType', 'MapType', 'StructField', 'StructType']

T = TypeVar('T')
U = TypeVar('U')

class DataType:
    """Base class for data types."""
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    @classmethod
    def typeName(cls) -> str: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> str | Dict[str, Any]: ...
    def json(self) -> str: ...
    def needConversion(self) -> bool:
        """
        Does this type needs conversion between Python object and internal SQL object.

        This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.
        """
    def toInternal(self, obj: Any) -> Any:
        """
        Converts a Python object into an internal SQL object.
        """
    def fromInternal(self, obj: Any) -> Any:
        """
        Converts an internal SQL object into a native Python object.
        """

class DataTypeSingleton(type):
    """Metaclass for DataType"""
    def __call__(cls) -> T: ...

class NullType(DataType, metaclass=DataTypeSingleton):
    """Null type.

    The data type representing None, used for the types that cannot be inferred.
    """
    @classmethod
    def typeName(cls) -> str: ...

class AtomicType(DataType):
    """An internal type used to represent everything that is not
    null, UDTs, arrays, structs, and maps."""
class NumericType(AtomicType):
    """Numeric data types."""
class IntegralType(NumericType, metaclass=DataTypeSingleton):
    """Integral data types."""
class FractionalType(NumericType):
    """Fractional data types."""
class StringType(AtomicType, metaclass=DataTypeSingleton):
    """String data type."""

class CharType(AtomicType):
    """Char data type

    Parameters
    ----------
    length : int
        the length limitation.
    """
    length: Incomplete
    def __init__(self, length: int) -> None: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> str: ...

class VarcharType(AtomicType):
    """Varchar data type

    Parameters
    ----------
    length : int
        the length limitation.
    """
    length: Incomplete
    def __init__(self, length: int) -> None: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> str: ...

class BinaryType(AtomicType, metaclass=DataTypeSingleton):
    """Binary (byte array) data type."""
class BooleanType(AtomicType, metaclass=DataTypeSingleton):
    """Boolean data type."""

class DateType(AtomicType, metaclass=DataTypeSingleton):
    """Date (datetime.date) data type."""
    EPOCH_ORDINAL: Incomplete
    def needConversion(self) -> bool: ...
    def toInternal(self, d: datetime.date) -> int: ...
    def fromInternal(self, v: int) -> datetime.date: ...

class TimestampType(AtomicType, metaclass=DataTypeSingleton):
    """Timestamp (datetime.datetime) data type."""
    def needConversion(self) -> bool: ...
    def toInternal(self, dt: datetime.datetime) -> int: ...
    def fromInternal(self, ts: int) -> datetime.datetime: ...

class TimestampNTZType(AtomicType, metaclass=DataTypeSingleton):
    """Timestamp (datetime.datetime) data type without timezone information."""
    def needConversion(self) -> bool: ...
    @classmethod
    def typeName(cls) -> str: ...
    def toInternal(self, dt: datetime.datetime) -> int: ...
    def fromInternal(self, ts: int) -> datetime.datetime: ...

class DecimalType(FractionalType):
    """Decimal (decimal.Decimal) data type.

    The DecimalType must have fixed precision (the maximum total number of digits)
    and scale (the number of digits on the right of dot). For example, (5, 2) can
    support the value from [-999.99 to 999.99].

    The precision can be up to 38, the scale must be less or equal to precision.

    When creating a DecimalType, the default precision and scale is (10, 0). When inferring
    schema from decimal.Decimal objects, it will be DecimalType(38, 18).

    Parameters
    ----------
    precision : int, optional
        the maximum (i.e. total) number of digits (default: 10)
    scale : int, optional
        the number of digits on right side of dot. (default: 0)
    """
    precision: Incomplete
    scale: Incomplete
    hasPrecisionInfo: bool
    def __init__(self, precision: int = 10, scale: int = 0) -> None: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> str: ...

class DoubleType(FractionalType, metaclass=DataTypeSingleton):
    """Double data type, representing double precision floats."""
class FloatType(FractionalType, metaclass=DataTypeSingleton):
    """Float data type, representing single precision floats."""

class ByteType(IntegralType):
    """Byte data type, i.e. a signed integer in a single byte."""
    def simpleString(self) -> str: ...

class IntegerType(IntegralType):
    """Int data type, i.e. a signed 32-bit integer."""
    def simpleString(self) -> str: ...

class LongType(IntegralType):
    """Long data type, i.e. a signed 64-bit integer.

    If the values are beyond the range of [-9223372036854775808, 9223372036854775807],
    please use :class:`DecimalType`.
    """
    def simpleString(self) -> str: ...

class DayTimeIntervalType(AtomicType):
    """DayTimeIntervalType (datetime.timedelta)."""
    DAY: int
    HOUR: int
    MINUTE: int
    SECOND: int
    startField: Incomplete
    endField: Incomplete
    def __init__(self, startField: int | None = None, endField: int | None = None) -> None: ...
    simpleString: Incomplete
    jsonValue: Incomplete
    def needConversion(self) -> bool: ...
    def toInternal(self, dt: datetime.timedelta) -> int | None: ...
    def fromInternal(self, micros: int) -> datetime.timedelta | None: ...

class ShortType(IntegralType):
    """Short data type, i.e. a signed 16-bit integer."""
    def simpleString(self) -> str: ...

class ArrayType(DataType):
    """Array data type.

    Parameters
    ----------
    elementType : :class:`DataType`
        :class:`DataType` of each element in the array.
    containsNull : bool, optional
        whether the array can contain null (None) values.

    Examples
    --------
    >>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType

    The below example demonstrates how to create class:`ArrayType`:

    >>> arr = ArrayType(StringType())

    The array can contain null (None) values by default:

    >>> ArrayType(StringType()) == ArrayType(StringType(), True)
    True
    >>> ArrayType(StringType(), False) == ArrayType(StringType())
    False
    """
    elementType: Incomplete
    containsNull: Incomplete
    def __init__(self, elementType: DataType, containsNull: bool = True) -> None: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> Dict[str, Any]: ...
    @classmethod
    def fromJson(cls, json: Dict[str, Any]) -> ArrayType: ...
    def needConversion(self) -> bool: ...
    def toInternal(self, obj: List[T | None]) -> List[T | None]: ...
    def fromInternal(self, obj: List[T | None]) -> List[T | None]: ...

class MapType(DataType):
    """Map data type.

    Parameters
    ----------
    keyType : :class:`DataType`
        :class:`DataType` of the keys in the map.
    valueType : :class:`DataType`
        :class:`DataType` of the values in the map.
    valueContainsNull : bool, optional
        indicates whether values can contain null (None) values.

    Notes
    -----
    Keys in a map data type are not allowed to be null (None).

    Examples
    --------
    >>> from pyspark.sql.types import IntegerType, FloatType, MapType, StringType

    The below example demonstrates how to create class:`MapType`:

    >>> map_type = MapType(StringType(), IntegerType())

    The values of the map can contain null (``None``) values by default:

    >>> (MapType(StringType(), IntegerType())
    ...        == MapType(StringType(), IntegerType(), True))
    True
    >>> (MapType(StringType(), IntegerType(), False)
    ...        == MapType(StringType(), FloatType()))
    False
    """
    keyType: Incomplete
    valueType: Incomplete
    valueContainsNull: Incomplete
    def __init__(self, keyType: DataType, valueType: DataType, valueContainsNull: bool = True) -> None: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> Dict[str, Any]: ...
    @classmethod
    def fromJson(cls, json: Dict[str, Any]) -> MapType: ...
    def needConversion(self) -> bool: ...
    def toInternal(self, obj: Dict[T, U | None]) -> Dict[T, U | None]: ...
    def fromInternal(self, obj: Dict[T, U | None]) -> Dict[T, U | None]: ...

class StructField(DataType):
    '''A field in :class:`StructType`.

    Parameters
    ----------
    name : str
        name of the field.
    dataType : :class:`DataType`
        :class:`DataType` of the field.
    nullable : bool, optional
        whether the field can be null (None) or not.
    metadata : dict, optional
        a dict from string to simple type that can be toInternald to JSON automatically

    Examples
    --------
    >>> from pyspark.sql.types import StringType, StructField
    >>> (StructField("f1", StringType(), True)
    ...      == StructField("f1", StringType(), True))
    True
    >>> (StructField("f1", StringType(), True)
    ...      == StructField("f2", StringType(), True))
    False
    '''
    name: Incomplete
    dataType: Incomplete
    nullable: Incomplete
    metadata: Incomplete
    def __init__(self, name: str, dataType: DataType, nullable: bool = True, metadata: Dict[str, Any] | None = None) -> None: ...
    def simpleString(self) -> str: ...
    def jsonValue(self) -> Dict[str, Any]: ...
    @classmethod
    def fromJson(cls, json: Dict[str, Any]) -> StructField: ...
    def needConversion(self) -> bool: ...
    def toInternal(self, obj: T) -> T: ...
    def fromInternal(self, obj: T) -> T: ...
    def typeName(self) -> str: ...

class StructType(DataType):
    '''Struct type, consisting of a list of :class:`StructField`.

    This is the data type representing a :class:`Row`.

    Iterating a :class:`StructType` will iterate over its :class:`StructField`\\s.
    A contained :class:`StructField` can be accessed by its name or position.

    Examples
    --------
    >>> from pyspark.sql.types import *
    >>> struct1 = StructType([StructField("f1", StringType(), True)])
    >>> struct1["f1"]
    StructField(\'f1\', StringType(), True)
    >>> struct1[0]
    StructField(\'f1\', StringType(), True)

    >>> struct1 = StructType([StructField("f1", StringType(), True)])
    >>> struct2 = StructType([StructField("f1", StringType(), True)])
    >>> struct1 == struct2
    True
    >>> struct1 = StructType([StructField("f1", CharType(10), True)])
    >>> struct2 = StructType([StructField("f1", CharType(10), True)])
    >>> struct1 == struct2
    True
    >>> struct1 = StructType([StructField("f1", VarcharType(10), True)])
    >>> struct2 = StructType([StructField("f1", VarcharType(10), True)])
    >>> struct1 == struct2
    True
    >>> struct1 = StructType([StructField("f1", StringType(), True)])
    >>> struct2 = StructType([StructField("f1", StringType(), True),
    ...     StructField("f2", IntegerType(), False)])
    >>> struct1 == struct2
    False

    The below example demonstrates how to create a DataFrame based on a struct created
    using class:`StructType` and class:`StructField`:

    >>> data = [("Alice", ["Java", "Scala"]), ("Bob", ["Python", "Scala"])]
    >>> schema = StructType([
    ...     StructField("name", StringType()),
    ...     StructField("languagesSkills", ArrayType(StringType())),
    ... ])
    >>> df = spark.createDataFrame(data=data, schema=schema)
    >>> df.printSchema()
    root
     |-- name: string (nullable = true)
     |-- languagesSkills: array (nullable = true)
     |    |-- element: string (containsNull = true)
    >>> df.show()
    +-----+---------------+
    | name|languagesSkills|
    +-----+---------------+
    |Alice|  [Java, Scala]|
    |  Bob|[Python, Scala]|
    +-----+---------------+
    '''
    fields: Incomplete
    names: Incomplete
    def __init__(self, fields: List[StructField] | None = None) -> None: ...
    @overload
    def add(self, field: str, data_type: str | DataType, nullable: bool = True, metadata: Dict[str, Any] | None = None) -> StructType: ...
    @overload
    def add(self, field: StructField) -> StructType: ...
    def __iter__(self) -> Iterator[StructField]:
        """Iterate the fields"""
    def __len__(self) -> int:
        """Return the number of fields."""
    def __getitem__(self, key: str | int) -> StructField:
        """Access fields by name or slice."""
    def simpleString(self) -> str: ...
    def jsonValue(self) -> Dict[str, Any]: ...
    @classmethod
    def fromJson(cls, json: Dict[str, Any]) -> StructType:
        '''
        Constructs :class:`StructType` from a schema defined in JSON format.

        Below is a JSON schema it must adhere to::

            {
              "title":"StructType",
              "description":"Schema of StructType in json format",
              "type":"object",
              "properties":{
                 "fields":{
                    "description":"Array of struct fields",
                    "type":"array",
                    "items":{
                        "type":"object",
                        "properties":{
                           "name":{
                              "description":"Name of the field",
                              "type":"string"
                           },
                           "type":{
                              "description": "Type of the field. Can either be
                                              another nested StructType or primitive type",
                              "type":"object/string"
                           },
                           "nullable":{
                              "description":"If nulls are allowed",
                              "type":"boolean"
                           },
                           "metadata":{
                              "description":"Additional metadata to supply",
                              "type":"object"
                           },
                           "required":[
                              "name",
                              "type",
                              "nullable",
                              "metadata"
                           ]
                        }
                   }
                }
             }
           }

        Parameters
        ----------
        json : dict or a dict-like object e.g. JSON object
            This "dict" must have "fields" key that returns an array of fields
            each of which must have specific keys (name, type, nullable, metadata).

        Returns
        -------
        :class:`StructType`

        Examples
        --------
        >>> json_str = \'\'\'
        ...  {
        ...      "fields": [
        ...          {
        ...              "metadata": {},
        ...              "name": "Person",
        ...              "nullable": true,
        ...              "type": {
        ...                  "fields": [
        ...                      {
        ...                          "metadata": {},
        ...                          "name": "name",
        ...                          "nullable": false,
        ...                          "type": "string"
        ...                      },
        ...                      {
        ...                          "metadata": {},
        ...                          "name": "surname",
        ...                          "nullable": false,
        ...                          "type": "string"
        ...                      }
        ...                  ],
        ...                  "type": "struct"
        ...              }
        ...          }
        ...      ],
        ...      "type": "struct"
        ...  }
        ...  \'\'\'
        >>> import json
        >>> scheme = StructType.fromJson(json.loads(json_str))
        >>> scheme.simpleString()
        \'struct<Person:struct<name:string,surname:string>>\'
        '''
    def fieldNames(self) -> List[str]:
        '''
        Returns all field names in a list.

        Examples
        --------
        >>> from pyspark.sql.types import StringType, StructField, StructType
        >>> struct = StructType([StructField("f1", StringType(), True)])
        >>> struct.fieldNames()
        [\'f1\']
        '''
    def needConversion(self) -> bool: ...
    def toInternal(self, obj: Tuple) -> Tuple: ...
    def fromInternal(self, obj: Tuple) -> Row: ...

class UserDefinedType(DataType):
    """User-defined type (UDT).

    .. note:: WARN: Spark Internal Use Only
    """
    @classmethod
    def typeName(cls) -> str: ...
    @classmethod
    def sqlType(cls) -> DataType:
        """
        Underlying SQL storage type for this UDT.
        """
    @classmethod
    def module(cls) -> str:
        """
        The Python module of the UDT.
        """
    @classmethod
    def scalaUDT(cls) -> str:
        """
        The class name of the paired Scala UDT (could be '', if there
        is no corresponding one).
        """
    def needConversion(self) -> bool: ...
    def toInternal(self, obj: Any) -> Any: ...
    def fromInternal(self, obj: Any) -> Any: ...
    def serialize(self, obj: Any) -> Any:
        """
        Converts a user-type object into a SQL datum.
        """
    def deserialize(self, datum: Any) -> Any:
        """
        Converts a SQL datum into a user-type object.
        """
    def simpleString(self) -> str: ...
    def json(self) -> str: ...
    def jsonValue(self) -> Dict[str, Any]: ...
    @classmethod
    def fromJson(cls, json: Dict[str, Any]) -> UserDefinedType: ...
    def __eq__(self, other: Any) -> bool: ...

class Row(tuple):
    '''
    A row in :class:`DataFrame`.
    The fields in it can be accessed:

    * like attributes (``row.key``)
    * like dictionary values (``row[key]``)

    ``key in row`` will search through row keys.

    Row can be used to create a row object by using named arguments.
    It is not allowed to omit a named argument to represent that the value is
    None or missing. This should be explicitly set to None in this case.

    .. versionchanged:: 3.0.0
        Rows created from named arguments no longer have
        field names sorted alphabetically and will be ordered in the position as
        entered.

    Examples
    --------
    >>> from pyspark.sql import Row
    >>> row = Row(name="Alice", age=11)
    >>> row
    Row(name=\'Alice\', age=11)
    >>> row[\'name\'], row[\'age\']
    (\'Alice\', 11)
    >>> row.name, row.age
    (\'Alice\', 11)
    >>> \'name\' in row
    True
    >>> \'wrong_key\' in row
    False

    Row also can be used to create another Row like class, then it
    could be used to create Row objects, such as

    >>> Person = Row("name", "age")
    >>> Person
    <Row(\'name\', \'age\')>
    >>> \'name\' in Person
    True
    >>> \'wrong_key\' in Person
    False
    >>> Person("Alice", 11)
    Row(name=\'Alice\', age=11)

    This form can also be used to create rows as tuple values, i.e. with unnamed
    fields.

    >>> row1 = Row("Alice", 11)
    >>> row2 = Row(name="Alice", age=11)
    >>> row1 == row2
    True
    '''
    @overload
    def __new__(cls, *args: str) -> Row: ...
    @overload
    def __new__(cls, **kwargs: Any) -> Row: ...
    def asDict(self, recursive: bool = False) -> Dict[str, Any]:
        '''
        Return as a dict

        Parameters
        ----------
        recursive : bool, optional
            turns the nested Rows to dict (default: False).

        Notes
        -----
        If a row contains duplicate field names, e.g., the rows of a join
        between two :class:`DataFrame` that both have the fields of same names,
        one of the duplicate fields will be selected by ``asDict``. ``__getitem__``
        will also return one of the duplicate fields, however returned value might
        be different to ``asDict``.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> Row(name="Alice", age=11).asDict() == {\'name\': \'Alice\', \'age\': 11}
        True
        >>> row = Row(key=1, value=Row(name=\'a\', age=2))
        >>> row.asDict() == {\'key\': 1, \'value\': Row(name=\'a\', age=2)}
        True
        >>> row.asDict(True) == {\'key\': 1, \'value\': {\'name\': \'a\', \'age\': 2}}
        True
        '''
    def __contains__(self, item: Any) -> bool: ...
    def __call__(self, *args: Any) -> Row:
        """create new Row object"""
    def __getitem__(self, item: Any) -> Any: ...
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, key: Any, value: Any) -> None: ...
    def __reduce__(self) -> str | Tuple[Any, ...]:
        """Returns a tuple so Python knows how to pickle Row."""

class DateConverter:
    def can_convert(self, obj: Any) -> bool: ...
    def convert(self, obj: datetime.date, gateway_client: GatewayClient) -> JavaObject: ...

class DatetimeConverter:
    def can_convert(self, obj: Any) -> bool: ...
    def convert(self, obj: datetime.datetime, gateway_client: GatewayClient) -> JavaObject: ...

class DatetimeNTZConverter:
    def can_convert(self, obj: Any) -> bool: ...
    def convert(self, obj: datetime.datetime, gateway_client: GatewayClient) -> JavaObject: ...

class DayTimeIntervalTypeConverter:
    def can_convert(self, obj: Any) -> bool: ...
    def convert(self, obj: datetime.timedelta, gateway_client: GatewayClient) -> JavaObject: ...

class NumpyScalarConverter:
    def can_convert(self, obj: Any) -> bool: ...
    def convert(self, obj: np.generic, gateway_client: GatewayClient) -> Any: ...

class NumpyArrayConverter:
    def can_convert(self, obj: Any) -> bool: ...
    def convert(self, obj: np.ndarray, gateway_client: GatewayClient) -> JavaObject: ...
