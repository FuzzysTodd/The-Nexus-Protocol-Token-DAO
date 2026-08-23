from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Generator
from typing import NamedTuple

__all__ = ['EventList', 'FormattedTimesMixin', 'Interval', 'Kernel', 'FunctionEvent', 'FunctionEventAvg', 'StringTable', 'MemRecordsAcc']

class EventList(list):
    """A list of Events (for pretty printing)"""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def self_cpu_time_total(self): ...
    def table(self, sort_by: Incomplete | None = None, row_limit: int = 100, max_src_column_width: int = 75, max_name_column_width: int = 55, max_shapes_column_width: int = 80, header: Incomplete | None = None, top_level_events_only: bool = False):
        """Prints an EventList as a nicely formatted table.

        Args:
            sort_by (str, optional): Attribute used to sort entries. By default
                they are printed in the same order as they were registered.
                Valid keys include: ``cpu_time``, ``cuda_time``, ``cpu_time_total``,
                ``cuda_time_total``, ``cpu_memory_usage``, ``cuda_memory_usage``,
                ``self_cpu_memory_usage``, ``self_cuda_memory_usage``, ``count``.
            top_level_events_only(bool, optional): Boolean flag to determine the
                selection of events to display. If true, the profiler will only
                display events at top level like top-level invocation of python
                `lstm`, python `add` or other functions, nested events like low-level
                cpu/cuda ops events are omitted for profiler result readability.

        Returns:
            A string containing the table.
        """
    def export_chrome_trace(self, path) -> None:
        """Exports an EventList as a Chrome tracing tools file.

        The checkpoint can be later loaded and inspected under ``chrome://tracing`` URL.

        Args:
            path (str): Path where the trace will be written.
        """
    def supported_export_stacks_metrics(self): ...
    def export_stacks(self, path: str, metric: str): ...
    def key_averages(self, group_by_input_shapes: bool = False, group_by_stack_n: int = 0):
        """Averages all function events over their keys.

        Args:
            group_by_input_shapes: group entries by
                (event name, input shapes) rather than just event name.
                This is useful to see which input shapes contribute to the runtime
                the most and may help with size-specific optimizations or
                choosing the best candidates for quantization (aka fitting a roof line)

            group_by_stack_n: group by top n stack trace entries

        Returns:
            An EventList containing FunctionEventAvg objects.
        """
    def total_average(self):
        """Averages all events.

        Returns:
            A FunctionEventAvg object.
        """

class FormattedTimesMixin:
    """Helpers for FunctionEvent and FunctionEventAvg.

    The subclass should define `*_time_total` and `count` attributes.
    """
    cpu_time_str: Incomplete
    cuda_time_str: Incomplete
    cpu_time_total_str: Incomplete
    cuda_time_total_str: Incomplete
    self_cpu_time_total_str: Incomplete
    self_cuda_time_total_str: Incomplete
    @property
    def cpu_time(self): ...
    @property
    def cuda_time(self): ...

class Interval:
    start: Incomplete
    end: Incomplete
    def __init__(self, start, end) -> None: ...
    def elapsed_us(self): ...

class Kernel(NamedTuple):
    name: Incomplete
    device: Incomplete
    duration: Incomplete

class FunctionEvent(FormattedTimesMixin):
    """Profiling information about a single function."""
    id: Incomplete
    node_id: Incomplete
    name: Incomplete
    trace_name: Incomplete
    time_range: Incomplete
    thread: Incomplete
    fwd_thread: Incomplete
    kernels: Incomplete
    count: int
    cpu_children: Incomplete
    cpu_parent: Incomplete
    input_shapes: Incomplete
    stack: Incomplete
    scope: Incomplete
    cpu_memory_usage: Incomplete
    cuda_memory_usage: Incomplete
    is_async: Incomplete
    is_remote: Incomplete
    sequence_nr: Incomplete
    device_type: Incomplete
    device_index: Incomplete
    is_legacy: Incomplete
    flops: Incomplete
    def __init__(self, id, name, thread, start_us, end_us, fwd_thread: Incomplete | None = None, input_shapes: Incomplete | None = None, stack: Incomplete | None = None, scope: int = 0, cpu_memory_usage: int = 0, cuda_memory_usage: int = 0, is_async: bool = False, is_remote: bool = False, sequence_nr: int = -1, node_id: int = -1, device_type=..., device_index: int = 0, is_legacy: bool = False, flops: Incomplete | None = None, trace_name: Incomplete | None = None) -> None: ...
    def append_kernel(self, name, device, duration) -> None: ...
    def append_cpu_child(self, child) -> None:
        """Append a CPU child of type FunctionEvent.

        One is supposed to append only direct children to the event to have
        correct self cpu time being reported.
        """
    def set_cpu_parent(self, parent) -> None:
        """Set the immediate CPU parent of type FunctionEvent

        One profiling FunctionEvent should have only one CPU parent such that
        the child's range interval is completely inside the parent's. We use
        this connection to determine the event is from top-level op or not.
        """
    @property
    def self_cpu_memory_usage(self): ...
    @property
    def self_cuda_memory_usage(self): ...
    @property
    def self_cpu_time_total(self): ...
    @property
    def cuda_time_total(self): ...
    @property
    def self_cuda_time_total(self): ...
    @property
    def cpu_time_total(self): ...
    @property
    def key(self): ...

class FunctionEventAvg(FormattedTimesMixin):
    """Used to average stats over multiple FunctionEvent objects."""
    key: Incomplete
    count: int
    node_id: int
    is_async: bool
    is_remote: bool
    cpu_time_total: int
    cuda_time_total: int
    self_cpu_time_total: int
    self_cuda_time_total: int
    input_shapes: Incomplete
    stack: Incomplete
    scope: Incomplete
    cpu_memory_usage: int
    cuda_memory_usage: int
    self_cpu_memory_usage: int
    self_cuda_memory_usage: int
    cpu_children: Incomplete
    cpu_parent: Incomplete
    device_type: Incomplete
    is_legacy: bool
    flops: int
    def __init__(self) -> None: ...
    def add(self, other): ...
    def __iadd__(self, other): ...

class StringTable(defaultdict):
    def __missing__(self, key): ...

class MemRecordsAcc:
    """Acceleration structure for accessing mem_records in interval"""
    def __init__(self, mem_records) -> None: ...
    def in_interval(self, start_us, end_us) -> Generator[Incomplete, None, None]: ...

# Names in __all__ with no definition:
#   Kernel
