from opentelemetry.context import Context as Context
from opentelemetry.propagators.textmap import CarrierT as CarrierT, Getter as Getter, Setter as Setter, TextMapPropagator
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.integrations.opentelemetry.consts import SENTRY_BAGGAGE_KEY as SENTRY_BAGGAGE_KEY, SENTRY_TRACE_KEY as SENTRY_TRACE_KEY
from sentry_sdk.integrations.opentelemetry.span_processor import SentrySpanProcessor as SentrySpanProcessor
from sentry_sdk.tracing import BAGGAGE_HEADER_NAME as BAGGAGE_HEADER_NAME, SENTRY_TRACE_HEADER_NAME as SENTRY_TRACE_HEADER_NAME
from sentry_sdk.tracing_utils import Baggage as Baggage, extract_sentrytrace_data as extract_sentrytrace_data
from typing import Set

class SentryPropagator(TextMapPropagator):
    """
    Propagates tracing headers for Sentry's tracing system in a way OTel understands.
    """
    def extract(self, carrier: CarrierT, context: Context | None = None, getter: Getter = ...) -> Context: ...
    def inject(self, carrier: CarrierT, context: Context | None = None, setter: Setter = ...) -> None: ...
    @property
    def fields(self) -> Set[str]: ...
