import sentry_sdk
from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.envelope import Envelope as Envelope
from sentry_sdk.session import Session as Session
from sentry_sdk.utils import format_timestamp as format_timestamp
from typing import Any, Callable, Generator

def is_auto_session_tracking_enabled(hub: sentry_sdk.Hub | None = None) -> Any | bool | None:
    """Utility function to find out if session tracking is enabled."""
def auto_session_tracking(hub: sentry_sdk.Hub | None = None, session_mode: str = 'application') -> Generator[None, None, None]:
    """Starts and stops a session automatically around a block."""

TERMINAL_SESSION_STATES: Incomplete
MAX_ENVELOPE_ITEMS: int

def make_aggregate_envelope(aggregate_states: Any, attrs: Any) -> Any: ...

class SessionFlusher:
    capture_func: Incomplete
    flush_interval: Incomplete
    pending_sessions: Incomplete
    pending_aggregates: Incomplete
    def __init__(self, capture_func: Callable[[Envelope], None], flush_interval: int = 60) -> None: ...
    def flush(self) -> None: ...
    def add_aggregate_session(self, session: Session) -> None: ...
    def add_session(self, session: Session) -> None: ...
    def kill(self) -> None: ...
    def __del__(self) -> None: ...
