from _typeshed import Incomplete
from types import TracebackType
from typing import Any, Dict, Tuple, Type

__all__ = ['Sentry']

class Sentry:
    dsn: Incomplete
    hub: Incomplete
    def __init__(self) -> None: ...
    @property
    def environment(self) -> str:
        """Return the environment we're running in."""
    def setup(self) -> None:
        """Setup Sentry SDK.

        We use lower-level APIs (i.e., not sentry_sdk.init) here
        to avoid the possibility of interfering with the user's
        own Sentry SDK setup.
        """
    def message(self, message: str, repeat: bool = True) -> None:
        """Send a message to Sentry."""
    def exception(self, exc: str | BaseException | Tuple[Type[BaseException] | None, BaseException | None, TracebackType | None] | None, handled: bool = False, status: SessionStatus | None = None) -> None:
        """Log an exception to Sentry."""
    def reraise(self, exc: Any) -> None:
        """Re-raise an exception after logging it to Sentry.

        Use this for top-level exceptions when you want the user to see the traceback.

        Must be called from within an exception handler.
        """
    def start_session(self) -> None:
        """Start a new session."""
    def end_session(self) -> None:
        """End the current session."""
    def mark_session(self, status: SessionStatus | None = None) -> None:
        """Mark the current session with a status."""
    def configure_scope(self, tags: Dict[str, Any] | None = None, process_context: str | None = None) -> None:
        """Configure the Sentry scope for the current thread.

        This function should be called at the beginning of every thread that
        will send events to Sentry. It sets the tags that will be applied to
        all events sent from this thread. It also tries to start a session
        if one doesn't already exist for this thread.
        """
