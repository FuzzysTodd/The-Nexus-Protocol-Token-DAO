from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.opentelemetry.propagator import SentryPropagator as SentryPropagator
from sentry_sdk.integrations.opentelemetry.span_processor import SentrySpanProcessor as SentrySpanProcessor
from sentry_sdk.utils import logger as logger

CLASSES_TO_INSTRUMENT: Incomplete

class OpenTelemetryIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
