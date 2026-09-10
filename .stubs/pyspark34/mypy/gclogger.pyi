from _typeshed import Incomplete
from typing import Mapping

class GcLogger:
    """Context manager to log GC stats and overall time."""
    gc_start_time: Incomplete
    gc_time: float
    gc_calls: int
    gc_collected: int
    gc_uncollectable: int
    start_time: Incomplete
    def __enter__(self) -> GcLogger: ...
    def gc_callback(self, phase: str, info: Mapping[str, int]) -> None: ...
    def __exit__(self, *args: object) -> None: ...
    def get_stats(self) -> Mapping[str, float]: ...
