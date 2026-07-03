from _typeshed import Incomplete
from sentry_sdk._compat import datetime_utcnow as datetime_utcnow
from sentry_sdk._types import EndpointType as EndpointType, Event as Event, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.envelope import Envelope as Envelope, Item as Item, PayloadRef as PayloadRef
from sentry_sdk.utils import Dsn as Dsn, capture_internal_exceptions as capture_internal_exceptions, json_dumps as json_dumps, logger as logger
from sentry_sdk.worker import BackgroundWorker as BackgroundWorker
from typing import Any, Callable, Dict
from urllib3.poolmanager import PoolManager as PoolManager, ProxyManager as ProxyManager

DataCategory = str | None

class Transport:
    """Baseclass for all transports.

    A transport is used to send an event to sentry.
    """
    parsed_dsn: Dsn | None
    options: Incomplete
    def __init__(self, options: Dict[str, Any] | None = None) -> None: ...
    def capture_event(self, event: Event) -> None:
        """
        This gets invoked with the event dictionary when an event should
        be sent to sentry.
        """
    def capture_envelope(self, envelope: Envelope) -> None:
        '''
        Send an envelope to Sentry.

        Envelopes are a data container format that can hold any type of data
        submitted to Sentry. We use it for transactions and sessions, but
        regular "error" events should go through `capture_event` for backwards
        compat.
        '''
    def flush(self, timeout: float, callback: Any | None = None) -> None:
        """Wait `timeout` seconds for the current events to be sent out."""
    def kill(self) -> None:
        """Forcefully kills the transport."""
    def record_lost_event(self, reason: str, data_category: str | None = None, item: Item | None = None) -> None:
        """This increments a counter for event loss by reason and
        data category.
        """
    def is_healthy(self) -> bool: ...
    def __del__(self) -> None: ...

class HttpTransport(Transport):
    """The default HTTP transport."""
    options: Incomplete
    hub_cls: Incomplete
    def __init__(self, options: Dict[str, Any]) -> None: ...
    def record_lost_event(self, reason: str, data_category: str | None = None, item: Item | None = None) -> None: ...
    def on_dropped_event(self, reason: str) -> None: ...
    def is_healthy(self) -> bool: ...
    def capture_event(self, event: Event) -> None: ...
    def capture_envelope(self, envelope: Envelope) -> None: ...
    def flush(self, timeout: float, callback: Any | None = None) -> None: ...
    def kill(self) -> None: ...

class _FunctionTransport(Transport):
    def __init__(self, func: Callable[[Event], None]) -> None: ...
    def capture_event(self, event: Event) -> None: ...

def make_transport(options: Dict[str, Any]) -> Transport | None: ...
