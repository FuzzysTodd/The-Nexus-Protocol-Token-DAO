from typing import Callable, Protocol

class EventListenerWithMetadata(Protocol):
    def __call__(self, event: str, **kwargs: str | int) -> None: ...

def record_event(event: str, **kwargs: str | int) -> None:
    """Record an event."""
def record_event_duration_secs(event: str, duration: float) -> None:
    """Record an event duration in seconds (float)."""
def register_event_listener(callback: Callable[[str], None]) -> None:
    """Register a callback to be invoked during record_event()."""
def register_event_listener_with_kwargs(callback: EventListenerWithMetadata) -> None:
    """Register a callback to be invoked during record_event()."""
def register_event_duration_secs_listener(callback: Callable[[str, float], None]) -> None:
    """Register a callback to be invoked during record_event_duration_secs()."""
def get_event_duration_listeners() -> list[Callable[[str, float], None]]:
    """Get event duration listeners."""
def get_event_listeners() -> list[Callable[[str], None]]:
    """Get event listeners."""
