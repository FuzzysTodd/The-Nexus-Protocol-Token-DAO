import logging
from _typeshed import Incomplete
from logging import Logger
from sempy._version import get_versions as get_versions

SEMPY_LOGGER_NAME: str
MDS_LOG_TABLE: str
mds_fields: dict

class DecoratorJSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord): ...
    def formatException(self, exc_info):
        """
        Override the default formatException to place exception type and error first.

        Also, inverts the stack sequence to go from top to bottom while skipping
        irrelelevant information.
        """

class ScrubbingFormatter(DecoratorJSONFormatter):
    """
    We need to differentiate scrubbing depending on where the exception was raised from,
    so we place scrubbing in the decorator, where we have access to the exception details.
    The IScrub implementation of pymds, applies simple string replacement based solely on
    the message text.
    """
    def format(self, record: logging.LogRecord): ...
    def formatException(self, exc_info): ...

class MdsExtractor:
    """
    Base extraction class used for standard logging.

    Parameters
    ----------
    logger : Logger
        Logger object used for telemetry.
    """
    logger: Incomplete
    start_time: Incomplete
    def __init__(self, logger: Logger | None = None) -> None: ...
    def get_initialization_mds_fields(self) -> dict:
        '''
        Returns the columns used for telemetry (prefixed with "mds").
        Executes BEFORE function execution.

        Returns
        -------
        Dict
            Mds column identifiers and their values.
        '''
    def get_completion_message_dict(self, result, arg_dict) -> dict:
        """
        Returns dictionary of key/value pairs that will be present in the log message.
        Executes AFTER function execution.

        Parameters
        ----------
        result : Any
            Object returned from function execution.
        arg_dict : Dict
            Arguments passed to function.

        Returns
        -------
        Dict[str, str]
            Additional message key/value pairs.
        """
    def get_execution_time(self, digits: int = 3) -> float:
        """
        Returns how long the function took to execute, based on provided start time.

        Parameters
        ----------
        digits : int, default=3
            How many significant digits to round result to.

        Returns
        -------
        float
            Execution time in seconds, rounded to provided significant digits.
        """

def mds_log(extractor: MdsExtractor = ..., log_level: int = ...): ...

class SemPyExtractor(MdsExtractor):
    """
    Base extraction class used for standard SemPy logging. Has logic for redacting and formatting values.
    """
    logger: Incomplete
    def __init__(self) -> None: ...
    def get_initialization_mds_fields(self) -> dict: ...
    def get_completion_message_dict(self, result, arg_dict) -> dict: ...

class TablesExtractor(SemPyExtractor):
    """
    Extraction class used for logging functions which have tables in the result.
    """
    def get_completion_message_dict(self, result, arg_dict) -> dict: ...

class RetryExtractor(SemPyExtractor):
    """
    Extraction class used for logging REST retries.
    """
    def get_completion_message_dict(self, result, arg_dict) -> dict: ...

class RestRequestExtractor(SemPyExtractor):
    """
    Extraction class used for logging REST requests.
    """
    def get_completion_message_dict(self, result, arg_dict) -> dict: ...

class RestResponseExtractor(SemPyExtractor):
    """
    Extraction class used for logging REST responses.
    """
    def get_completion_message_dict(self, result, arg_dict) -> dict: ...

class XmlaExtractor(SemPyExtractor):
    """
    Extraction class used for logging XMLA operations.
    This sets up the relevant correlation ID using Trace.CorrelationManager.
    """
    def get_initialization_mds_fields(self) -> dict: ...
    def get_completion_message_dict(self, result, arg_dict) -> dict: ...

log: Incomplete
log_error: Incomplete
log_retry: Incomplete
log_tables: Incomplete
log_rest_request: Incomplete
log_rest_response: Incomplete
log_xmla: Incomplete
