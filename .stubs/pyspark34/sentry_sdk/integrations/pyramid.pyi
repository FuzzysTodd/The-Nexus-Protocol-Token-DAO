from _typeshed import Incomplete
from pyramid.request import Request
from pyramid.response import Response as Response
from sentry_sdk._compat import iteritems as iteritems, reraise as reraise
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import RequestExtractor as RequestExtractor
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware as SentryWsgiMiddleware
from sentry_sdk.scope import Scope as Scope
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE
from sentry_sdk.utils import ExcInfo as ExcInfo, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception
from typing import Any, Dict
from webob.compat import cgi_FieldStorage as cgi_FieldStorage
from webob.cookies import RequestCookies as RequestCookies

def authenticated_userid(request: Request) -> Any | None: ...

TRANSACTION_STYLE_VALUES: Incomplete

class PyramidIntegration(Integration):
    identifier: str
    transaction_style: str
    def __init__(self, transaction_style: str = 'route_name') -> None: ...
    @staticmethod
    def setup_once() -> None: ...

class PyramidRequestExtractor(RequestExtractor):
    def url(self) -> str: ...
    def env(self) -> Dict[str, str]: ...
    def cookies(self) -> RequestCookies: ...
    def raw_data(self) -> str: ...
    def form(self) -> Dict[str, str]: ...
    def files(self) -> Dict[str, cgi_FieldStorage]: ...
    def size_of_file(self, postdata: cgi_FieldStorage) -> int: ...
