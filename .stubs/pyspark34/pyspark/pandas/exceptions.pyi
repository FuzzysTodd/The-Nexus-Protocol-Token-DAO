from _typeshed import Incomplete

class DataError(Exception): ...
class SparkPandasIndexingError(Exception): ...

def code_change_hint(pandas_function: str | None, spark_target_function: str | None) -> str: ...

class SparkPandasNotImplementedError(NotImplementedError):
    pandas_source: Incomplete
    spark_target: Incomplete
    def __init__(self, pandas_function: str | None = None, spark_target_function: str | None = None, description: str = '') -> None: ...

class PandasNotImplementedError(NotImplementedError):
    class_name: Incomplete
    method_name: Incomplete
    arg_name: Incomplete
    def __init__(self, class_name: str, method_name: str | None = None, arg_name: str | None = None, property_name: str | None = None, scalar_name: str | None = None, deprecated: bool = False, reason: str = '') -> None: ...
