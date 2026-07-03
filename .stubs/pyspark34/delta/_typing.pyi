from pyspark.sql.column import Column
from typing import Dict, Optional, Union

ExpressionOrColumn = Union[str, Column]
OptionalExpressionOrColumn = Optional[ExpressionOrColumn]
ColumnMapping = Dict[str, ExpressionOrColumn]
OptionalColumnMapping = Optional[ColumnMapping]
