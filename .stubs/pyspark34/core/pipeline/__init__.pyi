from ._base import Pipeline as Pipeline
from ._base_async import AsyncPipeline as AsyncPipeline
from .transport import AsyncHttpTransport, HttpTransport
from _typeshed import Incomplete
from typing import Any, Dict, Generic, Tuple, TypeVar, overload

__all__ = ['Pipeline', 'PipelineRequest', 'PipelineResponse', 'PipelineContext', 'AsyncPipeline']

HTTPResponseType = TypeVar('HTTPResponseType', covariant=True)
HTTPRequestType = TypeVar('HTTPRequestType', covariant=True)
TransportType = HttpTransport[Any, Any] | AsyncHttpTransport[Any, Any]

class PipelineContext(Dict[str, Any]):
    '''A context object carried by the pipeline request and response containers.

    This is transport specific and can contain data persisted between
    pipeline requests (for example reusing an open connection pool or "session"),
    as well as used by the SDK developer to carry arbitrary data through
    the pipeline.

    :param transport: The HTTP transport type.
    :type transport: ~azure.core.pipeline.transport.HttpTransport or ~azure.core.pipeline.transport.AsyncHttpTransport
    :param any kwargs: Developer-defined keyword arguments.
    '''
    transport: Incomplete
    options: Incomplete
    def __init__(self, transport: TransportType | None, **kwargs: Any) -> None: ...
    def __reduce__(self) -> Tuple[Any, ...]: ...
    def __setitem__(self, key: str, item: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def clear(self) -> None:
        """Context objects cannot be cleared.

        :raises: TypeError
        """
    def update(self, *args: Any, **kwargs: Any) -> None:
        """Context objects cannot be updated.

        :raises: TypeError
        """
    @overload
    def pop(self, __key: str) -> Any: ...
    @overload
    def pop(self, __key: str, __default: Any | None) -> Any: ...

class PipelineRequest(Generic[HTTPRequestType]):
    """A pipeline request object.

    Container for moving the HttpRequest through the pipeline.
    Universal for all transports, both synchronous and asynchronous.

    :param http_request: The request object.
    :type http_request: ~azure.core.pipeline.transport.HttpRequest
    :param context: Contains the context - data persisted between pipeline requests.
    :type context: ~azure.core.pipeline.PipelineContext
    """
    http_request: Incomplete
    context: Incomplete
    def __init__(self, http_request: HTTPRequestType, context: PipelineContext) -> None: ...

class PipelineResponse(Generic[HTTPRequestType, HTTPResponseType]):
    '''A pipeline response object.

    The PipelineResponse interface exposes an HTTP response object as it returns through the pipeline of Policy objects.
    This ensures that Policy objects have access to the HTTP response.

    This also has a "context" object where policy can put additional fields.
    Policy SHOULD update the "context" with additional post-processed field if they create them.
    However, nothing prevents a policy to actually sub-class this class a return it instead of the initial instance.

    :param http_request: The request object.
    :type http_request: ~azure.core.pipeline.transport.HttpRequest
    :param http_response: The response object.
    :type http_response: ~azure.core.pipeline.transport.HttpResponse
    :param context: Contains the context - data persisted between pipeline requests.
    :type context: ~azure.core.pipeline.PipelineContext
    '''
    http_request: Incomplete
    http_response: Incomplete
    context: Incomplete
    def __init__(self, http_request: HTTPRequestType, http_response: HTTPResponseType, context: PipelineContext) -> None: ...
