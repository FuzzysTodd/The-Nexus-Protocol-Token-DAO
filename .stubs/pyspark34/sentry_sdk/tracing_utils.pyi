import sentry_sdk
import typing
from _typeshed import Incomplete
from collections.abc import Mapping
from sentry_sdk._compat import PY2 as PY2, iteritems as iteritems
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.tracing import LOW_QUALITY_TRANSACTION_SOURCES as LOW_QUALITY_TRANSACTION_SOURCES
from sentry_sdk.utils import Dsn as Dsn, capture_internal_exceptions as capture_internal_exceptions, is_sentry_url as is_sentry_url, match_regex_list as match_regex_list, to_string as to_string
from typing import Any, Dict, Generator

SENTRY_TRACE_REGEX: Incomplete
base64_stripped: str

class EnvironHeaders(Mapping):
    environ: Incomplete
    prefix: Incomplete
    def __init__(self, environ: typing.Mapping[str, str], prefix: str = 'HTTP_') -> None: ...
    def __getitem__(self, key: str) -> Any | None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[str, None, None]: ...

def has_tracing_enabled(options: Dict[str, Any] | None) -> bool:
    """
    Returns True if either traces_sample_rate or traces_sampler is
    defined and enable_tracing is set and not false.
    """
def record_sql_queries(hub: sentry_sdk.Hub, cursor: Any, query: Any, params_list: Any, paramstyle: str | None, executemany: bool, record_cursor_repr: bool = False) -> Generator[sentry_sdk.tracing.Span, None, None]: ...
def maybe_create_breadcrumbs_from_span(hub: sentry_sdk.Hub, span: sentry_sdk.tracing.Span) -> None: ...
def extract_sentrytrace_data(header: str | None) -> Dict[str, str | bool | None] | None:
    """
    Given a `sentry-trace` header string, return a dictionary of data.
    """

class Baggage:
    """
    The W3C Baggage header information (see https://www.w3.org/TR/baggage/).
    """
    SENTRY_PREFIX: str
    SENTRY_PREFIX_REGEX: Incomplete
    sentry_items: Incomplete
    third_party_items: Incomplete
    mutable: Incomplete
    def __init__(self, sentry_items: Dict[str, str], third_party_items: str = '', mutable: bool = True) -> None: ...
    @classmethod
    def from_incoming_header(cls, header: str | None) -> Baggage:
        """
        freeze if incoming header already has sentry baggage
        """
    @classmethod
    def from_options(cls, scope: sentry_sdk.scope.Scope) -> Baggage | None: ...
    @classmethod
    def populate_from_transaction(cls, transaction: sentry_sdk.tracing.Transaction) -> Baggage:
        """
        Populate fresh baggage entry with sentry_items and make it immutable
        if this is the head SDK which originates traces.
        """
    def freeze(self) -> None: ...
    def dynamic_sampling_context(self) -> Dict[str, str]: ...
    def serialize(self, include_third_party: bool = False) -> str: ...

def should_propagate_trace(hub: sentry_sdk.Hub, url: str) -> bool:
    """
    Returns True if url matches trace_propagation_targets configured in the given hub. Otherwise, returns False.
    """
def normalize_incoming_data(incoming_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalizes incoming data so the keys are all lowercase with dashes instead of underscores and stripped from known prefixes.
    """
