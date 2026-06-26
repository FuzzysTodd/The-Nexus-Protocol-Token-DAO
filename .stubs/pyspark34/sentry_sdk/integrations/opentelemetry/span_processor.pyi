from opentelemetry.sdk.trace import SpanProcessor
from opentelemetry.trace import Span as OTelSpan, SpanContext as SpanContext
from sentry_sdk._types import Event as Event, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import INSTRUMENTER as INSTRUMENTER
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations.opentelemetry.consts import SENTRY_BAGGAGE_KEY as SENTRY_BAGGAGE_KEY, SENTRY_TRACE_KEY as SENTRY_TRACE_KEY
from sentry_sdk.scope import add_global_event_processor as add_global_event_processor
from sentry_sdk.tracing import Span as SentrySpan, Transaction as Transaction
from sentry_sdk.utils import Dsn as Dsn
from typing import Dict

OPEN_TELEMETRY_CONTEXT: str

def link_trace_context_to_error_event(event: Event, otel_span_map: Dict[str, Transaction | SentrySpan]) -> Event: ...

class SentrySpanProcessor(SpanProcessor):
    """
    Converts OTel spans into Sentry spans so they can be sent to the Sentry backend.
    """
    otel_span_map: Dict[str, Transaction | SentrySpan]
    def __new__(cls) -> SentrySpanProcessor: ...
    def __init__(self) -> None: ...
    def on_start(self, otel_span: OTelSpan, parent_context: SpanContext | None = None) -> None: ...
    def on_end(self, otel_span: OTelSpan) -> None: ...
