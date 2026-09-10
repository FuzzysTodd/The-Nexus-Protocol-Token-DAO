from _typeshed import Incomplete
from django.core.handlers.wsgi import WSGIRequest as WSGIRequest
from django.http.request import QueryDict as QueryDict
from django.http.response import HttpResponse as HttpResponse
from django.utils.datastructures import MultiValueDict as MultiValueDict
from sentry_sdk._compat import string_types as string_types, text_type as text_type
from sentry_sdk._types import Event as Event, EventProcessor as EventProcessor, Hint as Hint, NotImplementedType as NotImplementedType, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP, SPANDATA as SPANDATA
from sentry_sdk.db.explain_plan.django import attach_explain_plan_to_span as attach_explain_plan_to_span
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import RequestExtractor as RequestExtractor
from sentry_sdk.integrations.django.caching import patch_caching as patch_caching
from sentry_sdk.integrations.django.middleware import patch_django_middlewares as patch_django_middlewares
from sentry_sdk.integrations.django.signals_handlers import patch_signals as patch_signals
from sentry_sdk.integrations.django.templates import get_template_frame_from_exception as get_template_frame_from_exception, patch_templates as patch_templates
from sentry_sdk.integrations.django.transactions import LEGACY_RESOLVER as LEGACY_RESOLVER
from sentry_sdk.integrations.django.views import patch_views as patch_views
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware as SentryWsgiMiddleware
from sentry_sdk.scope import Scope as Scope, add_global_event_processor as add_global_event_processor
from sentry_sdk.serializer import add_global_repr_processor as add_global_repr_processor
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE, Span as Span, TRANSACTION_SOURCE_URL as TRANSACTION_SOURCE_URL
from sentry_sdk.tracing_utils import record_sql_queries as record_sql_queries
from sentry_sdk.utils import AnnotatedValue as AnnotatedValue, CONTEXTVARS_ERROR_MESSAGE as CONTEXTVARS_ERROR_MESSAGE, HAS_REAL_CONTEXTVARS as HAS_REAL_CONTEXTVARS, SENSITIVE_DATA_SUBSTITUTE as SENSITIVE_DATA_SUBSTITUTE, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, logger as logger, transaction_from_function as transaction_from_function, walk_exception_chain as walk_exception_chain
from typing import Any, Dict

def is_authenticated(request_user: Any) -> bool: ...

TRANSACTION_STYLE_VALUES: Incomplete

class DjangoIntegration(Integration):
    identifier: str
    transaction_style: str
    middleware_spans: Incomplete
    signals_spans: Incomplete
    cache_spans: Incomplete
    def __init__(self, transaction_style: str = 'url', middleware_spans: bool = True, signals_spans: bool = True, cache_spans: bool = False) -> None: ...
    @staticmethod
    def setup_once() -> None: ...

class DjangoRequestExtractor(RequestExtractor):
    def env(self) -> Dict[str, str]: ...
    def cookies(self) -> Dict[str, str | AnnotatedValue]: ...
    def raw_data(self) -> bytes: ...
    def form(self) -> QueryDict: ...
    def files(self) -> MultiValueDict: ...
    def size_of_file(self, file: Any) -> int: ...
    def parsed_body(self) -> Dict[str, Any] | None: ...

def install_sql_hook() -> None:
    """If installed this causes Django's queries to be captured."""
