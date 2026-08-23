import sentry_sdk
from _typeshed import Incomplete
from sentry_sdk._types import BreadcrumbProcessor as BreadcrumbProcessor, Event as Event, EventProcessor as EventProcessor, MetricTags as MetricTags, ProfilerMode as ProfilerMode, TYPE_CHECKING as TYPE_CHECKING, TracesSampler as TracesSampler, TransactionProcessor as TransactionProcessor
from sentry_sdk.integrations import Integration as Integration
from typing import Any, Callable, Dict, List, Sequence, Type
from typing_extensions import TypedDict

DEFAULT_MAX_VALUE_LENGTH: int

class Experiments(TypedDict, total=False):
    attach_explain_plans: dict[str, Any]
    max_spans: int | None
    record_sql_params: bool | None
    profiles_sample_rate: float | None
    profiler_mode: ProfilerMode | None
    otel_powered_performance: bool | None
    transport_zlib_compression_level: int | None
    enable_metrics: bool | None
    before_emit_metric: Callable[[str, MetricTags], bool] | None

DEFAULT_QUEUE_SIZE: int
DEFAULT_MAX_BREADCRUMBS: int
MATCH_ALL: str
FALSE_VALUES: Incomplete

class INSTRUMENTER:
    SENTRY: str
    OTEL: str

class SPANDATA:
    """
    Additional information describing the type of the span.
    See: https://develop.sentry.dev/sdk/performance/span-data-conventions/
    """
    DB_NAME: str
    DB_USER: str
    DB_OPERATION: str
    DB_SYSTEM: str
    CACHE_HIT: str
    CACHE_ITEM_SIZE: str
    HTTP_QUERY: str
    HTTP_FRAGMENT: str
    HTTP_METHOD: str
    HTTP_STATUS_CODE: str
    SERVER_ADDRESS: str
    SERVER_PORT: str
    SERVER_SOCKET_ADDRESS: str
    SERVER_SOCKET_PORT: str

class OP:
    CACHE_GET_ITEM: str
    DB: str
    DB_REDIS: str
    EVENT_DJANGO: str
    FUNCTION: str
    FUNCTION_AWS: str
    FUNCTION_GCP: str
    GRAPHQL_EXECUTE: str
    GRAPHQL_MUTATION: str
    GRAPHQL_PARSE: str
    GRAPHQL_RESOLVE: str
    GRAPHQL_SUBSCRIPTION: str
    GRAPHQL_QUERY: str
    GRAPHQL_VALIDATE: str
    GRPC_CLIENT: str
    GRPC_SERVER: str
    HTTP_CLIENT: str
    HTTP_CLIENT_STREAM: str
    HTTP_SERVER: str
    MIDDLEWARE_DJANGO: str
    MIDDLEWARE_STARLETTE: str
    MIDDLEWARE_STARLETTE_RECEIVE: str
    MIDDLEWARE_STARLETTE_SEND: str
    MIDDLEWARE_STARLITE: str
    MIDDLEWARE_STARLITE_RECEIVE: str
    MIDDLEWARE_STARLITE_SEND: str
    QUEUE_SUBMIT_ARQ: str
    QUEUE_TASK_ARQ: str
    QUEUE_SUBMIT_CELERY: str
    QUEUE_TASK_CELERY: str
    QUEUE_TASK_RQ: str
    QUEUE_SUBMIT_HUEY: str
    QUEUE_TASK_HUEY: str
    SUBPROCESS: str
    SUBPROCESS_WAIT: str
    SUBPROCESS_COMMUNICATE: str
    TEMPLATE_RENDER: str
    VIEW_RENDER: str
    VIEW_RESPONSE_RENDER: str
    WEBSOCKET_SERVER: str
    SOCKET_CONNECTION: str
    SOCKET_DNS: str

class ClientConstructor:
    def __init__(self, dsn: str | None = None, max_breadcrumbs: int = ..., release: str | None = None, environment: str | None = None, server_name: str | None = None, shutdown_timeout: float = 2, integrations: Sequence[Integration] = [], in_app_include: List[str] = [], in_app_exclude: List[str] = [], default_integrations: bool = True, dist: str | None = None, transport: sentry_sdk.transport.Transport | Type[sentry_sdk.transport.Transport] | Callable[[Event], None] | None = None, transport_queue_size: int = ..., sample_rate: float = 1.0, send_default_pii: bool = False, http_proxy: str | None = None, https_proxy: str | None = None, ignore_errors: Sequence[type | str] = [], max_request_body_size: str = 'medium', before_send: EventProcessor | None = None, before_breadcrumb: BreadcrumbProcessor | None = None, debug: bool = False, attach_stacktrace: bool = False, ca_certs: str | None = None, propagate_traces: bool = True, traces_sample_rate: float | None = None, traces_sampler: TracesSampler | None = None, profiles_sample_rate: float | None = None, profiles_sampler: TracesSampler | None = None, profiler_mode: ProfilerMode | None = None, auto_enabling_integrations: bool = True, auto_session_tracking: bool = True, send_client_reports: bool = True, _experiments: Experiments = {}, proxy_headers: Dict[str, str] | None = None, instrumenter: str | None = ..., before_send_transaction: TransactionProcessor | None = None, project_root: str | None = None, enable_tracing: bool | None = None, include_local_variables: bool | None = True, include_source_context: bool | None = True, trace_propagation_targets: Sequence[str] | None = ..., functions_to_trace: Sequence[Dict[str, str]] = [], event_scrubber: sentry_sdk.scrubber.EventScrubber | None = None, max_value_length: int = ..., enable_backpressure_handling: bool = True) -> None: ...

DEFAULT_OPTIONS: Incomplete
VERSION: str
