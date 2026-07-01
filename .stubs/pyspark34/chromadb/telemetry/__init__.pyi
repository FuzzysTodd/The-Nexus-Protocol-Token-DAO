import abc
from _typeshed import Incomplete
from abc import abstractmethod
from chromadb.config import Component as Component
from enum import Enum
from typing import Any, Callable, ClassVar, Dict

TELEMETRY_WHITELISTED_SETTINGS: Incomplete

class ServerContext(Enum):
    NONE: str
    FASTAPI: str

class TelemetryEvent:
    max_batch_size: ClassVar[int]
    batch_size: int
    def __init__(self, batch_size: int = 1) -> None: ...
    @property
    def properties(self) -> Dict[str, Any]: ...
    @property
    def name(self) -> str: ...
    @property
    def batch_key(self) -> str: ...
    def batch(self, other: TelemetryEvent) -> TelemetryEvent: ...

class RepeatedTelemetry:
    interval: Incomplete
    function: Incomplete
    start: Incomplete
    event: Incomplete
    thread: Incomplete
    def __init__(self, interval: int, function: Callable[[], None]) -> None: ...
    def stop(self) -> None: ...

class Telemetry(Component, metaclass=abc.ABCMeta):
    USER_ID_PATH: Incomplete
    UNKNOWN_USER_ID: str
    SERVER_CONTEXT: ServerContext
    @abstractmethod
    def capture(self, event: TelemetryEvent) -> None: ...
    def schedule_event_function(self, event_function: Callable[..., TelemetryEvent], every_seconds: int) -> None: ...
    @property
    def context(self) -> Dict[str, Any]: ...
    @property
    def user_id(self) -> str: ...
