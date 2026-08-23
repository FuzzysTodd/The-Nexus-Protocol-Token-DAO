from _typeshed import Incomplete
from sentry_sdk._compat import datetime_utcnow as datetime_utcnow, with_metaclass as with_metaclass
from sentry_sdk._types import Breadcrumb as Breadcrumb, BreadcrumbHint as BreadcrumbHint, Event as Event, ExcInfo as ExcInfo, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.client import Client as Client
from sentry_sdk.consts import ClientConstructor as ClientConstructor, INSTRUMENTER as INSTRUMENTER
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.profiler import Profile as Profile
from sentry_sdk.scope import Scope as Scope
from sentry_sdk.session import Session as Session
from sentry_sdk.tracing import BAGGAGE_HEADER_NAME as BAGGAGE_HEADER_NAME, NoOpSpan as NoOpSpan, SENTRY_TRACE_HEADER_NAME as SENTRY_TRACE_HEADER_NAME, Span as Span, Transaction as Transaction
from sentry_sdk.tracing_utils import has_tracing_enabled as has_tracing_enabled, normalize_incoming_data as normalize_incoming_data
from sentry_sdk.utils import ContextVar as ContextVar, event_from_exception as event_from_exception, exc_info_from_error as exc_info_from_error, logger as logger
from typing import Any, Callable, ContextManager, Dict, Generator, Tuple, Type, TypeVar, overload

T = TypeVar('T')

class _InitGuard:
    def __init__(self, client: Client) -> None: ...
    def __enter__(self) -> _InitGuard: ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any) -> None: ...

class init(ClientConstructor, _InitGuard): ...

class HubMeta(type):
    @property
    def current(cls) -> Hub:
        """Returns the current instance of the hub."""
    @property
    def main(cls) -> Hub:
        """Returns the main instance of the hub."""

class _ScopeManager:
    def __init__(self, hub: Hub) -> None: ...
    def __enter__(self) -> Scope: ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any) -> None: ...

class Hub(Incomplete):
    """The hub wraps the concurrency management of the SDK.  Each thread has
    its own hub but the hub might transfer with the flow of execution if
    context vars are available.

    If the hub is used with a with statement it's temporarily activated.
    """
    current: Hub
    main: Hub
    def __init__(self, client_or_hub: Hub | Client | None = None, scope: Any | None = None) -> None: ...
    def __enter__(self) -> Hub: ...
    def __exit__(self, exc_type: type | None, exc_value: BaseException | None, tb: Any | None) -> None: ...
    def run(self, callback: Callable[[], T]) -> T:
        """Runs a callback in the context of the hub.  Alternatively the
        with statement can be used on the hub directly.
        """
    def get_integration(self, name_or_class: str | Type[Integration]) -> Any:
        """Returns the integration for this hub by name or class.  If there
        is no client bound or the client does not have that integration
        then `None` is returned.

        If the return value is not `None` the hub is guaranteed to have a
        client attached.
        """
    @property
    def client(self) -> Client | None:
        """Returns the current client on the hub."""
    @property
    def scope(self) -> Scope:
        """Returns the current scope on the hub."""
    def last_event_id(self) -> str | None:
        """Returns the last event ID."""
    def bind_client(self, new: Client | None) -> None:
        """Binds a new client to the hub."""
    def capture_event(self, event: Event, hint: Hint | None = None, scope: Scope | None = None, **scope_args: Any) -> str | None:
        """
        Captures an event.

        Alias of :py:meth:`sentry_sdk.Client.capture_event`.

        :param scope_args: For supported `**scope_args` see
            :py:meth:`sentry_sdk.Scope.update_from_kwargs`.
        """
    def capture_message(self, message: str, level: str | None = None, scope: Scope | None = None, **scope_args: Any) -> str | None:
        """
        Captures a message.

        :param message: The string to send as the message.

        :param level: If no level is provided, the default level is `info`.

        :param scope: An optional :py:class:`sentry_sdk.Scope` to use.

        :param scope_args: For supported `**scope_args` see
            :py:meth:`sentry_sdk.Scope.update_from_kwargs`.

        :returns: An `event_id` if the SDK decided to send the event (see :py:meth:`sentry_sdk.Client.capture_event`).
        """
    def capture_exception(self, error: BaseException | ExcInfo | None = None, scope: Scope | None = None, **scope_args: Any) -> str | None:
        """Captures an exception.

        :param error: An exception to catch. If `None`, `sys.exc_info()` will be used.

        :param scope_args: For supported `**scope_args` see
            :py:meth:`sentry_sdk.Scope.update_from_kwargs`.

        :returns: An `event_id` if the SDK decided to send the event (see :py:meth:`sentry_sdk.Client.capture_event`).
        """
    def add_breadcrumb(self, crumb: Breadcrumb | None = None, hint: BreadcrumbHint | None = None, **kwargs: Any) -> None:
        """
        Adds a breadcrumb.

        :param crumb: Dictionary with the data as the sentry v7/v8 protocol expects.

        :param hint: An optional value that can be used by `before_breadcrumb`
            to customize the breadcrumbs that are emitted.
        """
    def start_span(self, span: Span | None = None, instrumenter: str = ..., **kwargs: Any) -> Span:
        """
        Start a span whose parent is the currently active span or transaction, if any.

        The return value is a :py:class:`sentry_sdk.tracing.Span` instance,
        typically used as a context manager to start and stop timing in a `with`
        block.

        Only spans contained in a transaction are sent to Sentry. Most
        integrations start a transaction at the appropriate time, for example
        for every incoming HTTP request. Use
        :py:meth:`sentry_sdk.start_transaction` to start a new transaction when
        one is not already in progress.

        For supported `**kwargs` see :py:class:`sentry_sdk.tracing.Span`.
        """
    def start_transaction(self, transaction: Transaction | None = None, instrumenter: str = ..., **kwargs: Any) -> Transaction | NoOpSpan:
        """
        Start and return a transaction.

        Start an existing transaction if given, otherwise create and start a new
        transaction with kwargs.

        This is the entry point to manual tracing instrumentation.

        A tree structure can be built by adding child spans to the transaction,
        and child spans to other spans. To start a new child span within the
        transaction or any span, call the respective `.start_child()` method.

        Every child span must be finished before the transaction is finished,
        otherwise the unfinished spans are discarded.

        When used as context managers, spans and transactions are automatically
        finished at the end of the `with` block. If not using context managers,
        call the `.finish()` method.

        When the transaction is finished, it will be sent to Sentry with all its
        finished child spans.

        For supported `**kwargs` see :py:class:`sentry_sdk.tracing.Transaction`.
        """
    def continue_trace(self, environ_or_headers: Dict[str, Any], op: str | None = None, name: str | None = None, source: str | None = None) -> Transaction:
        """
        Sets the propagation context from environment or headers and returns a transaction.
        """
    @overload
    def push_scope(self, callback: None | None = None) -> ContextManager[Scope]: ...
    @overload
    def push_scope(self, callback: Callable[[Scope], None]) -> None: ...
    def pop_scope_unsafe(self) -> Tuple[Client | None, Scope]:
        """
        Pops a scope layer from the stack.

        Try to use the context manager :py:meth:`push_scope` instead.
        """
    @overload
    def configure_scope(self, callback: None | None = None) -> ContextManager[Scope]: ...
    @overload
    def configure_scope(self, callback: Callable[[Scope], None]) -> None: ...
    def start_session(self, session_mode: str = 'application') -> None:
        """Starts a new session."""
    def end_session(self) -> None:
        """Ends the current session if there is one."""
    def stop_auto_session_tracking(self) -> None:
        """Stops automatic session tracking.

        This temporarily session tracking for the current scope when called.
        To resume session tracking call `resume_auto_session_tracking`.
        """
    def resume_auto_session_tracking(self) -> None:
        """Resumes automatic session tracking for the current scope if
        disabled earlier.  This requires that generally automatic session
        tracking is enabled.
        """
    def flush(self, timeout: float | None = None, callback: Callable[[int, float], None] | None = None) -> None:
        """
        Alias for :py:meth:`sentry_sdk.Client.flush`
        """
    def get_traceparent(self) -> str | None:
        """
        Returns the traceparent either from the active span or from the scope.
        """
    def get_baggage(self) -> str | None:
        """
        Returns Baggage either from the active span or from the scope.
        """
    def iter_trace_propagation_headers(self, span: Span | None = None) -> Generator[Tuple[str, str], None, None]:
        """
        Return HTTP headers which allow propagation of trace data. Data taken
        from the span representing the request, if available, or the current
        span on the scope if not.
        """
    def trace_propagation_meta(self, span: Span | None = None) -> str:
        """
        Return meta tags which should be injected into HTML templates
        to allow propagation of trace information.
        """

GLOBAL_HUB: Incomplete
