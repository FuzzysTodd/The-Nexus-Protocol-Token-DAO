from _typeshed import Incomplete
from pyspark.pandas.base import IndexOpsMixin as IndexOpsMixin
from pyspark.sql import Column as Column
from pyspark.sql.pandas.functions import pandas_udf as pandas_udf
from pyspark.sql.types import BooleanType as BooleanType, DoubleType as DoubleType, LongType as LongType
from typing import Any, Callable

unary_np_spark_mappings: Incomplete
binary_np_spark_mappings: Incomplete

def maybe_dispatch_ufunc_to_dunder_op(ser_or_index: IndexOpsMixin, ufunc: Callable, method: str, *inputs: Any, **kwargs: Any) -> IndexOpsMixin: ...
def maybe_dispatch_ufunc_to_spark_func(ser_or_index: IndexOpsMixin, ufunc: Callable, method: str, *inputs: Any, **kwargs: Any) -> IndexOpsMixin: ...
