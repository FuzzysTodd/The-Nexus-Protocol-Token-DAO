from inspect import Signature
from pyspark.sql.pandas._typing import PandasGroupedAggUDFType as PandasGroupedAggUDFType, PandasScalarIterUDFType as PandasScalarIterUDFType, PandasScalarUDFType as PandasScalarUDFType
from pyspark.sql.pandas.utils import require_minimum_pandas_version as require_minimum_pandas_version
from typing import Any, Callable, Dict

def infer_eval_type(sig: Signature, type_hints: Dict[str, Any]) -> PandasScalarUDFType | PandasScalarIterUDFType | PandasGroupedAggUDFType:
    """
    Infers the evaluation type in :class:`pyspark.rdd.PythonEvalType` from
    :class:`inspect.Signature` instance and type hints.
    """
def check_tuple_annotation(annotation: Any, parameter_check_func: Callable[[Any], bool] | None = None) -> bool: ...
def check_iterator_annotation(annotation: Any, parameter_check_func: Callable[[Any], bool] | None = None) -> bool: ...
def check_union_annotation(annotation: Any, parameter_check_func: Callable[[Any], bool] | None = None) -> bool: ...
