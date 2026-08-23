from _typeshed import Incomplete
from py4j.protocol import Py4JJavaError
from pyspark import SparkContext as SparkContext
from pyspark.errors.exceptions.base import AnalysisException as BaseAnalysisException, ArithmeticException as BaseArithmeticException, ArrayIndexOutOfBoundsException as BaseArrayIndexOutOfBoundsException, DateTimeException as BaseDateTimeException, IllegalArgumentException as BaseIllegalArgumentException, NumberFormatException as BaseNumberFormatException, ParseException as BaseParseException, PySparkException as PySparkException, PythonException as BasePythonException, QueryExecutionException as BaseQueryExecutionException, SparkRuntimeException as BaseSparkRuntimeException, SparkUpgradeException as BaseSparkUpgradeException, StreamingQueryException as BaseStreamingQueryException, UnknownException as BaseUnknownException
from typing import Any, Callable, Dict

class CapturedException(PySparkException):
    desc: Incomplete
    stackTrace: Incomplete
    cause: Incomplete
    def __init__(self, desc: str | None = None, stackTrace: str | None = None, cause: Py4JJavaError | None = None, origin: Py4JJavaError | None = None) -> None: ...
    def getErrorClass(self) -> str | None: ...
    def getMessageParameters(self) -> Dict[str, str] | None: ...
    def getSqlState(self) -> str | None: ...

def convert_exception(e: Py4JJavaError) -> CapturedException: ...
def capture_sql_exception(f: Callable[..., Any]) -> Callable[..., Any]: ...
def install_exception_handler() -> None:
    """
    Hook an exception handler into Py4j, which could capture some SQL exceptions in Java.

    When calling Java API, it will call `get_return_value` to parse the returned object.
    If any exception happened in JVM, the result will be Java exception object, it raise
    py4j.protocol.Py4JJavaError. We replace the original `get_return_value` with one that
    could capture the Java exception and throw a Python one (with the same error message).

    It's idempotent, could be called multiple times.
    """

class AnalysisException(CapturedException, BaseAnalysisException):
    """
    Failed to analyze a SQL query plan.
    """
class ParseException(AnalysisException, BaseParseException):
    """
    Failed to parse a SQL command.
    """
class IllegalArgumentException(CapturedException, BaseIllegalArgumentException):
    """
    Passed an illegal or inappropriate argument.
    """
class StreamingQueryException(CapturedException, BaseStreamingQueryException):
    """
    Exception that stopped a :class:`StreamingQuery`.
    """
class QueryExecutionException(CapturedException, BaseQueryExecutionException):
    """
    Failed to execute a query.
    """
class PythonException(CapturedException, BasePythonException):
    """
    Exceptions thrown from Python workers.
    """
class ArithmeticException(CapturedException, BaseArithmeticException):
    """
    Arithmetic exception.
    """
class ArrayIndexOutOfBoundsException(CapturedException, BaseArrayIndexOutOfBoundsException):
    """
    Array index out of bounds exception.
    """
class DateTimeException(CapturedException, BaseDateTimeException):
    """
    Datetime exception.
    """
class NumberFormatException(IllegalArgumentException, BaseNumberFormatException):
    """
    Number format exception.
    """
class SparkRuntimeException(CapturedException, BaseSparkRuntimeException):
    """
    Runtime exception.
    """
class SparkUpgradeException(CapturedException, BaseSparkUpgradeException):
    """
    Exception thrown because of Spark upgrade.
    """
class UnknownException(CapturedException, BaseUnknownException):
    """
    None of the above exceptions.
    """
