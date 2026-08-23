import io
import logging
from jupyter_events import EventLogger as EventLogger
from typing import Any, Callable

def jp_event_sink() -> io.StringIO:
    """A stream for capture events."""
def jp_event_handler(jp_event_sink: io.StringIO) -> logging.Handler:
    """A logging handler that captures any events emitted by the event handler"""
def jp_read_emitted_events(jp_event_handler: logging.Handler, jp_event_sink: io.StringIO) -> Callable[..., list[str] | None]:
    """Reads list of events since last time it was called."""
def jp_event_schemas() -> list[Any]:
    """A list of schema references.

    Each item should be one of the following:
    - string of serialized JSON/YAML content representing a schema
    - a pathlib.Path object pointing to a schema file on disk
    - a dictionary with the schema data.
    """
def jp_event_logger(jp_event_handler: logging.Handler, jp_event_schemas: list[Any]) -> EventLogger:
    """A pre-configured event logger for tests."""
