from _typeshed import Incomplete
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import RequestExtractor as RequestExtractor
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware as SentryWsgiMiddleware
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, parse_version as parse_version
from typing import Any, Dict

falcon_helpers: Incomplete
falcon_app_class: Incomplete
FALCON3: bool

class FalconRequestExtractor(RequestExtractor):
    def env(self) -> Dict[str, Any]: ...
    def cookies(self) -> Dict[str, Any]: ...
    def form(self) -> None: ...
    def files(self) -> None: ...
    def raw_data(self) -> str | None: ...
    def json(self) -> Dict[str, Any] | None: ...
    def json(self) -> Dict[str, Any] | None: ...

class SentryFalconMiddleware:
    """Captures exceptions in Falcon requests and send to Sentry"""
    def process_request(self, req: Any, resp: Any, *args: Any, **kwargs: Any) -> None: ...

TRANSACTION_STYLE_VALUES: Incomplete

class FalconIntegration(Integration):
    identifier: str
    transaction_style: str
    def __init__(self, transaction_style: str = 'uri_template') -> None: ...
    @staticmethod
    def setup_once() -> None: ...
