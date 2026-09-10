import string
from pyspark.sql import DataFrame as DataFrame, SparkSession as SparkSession
from pyspark.sql.functions import lit as lit
from typing import Any, Mapping, Sequence

class SQLStringFormatter(string.Formatter):
    """
    A standard ``string.Formatter`` in Python that can understand PySpark instances
    with basic Python objects. This object has to be clear after the use for single SQL
    query; cannot be reused across multiple SQL queries without cleaning.
    """
    def __init__(self, session: SparkSession) -> None: ...
    def get_field(self, field_name: str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> Any: ...
    def clear(self) -> None: ...
