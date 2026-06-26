import logging
import typing as t
from .schema import SchemaType as SchemaType
from .schema_registry import SchemaRegistry as SchemaRegistry
from .traits import Handlers as Handlers
from .validators import JUPYTER_EVENTS_CORE_VALIDATOR as JUPYTER_EVENTS_CORE_VALIDATOR
from _typeshed import Incomplete
from datetime import datetime
from traitlets.config import LoggingConfigurable

EVENTS_METADATA_VERSION: int

class SchemaNotRegistered(Warning):
    """A warning to raise when an event is given to the logger
    but its schema has not be registered with the EventLogger
    """
class ModifierError(Exception):
    """An exception to raise when a modifier does not
    show the proper signature.
    """
class CoreMetadataError(Exception):
    """An exception raised when event core metadata is not valid."""
class ListenerError(Exception):
    """An exception to raise when a listener does not
    show the proper signature.
    """

class EventLogger(LoggingConfigurable):
    """
    An Event logger for emitting structured events.

    Event schemas must be registered with the
    EventLogger using the `register_schema` or
    `register_schema_file` methods. Every schema
    will be validated against Jupyter Event's metaschema.
    """
    handlers: Incomplete
    schemas: Incomplete
    async def gather_listeners(self) -> list[t.Any]:
        """Gather all of the active listeners."""
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize the logger."""
    def register_event_schema(self, schema: SchemaType) -> None:
        """Register this schema with the schema registry.

        Get this registered schema using the EventLogger.schema.get() method.
        """
    def register_handler(self, handler: logging.Handler) -> None:
        """Register a new logging handler to the Event Logger.

        All outgoing messages will be formatted as a JSON string.
        """
    def remove_handler(self, handler: logging.Handler) -> None:
        """Remove a logging handler from the logger and list of handlers."""
    def add_modifier(self, *, schema_id: str | None = None, modifier: t.Callable[[str, dict[str, t.Any]], dict[str, t.Any]]) -> None:
        """Add a modifier (callable) to a registered event.

        Parameters
        ----------
        modifier: Callable
            A callable function/method that executes when the named event occurs.
            This method enforces a string signature for modifiers:

                (schema_id: str, data: dict) -> dict:
        """
    def remove_modifier(self, *, schema_id: str | None = None, modifier: t.Callable[[str, dict[str, t.Any]], dict[str, t.Any]]) -> None:
        """Remove a modifier from an event or all events.

        Parameters
        ----------
        schema_id: str
            If given, remove this modifier only for a specific event type.
        modifier: Callable[[str, dict], dict]

            The modifier to remove.
        """
    def add_listener(self, *, modified: bool = True, schema_id: str | None = None, listener: t.Callable[[EventLogger, str, dict[str, t.Any]], t.Coroutine[t.Any, t.Any, None]]) -> None:
        """Add a listener (callable) to a registered event.

        Parameters
        ----------
        modified: bool
            If True (default), listens to the data after it has been mutated/modified
            by the list of modifiers.
        schema_id: str
            $id of the schema
        listener: Callable
            A callable function/method that executes when the named event occurs.
        """
    def remove_listener(self, *, schema_id: str | None = None, listener: t.Callable[[EventLogger, str, dict[str, t.Any]], t.Coroutine[t.Any, t.Any, None]]) -> None:
        """Remove a listener from an event or all events.

        Parameters
        ----------
        schema_id: str
            If given, remove this modifier only for a specific event type.

        listener: Callable[[EventLogger, str, dict], dict]
            The modifier to remove.
        """
    def emit(self, *, schema_id: str, data: dict[str, t.Any], timestamp_override: datetime | None = None) -> dict[str, t.Any] | None:
        """
        Record given event with schema has occurred.

        Parameters
        ----------
        schema_id: str
            $id of the schema
        data: dict
            The event to record
        timestamp_override: datetime, optional
            Optionally override the event timestamp. By default it is set to the current timestamp.

        Returns
        -------
        dict
            The recorded event data
        """
