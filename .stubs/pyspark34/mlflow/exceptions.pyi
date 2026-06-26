from _typeshed import Incomplete
from mlflow.protos.databricks_pb2 import ABORTED as ABORTED, ALREADY_EXISTS as ALREADY_EXISTS, BAD_REQUEST as BAD_REQUEST, CANCELLED as CANCELLED, CUSTOMER_UNAUTHORIZED as CUSTOMER_UNAUTHORIZED, DATA_LOSS as DATA_LOSS, DEADLINE_EXCEEDED as DEADLINE_EXCEEDED, ENDPOINT_NOT_FOUND as ENDPOINT_NOT_FOUND, ErrorCode as ErrorCode, INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, INVALID_STATE as INVALID_STATE, NOT_FOUND as NOT_FOUND, NOT_IMPLEMENTED as NOT_IMPLEMENTED, PERMISSION_DENIED as PERMISSION_DENIED, REQUEST_LIMIT_EXCEEDED as REQUEST_LIMIT_EXCEEDED, RESOURCE_ALREADY_EXISTS as RESOURCE_ALREADY_EXISTS, RESOURCE_CONFLICT as RESOURCE_CONFLICT, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST, RESOURCE_EXHAUSTED as RESOURCE_EXHAUSTED, TEMPORARILY_UNAVAILABLE as TEMPORARILY_UNAVAILABLE, UNAUTHENTICATED as UNAUTHENTICATED

ERROR_CODE_TO_HTTP_STATUS: Incomplete
HTTP_STATUS_TO_ERROR_CODE: Incomplete

def get_error_code(http_status): ...

class MlflowException(Exception):
    """
    Generic exception thrown to surface failure information about external-facing operations.
    The error message associated with this exception may be exposed to clients in HTTP responses
    for debugging purposes. If the error text is sensitive, raise a generic `Exception` object
    instead.
    """
    error_code: Incomplete
    message: Incomplete
    json_kwargs: Incomplete
    def __init__(self, message, error_code=..., **kwargs) -> None:
        """
        :param message: The message or exception describing the error that occurred. This will be
                        included in the exception's serialized JSON representation.
        :param error_code: An appropriate error code for the error that occurred; it will be
                           included in the exception's serialized JSON representation. This should
                           be one of the codes listed in the `mlflow.protos.databricks_pb2` proto.
        :param kwargs: Additional key-value pairs to include in the serialized JSON representation
                       of the MlflowException.
        """
    def serialize_as_json(self): ...
    def get_http_status_code(self): ...
    @classmethod
    def invalid_parameter_value(cls, message, **kwargs):
        """
        Constructs an `MlflowException` object with the `INVALID_PARAMETER_VALUE` error code.

        :param message: The message describing the error that occurred. This will be included in the
                        exception's serialized JSON representation.
        :param kwargs: Additional key-value pairs to include in the serialized JSON representation
                       of the MlflowException.
        """

class RestException(MlflowException):
    """Exception thrown on non 200-level responses from the REST API"""
    json: Incomplete
    def __init__(self, json) -> None: ...

class ExecutionException(MlflowException):
    """Exception thrown when executing a project fails"""
class MissingConfigException(MlflowException):
    """Exception thrown when expected configuration file/directory not found"""
class InvalidUrlException(MlflowException):
    """Exception thrown when a http request fails to send due to an invalid URL"""
