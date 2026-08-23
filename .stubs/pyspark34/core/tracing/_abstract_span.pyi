from _typeshed import Incomplete
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest, HttpResponse
from azure.core.rest import AsyncHttpResponse as AsyncRestHttpResponse, HttpRequest as RestHttpRequest, HttpResponse as RestHttpResponse
from enum import Enum
from types import TracebackType
from typing import Any, Callable, Dict, Generic, Sequence, Type, TypeVar
from typing_extensions import ContextManager, Protocol

HttpResponseType = HttpResponse | AsyncHttpResponse | RestHttpResponse | AsyncRestHttpResponse
HttpRequestType = HttpRequest | RestHttpRequest
AttributeValue = str | bool | int | float | Sequence[str] | Sequence[bool] | Sequence[int] | Sequence[float]
Attributes = Dict[str, AttributeValue]
SpanType = TypeVar('SpanType')

class SpanKind(Enum):
    UNSPECIFIED: int
    SERVER: int
    CLIENT: int
    PRODUCER: int
    CONSUMER: int
    INTERNAL: int

class AbstractSpan(Generic[SpanType], Protocol):
    """Wraps a span from a distributed tracing implementation.

    If a span is given wraps the span. Else a new span is created.
    The optional argument name is given to the new span.

    :param span: The span to wrap
    :type span: Any
    :param name: The name of the span
    :type name: str
    """
    def __init__(self, span: SpanType | None = None, name: str | None = None, **kwargs: Any) -> None: ...
    def span(self, name: str = 'child_span', **kwargs: Any) -> AbstractSpan[SpanType]:
        """
        Create a child span for the current span and append it to the child spans list.
        The child span must be wrapped by an implementation of AbstractSpan

        :param name: The name of the child span
        :type name: str
        :return: The child span
        :rtype: AbstractSpan
        """
    @property
    def kind(self) -> SpanKind | None:
        """Get the span kind of this span.

        :rtype: SpanKind
        :return: The span kind of this span
        """
    @kind.setter
    def kind(self, value: SpanKind) -> None:
        """Set the span kind of this span.

        :param value: The span kind of this span
        :type value: SpanKind
        """
    def __enter__(self) -> AbstractSpan[SpanType]:
        """Start a span."""
    def __exit__(self, exception_type: Type[BaseException] | None, exception_value: BaseException | None, traceback: TracebackType) -> None:
        """Finish a span.

        :param exception_type: The type of the exception
        :type exception_type: type
        :param exception_value: The value of the exception
        :type exception_value: Exception
        :param traceback: The traceback of the exception
        :type traceback: Traceback
        """
    def start(self) -> None:
        """Set the start time for a span."""
    def finish(self) -> None:
        """Set the end time for a span."""
    def to_header(self) -> Dict[str, str]:
        """Returns a dictionary with the header labels and values.

        :return: A dictionary with the header labels and values
        :rtype: dict
        """
    def add_attribute(self, key: str, value: str | int) -> None:
        """
        Add attribute (key value pair) to the current span.

        :param key: The key of the key value pair
        :type key: str
        :param value: The value of the key value pair
        :type value: Union[str, int]
        """
    def set_http_attributes(self, request: HttpRequestType, response: HttpResponseType | None = None) -> None:
        """
        Add correct attributes for a http client span.

        :param request: The request made
        :type request: HttpRequest
        :param response: The response received by the server. Is None if no response received.
        :type response: ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse
        """
    def get_trace_parent(self) -> str:
        """Return traceparent string.

        :return: a traceparent string
        :rtype: str
        """
    @property
    def span_instance(self) -> SpanType:
        """
        Returns the span the class is wrapping.
        """
    @classmethod
    def link(cls, traceparent: str, attributes: Attributes | None = None) -> None:
        """
        Given a traceparent, extracts the context and links the context to the current tracer.

        :param traceparent: A string representing a traceparent
        :type traceparent: str
        :param attributes: Any additional attributes that should be added to link
        :type attributes: dict
        """
    @classmethod
    def link_from_headers(cls, headers: Dict[str, str], attributes: Attributes | None = None) -> None:
        """
        Given a dictionary, extracts the context and links the context to the current tracer.

        :param headers: A dictionary of the request header as key value pairs.
        :type headers: dict
        :param attributes: Any additional attributes that should be added to link
        :type attributes: dict
        """
    @classmethod
    def get_current_span(cls) -> SpanType:
        """
        Get the current span from the execution context. Return None otherwise.

        :return: The current span
        :rtype: AbstractSpan
        """
    @classmethod
    def get_current_tracer(cls) -> Any:
        """
        Get the current tracer from the execution context. Return None otherwise.

        :return: The current tracer
        :rtype: Any
        """
    @classmethod
    def set_current_span(cls, span: SpanType) -> None:
        """Set the given span as the current span in the execution context.

        :param span: The span to set as the current span
        :type span: Any
        """
    @classmethod
    def set_current_tracer(cls, tracer: Any) -> None:
        """Set the given tracer as the current tracer in the execution context.

        :param tracer: The tracer to set as the current tracer
        :type tracer: Any
        """
    @classmethod
    def change_context(cls, span: SpanType) -> ContextManager[SpanType]:
        """Change the context for the life of this context manager.

        :param span: The span to run in the new context
        :type span: Any
        :rtype: contextmanager
        :return: A context manager that will run the given span in the new context
        """
    @classmethod
    def with_current_context(cls, func: Callable) -> Callable:
        """Passes the current spans to the new context the function will be run in.

        :param func: The function that will be run in the new context
        :type func: callable
        :return: The target the pass in instead of the function
        :rtype: callable
        """

class HttpSpanMixin:
    """Can be used to get HTTP span attributes settings for free."""
    kind: Incomplete
    def set_http_attributes(self, request: HttpRequestType, response: HttpResponseType | None = None) -> None:
        """
        Add correct attributes for a http client span.

        :param request: The request made
        :type request: HttpRequest
        :param response: The response received from the server. Is None if no response received.
        :type response: ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse
        """

class Link:
    """
    This is a wrapper class to link the context to the current tracer.
    :param headers: A dictionary of the request header as key value pairs.
    :type headers: dict
    :param attributes: Any additional attributes that should be added to link
    :type attributes: dict
    """
    headers: Incomplete
    attributes: Incomplete
    def __init__(self, headers: Dict[str, str], attributes: Attributes | None = None) -> None: ...
