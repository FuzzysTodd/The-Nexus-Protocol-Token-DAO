import datetime
import decimal
import pyspark
import pyspark.sql.types
from _typeshed import Incomplete
from pyspark._typing import PrimitiveType as PrimitiveType
from pyspark.sql.column import Column as Column
from typing import Any, Callable, List, Tuple, TypeVar
from typing_extensions import Protocol

ColumnOrName = Column | str
ColumnOrName_ = TypeVar('ColumnOrName_', bound=ColumnOrName)
DecimalLiteral: Incomplete
DateTimeLiteral = datetime.datetime | datetime.date
LiteralType = PrimitiveType
AtomicDataTypeOrString = pyspark.sql.types.AtomicType | str
DataTypeOrString = pyspark.sql.types.DataType | str
OptionalPrimitiveType = PrimitiveType | None
AtomicValue = TypeVar('AtomicValue', datetime.datetime, datetime.date, decimal.Decimal, bool, str, int, float)
RowLike = TypeVar('RowLike', List[Any], Tuple[Any, ...], pyspark.sql.types.Row)
SQLBatchedUDFType: Incomplete

class SupportsOpen(Protocol):
    def open(self, partition_id: int, epoch_id: int) -> bool: ...

class SupportsProcess(Protocol):
    def process(self, row: pyspark.sql.types.Row) -> None: ...

class SupportsClose(Protocol):
    def close(self, error: Exception) -> None: ...

class UserDefinedFunctionLike(Protocol):
    func: Callable[..., Any]
    evalType: int
    deterministic: bool
    @property
    def returnType(self) -> pyspark.sql.types.DataType: ...
    def __call__(self, *args: ColumnOrName) -> Column: ...
    def asNondeterministic(self) -> UserDefinedFunctionLike: ...
