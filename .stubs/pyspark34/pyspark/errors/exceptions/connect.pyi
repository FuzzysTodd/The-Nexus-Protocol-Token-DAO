from _typeshed import Incomplete
from google.rpc.error_details_pb2 import ErrorInfo as ErrorInfo
from pyspark.errors.exceptions.base import AnalysisException as BaseAnalysisException, ArithmeticException as BaseArithmeticException, ArrayIndexOutOfBoundsException as BaseArrayIndexOutOfBoundsException, DateTimeException as BaseDateTimeException, IllegalArgumentException as BaseIllegalArgumentException, NumberFormatException as BaseNumberFormatException, ParseException as BaseParseException, PySparkException as PySparkException, PythonException as BasePythonException, QueryExecutionException as BaseQueryExecutionException, SparkRuntimeException as BaseSparkRuntimeException, SparkUpgradeException as BaseSparkUpgradeException, StreamingQueryException as BaseStreamingQueryException
from typing import Dict

class SparkConnectException(PySparkException):
    """
    Exception thrown from Spark Connect.
    """

def convert_exception(info: ErrorInfo, message: str) -> SparkConnectException: ...

class SparkConnectGrpcException(SparkConnectException):
    """
    Base class to handle the errors from GRPC.
    """
    message: Incomplete
    def __init__(self, message: str | None = None, error_class: str | None = None, message_parameters: Dict[str, str] | None = None, reason: str | None = None) -> None: ...

class AnalysisException(SparkConnectGrpcException, BaseAnalysisException):
    """
    Failed to analyze a SQL query plan, thrown from Spark Connect.
    """
class ParseException(AnalysisException, BaseParseException):
    """
    Failed to parse a SQL command, thrown from Spark Connect.
    """
class IllegalArgumentException(SparkConnectGrpcException, BaseIllegalArgumentException):
    """
    Passed an illegal or inappropriate argument, thrown from Spark Connect.
    """
class StreamingQueryException(SparkConnectGrpcException, BaseStreamingQueryException):
    """
    Exception that stopped a :class:`StreamingQuery` thrown from Spark Connect.
    """
class QueryExecutionException(SparkConnectGrpcException, BaseQueryExecutionException):
    """
    Failed to execute a query, thrown from Spark Connect.
    """
class PythonException(SparkConnectGrpcException, BasePythonException):
    """
    Exceptions thrown from Spark Connect.
    """
class ArithmeticException(SparkConnectGrpcException, BaseArithmeticException):
    """
    Arithmetic exception thrown from Spark Connect.
    """
class ArrayIndexOutOfBoundsException(SparkConnectGrpcException, BaseArrayIndexOutOfBoundsException):
    """
    Array index out of bounds exception thrown from Spark Connect.
    """
class DateTimeException(SparkConnectGrpcException, BaseDateTimeException):
    """
    Datetime exception thrown from Spark Connect.
    """
class NumberFormatException(IllegalArgumentException, BaseNumberFormatException):
    """
    Number format exception thrown from Spark Connect.
    """
class SparkRuntimeException(SparkConnectGrpcException, BaseSparkRuntimeException):
    """
    Runtime exception thrown from Spark Connect.
    """
class SparkUpgradeException(SparkConnectGrpcException, BaseSparkUpgradeException):
    """
    Exception thrown because of Spark upgrade from Spark Connect.
    """
