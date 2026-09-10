from _typeshed import Incomplete
from chromadb.config import System as System
from chromadb.telemetry import Telemetry as Telemetry, TelemetryEvent as TelemetryEvent

logger: Incomplete

class Posthog(Telemetry):
    batched_events: Incomplete
    seen_event_types: Incomplete
    def __init__(self, system: System) -> None: ...
    def capture(self, event: TelemetryEvent) -> None: ...
