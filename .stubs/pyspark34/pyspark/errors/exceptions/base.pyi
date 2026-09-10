from _typeshed import Incomplete
from pyspark.errors.utils import ErrorClassesReader as ErrorClassesReader
from typing import Dict

class PySparkException(Exception):
    """
    Base Exception for handling errors generated from PySpark.
    """
    error_reader: Incomplete
    message: Incomplete
    error_class: Incomplete
    message_parameters: Incomplete
    def __init__(self, message: str | None = None, error_class: str | None = None, message_parameters: Dict[str, str] | None = None) -> None: ...
    def getErrorClass(self) -> str | None:
        """
        Returns an error class as a string.

        .. versionadded:: 3.4.0

        See Also
        --------
        :meth:`PySparkException.getMessageParameters`
        :meth:`PySparkException.getSqlState`
        """
    def getMessageParameters(self) -> Dict[str, str] | None:
        """
        Returns a message parameters as a dictionary.

        .. versionadded:: 3.4.0

        See Also
        --------
        :meth:`PySparkException.getErrorClass`
        :meth:`PySparkException.getSqlState`
        """
    def getSqlState(self) -> None:
        """
        Returns an SQLSTATE as a string.

        Errors generated in Python have no SQLSTATE, so it always returns None.

        .. versionadded:: 3.4.0

        See Also
        --------
        :meth:`PySparkException.getErrorClass`
        :meth:`PySparkException.getMessageParameters`
        """

class AnalysisException(PySparkException):
    """
    Failed to analyze a SQL query plan.
    """
class TempTableAlreadyExistsException(AnalysisException):
    """
    Failed to create temp view since it is already exists.
    """
class ParseException(AnalysisException):
    """
    Failed to parse a SQL command.
    """
class IllegalArgumentException(PySparkException):
    """
    Passed an illegal or inappropriate argument.
    """
class ArithmeticException(PySparkException):
    """
    Arithmetic exception thrown from Spark with an error class.
    """
class ArrayIndexOutOfBoundsException(PySparkException):
    """
    Array index out of bounds exception thrown from Spark with an error class.
    """
class DateTimeException(PySparkException):
    """
    Datetime exception thrown from Spark with an error class.
    """
class NumberFormatException(IllegalArgumentException):
    """
    Number format exception thrown from Spark with an error class.
    """
class StreamingQueryException(PySparkException):
    """
    Exception that stopped a :class:`StreamingQuery`.
    """
class QueryExecutionException(PySparkException):
    """
    Failed to execute a query.
    """
class PythonException(PySparkException):
    """
    Exceptions thrown from Python workers.
    """
class SparkRuntimeException(PySparkException):
    """
    Runtime exception thrown from Spark with an error class.
    """
class SparkUpgradeException(PySparkException):
    """
    Exception thrown because of Spark upgrade.
    """
class UnknownException(PySparkException):
    """
    None of the above exceptions.
    """
class PySparkValueError(PySparkException, ValueError):
    """
    Wrapper class for ValueError to support error classes.
    """
class PySparkTypeError(PySparkException, TypeError):
    """
    Wrapper class for TypeError to support error classes.
    """
class PySparkAttributeError(PySparkException, AttributeError):
    """
    Wrapper class for AttributeError to support error classes.
    """
