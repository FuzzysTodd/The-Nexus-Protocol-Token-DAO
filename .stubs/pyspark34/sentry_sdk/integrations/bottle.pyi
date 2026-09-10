from _typeshed import Incomplete
from bottle import FileUpload as FileUpload, FormsDict as FormsDict, LocalRequest as LocalRequest
from sentry_sdk._types import Event as Event, EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import RequestExtractor as RequestExtractor
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware as SentryWsgiMiddleware
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, parse_version as parse_version, transaction_from_function as transaction_from_function
from typing import Dict

TRANSACTION_STYLE_VALUES: Incomplete

class BottleIntegration(Integration):
    identifier: str
    transaction_style: str
    def __init__(self, transaction_style: str = 'endpoint') -> None: ...
    @staticmethod
    def setup_once() -> None: ...

class BottleRequestExtractor(RequestExtractor):
    def env(self) -> Dict[str, str]: ...
    def cookies(self) -> Dict[str, str]: ...
    def raw_data(self) -> bytes: ...
    def form(self) -> FormsDict: ...
    def files(self) -> Dict[str, str] | None: ...
    def size_of_file(self, file: FileUpload) -> int: ...
