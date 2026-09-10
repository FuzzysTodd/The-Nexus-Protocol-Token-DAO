from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import Breadcrumb as Breadcrumb, ErrorProcessor as ErrorProcessor, Event as Event, EventProcessor as EventProcessor, ExcInfo as ExcInfo, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING, Type as Type
from sentry_sdk.attachments import Attachment as Attachment
from sentry_sdk.consts import FALSE_VALUES as FALSE_VALUES
from sentry_sdk.profiler import Profile as Profile
from sentry_sdk.session import Session as Session
from sentry_sdk.tracing import BAGGAGE_HEADER_NAME as BAGGAGE_HEADER_NAME, SENTRY_TRACE_HEADER_NAME as SENTRY_TRACE_HEADER_NAME, Span as Span, Transaction as Transaction
from sentry_sdk.tracing_utils import Baggage as Baggage, extract_sentrytrace_data as extract_sentrytrace_data, has_tracing_enabled as has_tracing_enabled, normalize_incoming_data as normalize_incoming_data
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, logger as logger
from typing import Any, Callable, Dict, Iterator, List, Tuple, TypeVar

F = TypeVar('F', bound=Callable[..., Any])
T = TypeVar('T')
global_event_processors: List[EventProcessor]

def add_global_event_processor(processor: EventProcessor) -> None: ...

class Scope:
    """The scope holds extra information that should be sent with all
    events that belong to it.
    """
    def __init__(self) -> None: ...
    def set_new_propagation_context(self) -> None:
        """
        Creates a new propagation context and sets it as `_propagation_context`. Overwriting existing one.
        """
    def generate_propagation_context(self, incoming_data: Dict[str, str] | None = None) -> None:
        """
        Makes sure `_propagation_context` is set.
        If there is `incoming_data` overwrite existing `_propagation_context`.
        if there is no `incoming_data` create new `_propagation_context`, but do NOT overwrite if already existing.
        """
    def get_dynamic_sampling_context(self) -> Dict[str, str] | None:
        """
        Returns the Dynamic Sampling Context from the Propagation Context.
        If not existing, creates a new one.
        """
    def get_traceparent(self) -> str | None:
        '''
        Returns the Sentry "sentry-trace" header (aka the traceparent) from the Propagation Context.
        '''
    def get_baggage(self) -> Baggage | None: ...
    def get_trace_context(self) -> Any:
        '''
        Returns the Sentry "trace" context from the Propagation Context.
        '''
    def iter_headers(self) -> Iterator[Tuple[str, str]]:
        """
        Creates a generator which returns the `sentry-trace` and `baggage` headers from the Propagation Context.
        """
    def clear(self) -> None:
        """Clears the entire scope."""
    def level(self, value: str | None) -> None:
        """When set this overrides the level. Deprecated in favor of set_level."""
    def set_level(self, value: str | None) -> None:
        """Sets the level for the scope."""
    def fingerprint(self, value: List[str] | None) -> None:
        """When set this overrides the default fingerprint."""
    @property
    def transaction(self) -> Any:
        """Return the transaction (root span) in the scope, if any."""
    @transaction.setter
    def transaction(self, value: Any) -> None:
        """When set this forces a specific transaction name to be set.

        Deprecated: use set_transaction_name instead."""
    def set_transaction_name(self, name: str, source: str | None = None) -> None:
        """Set the transaction name and optionally the transaction source."""
    def user(self, value: Dict[str, Any] | None) -> None:
        """When set a specific user is bound to the scope. Deprecated in favor of set_user."""
    def set_user(self, value: Dict[str, Any] | None) -> None:
        """Sets a user for the scope."""
    @property
    def span(self) -> Span | None:
        """Get/set current tracing span or transaction."""
    @span.setter
    def span(self, span: Span | None) -> None: ...
    @property
    def profile(self) -> Profile | None: ...
    @profile.setter
    def profile(self, profile: Profile | None) -> None: ...
    def set_tag(self, key: str, value: Any) -> None:
        """Sets a tag for a key to a specific value."""
    def remove_tag(self, key: str) -> None:
        """Removes a specific tag."""
    def set_context(self, key: str, value: Dict[str, Any]) -> None:
        """Binds a context at a certain key to a specific value."""
    def remove_context(self, key: str) -> None:
        """Removes a context."""
    def set_extra(self, key: str, value: Any) -> None:
        """Sets an extra key to a specific value."""
    def remove_extra(self, key: str) -> None:
        """Removes a specific extra key."""
    def clear_breadcrumbs(self) -> None:
        """Clears breadcrumb buffer."""
    def add_attachment(self, bytes: bytes | None = None, filename: str | None = None, path: str | None = None, content_type: str | None = None, add_to_transactions: bool = False) -> None:
        """Adds an attachment to future events sent."""
    def add_event_processor(self, func: EventProcessor) -> None:
        """Register a scope local event processor on the scope.

        :param func: This function behaves like `before_send.`
        """
    def add_error_processor(self, func: ErrorProcessor, cls: Type[BaseException] | None = None) -> None:
        """Register a scope local error processor on the scope.

        :param func: A callback that works similar to an event processor but is invoked with the original exception info triple as second argument.

        :param cls: Optionally, only process exceptions of this type.
        """
    def apply_to_event(self, event: Event, hint: Hint, options: Dict[str, Any] | None = None) -> Event | None:
        """Applies the information contained on the scope to the given event."""
    def update_from_scope(self, scope: Scope) -> None:
        """Update the scope with another scope's data."""
    def update_from_kwargs(self, user: Any | None = None, level: str | None = None, extras: Dict[str, Any] | None = None, contexts: Dict[str, Any] | None = None, tags: Dict[str, str] | None = None, fingerprint: List[str] | None = None) -> None:
        """Update the scope's attributes."""
    def __copy__(self) -> Scope: ...
