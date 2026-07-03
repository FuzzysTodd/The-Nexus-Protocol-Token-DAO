from _typeshed import Incomplete
from sentry_sdk._compat import datetime_utcnow as datetime_utcnow, iteritems as iteritems, string_types as string_types, text_type as text_type
from sentry_sdk._types import Event as Event, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import ClientConstructor as ClientConstructor, DEFAULT_MAX_VALUE_LENGTH as DEFAULT_MAX_VALUE_LENGTH, DEFAULT_OPTIONS as DEFAULT_OPTIONS, INSTRUMENTER as INSTRUMENTER, VERSION as VERSION
from sentry_sdk.envelope import Envelope as Envelope
from sentry_sdk.integrations import setup_integrations as setup_integrations
from sentry_sdk.monitor import Monitor as Monitor
from sentry_sdk.profiler import has_profiling_enabled as has_profiling_enabled, setup_profiler as setup_profiler
from sentry_sdk.scope import Scope as Scope
from sentry_sdk.scrubber import EventScrubber as EventScrubber
from sentry_sdk.serializer import serialize as serialize
from sentry_sdk.session import Session as Session
from sentry_sdk.sessions import SessionFlusher as SessionFlusher
from sentry_sdk.tracing import has_tracing_enabled as has_tracing_enabled, trace as trace
from sentry_sdk.transport import make_transport as make_transport
from sentry_sdk.utils import ContextVar as ContextVar, capture_internal_exceptions as capture_internal_exceptions, current_stacktrace as current_stacktrace, disable_capture_event as disable_capture_event, format_timestamp as format_timestamp, get_default_release as get_default_release, get_sdk_name as get_sdk_name, get_type_name as get_type_name, handle_in_app as handle_in_app, logger as logger
from typing import Any, Callable, Dict

SDK_INFO: Incomplete
module_not_found_error = ModuleNotFoundError
module_not_found_error = ImportError

class _Client:
    """The client is internally responsible for capturing the events and
    forwarding them to sentry through the configured transport.  It takes
    the client options as keyword arguments and optionally the DSN as first
    argument.
    """
    options: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def dsn(self) -> str | None:
        """Returns the configured DSN as string."""
    def capture_event(self, event: Event, hint: Hint | None = None, scope: Scope | None = None) -> str | None:
        """Captures an event.

        :param event: A ready-made event that can be directly sent to Sentry.

        :param hint: Contains metadata about the event that can be read from `before_send`, such as the original exception object or a HTTP request object.

        :param scope: An optional scope to use for determining whether this event
            should be captured.

        :returns: An event ID. May be `None` if there is no DSN set or of if the SDK decided to discard the event for other reasons. In such situations setting `debug=True` on `init()` may help.
        """
    def capture_session(self, session: Session) -> None: ...
    transport: Incomplete
    def close(self, timeout: float | None = None, callback: Callable[[int, float], None] | None = None) -> None:
        """
        Close the client and shut down the transport. Arguments have the same
        semantics as :py:meth:`Client.flush`.
        """
    def flush(self, timeout: float | None = None, callback: Callable[[int, float], None] | None = None) -> None:
        """
        Wait for the current events to be sent.

        :param timeout: Wait for at most `timeout` seconds. If no `timeout` is provided, the `shutdown_timeout` option value is used.

        :param callback: Is invoked with the number of pending events and the configured timeout.
        """
    def __enter__(self) -> _Client: ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any) -> None: ...

class get_options(ClientConstructor, Dict[str, Any]): ...
class Client(ClientConstructor, _Client): ...
