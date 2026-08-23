from dataclasses import dataclass
from enum import Enum
from typing import Dict

__all__ = ['EventSource', 'Event', 'NodeState', 'RdzvEvent']

EventMetadataValue = str | int | float | bool | None

class EventSource(str, Enum):
    """
    Known identifiers of the event producers.
    """
    AGENT: str
    WORKER: str

@dataclass
class Event:
    """
    The class represents the generic event that occurs during the torchelastic
    job execution. The event can be any kind of meaningful action.

    Args:
        name: event name.
        source: the event producer, e.g. agent or worker
        timestamp: timestamp in milliseconds when event occured.
        metadata: additional data that is associated with the event.
    """
    name: str
    source: EventSource
    timestamp: int = ...
    metadata: Dict[str, EventMetadataValue] = ...
    @staticmethod
    def deserialize(data: str | Event) -> Event: ...
    def serialize(self) -> str: ...
    def __init__(self, name, source, timestamp, metadata) -> None: ...

class NodeState(str, Enum):
    """
    The states that a node can be in rendezvous.
    """
    INIT: str
    RUNNING: str
    SUCCEEDED: str
    FAILED: str

@dataclass
class RdzvEvent:
    """
    Dataclass to represent any rendezvous event.

    Args:
        name: Event name. (E.g. Current action being performed)
        run_id: The run id of the rendezvous
        message: The message describing the event
        hostname: Hostname of the node
        pid: The process id of the node
        node_state: The state of the node (INIT, RUNNING, SUCCEEDED, FAILED)
        master_endpoint: The master endpoint for the rendezvous store, if known
        rank: The rank of the node, if known
        local_id: The local_id of the node, if defined in dynamic_rendezvous.py
        error_trace: Error stack trace, if this is an error event.
    """
    name: str
    run_id: str
    message: str
    hostname: str
    pid: int
    node_state: NodeState
    master_endpoint: str = ...
    rank: int | None = ...
    local_id: int | None = ...
    error_trace: str = ...
    @staticmethod
    def deserialize(data: str | RdzvEvent) -> RdzvEvent: ...
    def serialize(self) -> str: ...
    def __init__(self, name, run_id, message, hostname, pid, node_state, master_endpoint, rank, local_id, error_trace) -> None: ...
