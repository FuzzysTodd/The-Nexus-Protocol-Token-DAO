from _typeshed import Incomplete
from py4j.java_collections import JavaArray as JavaArray
from py4j.java_gateway import JavaClass as JavaClass, JavaGateway as JavaGateway, JavaObject as JavaObject
from pyspark import SparkContext as SparkContext
from pyspark.errors import AnalysisException as AnalysisException, IllegalArgumentException as IllegalArgumentException, ParseException as ParseException, PythonException as PythonException, QueryExecutionException as QueryExecutionException, SparkUpgradeException as SparkUpgradeException, StreamingQueryException as StreamingQueryException, UnknownException as UnknownException
from pyspark.errors.exceptions.captured import CapturedException as CapturedException
from pyspark.sql.dataframe import DataFrame as DataFrame
from pyspark.sql.session import SparkSession as SparkSession
from typing import Any, Callable, Sequence, TypeVar

has_numpy: bool
FuncT = TypeVar('FuncT', bound=Callable[..., Any])

def toJArray(gateway: JavaGateway, jtype: JavaClass, arr: Sequence[Any]) -> JavaArray:
    """
    Convert python list to java type array

    Parameters
    ----------
    gateway :
        Py4j Gateway
    jtype :
        java type of element in array
    arr :
        python type list
    """
def require_test_compiled() -> None:
    """Raise Exception if test classes are not compiled"""

class ForeachBatchFunction:
    """
    This is the Python implementation of Java interface 'ForeachBatchFunction'. This wraps
    the user-defined 'foreachBatch' function such that it can be called from the JVM when
    the query is active.
    """
    func: Incomplete
    session: Incomplete
    def __init__(self, session: SparkSession, func: Callable[[DataFrame, int], None]) -> None: ...
    error: Incomplete
    def call(self, jdf: JavaObject, batch_id: int) -> None: ...
    class Java:
        implements: Incomplete

def to_str(value: Any) -> str | None:
    '''
    A wrapper over str(), but converts bool values to lower case strings.
    If None is given, just returns None, instead of converting it to string "None".
    '''
def is_timestamp_ntz_preferred() -> bool:
    """
    Return a bool if TimestampNTZType is preferred according to the SQL configuration set.
    """
def is_remote() -> bool:
    """
    Returns if the current running environment is for Spark Connect.
    """
def try_remote_functions(f: FuncT) -> FuncT:
    """Mark API supported from Spark Connect."""
def try_remote_window(f: FuncT) -> FuncT:
    """Mark API supported from Spark Connect."""
def try_remote_windowspec(f: FuncT) -> FuncT:
    """Mark API supported from Spark Connect."""
def get_active_spark_context() -> SparkContext:
    """Raise RuntimeError if SparkContext is not initialized,
    otherwise, returns the active SparkContext."""
def try_remote_observation(f: FuncT) -> FuncT:
    """Mark API supported from Spark Connect."""
