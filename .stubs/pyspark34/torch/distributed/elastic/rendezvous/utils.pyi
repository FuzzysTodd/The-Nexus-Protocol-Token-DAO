from datetime import timedelta
from threading import Event
from typing import Any, Callable, Dict, Tuple

__all__ = ['parse_rendezvous_endpoint']

def parse_rendezvous_endpoint(endpoint: str | None, default_port: int) -> Tuple[str, int]:
    """Extracts the hostname and the port number from a rendezvous endpoint.

    Args:
        endpoint:
            A string in format <hostname>[:<port>].
        default_port:
            The port number to use if the endpoint does not include one.

    Returns:
        A tuple of hostname and port number.
    """

class _PeriodicTimer:
    """Represents a timer that periodically runs a specified function.

    Args:
        interval:
            The interval, in seconds, between each run.
        function:
            The function to run.
    """
    class _Context:
        interval: float
        function: Callable[..., None]
        args: Tuple[Any, ...]
        kwargs: Dict[str, Any]
        stop_event: Event
    def __init__(self, interval: timedelta, function: Callable[..., None], *args: Any, **kwargs: Any) -> None: ...
    @property
    def name(self) -> str | None:
        """Gets the name of the timer."""
    def set_name(self, name: str) -> None:
        """Sets the name of the timer.

        The specified name will be assigned to the background thread and serves
        for debugging and troubleshooting purposes.
        """
    def start(self) -> None:
        """Start the timer."""
    def cancel(self) -> None:
        """Stop the timer at the next opportunity."""
