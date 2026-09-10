import sentry_sdk
import typing
from _typeshed import Incomplete
from datetime import datetime
from sentry_sdk._compat import PY2 as PY2, datetime_utcnow as datetime_utcnow
from sentry_sdk._types import Event as Event, MeasurementUnit as MeasurementUnit, SamplingContext as SamplingContext, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import INSTRUMENTER as INSTRUMENTER, SPANDATA as SPANDATA
from sentry_sdk.tracing_utils import Baggage as Baggage, EnvironHeaders as EnvironHeaders, extract_sentrytrace_data as extract_sentrytrace_data, has_tracing_enabled as has_tracing_enabled, maybe_create_breadcrumbs_from_span as maybe_create_breadcrumbs_from_span
from sentry_sdk.utils import is_valid_sample_rate as is_valid_sample_rate, logger as logger, nanosecond_time as nanosecond_time
from typing import Any, Dict, Iterator, Tuple

BAGGAGE_HEADER_NAME: str
SENTRY_TRACE_HEADER_NAME: str
TRANSACTION_SOURCE_CUSTOM: str
TRANSACTION_SOURCE_URL: str
TRANSACTION_SOURCE_ROUTE: str
TRANSACTION_SOURCE_VIEW: str
TRANSACTION_SOURCE_COMPONENT: str
TRANSACTION_SOURCE_TASK: str
LOW_QUALITY_TRANSACTION_SOURCES: Incomplete
SOURCE_FOR_STYLE: Incomplete

class _SpanRecorder:
    """Limits the number of spans recorded in a transaction."""
    maxlen: Incomplete
    spans: Incomplete
    def __init__(self, maxlen: int) -> None: ...
    def add(self, span: Span) -> None: ...

class Span:
    """A span holds timing information of a block of code.
    Spans can have multiple child spans thus forming a span tree."""
    def __new__(cls, **kwargs: Any) -> Any:
        """
        Backwards-compatible implementation of Span and Transaction
        creation.
        """
    trace_id: Incomplete
    span_id: Incomplete
    parent_span_id: Incomplete
    same_process_as_parent: Incomplete
    sampled: Incomplete
    op: Incomplete
    description: Incomplete
    status: Incomplete
    hub: Incomplete
    start_timestamp: Incomplete
    timestamp: Incomplete
    def __init__(self, trace_id: str | None = None, span_id: str | None = None, parent_span_id: str | None = None, same_process_as_parent: bool = True, sampled: bool | None = None, op: str | None = None, description: str | None = None, hub: sentry_sdk.Hub | None = None, status: str | None = None, transaction: str | None = None, containing_transaction: Transaction | None = None, start_timestamp: datetime | None = None) -> None: ...
    def init_span_recorder(self, maxlen: int) -> None: ...
    def __enter__(self) -> Span: ...
    def __exit__(self, ty: Any | None, value: Any | None, tb: Any | None) -> None: ...
    @property
    def containing_transaction(self) -> Transaction | None:
        '''The ``Transaction`` that this span belongs to.
        The ``Transaction`` is the root of the span tree,
        so one could also think of this ``Transaction`` as the "root span".'''
    def start_child(self, instrumenter: str = ..., **kwargs: Any) -> Span:
        """
        Start a sub-span from the current span or transaction.

        Takes the same arguments as the initializer of :py:class:`Span`. The
        trace id, sampling decision, transaction pointer, and span recorder are
        inherited from the current span/transaction.
        """
    def new_span(self, **kwargs: Any) -> Span:
        """DEPRECATED: use :py:meth:`sentry_sdk.tracing.Span.start_child` instead."""
    @classmethod
    def continue_from_environ(cls, environ: typing.Mapping[str, str], **kwargs: Any) -> Transaction:
        """
        Create a Transaction with the given params, then add in data pulled from
        the ``sentry-trace`` and ``baggage`` headers from the environ (if any)
        before returning the Transaction.

        This is different from :py:meth:`~sentry_sdk.tracing.Span.continue_from_headers`
        in that it assumes header names in the form ``HTTP_HEADER_NAME`` -
        such as you would get from a WSGI/ASGI environ -
        rather than the form ``header-name``.

        :param environ: The ASGI/WSGI environ to pull information from.
        """
    @classmethod
    def continue_from_headers(cls, headers: typing.Mapping[str, str], **kwargs: Any) -> Transaction:
        """
        Create a transaction with the given params (including any data pulled from
        the ``sentry-trace`` and ``baggage`` headers).

        :param headers: The dictionary with the HTTP headers to pull information from.
        """
    def iter_headers(self) -> Iterator[Tuple[str, str]]:
        """
        Creates a generator which returns the span's ``sentry-trace`` and ``baggage`` headers.
        If the span's containing transaction doesn't yet have a ``baggage`` value,
        this will cause one to be generated and stored.
        """
    @classmethod
    def from_traceparent(cls, traceparent: str | None, **kwargs: Any) -> Transaction | None:
        """
        DEPRECATED: Use :py:meth:`sentry_sdk.tracing.Span.continue_from_headers`.

        Create a ``Transaction`` with the given params, then add in data pulled from
        the given ``sentry-trace`` header value before returning the ``Transaction``.
        """
    def to_traceparent(self) -> str: ...
    def to_baggage(self) -> Baggage | None:
        """Returns the :py:class:`~sentry_sdk.tracing_utils.Baggage`
        associated with this ``Span``, if any. (Taken from the root of the span tree.)
        """
    def set_tag(self, key: str, value: Any) -> None: ...
    def set_data(self, key: str, value: Any) -> None: ...
    def set_status(self, value: str) -> None: ...
    def set_http_status(self, http_status: int) -> None: ...
    def is_success(self) -> bool: ...
    def finish(self, hub: sentry_sdk.Hub | None = None, end_timestamp: datetime | None = None) -> str | None:
        """Sets the end timestamp of the span.
        Additionally it also creates a breadcrumb from the span,
        if the span represents a database or HTTP request.

        :param hub: The hub to use for this transaction.
            If not provided, the current hub will be used.
        :param end_timestamp: Optional timestamp that should
            be used as timestamp instead of the current time.

        :return: Always ``None``. The type is ``Optional[str]`` to match
            the return value of :py:meth:`sentry_sdk.tracing.Transaction.finish`.
        """
    def to_json(self) -> Dict[str, Any]:
        """Returns a JSON-compatible representation of the span."""
    def get_trace_context(self) -> Any: ...

class Transaction(Span):
    """The Transaction is the root element that holds all the spans
    for Sentry performance instrumentation."""
    name: Incomplete
    source: Incomplete
    sample_rate: Incomplete
    parent_sampled: Incomplete
    def __init__(self, name: str = '', parent_sampled: bool | None = None, baggage: Baggage | None = None, source: str = ..., **kwargs: Any) -> None:
        '''Constructs a new Transaction.

        :param name: Identifier of the transaction.
            Will show up in the Sentry UI.
        :param parent_sampled: Whether the parent transaction was sampled.
            If True this transaction will be kept, if False it will be discarded.
        :param baggage: The W3C baggage header value.
            (see https://www.w3.org/TR/baggage/)
        :param source: A string describing the source of the transaction name.
            This will be used to determine the transaction\'s type.
            See https://develop.sentry.dev/sdk/event-payloads/transaction/#transaction-annotations
            for more information. Default "custom".
        '''
    def __enter__(self) -> Transaction: ...
    def __exit__(self, ty: Any | None, value: Any | None, tb: Any | None) -> None: ...
    @property
    def containing_transaction(self) -> Transaction:
        """The root element of the span tree.
        In the case of a transaction it is the transaction itself.
        """
    def finish(self, hub: sentry_sdk.Hub | None = None, end_timestamp: datetime | None = None) -> str | None:
        """Finishes the transaction and sends it to Sentry.
        All finished spans in the transaction will also be sent to Sentry.

        :param hub: The hub to use for this transaction.
            If not provided, the current hub will be used.
        :param end_timestamp: Optional timestamp that should
            be used as timestamp instead of the current time.

        :return: The event ID if the transaction was sent to Sentry,
            otherwise None.
        """
    def set_measurement(self, name: str, value: float, unit: MeasurementUnit = '') -> None: ...
    def set_context(self, key: str, value: Any) -> None:
        '''Sets a context. Transactions can have multiple contexts
        and they should follow the format described in the "Contexts Interface"
        documentation.

        :param key: The name of the context.
        :param value: The information about the context.
        '''
    def set_http_status(self, http_status: int) -> None:
        """Sets the status of the Transaction according to the given HTTP status.

        :param http_status: The HTTP status code."""
    def to_json(self) -> Dict[str, Any]:
        """Returns a JSON-compatible representation of the transaction."""
    def get_baggage(self) -> Baggage:
        """Returns the :py:class:`~sentry_sdk.tracing_utils.Baggage`
        associated with the Transaction.

        The first time a new baggage with Sentry items is made,
        it will be frozen."""

class NoOpSpan(Span):
    @property
    def containing_transaction(self) -> Transaction | None: ...
    def start_child(self, instrumenter: str = ..., **kwargs: Any) -> NoOpSpan: ...
    def new_span(self, **kwargs: Any) -> NoOpSpan: ...
    def to_traceparent(self) -> str: ...
    def to_baggage(self) -> Baggage | None: ...
    def get_baggage(self) -> Baggage | None: ...
    def iter_headers(self) -> Iterator[Tuple[str, str]]: ...
    def set_tag(self, key: str, value: Any) -> None: ...
    def set_data(self, key: str, value: Any) -> None: ...
    def set_status(self, value: str) -> None: ...
    def set_http_status(self, http_status: int) -> None: ...
    def is_success(self) -> bool: ...
    def to_json(self) -> Dict[str, Any]: ...
    def get_trace_context(self) -> Any: ...
    def finish(self, hub: sentry_sdk.Hub | None = None, end_timestamp: datetime | None = None) -> str | None: ...
    def set_measurement(self, name: str, value: float, unit: MeasurementUnit = '') -> None: ...
    def set_context(self, key: str, value: Any) -> None: ...
    def init_span_recorder(self, maxlen: int) -> None: ...

def trace(func: Any = None) -> Any:
    """
    Decorator to start a child span under the existing current transaction.
    If there is no current transaction, then nothing will be traced.

    .. code-block::
        :caption: Usage

        import sentry_sdk

        @sentry_sdk.trace
        def my_function():
            ...

        @sentry_sdk.trace
        async def my_async_function():
            ...
    """
