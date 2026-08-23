from _typeshed import Incomplete
from typing import NamedTuple

class CallSite(NamedTuple):
    function: Incomplete
    file: Incomplete
    linenum: Incomplete

def first_spark_call():
    """
    Return a CallSite representing the first Spark call in the current call stack.
    """

class SCCallSiteSync:
    """
    Helper for setting the spark context call site.

    Example usage:
    from pyspark.context import SCCallSiteSync
    with SCCallSiteSync(<relevant SparkContext>) as css:
        <a Spark call>
    """
    def __init__(self, sc) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
