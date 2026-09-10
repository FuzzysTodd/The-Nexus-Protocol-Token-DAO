import datetime
from _typeshed import Incomplete
from pandas.core.frame import DataFrame as PandasDataFrame
from pyspark.sql.connect.column import Column as Column
from pyspark.sql.connect.types import DataType as DataType
from typing import Any, Callable, Iterable, Protocol

ColumnOrName = Column | str
PrimitiveType = bool | float | int | str
OptionalPrimitiveType = PrimitiveType | None
LiteralType = PrimitiveType
DecimalLiteral: Incomplete
DateTimeLiteral = datetime.datetime | datetime.date
DataTypeOrString = DataType | str
DataFrameLike = PandasDataFrame
PandasMapIterFunction = Callable[[Iterable[DataFrameLike]], Iterable[DataFrameLike]]
ArrowMapIterFunction: Incomplete
PandasGroupedMapFunction = Callable[[DataFrameLike], DataFrameLike] | Callable[[Any, DataFrameLike], DataFrameLike]
GroupedMapPandasUserDefinedFunction: Incomplete
PandasCogroupedMapFunction = Callable[[DataFrameLike, DataFrameLike], DataFrameLike]

class UserDefinedFunctionLike(Protocol):
    func: Callable[..., Any]
    evalType: int
    deterministic: bool
    @property
    def returnType(self) -> DataType: ...
    def __call__(self, *args: ColumnOrName) -> Column: ...
    def asNondeterministic(self) -> UserDefinedFunctionLike: ...

class UserDefinedFunctionCallable(Protocol):
    def __call__(self, *_: ColumnOrName) -> Column: ...
