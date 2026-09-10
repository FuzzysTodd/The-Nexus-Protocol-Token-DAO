from pyspark.sql.types import Row, StructType
from typing import Tuple

__all__ = ['GroupState', 'GroupStateTimeout']

class GroupStateTimeout:
    """
    Represents the type of timeouts possible for the Dataset operations applyInPandasWithState.
    """
    NoTimeout: str
    ProcessingTimeTimeout: str
    EventTimeTimeout: str

class GroupState:
    """
    Wrapper class for interacting with per-group state data in `applyInPandasWithState`.
    """
    NO_TIMESTAMP: int
    def __init__(self, optionalValue: Row, batchProcessingTimeMs: int, eventTimeWatermarkMs: int, timeoutConf: str, hasTimedOut: bool, watermarkPresent: bool, defined: bool, updated: bool, removed: bool, timeoutTimestamp: int, keyAsUnsafe: bytes, valueSchema: StructType) -> None: ...
    @property
    def exists(self) -> bool:
        """
        Whether state exists or not.
        """
    @property
    def get(self) -> Tuple:
        """
        Get the state value if it exists, or throw ValueError.
        """
    @property
    def getOption(self) -> Tuple | None:
        """
        Get the state value if it exists, or return None.
        """
    @property
    def hasTimedOut(self) -> bool:
        """
        Whether the function has been called because the key has timed out.
        This can return true only when timeouts are enabled.
        """
    @property
    def oldTimeoutTimestamp(self) -> int: ...
    def update(self, newValue: Tuple) -> None:
        """
        Update the value of the state. The value of the state cannot be null.
        """
    def remove(self) -> None:
        """
        Remove this state.
        """
    def setTimeoutDuration(self, durationMs: int) -> None:
        """
        Set the timeout duration in ms for this key.
        Processing time timeout must be enabled.
        """
    def setTimeoutTimestamp(self, timestampMs: int) -> None:
        """
        Set the timeout timestamp for this key as milliseconds in epoch time.
        This timestamp cannot be older than the current watermark.
        Event time timeout must be enabled.
        """
    def getCurrentWatermarkMs(self) -> int:
        """
        Get the current event time watermark as milliseconds in epoch time.
        In a streaming query, this can be called only when watermark is set.
        """
    def getCurrentProcessingTimeMs(self) -> int:
        """
        Get the current processing time as milliseconds in epoch time.
        In a streaming query, this will return a constant value throughout the duration of a
        trigger, even if the trigger is re-executed.
        """
    def json(self) -> str:
        """
        Convert the internal values of instance into JSON. This is used to send out the update
        from Python worker to executor.
        """
