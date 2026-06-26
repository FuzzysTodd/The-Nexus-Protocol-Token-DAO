from _typeshed import Incomplete
from azure.core.pipeline.policies import RequestHistory
from typing import Any, Generic, List, Mapping, TypeVar
from typing_extensions import Protocol

__all__ = ['AzureError', 'ServiceRequestError', 'ServiceResponseError', 'HttpResponseError', 'DecodeError', 'ResourceExistsError', 'ResourceNotFoundError', 'ClientAuthenticationError', 'ResourceModifiedError', 'ResourceNotModifiedError', 'TooManyRedirectsError', 'ODataV4Format', 'ODataV4Error', 'StreamConsumedError', 'StreamClosedError', 'ResponseNotReadError', 'SerializationError', 'DeserializationError']

HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')
KeyType = TypeVar('KeyType')
ValueType = TypeVar('ValueType')
SelfODataV4Format = TypeVar('SelfODataV4Format', bound='ODataV4Format')

class _HttpResponseCommonAPI(Protocol):
    """Protocol used by exceptions for HTTP response.

    As HttpResponseError uses very few properties of HttpResponse, a protocol
    is faster and simpler than import all the possible types (at least 6).
    """
    @property
    def reason(self) -> str | None: ...
    @property
    def status_code(self) -> int | None: ...
    def text(self) -> str: ...
    @property
    def request(self) -> object: ...

class ErrorMap(Generic[KeyType, ValueType]):
    """Error Map class. To be used in map_error method, behaves like a dictionary.
    It returns the error type if it is found in custom_error_map. Or return default_error

    :param dict custom_error_map: User-defined error map, it is used to map status codes to error types.
    :keyword error default_error: Default error type. It is returned if the status code is not found in custom_error_map
    """
    def __init__(self, custom_error_map: Mapping[KeyType, ValueType] | None = None, *, default_error: ValueType | None = None, **kwargs: Any) -> None: ...
    def get(self, key: KeyType) -> ValueType | None: ...

class ODataV4Format:
    '''Class to describe OData V4 error format.

    http://docs.oasis-open.org/odata/odata-json-format/v4.0/os/odata-json-format-v4.0-os.html#_Toc372793091

    Example of JSON:

    error: {
        "code": "ValidationError",
        "message": "One or more fields contain incorrect values: ",
        "details": [
            {
                "code": "ValidationError",
                "target": "representation",
                "message": "Parsing error(s): String \'\' does not match regex pattern \'^[^{}/ :]+(?: :\\\\d+)?$\'.
                Path \'host\', line 1, position 297."
            },
            {
                "code": "ValidationError",
                "target": "representation",
                "message": "Parsing error(s): The input OpenAPI file is not valid for the OpenAPI specificate
                https: //github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
                (schema https://github.com/OAI/OpenAPI-Specification/blob/master/schemas/v2.0/schema.json)."
            }
        ]
    }

    :param dict json_object: A Python dict representing a ODataV4 JSON
    :ivar str ~.code: Its value is a service-defined error code.
     This code serves as a sub-status for the HTTP error code specified in the response.
    :ivar str message: Human-readable, language-dependent representation of the error.
    :ivar str target: The target of the particular error (for example, the name of the property in error).
     This field is optional and may be None.
    :ivar list[ODataV4Format] details: Array of ODataV4Format instances that MUST contain name/value pairs
     for code and message, and MAY contain a name/value pair for target, as described above.
    :ivar dict innererror: An object. The contents of this object are service-defined.
     Usually this object contains information that will help debug the service.
    '''
    CODE_LABEL: str
    MESSAGE_LABEL: str
    TARGET_LABEL: str
    DETAILS_LABEL: str
    INNERERROR_LABEL: str
    code: Incomplete
    message: Incomplete
    target: Incomplete
    details: Incomplete
    innererror: Incomplete
    def __init__(self, json_object: Mapping[str, Any]) -> None: ...
    @property
    def error(self) -> SelfODataV4Format: ...
    def message_details(self) -> str:
        """Return a detailed string of the error.

        :return: A string with the details of the error.
        :rtype: str
        """

class AzureError(Exception):
    """Base exception for all errors.

    :param object message: The message object stringified as 'message' attribute
    :keyword error: The original exception if any
    :paramtype error: Exception

    :ivar inner_exception: The exception passed with the 'error' kwarg
    :vartype inner_exception: Exception
    :ivar exc_type: The exc_type from sys.exc_info()
    :ivar exc_value: The exc_value from sys.exc_info()
    :ivar exc_traceback: The exc_traceback from sys.exc_info()
    :ivar exc_msg: A string formatting of message parameter, exc_type and exc_value
    :ivar str message: A stringified version of the message parameter
    :ivar str continuation_token: A token reference to continue an incomplete operation. This value is optional
     and will be `None` where continuation is either unavailable or not applicable.
    """
    inner_exception: Incomplete
    exc_type: Incomplete
    exc_value: Incomplete
    exc_traceback: Incomplete
    exc_msg: Incomplete
    message: Incomplete
    continuation_token: Incomplete
    def __init__(self, message: object | None, *args: Any, **kwargs: Any) -> None: ...
    __traceback__: Incomplete
    def raise_with_traceback(self) -> None:
        """Raise the exception with the existing traceback.

        .. deprecated:: 1.22.0
           This method is deprecated as we don't support Python 2 anymore. Use raise/from instead.
        """

class ServiceRequestError(AzureError):
    """An error occurred while attempt to make a request to the service.
    No request was sent.
    """
class ServiceResponseError(AzureError):
    """The request was sent, but the client failed to understand the response.
    The connection may have timed out. These errors can be retried for idempotent or
    safe operations"""
class ServiceRequestTimeoutError(ServiceRequestError):
    """Error raised when timeout happens"""
class ServiceResponseTimeoutError(ServiceResponseError):
    """Error raised when timeout happens"""

class HttpResponseError(AzureError):
    """A request was made, and a non-success status code was received from the service.

    :param object message: The message object stringified as 'message' attribute
    :param response: The response that triggered the exception.
    :type response: ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse

    :ivar reason: The HTTP response reason
    :vartype reason: str
    :ivar status_code: HttpResponse's status code
    :vartype status_code: int
    :ivar response: The response that triggered the exception.
    :vartype response: ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse
    :ivar model: The request body/response body model
    :vartype model: ~msrest.serialization.Model
    :ivar error: The formatted error
    :vartype error: ODataV4Format
    """
    reason: Incomplete
    status_code: Incomplete
    response: Incomplete
    model: Incomplete
    error: Incomplete
    def __init__(self, message: object | None = None, response: _HttpResponseCommonAPI | None = None, **kwargs: Any) -> None: ...

class DecodeError(HttpResponseError):
    """Error raised during response deserialization."""
class IncompleteReadError(DecodeError):
    """Error raised if peer closes the connection before we have received the complete message body."""
class ResourceExistsError(HttpResponseError):
    """An error response with status code 4xx.
    This will not be raised directly by the Azure core pipeline."""
class ResourceNotFoundError(HttpResponseError):
    """An error response, typically triggered by a 412 response (for update) or 404 (for get/post)"""
class ClientAuthenticationError(HttpResponseError):
    """An error response with status code 4xx.
    This will not be raised directly by the Azure core pipeline."""
class ResourceModifiedError(HttpResponseError):
    """An error response with status code 4xx, typically 412 Conflict.
    This will not be raised directly by the Azure core pipeline."""
class ResourceNotModifiedError(HttpResponseError):
    """An error response with status code 304.
    This will not be raised directly by the Azure core pipeline."""

class TooManyRedirectsError(HttpResponseError, Generic[HTTPRequestType, HTTPResponseType]):
    """Reached the maximum number of redirect attempts.

    :param history: The history of requests made while trying to fulfill the request.
    :type history: list[~azure.core.pipeline.policies.RequestHistory]
    """
    history: Incomplete
    def __init__(self, history: List[RequestHistory[HTTPRequestType, HTTPResponseType]], *args: Any, **kwargs: Any) -> None: ...

class ODataV4Error(HttpResponseError):
    """An HTTP response error where the JSON is decoded as OData V4 error format.

    http://docs.oasis-open.org/odata/odata-json-format/v4.0/os/odata-json-format-v4.0-os.html#_Toc372793091

    :param ~azure.core.rest.HttpResponse response: The response object.
    :ivar dict odata_json: The parsed JSON body as attribute for convenience.
    :ivar str ~.code: Its value is a service-defined error code.
     This code serves as a sub-status for the HTTP error code specified in the response.
    :ivar str message: Human-readable, language-dependent representation of the error.
    :ivar str target: The target of the particular error (for example, the name of the property in error).
     This field is optional and may be None.
    :ivar list[ODataV4Format] details: Array of ODataV4Format instances that MUST contain name/value pairs
     for code and message, and MAY contain a name/value pair for target, as described above.
    :ivar dict innererror: An object. The contents of this object are service-defined.
     Usually this object contains information that will help debug the service.
    """
    odata_json: Incomplete
    code: Incomplete
    target: Incomplete
    details: Incomplete
    innererror: Incomplete
    def __init__(self, response: _HttpResponseCommonAPI, **kwargs: Any) -> None: ...

class StreamConsumedError(AzureError):
    """Error thrown if you try to access the stream of a response once consumed.

    It is thrown if you try to read / stream an ~azure.core.rest.HttpResponse or
    ~azure.core.rest.AsyncHttpResponse once the response's stream has been consumed.

    :param response: The response that triggered the exception.
    :type response: ~azure.core.rest.HttpResponse or ~azure.core.rest.AsyncHttpResponse
    """
    def __init__(self, response: _HttpResponseCommonAPI) -> None: ...

class StreamClosedError(AzureError):
    """Error thrown if you try to access the stream of a response once closed.

    It is thrown if you try to read / stream an ~azure.core.rest.HttpResponse or
    ~azure.core.rest.AsyncHttpResponse once the response's stream has been closed.

    :param response: The response that triggered the exception.
    :type response: ~azure.core.rest.HttpResponse or ~azure.core.rest.AsyncHttpResponse
    """
    def __init__(self, response: _HttpResponseCommonAPI) -> None: ...

class ResponseNotReadError(AzureError):
    """Error thrown if you try to access a response's content without reading first.

    It is thrown if you try to access an ~azure.core.rest.HttpResponse or
    ~azure.core.rest.AsyncHttpResponse's content without first reading the response's bytes in first.

    :param response: The response that triggered the exception.
    :type response: ~azure.core.rest.HttpResponse or ~azure.core.rest.AsyncHttpResponse
    """
    def __init__(self, response: _HttpResponseCommonAPI) -> None: ...

class SerializationError(ValueError):
    """Raised if an error is encountered during serialization."""
class DeserializationError(ValueError):
    """Raised if an error is encountered during deserialization."""
